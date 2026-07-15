---
$id: ent_paper_zhang_hirt_enhancing_robotic_control_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers'
  zh: HiRT
  ko: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers'
summary:
  en: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers (HiRT), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences, Tsinghua University,
    University of California, Berkeley, Shanghai Qizhi Institute, and published at CoRL 2024.'
  zh: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers (HiRT), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences, Tsinghua University,
    University of California, Berkeley, Shanghai Qizhi Institute, and published at CoRL 2024.'
  ko: 'HiRT: Enhancing Robotic Control with Hierarchical Robot Transformers (HiRT), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences, Tsinghua University,
    University of California, Berkeley, Shanghai Qizhi Institute, and published at CoRL 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hirt
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.05273v3.
sources:
- id: src_001
  type: paper
  title: HiRT source
  url: https://proceedings.mlr.press/v270/zhang25b.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Large Vision-Language-Action (VLA) models, leveraging powerful pre trained Vision-Language Models (VLMs) backends, have shown promise in robotic control due to their impressive generalization ability. However, the success comes at a cost. Their reliance on VLM backends with billions of parameters leads to high computational costs and inference latency, limiting the testing scenarios to mainly quasi-static tasks and hindering performance in dynamic tasks requiring rapid interactions. To address these limitations, this paper proposes HiRT, a Hierarchical Robot Transformer framework that enables flexible frequency and performance trade-off. HiRT keeps VLMs running at low frequencies to capture temporarily invariant features while enabling real-time interaction through a high-frequency vision-based policy guided by the slowly updated features. Experiment results in both simulation and real-world settings demonstrate significant improvements over baseline methods. Empirically, in static tasks, we double the control frequency and achieve comparable success rates. Additionally, on novel real-world dynamic ma nipulation tasks which are challenging for previous VLA models, HiRT improves the success rate from 48% to 75%.

## 核心内容
Large Vision-Language-Action (VLA) models, leveraging powerful pre trained Vision-Language Models (VLMs) backends, have shown promise in robotic control due to their impressive generalization ability. However, the success comes at a cost. Their reliance on VLM backends with billions of parameters leads to high computational costs and inference latency, limiting the testing scenarios to mainly quasi-static tasks and hindering performance in dynamic tasks requiring rapid interactions. To address these limitations, this paper proposes HiRT, a Hierarchical Robot Transformer framework that enables flexible frequency and performance trade-off. HiRT keeps VLMs running at low frequencies to capture temporarily invariant features while enabling real-time interaction through a high-frequency vision-based policy guided by the slowly updated features. Experiment results in both simulation and real-world settings demonstrate significant improvements over baseline methods. Empirically, in static tasks, we double the control frequency and achieve comparable success rates. Additionally, on novel real-world dynamic ma nipulation tasks which are challenging for previous VLA models, HiRT improves the success rate from 48% to 75%.

## 参考
- http://arxiv.org/abs/2410.05273v3

