---
$id: ent_paper_semantic_co_speech_gesture_syn_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots
  zh: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots
  ko: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots
summary:
  en: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.
  zh: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.
  ko: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- loco_manipulation
- semantic_co_speech_gesture_syn
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.17183v1.
sources:
- id: src_001
  type: paper
  title: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2512.17183
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present an innovative end-to-end framework for synthesizing semantically meaningful co-speech gestures and deploying them in real-time on a humanoid robot. This system addresses the challenge of creating natural, expressive non-verbal communication for robots by integrating advanced gesture generation techniques with robust physical control. Our core innovation lies in the meticulous integration of a semantics-aware gesture synthesis module, which derives expressive reference motions from speech input by leveraging a generative retrieval mechanism based on large language models (LLMs) and an autoregressive Motion-GPT model. This is coupled with a high-fidelity imitation learning control policy, the MotionTracker, which enables the Unitree G1 humanoid robot to execute these complex motions dynamically and maintain balance. To ensure feasibility, we employ a robust General Motion Retargeting (GMR) method to bridge the embodiment gap between human motion data and the robot platform. Through comprehensive evaluation, we demonstrate that our combined system produces semantically appropriate and rhythmically coherent gestures that are accurately tracked and executed by the physical robot. To our knowledge, this work represents a significant step toward general real-world use by providing a complete pipeline for automatic, semantic-aware, co-speech gesture generation and synchronized real-time physical deployment on a humanoid robot.

## 核心内容
We present an innovative end-to-end framework for synthesizing semantically meaningful co-speech gestures and deploying them in real-time on a humanoid robot. This system addresses the challenge of creating natural, expressive non-verbal communication for robots by integrating advanced gesture generation techniques with robust physical control. Our core innovation lies in the meticulous integration of a semantics-aware gesture synthesis module, which derives expressive reference motions from speech input by leveraging a generative retrieval mechanism based on large language models (LLMs) and an autoregressive Motion-GPT model. This is coupled with a high-fidelity imitation learning control policy, the MotionTracker, which enables the Unitree G1 humanoid robot to execute these complex motions dynamically and maintain balance. To ensure feasibility, we employ a robust General Motion Retargeting (GMR) method to bridge the embodiment gap between human motion data and the robot platform. Through comprehensive evaluation, we demonstrate that our combined system produces semantically appropriate and rhythmically coherent gestures that are accurately tracked and executed by the physical robot. To our knowledge, this work represents a significant step toward general real-world use by providing a complete pipeline for automatic, semantic-aware, co-speech gesture generation and synchronized real-time physical deployment on a humanoid robot.

## 参考
- http://arxiv.org/abs/2512.17183v1

