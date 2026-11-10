"""
DETAILED 3D HELICOPTER INSPECTION + FLIGHT DEMO
------------------------------------------------
A procedural educational model built with Ursina.

Install:
    py -m pip install ursina

Run:
    python helicopter_3d_inspection.py

Controls:
    W/S          collective up/down (climb/descend)
    A/D          yaw left/right
    UP/DOWN      pitch forward/back
    LEFT/RIGHT   roll left/right
    SPACE        toggle engine on/off
    E            open/close engine cowling
    O            open/close cabin door
    X            toggle X-ray / cutaway view
    1            exterior camera
    2            cockpit camera
    3            engine inspection camera
    4            rotor inspection camera
    R            reset aircraft
    ESC          quit

This is a visual/educational approximation, not an engineering CAD model,
flight-training device, or representation of a specific certified aircraft.
"""

from ursina import *
from ursina.shaders import lit_with_shadows_shader
import math

app = Ursina()
window.title = "Helicopter 3D - Systems Inspection & Flight Demo"
window.borderless = False
window.fullscreen = False
window.size = (1440, 900)
window.color = color.rgb(125, 185, 220)
window.exit_button.visible = False
window.fps_counter.enabled = True

# ---------- Materials / helpers ----------
BODY = color.rgb(42, 105, 78)
BODY_LIGHT = color.rgb(68, 145, 105)
DARK = color.rgb(35, 43, 48)
METAL = color.rgb(155, 168, 174)
GLASS = color.rgba(65, 175, 220, 145)
RUBBER = color.rgb(24, 27, 29)
YELLOW = color.rgb(245, 190, 40)
COPPER = color.rgb(190, 105, 55)
RED = color.rgb(205, 55, 45)
WHITE = color.rgb(235, 240, 240)

def part(parent, name, model='cube', pos=(0,0,0), scale=(1,1,1),
         tint=WHITE, rot=(0,0,0), collider=None):
    obj = Entity(parent=parent, name=name, model=model, position=pos,
                 scale=scale, color=tint, rotation=rot,
                 shader=lit_with_shadows_shader, collider=collider)
    return obj

def rod(parent, name, a, b, radius, tint):
    mid = (Vec3(*a) + Vec3(*b)) / 2
    vec = Vec3(*b) - Vec3(*a)
    obj = Entity(parent=parent, name=name, model='cylinder',
                 position=mid, scale=(radius, vec.length, radius),
                 color=tint, shader=lit_with_shadows_shader)
    obj.look_at(Vec3(*b))
    obj.rotation_x += 90
    return obj

# ---------- Scene ----------
ground = Entity(model='plane', scale=180, texture='white_cube',
                texture_scale=(90,90), color=color.rgb(90, 125, 83),
                collider='box')
Sky()
sun = DirectionalLight()
sun.look_at(Vec3(1,-2,-1))
sun.shadows = True
AmbientLight(color=color.rgba(115, 115, 130, 0.55))
for i in range(12):
    Entity(model='cube', position=(i*13-70, 2, 38),
           scale=(7,4,7), color=color.rgb(100+i*3, 115+i*2, 130),
           collider='box')

# ---------- Helicopter assembly ----------
heli = Entity(position=(0, 3, 0), rotation=(0,0,0))
body = Entity(parent=heli)

# Main fuselage: nose points toward +Z
part(body, 'main_fuselage', 'sphere', (0,0,0), (2.25,1.05,4.5), BODY)
part(body, 'lower_keel', 'cube', (0,-0.48,0.1), (1.25,.28,3.4), DARK)
part(body, 'nose', 'sphere', (0,-.05,2.0), (1.65,.85,1.65), BODY_LIGHT)
part(body, 'nose_lower', 'sphere', (0,-.42,2.25), (1.3,.38,1.0), BODY)

# Cockpit windscreen panes (front and sides)
part(body, 'front_windscreen_left', 'sphere', (-.43,.38,2.52), (.78,.60,.12), GLASS,
     rot=(0,-13,0))
part(body, 'front_windscreen_right', 'sphere', (.43,.38,2.52), (.78,.60,.12), GLASS,
     rot=(0,13,0))
part(body, 'windscreen_center_frame', 'cube', (0,.40,2.58), (.055,.66,.10), DARK)
for side in (-1,1):
    part(body, f'pilot_side_window_{side}', 'cube',
         (side*.99,.28,1.55), (.045,.55,1.05), GLASS,
         rot=(0, side*8, 0))
    part(body, f'cabin_window_{side}', 'cube',
         (side*1.105,.22,-.15), (.035,.55,1.1), GLASS)

# Cabin door on right side: hinged visual panel
door_pivot = Entity(parent=body, position=(1.12, -.02, -.72))
door = part(door_pivot, 'sliding_cabin_door', 'cube',
            (0,.20,.0), (.055,.86,1.48), BODY_LIGHT)
