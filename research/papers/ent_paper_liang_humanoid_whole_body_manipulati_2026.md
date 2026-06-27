---
$id: ent_paper_liang_humanoid_whole_body_manipulati_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable
    Action Cerebellum
  zh: 通过主动空间脑和可泛化动作小脑实现人形全身操作
  ko: 능동 공간 뇌와 일반화 가능한 동작 소뇌를 통한 휴머노이드 전신 조작
summary:
  en: This paper proposes a multi-agent framework—Active Spatial Brain for active
    spatial perception and planning, and Generalizable Action Cerebellum for decoupled
    lower-body locomotion and upper-body dexterous manipulation—that enables spatial-aware
    humanoid whole-body manipulation without task-specific real-robot data. It is
    validated on a spatial intelligence benchmark and on a real Unitree G1 humanoid
    robot.
  zh: 本文提出了一种多智能体框架——主动空间脑负责主动空间感知与规划，可泛化动作小脑负责解耦的下肢移动与上肢灵巧操作——无需任务特定的真实机器人数据即可实现空间感知的人形全身操作，并在空间智能基准与真实Unitree
    G1人形机器人上进行了验证。
  ko: 본 논문은 능동 공간 지각 및 계획을 담당하는 능동 공간 뇌와 하지 이동·상지 정교 조작으로 분리된 일반화 가능한 동작 소뇌를 결합한 다중
    에이전트 프레임워크를 제안하여, 작업별 실제 로봇 데이터 없이 공간 인식형 휴머노이드 전신 조작을 수행하고 공간 지능 벤치마크와 실제 Unitree
    G1 휴머노이드 로봇으로 검증한다.
domains:
- 07_ai_models_algorithms
- 10_evaluation_benchmarks
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- whole_body_manipulation
- loco_manipulation
- vlm
- active_perception
- spatial_reasoning
- dexterous_manipulation
- unitree_g1
- reinforcement_learning
- generalizable_policy
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from supplied metadata; full paper was not accessed, so hardware
    details, benchmark design, and exact citations require human review.
sources:
- id: src_001
  type: paper
  title: Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable
    Action Cerebellum
  url: https://arxiv.org/abs/2605.21133
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## Overview

The paper targets spatial-aware humanoid whole-body manipulation in complex 3D environments. It identifies two core obstacles: understanding diverse spatial relations from limited 2D observations, and generalizing action policies when real-robot data are scarce and expensive. To overcome these, the authors present a two-part framework driven by multi-agent large models.

The Active Spatial Brain actively perceives the scene through a controllable camera neck and a memory bank, then performs task planning and adaptive replanning. The Generalizable Action Cerebellum converts these decisions into executable whole-body motions by decoupling control into a lower-body locomotion agent and an upper-body dexterous manipulation agent. The locomotion agent combines obstacle-aware A* navigation, an end-effector reachable-space solver, and reinforcement-learning-based tracking, while the manipulation agent uses foundation-model grasp generation followed by parametric post-grasp primitives. Importantly, the framework is designed to avoid task-specific real-robot training data.

Evaluation is carried out in two parts: a Spatial Intelligence Benchmark for Manipulation Tasks that tests 3D spatial reasoning, active perception, and waypoint generation, and real-robot experiments on a Unitree G1 equipped with INSPIRE-ROBOTS RH56DFTP hands and an Intel RealSense D435i RGB-D camera mounted on a 2-DoF active neck. The reported results show strong performance across varied tasks and environments, with better generalization than data-driven and pure VLM baselines.

## Key Contributions

- Coupled Active Spatial Brain and Generalizable Action Cerebellum architecture for generalizable humanoid whole-body manipulation.
- Active spatial perception using a controllable camera neck, a memory bank, and closed-loop adaptive task planning and replanning.
- Decoupled lower-body locomotion (obstacle-aware A* navigation, end-effector reachable-space solver, RL-based tracking) and upper-body manipulation (foundation-model grasp generation and parametric post-grasp primitives).
- A spatial intelligence benchmark evaluating 3D spatial reasoning, active perception, and waypoint generation, alongside real-robot task evaluations.
- Real-robot demonstration on a Unitree G1 showing stronger generalization than data-driven and VLM baselines without task-specific real-robot training data.

## Relevance to Humanoid Robotics

By enabling generalizable whole-body manipulation without collecting task-specific real-robot data, the framework directly lowers the data-cost barrier that limits scalable deployment of humanoid robots. Its emphasis on spatial reasoning and active perception also improves adaptability to unstructured 3D environments, which is important for industrial and service applications of humanoids.
