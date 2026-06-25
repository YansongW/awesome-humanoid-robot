---
$id: ent_paper_zorin_ruka_rethinking_the_design_of_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RUKA: Rethinking the Design of Humanoid Hands with Learning'
  zh: RUKA：以学习重新思考人形手机器人设计
  ko: 'RUKA: 학습을 통한 휴머노이드 손 설계의 재고'
summary:
  en: RUKA is a low-cost, 3D-printed, tendon-driven anthropomorphic hand with 15 underactuated
    degrees of freedom and 11 actuators, controlled by learned LSTM+MLP models trained
    on MANUS motion-capture glove data. The open-source design costs under $1,300
    USD and is evaluated against LEAP and Allegro hands on reachability, durability,
    and strength, with demonstrations in teleoperation and imitation learning.
  zh: RUKA 是一种低成本的3D打印肌腱驱动拟人手，具有15个欠驱动自由度和11个执行器，通过从 MANUS 动作捕捉手套数据训练的 LSTM+MLP 模型进行控制。该开源设计成本低于1300美元，并在可达性、耐久性和力量方面与
    LEAP 和 Allegro 手进行了评估，同时展示了遥操作和模仿学习应用。
  ko: RUKA는 15개의 과소 구동 자유도와 11개의 액추에이터를 갖춘 저렴한 3D 프린팅 틴돈 구동 의인화 손으로, MANUS 모션 캡처 장갑
    데이터로 학습한 LSTM+MLP 모델로 제어됩니다. 오픈소스 설계 비용은 1,300달러 미만이며, 도달성, 내구성 및 힘에 대해 LEAP 및
    Allegro 손과 비교 평가되었고 원격 조작 및 모방 학습 응용도 시연되었습니다.
domains:
- 02_components
- 07_ai_models_algorithms
- 03_manufacturing_processes
- 06_design_engineering
- 05_mass_production
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- tendon_driven_hand
- dexterous_manipulation
- 3d_printed_hand
- underactuated_hand
- humanoid_hand
- affordable_robotics
- motion_capture_teleoperation
- lstm_mlp_controller
- manus_glove
- imitation_learning
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text verification
    and exact section/page references require human review.; approved by human reviewer.
sources:
- id: src_001
  type: paper
  title: 'RUKA: Rethinking the Design of Humanoid Hands with Learning'
  url: https://arxiv.org/abs/2504.13165
  date: '2025'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_component_leap_hand
  relationship: is_alternative_to
  description:
    en: RUKA is compared against the LEAP hand in reachability, durability, and strength
      evaluations.
    zh: RUKA 在可达性、耐久性和力量评估中与 LEAP 手进行了比较。
    ko: RUKA는 도달성, 내구성 및 힘 평가에서 LEAP 손과 비교되었습니다.
- id: ent_component_allegro_hand
  relationship: is_alternative_to
  description:
    en: RUKA is compared against the Allegro hand in reachability, durability, and
      strength evaluations.
    zh: RUKA 在可达性、耐久性和力量评估中与 Allegro 手进行了比较。
    ko: RUKA는 도달성, 내구성 및 힘 평가에서 Allegro 손과 비교되었습니다.
- id: ent_component_manus_metaglove
  relationship: sources_from
  description:
    en: RUKA uses MANUS glove motion-capture data to train joint-to-actuator and fingertip-to-actuator
      models.
    zh: RUKA 使用 MANUS 手套动作捕捉数据训练关节到执行器和指尖到执行器模型。
    ko: RUKA는 MANUS 장갑 모션 캡처 데이터를 사용하여 관절-액추에이터 및 손가락 끝-액추에이터 모델을 학습합니다.
- id: ent_hudor
  relationship: is_based_on
  description:
    en: RUKA is demonstrated in teleoperation and imitation-learning applications
      using HuDOR.
    zh: RUKA 在基于 HuDOR 的遥操作和模仿学习应用中得到了展示。
    ko: RUKA는 HuDOR를 사용한 원격 조작 및 모방 학습 응용에서 시연되었습니다.
- id: ent_component_dynamixel_xm430_w210_t
  relationship: integrates
  description:
    en: RUKA uses Dynamixel XM430-W210-T motors as part of its actuation system.
    zh: RUKA 在其驱动系统中使用 Dynamixel XM430-W210-T 电机。
    ko: RUKA는 구동 시스템의 일부로 Dynamixel XM430-W210-T 모터를 사용합니다.
