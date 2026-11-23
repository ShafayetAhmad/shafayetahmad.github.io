#!/usr/bin/env python3
"""Make the social preview image (images/og-image.png, 1200x630).

Link previews on LinkedIn, X, Slack and similar sites use this image.
Name and role on the left, the portrait on the right, with a green rule.

Requires Pillow and the DejaVu Sans fonts. Point FONT_DIR at another folder
with DejaVuSans.ttf and DejaVuSans-Bold.ttf if needed.

    python3 scripts/make-og-image.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTRAIT = os.path.join(REPO_ROOT, "images", "shafayet-portrait.webp")
OUT = os.path.join(REPO_ROOT, "images", "og-image.png")

NAME = "Shafayet Ahmad Kanon"
ROLE = ["PhD Student in Computer Science", "University of Greenwich"]
TOPICS = "Reliable AI · LLM evaluation · RAG · Fire safety engineering"
DOMAIN = "shafayetahmad.com"

W, H = 1200, 630
BG = (255, 255, 255)
GREEN = (17, 134, 89)          # site accent #118659
TEXT = (73, 78, 82)            # site text colour
MUTED = (108, 115, 128)        # site muted colour #6c7380
FONT_DIR = os.environ.get("FONT_DIR", "/usr/share/fonts/truetype/dejavu")


def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def rounded_photo(path, size, radius):
    photo = Image.open(path).convert("RGB")
    # Cover-crop to the target size
    scale = max(size[0] / photo.width, size[1] / photo.height)
    photo = photo.resize((round(photo.width * scale), round(photo.height * scale)), Image.LANCZOS)
    left = (photo.width - size[0]) // 2
    top = (photo.height - size[1]) // 2
    photo = photo.crop((left, top, left + size[0], top + size[1]))
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255)
    return photo, mask


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Portrait on the right
    pw, ph = 360, 440
    photo, mask = rounded_photo(PORTRAIT, (pw, ph), 18)
    img.paste(photo, (W - 70 - pw, (H - ph) // 2), mask)

    # Text on the left, sized to fit beside the portrait
    x = 70
    max_w = W - 70 - pw - 50 - x
    size = 50
    while d.textlength(NAME, font=font(size, bold=True)) > max_w and size > 30:
        size -= 1
    d.text((x, 150), NAME, font=font(size, bold=True), fill=TEXT)
    d.rectangle((x, 228, x + 90, 232), fill=GREEN)
    y = 262
    for line in ROLE:
        d.text((x, y), line, font=font(30), fill=MUTED)
        y += 42
    topic_size = 21
    while d.textlength(TOPICS, font=font(topic_size)) > max_w and topic_size > 14:
        topic_size -= 1
    d.text((x, y + 28), TOPICS, font=font(topic_size), fill=TEXT)
    d.text((x, H - 120), DOMAIN, font=font(24, bold=True), fill=GREEN)

    img.save(OUT, "PNG", optimize=True)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
