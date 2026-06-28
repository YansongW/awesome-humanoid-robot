---
$id: ent_paper_ramadurai_effect_of_human_involvement_on_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Effect of Human Involvement on Work Performance and Fluency in Human-Robot Collaboration
    for Recycling
  zh: 人类参与对回收中人机协作工作性能与流畅性的影响
  ko: 재활용을 위한 인간-로봇 협업에서 인간 참여가 작업 수행 및 유동성에 미치는 영향
summary:
  en: A within-subjects study with six participants and a UR3e cobot shows that increasing
    human assistance in occlusion removal, spacing, and grip selection raises robot
    sorting accuracy from 33.3% to 100% and improves subjective fluency in a recyclable
    cup sorting task.
  zh: 一项包含6名参与者与UR3e协作机器人的被试内研究表明，在遮挡移除、间距优化和夹持选择中增加人类辅助，可将可回收杯子分拣任务的机器人准确率从33.3%提升至100%，并改善主观流畅性。
  ko: 6명의 참가자와 UR3e 협동로봇을 대상으로 한 피험자내 연구는, 가림 제거, 간격 최적화 및 그립 선택에서 인간 보조를 늘리면 재활용
    컵 분류 작업의 로봇 정확도가 33.3%에서 100%로 향상되고 주관적 유동성이 개선됨을 보여준다.
domains:
- 11_applications_markets
- 02_components
- 07_ai_models_algorithms
- 03_manufacturing_processes
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
tags:
- human_robot_collaboration
- recycling
- cobot
- vision_guided_grasping
- sorting
- task_fluency
- human_in_the_loop
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; full-text verification
    and human review are recommended before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Effect of Human Involvement on Work Performance and Fluency in Human-Robot
    Collaboration for Recycling
  url: https://arxiv.org/abs/2201.07990
  date: '2022'
  accessed_at: '2026-06-26'
---

## Overview

This paper investigates how different levels of human assistance affect performance and subjective fluency in a human-robot collaborative recycling task. Six participants worked with a UR3e collaborative robot arm fitted with an OnRobot 2FG7 gripper and an OnRobot Eyes vision system to sort plastic cups mixed with non-recyclable distractors. The experiment used a within-subjects factorial design with three human-involvement levels—Level 1 occlusion removal, Level 2 optimal spacing, and Level 3 optimal grip—and two proportions of recyclables.

The results show a clear monotonic relationship between human involvement and robot accuracy. Mean accuracy improved from 33.3% at Level 1 to 69% at Level 2 and reached 100% at Level 3. Subjective fluency, measured through participant-reported ratings, also increased with higher human involvement. The authors further analyze how human time and robot time are influenced by the interaction between involvement level and recyclables proportion, finding that human time depends on both factors whereas robot time is driven primarily by the percentage of recyclables.

The authors argue that human-robot collaboration can be a practical, cost-effective alternative to full automation for recycling sortation, especially when waste streams are highly heterogeneous in size, shape, and composition. The work emphasizes that strategic human assistance in perception and grasp planning can substantially improve robot reliability without requiring more complex autonomous systems.

## Key Contributions

- Demonstrated that robot accuracy rises monotonically with human involvement, from 33.3% (occlusion removal) to 69% (optimal spacing) and 100% (optimal grip).
- Showed that subjective human-robot fluency increases with higher human involvement, likely tied to team success.
- Identified that human time depends on the interaction between involvement level and percentage of recyclables, while robot time depends mainly on recyclables proportion.
- Provided empirical evidence that human-robot collaboration can be a cost-effective alternative to full automation for recycling sortation.

## Relevance to Humanoid Robotics

Although the study uses a fixed-base robot arm rather than a full humanoid, its findings are directly relevant to future humanoid deployment in unstructured industrial settings. Recycling and material handling require operation alongside people in cluttered, variable environments, and the paper quantifies how human assistance in perception and grasping can raise system accuracy and fluency.

For humanoid robots, the results support the design of shared-autonomy and human-in-the-loop behaviors: a humanoid can offload uncertain vision and grasp decisions to nearby workers, improving robustness while maintaining safe, fluent collaboration. The metrics and task structure also offer a template for benchmarking humanoid assistance in logistics and waste-management applications.
