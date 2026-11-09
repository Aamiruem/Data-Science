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
    Flowable,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Python Mastery Course.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 15 * mm
CONTENT_WIDTH = PAGE_WIDTH - MARGIN * 2
NAVY = colors.HexColor("#17324D")
TEAL = colors.HexColor("#137C78")
MUTED = colors.HexColor("#5F7180")
PALE = colors.HexColor("#F1F6F7")
LINE = colors.HexColor("#D9E3E7")

pdfmetrics.registerFont(TTFont("Arial", "C:/Windows/Fonts/arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "C:/Windows/Fonts/arialbd.ttf"))
pdfmetrics.registerFontFamily(
    "Arial", normal="Arial", bold="Arial-Bold",
    italic="Arial", boldItalic="Arial-Bold",
)

STYLES = getSampleStyleSheet()
STYLES.add(ParagraphStyle(
    "Kicker", fontName="Arial-Bold", fontSize=8.5, leading=11,
    textColor=TEAL, spaceAfter=8,
))
STYLES.add(ParagraphStyle(
    "CoverTitle", fontName="Arial-Bold", fontSize=30, leading=36,
    textColor=NAVY, spaceAfter=10,
))
STYLES.add(ParagraphStyle(
    "CoverBody", fontName="Arial", fontSize=11.5, leading=17,
    textColor=colors.HexColor("#405767"), spaceAfter=8,
))
STYLES.add(ParagraphStyle(
    "BodyTextCourse", fontName="Arial", fontSize=10.4, leading=15,
    textColor=NAVY, spaceAfter=6, allowWidows=0, allowOrphans=0,
))
STYLES.add(ParagraphStyle(
    "ChapterHeading", fontName="Arial-Bold", fontSize=22, leading=28,
    textColor=NAVY, backColor=PALE, borderColor=LINE, borderWidth=0.5,
    borderPadding=(10, 9, 10, 13), leftIndent=8, spaceBefore=8,
    spaceAfter=14, keepWithNext=1,
))
STYLES.add(ParagraphStyle(
    "SectionHeading", fontName="Arial-Bold", fontSize=15, leading=20,
    textColor=NAVY, backColor=PALE, borderColor=LINE, borderWidth=0.4,
    borderPadding=(7, 7, 7, 11), leftIndent=7, spaceBefore=13,
    spaceAfter=8, keepWithNext=1,
))
STYLES.add(ParagraphStyle(
    "Subheading", fontName="Arial-Bold", fontSize=12, leading=16,
    textColor=TEAL, spaceBefore=8, spaceAfter=5, keepWithNext=1,
))
STYLES.add(ParagraphStyle(
    "ListText", fontName="Arial", fontSize=10, leading=14,
    textColor=NAVY, spaceAfter=3,
))
STYLES.add(ParagraphStyle(
    "TableCellCourse", fontName="Arial", fontSize=9.2, leading=12.4,
    textColor=NAVY, spaceAfter=0,
))
STYLES.add(ParagraphStyle(
    "TableHeaderCourse", fontName="Arial-Bold", fontSize=9.2,
    leading=12.4, textColor=colors.white, spaceAfter=0,
))
STYLES.add(ParagraphStyle(
    "CodeBlock", fontName="Courier", fontSize=9, leading=12.5,
    textColor=colors.HexColor("#17324D"), backColor=colors.HexColor("#F3F6FB"),
    borderColor=LINE, borderWidth=0.5, borderPadding=8, leftIndent=5,
    rightIndent=5, spaceBefore=3, spaceAfter=7,
))
STYLES.add(ParagraphStyle(
    "SmallMutedCourse", fontName="Arial", fontSize=9, leading=12,
    textColor=MUTED, spaceAfter=5,
))
STYLES.add(ParagraphStyle(
    "DiagramLabel", fontName="Arial-Bold", fontSize=8.3, leading=10,
    textColor=NAVY, alignment=1, spaceAfter=2,
))
STYLES.add(ParagraphStyle(
    "DiagramDetail", fontName="Arial", fontSize=7.4, leading=9.2,
    textColor=colors.HexColor("#405767"), alignment=1,
))
STYLES.add(ParagraphStyle(
    "CodePanelLabel", fontName="Arial-Bold", fontSize=8.2, leading=10,
    textColor=colors.white,
))


def inline_markup(text):
    parts = re.split(r"`([^`]+)`", text)
    converted = []
    for index, part in enumerate(parts):
        safe = escape(part)
        if index % 2:
            converted.append(
                f'<font name="Courier" color="#315A70">{safe}</font>'
            )
        else:
            converted.append(safe)
    result = "".join(converted)
    result = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", result)
    return re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<link href="\2" color="#137C78">\1</link>',
        result,
    )


class OutlineParagraph(Paragraph):
    def __init__(self, text, style, key, title, level):
        super().__init__(text, style)
        self.outline_key = key
        self.outline_title = title
        self.outline_level = level


class MarkdownListItem(Flowable):
    def __init__(self, text, checkbox=False, checked=False):
        super().__init__()
        self.paragraph = Paragraph(inline_markup(text), STYLES["ListText"])
        self.checkbox = checkbox
        self.checked = checked
        self.text_height = 0

    def wrap(self, available_width, available_height):
        self.width = available_width
        _, self.text_height = self.paragraph.wrap(
            max(1, available_width - 17), available_height
        )
        self.height = self.text_height + 2
        return self.width, self.height

    def draw(self):
        canvas = self.canv
        if self.checkbox:
            canvas.setStrokeColor(colors.HexColor("#7A929F"))
            canvas.setLineWidth(0.7)
            canvas.rect(1, self.height - 9, 7, 7, stroke=1, fill=0)
            if self.checked:
                canvas.setStrokeColor(TEAL)
                canvas.setLineWidth(1)
                canvas.line(2, self.height - 5, 4, self.height - 7)
                canvas.line(4, self.height - 7, 7, self.height - 3)
        else:
            canvas.setFillColor(TEAL)
            canvas.circle(5, self.height - 6, 1.5, stroke=0, fill=1)
        self.paragraph.drawOn(
            canvas, 14, self.height - self.text_height
        )


DIAGRAMS = {
    "applications": (
        "WHERE PYTHON IS USED",
        [
            ("Automation", "Repeatable file and task workflows"),
            ("Data science", "Explore, clean, and explain data"),
            ("Web and APIs", "Build services that communicate"),
            ("AI and machine learning", "Train and use predictive models"),
            ("Testing", "Check software behavior automatically"),
            ("Research", "Express experiments and calculations"),
        ],
    ),
    "execution_pipeline": (
        "HOW A PYTHON SCRIPT RUNS",
        [
            ("Source file", "Readable instructions in a .py file"),
            ("Parser and compiler", "Check syntax and create bytecode"),
            ("Bytecode", "Lower-level Python instructions"),
            ("CPython VM", "Execute bytecode step by step"),
            ("Result", "Output or a useful traceback"),
        ],
    ),
    "repl": (
        "THE INTERACTIVE REPL CYCLE",
        [
            ("Read", "Receive a statement"),
            ("Evaluate", "Run the statement"),
            ("Print", "Show the result"),
            ("Loop", "Wait for more input"),
        ],
    ),
    "tools": (
        "A SIMPLE PYTHON WORKFLOW",
        [
            ("Editor or IDE", "Write and save a .py file"),
            ("Python interpreter", "Run the saved instructions"),
            ("Terminal or notebook", "See output and inspect errors"),
        ],
    ),
    "add_numbers": (
        "FROM INPUT TO ANSWER",
        [
            ("Input", "Text: 12 and 8"),
            ("Convert", "Integers: 12 and 8"),
            ("Calculate", "12 + 8 = 20"),
            ("Output", "Display: Sum: 20"),
        ],
    ),
    "variable_reference": (
        "A NAME REFERS TO AN OBJECT",
        [
            ("Name", "The label used in your code: score"),
            ("Reference", "The name refers to a value object"),
            ("Object", "The integer value: 85"),
        ],
    ),
    "scope_lookup": (
        "WHERE PYTHON LOOKS FOR A NAME",
        [
            ("Local", "Inside the current function"),
            ("Enclosing", "Inside a surrounding function"),
            ("Global", "At the module level"),
            ("Built-ins", "Names such as print and len"),
        ],
    ),
    "built_in_types": (
        "PYTHON'S EVERYDAY BUILT-IN TYPES",
        [
            ("Numbers", "int, float, complex"),
            ("Text", "str"),
            ("Sequences", "list, tuple, range"),
            ("Mappings", "dict"),
            ("Sets", "set, frozenset"),
            ("Other", "bool, bytes, None"),
        ],
    ),
    "mutability": (
        "MUTABLE AND IMMUTABLE VALUES",
        [
            ("Immutable value", "A change creates or refers to another value"),
            ("Mutable object", "The same object can be changed"),
            ("Shared reference", "Two names can refer to one object"),
        ],
    ),
}


class ConceptDiagram(Flowable):
    def __init__(self, diagram_name):
        super().__init__()
        try:
            self.title, self.cards = DIAGRAMS[diagram_name]
        except KeyError as error:
            raise ValueError(f"Unknown course diagram: {diagram_name}") from error
        self.diagram_name = diagram_name

    def wrap(self, available_width, available_height):
        self.width = available_width
        self.height = 144 if self.diagram_name == "applications" else 104
        return self.width, self.height

    def _draw_card(self, canvas, x, y, width, height, index, title, detail):
        fill = colors.HexColor(("#EAF3F9", "#EAF5EE", "#FFF3E5", "#E7F5F3")[index % 4])
        accent = colors.HexColor(("#286D9C", "#237A57", "#B66A24", "#167C79")[index % 4])
        canvas.setFillColor(fill)
        canvas.setStrokeColor(accent)
        canvas.setLineWidth(0.8)
        canvas.roundRect(x, y, width, height, 5, stroke=1, fill=1)

        title_paragraph = Paragraph(
            escape(title), STYLES["DiagramLabel"]
        )
        _, title_height = title_paragraph.wrap(width - 10, 22)
        title_paragraph.drawOn(
            canvas, x + 5, y + height - title_height - 6
        )
        detail_paragraph = Paragraph(
            escape(detail), STYLES["DiagramDetail"]
        )
        _, detail_height = detail_paragraph.wrap(width - 10, height - 23)
        detail_paragraph.drawOn(
            canvas, x + 5, y + 5 + max(0, (height - 20 - detail_height) / 2)
        )

    def _draw_arrow(self, canvas, x1, x2, y):
        canvas.setStrokeColor(TEAL)
        canvas.setFillColor(TEAL)
        canvas.setLineWidth(1.2)
        canvas.line(x1, y, x2 - 4, y)
        canvas.line(x2 - 4, y, x2 - 8, y + 3)
        canvas.line(x2 - 4, y, x2 - 8, y - 3)

    def draw(self):
        canvas = self.canv
        canvas.saveState()
        canvas.setFont("Arial-Bold", 9)
        canvas.setFillColor(NAVY)
        canvas.drawString(0, self.height - 11, self.title)

        if self.diagram_name in {"applications", "built_in_types"}:
            gap_x, gap_y = 9, 8
            card_width = (self.width - 2 * gap_x) / 3
            card_height = 51
            top_y = self.height - 19 - card_height
            for index, (title, detail) in enumerate(self.cards):
                row, column = divmod(index, 3)
                y = top_y - row * (card_height + gap_y)
                x = column * (card_width + gap_x)
                self._draw_card(
                    canvas, x, y, card_width, card_height,
                    index, title, detail,
                )
        else:
            count = len(self.cards)
            gap = 17 if count == 5 else 19
            card_width = min(105, (self.width - gap * (count - 1)) / count)
            card_height = 70
            total_width = count * card_width + (count - 1) * gap
            start_x = max(0, (self.width - total_width) / 2)
            y = 12
            for index, (title, detail) in enumerate(self.cards):
                x = start_x + index * (card_width + gap)
                self._draw_card(
                    canvas, x, y, card_width, card_height,
                    index, title, detail,
                )
                if index + 1 < count:
                    self._draw_arrow(
                        canvas, x + card_width + 2,
                        x + card_width + gap - 2, y + card_height / 2,
                    )

        canvas.restoreState()


class CourseDocument(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, OutlineParagraph):
            self.canv.bookmarkPage(flowable.outline_key)
            self.canv.addOutlineEntry(
                flowable.outline_title,
                flowable.outline_key,
                level=flowable.outline_level,
                closed=False,
            )


def page_chrome(canvas, document):
    canvas.saveState()
    if document.page > 1:
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(
            MARGIN, PAGE_HEIGHT - 10 * mm,
            PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 10 * mm,
        )
        canvas.setFont("Arial-Bold", 7.2)
        canvas.setFillColor(MUTED)
        canvas.drawString(
            MARGIN, PAGE_HEIGHT - 8 * mm, "PYTHON MASTERY COURSE"
        )
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, 10 * mm, PAGE_WIDTH - MARGIN, 10 * mm)
    canvas.setFont("Arial", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN, 6.5 * mm, "Chapter-by-chapter learning guide")
    canvas.drawRightString(
        PAGE_WIDTH - MARGIN, 6.5 * mm, f"Page {document.page}"
    )
    canvas.restoreState()