part(door_pivot, 'door_window', 'cube', (.035,.30,.0),
     (.025,.38,.86), GLASS)
part(door_pivot, 'door_handle', 'cube', (.05,-.05,.55),
     (.035,.07,.16), METAL)

# Tail boom and stabilizers
part(body, 'tail_boom', 'cylinder', (0,.12,-3.05),
     (.28,3.65,.28), BODY, rot=(90,0,0))
part(body, 'horizontal_stabilizer', 'cube',
     (0,.12,-4.15), (2.0,.12,.52), BODY_LIGHT)
part(body, 'vertical_fin', 'cube',
     (0,.65,-4.45), (.16,1.25,.68), BODY)

# Tail rotor on left side of fin
tail_rotor_hub = Entity(parent=body, position=(-.18,.58,-4.48))
part(tail_rotor_hub, 'tail_rotor_hub', 'cylinder',
     (0,0,0), (.13,.22,.13), METAL, rot=(0,0,90))
tail_blades = []
for angle in (0, 90):
    blade = part(tail_rotor_hub, f'tail_blade_{angle}', 'cube',
                 (0,0,.48), (.09,.95,.12), DARK, rot=(0,0,angle))
    tail_blades.append(blade)

# Main rotor mast, transmission housing, rotor hub and blades
part(body, 'transmission_housing', 'sphere', (0,.82,-.10),
     (.78,.42,.92), METAL)
mast = part(body, 'main_rotor_mast', 'cylinder',
            (0,1.35,-.10), (.12,.92,.12), METAL)
rotor_hub = Entity(parent=body, position=(0,1.88,-.10))
part(rotor_hub, 'main_rotor_hub', 'cylinder',
     (0,0,0), (.32,.18,.32), DARK)
main_blades = []
for i in range(4):
    blade = part(rotor_hub, f'main_rotor_blade_{i+1}', 'cube',
                 (0,0,3.45), (.19,.075,3.25), DARK,
                 rot=(0, i*90, 0))
    main_blades.append(blade)
    part(rotor_hub, f'blade_tip_{i+1}', 'cube',
         (0,0,5.0), (.20,.08,.35), YELLOW,
         rot=(0, i*90, 0))

# Engine bay: visible internal engine components, located behind cabin
engine_bay = Entity(parent=body, position=(0,.52,-1.15))
part(engine_bay, 'engine_bay_frame', 'cube', (0,0,0),
     (1.55,.88,1.55), color.rgba(25,30,32,80))
# Engine core and accessory components
part(engine_bay, 'turboshaft_engine_core', 'cylinder',
     (0,.05,0), (.48,1.12,.48), COPPER, rot=(90,0,0))
part(engine_bay, 'compressor_case', 'cylinder',
     (0,.05,.48), (.38,.38,.38), METAL, rot=(90,0,0))
part(engine_bay, 'combustion_chamber', 'sphere',
     (0,.04,-.05), (.62,.55,.62), RED)
part(engine_bay, 'exhaust_pipe', 'cylinder',
     (0,.12,-.72), (.20,.75,.20), DARK, rot=(90,0,0))
part(engine_bay, 'oil_tank', 'cylinder',
     (-.55,-.10,-.15), (.18,.55,.18), YELLOW)
part(engine_bay, 'fuel_control_unit', 'cube',
     (.55,-.10,.25), (.28,.35,.32), BLUE)
part(engine_bay, 'air_intake', 'cube',
     (0,.40,.70), (1.05,.25,.28), DARK)
# Shafts / drive train shown as bright rods
rod(engine_bay, 'engine_to_gearbox_drive_shaft',
    (0,-.15,.30), (0,.65,1.20), .075, YELLOW)
part(engine_bay, 'main_gearbox', 'cube',
     (0,.78,1.18), (.90,.42,.70), METAL)
part(engine_bay, 'gearbox_inspection_cap', 'cylinder',
     (0,1.02,1.18), (.20,.08,.20), YELLOW)

# Engine cowling panels, hinged open/close
cowling_pivot = Entity(parent=body, position=(.82,.48,-1.18))
cowling = part(cowling_pivot, 'right_engine_cowling',
               'cube', (0,.20,0), (.12,.95,1.65), BODY_LIGHT)
cowling.rotation_z = 0
cowling_open = False

# Left cowling also opens to expose engine
left_cowling_pivot = Entity(parent=body, position=(-.82,.48,-1.18))
left_cowling = part(left_cowling_pivot, 'left_engine_cowling',
                    'cube', (0,.20,0), (.12,.95,1.65), BODY_LIGHT)

