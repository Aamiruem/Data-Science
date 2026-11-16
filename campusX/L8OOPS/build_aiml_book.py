import re
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    LongTable,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "AIML_Book.txt"
OUTPUT = ROOT / "AIML_Book.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_X = 17 * mm
MARGIN_TOP = 18 * mm
MARGIN_BOTTOM = 16 * mm
CONTENT_WIDTH = PAGE_WIDTH - MARGIN_X * 2

NAVY = colors.HexColor("#18324A")
MUTED = colors.HexColor("#617587")
PALE = colors.HexColor("#F3F6F9")
LINE = colors.HexColor("#D7E0E7")
PARTS = [
    ("HTML MASTERY", "HTML Foundations to Advanced", colors.HexColor("#168273")),
    ("CSS MASTERY", "CSS Foundations to Advanced", colors.HexColor("#3273A8")),
    ("JAVASCRIPT — COMPLETE MASTERY GUIDE", "JavaScript: Complete Mastery", colors.HexColor("#B56A24")),
    ("CHAPTER 11: OBJECT-ORIENTED PROGRAMMING", "Python OOP: Chapter 11", colors.HexColor("#7654A5")),
    ("COMPLETE MACHINE LEARNING FOR INTERVIEW", "Machine Learning: Complete Interview Guide", colors.HexColor("#287A69")),
    ("COMPLETE PYTHON: BEGINNER TO ADVANCED", "Python: Beginner to Advanced", colors.HexColor("#326DA1")),
    ("COMPLETE PYTHON: 34 TOPICS WITH DETAILED CODE", "Python: 34 Topics with Detailed Code", colors.HexColor("#8C5CA8")),
    ("COMPLETE MACHINE LEARNING INTERVIEW CHEAT SHEET", "Machine Learning Interview Cheat Sheet", colors.HexColor("#B66A2B")),
]

pdfmetrics.registerFont(TTFont("BookArial", "C:/Windows/Fonts/arial.ttf"))
pdfmetrics.registerFont(TTFont("BookArial-Bold", "C:/Windows/Fonts/arialbd.ttf"))
pdfmetrics.registerFont(TTFont("BookConsolas", "C:/Windows/Fonts/consola.ttf"))
pdfmetrics.registerFontFamily(
    "BookArial",
    normal="BookArial",
    bold="BookArial-Bold",
    italic="BookArial",
    boldItalic="BookArial-Bold",
)

STYLES = getSampleStyleSheet()
STYLES.add(ParagraphStyle(
    "CoverKicker", fontName="BookArial-Bold", fontSize=9, leading=12,
    textColor=colors.HexColor("#168273"), spaceAfter=12,
))
STYLES.add(ParagraphStyle(
    "CoverTitleAIML", fontName="BookArial-Bold", fontSize=32, leading=38,
    textColor=NAVY, spaceAfter=12,
))
STYLES.add(ParagraphStyle(
    "CoverSubtitleAIML", fontName="BookArial", fontSize=13, leading=19,
    textColor=MUTED, spaceAfter=14,
))
STYLES.add(ParagraphStyle(
    "BodyAIML", fontName="BookArial", fontSize=10.2, leading=14.3,
    textColor=NAVY, spaceAfter=3.4, allowWidows=0, allowOrphans=0,
))
STYLES.add(ParagraphStyle(
    "BodyCompactAIML", fontName="BookArial", fontSize=9.6, leading=12.4,
    textColor=NAVY, spaceAfter=0, allowWidows=0, allowOrphans=0,
))
STYLES.add(ParagraphStyle(
    "PartTitleAIML", fontName="BookArial-Bold", fontSize=21, leading=27,
    textColor=NAVY, backColor=PALE, borderColor=LINE, borderWidth=0.6,
    borderPadding=(10, 10, 10, 13), leftIndent=7, spaceAfter=11,
    keepWithNext=1,
))
STYLES.add(ParagraphStyle(
    "SectionAIML", fontName="BookArial-Bold", fontSize=13.2, leading=17.5,
    textColor=NAVY, backColor=PALE, borderColor=LINE, borderWidth=0.4,
    borderPadding=(6, 6, 6, 10), leftIndent=5, spaceBefore=9,
    spaceAfter=5, keepWithNext=1,
))
STYLES.add(ParagraphStyle(
    "SubsectionAIML", fontName="BookArial-Bold", fontSize=11.2, leading=15,
    textColor=NAVY, spaceBefore=7, spaceAfter=3, keepWithNext=1,
))
STYLES.add(ParagraphStyle(
    "LabelAIML", fontName="BookArial-Bold", fontSize=10, leading=13.5,
    textColor=NAVY, spaceBefore=5, spaceAfter=3, keepWithNext=1,
))
STYLES.add(ParagraphStyle(
    "CodeAIML", fontName="BookConsolas", fontSize=8.1, leading=10.3,
    textColor=colors.HexColor("#223A50"), leftIndent=3, rightIndent=3,
))
STYLES.add(ParagraphStyle(
    "CodeLabelAIML", fontName="BookArial-Bold", fontSize=7.8, leading=10,
    textColor=colors.white,
))
STYLES.add(ParagraphStyle(
    "TableCellAIML", fontName="BookArial", fontSize=8.8, leading=11.5,
    textColor=NAVY, spaceAfter=0,
))
STYLES.add(ParagraphStyle(
    "TableHeaderAIML", fontName="BookArial-Bold", fontSize=8.8, leading=11.5,
    textColor=colors.white, spaceAfter=0,
))
STYLES.add(ParagraphStyle(
    "TOCLevelAIML", fontName="BookArial-Bold", fontSize=11.3, leading=17,
    leftIndent=0, firstLineIndent=0, textColor=NAVY, spaceBefore=3,
))


