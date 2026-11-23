# scripts/

Utility scripts for this website.

## `make-og-image.py`

Makes the social preview image `images/og-image.png` (1200x630 PNG). Link
previews on LinkedIn, X, Slack and similar sites show it. It uses your name,
role and topics from the top of the script, and the portrait at
`images/shafayet-portrait.webp`.

```
python3 scripts/make-og-image.py
```

You need Python 3 with [Pillow](https://python-pillow.org) (`pip install Pillow`)
and the DejaVu Sans fonts. Set `FONT_DIR` if the fonts are somewhere other than
`/usr/share/fonts/truetype/dejavu`.

The image is committed to the repo, so the site build does not need Pillow.
Run the script again after changing your role, topics or photo.

## `make-favicons.py`

Makes the PNG and ICO favicons (`images/favicon-*.png`, `images/favicon.ico` and
`images/apple-touch-icon-180x180.png`) from the same serif "S" as
`images/favicon.svg`. Needs Pillow and the DejaVu Serif font.

```
python3 scripts/make-favicons.py
```

## `make-cv-pdf.py`

Makes a PDF of your CV, for your own use, by printing the CV page (`/cv/`) to
A4 in a headless browser, with links pointing to www.shafayetahmad.com. It is
saved to `cv-pdf/Shafayet-Ahmad-Kanon-CV.pdf`, which git ignores and the site
does not publish. The page's print styles add the name and contact block and
hide the masthead and footer. Build the site first.

```
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/make-cv-pdf.py
```

Needs Playwright (`pip install playwright`, then
`python3 -m playwright install chromium`). Set `CHROME` to use another
Chromium-based browser.