# Landing gear: two skids and support struts
for side in (-1,1):
    x = side*.82
    rod(body, f'landing_strut_front_{side}',
        (side*.62,-.35,1.05), (x,-1.02,1.18), .075, METAL)
    rod(body, f'landing_strut_rear_{side}',
        (side*.62,-.35,-1.55), (x,-1.02,-1.40), .075, METAL)
    rod(body, f'landing_skid_{side}',
        (x,-1.05,1.75), (x,-1.05,-2.05), .09, RUBBER)
    part(body, f'skid_front_curve_{side}', 'sphere',
         (x,-1.05,1.75), (.18,.12,.28), METAL)
    part(body, f'skid_rear_curve_{side}', 'sphere',
         (x,-1.05,-2.05), (.18,.12,.28), METAL)

# Tail navigation lights
part(body, 'tail_red_light', 'sphere', (-.14,.78,-4.72),
     (.12,.12,.12), RED)
part(body, 'tail_green_light', 'sphere', (.14,.78,-4.72),
     (.12,.12,.12), GREEN)

# Cockpit dashboard / seats, visible when cockpit camera is selected
cockpit = Entity(parent=body, position=(0,-.05,1.85))
part(cockpit, 'dashboard', 'cube', (0,.05,.15),
     (1.35,.18,.38), DARK)
for i in range(5):
    part(cockpit, f'instrument_{i}', 'cylinder',
         (-.52+i*.26,.17,.18), (.12,.035,.12),
         YELLOW if i == 0 else WHITE)
part(cockpit, 'pilot_seat', 'cube', (-.42,-.38,-.25),
     (.48,.75,.48), DARK)
part(cockpit, 'copilot_seat', 'cube', (.42,-.38,-.25),
     (.48,.75,.48), DARK)
part(cockpit, 'cyclic_control', 'cylinder',
     (-.30,-.17,.48), (.035,.42,.035), METAL)
part(cockpit, 'collective_lever', 'cylinder',
     (.48,-.16,.05), (.045,.48,.045), METAL)

# Make body parts individually translucent in X-ray mode
xray_parts = [
    body, engine_bay
]
# selected body shell objects
shell_names = {'main_fuselage','nose','nose_lower','lower_keel',
               'right_engine_cowling','left_engine_cowling'}
shell_objects = [e for e in body.children if e.name in shell_names]

# ---------- Flight state ----------
engine_on = False
xray = False
door_open = False
vertical_speed = 0.0
forward_speed = 0.0
camera_mode = 1
flight_yaw = 0.0
flight_pitch = 0.0
flight_roll = 0.0
engine_rpm = 0
rotor_spin = 0
message = "SPACE: start engine | E: engine panels | X: X-ray view"

# ---------- Cameras ----------
camera.position = (11, 8, 13)
camera.look_at(heli.position)

def set_camera(mode):
    global camera_mode, message
    camera_mode = mode
    if mode == 1:
        camera.parent = scene
        camera.position = heli.position + Vec3(10, 7, 12)
        camera.look_at(heli.position)
        message = "Exterior view"
    elif mode == 2:
        camera.parent = heli
        camera.position = (0, .15, 2.0)
        camera.rotation = (0,0,0)
        message = "Cockpit view - instruments and controls"
    elif mode == 3:
        camera.parent = scene
        camera.position = heli.position + Vec3(4, 3, -4)
        camera.look_at(heli.position + Vec3(0,.2,-1))
        message = "Engine inspection view"
    elif mode == 4:
        camera.parent = scene
        camera.position = heli.position + Vec3(0, 8, 1)
        camera.look_at(heli.position + Vec3(0,1,0))
        message = "Rotor and transmission view"

def reset_aircraft():
    global vertical_speed, forward_speed, flight_yaw
    global flight_pitch, flight_roll, engine_on, engine_rpm
    heli.position = (0,3,0)
    heli.rotation = (0,0,0)
    vertical_speed = 0
    forward_speed = 0
    flight_yaw = flight_pitch = flight_roll = 0
    engine_on = False
    engine_rpm = 0

def input(key):
    global engine_on, cowling_open, door_open, xray, message
    if key == 'escape':
        application.quit()
    elif key == 'space':
        engine_on = not engine_on
        message = "Engine started" if engine_on else "Engine shut down"
    elif key == 'e':
        cowling_open = not cowling_open
        # Rotate panels outward to expose engine bay
        cowling_pivot.rotation_z = -78 if cowling_open else 0
        left_cowling_pivot.rotation_z = 78 if cowling_open else 0
        message = "Engine cowlings open - inspect engine and gearbox" if cowling_open else "Engine cowlings closed"
    elif key == 'o':
        door_open = not door_open
        door_pivot.rotation_y = 75 if door_open else 0
        message = "Cabin door open" if door_open else "Cabin door closed"
    elif key == 'x':
        xray = not xray
        for obj in shell_objects:
            obj.color = color.rgba(42,105,78,75) if xray else BODY
        # Keep engine parts bright and visible through transparent shell
        message = "X-ray cutaway ON" if xray else "Normal exterior view"
    elif key in ('1','2','3','4'):
        set_camera(int(key))
    elif key == 'r':
        reset_aircraft()
        set_camera(1)

