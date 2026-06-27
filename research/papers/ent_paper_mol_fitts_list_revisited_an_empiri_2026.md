---
$id: ent_paper_mol_fitts_list_revisited_an_empiri_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Fitts'' List Revisited: An Empirical Study on Function Allocation in a Two-Agent
    Physical Human-Robot Collaborative Position/Force Task'
  zh: 重新审视菲茨列表：双主体物理人机协作位置/力任务中功能分配的实证研究
  ko: '피츠 목록 재검토: 이중 주체 물리적 인간-로봇 협업 위치/력 작업에서 기능 할당에 대한 실증 연구'
summary:
  en: Empirically evaluates Fitts' List by allocating position and force control between
    a human and a robot in an abstract blending task, showing that assigning position
    control to the human and force control to the robot improves performance and user
    acceptance.
  zh: 在抽象混合任务中实证评估人机位置与力控制分配对菲茨列表的适用性，发现将位置控制分配给人、力控制分配给机器人可提升性能与用户接受度。
  ko: 추상적 블렌딩 작업에서 인간과 로봇 간 위치 및 힘 제어 할당을 통해 피츠 목록을 실증적으로 평가하였으며, 위치 제어를 인간에게, 힘 제어를
    로봇에게 할당할 때 성능과 사용자 수용도가 향상됨을 보임.
domains:
- 05_mass_production
- 04_assembly_integration_testing
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- physical_human_robot_collaboration
- function_allocation
- fitts_list
- maba_maba
- shared_control
- position_force_control
- human_robot_interaction
- industry_5_0
- blending_task
- user_study
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided abstract and metadata; full-text human review
    is recommended before final verification.
sources:
- id: src_001
  type: paper
  title: 'Fitts'' List Revisited: An Empirical Study on Function Allocation in a Two-Agent
    Physical Human-Robot Collaborative Position/Force Task'
  url: https://arxiv.org/abs/2505.04722
  date: '2026'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2025.3632607
theoretical_depth:
- method
---

## Overview

This letter investigates the classical problem of function allocation—assigning control tasks to either a human or a machine—in the context of physical Human-Robot Collaboration (pHRC). The authors conducted a within-subject user study with 26 participants to evaluate four distinct static allocations of position and force control (human-human HH, human-robot HR, robot-human RH, robot-robot RR) in an abstract blending task. Objective performance metrics and subjective questionnaires were used to compare the conditions and to test whether Fitts' List, also known as the MABA-MABA principle, applies to pHRC.

The results indicate that allocating position control to the human and force control to the robot (HR) significantly reduced overblending compared with the opposite allocation (RH). Participants also rated this condition lower in physical demand and higher in overall system acceptance, autonomy, and engagement. Surprisingly, the supervisory role in which the robot controlled both position and force (RR) was rated second best in subjective acceptance. The study further reveals that delegating position control to the robot reduced perceived autonomy substantially more than delegating force control to the robot, highlighting nuanced user-experience trade-offs.

## Key Contributions

- Empirically validates that Fitts' classical MABA-MABA principle applies to static function allocation in physical human-robot collaboration.
- Demonstrates that allocating position control to the human and force control to the robot (HR) yields lower overblending, lower physical demand, and higher subjective acceptance than the reverse allocation (RH).
- Reveals that delegating position control to the robot reduces perceived autonomy substantially more than delegating force control to the robot.
- Finds that a supervisory role in which the robot controls both position and force ranks second in subjective acceptance despite high objective performance.
- Provides new user-experience insights on autonomy, competence, engagement, and usefulness across different position/force distributions.

## Relevance to Humanoid Robotics

For humanoid robots deployed in mass-production and industrial assembly, the results provide evidence-based guidance on how to statically allocate position and force control between human workers and robots. Because humanoids must physically interact with humans in shared workspaces, understanding which control modality should remain with the human is critical for acceptance and performance. The finding that position control is better retained by the human while force control can be delegated to the robot is directly transferable to assembly, blending, polishing, and insertion tasks in humanoid manufacturing cells.
