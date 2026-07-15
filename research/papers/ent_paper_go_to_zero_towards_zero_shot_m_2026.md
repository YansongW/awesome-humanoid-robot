---
$id: ent_paper_go_to_zero_towards_zero_shot_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data'
  zh: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data'
  ko: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data'
summary:
  en: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data is a paper on Human Motion for humanoid robotics.'
  zh: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data is a paper on Human Motion for humanoid robotics.'
  ko: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data is a paper on Human Motion for humanoid robotics.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- go_to_zero
- human_motion
- humanoid
- motion_synthesis
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.07095v1.
sources:
- id: src_001
  type: website
  title: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data'
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Generating diverse and natural human motion sequences based on textual descriptions constitutes a fundamental and challenging research area within the domains of computer vision, graphics, and robotics. Despite significant advancements in this field, current methodologies often face challenges regarding zero-shot generalization capabilities, largely attributable to the limited size of training datasets. Moreover, the lack of a comprehensive evaluation framework impedes the advancement of this task by failing to identify directions for improvement. In this work, we aim to push text-to-motion into a new era, that is, to achieve the generalization ability of zero-shot. To this end, firstly, we develop an efficient annotation pipeline and introduce MotionMillion-the largest human motion dataset to date, featuring over 2,000 hours and 2 million high-quality motion sequences. Additionally, we propose MotionMillion-Eval, the most comprehensive benchmark for evaluating zero-shot motion generation. Leveraging a scalable architecture, we scale our model to 7B parameters and validate its performance on MotionMillion-Eval. Our results demonstrate strong generalization to out-of-domain and complex compositional motions, marking a significant step toward zero-shot human motion generation. The code is available at https://github.com/VankouF/MotionMillion-Codes.

## 核心内容
Generating diverse and natural human motion sequences based on textual descriptions constitutes a fundamental and challenging research area within the domains of computer vision, graphics, and robotics. Despite significant advancements in this field, current methodologies often face challenges regarding zero-shot generalization capabilities, largely attributable to the limited size of training datasets. Moreover, the lack of a comprehensive evaluation framework impedes the advancement of this task by failing to identify directions for improvement. In this work, we aim to push text-to-motion into a new era, that is, to achieve the generalization ability of zero-shot. To this end, firstly, we develop an efficient annotation pipeline and introduce MotionMillion-the largest human motion dataset to date, featuring over 2,000 hours and 2 million high-quality motion sequences. Additionally, we propose MotionMillion-Eval, the most comprehensive benchmark for evaluating zero-shot motion generation. Leveraging a scalable architecture, we scale our model to 7B parameters and validate its performance on MotionMillion-Eval. Our results demonstrate strong generalization to out-of-domain and complex compositional motions, marking a significant step toward zero-shot human motion generation. The code is available at https://github.com/VankouF/MotionMillion-Codes.

## 参考
- http://arxiv.org/abs/2507.07095v1

