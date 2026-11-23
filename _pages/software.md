---
title: "Software and projects"
permalink: /software/
redirect_from:
  - /classic/software/
layout: profile
author_profile: false
---

## Real-time fire and smoke detection from video

For my MSc dissertation at Greenwich, I developed a system that detects fire and smoke in a video feed and sends each alarm to a human reviewer. I used transfer learning with MobileNetV2 and MobileNetV3-Large in TensorFlow and Keras, OpenCV for video processing, and PyQt5 for the operator console. The reviewer could inspect the alarm before escalation.

The dataset contained 651 images derived from MIVIA fire-detection video sequences. Its size limits the conclusions I can draw about performance on other footage.