def clean_display(text):
    cleaned = []
    for char in text:
        code = ord(char)
        if (
            0x1F000 <= code <= 0x1FAFF
            or 0x2600 <= code <= 0x27BF
            or code in (0xFE0E, 0xFE0F, 0x200D)
        ):
            continue
        cleaned.append(char)
    return "".join(cleaned)


def inline_markup(text):
    parts = re.split(r"`([^`]+)`", clean_display(text))
    converted = []
    for index, part in enumerate(parts):
        safe = escape(part)
        if index % 2:
            converted.append(
                f'<font name="BookConsolas" color="#315A70">{safe}</font>'
            )
        else:
            converted.append(safe)
    result = "".join(converted)
    result = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", result)
    return re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<link href="\2" color="#168273">\1</link>',
        result,
    )


def part_index(text):
    normalized = clean_display(text).strip().upper()
    for index, (marker, _title, _accent) in enumerate(PARTS):
        if normalized.startswith(marker):
            return index
    return None


def is_ui_footer(lines, index):
    if lines[index].strip() != "Tools":
        return False
    following = [
        line.strip()
        for line in lines[index + 1:index + 24]
        if line.strip()
    ]
    return bool(
        following
        and following[0] == "Learn & Research"
        and "Music Generator" in following
    )


def clean_source():
    lines = SOURCE.read_text(encoding="utf-8-sig").splitlines()
    first_part = next(
        (index for index, line in enumerate(lines) if part_index(line) is not None),
        None,
    )
    if first_part is None:
        raise ValueError(f"No study sections found in {SOURCE}")

    kept = []
    omitted = 0
    skipping_prompt = False
    in_footer = False

    for index in range(first_part, len(lines)):
        raw = lines[index]
        text = raw.strip()

        if in_footer:
            omitted += 1
            if text == "Music Generator":
                in_footer = False
            continue
        if is_ui_footer(lines, index):
            in_footer = True
            omitted += 1
            continue
        if text.startswith("Loading older messages"):
            omitted += 1
            continue

        is_part = part_index(raw) is not None
        is_oop_body = "Chapter 11 — Object-Oriented Programming (OOP) in Python" in clean_display(raw)
        if skipping_prompt:
            if is_part or is_oop_body:
                skipping_prompt = False
            else:
                omitted += 1
                continue

        if "<Topicwise>" in raw:
            prefix = raw.split("Explain the chapter <Topicwise> in detail.", 1)[0].strip()
            if prefix:
                kept.append(prefix)
            omitted += 1
            skipping_prompt = True
            continue

        lowered = text.lower()
        if lowered.startswith((
            "all css complete code",
            "all javascript complete code",
            "complete ml for interview all concept",
            "complete python explain every concept and code",
            "complete and all ml cheat sheet for interview",
        )):
            omitted += 1
            if lowered.startswith(("all css ", "all javascript ")):
                skipping_prompt = True
            continue

        if "only all topic long code to clera concept" in lowered:
            raw = re.split(
                r"\s+only all topic long code to clera concept",
                raw,
                flags=re.IGNORECASE,
            )[0]
            text = raw.strip()

        if text == "…" or not text:
            if not text:
                kept.append("")
            else:
                omitted += 1
            continue
        kept.append(raw)

    return kept, omitted, len(lines)


