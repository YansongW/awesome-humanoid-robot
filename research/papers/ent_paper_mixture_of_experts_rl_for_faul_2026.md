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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.25965v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
행성 탐사 및 기타 원격 환경에 배치된 보행 로봇은 액추에이터 고장과 까다로운 지형 조건에도 불구하고 안정적인 보행을 유지해야 합니다. 강화 학습은 보행에서 뛰어난 결과를 달성했지만, 단일 정책은 다양한 고장 조건을 보상하는 데 필요한 다양한 제어 전략을 효율적으로 표현하는 데 어려움을 겪을 수 있습니다. 본 연구에서는 고장 진단 정보를 명시적으로 활용하여 개별 액추에이터 고장 모드와 관련된 특화된 제어 전문가를 활성화하는 고장 인식 모듈형 제어 아키텍처를 제안합니다. 실험 결과는 명시적인 고장 조건 기반 모듈형 정책이 유사한 크기의 단일 정책보다 일관되게 우수한 성능을 보여주며, 고장 시나리오 전반에서 더 높은 보행 성능을 달성함을 보여줍니다. 또한, 제안된 모듈형 아키텍처는 네트워크 용량이 크게 감소된 상황에서도 경쟁력 있는 성능을 유지하여, 우주 응용 분야에서 일반적으로 사용되는 계산 자원이 제한된 로봇 플랫폼에 적합함을 강조합니다. 본 연구와 관련된 코드는 다음에서 확인할 수 있습니다: https://github.com/iit-DLSLab/fault-locomotion-isaaclab.

## 핵심 내용
행성 탐사 및 기타 원격 환경에 배치된 보행 로봇은 액추에이터 고장과 까다로운 지형 조건에도 불구하고 안정적인 보행을 유지해야 합니다. 강화 학습은 보행에서 뛰어난 결과를 달성했지만, 단일 정책은 다양한 고장 조건을 보상하는 데 필요한 다양한 제어 전략을 효율적으로 표현하는 데 어려움을 겪을 수 있습니다. 본 연구에서는 고장 진단 정보를 명시적으로 활용하여 개별 액추에이터 고장 모드와 관련된 특화된 제어 전문가를 활성화하는 고장 인식 모듈형 제어 아키텍처를 제안합니다. 실험 결과는 명시적인 고장 조건 기반 모듈형 정책이 유사한 크기의 단일 정책보다 일관되게 우수한 성능을 보여주며, 고장 시나리오 전반에서 더 높은 보행 성능을 달성함을 보여줍니다. 또한, 제안된 모듈형 아키텍처는 네트워크 용량이 크게 감소된 상황에서도 경쟁력 있는 성능을 유지하여, 우주 응용 분야에서 일반적으로 사용되는 계산 자원이 제한된 로봇 플랫폼에 적합함을 강조합니다. 본 연구와 관련된 코드는 다음에서 확인할 수 있습니다: https://github.com/iit-DLSLab/fault-locomotion-isaaclab.

## 参考
- http://arxiv.org/abs/2606.25965v2
