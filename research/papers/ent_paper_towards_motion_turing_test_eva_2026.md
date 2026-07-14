---
$id: ent_paper_towards_motion_turing_test_eva_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots'
  zh: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots'
  ko: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots'
summary:
  en: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots is a 2026 work on simulation benchmark for
    humanoid robots.'
  zh: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots is a 2026 work on simulation benchmark for
    humanoid robots.'
  ko: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots is a 2026 work on simulation benchmark for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- humanoid
- simulation
- towards_motion_turing_test
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.06181v1.
sources:
- id: src_001
  type: paper
  title: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2603.06181
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have achieved significant progress in motion generation and control, exhibiting movements that appear increasingly natural and human-like. Inspired by the Turing Test, we propose the Motion Turing Test, a framework that evaluates whether human observers can discriminate between humanoid robot and human poses using only kinematic information. To facilitate this evaluation, we present the Human-Humanoid Motion (HHMotion) dataset, which consists of 1,000 motion sequences spanning 15 action categories, performed by 11 humanoid models and 10 human subjects. All motion sequences are converted into SMPL-X representations to eliminate the influence of visual appearance. We recruited 30 annotators to rate the human-likeness of each pose on a 0-5 scale, resulting in over 500 hours of annotation. Analysis of the collected data reveals that humanoid motions still exhibit noticeable deviations from human movements, particularly in dynamic actions such as jumping, boxing, and running. Building on HHMotion, we formulate a human-likeness evaluation task that aims to automatically predict human-likeness scores from motion data. Despite recent progress in multimodal large language models, we find that they remain inadequate for assessing motion human-likeness. To address this, we propose a simple baseline model and demonstrate that it outperforms several contemporary LLM-based methods. The dataset, code, and benchmark will be publicly released to support future research in the community.

## 核心内容
Humanoid robots have achieved significant progress in motion generation and control, exhibiting movements that appear increasingly natural and human-like. Inspired by the Turing Test, we propose the Motion Turing Test, a framework that evaluates whether human observers can discriminate between humanoid robot and human poses using only kinematic information. To facilitate this evaluation, we present the Human-Humanoid Motion (HHMotion) dataset, which consists of 1,000 motion sequences spanning 15 action categories, performed by 11 humanoid models and 10 human subjects. All motion sequences are converted into SMPL-X representations to eliminate the influence of visual appearance. We recruited 30 annotators to rate the human-likeness of each pose on a 0-5 scale, resulting in over 500 hours of annotation. Analysis of the collected data reveals that humanoid motions still exhibit noticeable deviations from human movements, particularly in dynamic actions such as jumping, boxing, and running. Building on HHMotion, we formulate a human-likeness evaluation task that aims to automatically predict human-likeness scores from motion data. Despite recent progress in multimodal large language models, we find that they remain inadequate for assessing motion human-likeness. To address this, we propose a simple baseline model and demonstrate that it outperforms several contemporary LLM-based methods. The dataset, code, and benchmark will be publicly released to support future research in the community.

## 参考
- http://arxiv.org/abs/2603.06181v1