def update():
    global vertical_speed, forward_speed, flight_yaw
    global flight_pitch, flight_roll, engine_rpm, rotor_spin

    dt = time.dt
    if engine_on:
        engine_rpm = min(100, engine_rpm + 30*dt)
    else:
        engine_rpm = max(0, engine_rpm - 45*dt)

    rotor_spin += engine_rpm * 12 * dt
    rotor_hub.rotation_y = rotor_spin
    tail_rotor_hub.rotation_z = rotor_spin * 2.7

    # Flight is intentionally simplified for an educational interactive demo.
    if engine_on and engine_rpm > 15:
        if held_keys['w']:
            vertical_speed += 2.2 * dt
        if held_keys['s']:
            vertical_speed -= 2.2 * dt
        if held_keys['up arrow']:
            forward_speed = min(8, forward_speed + 2.0*dt)
            flight_pitch = -min(12, forward_speed*1.5)
        elif held_keys['down arrow']:
            forward_speed = max(-2, forward_speed - 2.0*dt)
            flight_pitch = 5
        else:
            forward_speed *= max(0, 1-0.35*dt)
            flight_pitch = lerp(flight_pitch, 0, 2*dt)

        if held_keys['a']:
            flight_yaw -= 55*dt
        if held_keys['d']:
            flight_yaw += 55*dt
        if held_keys['left arrow']:
            flight_roll = lerp(flight_roll, -12, 3*dt)
        elif held_keys['right arrow']:
            flight_roll = lerp(flight_roll, 12, 3*dt)
        else:
            flight_roll = lerp(flight_roll, 0, 3*dt)

        vertical_speed -= 1.4*dt  # simplified gravity / settling
    else:
        vertical_speed -= 2.8*dt
        forward_speed *= max(0, 1-0.8*dt)
        flight_pitch = lerp(flight_pitch, 0, dt*2)
        flight_roll = lerp(flight_roll, 0, dt*2)

    vertical_speed = clamp(vertical_speed, -4.5, 4.5)
    heli.y += vertical_speed * dt
    heli.y = max(1.35, min(18, heli.y))
    heli.rotation_y = flight_yaw
    heli.rotation_x = flight_pitch
    heli.rotation_z = flight_roll
    heli.position += heli.forward * forward_speed * dt

    # Follow camera in exterior / inspection modes
    if camera_mode == 1:
        camera.position = lerp(camera.position,
            heli.position + Vec3(10,7,12), dt*2)
        camera.look_at(heli.position)
    elif camera_mode == 3:
        camera.position = lerp(camera.position,
            heli.position + Vec3(4,3,-4), dt*2)
        camera.look_at(heli.position + Vec3(0,.2,-1))
    elif camera_mode == 4:
        camera.position = lerp(camera.position,
            heli.position + Vec3(0,8,1), dt*2)
        camera.look_at(heli.position + Vec3(0,1,0))

    # Slight rotor wash visual effect when running
    if engine_rpm > 50:
        heli.y += math.sin(time.time()*8)*0.001

# ---------- On-screen information ----------
panel = Entity(parent=camera.ui, model='quad', position=(-.66,.39),
               scale=(.62,.35), color=color.rgba(10,20,30,210))
hud = Text(parent=camera.ui, text='', position=(-.95,.53),
           scale=.78, color=color.white)
help_text = Text(parent=camera.ui,
    text=("W/S: climb/descend   A/D: yaw   ↑/↓: forward/back\n"
          "SPACE: engine   E: engine covers   O: cabin door   X: X-ray\n"
          "1: exterior   2: cockpit   3: engine   4: rotor   R: reset"),
    position=(-.95,-.46), scale=.72, color=color.white)
status = Text(parent=camera.ui, text=message,
              position=(-.95,.68), scale=.8, color=color.yellow)

def late_update():
    hud.text = (
        f"ENGINE: {'ON' if engine_on else 'OFF'}\n"
        f"ROTOR RPM (demo): {engine_rpm:05.1f}%\n"
        f"ALTITUDE (demo): {heli.y:04.1f}\n"
        f"FORWARD SPEED (demo): {forward_speed:04.1f}\n"
        f"ENGINE COWL: {'OPEN' if cowling_open else 'CLOSED'}\n"
        f"CABIN DOOR: {'OPEN' if door_open else 'CLOSED'}\n"
        f"CUTAWAY: {'ON' if xray else 'OFF'}"
    )
    status.text = message

set_camera(1)
app.run()
