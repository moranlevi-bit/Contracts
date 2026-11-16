#!/usr/bin/env python3
"""Build a Contract.ly-branded PowerPoint deck from a JSON spec.

Usage:  python3 tools/make_presentation.py spec.json out.pptx

Spec (all slide fields optional except "type"):
{
  "title": "Contracts status", "subtitle": "Prepared for management", "date": "November 16, 2026",
  "slides": [
    {"type": "kpis", "title": "At a glance", "items": [{"label": "Net balance, 12 months", "value": "+$1.1M", "note": "money in minus money out", "tone": "good|bad|neutral"}]},
    {"type": "bullets", "title": "Key points", "bullets": ["...", "..."]},
    {"type": "table", "title": "Overdue items", "columns": ["Due", "Counterparty", "Item", "Amount"], "rows": [["Nov 1", "Acme", "Invoice", "$4,170"]]},
    {"type": "chart", "title": "Money by month", "chart": "column|bar|line|pie", "categories": ["Nov", "Dec"],
     "series": [{"name": "Money in", "values": [1, 2]}, {"name": "Money out", "values": [3, 4]}], "number_format": "$#,##0"},
    {"type": "timeline", "title": "Key dates", "items": [{"date": "Dec 1, 2026", "label": "Notice deadline: Lakeshore"}]}
  ],
  "sources": "Figures from Contract.ly on November 16, 2026. Values marked unverified are not yet confirmed."
}
Every slide may also have "notes" (speaker notes).
"""
import json
import os
import sys

from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt, Emu

INK = RGBColor(0x0E, 0x0C, 0x20)
MUTED = RGBColor(0x5B, 0x58, 0x78)
LINE = RGBColor(0xDE, 0xDB, 0xEE)
SOFT = RGBColor(0xF6, 0xF5, 0xFB)
VIOLET = RGBColor(0x6B, 0x4D, 0xFF)
PINK = RGBColor(0xFF, 0x5C, 0x93)
GOOD = RGBColor(0x1E, 0x7F, 0x4A)
BAD = RGBColor(0xB4, 0x23, 0x18)
SERIES = [RGBColor(0x6B, 0x4D, 0xFF), RGBColor(0x0B, 0x82, 0x7C), RGBColor(0xFF, 0x5C, 0x93), RGBColor(0xDD, 0x7A, 0x01)]
FONT = "Inter"
LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "app", "brand", "logo-full-light-bg-600w.png")
W, H = Inches(13.333), Inches(7.5)


def text(slide, x, y, w, h, s, size=14, bold=False, color=INK, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05)
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = str(s)
    r.font.size, r.font.bold, r.font.name = Pt(size), bold, FONT
    r.font.color.rgb = color
    return box


