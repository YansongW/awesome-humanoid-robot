---
$id: ent_paper_xiloyannis_soft_robotic_suits_state_of_th_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Soft robotic suits: State of the art, core technologies and open challenges'
  zh: 软体机器人服：现状、核心技术与开放挑战
  ko: '소프트 로봇 슈트: 최신 기술, 핵심 기술 및 열린 과제'
summary:
  en: A 2021 arXiv survey that defines soft robotic suits, proposes a taxonomy, and
    reviews actuation, physical human-robot interfaces, intention-detection strategies,
    and biomechanical effects on human movement.
  zh: 2021年发表于arXiv的综述，定义了软体机器人服并提出分类法，系统回顾了驱动方式、物理人机接口、意图检测策略及其对人体运动的影响。
  ko: 2021년 arXiv에 발표된 종합 논문으로, 소프트 로봇 슈트를 정의하고 분류 체계를 제안하며 구동 방식, 물리적 인간-로봇 인터페이스,
    의도 검출 전략 및 인간 움직임에 대한 생체역학적 영향을 검토한다.
domains:
- 02_components
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
tags:
- soft_robotic_suit
- wearable_robot
- exosuit
- actuation
- human_robot_interface
- intention_detection
- assistive_robotics
- human_augmentation
- textile_based_assistance
- metabolic_cost
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text review is needed before
    final verification.
sources:
- id: src_001
  type: paper
  title: 'Soft robotic suits: State of the art, core technologies and open challenges'
  url: https://arxiv.org/abs/2105.10588
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper surveys the emerging class of soft robotic suits—lightweight, apparel-like wearable robots that contrast with traditional rigid exoskeletons. The authors propose a formal definition and a taxonomy for classifying existing systems, then review core technologies including actuation, the physical human-robot interface, and intention-detection methods. The survey emphasizes the advantages and limitations of each approach and provides a quantitative summary of the effects of soft suits on metabolic cost and muscular effort during human movement.

The reviewed actuation technologies include motor-tendon units, pneumatic artificial muscles (PAMs), pneumatic interference actuators (PIAs), twisted string actuators, and shape-memory alloys. Interface materials and sensors such as textiles, elastomers, Bowden cables, inertial measurement units (IMUs), load cells, and pressure sensors are discussed in terms of comfort and force transmission. The paper also distinguishes mechanically intrinsic intention-detection strategies (e.g., force/position sensing) from neural approaches (e.g., electromyography or electroencephalography).

## Key Contributions

- Proposes a formal definition and taxonomy for soft robotic suits versus rigid exoskeletons.
- Surveys and compares actuation technologies: motor-tendon units, PAMs, PIAs, twisted strings, and SMAs.
- Analyzes physical human-robot interface design for comfort and efficient force transfer.
- Reviews mechanically intrinsic and neural intention-detection strategies.
- Summarizes quantitative effects of soft suits on metabolic cost and muscular effort.

## Relevance to Humanoid Robotics

Although the paper focuses on soft wearable suits rather than full humanoid robots, its analysis of actuation, human-robot interfaces, and intention detection is foundational for any robotic system that physically interacts with humans. The technologies reviewed are directly applicable to lower-limb and whole-body assistance systems that may augment humanoid mobility or be manufactured as scalable assistive apparel. In addition, the discussion of portability, comfort, and real-world usability identifies constraints that also affect humanoid-adjacent wearable systems.
