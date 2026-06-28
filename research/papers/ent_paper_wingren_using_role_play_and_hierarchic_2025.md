---
$id: ent_paper_wingren_using_role_play_and_hierarchic_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Using role-play and Hierarchical Task Analysis for designing human-robot interaction
  zh: 利用角色扮演与层次任务分析设计人机交互
  ko: 인간-로봇 상호작용 설계를 위한 역할극과 계층적 작업 분석 활용
summary:
  en: The paper demonstrates the use of role-play and Hierarchical Task Analysis to
    design a community-pharmacy assistance robot on the Furhat platform, showing how
    expert behavior can be captured, modeled, and implemented for social-robot interaction.
  zh: 本文展示了利用角色扮演与层次任务分析在Furhat平台上设计社区药房辅助机器人，说明如何捕获、建模并实现专家行为以用于社交机器人交互。
  ko: 본 논문은 Furhat 플랫폼에서 커뮤니티 약국 지원 로봇을 설계하기 위해 역할극과 계층적 작업 분석을 적용하여 전문가 행동을 포착, 모델링,
    구현하는 방법을 보여준다.
domains:
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- validation_markets
functional_roles:
- knowledge
tags:
- human_robot_interaction
- social_robot
- service_robot
- hierarchical_task_analysis
- role_play
- furhat
- co_design
- behavior_modeling
- interaction_design
- pharmacy_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from supplied metadata/abstract; full text not independently
    read; requires human review before promotion to verified.; approved by autonomous
    review workflow.
sources:
- id: src_001
  type: paper
  title: Using role-play and Hierarchical Task Analysis for designing human-robot
    interaction
  url: https://arxiv.org/abs/2509.13378
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

The authors argue that role-play and Hierarchical Task Analysis (HTA) are underused in human-robot interaction design, especially for social robots operating in sensitive service contexts. They apply both methods in an ongoing project that develops a robot assistant for a community pharmacy. Pharmacists and customers participate in role-play sessions that provide a controlled, adjustable environment for observing and capturing customer needs and expert behaviors. The captured pharmacist behavior is then modeled with HTA, producing a structured task decomposition that guides robot behavior design.

The HTA results are translated into concrete states implemented on the Furhat social robot platform, enabling the robot to perform medication-counseling interactions. The authors report that role-play let pharmacists act as models for the robot's behavior, while HTA ensured the behavior was modeled correctly and supported co-design among researchers and domain experts. They also identify limitations of existing task-analysis methods for parallel, conditional, and turn-taking social interactions, and call for new task-analysis methods tailored to social robot interaction.

Overall, the work is positioned as a practical, human-centered methodology paper rather than a hardware or algorithm contribution. Its central value lies in demonstrating how well-established human-factors methods can be systematically adapted to social-robot interaction design and co-design practice.

## Key Contributions

- Demonstrate role-play as a practical, controllable method for capturing expert behavior in sensitive service settings.
- Show how Hierarchical Task Analysis can structure and validate robot behavior derived from human expert tasks.
- Provide an example implementation mapping HTA goals to Furhat states for medication counseling.
- Argue for broader adoption of these methods in social robotics design and co-design practice.

## Relevance to Humanoid Robotics

The role-play and HTA workflow is directly transferable to humanoid robots deployed in customer-facing automation, such as retail, hospitality, healthcare, and public services. Humanoid platforms must produce natural, socially acceptable interactions; this paper offers a reusable, human-centered process for eliciting, structuring, and validating the behaviors required in such contexts. The emphasis on co-design with domain experts also helps align robot behavior with real operational and ethical requirements.

For mass-production and deployment of humanoid service robots, the methodology can reduce design risk by grounding interaction logic in observed human expert behavior rather than ad-hoc scripting. Although the paper uses the Furhat head-style robot, the underlying methods—role-play protocols and hierarchical task decomposition—are platform-agnostic and scalable to more complex humanoid embodiments.
