---
$id: ent_paper_wang_vlm_see_robot_do_human_demo_vi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model'
  zh: SeeDo
  ko: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model'
summary:
  en: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model (SeeDo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by New York University, and published at IROS25.'
  zh: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model (SeeDo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by New York University, and published at IROS25.'
  ko: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model (SeeDo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by New York University, and published at IROS25.'
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
- seedo
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.08792v2.
sources:
- id: src_001
  type: website
  title: SeeDo source
  url: https://doi.org/10.1109/IROS60139.2025.11246682
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision Language Models (VLMs) have recently been adopted in robotics for their capability in common sense reasoning and generalizability. Existing work has applied VLMs to generate task and motion planning from natural language instructions and simulate training data for robot learning. In this work, we explore using VLM to interpret human demonstration videos and generate robot task planning. Our method integrates keyframe selection, visual perception, and VLM reasoning into a pipeline. We named it SeeDo because it enables the VLM to ''see'' human demonstrations and explain the corresponding plans to the robot for it to ''do''. To validate our approach, we collected a set of long-horizon human videos demonstrating pick-and-place tasks in three diverse categories and designed a set of metrics to comprehensively benchmark SeeDo against several baselines, including state-of-the-art video-input VLMs. The experiments demonstrate SeeDo's superior performance. We further deployed the generated task plans in both a simulation environment and on a real robot arm.

## 核心内容
Vision Language Models (VLMs) have recently been adopted in robotics for their capability in common sense reasoning and generalizability. Existing work has applied VLMs to generate task and motion planning from natural language instructions and simulate training data for robot learning. In this work, we explore using VLM to interpret human demonstration videos and generate robot task planning. Our method integrates keyframe selection, visual perception, and VLM reasoning into a pipeline. We named it SeeDo because it enables the VLM to ''see'' human demonstrations and explain the corresponding plans to the robot for it to ''do''. To validate our approach, we collected a set of long-horizon human videos demonstrating pick-and-place tasks in three diverse categories and designed a set of metrics to comprehensively benchmark SeeDo against several baselines, including state-of-the-art video-input VLMs. The experiments demonstrate SeeDo's superior performance. We further deployed the generated task plans in both a simulation environment and on a real robot arm.

## 参考
- http://arxiv.org/abs/2410.08792v2

