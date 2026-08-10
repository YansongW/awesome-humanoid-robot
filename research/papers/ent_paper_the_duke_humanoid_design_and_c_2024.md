---
$id: ent_paper_the_duke_humanoid_design_and_c_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'The Duke Humanoid: Design and Control For Energy Efficient Bipedal Locomotion Using Passive Dynamics'
  zh: 'The Duke Humanoid: Design and Control For Energy Efficient Bipedal Locomotion Using Passive Dynamics'
  ko: 'The Duke Humanoid: Design and Control For Energy Efficient Bipedal Locomotion Using Passive Dynamics'
summary:
  en: 'The Duke Humanoid: Design and Control For Energy Efficient Bipedal Locomotion Using Passive Dynamics is a 2024 work
    on hardware design for humanoid robots, with open-source code available.'
  zh: Duke Humanoid 是 2024 年发布的一款开源 10 自由度双足人形机器人平台，由通用机器人实验室设计。其核心贡献在于通过模仿人体生理结构的对称布局实现静态平衡，并提出一种端到端强化学习算法，鼓励机器人利用被动动力学行走。实验表明，该策略在仿真中降低运输成本高达
    50%，在真实世界中降低 31%。
  ko: 'The Duke Humanoid: Design and Control For Energy Efficient Bipedal Locomotion Using Passive Dynamics is a 2024 work
    on hardware design for humanoid robots, with open-source code available.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- hardware_design
- humanoid
- the_duke_humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.19795v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (655 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'The Duke Humanoid: Design and Control For Energy Efficient Bipedal Locomotion Using Passive Dynamics (arXiv)'
  url: https://arxiv.org/abs/2409.19795
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'The Duke Humanoid: Design and Control For Energy Efficient Bipedal Locomotion Using Passive Dynamics project page'
  url: http://www.generalroboticslab.com/blogs/blog/2024-09-29-dukehumanoidv1/index.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Duke Humanoid 是一款专为双足运动研究设计的开源人形机器人，拥有 10 个自由度。其硬件设计模仿人体生理结构，在额状面采用对称身体对齐，使机器人能在膝盖伸直状态下保持静态平衡。研究团队开发了一种强化学习策略，可直接零样本部署到硬件上执行速度跟踪行走任务。为进一步提升运动能效，他们提出了一种端到端强化学习算法，鼓励机器人利用被动动力学（如摆动腿的自然摆动）来减少主动控制能耗。实验结果显示，该被动策略在仿真环境中将运输成本降低 50%，在真实硬件测试中降低 31%。

## 核心内容
### 硬件设计
- Duke Humanoid 是一个 10 自由度的开源人形机器人平台，旨在作为可扩展的 locomotion 研究平台。
- 设计模仿人体生理结构，在额状面采用对称身体对齐，使机器人能在膝盖伸直状态下保持静态平衡。

### 控制方法
- 开发了一种强化学习策略，可直接零样本部署到硬件上，用于执行速度跟踪行走任务。
- 提出了一种端到端强化学习算法，通过奖励函数设计鼓励机器人利用被动动力学（如摆动腿的自然摆动），从而减少主动控制能耗。

### 实验设置与结果
- 实验在仿真环境和真实硬件上分别进行。
- 在仿真中，被动策略将运输成本（cost of transport）降低 50%。
- 在真实世界测试中，运输成本降低 31%。
- 所有代码和硬件设计均已开源，项目网站为 http://generalroboticslab.com/DukeHumanoidv1/ 。

## 参考
- http://arxiv.org/abs/2409.19795v2

## Overview
Duke Humanoid is an open-source humanoid robot designed for bipedal locomotion research, featuring 10 degrees of freedom. Its hardware design mimics human physiological structure, with symmetrical body alignment in the frontal plane, enabling the robot to maintain static balance with straight knees. The research team developed a reinforcement learning policy that can be deployed directly to hardware with zero-shot transfer for velocity-tracking walking tasks. To further enhance locomotion energy efficiency, they proposed an end-to-end reinforcement learning algorithm that encourages the robot to exploit passive dynamics (such as the natural swing of the legs) to reduce active control energy consumption. Experimental results show that this passive policy reduces the cost of transport by 50% in simulation and by 31% in real hardware tests.

## Content
### Hardware Design
- Duke Humanoid is an open-source humanoid robot platform with 10 degrees of freedom, designed as a scalable locomotion research platform.
- The design mimics human physiological structure, with symmetrical body alignment in the frontal plane, allowing the robot to maintain static balance with straight knees.

### Control Method
- Developed a reinforcement learning policy that can be deployed directly to hardware with zero-shot transfer for velocity-tracking walking tasks.
- Proposed an end-to-end reinforcement learning algorithm that, through reward function design, encourages the robot to exploit passive dynamics (such as the natural swing of the legs) to reduce active control energy consumption.

### Experimental Setup and Results
- Experiments were conducted in both simulation and real hardware environments.
- In simulation, the passive policy reduced the cost of transport by 50%.
- In real-world tests, the cost of transport was reduced by 31%.
- All code and hardware designs are open-sourced, with the project website at http://generalroboticslab.com/DukeHumanoidv1/ .

## 개요
Duke Humanoid는 이족 보행 연구를 위해 설계된 오픈소스 휴머노이드 로봇으로, 10개의 자유도를 보유하고 있습니다. 하드웨어 설계는 인체 생리 구조를 모방하며, 관상면에서 대칭적인 신체 정렬을 채택하여 로봇이 무릎을 편 상태에서도 정적 균형을 유지할 수 있게 합니다. 연구팀은 강화 학습 정책을 개발하여 하드웨어에 직접 제로샷 배포가 가능하며, 속도 추적 보행 작업을 수행합니다. 운동 효율을 더욱 향상시키기 위해, 그들은 능동 제어 에너지 소비를 줄이기 위해 수동 역학(예: 스윙 다리의 자연스러운 움직임)을 활용하도록 장려하는 엔드투엔드 강화 학습 알고리즘을 제안했습니다. 실험 결과, 이 수동 정책은 시뮬레이션 환경에서 운송 비용을 50% 줄였고, 실제 하드웨어 테스트에서는 31% 줄였습니다.

## 핵심 내용
### 하드웨어 설계
- Duke Humanoid는 10자유도 오픈소스 휴머노이드 로봇 플랫폼으로, 확장 가능한 로코모션 연구 플랫폼으로 설계되었습니다.
- 설계는 인체 생리 구조를 모방하며, 관상면에서 대칭적인 신체 정렬을 채택하여 로봇이 무릎을 편 상태에서도 정적 균형을 유지할 수 있게 합니다.

### 제어 방법
- 하드웨어에 직접 제로샷 배포가 가능한 강화 학습 정책을 개발하여 속도 추적 보행 작업을 수행합니다.
- 보상 함수 설계를 통해 로봇이 수동 역학(예: 스윙 다리의 자연스러운 움직임)을 활용하도록 장려하는 엔드투엔드 강화 학습 알고리즘을 제안하여 능동 제어 에너지 소비를 줄입니다.

### 실험 설정 및 결과
- 실험은 시뮬레이션 환경과 실제 하드웨어에서 각각 수행되었습니다.
- 시뮬레이션에서 수동 정책은 운송 비용(cost of transport)을 50% 줄였습니다.
- 실제 세계 테스트에서 운송 비용은 31% 줄었습니다.
- 모든 코드와 하드웨어 설계는 오픈소스로 제공되며, 프로젝트 웹사이트는 http://generalroboticslab.com/DukeHumanoidv1/ 입니다.
