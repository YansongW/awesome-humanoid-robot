---
$id: ent_paper_li_vla_rft_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators'
  zh: VLA-RFT
  ko: 'VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators'
summary:
  en: 'VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators (VLA-RFT), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Westlake University, Zhejiang University,
    OpenHelix Team, Fudan University, Zhengzhou University, BUPT, Hebei University of Technology.'
  zh: VLA-RFT 是由西湖大学、浙江大学、OpenHelix Team、复旦大学、郑州大学、北京邮电大学、河北工业大学联合提出的2025年大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于利用数据驱动的世界模型作为可控模拟器，通过强化微调（RFT）提供基于已验证奖励的密集轨迹级学习信号，从而在不到400步微调内超越强监督基线，并显著提升模型在分布偏移下的鲁棒性。
  ko: 'VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators (VLA-RFT), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Westlake University, Zhejiang University,
    OpenHelix Team, Fudan University, Zhengzhou University, BUPT, Hebei University of Technology.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
- vla_rft
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.00406v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators (arXiv)'
  url: https://arxiv.org/abs/2510.00406
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-RFT source
  url: https://doi.org/10.48550/arXiv.2510.00406
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
VLA-RFT 针对现有视觉-语言-动作模型依赖模仿学习导致的复合误差和分布偏移鲁棒性差的问题，提出了一种基于世界模型的强化微调框架。该框架从真实交互数据中训练世界模型，使其能根据动作预测未来视觉观察，从而在模拟环境中生成密集的、与目标达成参考对齐的轨迹级奖励。这种设计提供了高效且与动作对齐的学习信号，大幅降低了样本需求。实验表明，VLA-RFT 在不到400步微调内即超越强监督基线，且效率高于传统基于模拟器的强化学习方法，同时在扰动条件下展现出强鲁棒性，能稳定执行任务。

## 核心内容
### 方法
- **核心问题**：现有 VLA 模型依赖模仿学习，在分布偏移下易产生复合误差；强化学习虽能缓解，但需昂贵真实交互或面临 sim-to-real 差距。
- **解决方案**：VLA-RFT 引入数据驱动的世界模型作为可控模拟器，该模型从真实交互数据中训练，能根据动作序列预测未来视觉观察。
- **奖励设计**：利用目标达成参考（goal-achieving references）生成密集的轨迹级奖励，提供与动作对齐的高效学习信号，大幅降低样本需求。

### 实验设置
- **微调步骤**：少于400步。
- **基线对比**：强监督基线（如行为克隆）和基于模拟器的强化学习方法。
- **鲁棒性测试**：在扰动条件下（如视觉噪声、动作干扰）评估任务执行稳定性。

### 关键结果
- **效率与性能**：VLA-RFT 在不到400步微调内超越强监督基线，且效率高于传统基于模拟器的强化学习。
- **鲁棒性**：在扰动条件下，VLA-RFT 能稳定执行任务，展现出强鲁棒性。
- **结论**：基于世界模型的强化微调（RFT）可作为 VLA 模型的后训练范式，有效提升其泛化能力和鲁棒性。

## Overview
Vision-Language-Action (VLA) models enable embodied decision-making but rely heavily on imitation learning, leading to compounding errors and poor robustness under distribution shift. Reinforcement learning (RL) can mitigate these issues yet typically demands costly real-world interactions or suffers from sim-to-real gaps. We introduce VLA-RFT, a reinforcement fine-tuning framework that leverages a data-driven world model as a controllable simulator. Trained from real interaction data, the simulator predicts future visual observations conditioned on actions, allowing policy rollouts with dense, trajectory-level rewards derived from goal-achieving references. This design delivers an efficient and action-aligned learning signal, drastically lowering sample requirements. With fewer than 400 fine-tuning steps, VLA-RFT surpasses strong supervised baselines and achieves greater efficiency than simulator-based RL. Moreover, it exhibits strong robustness under perturbed conditions, sustaining stable task execution. Our results establish world-model-based RFT as a practical post-training paradigm to enhance the generalization and robustness of VLA models. For more details, please refer to https://vla-rft.github.io/.

## 개요
Vision-Language-Action (VLA) 모델은 구현된 의사 결정을 가능하게 하지만, 모방 학습에 크게 의존하여 분포 변화 하에서 오류가 누적되고 견고성이 떨어집니다. 강화 학습(RL)은 이러한 문제를 완화할 수 있지만, 일반적으로 비용이 많이 드는 실제 환경 상호작용을 요구하거나 시뮬레이션-실제 간 차이로 인해 어려움을 겪습니다. 우리는 데이터 기반 세계 모델을 제어 가능한 시뮬레이터로 활용하는 강화 미세 조정 프레임워크인 VLA-RFT를 소개합니다. 실제 상호작용 데이터로 훈련된 시뮬레이터는 행동에 따라 미래 시각적 관찰을 예측하여, 목표 달성 참조에서 파생된 밀집된 궤적 수준 보상으로 정책 롤아웃을 가능하게 합니다. 이 설계는 효율적이고 행동에 정렬된 학습 신호를 제공하여 샘플 요구 사항을 크게 낮춥니다. 400회 미만의 미세 조정 단계로 VLA-RFT는 강력한 지도 학습 기준을 능가하고 시뮬레이터 기반 RL보다 더 높은 효율성을 달성합니다. 또한 교란된 조건에서 강력한 견고성을 보여주며 안정적인 작업 실행을 유지합니다. 우리의 결과는 세계 모델 기반 RFT가 VLA 모델의 일반화와 견고성을 향상시키는 실용적인 사후 훈련 패러다임임을 입증합니다. 자세한 내용은 https://vla-rft.github.io/를 참조하십시오.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 구현된 의사 결정을 가능하게 하지만, 모방 학습에 크게 의존하여 분포 변화 하에서 오류가 누적되고 견고성이 떨어집니다. 강화 학습(RL)은 이러한 문제를 완화할 수 있지만, 일반적으로 비용이 많이 드는 실제 환경 상호작용을 요구하거나 시뮬레이션-실제 간 차이로 인해 어려움을 겪습니다. 우리는 데이터 기반 세계 모델을 제어 가능한 시뮬레이터로 활용하는 강화 미세 조정 프레임워크인 VLA-RFT를 소개합니다. 실제 상호작용 데이터로 훈련된 시뮬레이터는 행동에 따라 미래 시각적 관찰을 예측하여, 목표 달성 참조에서 파생된 밀집된 궤적 수준 보상으로 정책 롤아웃을 가능하게 합니다. 이 설계는 효율적이고 행동에 정렬된 학습 신호를 제공하여 샘플 요구 사항을 크게 낮춥니다. 400회 미만의 미세 조정 단계로 VLA-RFT는 강력한 지도 학습 기준을 능가하고 시뮬레이터 기반 RL보다 더 높은 효율성을 달성합니다. 또한 교란된 조건에서 강력한 견고성을 보여주며 안정적인 작업 실행을 유지합니다. 우리의 결과는 세계 모델 기반 RFT가 VLA 모델의 일반화와 견고성을 향상시키는 실용적인 사후 훈련 패러다임임을 입증합니다. 자세한 내용은 https://vla-rft.github.io/를 참조하십시오.

## 参考
- http://arxiv.org/abs/2510.00406v1
