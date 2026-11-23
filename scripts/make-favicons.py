#!/usr/bin/env python3
"""Make the PNG and ICO favicons from the same serif "S" as images/favicon.svg.

The letter sits on a white rounded square, so it stays visible on light and
dark browser tabs and on phone home screens.

Requires Pillow and the DejaVu Serif font (set FONT_DIR if it is elsewhere).

    python3 scripts/make-favicons.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(REPO_ROOT, "images")
FONT_DIR = os.environ.get("FONT_DIR", "/usr/share/fonts/truetype/dejavu")
INK = (26, 26, 26)


def icon(size, rounded=True):
    scale = 4  # draw large, then shrink for smooth edges
    big = size * scale
    img = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if rounded:
        d.rounded_rectangle((0, 0, big - 1, big - 1), radius=big // 5, fill="white")
    else:
        d.rectangle((0, 0, big - 1, big - 1), fill="white")
    f = ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSerif.ttf"), int(big * 0.78))
    d.text((big / 2, big / 2), "S", font=f, fill=INK, anchor="mm")
    return img.resize((size, size), Image.LANCZOS)


def main():
    for size in (32, 192, 512):
        icon(size).save(os.path.join(IMAGES, f"favicon-{size}x{size}.png"), optimize=True)
    # iOS adds its own rounded corners and needs an opaque square
    icon(180, rounded=False).convert("RGB").save(os.path.join(IMAGES, "apple-touch-icon-180x180.png"), optimize=True)
    icon(256).save(os.path.join(IMAGES, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    print("Wrote favicons to", IMAGES)


if __name__ == "__main__":
    main()
