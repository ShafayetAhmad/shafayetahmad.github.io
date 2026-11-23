---
layout: profile
title: Sitemap
permalink: /sitemap/
---

- [Home]({{ '/' | relative_url }})
{% include blog-count.html %}{% for item in site.data.navigation.pages %}{% if item.url == '/blog/' and blog_count == 0 %}{% continue %}{% endif %}- [{{ item.title }}]({{ item.url | relative_url }})
{% endfor %}
[XML sitemap]({{ '/sitemap.xml' | relative_url }}).
