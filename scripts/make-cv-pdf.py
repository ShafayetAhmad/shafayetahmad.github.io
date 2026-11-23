#!/usr/bin/env python3
"""Make a PDF of the CV page, for your own use.

The PDF is the /cv/ page printed to A4 in a headless browser, so it always says
the same as the page. It is saved to cv-pdf/, which git ignores and the site
does not publish. Edit _pages/cv.md, then run:

    JEKYLL_ENV=production bundle exec jekyll build
    python3 scripts/make-cv-pdf.py

Requires Python 3 with Playwright (pip install playwright) and a Chromium
browser (python3 -m playwright install chromium). Set CHROME to the path of
another Chromium-based browser to use that instead.
"""
import asyncio
import functools
import http.server
import os
import socketserver
import threading

from playwright.async_api import async_playwright

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(REPO_ROOT, "_site")
OUT = os.path.join(REPO_ROOT, "cv-pdf", "Shafayet-Ahmad-Kanon-CV.pdf")  # not published
SITE_URL = "https://www.shafayetahmad.com"  # links in the PDF point here

FOOTER = (
    '<div style="width:100%;margin:0 16mm;font-size:8px;color:#888;'
    'font-family:-apple-system,Helvetica,Arial,sans-serif;display:flex;justify-content:space-between">'
    "<span>Shafayet Ahmad Kanon · Curriculum vitae</span>"
    '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'
)


def serve(directory):
    """Serve the built site on a free local port, in the background."""
    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    handler = functools.partial(QuietHandler, directory=directory)
    server = socketserver.TCPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


async def main():
    if not os.path.exists(os.path.join(SITE_DIR, "cv", "index.html")):
        raise SystemExit("Build the site first: JEKYLL_ENV=production bundle exec jekyll build")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    server = serve(SITE_DIR)
    origin = f"http://127.0.0.1:{server.server_address[1]}"
    async with async_playwright() as p:
        launch = {"executable_path": os.environ["CHROME"]} if os.environ.get("CHROME") else {}
        browser = await p.chromium.launch(**launch)
        page = await browser.new_page(color_scheme="light")
        await page.goto(f"{origin}/cv/", wait_until="networkidle")
        await page.emulate_media(media="print", color_scheme="light")
        # Links to the site's own pages should point to the live site, not this local server
        await page.evaluate(
            """([origin, site]) => document.querySelectorAll('a[href]').forEach(a => {
                 if (a.href.startsWith(origin)) a.href = site + a.href.slice(origin.length);
               })""",
            [origin, SITE_URL],
        )
        await page.pdf(
            path=OUT,
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template=FOOTER,
        )
        await browser.close()
    server.shutdown()
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    asyncio.run(main())