def parse_table_row(line):
    cells = line.strip().strip("|").split("|")
    return [cell.strip().replace(r"\|", "|") for cell in cells]


def make_markdown_table(lines):
    rows = [parse_table_row(line) for line in lines]
    if len(rows) > 1 and all(
        re.fullmatch(r":?-{3,}:?", cell.replace(" ", ""))
        for cell in rows[1]
    ):
        rows.pop(1)
    column_count = max(map(len, rows))
    rows = [row + [""] * (column_count - len(row)) for row in rows]
    if column_count == 2:
        widths = [CONTENT_WIDTH * 0.37, CONTENT_WIDTH * 0.63]
    else:
        widths = [CONTENT_WIDTH / column_count] * column_count
    data = []
    for row_index, row in enumerate(rows):
        style = "TableHeaderCourse" if row_index == 0 else "TableCellCourse"
        data.append([
            Paragraph(inline_markup(cell), STYLES[style]) for cell in row
        ])
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, TEAL),
        ("LINEBELOW", (0, 1), (-1, -1), 0.35, LINE),
    ]
    for row_index in range(1, len(data)):
        if row_index % 2 == 0:
            commands.append((
                "BACKGROUND", (0, row_index), (-1, row_index),
                colors.HexColor("#F5F8F9"),
            ))
    table.setStyle(TableStyle(commands))
    table.spaceBefore = 3
    table.spaceAfter = 8
    return table


