---
$id: ent_paper_mixture_of_experts_rl_for_faul_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Mixture-of-Experts RL for Fault-Tolerant Legged Locomotion
  zh: Mixture-of-Experts RL for Fault-Tolerant Legged Locomotion
  ko: Mixture-of-Experts RL for Fault-Tolerant Legged Locomotion
summary:
  en: 'arXiv:2606.25965v2 Announce Type: replace Abstract: Legged robots deployed in planetary exploration and other remote
    environments must maintain reliable locomotion despite actuator failures and challenging terrain conditions. Although
    reinforcement learning has achieved strong results in legged locomotion, monolithic policies can struggle to efficiently
    represent the diverse control strategies required to compensate for different fault conditions. In this work, we propose
    a fault-aware modular control architecture that explicitly leverages fault-diagnosis information to activate specialized
    control experts associated with distinct actuator failure modes. Experimental results show that explicit fault-conditioned
    modular policies consistently outperform monolithic policies of comparable size, achieving higher locomotion performance
    across failure scenarios. Moreover, the proposed modular architecture retains competitive performance even under significantly
    reduced network capacity, highlighting its suitability for compute-constrained robotic platforms, such as those typically
    employed in space applications. The code associated with this work is available at: https://github.com/iit-DLSLab/fault-locomotion-isaaclab.'
  zh: 本文提出一种面向足式机器人容错运动的专家混合强化学习架构。该工作由意大利技术研究所（IIT）完成，核心贡献在于利用故障诊断信息激活对应特定执行器故障模式的专用控制专家，在多种故障场景下均优于同等规模的单一策略模型，且在降低网络容量时仍保持竞争力。
  ko: 'arXiv:2606.25965v2 Announce Type: replace Abstract: Legged robots deployed in planetary exploration and other remote
    environments must maintain reliable locomotion despite actuator failures and challenging terrain conditions. Although
    reinforcement learning has achieved strong results in legged locomotion, monolithic policies can struggle to efficiently
    represent the diverse control strategies required to compensate for different fault conditions. In this work, we propose
    a fault-aware modular control architecture that explicitly leverages fault-diagnosis information to activate specialized
    control experts associated with distinct actuator failure modes. Experimental results show that explicit fault-conditioned
    modular policies consistently outperform monolithic policies of comparable size, achieving higher locomotion performance
    across failure scenarios. Moreover, the proposed modular architecture retains competitive performance even under significantly
    reduced network capacity, highlighting its suitability for compute-constrained robotic platforms, such as those typically
    employed in space applications. The code associated with this work is available at: https://github.com/iit-DLSLab/fault-locomotion-isaaclab.'
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
- robotics
- mixture_of_experts_rl_for_faul
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.25965v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (772 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Mixture-of-Experts RL for Fault-Tolerant Legged Locomotion (arXiv)
  url: https://arxiv.org/abs/2606.25965
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
在行星探测等远程环境中，足式机器人需在遭遇执行器故障和复杂地形时保持可靠运动。传统强化学习训练的单一策略难以高效表征应对不同故障所需的多样化控制策略。为此，本文设计了一种故障感知模块化控制架构，显式利用故障诊断信息激活与特定执行器故障模式对应的专用控制专家。实验表明，这种显式故障条件化的模块化策略在多种故障场景下均优于同等规模的单一策略模型，且即使在网络容量大幅缩减时仍能保持竞争力，特别适合计算资源受限的太空机器人平台。

## 核心内容
### 方法架构
- 提出**故障感知模块化控制架构**，核心思想是将故障诊断信息作为条件输入，激活对应特定执行器故障模式的专用控制专家（specialized control experts）。
- 每个专家模块负责处理一种故障模式（如单关节锁定、力矩输出异常等），通过门控机制或条件选择实现专家激活。

### 实验设置
- 在足式机器人平台上进行仿真实验，对比对象为同等规模的**单一策略模型（monolithic policy）**。
- 测试场景包括多种执行器故障模式（如关节锁定、部分力矩失效）以及复杂地形条件。

### 关键结果
- **性能优势**：显式故障条件化的模块化策略在所有故障场景下均优于单一策略模型，运动性能提升显著。
- **容量效率**：即使将网络容量大幅缩减（如减少参数数量），模块化架构仍能保持与全尺寸单一策略相当的竞争力，验证了其在计算受限平台（如太空机器人）上的适用性。
- 代码已开源：https://github.com/iit-DLSLab/fault-locomotion-isaaclab

### 结论
该工作证明了显式利用故障诊断信息进行专家模块化设计的有效性，为足式机器人在极端环境下的容错运动控制提供了高效且资源友好的解决方案。

## Overview
Legged robots deployed in planetary exploration and other remote environments must maintain reliable locomotion despite actuator failures and challenging terrain conditions. Although reinforcement learning has achieved strong results in legged locomotion, monolithic policies can struggle to efficiently represent the diverse control strategies required to compensate for different fault conditions. In this work, we propose a fault-aware modular control architecture that explicitly leverages fault-diagnosis information to activate specialized control experts associated with distinct actuator failure modes. Experimental results show that explicit fault-conditioned modular policies consistently outperform monolithic policies of comparable size, achieving higher locomotion performance across failure scenarios. Moreover, the proposed modular architecture retains competitive performance even under significantly reduced network capacity, highlighting its suitability for compute-constrained robotic platforms, such as those typically employed in space applications. The code associated with this work is available at: https://github.com/iit-DLSLab/fault-locomotion-isaaclab.

## 参考
- http://arxiv.org/abs/2606.25965v2

## 개요
행성 탐사와 같은 원격 환경에서 족형 로봇은 액추에이터 고장과 복잡한 지형에 직면했을 때도 안정적인 운동을 유지해야 합니다. 전통적인 강화 학습으로 훈련된 단일 정책은 다양한 고장에 대응하는 다각화된 제어 전략을 효율적으로 표현하기 어렵습니다. 이를 위해 본 논문은 고장 인식 모듈식 제어 아키텍처를 설계하여, 고장 진단 정보를 명시적으로 활용해 특정 액추에이터 고장 모드에 대응하는 전용 제어 전문가를 활성화합니다. 실험 결과, 이러한 명시적 고장 조건화 모듈식 정책은 다양한 고장 시나리오에서 동일 규모의 단일 정책 모델보다 우수했으며, 네트워크 용량을 크게 줄여도 경쟁력을 유지하여 계산 자원이 제한된 우주 로봇 플랫폼에 특히 적합함을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **고장 인식 모듈식 제어 아키텍처**를 제안하며, 핵심 아이디어는 고장 진단 정보를 조건 입력으로 사용하여 특정 액추에이터 고장 모드에 대응하는 전용 제어 전문가(specialized control experts)를 활성화하는 것입니다.
- 각 전문가 모듈은 하나의 고장 모드(예: 단일 관절 잠금, 토크 출력 이상)를 처리하며, 게이팅 메커니즘 또는 조건 선택을 통해 전문가 활성화를 구현합니다.

### 실험 설정
- 족형 로봇 플랫폼에서 시뮬레이션 실험을 수행했으며, 비교 대상은 동일 규모의 **단일 정책 모델(monolithic policy)**입니다.
- 테스트 시나리오에는 다양한 액추에이터 고장 모드(예: 관절 잠금, 부분 토크 손실)와 복잡한 지형 조건이 포함됩니다.

### 주요 결과
- **성능 우위**: 명시적 고장 조건화 모듈식 정책은 모든 고장 시나리오에서 단일 정책 모델보다 우수했으며, 운동 성능이 크게 향상되었습니다.
- **용량 효율성**: 네트워크 용량을 크게 줄여도(예: 파라미터 수 감소) 모듈식 아키텍처는 전체 규모 단일 정책과 경쟁력 있는 성능을 유지하여, 계산 제한 플랫폼(예: 우주 로봇)에서의 적용 가능성을 검증했습니다.
- 코드는 오픈소스로 공개되었습니다: https://github.com/iit-DLSLab/fault-locomotion-isaaclab

### 결론
본 연구는 고장 진단 정보를 명시적으로 활용한 전문가 모듈식 설계의 효율성을 입증했으며, 족형 로봇의 극한 환경에서의 고장 허용 운동 제어를 위한 효율적이고 자원 친화적인 솔루션을 제공합니다.
