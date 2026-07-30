---
$id: ent_paper_dexterous_teleoperation_of_20_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dexterous Teleoperation of 20-DoF ByteDexter Hand via Human Motion Retargeting
  zh: Dexterous Teleoperation of 20-DoF ByteDexter Hand via Human Motion Retargeting
  ko: Dexterous Teleoperation of 20-DoF ByteDexter Hand via Human Motion Retargeting
summary:
  en: Dexterous Teleoperation of 20-DoF ByteDexter Hand via Human Motion Retargeting is a 2025 work on hardware design for
    humanoid robots.
  zh: 本文提出了一套手-臂遥操作系统的硬件与算法设计，包含20自由度ByteDexter灵巧手与基于优化的运动重定向方法。该系统由字节跳动团队开发，核心贡献在于实现了高保真的人手运动复现与手-臂协同控制，并通过杂乱桌面整理等长时任务验证了其生成高质量示教数据的能力。
  ko: Dexterous Teleoperation of 20-DoF ByteDexter Hand via Human Motion Retargeting is a 2025 work on hardware design for
    humanoid robots.
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
- dexterous_teleoperation_of_20
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.03227v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Dexterous Teleoperation of 20-DoF ByteDexter Hand via Human Motion Retargeting (arXiv)
  url: https://arxiv.org/abs/2507.03227
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对机器人灵巧操作中示教数据质量不足的问题，设计了一套完整的遥操作解决方案。硬件方面采用20自由度连杆驱动仿人灵巧手ByteDexter，软件层面则通过优化算法实现实时运动重定向。实验涵盖手指间物体操控与九物体杂乱桌面整理等长时任务，验证了系统在实时控制与数据生成方面的有效性。

## 核心内容
### 系统设计
- **硬件架构**：20自由度ByteDexter灵巧手采用连杆驱动机制，模仿人类手部运动学结构，支持精细的指尖操作与手-臂协同动作。
- **运动重定向**：基于优化的实时算法，将人类手部运动映射到机器人高自由度空间，同时保持手-臂协调性，避免运动学冲突。

### 实验验证
- **任务类型**：
  - 手指间物体操控（如旋转、抓取）
  - 长时任务：整理包含9个随机放置物体的杂乱化妆台
- **关键指标**：
  - 实时控制延迟满足遥操作需求
  - 生成的高质量示教数据可直接用于模仿学习策略训练
- **结果**：系统在复杂场景下保持稳定操作，视频资料展示了完整执行过程。

### 结论
该系统通过硬件与算法的协同设计，有效解决了高自由度灵巧手遥操作中的运动复现与数据质量瓶颈，为后续模仿学习研究提供了可靠的数据采集平台。

## Overview
Replicating human--level dexterity remains a fundamental robotics challenge, requiring integrated solutions from mechatronic design to the control of high degree--of--freedom (DoF) robotic hands. While imitation learning shows promise in transferring human dexterity to robots, the efficacy of trained policies relies on the quality of human demonstration data. We bridge this gap with a hand--arm teleoperation system featuring: (1) a 20--DoF linkage--driven anthropomorphic robotic hand for biomimetic dexterity, and (2) an optimization--based motion retargeting for real--time, high--fidelity reproduction of intricate human hand motions and seamless hand--arm coordination. We validate the system via extensive empirical evaluations, including dexterous in-hand manipulation tasks and a long--horizon task requiring the organization of a cluttered makeup table randomly populated with nine objects. Experimental results demonstrate its intuitive teleoperation interface with real--time control and the ability to generate high--quality demonstration data. Please refer to the accompanying video for further details.

## Overview
Replicating human-level dexterity remains a fundamental robotics challenge, requiring integrated solutions from mechatronic design to the control of high degree-of-freedom (DoF) robotic hands. While imitation learning shows promise in transferring human dexterity to robots, the efficacy of trained policies relies on the quality of human demonstration data. We bridge this gap with a hand-arm teleoperation system featuring: (1) a 20-DoF linkage-driven anthropomorphic robotic hand for biomimetic dexterity, and (2) an optimization-based motion retargeting for real-time, high-fidelity reproduction of intricate human hand motions and seamless hand-arm coordination. We validate the system via extensive empirical evaluations, including dexterous in-hand manipulation tasks and a long-horizon task requiring the organization of a cluttered makeup table randomly populated with nine objects. Experimental results demonstrate its intuitive teleoperation interface with real-time control and the ability to generate high-quality demonstration data. Please refer to the accompanying video for further details.