def is_diagram_line(line):
    return any(char in line for char in "┌┐└┘├┤┬┴┼─│▼▲↓↑→←")


CODE_START = re.compile(
    r"^(?:"
    r"<[/!?A-Za-z]|"
    r"(?:const|let|var|function|class|async|await|return|if|else|elif|for|while|def|from|import|try|except|raise|with|yield|pass)\b|"
    r"(?:print|console\.|document\.|alert|self\.)|"
    r"//|/\*|"
    r"[A-Za-z_$][\w.$]*\s*(?:\(|=)|"
    r"[.#][A-Za-z_][\w-]*\s*\{|"
    r"(?:color|background|display|margin|padding|border|width|height|font(?:-size|-family|-weight)?|position|top|left|right|bottom|gap|grid-template-columns|justify-content|align-items)\s*:\s*[^:]+;?$"
    r")"
)


def is_code_line(line):
    if not line.strip():
        return False
    if is_diagram_line(line):
        return True
    if len(line) - len(line.lstrip()) >= 4:
        return True
    return bool(CODE_START.match(line.strip()))


def is_bullet(line):
    stripped = line.strip()
    return bool(re.match(r"^(?:[-*•▪◦]|□|☐|✓|✔|✅|☑)\s*", stripped))


def numbered_item(line):
    return re.match(r"^\s*(\d+)\.\s+(.+)$", clean_display(line))


def is_numbered_list(lines, index, match):
    expected = int(match.group(1)) + 1
    cursor = index + 1
    while cursor < len(lines) and not lines[cursor].strip() and cursor <= index + 3:
        cursor += 1
    if cursor >= len(lines):
        return False
    following = numbered_item(lines[cursor])
    return bool(following and int(following.group(1)) == expected)


def heading_level(line, lines, index):
    text = clean_display(line).strip()
    if text.startswith("#"):
        level = min(len(text) - len(text.lstrip("#")), 2)
        return level, text.lstrip("# ").strip()
    match = re.match(r"^(\d+(?:\.\d+)*)(?:\.)?\s+(.+)$", text)
    if not match:
        return None
    if "." in match.group(1):
        return 2, text
    if is_numbered_list(lines, index, match):
        return None
    return 1, text


NOTE_LABELS = (
    "master formula", "goal", "important", "simple definition", "easy meaning",
    "real-world example", "example", "dry run", "common mistake", "common mistakes",
    "remember", "best practice", "interview answer", "a common interview answer",
    "key idea", "important note", "important formula", "formula",
)


def is_note_label(line):
    text = clean_display(line).strip().rstrip(":").lower()
    return any(text == label or text.startswith(label + ":") for label in NOTE_LABELS)


def make_part_heading(text, index):
    title = clean_display(text).strip()
    display_title = f"PART {index + 1}  |  {title}"
    accent = PARTS[index][2]
    style = ParagraphStyle(
        f"PartTitle{index}",
        parent=STYLES["PartTitleAIML"],
        textColor=accent,
        borderColor=accent,
        backColor=colors.HexColor("#F5F7FA"),
    )
    return OutlineParagraph(
        escape(display_title),
        style,
        f"part-{index + 1}",
        display_title,
        0,
        toc=True,
    )


class OutlineParagraph(Paragraph):
    def __init__(self, text, style, key, title, level, toc=False):
        super().__init__(text, style)
        self.outline_key = key
        self.outline_title = title
        self.outline_level = level
        self.toc_entry = toc


