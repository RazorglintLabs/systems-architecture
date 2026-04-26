"""
Render terminal text to dark-background JPG proof images.
Usage: Called by proof generation pipeline.
"""
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PROOF_DIR = Path(__file__).parent
# Try to use Consolas (Windows), fall back to default monospace
FONT_NAME = "consola.ttf"
FONT_SIZE = 16
LINE_HEIGHT = 22
PADDING = 32
BG_COLOR = (24, 24, 28)
FG_COLOR = (204, 204, 204)
GREEN = (80, 200, 120)
RED = (220, 70, 70)
YELLOW = (220, 200, 80)
CYAN = (100, 200, 220)
DIM = (120, 120, 130)
MAX_WIDTH = 1100


def get_font():
    try:
        return ImageFont.truetype(FONT_NAME, FONT_SIZE)
    except OSError:
        try:
            return ImageFont.truetype("C:/Windows/Fonts/consola.ttf", FONT_SIZE)
        except OSError:
            return ImageFont.load_default()


def color_for_line(line: str) -> tuple:
    lo = line.lower().strip()
    if any(k in lo for k in ["passed", "pass", "ok", "verified", "valid", "safe to say"]):
        if any(k in lo for k in ["fail", "error", "deny", "breach", "block", "forbidden", "rejected"]):
            return RED
        return GREEN
    if any(k in lo for k in ["failed", "fail", "error", "deny", "denied", "breach",
                              "block", "blocked", "forbidden", "rejected", "panic", "invalid"]):
        return RED
    if any(k in lo for k in ["warning", "skip", "gap", "partial", "open"]):
        return YELLOW
    if any(k in lo for k in ["───", "═══", "---", "===", "┌", "├", "└", "│"]):
        return DIM
    if lo.startswith(("#", "$", ">")):
        return CYAN
    return FG_COLOR


def render_proof(text: str, filename: str, title: str = ""):
    font = get_font()
    lines = text.split("\n")

    # Measure max line width
    tmp = Image.new("RGB", (1, 1))
    tmp_draw = ImageDraw.Draw(tmp)
    max_line_w = 0
    for line in lines:
        bbox = tmp_draw.textbbox((0, 0), line, font=font)
        max_line_w = max(max_line_w, bbox[2] - bbox[0])

    img_w = min(max(max_line_w + PADDING * 2, 600), MAX_WIDTH + PADDING * 2)
    title_offset = LINE_HEIGHT + 12 if title else 0
    img_h = PADDING * 2 + title_offset + len(lines) * LINE_HEIGHT + 8

    img = Image.new("RGB", (img_w, img_h), BG_COLOR)
    draw = ImageDraw.Draw(img)

    y = PADDING
    if title:
        draw.text((PADDING, y), title, fill=CYAN, font=font)
        y += LINE_HEIGHT + 12
        draw.line([(PADDING, y - 6), (img_w - PADDING, y - 6)], fill=DIM, width=1)

    for line in lines:
        color = color_for_line(line)
        draw.text((PADDING, y), line, fill=color, font=font)
        y += LINE_HEIGHT

    out = PROOF_DIR / filename
    img.save(str(out), "JPEG", quality=92)
    print(f"  -> {out.name}")
    return out
