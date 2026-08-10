---
$id: ent_paper_davies_ebt_policy_energy_unlocks_emer_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities'
  zh: EBT-Policy
  ko: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities'
summary:
  en: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities (EBT-Policy), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ZhiCheng AI, UIUC, Tsinghua University, Peking University.'
  zh: EBT-Policy 是由智源人工智能研究院、UIUC、清华大学和北京大学于2025年提出的基于能量的大视觉-语言-动作模型，用于机器人操作。其核心贡献在于通过能量基模型（EBM）学习端到端的能量景观并建模平衡动力学，在模拟和真实任务中持续优于扩散策略，且训练和推理计算量更少。关键参数包括仅需两步推理即可收敛（相比Diffusion
    Policy的100步减少50倍），并展现出零样本恢复失败动作序列等涌现能力。
  ko: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities (EBT-Policy), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ZhiCheng AI, UIUC, Tsinghua University, Peking University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ebt_policy
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.27545v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (954 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities (arXiv)'
  url: https://arxiv.org/abs/2510.27545
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EBT-Policy source
  url: https://doi.org/10.48550/arXiv.2510.27545
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
EBT-Policy 是一种新型能量基架构，旨在解决扩散策略等隐式策略模型在机器人操作中面临的高计算成本、暴露偏差和分布偏移下的推理不稳定性问题。通过将能量基模型（EBM）与Transformer架构结合，EBT-Policy 实现了对高维空间的扩展，并在模拟和真实任务中显著优于扩散策略。其关键优势包括更低的训练和推理计算需求，例如在某些任务中仅需两步推理即可收敛，相比Diffusion Policy的100步减少50倍。此外，EBT-Policy 展现出涌现能力，如仅通过行为克隆即可零样本恢复失败动作序列，无需显式重试训练。通过利用标量能量进行不确定性感知推理和动态计算分配，EBT-Policy 为在分布偏移下实现鲁棒、可泛化的机器人行为提供了新路径。

## 核心内容
### 方法
EBT-Policy 基于能量基模型（EBM）构建，通过端到端学习能量景观并建模平衡动力学，解决了扩散策略中常见的暴露偏差和推理不稳定性问题。其架构采用能量基Transformer（EBT），将EBM扩展到高维空间，同时保持计算效率。

### 实验设置
- **模拟任务**：在多个标准机器人操作基准上测试，包括物体抓取、堆叠和工具使用。
- **真实任务**：在真实机器人平台上执行操作任务，评估模型在分布偏移下的鲁棒性。
- **对比基线**：主要与Diffusion Policy等扩散策略模型进行比较。

### 关键数字
- **推理效率**：EBT-Policy 在某些任务中仅需2步推理即可收敛，而Diffusion Policy需要100步，推理计算量减少50倍。
- **性能优势**：在模拟和真实任务中，EBT-Policy 持续优于扩散策略，且训练和推理计算量更低。
- **涌现能力**：模型展现出零样本恢复失败动作序列的能力，仅通过行为克隆训练，无需显式重试训练。

### 结论
EBT-Policy 通过能量基架构解决了机器人操作中扩散策略的核心问题，包括高计算成本、暴露偏差和分布偏移下的不稳定性。其标量能量机制支持不确定性感知推理和动态计算分配，为构建鲁棒、可泛化的机器人行为提供了新范式。未来工作可进一步探索EBT-Policy在更复杂任务和真实环境中的扩展性。

## Overview
Implicit policies parameterized by generative models, such as Diffusion Policy, have become the standard for policy learning and Vision-Language-Action (VLA) models in robotics. However, these approaches often suffer from high computational cost, exposure bias, and unstable inference dynamics, which lead to divergence under distribution shifts. Energy-Based Models (EBMs) address these issues by learning energy landscapes end-to-end and modeling equilibrium dynamics, offering improved robustness and reduced exposure bias. Yet, policies parameterized by EBMs have historically struggled to scale effectively. Recent work on Energy-Based Transformers (EBTs) demonstrates the scalability of EBMs to high-dimensional spaces, but their potential for solving core challenges in physically embodied models remains underexplored. We introduce a new energy-based architecture, EBT-Policy, that solves core issues in robotic and real-world settings. Across simulated and real-world tasks, EBT-Policy consistently outperforms diffusion-based policies, while requiring less training and inference computation. Remarkably, on some tasks it converges within just two inference steps, a 50x reduction compared to Diffusion Policy's 100. Moreover, EBT-Policy exhibits emergent capabilities not seen in prior models, such as zero-shot recovery from failed action sequences using only behavior cloning and without explicit retry training. By leveraging its scalar energy for uncertainty-aware inference and dynamic compute allocation, EBT-Policy offers a promising path toward robust, generalizable robot behavior under distribution shifts.

## 参考
- http://arxiv.org/abs/2510.27545v1

## 개요
EBT-Policy는 확산 정책과 같은 암시적 정책 모델이 로봇 조작에서 직면하는 높은 계산 비용, 노출 편향, 분포 이동 하에서의 추론 불안정성 문제를 해결하기 위해 설계된 새로운 에너지 기반 아키텍처입니다. 에너지 기반 모델(EBM)과 Transformer 아키텍처를 결합함으로써, EBT-Policy는 고차원 공간으로의 확장을 실현하고 시뮬레이션 및 실제 작업에서 확산 정책보다 현저히 우수한 성능을 보여줍니다. 주요 장점으로는 더 낮은 훈련 및 추론 계산 요구량이 있으며, 예를 들어 일부 작업에서는 단 두 단계의 추론만으로 수렴하여 Diffusion Policy의 100단계 대비 50배 감소 효과를 보입니다. 또한 EBT-Policy는 행동 클로닝만으로 명시적 재시도 훈련 없이 실패한 동작 시퀀스를 제로샷으로 복구하는 창발적 능력을 보여줍니다. 스칼라 에너지를 활용한 불확실성 인지 추론과 동적 계산 할당을 통해, EBT-Policy는 분포 이동 하에서 강건하고 일반화 가능한 로봇 행동을 구현하는 새로운 경로를 제시합니다.

## 핵심 내용
### 방법
EBT-Policy는 에너지 기반 모델(EBM)을 기반으로 구축되었으며, 에너지 랜드스케이프를 종단 간 학습하고 평형 동역학을 모델링하여 확산 정책에서 흔히 발생하는 노출 편향과 추론 불안정성 문제를 해결합니다. 그 아키텍처는 에너지 기반 Transformer(EBT)를 채택하여 EBM을 고차원 공간으로 확장하면서도 계산 효율성을 유지합니다.

### 실험 설정
- **시뮬레이션 작업**: 객체 파지, 적재, 도구 사용을 포함한 여러 표준 로봇 조작 벤치마크에서 테스트되었습니다.
- **실제 작업**: 실제 로봇 플랫폼에서 조작 작업을 수행하여 분포 이동 하에서의 강건성을 평가합니다.
- **비교 기준선**: 주로 Diffusion Policy와 같은 확산 정책 모델과 비교됩니다.

### 주요 수치
- **추론 효율성**: EBT-Policy는 일부 작업에서 단 2단계의 추론만으로 수렴하는 반면, Diffusion Policy는 100단계가 필요하여 추론 계산량이 50배 감소합니다.
- **성능 우위**: 시뮬레이션 및 실제 작업에서 EBT-Policy는 지속적으로 확산 정책을 능가하며, 훈련 및 추론 계산량도 더 낮습니다.
- **창발적 능력**: 모델은 행동 클로닝만으로 훈련되었음에도 명시적 재시도 훈련 없이 실패한 동작 시퀀스를 제로샷으로 복구하는 능력을 보여줍니다.

### 결론
EBT-Policy는 에너지 기반 아키텍처를 통해 로봇 조작에서 확산 정책의 핵심 문제인 높은 계산 비용, 노출 편향, 분포 이동 하에서의 불안정성을 해결합니다. 스칼라 에너지 메커니즘은 불확실성 인지 추론과 동적 계산 할당을 지원하여 강건하고 일반화 가능한 로봇 행동을 구축하는 새로운 패러다임을 제공합니다. 향후 연구에서는 더 복잡한 작업과 실제 환경에서 EBT-Policy의 확장성을 추가로 탐구할 수 있습니다.
