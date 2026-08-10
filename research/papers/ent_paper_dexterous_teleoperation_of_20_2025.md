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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.03227v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (540 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2507.03227v1

## 개요
본 연구는 로봇의 정밀 조작에서 시범 데이터 품질이 부족한 문제를 해결하기 위해 완전한 원격 조작 솔루션을 설계했습니다. 하드웨어 측면에서는 20자유도 링크 구동 방식의 인간형 정밀 손 ByteDexter를 채택했으며, 소프트웨어 측면에서는 최적화 알고리즘을 통해 실시간 운동 재지향을 구현했습니다. 실험은 손가락 간 객체 조작과 9개 객체가 어지럽게 놓인 탁자 정리 같은 장시간 작업을 포함하며, 시스템의 실시간 제어 및 데이터 생성 효율성을 검증했습니다.

## 핵심 내용
### 시스템 설계
- **하드웨어 아키텍처**: 20자유도 ByteDexter 정밀 손은 링크 구동 메커니즘을 사용하여 인간 손의 운동학적 구조를 모방하며, 정밀한 손끝 조작과 손-팔 협응 동작을 지원합니다.
- **운동 재지향**: 최적화 기반 실시간 알고리즘으로 인간 손 동작을 로봇의 고자유도 공간에 매핑하며, 손-팔 협응성을 유지하고 운동학적 충돌을 방지합니다.

### 실험 검증
- **작업 유형**:
  - 손가락 간 객체 조작 (예: 회전, 파지)
  - 장시간 작업: 9개의 무작위로 배치된 객체가 있는 어지러운 화장대 정리
- **핵심 지표**:
  - 실시간 제어 지연이 원격 조작 요구를 충족
  - 생성된 고품질 시범 데이터는 모방 학습 전략 훈련에 직접 사용 가능
- **결과**: 시스템은 복잡한 환경에서 안정적인 조작을 유지했으며, 비디오 자료는 전체 실행 과정을 보여줍니다.

### 결론
본 시스템은 하드웨어와 알고리즘의 협력 설계를 통해 고자유도 정밀 손 원격 조작에서의 운동 재현 및 데이터 품질 병목 문제를 효과적으로 해결했으며, 향후 모방 학습 연구를 위한 신뢰할 수 있는 데이터 수집 플랫폼을 제공합니다.
