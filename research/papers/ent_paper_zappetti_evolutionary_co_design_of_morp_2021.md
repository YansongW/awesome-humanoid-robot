---
$id: ent_paper_zappetti_evolutionary_co_design_of_morp_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Evolutionary Co-Design of Morphology and Control of Soft Tensegrity Modular
    Robots with Programmable Stiffness
  zh: 具有可编程刚度的软体张拉整体模块化机器人形态与控制的进化协同设计
  ko: 프로그래머블 강성을 가진 연체 텐세그리티 모듈 로봇의 형태와 제어 공동 진화
summary:
  en: This paper proposes easy-to-assemble, actuated tensegrity modules with programmable
    stiffness and applies body-brain co-evolution in the TensSoft platform to demonstrate
    that module stiffness strongly influences the evolved morphology, control policy,
    and locomotion strategy.
  zh: 本文提出易于组装且具有可编程刚度的驱动张拉整体模块，并在TensSoft平台上采用形体-控制协同进化方法，证明模块刚度会显著影响进化出的机器人形态、控制策略和运动模式。
  ko: 본 논문은 조립이 용이하고 프로그래머블 강성을 가진 구동식 텐세그리티 모듈을 제안하고, TensSoft 플랫폼에서 바디-브레인 공진화를
    적용하여 모듈 강성이 진화된 형태, 제어 정책, 이동 전략에 큰 영향을 미침을 보인다.
domains:
- 06_design_engineering
- 02_components
layers:
- upstream
- midstream
- intelligence
functional_roles:
- knowledge
tags:
- tensegrity
- modular_robot
- programmable_stiffness
- body_brain_coevolution
- evolutionary_design
- soft_robotics
- icosahedron_module
- ntrt
- galib
- simulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from full-text PDF of the arXiv preprint; awaits human review
    before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Evolutionary Co-Design of Morphology and Control of Soft Tensegrity Modular
    Robots with Programmable Stiffness
  url: https://arxiv.org/abs/2101.11772
  date: '2021'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Tensegrity structures combine rigid struts and elastic cables into lightweight systems that can undergo large deformations while remaining robust. These properties make them attractive for soft robotics, yet designing the morphology, control, assembly, actuation, and stiffness of tensegrity robots remains difficult. Zappetti, Bejjani, and Floreano address this by proposing a modular approach based on 3D-printed, easy-to-assemble icosahedron tensegrity modules whose cable stiffness can be programmed and whose motion is driven by internal tendon-driven servo actuators.

The authors introduce TensSoft, a body-brain co-evolution platform layered on NASA's NTRT simulator and the GAlib 2.4 genetic-algorithm library. The platform co-evolves the number of modules, their connection orientations, the actuation direction of each module, and the amplitude, frequency, and phase of open-loop sawtooth control signals. Fitness is defined as the distance traveled in 10 seconds on flat ground. The authors compare two uniform stiffness values (high stiffness = 4x low stiffness, both in the 10–100 MPa elastic range). Evolution with high-stiffness modules consistently produces longer robots of 6–8 modules that move with caterpillar-like peristaltic locomotion, whereas evolution with low-stiffness modules favors compact 2–3-module robots that hop or roll on their side. The study therefore demonstrates that stiffness is a critical design parameter that shapes the emerged morphology, control, and gait.

All results are obtained in simulation; no physical robot is built or validated in this work. The experiments also keep stiffness uniform across modules and use only open-loop sawtooth signals without sensory feedback.

## Key Contributions

- A modular tensegrity robot design using 3D-printed, easy-to-assemble icosahedron modules with programmable cable stiffness and internal tendon-driven servo actuation.
- The TensSoft body-brain co-evolution platform, built on the NASA Tensegrity Robotics Toolkit (NTRT) and the GAlib 2.4 genetic-algorithm library.
- Empirical evidence that module stiffness strongly influences evolved morphology, control policy, and locomotion strategy.
- Discovery of distinct stiffness-dependent gaits: caterpillar-like peristaltic locomotion for high-stiffness robots versus hopping or rolling for low-stiffness robots.

## Relevance to Humanoid Robotics

Programmable-stiffness modular tensegrity units offer lightweight, deformable, and robust compliant-body building blocks. In principle, such modules could inform the design of safe, low-cost limbs or subsystems for humanoid robots that must interact with unstructured or human-centric environments. However, the paper does not address bipedal humanoid hardware, torque-driven joints, or whole-body balance; its direct contribution is to soft modular robotics and evolutionary design methodology rather than to humanoid platforms.
