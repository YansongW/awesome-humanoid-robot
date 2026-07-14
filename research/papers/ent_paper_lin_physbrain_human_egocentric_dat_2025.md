---
$id: ent_paper_lin_physbrain_human_egocentric_dat_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence'
  zh: PhysBrain
  ko: 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence'
summary:
  en: 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence (PhysBrain), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    The Hong Kong University of Science and Technology (Guangzhou), Zhongguancun Academy, Zhongguancun Institute of Artificial
    Intelligence, DeepCybo, Harbin Institute of Technology.'
  zh: 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence (PhysBrain), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    The Hong Kong University of Science and Technology (Guangzhou), Zhongguancun Academy, Zhongguancun Institute of Artificial
    Intelligence, DeepCybo, Harbin Institute of Technology.'
  ko: 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence (PhysBrain), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    The Hong Kong University of Science and Technology (Guangzhou), Zhongguancun Academy, Zhongguancun Institute of Artificial
    Intelligence, DeepCybo, Harbin Institute of Technology.'
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
- physbrain
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.16793v2.
sources:
- id: src_001
  type: paper
  title: 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence (arXiv)'
  url: https://arxiv.org/abs/2512.16793
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: PhysBrain source
  url: https://doi.org/10.48550/arXiv.2512.16793
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robotic generalization relies on physical intelligence: the ability to reason about state changes, contact-rich interactions, and long-horizon planning under egocentric perception and action. Vision Language Models (VLMs) are essential to Vision-Language-Action (VLA) systems, but the reliance on third-person training data creates a viewpoint gap for humanoid robots. Collecting massive robot-centric data is an ideal but impractical solution due to cost and diversity constraints. Conversely, human egocentric videos offer a highly scalable data source with rich interaction context, yet the embodiment mismatch prevents the direct application. To bridge this gap, we propose an Egocentric2Embodiment Translation Pipeline that transforms raw human egocentric videos into multi-level, schema-driven embodiment supervision with enforced evidence grounding and temporal consistency, enabling the construction of the Egocentric2Embodiment dataset (E2E-3M) at scale. An egocentric-aware embodied brain, termed PhysBrain, is obtained by training on the E2E-3M dataset. PhysBrain exhibits substantially improved egocentric understanding, particularly for planning. It provides an egocentric-aware initialization that enables more sample-efficient VLA fine-tuning and higher success rates, demonstrating effective transfer from human egocentric supervision to downstream robot control.

## 核心内容
Robotic generalization relies on physical intelligence: the ability to reason about state changes, contact-rich interactions, and long-horizon planning under egocentric perception and action. Vision Language Models (VLMs) are essential to Vision-Language-Action (VLA) systems, but the reliance on third-person training data creates a viewpoint gap for humanoid robots. Collecting massive robot-centric data is an ideal but impractical solution due to cost and diversity constraints. Conversely, human egocentric videos offer a highly scalable data source with rich interaction context, yet the embodiment mismatch prevents the direct application. To bridge this gap, we propose an Egocentric2Embodiment Translation Pipeline that transforms raw human egocentric videos into multi-level, schema-driven embodiment supervision with enforced evidence grounding and temporal consistency, enabling the construction of the Egocentric2Embodiment dataset (E2E-3M) at scale. An egocentric-aware embodied brain, termed PhysBrain, is obtained by training on the E2E-3M dataset. PhysBrain exhibits substantially improved egocentric understanding, particularly for planning. It provides an egocentric-aware initialization that enables more sample-efficient VLA fine-tuning and higher success rates, demonstrating effective transfer from human egocentric supervision to downstream robot control.

## 参考
- http://arxiv.org/abs/2512.16793v2

