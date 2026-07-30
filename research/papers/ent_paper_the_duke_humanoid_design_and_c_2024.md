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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.19795v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## Overview
We present the Duke Humanoid, an open-source 10-degrees-of-freedom humanoid, as an extensible platform for locomotion research. The design mimics human physiology, with symmetrical body alignment in the frontal plane to maintain static balance with straight knees. We develop a reinforcement learning policy that can be deployed zero-shot on the hardware for velocity-tracking walking tasks. Additionally, to enhance energy efficiency in locomotion, we propose an end-to-end reinforcement learning algorithm that encourages the robot to leverage passive dynamics. Our experimental results show that our passive policy reduces the cost of transport by up to $50\%$ in simulation and $31\%$ in real-world tests. Our website is http://generalroboticslab.com/DukeHumanoidv1/ .

## 개요
우리는 Duke Humanoid를 소개합니다. 이는 오픈소스 10자유도 휴머노이드로, 보행 연구를 위한 확장 가능한 플랫폼입니다. 디자인은 인간 생리학을 모방하여 정면 평면에서 대칭적인 신체 정렬을 통해 무릎을 곧게 편 상태에서 정적 균형을 유지합니다. 우리는 속도 추적 보행 작업을 위해 하드웨어에 제로샷으로 배포할 수 있는 강화 학습 정책을 개발했습니다. 또한, 보행의 에너지 효율성을 높이기 위해 로봇이 수동 역학을 활용하도록 장려하는 종단간 강화 학습 알고리즘을 제안합니다. 실험 결과에 따르면, 우리의 수동 정책은 시뮬레이션에서 최대 $50\%$, 실제 테스트에서 $31\%$의 운송 비용을 절감했습니다. 웹사이트는 http://generalroboticslab.com/DukeHumanoidv1/ 입니다.

## 핵심 내용
우리는 Duke Humanoid를 소개합니다. 이는 오픈소스 10자유도 휴머노이드로, 보행 연구를 위한 확장 가능한 플랫폼입니다. 디자인은 인간 생리학을 모방하여 정면 평면에서 대칭적인 신체 정렬을 통해 무릎을 곧게 편 상태에서 정적 균형을 유지합니다. 우리는 속도 추적 보행 작업을 위해 하드웨어에 제로샷으로 배포할 수 있는 강화 학습 정책을 개발했습니다. 또한, 보행의 에너지 효율성을 높이기 위해 로봇이 수동 역학을 활용하도록 장려하는 종단간 강화 학습 알고리즘을 제안합니다. 실험 결과에 따르면, 우리의 수동 정책은 시뮬레이션에서 최대 $50\%$, 실제 테스트에서 $31\%$의 운송 비용을 절감했습니다. 웹사이트는 http://generalroboticslab.com/DukeHumanoidv1/ 입니다.

## 参考
- http://arxiv.org/abs/2409.19795v2
