---
$id: ent_paper_scaling_large_motion_models_wi_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Scaling Large Motion Models with Million-Level Human Motions
  zh: Scaling Large Motion Models with Million-Level Human Motions
  ko: Scaling Large Motion Models with Million-Level Human Motions
summary:
  en: Scaling Large Motion Models with Million-Level Human Motions is a 2024 work on human motion analysis and synthesis for
    humanoid robots.
  zh: Scaling Large Motion Models with Million-Level Human Motions is a 2024 work on human motion analysis and synthesis for
    humanoid robots.
  ko: Scaling Large Motion Models with Million-Level Human Motions is a 2024 work on human motion analysis and synthesis for
    humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- motion_analysis
- motion_synthesis
- scaling_large_motion_models_wi
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.03311v3.
sources:
- id: src_001
  type: paper
  title: Scaling Large Motion Models with Million-Level Human Motions (arXiv)
  url: https://arxiv.org/abs/2410.03311
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Inspired by the recent success of LLMs, the field of human motion understanding has increasingly shifted toward developing large motion models. Despite some progress, current efforts remain far from achieving truly generalist models, primarily due to the lack of massive high-quality data. To address this gap, we present MotionLib, the first million-level dataset for motion generation, which is at least 15$\times$ larger than existing counterparts and enriched with hierarchical text descriptions. Using MotionLib, we train a large motion model named \projname, demonstrating robust performance across a wide range of human activities, including unseen ones. Through systematic investigation, for the first time, we highlight the importance of scaling both data and model size for advancing motion generation, along with key insights to achieve this goal. To better integrate the motion modality, we propose Motionbook, an innovative motion encoding approach including (1) a compact yet lossless feature to represent motions; (2) a novel 2D lookup-free motion tokenizer that preserves fine-grained motion details while expanding codebook capacity, significantly enhancing the representational power of motion tokens. We believe this work lays the groundwork for developing more versatile and powerful motion generation models in the future. For further details, visit https://beingbeyond.github.io/Being-M0/.

## 核心内容
Inspired by the recent success of LLMs, the field of human motion understanding has increasingly shifted toward developing large motion models. Despite some progress, current efforts remain far from achieving truly generalist models, primarily due to the lack of massive high-quality data. To address this gap, we present MotionLib, the first million-level dataset for motion generation, which is at least 15$\times$ larger than existing counterparts and enriched with hierarchical text descriptions. Using MotionLib, we train a large motion model named \projname, demonstrating robust performance across a wide range of human activities, including unseen ones. Through systematic investigation, for the first time, we highlight the importance of scaling both data and model size for advancing motion generation, along with key insights to achieve this goal. To better integrate the motion modality, we propose Motionbook, an innovative motion encoding approach including (1) a compact yet lossless feature to represent motions; (2) a novel 2D lookup-free motion tokenizer that preserves fine-grained motion details while expanding codebook capacity, significantly enhancing the representational power of motion tokens. We believe this work lays the groundwork for developing more versatile and powerful motion generation models in the future. For further details, visit https://beingbeyond.github.io/Being-M0/.

## 参考
- http://arxiv.org/abs/2410.03311v3

