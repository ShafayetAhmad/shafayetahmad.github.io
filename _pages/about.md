---
permalink: /
redirect_from:
  - /classic/
  - /about/
  - /bn/
  - /news/
layout: profile
home: true
author_profile: false
---

<h1 class="hero-title">Shafayet Ahmad Kanon</h1>
<div class="hero-subtitle">PhD Student in Computer Science at the University of Greenwich</div>

<img class="about-photo" src="{{ '/images/shafayet-portrait.webp' | relative_url }}" alt="Shafayet Ahmad Kanon beside a lake with mountains behind him" width="300" height="276" fetchpriority="high">

<p>I am a PhD student in Computer Science at the <a href="https://www.gre.ac.uk/">University of Greenwich</a> in London, supervised by <a href="https://www.gre.ac.uk/people/rep/faculty-of-engineering-and-science/peter-lawrence">Dr Peter Lawrence</a> and <a href="https://www.gre.ac.uk/people/rep/faculty-of-engineering-and-science/asim-siddiqui">Dr Asim Siddiqui</a>, with an M³4Impact Funded Doctoral Studentship. I work in the <a href="https://www.gre.ac.uk/research/groups/safety-disaster-resilience-and-protective-security">Centre for Safety, Resilience and Protective Security (CSRPS)</a>, School of Computing and Mathematical Sciences. Before my PhD, I received an MSc in Computer Science with Distinction from Greenwich and a BTech in Computer Science and Engineering from <a href="https://kiit.ac.in/">KIIT University</a>, India.</p>

<p>I am interested in <strong>reliable and accountable AI</strong>, <strong>LLM evaluation</strong>, <strong>retrieval-augmented generation (RAG)</strong>, <strong>computer vision</strong> and <strong>human oversight of AI</strong>. I want AI outputs that people can evaluate, trace and use responsibly in high-stakes work. Fire safety engineering is my application domain. For example, when a language model cites a clause in a building regulation, can an engineer trace its answer back to evidence that supports it? <a href="{{ '/research/' | relative_url }}">More about my research</a>.</p>

<div class="quick-links">
  <a href="#">CV</a><span class="divider">|</span>
  <a href="mailto:{{ site.author.email }}">Email</a><span class="divider">|</span>
  <a href="https://github.com/{{ site.author.github }}">GitHub</a><span class="divider">|</span>
  <a href="https://linkedin.com/in/{{ site.author.linkedin }}">LinkedIn</a><span class="divider">|</span>
  <a href="{{ site.author.orcid }}">ORCID</a><span class="divider">|</span>
  <a href="{{ site.author.medium }}">Medium</a><span class="divider">|</span>
  <a href="https://www.youtube.com/@{{ site.author.youtube }}">YouTube</a>
</div>

<h2 id="news">News</h2>
{% if site.data.news.size > 4 %}<div class="news-hint">scroll ↓</div>{% endif %}
<div class="news-box" tabindex="0" aria-label="News, newest first">
{% include news.html %}
</div>

<h2 id="publications">Publications</h2>
{% include manuscript.html %}

<h2 id="projects">Projects</h2>
<ol class="pub-list">
  <li class="pub-item">
    <span class="pub-title">Real-Time Fire and Smoke Detection from Video with Human-in-the-Loop Verification</span><br>
    MSc dissertation, University of Greenwich. 2025.<br>
    <em>Transfer learning with MobileNetV2 and MobileNetV3-Large (TensorFlow, Keras), OpenCV and a PyQt5 operator console.</em><br>
    The system detects fire and smoke in a video feed and sends each alarm to a human operator, who checks it before escalation.<br>
    <span class="pub-links"><a href="{{ '/software/' | relative_url }}">details</a></span>
  </li>
</ol>

{% include blog-count.html %}{% if blog_count > 0 %}
<h2 id="blog">Blog</h2>
{% include post-list.html limit=3 %}
<p class="section-more"><a href="{{ '/blog/' | relative_url }}">All posts</a> <span class="divider">|</span> <a href="https://www.youtube.com/@{{ site.author.youtube }}">Videos on YouTube</a></p>
{% endif %}

<h2 id="experience">Experience</h2>
<ul class="entry-list">
  <li class="entry">
    <div class="entry__meta">Apr 2026 - present · London, UK</div>
    <div class="entry__title">Doctoral Research Student, <a href="https://www.gre.ac.uk/">University of Greenwich</a></div>
    <div class="entry__details">AI for performance-based fire safety engineering: reliability of language model outputs, retrieval over regulatory documents, and which decisions engineers can safely delegate to AI.</div>
  </li>
  <li class="entry">
    <div class="entry__meta">May 2024 - Aug 2024</div>
    <div class="entry__title">Backend Software Engineer Intern, ANTT Robotics R&amp;D</div>
    <div class="entry__details">Built and documented REST APIs with Node.js, Express and MongoDB. Integrated the OpenAI API into a customer-needs prediction feature.</div>
  </li>
</ul>

<h2 id="education">Education</h2>
<ul class="entry-list">
  <li class="entry">
    <div class="entry__meta">Apr 2026 - present · London, UK</div>
    <div class="entry__title">PhD in Computer Science, <a href="https://www.gre.ac.uk/">University of Greenwich</a></div>
  </li>
  <li class="entry">
    <div class="entry__meta">Oct 2024 - Oct 2025 · London, UK</div>
    <div class="entry__title">MSc in Computer Science (Distinction), <a href="https://www.gre.ac.uk/">University of Greenwich</a></div>
  </li>
  <li class="entry">
    <div class="entry__meta">Oct 2020 - May 2024 · Bhubaneswar, India</div>
    <div class="entry__title">BTech in Computer Science and Engineering, <a href="https://kiit.ac.in/">KIIT University</a></div>
  </li>
</ul>

<h2 id="awards">Achievements</h2>
<div class="achievement-list">
  <div class="achievement-card">
    <div class="achievement__meta">Apr 2026 · University of Greenwich</div>
    <div class="achievement__title">M³4Impact Funded Doctoral Studentship</div>
    <p>Funding for my PhD in Computer Science at the University of Greenwich.</p>
  </div>
  <div class="achievement-card">
    <div class="achievement__meta">Sep 2020 · Kalinga Institute of Industrial Technology (KIIT) &amp; Government of India</div>
    <div class="achievement__title">Study in India (SII) Scholarship &amp; KIIT University International Scholarship</div>
    <p>Funding for my BTech in Computer Science and Engineering at KIIT University, Bhubaneswar, India.</p>
  </div>
</div>

<h2 id="talks">Talks</h2>
{% include nrips-talk.html %}