- id: ent_component_dynamixel_xl330_m288_t
  relationship: integrates
  description:
    en: RUKA uses Dynamixel XL330-M288-T motors as part of its actuation system.
    zh: RUKA 在其驱动系统中使用 Dynamixel XL330-M288-T 电机。
    ko: RUKA는 구동 시스템의 일부로 Dynamixel XL330-M288-T 모터를 사용합니다.
- id: ent_kapandji_test
  relationship: verified_by
  description:
    en: RUKA is evaluated using the Kapandji Test for thumb opposability.
    zh: RUKA 使用 Kapandji 测试评估拇指对掌能力。
    ko: RUKA는 엄지 손가락 대립 운동을 평가하기 위해 Kapandji 테스트를 사용합니다.
- id: ent_grasp_taxonomy
  relationship: verified_by
  description:
    en: RUKA is evaluated against the GRASP Taxonomy for grasp diversity.
    zh: RUKA 使用 GRASP 分类法评估抓取多样性。
    ko: RUKA는 GRASP 분류법을 사용하여 그립 다양성을 평가합니다.
- id: ent_rom_test
  relationship: verified_by
  description:
    en: RUKA is evaluated with a Range of Motion Test for joint reachability.
    zh: RUKA 使用活动范围测试评估关节可达性。
    ko: RUKA는 관절 도달성을 평가하기 위해 가동 범위 테스트를 사용합니다.
---





# RUKA: Rethinking the Design of Humanoid Hands with Learning

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：它就像一个创客用 3D 打印零件和普通舵机拼出一只仿生手，然后戴上数据手套做一遍动作，让这只手通过观察“学会”跟着做。

> **自然语言逻辑**：RUKA 是一款低成本、开源、肌腱驱动的拟人灵巧手，具有 15 个欠驱动自由度和 11 个执行器；它通过 MANUS 动作捕捉手套采集人类手势，再用 LSTM+MLP 学习关节/指尖到电机的映射，从而实现数据驱动的灵巧控制，并在可达性、耐久性和力量上与 LEAP、Allegro 等手进行比较。

## Overview

Dexterous manipulation remains a fundamental challenge for robotic systems, constrained by trade-offs among precision, compactness, strength, and affordability. RUKA addresses these trade-offs by combining a tendon-driven, anthropomorphic mechanical design with learning-based control. The hand is built from 3D-printed parts and off-the-shelf components, achieving a compact, human-sized form factor with five fingers, fifteen underactuated degrees of freedom, and eleven actuators.

To overcome the control difficulties typical of tendon-driven actuation, RUKA leverages data collected with MANUS motion-capture gloves. Supervised training data is gathered by fitting the gloves directly onto the robot, exploiting the hand's morphological similarity to a human hand. From this data, the authors learn both joint-to-actuator and fingertip-to-actuator models implemented as LSTM+MLP controllers, which map desired joint angles or fingertip positions into motor commands.

The paper reports extensive hardware evaluations of reachability, durability, and strength, comparing RUKA against the LEAP and Allegro robotic hands. It also demonstrates teleoperation and imitation-learning tasks, showing that the low-cost platform can produce dexterous, human-like grasps. The complete design, assembly instructions, code, and data are released as open source.

## Key Contributions

- Open-source, human-sized tendon-driven robotic hand design costing under $1,300 USD.
- Data-driven control approach that fits MANUS motion-capture gloves directly onto the robot for autonomous supervised data collection.
- Learned LSTM+MLP controllers that map desired fingertip positions or joint angles to motor commands.
- Extensive hardware evaluations showing superior reachability, durability, and strength versus LEAP and Allegro hands.
- Demonstration of teleoperation and imitation-learning (HuDOR) applications with RUKA.

## Relevance to Humanoid Robotics

RUKA is highly relevant to humanoid robotics because it provides an affordable, human-scale, open-source end-effector that lowers three major barriers to mass production: cost, manufacturability, and control. By using 3D-printed parts and widely available off-the-shelf components, the design can be replicated and iterated without specialized manufacturing infrastructure. Its tendon-driven architecture delivers powerful grasping in a compact form factor suited to humanoid arms.

The learning-based control strategy is especially significant for humanoid deployment, where accurate models of cable-driven, low-cost mechanisms are difficult to derive analytically. By training controllers directly from motion-capture data, RUKA offers a practical path to robust, dexterous manipulation on low-cost hardware, bringing capable humanoid hands closer to scalable, real-world use.
