---
$id: ent_paper_zhang_unicod_enhancing_robot_policy_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning'
  zh: UniCoD
  ko: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning'
summary:
  en: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning (UniCoD), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences,
    Tsinghua University, Shanghai Qizhi Institute, Peking University, Shanghai AI Lab.'
  zh: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning (UniCoD), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences,
    Tsinghua University, Shanghai Qizhi Institute, Peking University, Shanghai AI Lab.'
  ko: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning (UniCoD), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences,
    Tsinghua University, Shanghai Qizhi Institute, Peking University, Shanghai AI Lab.'
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
- robotic_manipulation
- unicod
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10642v3.
sources:
- id: src_001
  type: paper
  title: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning (arXiv)'
  url: https://arxiv.org/abs/2510.10642
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UniCoD source
  url: https://doi.org/10.48550/arXiv.2510.10642
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Building generalist robot policies that can handle diverse tasks in open-ended environments is a central challenge in robotics. To leverage knowledge from large-scale pretraining, prior work (VLA) has typically built generalist policies either on top of vision-language understanding models (VLMs) or generative models. However, both semantic understanding from vision-language pretraining and visual dynamics modeling from visual-generation pretraining are crucial for embodied robots. Recent unified models of generation and understanding have demonstrated strong capabilities in both comprehension and generation through large-scale pretraining. We posit that robotic policy learning can likewise benefit from the combined strengths of understanding, planning, and continuous future representation learning. Building on this insight, we introduce UniJEPA, which acquires the ability to dynamically model high-dimensional visual features through pretraining on over 1M internet-scale instructional manipulation videos. Subsequently, UniJEPA is fine-tuned on data collected from the robot embodiment, enabling the learning of mappings from predictive representations to action tokens. Extensive experiments show our approach consistently outperforms baseline methods in terms of 9\% and 12\% across simulation environments and real-world out-of-distribution tasks.

## 核心内容
Building generalist robot policies that can handle diverse tasks in open-ended environments is a central challenge in robotics. To leverage knowledge from large-scale pretraining, prior work (VLA) has typically built generalist policies either on top of vision-language understanding models (VLMs) or generative models. However, both semantic understanding from vision-language pretraining and visual dynamics modeling from visual-generation pretraining are crucial for embodied robots. Recent unified models of generation and understanding have demonstrated strong capabilities in both comprehension and generation through large-scale pretraining. We posit that robotic policy learning can likewise benefit from the combined strengths of understanding, planning, and continuous future representation learning. Building on this insight, we introduce UniJEPA, which acquires the ability to dynamically model high-dimensional visual features through pretraining on over 1M internet-scale instructional manipulation videos. Subsequently, UniJEPA is fine-tuned on data collected from the robot embodiment, enabling the learning of mappings from predictive representations to action tokens. Extensive experiments show our approach consistently outperforms baseline methods in terms of 9\% and 12\% across simulation environments and real-world out-of-distribution tasks.

## 参考
- http://arxiv.org/abs/2510.10642v3

