---
$id: ent_paper_kurenkov_dont_blind_your_vla_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Don't Blind Your VLA
  zh: Don't Blind Your VLA
  ko: Don't Blind Your VLA
summary:
  en: Don't Blind Your VLA (Don't Blind Your VLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Cognitive AI Lab, IAI MIPT.
  zh: Don't Blind Your VLA (Don't Blind Your VLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Cognitive AI Lab, IAI MIPT.
  ko: Don't Blind Your VLA (Don't Blind Your VLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Cognitive AI Lab, IAI MIPT.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dont_blind_your_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.25616v1.
sources:
- id: src_001
  type: paper
  title: Don't Blind Your VLA (arXiv)
  url: https://arxiv.org/abs/2510.25616
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Don't Blind Your VLA source
  url: https://doi.org/10.48550/arXiv.2510.25616
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The growing success of Vision-Language-Action (VLA) models stems from the promise that pretrained Vision-Language Models (VLMs) can endow agents with transferable world knowledge and vision-language (VL) grounding, laying a foundation for action models with broader generalization. Yet when these VLMs are adapted to the action modality, it remains unclear to what extent their original VL representations and knowledge are preserved. In this work, we conduct a systematic study of representation retention during VLA fine-tuning, showing that naive action fine-tuning leads to degradation of visual representations. To characterize and measure these effects, we probe VLA's hidden representations and analyze attention maps, further, we design a set of targeted tasks and methods that contrast VLA models with their counterpart VLMs, isolating changes in VL capabilities induced by action fine-tuning. We further evaluate a range of strategies for aligning visual representations and introduce a simple yet effective method that mitigates degradation and yields improved generalization to out-of-distribution (OOD) scenarios. Taken together, our analysis clarifies the trade-off between action fine-tuning and the degradation of VL representations and highlights practical approaches to recover inherited VL capabilities. Code is publicly available: https://blind-vla-paper.github.io

## 核心内容
The growing success of Vision-Language-Action (VLA) models stems from the promise that pretrained Vision-Language Models (VLMs) can endow agents with transferable world knowledge and vision-language (VL) grounding, laying a foundation for action models with broader generalization. Yet when these VLMs are adapted to the action modality, it remains unclear to what extent their original VL representations and knowledge are preserved. In this work, we conduct a systematic study of representation retention during VLA fine-tuning, showing that naive action fine-tuning leads to degradation of visual representations. To characterize and measure these effects, we probe VLA's hidden representations and analyze attention maps, further, we design a set of targeted tasks and methods that contrast VLA models with their counterpart VLMs, isolating changes in VL capabilities induced by action fine-tuning. We further evaluate a range of strategies for aligning visual representations and introduce a simple yet effective method that mitigates degradation and yields improved generalization to out-of-distribution (OOD) scenarios. Taken together, our analysis clarifies the trade-off between action fine-tuning and the degradation of VL representations and highlights practical approaches to recover inherited VL capabilities. Code is publicly available: https://blind-vla-paper.github.io

## 参考
- http://arxiv.org/abs/2510.25616v1

