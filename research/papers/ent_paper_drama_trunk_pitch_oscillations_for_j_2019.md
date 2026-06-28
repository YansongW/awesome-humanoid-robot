---
$id: ent_paper_drama_trunk_pitch_oscillations_for_j_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Trunk Pitch Oscillations for Joint Load Redistribution in Humans and Humanoid
    Robots
  zh: 人类与仿人机器人中躯干俯仰振荡对关节负载重分配的影响
  ko: 인간과 휴머노이드 로봇에서의 관절 하중 재분배를 위한 몸통 피치 진동
summary:
  en: This 2019 arXiv paper by Drama and Badri-Spröwitz uses a trunk-equipped spring-loaded
    inverted pendulum (TSLIP) model with a virtual point target to generate and analyze
    trunk pitch oscillations, showing that a virtual point below the center of mass
    can reproduce forward trunk pitching in human running and redistribute joint work
    between hip and leg.
  zh: Drama与Badri-Spröwitz于2019年发表于arXiv的论文，使用带躯干的弹簧负载倒立摆（TSLIP）模型与虚拟点目标生成并分析躯干俯仰振荡，证明位于质心下方的虚拟点可复现人类跑步中的前向躯干俯仰，并在髋关节与腿部之间重新分配关节做功。
  ko: Drama와 Badri-Spröwitz의 2019년 arXiv 논문은 몸통이 있는 스프링 로드 인버티드 펜듈럼(TSLIP) 모델과 가상점(VP)
    목표를 사용하여 몸통 피치 진동을 생성하고 분석하며, 질량 중심 아래의 가상점이 인간 달리기에서 관찰되는 전방 몸통 피치를 설명하고 고관절과
    다리 사이의 관절 일을 재분배할 수 있음을 보여준다.
domains:
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- humanoid_running
- trunk_oscillation
- spring_loaded_inverted_pendulum
- virtual_point_control
- gait_generation
- joint_load_redistribution
- bipedal_locomotion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full paper not independently read.
    Claims should be cross-checked against the PDF before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Trunk Pitch Oscillations for Joint Load Redistribution in Humans and Humanoid
    Robots
  url: https://arxiv.org/abs/1909.03687
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

The paper addresses the difficulty of creating natural-looking running gaits for humanoid robots, especially the underactuated trunk degree of freedom. It proposes a trunk-equipped spring-loaded inverted pendulum (TSLIP) model combined with a virtual point (VP) target to generate trunk pitch oscillations. The VP location and running speed are varied to study their effects on trunk pitching direction, angular excursion, and joint loading.

The authors find that placing the VP above the center of mass (CoM) produces backward trunk pitching, whereas placing it below the CoM produces forward trunk pitching similar to human running. Larger VP radii below the CoM lead to greater trunk angular excursions and can reduce leg loading through synergistic hip-leg work, but at the cost of increased peak hip torque. The work also introduces a bilinear leg damper to produce smooth, human-like ground reaction force profiles within the TSLIP framework.

Overall, the study frames trunk oscillation not merely as a cosmetic feature of human gait but as a functional mechanism for joint load redistribution, with direct implications for humanoid robot control design.

## Key Contributions

- Demonstrates that a virtual point (VP) above the CoM yields backward trunk pitching, while a VP below the CoM yields forward trunk pitching consistent with human running.
- Shows that VP-below-CoM placement produces larger trunk angular excursions than VP-above-CoM placement for the same VP radius.
- Finds that trunk angular excursion and mean trunk angular velocity increase with forward running speed when the VP target is held fixed.
- Introduces a bilinear leg damper to obtain smooth, human-like ground reaction force profiles in the TSLIP model.
- Reveals a control trade-off: VP below the CoM reduces leg loading and net hip work but increases peak hip torque, informing humanoid motor sizing and gait design.

## Relevance to Humanoid Robotics

The paper is directly relevant to humanoid robotics because it provides a template-based control principle for generating natural trunk oscillations in bipedal running. By relating VP placement to trunk pitching and joint loading, it offers a design guideline for redistributing work between hip and leg actuators. This can help address motor torque limits, improve energetic economy, and produce more human-like gaits in humanoid robots.
