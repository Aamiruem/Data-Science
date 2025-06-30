# # Tiranga flag using ANSI escape sequences for color
# orange = '\033[38;5;208m'
# white = '\033[97m'
# green = '\033[92m'
# blue = '\033[94m'
# reset = '\033[0m'

# # Each color band
# print(orange + "██████████████████████████████████████" + reset)
# print(white  + "██████████████████████████████████████" + reset)
# print(green  + "██████████████████████████████████████" + reset)

# # Ashoka Chakra in the center (blue)
# print(" " * 15 + blue + "⚙" + reset)





# orange = '\033[38;5;208m'
# white = '\033[97m'
# green = '\033[92m'
# blue = '\033[94m'
# reset = '\033[0m'

# print(orange + "=" * 40 + reset)
# print(white + "=" * 40 + reset)
# print(green + "=" * 40 + reset)
# print(" " * 15 + blue + "Ashoka Chakra" + reset)







import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Lahrata Tiranga Flag 🇮🇳")
t = turtle.Turtle()
t.speed(0)

# Draw the flag pole (दंड)
def draw_pole():
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    t.color("black")
    t.width(10)
    t.goto(-200, 200)

# Draw a waving rectangle for flag band
def draw_wave_band(color, y_offset):
    t.penup()
    t.goto(-200, y_offset)
    t.color(color)
    t.begin_fill()
    for x in range(0, 360, 10):
        y = 20 * math.sin(math.radians(x)) + y_offset
        t.goto(-200 + x, y)
    for x in range(360, 0, -10):
        y = 20 * math.sin(math.radians(x)) + y_offset - 60
        t.goto(-200 + x, y)
    t.goto(-200, y_offset - 60)
    t.goto(-200, y_offset)
    t.end_fill()

# Draw Ashoka Chakra in center of white band
def draw_chakra():
    t.penup()
    t.goto(-20, 30)
    t.setheading(0)
    t.pendown()
    t.color("blue")
    t.width(2)
    t.circle(30)

    # Spokes
    for _ in range(24):
        t.penup()
        t.goto(-20, 30)
        t.setheading(_ * 15)
        t.pendown()
        t.forward(30)

# Draw everything
draw_pole()
draw_wave_band("orange", 180)
draw_wave_band("white", 120)
draw_wave_band("green", 60)
draw_chakra()

t.hideturtle()
turtle.done()
