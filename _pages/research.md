---
title: "Research"
permalink: /research/
redirect_from:
  - /classic/research/
layout: profile
author_profile: false
---

I began my PhD in April 2026. My current work defines the questions and methods.

## When can an engineer rely on an AI answer?

Fire engineers often combine prescriptive guidance with performance-based analysis. A building may fall outside the scope of a rule, or a designer may need to justify a departure from it. Either way, other engineers review the argument, a regulator considers it, and the engineer carries professional responsibility. A confident answer that misquotes a clause can find its way into a fire strategy. A system that recognises a gap in its evidence gives the engineer a chance to investigate.

## Three questions guide my PhD

1. **Does the evidence support the answer?** I evaluate language models on fire-safety guidance by checking whether their answers stay faithful to retrieved sources, which claims lack support, and whether each cited clause actually supports the claim attached to it.
2. **What does retrieval need to preserve?** A table, an exception or a cross-reference can change how a clause applies. I study retrieval-augmented generation (RAG) over technical, regulatory and scientific documents, including how a system should respond when it retrieves too little evidence.
3. **Who has authority to act?** I study how engineers allocate decisions and actions between people and AI. Some tasks can proceed directly, some require review, and others should remain entirely with the engineer. This is the subject of our [manuscript in preparation]({{ '/publications/' | relative_url }}).

## Research interests

In AI evaluation, I am most interested in measuring unsupported claims, checking whether citations are correct, and comparing model judgements with those of human reviewers. I am also interested in how building data in openBIM/IFC and graph representations can support these checks. My MSc work on fire and smoke detection from video gives me a background in computer vision.

## Fire engineering tools

Our group uses **buildingEXODUS** to model evacuation and **SMARTFIRE** for computational fluid dynamics simulations of fire and smoke. Both need considerable manual setup and engineering judgement to interpret their results, and I am learning to use them. I work with openBIM/IFC and IfcOpenShell to represent buildings, alongside graph representations, Python, TensorFlow, RAG and language model evaluation. Applications include regulatory compliance, drawing and geometry interpretation, and performance-based fire safety engineering.
