---
$id: ent_paper_towards_bridging_the_gap_syste_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots'
  zh: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots'
  ko: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots'
summary:
  en: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots is a 2025 work on sim-to-real for
    humanoid robots.'
  zh: 本文提出了一种面向多种腿式机器人的系统性仿真到现实迁移框架，由研究团队于2025年发布。核心贡献在于结合物理驱动的永磁同步电机能量模型与强化学习，仅需少量参数即可弥合仿真与现实差距，并在ANYmal机器人上实现了32%的全运输成本降低（值1.27）。
  ko: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots is a 2025 work on sim-to-real for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- sim_to_real
- towards_bridging_the_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.06342v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (624 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots (arXiv)'
  url: https://arxiv.org/abs/2509.06342
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
腿式机器人在实际环境中需兼顾鲁棒运动与能效，但仿真训练的控制器常迁移失败，且现有方法多忽略执行器特定能量损耗或依赖复杂奖励函数。本文提出的框架通过集成强化学习与基于第一性原理的永磁同步电机能量模型，采用紧凑的四项奖励函数平衡电学与机械耗散。研究通过自底向上的动态参数识别研究（涵盖执行器、全机器人空中轨迹与地面运动）验证方法，并在三个主要平台测试后部署于十台额外机器人，无需动态参数随机化即可实现可靠策略迁移。

## 核心内容
### 方法架构
- 框架整合sim-to-real强化学习与物理驱动的永磁同步电机能量模型，仅需最小参数集捕捉仿真与现实差距。
- 采用紧凑的四项奖励函数，基于第一性原理构建能量损耗公式，平衡电学耗散（铜损、铁损）与机械耗散（摩擦、阻尼）。

### 实验设置
- 通过自底向上的动态参数识别研究验证方法，分三个阶段：执行器级参数标定、全机器人空中轨迹匹配、地面运动迁移测试。
- 在三个主要平台（包括ANYmal）上评估，并额外部署于十台不同构型机器人，未使用动态参数随机化。

### 关键结果
- 方法在ANYmal上实现全运输成本（CoT）降低32%，达到值1.27，优于现有最先进方法。
- 所有代码、模型与数据集将开源发布，支持复现与扩展。

### 结论
该框架通过物理约束的奖励设计与最小参数化迁移策略，显著提升了多类腿式机器人的仿真到现实迁移效率与能效，为实际部署提供了系统化解决方案。

## Overview
Legged robots must achieve both robust locomotion and energy efficiency to be practical in real-world environments. Yet controllers trained in simulation often fail to transfer reliably, and most existing approaches neglect actuator-specific energy losses or depend on complex, hand-tuned reward formulations. We propose a framework that integrates sim-to-real reinforcement learning with a physics-grounded energy model for permanent magnet synchronous motors. The framework requires a minimal parameter set to capture the simulation-to-reality gap and employs a compact four-term reward with a first-principle-based energetic loss formulation that balances electrical and mechanical dissipation. We evaluate and validate the approach through a bottom-up dynamic parameter identification study, spanning actuators, full-robot in-air trajectories and on-ground locomotion. The framework is tested on three primary platforms and deployed on ten additional robots, demonstrating reliable policy transfer without randomization of dynamic parameters. Our method improves energetic efficiency over state-of-the-art methods, achieving a 32 percent reduction in the full Cost of Transport of ANYmal (value 1.27). All code, models, and datasets will be released.

## 参考
- http://arxiv.org/abs/2509.06342v1

## 개요
보행 로봇은 실제 환경에서 강인한 운동과 에너지 효율을 동시에 고려해야 하지만, 시뮬레이션에서 훈련된 컨트롤러는 종종 전이에 실패하며, 기존 방법들은 대부분 액추에이터 특정 에너지 손실을 무시하거나 복잡한 보상 함수에 의존합니다. 본 논문에서 제안하는 프레임워크는 강화 학습과 제1원리에 기반한 영구자석 동기 모터 에너지 모델을 통합하고, 간결한 4항 보상 함수를 사용하여 전기적 및 기계적 소산을 균형 있게 조정합니다. 연구는 하향식 동적 파라미터 식별 연구(액추에이터, 전 로봇 공중 궤적 및 지상 운동 포함)를 통해 방법을 검증하고, 세 가지 주요 플랫폼에서 테스트한 후 추가 로봇 10대에 배포하여 동적 파라미터 무작위화 없이도 신뢰할 수 있는 정책 전이를 달성합니다.

## 핵심 내용
### 방법 아키텍처
- 프레임워크는 sim-to-real 강화 학습과 물리 기반 영구자석 동기 모터 에너지 모델을 통합하며, 최소한의 파라미터 집합만으로 시뮬레이션과 실제 환경의 차이를 포착합니다.
- 제1원리에 기반한 에너지 손실 공식을 사용하는 간결한 4항 보상 함수를 채택하여 전기적 소산(구리 손실, 철 손실)과 기계적 소산(마찰, 감쇠)을 균형 있게 조정합니다.

### 실험 설정
- 하향식 동적 파라미터 식별 연구를 통해 방법을 검증하며, 세 단계로 구성됩니다: 액추에이터 수준 파라미터 보정, 전 로봇 공중 궤적 매칭, 지상 운동 전이 테스트.
- 세 가지 주요 플랫폼(ANYmal 포함)에서 평가하고, 추가로 10대의 다양한 구성 로봇에 배포했으며, 동적 파라미터 무작위화는 사용하지 않았습니다.

### 주요 결과
- 이 방법은 ANYmal에서 총 운송 비용(CoT)을 32% 절감하여 1.27의 값을 달성했으며, 기존 최첨단 방법보다 우수합니다.
- 모든 코드, 모델 및 데이터 세트는 오픈소스로 공개되어 재현 및 확장을 지원합니다.

### 결론
이 프레임워크는 물리적 제약 기반 보상 설계와 최소 파라미터화 전이 전략을 통해 다양한 보행 로봇의 시뮬레이션-실제 전이 효율과 에너지 효율을 크게 향상시켜, 실제 배포를 위한 체계적인 솔루션을 제공합니다.