class BookDocument(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(
            str(filename),
            pagesize=A4,
            leftMargin=MARGIN_X,
            rightMargin=MARGIN_X,
            topMargin=MARGIN_TOP,
            bottomMargin=MARGIN_BOTTOM,
            title="AIML Book | Complete Study Guide",
            author="AIML Study Notes",
            subject="HTML, CSS, JavaScript, Python OOP, Python, and Machine Learning",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="content",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates([
            PageTemplate(id="book", frames=[frame], onPage=self.draw_page)
        ])

    def draw_page(self, canvas, document):
        canvas.saveState()
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(MARGIN_X, 12 * mm, PAGE_WIDTH - MARGIN_X, 12 * mm)
        canvas.setFont("BookArial", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(MARGIN_X, 8 * mm, "AIML BOOK  |  Foundations to Advanced")
        canvas.drawRightString(PAGE_WIDTH - MARGIN_X, 8 * mm, f"Page {document.page}")
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if not isinstance(flowable, OutlineParagraph):
            return
        self.canv.bookmarkPage(flowable.outline_key)
        self.canv.addOutlineEntry(
            flowable.outline_title,
            flowable.outline_key,
            flowable.outline_level,
            closed=False,
        )
        if flowable.toc_entry:
            self.notify(
                "TOCEntry",
                (flowable.outline_level, flowable.outline_title, self.page, flowable.outline_key),
            )


def code_panel(lines, accent, label, diagram=False):
    code = "\n".join(clean_display(line).rstrip() for line in lines)
    preformatted = Preformatted(
        code,
        STYLES["CodeAIML"],
        maxLineLength=100,
    )
    table = Table(
        [[Paragraph(escape(label), STYLES["CodeLabelAIML"])], [preformatted]],
        colWidths=[CONTENT_WIDTH],
        hAlign="LEFT",
        splitByRow=1,
        spaceBefore=3,
        spaceAfter=6,
    )
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), accent),
        ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F3F6FA") if not diagram else colors.HexColor("#F5F7FA")),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, 0), 4),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 4),
        ("TOPPADDING", (0, 1), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
    ]))
    return table


