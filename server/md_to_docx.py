"""Convert Markdown text to a DOCX file (returns a BytesIO buffer)."""

import io
import re

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH


def md_to_docx(md_text: str, title: str = '') -> io.BytesIO:
    doc = Document()

    # Basic style tweaks
    style = doc.styles['Normal']
    style.font.name = 'Marianne'
    style.font.size = Pt(11)
    style.paragraph_format.space_after = Pt(6)

    if title:
        doc.add_heading(title, level=0)

    lines = md_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]

        # Headings
        m = re.match(r'^(#{1,4})\s+(.*)', line)
        if m:
            level = len(m.group(1))
            doc.add_heading(m.group(2).strip(), level=level)
            i += 1
            continue

        # Table: detect header row starting with |
        if line.strip().startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s\-:|]+\|', lines[i + 1]):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i])
                i += 1
            _add_table(doc, table_lines)
            continue

        # Bullet list
        m = re.match(r'^[-*]\s+(.*)', line)
        if m:
            doc.add_paragraph(m.group(1).strip(), style='List Bullet')
            i += 1
            continue

        # Numbered list
        m = re.match(r'^\d+\.\s+(.*)', line)
        if m:
            doc.add_paragraph(m.group(1).strip(), style='List Number')
            i += 1
            continue

        # Blank line → skip
        if not line.strip():
            i += 1
            continue

        # Regular paragraph
        doc.add_paragraph(_clean_inline(line))
        i += 1

    buf = io.BytesIO()
    doc.save(buf)
    buf.seek(0)
    return buf


def _clean_inline(text: str) -> str:
    """Strip basic markdown inline markers (**bold**, *italic*, `code`)."""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    return text.strip()


def _add_table(doc: Document, table_lines: list[str]):
    """Parse markdown table lines and add a Word table."""
    def parse_row(line):
        cells = line.strip().strip('|').split('|')
        return [c.strip() for c in cells]

    rows = []
    for idx, line in enumerate(table_lines):
        if idx == 1 and re.match(r'^[\s\-:|]+$', line.strip().strip('|')):
            continue  # skip separator row
        rows.append(parse_row(line))

    if not rows:
        return

    n_cols = len(rows[0])
    table = doc.add_table(rows=len(rows), cols=n_cols)
    table.style = 'Table Grid'

    for r_idx, row_data in enumerate(rows):
        for c_idx, cell_text in enumerate(row_data):
            if c_idx < n_cols:
                table.rows[r_idx].cells[c_idx].text = _clean_inline(cell_text)
