---
$id: ent_paper_lee_bring_my_cup_personalizing_vis_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting
  zh: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting
  ko: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting
summary:
  en: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting (Bring My Cup Personalizing
    Vision-Language-Action Models with Visual Attentive Prompting), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by POSTECH, GSAI, IME, dblab.
  zh: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting (Bring My Cup Personalizing
    Vision-Language-Action Models with Visual Attentive Prompting), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by POSTECH, GSAI, IME, dblab.
  ko: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting (Bring My Cup Personalizing
    Vision-Language-Action Models with Visual Attentive Prompting), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by POSTECH, GSAI, IME, dblab.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bring_my_cup_personalizing_vis
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.20014v3.
sources:
- id: src_001
  type: paper
  title: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting (arXiv)
  url: https://arxiv.org/abs/2512.20014
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Bring My Cup Personalizing Vision-Language-Action Models with Visual Attentive Prompting source
  url: https://doi.org/10.48550/arXiv.2512.20014
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
While Vision-Language-Action (VLA) models generalize well to generic instructions, they struggle with personalized commands such as "bring my cup," where the robot must act on one specific instance among visually similar objects. We study this setting of manipulating personal objects, in which a VLA must identify and control a user-specific object unseen during training using only a few reference images. To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with top-down selective attention. VAP treats the reference images as a non-parametric visual memory, grounds the personal object in the scene through open-vocabulary detection and embedding-based matching, and then injects this grounding as a visual prompt by highlighting the object and rewriting the instruction. We construct two simulation benchmarks, Personalized-SIMPLER and Personalized-VLABench, and a real-world tabletop benchmark to evaluate personalized manipulation across multiple robots and tasks. Experiments show that VAP consistently outperforms generic policies and token-learning baselines in both success rate and correct-object manipulation, helping to bridge the gap between semantic understanding and instance-level control.

## 核心内容
While Vision-Language-Action (VLA) models generalize well to generic instructions, they struggle with personalized commands such as "bring my cup," where the robot must act on one specific instance among visually similar objects. We study this setting of manipulating personal objects, in which a VLA must identify and control a user-specific object unseen during training using only a few reference images. To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with top-down selective attention. VAP treats the reference images as a non-parametric visual memory, grounds the personal object in the scene through open-vocabulary detection and embedding-based matching, and then injects this grounding as a visual prompt by highlighting the object and rewriting the instruction. We construct two simulation benchmarks, Personalized-SIMPLER and Personalized-VLABench, and a real-world tabletop benchmark to evaluate personalized manipulation across multiple robots and tasks. Experiments show that VAP consistently outperforms generic policies and token-learning baselines in both success rate and correct-object manipulation, helping to bridge the gap between semantic understanding and instance-level control.

## 参考
- http://arxiv.org/abs/2512.20014v3