def chrome(prs, title, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bar = s.shapes.add_shape(1, 0, 0, W, Inches(0.08))
    bar.fill.solid(); bar.fill.fore_color.rgb = VIOLET; bar.line.fill.background()
    text(s, Inches(0.6), Inches(0.35), Inches(10.5), Inches(0.8), title, 28, True)
    if os.path.exists(LOGO):
        s.shapes.add_picture(LOGO, W - Inches(2.1), Inches(0.42), height=Inches(0.42))
    text(s, Inches(0.6), H - Inches(0.5), Inches(8), Inches(0.3), "Contract.ly", 10, color=MUTED)
    text(s, W - Inches(1.6), H - Inches(0.5), Inches(1), Inches(0.3), str(n), 10, color=MUTED, align=PP_ALIGN.RIGHT)
    return s


def notes(s, spec):
    if spec.get("notes"):
        s.notes_slide.notes_text_frame.text = str(spec["notes"])


def kpis(prs, spec, n):
    s = chrome(prs, spec.get("title", "At a glance"), n)
    items = spec.get("items", [])[:6]
    cols = min(3, max(1, len(items)))
    rows = (len(items) + cols - 1) // cols
    gw, gh = Inches(12.1), Inches(5.3)
    cw, ch = (gw - Inches(0.3) * (cols - 1)) / cols, min(Inches(2.4), (gh - Inches(0.3) * (rows - 1)) / max(rows, 1))
    for i, it in enumerate(items):
        x = Inches(0.6) + (cw + Inches(0.3)) * (i % cols)
        y = Inches(1.5) + (ch + Inches(0.3)) * (i // cols)
        card = s.shapes.add_shape(5, x, y, cw, ch)
        card.fill.solid(); card.fill.fore_color.rgb = SOFT; card.line.color.rgb = LINE
        card.adjustments[0] = 0.08
        tone = {"good": GOOD, "bad": BAD}.get(it.get("tone"), INK)
        text(s, x + Inches(0.3), y + Inches(0.25), cw - Inches(0.6), Inches(0.4), it.get("label", ""), 14, color=MUTED)
        text(s, x + Inches(0.3), y + Inches(0.7), cw - Inches(0.6), Inches(0.9), it.get("value", ""), 36, True, tone)
        if it.get("note"):
            text(s, x + Inches(0.3), y + ch - Inches(0.65), cw - Inches(0.6), Inches(0.5), it["note"], 12, color=MUTED)
    notes(s, spec)


def bullets(prs, spec, n):
    s = chrome(prs, spec.get("title", ""), n)
    box = s.shapes.add_textbox(Inches(0.7), Inches(1.5), Inches(11.9), Inches(5.2))
    tf = box.text_frame
    tf.word_wrap = True
    for i, b in enumerate(spec.get("bullets", [])[:8]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(12)
        r = p.add_run()
        r.text = "•  " + str(b)
        r.font.size, r.font.name = Pt(20), FONT
        r.font.color.rgb = INK
    notes(s, spec)


def table(prs, spec, n):
    s = chrome(prs, spec.get("title", ""), n)
    cols, rows = spec.get("columns", []), spec.get("rows", [])[:14]
    if not cols:
        return
    t = s.shapes.add_table(len(rows) + 1, len(cols), Inches(0.6), Inches(1.5), Inches(12.1), Inches(0.4) * (len(rows) + 1)).table
    for j, c in enumerate(cols):
        cell = t.cell(0, j)
        cell.text = str(c)
        cell.fill.solid(); cell.fill.fore_color.rgb = INK
        f = cell.text_frame.paragraphs[0].runs[0].font
        f.size, f.bold, f.name, f.color.rgb = Pt(13), True, FONT, RGBColor(0xFF, 0xFF, 0xFF)
    for i, row in enumerate(rows, start=1):
        for j in range(len(cols)):
            cell = t.cell(i, j)
            cell.text = str(row[j]) if j < len(row) and row[j] is not None else ""
            cell.fill.solid(); cell.fill.fore_color.rgb = SOFT if i % 2 else RGBColor(0xFF, 0xFF, 0xFF)
            for p in cell.text_frame.paragraphs:
                for r in p.runs:
                    r.font.size, r.font.name, r.font.color.rgb = Pt(12), FONT, INK
    if len(spec.get("rows", [])) > 14:
        text(s, Inches(0.6), H - Inches(0.9), Inches(10), Inches(0.3), f"Showing 14 of {len(spec['rows'])} rows.", 11, color=MUTED)
    notes(s, spec)


def chart(prs, spec, n):
    s = chrome(prs, spec.get("title", ""), n)
    kind = {"column": XL_CHART_TYPE.COLUMN_CLUSTERED, "bar": XL_CHART_TYPE.BAR_CLUSTERED, "line": XL_CHART_TYPE.LINE_MARKERS, "pie": XL_CHART_TYPE.PIE}.get(spec.get("chart", "column"), XL_CHART_TYPE.COLUMN_CLUSTERED)
    data = CategoryChartData()
    data.categories = spec.get("categories", [])
    series = spec.get("series", [])[: (1 if kind == XL_CHART_TYPE.PIE else 4)]
    for se in series:
        data.add_series(se.get("name", ""), [float(v or 0) for v in se.get("values", [])])
    gf = s.shapes.add_chart(kind, Inches(0.6), Inches(1.4), Inches(12.1), Inches(5.4), data)
    c = gf.chart
    c.font.name, c.font.size = FONT, Pt(12)
    c.has_legend = len(series) > 1 or kind == XL_CHART_TYPE.PIE
    if c.has_legend:
        c.legend.position, c.legend.include_in_layout = XL_LEGEND_POSITION.BOTTOM, False
    fmt = spec.get("number_format", "#,##0")
    if kind == XL_CHART_TYPE.PIE:
        pts = c.plots[0].series[0].points
        for i in range(len(spec.get("categories", []))):
            pts[i].format.fill.solid(); pts[i].format.fill.fore_color.rgb = SERIES[i % len(SERIES)]
    else:
        c.value_axis.tick_labels.number_format, c.value_axis.tick_labels.number_format_is_linked = fmt, False
        c.value_axis.major_gridlines.format.line.color.rgb = LINE
        c.value_axis.format.line.fill.background()
        for i, se in enumerate(c.plots[0].series):
            col = SERIES[i % len(SERIES)]
            if kind == XL_CHART_TYPE.LINE_MARKERS:
                se.format.line.color.rgb = col; se.format.line.width = Pt(2.25)
            else:
                se.format.fill.solid(); se.format.fill.fore_color.rgb = col
        if kind != XL_CHART_TYPE.LINE_MARKERS:
            c.plots[0].gap_width = 80
    notes(s, spec)


def timeline(prs, spec, n):
    s = chrome(prs, spec.get("title", "Key dates"), n)
    items = spec.get("items", [])[:8]
    if not items:
        return
    y = Inches(3.9)
    line = s.shapes.add_connector(1, Inches(0.8), y, W - Inches(0.8), y)
    line.line.color.rgb = LINE; line.line.width = Pt(3)
    step = (W - Inches(1.6)) / max(len(items), 1)
    for i, it in enumerate(items):
        cx = Inches(0.8) + step * i + step / 2
        dot = s.shapes.add_shape(9, cx - Inches(0.14), y - Inches(0.14), Inches(0.28), Inches(0.28))
        dot.fill.solid(); dot.fill.fore_color.rgb = PINK if i % 2 else VIOLET; dot.line.fill.background()
        up = i % 2 == 0
        text(s, cx - step / 2 + Inches(0.05), y - Inches(1.6) if up else y + Inches(0.35), step - Inches(0.1), Inches(0.4), it.get("date", ""), 14, True, align=PP_ALIGN.CENTER)
        text(s, cx - step / 2 + Inches(0.05), y - Inches(1.2) if up else y + Inches(0.75), step - Inches(0.1), Inches(0.9), it.get("label", ""), 12, color=MUTED, align=PP_ALIGN.CENTER)
    notes(s, spec)


def build(spec, out):
    prs = Presentation()
    prs.slide_width, prs.slide_height = W, H
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg = s.shapes.add_shape(1, 0, 0, W, H)
    bg.fill.solid(); bg.fill.fore_color.rgb = INK; bg.line.fill.background()
    band = s.shapes.add_shape(1, 0, H - Inches(0.12), W, Inches(0.12))
    band.fill.solid(); band.fill.fore_color.rgb = VIOLET; band.line.fill.background()
    text(s, Inches(0.9), Inches(2.4), Inches(11.5), Inches(1.4), spec.get("title", "Contracts update"), 44, True, RGBColor(0xFF, 0xFF, 0xFF))
    text(s, Inches(0.9), Inches(3.8), Inches(11.5), Inches(0.8), spec.get("subtitle", ""), 22, color=RGBColor(0xC9, 0xC4, 0xEE))
    text(s, Inches(0.9), Inches(6.2), Inches(8), Inches(0.5), f"Contract.ly · {spec.get('date', '')}".strip(" ·"), 14, color=RGBColor(0xA9, 0xA5, 0xCC))
    makers = {"kpis": kpis, "bullets": bullets, "table": table, "chart": chart, "timeline": timeline}
    n = 1
    for sl in spec.get("slides", [])[:20]:
        if sl.get("type") in makers:
            n += 1
            makers[sl["type"]](prs, sl, n)
    if spec.get("sources"):
        n += 1
        s = chrome(prs, "Sources and notes", n)
        text(s, Inches(0.7), Inches(1.5), Inches(11.9), Inches(4), spec["sources"], 16, color=MUTED)
    prs.save(out)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as fh:
        build(json.load(fh), sys.argv[2])
    print(sys.argv[2])
