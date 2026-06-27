---
$id: ent_paper_prasad_geometric_mechanics_of_contact_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Geometric Mechanics of Contact-Switching Systems
  zh: 接触切换系统的几何力学
  ko: 접촉 전환 시스템의 기하학적 역학
summary:
  en: This paper introduces a geometric-mechanics framework for legged locomotion
    that combines continuous limb angles with discrete contact states in a hybrid
    shape-space, and defines stratified panels to optimize gaits across contact modes.
  zh: 本文提出了一种用于腿式运动的几何力学框架，将连续肢体角度与离散接触状态结合在混合形状空间中，并定义分层面板以跨接触模式优化步态。
  ko: 본 논문은 연속적인 사지 각도와 이산적인 접촉 상태를 하이브리드 형상 공간에 결합하여 보행 운동을 위한 기하학적 역학 프레임워크를 제안하고,
    접촉 모드 간 보행 최적화를 위해 계층화된 패널을 정의한다.
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- geometric_mechanics
- contact_switching
- legged_locomotion
- gait_optimization
- hybrid_shape_space
- stratified_panels
- quasistatic_locomotion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full text not independently
    reviewed. Citation locations are approximate and require human verification before
    promotion.
sources:
- id: src_001
  type: paper
  title: Geometric Mechanics of Contact-Switching Systems
  url: https://arxiv.org/abs/2306.10276
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- formalism
- method
---

## Overview

Legged robots repeatedly make and break contact with the ground, producing hybrid dynamics that classical geometric-mechanics tools do not directly capture. This work models such systems using a hybrid shape-space that contains continuous limb-angle coordinates together with a discrete set of contact states. By extending the generalized Stokes' theorem to this hybrid setting, the authors introduce stratified panels—discrete curvature-like functions that quantify how infinitesimal shape variations in one contact mode couple to displacement after a switch to another mode. The framework is demonstrated on planar toy robots with two and three feet, and on a model with diametrically coupled legs driven by rate-limited servo motors.

The stratified-panel representation allows average body displacement to be estimated from a gait that spans multiple contact modes, without simulating the full hybrid dynamics. The authors formulate a locomotion-effectiveness cost and use it to optimize gaits subject to constraints such as allowable contact sequences and actuator limits. They also show how complex multi-contact gaits can be reduced to simpler, interpretable sequences, suggesting scalability to multilegged systems.

## Key Contributions

- Introduces a geometric-mechanics modeling framework for hybrid shape-spaces that combine continuous limb angles with discrete contact states.
- Defines stratified panels as discrete curvature functions derived via generalized Stokes' theorem to encode displacement strength across contact-switching submanifolds.
- Demonstrates optimal gait generation for contact-switching systems using a locomotion-effectiveness cost function and system constraints.
- Extends the approach to multi-footed planar models and performs gait reduction on complex gaits spanning multiple contact modes.

## Relevance to Humanoid Robotics

Humanoid walking is fundamentally a contact-switching process: each step involves deliberate foot placement, single-support and double-support phases, and discrete transitions between them. The paper's hybrid shape-space and stratified-panel formalism provide a low-dimensional, geometrically principled way to represent and optimize such gaits. Although the toy models are far simpler than full humanoids, the concepts of contact-mode decomposition, gait reduction, and locomotion-effectiveness optimization are directly transferable to humanoid gait planning and footstep selection. The framework can inform the design of motion planners and low-level controllers that must respect discrete contact constraints while achieving continuous body motion.