def make_code_panel(lines, language):
    labels = {
        "python": "PYTHON EXAMPLE",
        "py": "PYTHON EXAMPLE",
        "text": "SAMPLE OUTPUT",
        "powershell": "TERMINAL COMMAND",
    }
    label_text = labels.get(
        language, f"{language.upper()} CODE" if language else "CODE EXAMPLE"
    )
    code = Preformatted(
        "\n".join(lines), STYLES["CodeBlock"], maxLineLength=76,
    )
    label = Paragraph(label_text, STYLES["CodePanelLabel"])
    panel = Table(
        [[label], [code]], colWidths=[CONTENT_WIDTH], hAlign="LEFT"
    )
    panel.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TEAL),
        ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F3F6FB")),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("LINEBEFORE", (0, 0), (0, -1), 3, TEAL),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    panel.spaceBefore = 3
    panel.spaceAfter = 8
    return panel


def parse_chapter(path, chapter_index):
    lines = path.read_text(encoding="utf-8").splitlines()
    story = []
    code = []
    code_language = ""
    in_code = False
    heading_index = 0
    index = 0

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if stripped.startswith("```"):
            if in_code:
                story.append(make_code_panel(code, code_language))
                code = []
                code_language = ""
                in_code = False
            else:
                in_code = True
                code_language = stripped[3:].strip().split(" ", 1)[0].lower()
            index += 1
            continue
        if in_code:
            code.append(line.rstrip())
            index += 1
            continue
        if not stripped or stripped == "---":
            index += 1
            continue
        diagram = re.fullmatch(r"\[\[diagram:([a-z_]+)\]\]", stripped)
        if diagram:
            story.append(ConceptDiagram(diagram.group(1)))
            index += 1
            continue
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            heading_index += 1
            story.append(OutlineParagraph(
                inline_markup(title), STYLES["ChapterHeading"],
                f"ch{chapter_index}-heading{heading_index}",
                title, 0,
            ))
            index += 1
            continue
        if stripped.startswith("## "):
            title = stripped[3:].strip()
            heading_index += 1
            story.append(OutlineParagraph(
                inline_markup(title), STYLES["SectionHeading"],
                f"ch{chapter_index}-heading{heading_index}",
                title, 1,
            ))
            index += 1
            continue
        if stripped.startswith("### "):
            story.append(Paragraph(
                inline_markup(stripped[4:].strip()), STYLES["Subheading"]
            ))
            index += 1
            continue
        if stripped.startswith("|") and "|" in stripped[1:]:
            table_lines = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index].strip())
                index += 1
            story.append(make_markdown_table(table_lines))
            continue
        if stripped.startswith("- [ ] ") or stripped.startswith("- [x] "):
            item = stripped[6:]
            story.append(MarkdownListItem(
                item, checkbox=True, checked=stripped.startswith("- [x] ")
            ))
            index += 1
            continue
        if stripped.startswith("- "):
            story.append(MarkdownListItem(stripped[2:].strip()))
            index += 1
            continue
        numbered = re.match(r"^(\d+)\.\s+(.+)$", stripped)
        if numbered:
            story.append(Paragraph(
                f'<font name="Arial-Bold" color="#137C78">'
                f'{numbered.group(1)}.</font> '
                f'{inline_markup(numbered.group(2))}',
                ParagraphStyle(
                    "NumberedCourse", parent=STYLES["ListText"],
                    leftIndent=16, firstLineIndent=-16,
                ),
            ))
            index += 1
            continue
        if stripped.startswith("> "):
            story.append(Paragraph(
                inline_markup(stripped[2:]),
                ParagraphStyle(
                    "QuoteCourse", parent=STYLES["BodyTextCourse"],
                    leftIndent=10, borderColor=TEAL, borderWidth=0.5,
                    borderPadding=6, backColor=colors.HexColor("#EEF6F5"),
                ),
            ))
            index += 1
            continue

        paragraph_lines = [stripped]
        index += 1
        while index < len(lines):
            following = lines[index].strip()
            if (
                not following
                or following.startswith(("#", "```", "|", "- ", "> "))
                or re.match(r"^\d+\.\s+", following)
            ):
                break
            paragraph_lines.append(following)
            index += 1
        story.append(Paragraph(
            inline_markup(" ".join(paragraph_lines)),
            STYLES["BodyTextCourse"],
        ))

    if in_code:
        raise ValueError(f"Unclosed code fence in {path.name}")
    return story


