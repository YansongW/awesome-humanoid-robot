---
$id: ent_paper_leverb_humanoid_whole_body_con_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction'
  zh: LeVERB｜具有潜在视觉语言指令的人形全身控制
  ko: 'LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction'
summary:
  en: 'Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet
    most existing systems assume an accurate low-level controller with hand-crafted action"vocabulary"such as end-effector
    pose or root velocity. This assumption confines prior work to quasi-static tasks and precludes the agile, whole-body behaviors
    required by humanoid whole-body control (WBC) tasks. To capture this gap in the literature, we start by introducing the
    first sim-to-real-ready, vision-language, closed-loop benchmark for humanoid WBC, comprising over 150 tasks from 10 categories.
    We then propose LeVERB: Latent Vision-Language-Encoded Robot Behavior, a hierarchical latent instruction-following framework
    for humanoid vision-language WBC, the first of its kind. At the'
  zh: LeVERB 的实现路径是先把语言指令、相机图像/多视角观测、仿真交互数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、潜变量/动作 token预测全身轨迹/动作序列、动作 chunk/token、低层控制器目标。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  ko: LeVERB 的实现路径是先把语言指令、相机图像/多视角观测、仿真交互数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、潜变量/动作 token预测全身轨迹/动作序列、动作 chunk/token、低层控制器目标。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- contact_planning
- leverb
- mobile_manipulation
- task_planning
- visual_closed_loop
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: LeVERB: Humanoid Whole-Body
    Control with Latent Vision-Language Instruction.'
sources:
- id: src_001
  type: website
  title: LeVERB project page
  url: https://github.com/ember-lab-berkeley/LeVERB-Website
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet most existing systems assume an accurate low-level controller with hand-crafted action"vocabulary"such as end-effector pose or root velocity. This assumption confines prior work to quasi-static tasks and precludes the agile, whole-body behaviors required by humanoid whole-body control (WBC) tasks. To capture this gap in the literature, we start by introducing the first sim-to-real-ready, vision-language, closed-loop benchmark for humanoid WBC, comprising over 150 tasks from 10 categories. We then propose LeVERB: Latent Vision-Language-Encoded Robot Behavior, a hierarchical latent instruction-following framework for humanoid vision-language WBC, the first of its kind. At the top level, a vision-language policy learns a latent action vocabulary from synthetically rendered kinematic demonstrations; at the low level, a reinforcement-learned WBC policy consumes these latent verbs to generate dynamics-level commands. In our benchmark, LeVERB can zero-shot attain a 80% success rate on simple visual navigation tasks, and 58.5% success rate overall, outperforming naive hierarchical whole-body VLA implementation by 7.8 times.

## 核心内容
Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet most existing systems assume an accurate low-level controller with hand-crafted action"vocabulary"such as end-effector pose or root velocity. This assumption confines prior work to quasi-static tasks and precludes the agile, whole-body behaviors required by humanoid whole-body control (WBC) tasks. To capture this gap in the literature, we start by introducing the first sim-to-real-ready, vision-language, closed-loop benchmark for humanoid WBC, comprising over 150 tasks from 10 categories. We then propose LeVERB: Latent Vision-Language-Encoded Robot Behavior, a hierarchical latent instruction-following framework for humanoid vision-language WBC, the first of its kind. At the top level, a vision-language policy learns a latent action vocabulary from synthetically rendered kinematic demonstrations; at the low level, a reinforcement-learned WBC policy consumes these latent verbs to generate dynamics-level commands. In our benchmark, LeVERB can zero-shot attain a 80% success rate on simple visual navigation tasks, and 58.5% success rate overall, outperforming naive hierarchical whole-body VLA implementation by 7.8 times.

## 参考
- Semantic Scholar search: LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction

