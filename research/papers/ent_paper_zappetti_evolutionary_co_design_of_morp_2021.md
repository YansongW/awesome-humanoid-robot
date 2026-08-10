---
$id: ent_paper_zappetti_evolutionary_co_design_of_morp_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Evolutionary Co-Design of Morphology and Control of Soft Tensegrity Modular Robots with Programmable Stiffness
  zh: 具有可编程刚度的软体张拉整体模块化机器人形态与控制的进化协同设计
  ko: 프로그래머블 강성을 가진 연체 텐세그리티 모듈 로봇의 형태와 제어 공동 진화
summary:
  en: This paper proposes easy-to-assemble, actuated tensegrity modules with programmable stiffness and applies body-brain
    co-evolution in the TensSoft platform to demonstrate that module stiffness strongly influences the evolved morphology,
    control policy, and locomotion strategy.
  zh: 本文提出一种易于组装、刚度可编程的软张拉整体模块，并在TensSoft平台上通过形态与控制协同进化，证明模块刚度显著影响进化出的形态、控制策略和运动方式。
  ko: 본 논문은 조립이 용이하고 프로그래머블 강성을 가진 구동식 텐세그리티 모듈을 제안하고, TensSoft 플랫폼에서 바디-브레인 공진화를 적용하여 모듈 강성이 진화된 형태, 제어 정책, 이동 전략에 큰 영향을
    미침을 보인다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2101.11772v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (624 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Evolutionary Co-Design of Morphology and Control of Soft Tensegrity Modular Robots with Programmable Stiffness
  url: https://arxiv.org/abs/2101.11772
  date: '2021'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
张拉整体结构具有轻质、大变形和强鲁棒性等独特优势，但现有张拉整体机器人在形态设计、控制、组装和驱动方面仍面临挑战，且刚度常被忽视。本文通过引入可编程刚度的驱动模块，结合身体-大脑协同进化方法，在TensSoft平台上自动设计软张拉整体模块机器人。实验表明，模块刚度是决定进化结果的关键参数，不同刚度会引导出截然不同的形态、控制策略和运动模式。

## 核心内容
### 方法
- 提出**可编程刚度驱动模块**：模块采用张拉整体结构，通过调节绳索张力实现刚度变化，且易于组装。
- 采用**身体-大脑协同进化**（body-brain co-evolution）：在TensSoft仿真平台中，同时进化机器人的形态（模块数量、连接方式）和控制策略（关节角度序列）。

### 实验设置
- 平台：TensSoft，支持张拉整体机器人的物理仿真与进化优化。
- 变量：模块刚度设为低、中、高三个等级，分别进行进化实验。
- 任务：机器人需在平坦地面上实现最大前进距离。

### 关键结果
- **低刚度模块**：进化出类似蠕动的运动方式，形态紧凑，依靠弹性变形推进。
- **中等刚度模块**：产生摆动式运动，形态更细长，利用惯性力移动。
- **高刚度模块**：采用跳跃或步态运动，形态呈刚性框架，依赖地面反作用力。
- 结论：模块刚度直接决定了进化出的最优形态、控制策略和运动模式，证明刚度是张拉整体机器人设计中不可忽视的关键参数。

## 参考
- http://arxiv.org/abs/2101.11772v1

## Overview
Tensegrity structures offer unique advantages such as being lightweight, capable of large deformations, and highly robust. However, existing tensegrity robots still face challenges in morphology design, control, assembly, and actuation, and stiffness is often overlooked. This paper introduces actuation modules with programmable stiffness and, combined with a body-brain co-evolution approach, automatically designs soft tensegrity modular robots on the TensSoft platform. Experiments show that module stiffness is a key parameter determining evolutionary outcomes, with different stiffness levels leading to distinctly different morphologies, control strategies, and locomotion patterns.

## Content
### Method
- Proposes **programmable stiffness actuation modules**: The modules adopt a tensegrity structure, achieving stiffness variation by adjusting cable tension, and are easy to assemble.
- Employs **body-brain co-evolution**: Within the TensSoft simulation platform, both the robot's morphology (number of modules, connection patterns) and control strategy (joint angle sequences) are evolved simultaneously.

### Experimental Setup
- Platform: TensSoft, which supports physical simulation and evolutionary optimization of tensegrity robots.
- Variables: Module stiffness is set to three levels—low, medium, and high—with separate evolution experiments conducted for each.
- Task: Robots must achieve maximum forward distance on flat ground.

### Key Results
- **Low-stiffness modules**: Evolve a worm-like locomotion pattern, with a compact morphology that advances through elastic deformation.
- **Medium-stiffness modules**: Produce a swinging motion, with a more elongated morphology that moves using inertial forces.
- **High-stiffness modules**: Adopt jumping or gait-based locomotion, featuring a rigid frame morphology that relies on ground reaction forces.
- Conclusion: Module stiffness directly determines the optimal morphology, control strategy, and locomotion pattern that evolve, demonstrating that stiffness is a critical parameter that cannot be overlooked in tensegrity robot design.

## 개요
텐세그리티 구조는 경량성, 대변형, 강한 견고성 등의 독특한 장점을 가지지만, 기존 텐세그리티 로봇은 형태 설계, 제어, 조립, 구동 측면에서 여전히 과제를 안고 있으며, 강성은 종종 간과됩니다. 본 논문은 프로그래밍 가능한 강성을 가진 구동 모듈을 도입하고, 신체-뇌 공진화 방법을 결합하여 TensSoft 플랫폼에서 소프트 텐세그리티 모듈 로봇을 자동 설계합니다. 실험 결과, 모듈 강성은 진화 결과를 결정하는 핵심 매개변수이며, 서로 다른 강성은 전혀 다른 형태, 제어 전략 및 운동 패턴을 유도함을 보여줍니다.

## 핵심 내용
### 방법
- **프로그래밍 가능한 강성 구동 모듈** 제안: 모듈은 텐세그리티 구조를 채택하며, 로프 장력 조절을 통해 강성 변화를 구현하고 조립이 용이합니다.
- **신체-뇌 공진화**(body-brain co-evolution) 채택: TensSoft 시뮬레이션 플랫폼에서 로봇의 형태(모듈 수, 연결 방식)와 제어 전략(관절 각도 시퀀스)을 동시에 진화시킵니다.

### 실험 설정
- 플랫폼: TensSoft, 텐세그리티 로봇의 물리 시뮬레이션 및 진화 최적화를 지원합니다.
- 변수: 모듈 강성을 낮음, 중간, 높음의 세 등급으로 설정하고 각각 진화 실험을 수행합니다.
- 작업: 로봇은 평평한 지면에서 최대 전진 거리를 달성해야 합니다.

### 핵심 결과
- **낮은 강성 모듈**: 움직임과 유사한 운동 방식으로 진화하며, 형태는 컴팩트하고 탄성 변형에 의존하여 추진합니다.
- **중간 강성 모듈**: 흔들림 운동을 생성하며, 형태는 더 가늘고 길며 관성력을 이용해 이동합니다.
- **높은 강성 모듈**: 점프 또는 보행 운동을 채택하며, 형태는 강성 프레임을 이루고 지면 반력에 의존합니다.
- 결론: 모듈 강성은 진화된 최적 형태, 제어 전략 및 운동 패턴을 직접 결정하며, 강성이 텐세그리티 로봇 설계에서 무시할 수 없는 핵심 매개변수임을 증명합니다.
