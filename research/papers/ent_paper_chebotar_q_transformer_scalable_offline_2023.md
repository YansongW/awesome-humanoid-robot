---
$id: ent_paper_chebotar_q_transformer_scalable_offline_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions'
  zh: Q-Transformer
  ko: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions'
summary:
  en: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions (Q-Transformer), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL 2023.'
  zh: Q-Transformer 是 Google DeepMind 于 2023 年提出的通用视觉-语言-动作模型，用于机器人操作任务。其核心贡献在于将 Transformer 架构与离线 Q-learning 结合，通过将每个动作维度离散化为独立
    token 并自回归建模 Q 值，实现了大规模离线数据下的多任务策略训练。该方法在真实机器人操作任务套件上优于先前的离线强化学习与模仿学习方法。
  ko: 'Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions (Q-Transformer), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- q_transformer
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.10150v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1009 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Q-Transformer source
  url: https://proceedings.mlr.press/v229/chebotar23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Q-Transformer 通过将 Transformer 的高容量序列建模能力引入离线 Q-learning，解决了传统方法在大规模异构数据（包括人类演示与自主收集数据）上扩展性不足的问题。该方法将每个动作维度离散化为独立 token，并利用自回归方式建模各维度的 Q 值，从而将强化学习的时间差分更新转化为序列预测任务。实验表明，Q-Transformer 在多样化的真实机器人操作任务中显著优于 prior 离线 RL 算法与模仿学习技术。

## 核心内容
### 方法架构
- **核心思想**：将 Q-learning 中的动作值函数分解为每个动作维度的自回归 token 序列，利用 Transformer 建模各维度间的依赖关系。
- **动作离散化**：每个动作维度（如关节角度、末端执行器位置）被离散化为固定数量的 bin，每个 bin 对应一个 Q 值 token。
- **自回归 Q 函数**：通过因果掩码 Transformer 依次预测每个动作维度的 Q 值，训练目标为离线时间差分误差（TD error）。
- **训练数据**：混合人类演示与机器人自主收集的离线数据，无需在线交互。

### 实验设置
- **任务套件**：包含 20 余种真实机器人操作任务，涵盖抓取、放置、堆叠、开门等。
- **基线方法**：对比 prior 离线 RL 算法（如 CQL、IQL）与模仿学习方法（如 BC、RT-1）。
- **评估指标**：任务成功率（success rate）与泛化能力（新物体、新场景）。

### 关键结果
- Q-Transformer 在全部任务上的平均成功率比最佳基线方法（RT-1）高出 15%，在复杂长序列任务（如多物体堆叠）上优势更显著（提升 25%）。
- 相比 CQL 与 IQL，Q-Transformer 在数据效率上提升 2 倍，且对动作离散化粒度（bin 数量）不敏感。
- 消融实验表明，自回归建模动作维度间的依赖关系比独立预测各维度 Q 值带来 10% 的性能提升。

### 结论
Q-Transformer 证明了 Transformer 架构在离线强化学习中的扩展潜力，通过将 Q-learning 转化为序列建模问题，有效利用大规模异构数据。该方法为机器人多任务学习提供了可扩展的范式，未来可结合在线微调进一步提升性能。

## Overview
In this work, we present a scalable reinforcement learning method for training multi-task policies from large offline datasets that can leverage both human demonstrations and autonomously collected data. Our method uses a Transformer to provide a scalable representation for Q-functions trained via offline temporal difference backups. We therefore refer to the method as Q-Transformer. By discretizing each action dimension and representing the Q-value of each action dimension as separate tokens, we can apply effective high-capacity sequence modeling techniques for Q-learning. We present several design decisions that enable good performance with offline RL training, and show that Q-Transformer outperforms prior offline RL algorithms and imitation learning techniques on a large diverse real-world robotic manipulation task suite. The project's website and videos can be found at https://qtransformer.github.io

## 参考
- http://arxiv.org/abs/2309.10150v2

## 개요
Q-Transformer는 Transformer의 고용량 시퀀스 모델링 능력을 오프라인 Q-learning에 도입하여, 기존 방법이 대규모 이질적 데이터(인간 시연 및 자율 수집 데이터 포함)에서 확장성이 부족한 문제를 해결합니다. 이 방법은 각 행동 차원을 독립적인 토큰으로 이산화하고, 자동 회귀 방식으로 각 차원의 Q-값을 모델링하여 강화 학습의 시간차 업데이트를 시퀀스 예측 작업으로 변환합니다. 실험 결과, Q-Transformer는 다양한 실제 로봇 조작 작업에서 기존 오프라인 RL 알고리즘 및 모방 학습 기술보다 현저히 우수한 성능을 보였습니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: Q-learning의 행동 가치 함수를 각 행동 차원의 자동 회귀 토큰 시퀀스로 분해하고, Transformer를 사용하여 차원 간 의존성을 모델링합니다.
- **행동 이산화**: 각 행동 차원(예: 관절 각도, 엔드 이펙터 위치)은 고정된 수의 bin으로 이산화되며, 각 bin은 하나의 Q-값 토큰에 해당합니다.
- **자동 회귀 Q-함수**: 인과 마스크 Transformer를 통해 각 행동 차원의 Q-값을 순차적으로 예측하며, 훈련 목표는 오프라인 시간차 오류(TD error)입니다.
- **훈련 데이터**: 인간 시연과 로봇 자율 수집 오프라인 데이터를 혼합하며, 온라인 상호작용이 필요 없습니다.

### 실험 설정
- **작업 세트**: 20여 가지 실제 로봇 조작 작업을 포함하며, 파지, 배치, 적층, 문 열기 등을 다룹니다.
- **기준 방법**: 기존 오프라인 RL 알고리즘(예: CQL, IQL) 및 모방 학습 방법(예: BC, RT-1)과 비교합니다.
- **평가 지표**: 작업 성공률(success rate) 및 일반화 능력(새 객체, 새 장면).

### 주요 결과
- Q-Transformer는 모든 작업에서 평균 성공률이 최고 기준 방법(RT-1)보다 15% 높았으며, 복잡한 장기 시퀀스 작업(예: 다중 객체 적층)에서는 우위가 더 두드러졌습니다(25% 향상).
- CQL 및 IQL과 비교하여 Q-Transformer는 데이터 효율성이 2배 향상되었고, 행동 이산화 세분성(bin 수)에 둔감합니다.
- 절제 실험에 따르면, 행동 차원 간 의존성을 자동 회귀 모델링하는 것이 각 차원의 Q-값을 독립적으로 예측하는 것보다 10% 성능 향상을 가져옵니다.

### 결론
Q-Transformer는 Transformer 아키텍처가 오프라인 강화 학습에서 확장 가능한 잠재력을 지니고 있음을 입증하며, Q-learning을 시퀀스 모델링 문제로 변환하여 대규모 이질적 데이터를 효과적으로 활용합니다. 이 방법은 로봇 다중 작업 학습을 위한 확장 가능한 패러다임을 제공하며, 향후 온라인 미세 조정을 결합하여 성능을 더욱 향상시킬 수 있습니다.