## Content
Replicating human-level dexterity remains a fundamental robotics challenge, requiring integrated solutions from mechatronic design to the control of high degree-of-freedom (DoF) robotic hands. While imitation learning shows promise in transferring human dexterity to robots, the efficacy of trained policies relies on the quality of human demonstration data. We bridge this gap with a hand-arm teleoperation system featuring: (1) a 20-DoF linkage-driven anthropomorphic robotic hand for biomimetic dexterity, and (2) an optimization-based motion retargeting for real-time, high-fidelity reproduction of intricate human hand motions and seamless hand-arm coordination. We validate the system via extensive empirical evaluations, including dexterous in-hand manipulation tasks and a long-horizon task requiring the organization of a cluttered makeup table randomly populated with nine objects. Experimental results demonstrate its intuitive teleoperation interface with real-time control and the ability to generate high-quality demonstration data. Please refer to the accompanying video for further details.

## 개요
인간 수준의 손재주를 재현하는 것은 여전히 로봇 공학의 근본적인 도전 과제로, 메카트로닉스 설계부터 고자유도(DoF) 로봇 손의 제어에 이르기까지 통합된 솔루션이 필요합니다. 모방 학습은 인간의 손재주를 로봇으로 전이하는 데 가능성을 보여주지만, 훈련된 정책의 효율성은 인간 시연 데이터의 품질에 의존합니다. 우리는 다음과 같은 특징을 가진 손-팔 원격 조작 시스템으로 이 격차를 해소합니다: (1) 생체 모방 손재주를 위한 20자유도 링크 구동 인체 모방 로봇 손, (2) 복잡한 인간 손 움직임의 실시간 고충실도 재현과 원활한 손-팔 협응을 위한 최적화 기반 모션 리타겟팅. 우리는 손 안에서의 정교한 조작 작업과 무작위로 배치된 9개의 물체로 어지럽혀진 화장대 정리 작업을 포함한 장기적 작업 등 광범위한 실증 평가를 통해 시스템을 검증합니다. 실험 결과는 실시간 제어가 가능한 직관적인 원격 조작 인터페이스와 고품질 시연 데이터 생성 능력을 입증합니다. 자세한 내용은 첨부된 비디오를 참조하시기 바랍니다.

## 핵심 내용
인간 수준의 손재주를 재현하는 것은 여전히 로봇 공학의 근본적인 도전 과제로, 메카트로닉스 설계부터 고자유도(DoF) 로봇 손의 제어에 이르기까지 통합된 솔루션이 필요합니다. 모방 학습은 인간의 손재주를 로봇으로 전이하는 데 가능성을 보여주지만, 훈련된 정책의 효율성은 인간 시연 데이터의 품질에 의존합니다. 우리는 다음과 같은 특징을 가진 손-팔 원격 조작 시스템으로 이 격차를 해소합니다: (1) 생체 모방 손재주를 위한 20자유도 링크 구동 인체 모방 로봇 손, (2) 복잡한 인간 손 움직임의 실시간 고충실도 재현과 원활한 손-팔 협응을 위한 최적화 기반 모션 리타겟팅. 우리는 손 안에서의 정교한 조작 작업과 무작위로 배치된 9개의 물체로 어지럽혀진 화장대 정리 작업을 포함한 장기적 작업 등 광범위한 실증 평가를 통해 시스템을 검증합니다. 실험 결과는 실시간 제어가 가능한 직관적인 원격 조작 인터페이스와 고품질 시연 데이터 생성 능력을 입증합니다. 자세한 내용은 첨부된 비디오를 참조하시기 바랍니다.

## 参考
- http://arxiv.org/abs/2507.03227v1
