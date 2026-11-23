# shafayetahmad.github.io

Source for the academic website of **Shafayet Ahmad Kanon**, a PhD student in Computer Science at the University of Greenwich working on reliable AI for fire safety engineering.

**Live site:** https://www.shafayetahmad.com

The site is built with [Jekyll](https://jekyllrb.com/) and published by GitHub Pages through GitHub Actions, on the custom domain `www.shafayetahmad.com` (set in the repo's Pages settings). `shafayetahmad.github.io` forwards there.

## Where things live

| What | File |
| --- | --- |
| Homepage (intro, publications, projects, experience, education, awards, talks) | `_pages/about.md` |
| News items, newest first | `_data/news.yml` |
| Blog posts written on this site | `_posts/` |
| Posts published on Medium (listed with the blog posts, linking out) | `_external_posts/` |
| Publication and talk entries shared across pages | `_includes/manuscript.html`, `_includes/nrips-talk.html` |
| Other pages: research, publications, CV, software, blog | `_pages/` |
| Portrait | `images/shafayet-portrait.webp` |
| Top navigation and sitemap links | `_data/navigation.yml` |
| Site name, profile links and email | `_config.yml` |
| Page styles | `_sass/layout/_academic-profile.scss` |

### Writing a blog post

1. Copy `_drafts/post-template.md` to `_posts/YYYY-MM-DD-short-title.md`, for example `_posts/2026-12-01-reliable-ai-for-fire-engineering.md`. The date in the file name is the post's date.
2. Set `title` and a one-sentence `summary` in the front matter, then write the post in Markdown below it. For a post first published somewhere else, add `original_url` and `original_source` (for example `Medium`); the post page then says where it first appeared.
3. Put images in `images/blog/` and link them as `![Alt text](/images/blog/name.png)`.

The post appears at `/blog/short-title/`. The homepage shows the 3 newest posts and `/blog/` lists them all, together with the Medium posts. Posts also go into the RSS feed at `/rss.xml`. To preview drafts locally, run `bundle exec jekyll serve --drafts`.

To hide a post without deleting it, add `published: false` to its front matter. The file stays in the repo, but the post is not built. All posts are hidden at the moment. While no post is published, the homepage Blog section and the Blog link in the navigation are hidden too, and they come back when you publish a post. To preview hidden posts locally, run `bundle exec jekyll serve --unpublished`.

To list a post published elsewhere, add a file to `_external_posts/` with `title`, `date`, `external_url`, `source` and `summary`. No page is built for it; the list links straight to it.

### Adding a news item

Add an entry at the top of `_data/news.yml`:

```yaml
- date: "2026-12"
  text: Presented a poster at <a href="https://example.org">Example Conference</a>.
```

`text` can contain HTML. The homepage news box updates from this file.

### Making a CV PDF

The site does not publish a CV PDF. To make one for yourself, print the CV page to A4:

```bash
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/make-cv-pdf.py
```

The PDF is saved to `cv-pdf/`, which git ignores. This needs Playwright (`pip install playwright` and `python3 -m playwright install chromium`).

## Preview locally

You need Ruby with Bundler, and Node.js.

```bash
bundle config set --local path vendor/bundle
bundle install
npm install
npm run build:js          # builds assets/js/main.min.js
bundle exec jekyll serve -l -H localhost
```

Then open http://localhost:4000. Changes to `_config.yml` need a restart.

With Docker instead: `docker compose up`, then open http://localhost:4000. The `.devcontainer` folder sets up the same environment in VS Code.

## Publishing

Pushing to `master` builds and deploys the site with `.github/workflows/jekyll.yml`. Pull requests run the same build plus a check that every page, homepage section and the CV PDF exist, but they do not deploy.

## Credits and licence

Built on the [AcademicPages](https://github.com/academicpages/academicpages.github.io) theme, a fork of [Minimal Mistakes](https://mademistakes.com/work/minimal-mistakes-jekyll-theme/), both MIT-licensed (see `LICENSE`). Design based on [Rikiya Takehi's website](https://rikiyat.github.io/).

The theme code is under the MIT licence. The text, photos and CV are © Shafayet Ahmad Kanon.