def make_table(rows, accent):
    column_count = max(len(row) for row in rows)
    table_data = []
    for row_index, row in enumerate(rows):
        normalized = row + [""] * (column_count - len(row))
        style = STYLES["TableHeaderAIML"] if row_index == 0 else STYLES["TableCellAIML"]
        table_data.append([
            Paragraph(inline_markup(cell.strip()), style)
            for cell in normalized
        ])
    widths = [CONTENT_WIDTH / column_count] * column_count
    table = LongTable(
        table_data,
        colWidths=widths,
        repeatRows=1,
        hAlign="LEFT",
        splitByRow=1,
        spaceBefore=3,
        spaceAfter=7,
    )
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), accent),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE]),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def note_panel(text, accent):
    body = Paragraph(inline_markup(text), STYLES["BodyAIML"])
    panel = Table([[body]], colWidths=[CONTENT_WIDTH], hAlign="LEFT", spaceBefore=2, spaceAfter=5)
    panel.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F5F7FA")),
        ("LINEBEFORE", (0, 0), (0, -1), 3, accent),
        ("BOX", (0, 0), (-1, -1), 0.35, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return panel


def add_cover(story):
    story.extend([
        Spacer(1, 34 * mm),
        Paragraph("COLOR-CODED STUDY BOOK  |  BASICS TO ADVANCED", STYLES["CoverKicker"]),
        Paragraph("AIML BOOK", STYLES["CoverTitleAIML"]),
        Paragraph(
            "Complete notes for HTML, CSS, JavaScript, Python OOP, Python, and Machine Learning",
            STYLES["CoverSubtitleAIML"],
        ),
    ])
    card_rows = [
        ["01  HTML", "02  CSS"],
        ["03  JavaScript", "04  Python OOP"],
        ["05  Machine Learning", "06  Python: Beginner to Advanced"],
        ["07  Python: 34 Topics with Code", "08  ML Interview Cheat Sheet"],
    ]
    cards = []
    card_colors = [
        colors.HexColor("#E8F4F1"), colors.HexColor("#EAF1F8"),
        colors.HexColor("#FBF1E5"), colors.HexColor("#F0EAF7"),
        colors.HexColor("#E8F4F1"), colors.HexColor("#EAF1F8"),
        colors.HexColor("#F0EAF7"), colors.HexColor("#FBF1E5"),
    ]
    for row in card_rows:
        cards.append([
            Paragraph(escape(text), ParagraphStyle(
                "CoverCard",
                parent=STYLES["BodyAIML"],
                fontName="BookArial-Bold",
                fontSize=9.5,
                leading=13,
                spaceAfter=0,
            ))
            for text in row
        ])
    card_table = Table(cards, colWidths=[CONTENT_WIDTH / 2] * 2, hAlign="LEFT")
    commands = [
        ("GRID", (0, 0), (-1, -1), 0.5, colors.white),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]
    for i, fill in enumerate(card_colors):
        row, col = divmod(i, 2)
        commands.append(("BACKGROUND", (col, row), (col, row), fill))
    card_table.setStyle(TableStyle(commands))
    story.extend([
        card_table,
        Spacer(1, 10 * mm),
        Paragraph(
            "Built from the supplied notes: examples, code, dry runs, formulas, "
            "mind maps, interview guidance, and revision tables are retained.",
            STYLES["BodyAIML"],
        ),
        PageBreak(),
        Paragraph("Contents", STYLES["CoverTitleAIML"]),
    ])
    toc = TableOfContents()
    toc.levelStyles = [STYLES["TOCLevelAIML"]]
    toc.dotsMinLevel = 0
    story.extend([toc, PageBreak()])


def render_content(lines):
    story = []
    current_part = 0
    part_seen = False
    counter = 0
    index = 0

    while index < len(lines):
        raw = lines[index]
        text = raw.strip()
        if not text:
            index += 1
            continue

        new_part = part_index(raw)
        if new_part is not None:
            current_part = new_part
            if part_seen:
                story.append(PageBreak())
            story.append(make_part_heading(raw, new_part))
            part_seen = True
            index += 1
            continue

        accent = PARTS[current_part][2]

        if "\t" in raw:
            rows = []
            while index < len(lines) and "\t" in lines[index]:
                rows.append(lines[index].split("\t"))
                index += 1
            for start in range(0, len(rows), 36):
                story.append(make_table(rows[start:start + 36], accent))
            continue

        if is_diagram_line(raw) or is_code_line(raw):
            block = []
            diagram = is_diagram_line(raw)
            cursor = index
            while cursor < len(lines):
                candidate = lines[cursor]
                if not candidate.strip():
                    if cursor + 1 < len(lines) and is_code_line(lines[cursor + 1]):
                        block.append("")
                        cursor += 1
                        continue
                    break
                if not is_code_line(candidate):
                    break
                block.append(candidate)
                diagram = diagram or is_diagram_line(candidate)
                cursor += 1
            label = "CONCEPT MAP" if diagram else PARTS[current_part][1].upper()
            for start in range(0, len(block), 34):
                story.append(code_panel(block[start:start + 34], accent, label, diagram))
            index = cursor
            continue

        number_match = numbered_item(raw)
        if is_bullet(raw) or (number_match and is_numbered_list(lines, index, number_match)):
            cleaned = clean_display(text)
            if number_match:
                cleaned = re.sub(r"^\d+\.\s*", "", cleaned)
                bullet = f"{number_match.group(1)}."
            else:
                checked = text.startswith(("□", "☐", "✓", "✔", "✅", "☑"))
                cleaned = re.sub(r"^(?:[-*•▪◦]|□|☐|✓|✔|✅|☑)\s*", "", cleaned)
                bullet = "[ ]" if checked else "•"
            style = ParagraphStyle(
                "ListAIMLDynamic",
                parent=STYLES["BodyAIML"],
                leftIndent=15,
                firstLineIndent=-12,
                spaceAfter=2,
            )
            story.append(Paragraph(inline_markup(cleaned), style, bulletText=bullet))
            index += 1
            continue

        heading = heading_level(raw, lines, index)
        if heading:
            level, title = heading
            counter += 1
            style = STYLES["SectionAIML"] if level == 1 else STYLES["SubsectionAIML"]
            story.append(OutlineParagraph(
                inline_markup(title),
                style,
                f"section-{counter}",
                clean_display(title),
                1,
            ))
            index += 1
            continue

        if is_note_label(raw):
            story.append(note_panel(text, accent))
        else:
            story.append(Paragraph(inline_markup(text), STYLES["BodyAIML"]))
        index += 1

    return story


def build():
    lines, omitted, total = clean_source()
    story = []
    add_cover(story)
    story.extend(render_content(lines))
    document = BookDocument(OUTPUT)
    document.multiBuild(story, maxPasses=4)
    nonempty = sum(bool(line.strip()) for line in lines)
    print(
        f"Created {OUTPUT.name}: {OUTPUT.stat().st_size:,} bytes; "
        f"{document.page} pages; retained {nonempty:,} study lines; "
        f"omitted {omitted:,} prompt/UI lines from {total:,} source lines."
    )


if __name__ == "__main__":
    build()