def main():
    chapters = sorted(ROOT.glob("Chapter *.md"))
    if not chapters:
        raise FileNotFoundError(f"No chapter files found in {ROOT}")

    story = [
        Spacer(1, 18 * mm),
        Paragraph("PYTHON MASTERY COURSE", STYLES["Kicker"]),
        Paragraph("Concepts, Code, and Practice", STYLES["CoverTitle"]),
        Paragraph(
            "A plain-language, chapter-by-chapter guide from Python basics "
            "to AI/ML engineering.",
            STYLES["CoverBody"],
        ),
        Spacer(1, 5 * mm),
        Paragraph(
            f"<b>Course progress:</b> {len(chapters)} of 37 chapters authored. "
            "This PDF contains the chapters currently available; it will grow "
            "as the remaining chapter files are added.",
            STYLES["CoverBody"],
        ),
        Spacer(1, 5 * mm),
        Paragraph("AVAILABLE CHAPTERS", STYLES["Subheading"]),
    ]
    for chapter in chapters:
        title = next(
            (
                line[2:].strip()
                for line in chapter.read_text(encoding="utf-8").splitlines()
                if line.startswith("# ")
            ),
            chapter.stem,
        )
        story.append(Paragraph(
            f'<font color="#137C78">-</font> {inline_markup(title)}',
            STYLES["ListText"],
        ))

    for index, chapter in enumerate(chapters, start=1):
        story.append(PageBreak())
        story.extend(parse_chapter(chapter, index))

    document = CourseDocument(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=MARGIN,
        leftMargin=MARGIN,
        topMargin=17 * mm,
        bottomMargin=16 * mm,
        title="Python Mastery Course",
    )
    document.build(story, onFirstPage=page_chrome, onLaterPages=page_chrome)
    print(f"Built {OUTPUT} from {len(chapters)} chapter file(s).")


if __name__ == "__main__":
    main()
