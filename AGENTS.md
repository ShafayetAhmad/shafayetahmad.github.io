# Notes for coding agents

This is Shafayet Ahmad Kanon's personal academic website, built with Jekyll on the AcademicPages theme and deployed to GitHub Pages. It is not the AcademicPages template project, so do not open pull requests against that project.

- Content lives in `_pages/`, `_posts/` (blog posts), `_external_posts/` (Medium posts), `_data/news.yml` and the includes listed in `README.md`.
- Blog posts use the `post` layout (`_layouts/post.html`). `_includes/post-list.html` lists site and external posts together, newest first.
- Pages use the `profile` layout (`_layouts/profile.html`). Page styles are in `_sass/layout/_academic-profile.scss`.
- The site is English only. It has a light and a dark theme: it follows the visitor's system setting, and the toggle in the masthead overrides it. Profile colours are CSS custom properties in `_sass/layout/_academic-profile.scss`, with a dark set under `html[data-theme="dark"]`.
- Before opening a pull request, build with `JEKYLL_ENV=production bundle exec jekyll build` and run the output checks in `.github/workflows/jekyll.yml`.
- `assets/js/main.min.js` is generated (`npm run build:js`) and is not committed.
