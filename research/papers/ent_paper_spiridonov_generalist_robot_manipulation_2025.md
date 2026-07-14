---
$id: ent_paper_spiridonov_generalist_robot_manipulation_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Generalist Robot Manipulation beyond Action Labeled Data
  zh: MotoVLA
  ko: Generalist Robot Manipulation beyond Action Labeled Data
summary:
  en: Generalist Robot Manipulation beyond Action Labeled Data (MotoVLA), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by INSAIT, Sofia University “St. Kliment Ohridski”, ETH Zurich, and published at CoRL25.
  zh: Generalist Robot Manipulation beyond Action Labeled Data (MotoVLA), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by INSAIT, Sofia University “St. Kliment Ohridski”, ETH Zurich, and published at CoRL25.
  ko: Generalist Robot Manipulation beyond Action Labeled Data (MotoVLA), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by INSAIT, Sofia University “St. Kliment Ohridski”, ETH Zurich, and published at CoRL25.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- motovla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19958v1.
sources:
- id: src_001
  type: paper
  title: Generalist Robot Manipulation beyond Action Labeled Data (arXiv)
  url: https://arxiv.org/abs/2509.19958
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MotoVLA source
  url: https://doi.org/10.48550/arXiv.2509.19958
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in generalist robot manipulation leverage pre-trained Vision-Language Models (VLMs) and large-scale robot demonstrations to tackle diverse tasks in a zero-shot manner. A key challenge remains: scaling high-quality, action-labeled robot demonstration data, which existing methods rely on for robustness and generalization. To address this, we propose a method that benefits from videos without action labels - featuring humans and/or robots in action - enhancing open-vocabulary performance and enabling data-efficient learning of new tasks. Our method extracts dense, dynamic 3D point clouds at the hand or gripper location and uses a proposed 3D dynamics predictor for self-supervision. This predictor is then tuned to an action predictor using a smaller labeled dataset for action alignment. We show that our method not only learns from unlabeled human and robot demonstrations - improving downstream generalist robot policies - but also enables robots to learn new tasks without action labels (i.e., out-of-action generalization) in both real-world and simulated settings.

## 核心内容
Recent advances in generalist robot manipulation leverage pre-trained Vision-Language Models (VLMs) and large-scale robot demonstrations to tackle diverse tasks in a zero-shot manner. A key challenge remains: scaling high-quality, action-labeled robot demonstration data, which existing methods rely on for robustness and generalization. To address this, we propose a method that benefits from videos without action labels - featuring humans and/or robots in action - enhancing open-vocabulary performance and enabling data-efficient learning of new tasks. Our method extracts dense, dynamic 3D point clouds at the hand or gripper location and uses a proposed 3D dynamics predictor for self-supervision. This predictor is then tuned to an action predictor using a smaller labeled dataset for action alignment. We show that our method not only learns from unlabeled human and robot demonstrations - improving downstream generalist robot policies - but also enables robots to learn new tasks without action labels (i.e., out-of-action generalization) in both real-world and simulated settings.

## 参考
- http://arxiv.org/abs/2509.19958v1

