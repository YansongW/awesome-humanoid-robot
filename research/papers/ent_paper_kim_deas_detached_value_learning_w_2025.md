---
$id: ent_paper_kim_deas_detached_value_learning_w_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DEAS: DEtached value learning with Action Sequence for Scalable Offline RL'
  zh: DEAS
  ko: 'DEAS: DEtached value learning with Action Sequence for Scalable Offline RL'
summary:
  en: 'DEAS: DEtached value learning with Action Sequence for Scalable Offline RL (DEAS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST, UC Berkeley, University of Texas at Austin, NVIDIA.'
  zh: DEAS 是由 KAIST、UC Berkeley、University of Texas at Austin 与 NVIDIA 于 2025 年提出的离线强化学习框架，核心贡献在于利用动作序列进行价值学习，并通过解耦价值学习缓解估值过高问题。该方法在
    OGBench 长时域任务及 RoboCasa Kitchen 仿真与真实操作中显著超越基线，并能增强大规模 Vision-Language-Action 模型的性能。
  ko: 'DEAS: DEtached value learning with Action Sequence for Scalable Offline RL (DEAS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST, UC Berkeley, University of Texas at Austin, NVIDIA.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- deas
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07730v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DEAS: DEtached value learning with Action Sequence for Scalable Offline RL (arXiv)'
  url: https://arxiv.org/abs/2510.07730
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DEAS source
  url: https://doi.org/10.48550/arXiv.2510.07730
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
DEAS 针对离线强化学习在复杂长时域顺序决策中的挑战，提出一种简洁有效的框架。它通过动作序列（而非单步动作）进行价值学习，利用半马尔可夫决策过程 Q-learning 将动作序列解释为选项，从而缩短有效规划视界。为解决直接采用动作序列导致的估值过高问题，DEAS 引入解耦价值学习，将价值估计引导至离线数据集中高回报的分布内动作。实验表明，DEAS 在 OGBench 的复杂长时域任务上持续优于基线，并能提升预测动作序列的大规模 Vision-Language-Action 模型在 RoboCasa Kitchen 仿真与真实操作任务中的表现。

## 核心内容
### 方法
- DEAS 的核心思想是将动作序列（temporally extended actions）引入离线强化学习的价值学习过程。这些序列比单步动作包含更丰富的信息，可通过半马尔可夫决策过程 Q-learning 在选项框架下解释，从而通过一次考虑更长序列来减少有效规划视界。
- 直接采用动作序列会导致 actor-critic 算法中出现过度的价值高估。DEAS 通过解耦价值学习（detached value learning）解决此问题，将价值估计引导至离线数据集中实现高回报的分布内动作。

### 实验设置
- 在 OGBench 的复杂长时域任务上评估 DEAS，并与基线方法对比。
- 将 DEAS 应用于大规模 Vision-Language-Action 模型（该模型预测动作序列），在 RoboCasa Kitchen 仿真任务和真实世界操作任务中测试。

### 关键结果
- DEAS 在 OGBench 任务上持续优于基线方法。
- 在 RoboCasa Kitchen 仿真任务中，DEAS 显著提升了 Vision-Language-Action 模型的性能。
- 在真实世界操作任务中，DEAS 同样带来显著性能提升。

### 结论
DEAS 通过动作序列与解耦价值学习，为离线强化学习在长时域任务中提供了一种有效且可扩展的解决方案，并能增强现有大规模 Vision-Language-Action 模型的实际操作能力。

## Overview
Offline reinforcement learning (RL) presents an attractive paradigm for training intelligent agents without expensive online interactions. However, current approaches still struggle with complex, long-horizon sequential decision making. In this work, we introduce DEtached value learning with Action Sequence (DEAS), a simple yet effective offline RL framework that leverages action sequences for value learning. These temporally extended actions provide richer information than single-step actions and can be interpreted through the options framework via semi-Markov decision process Q-learning, enabling reduction of the effective planning horizon by considering longer sequences at once. However, directly adopting such sequences in actor-critic algorithms introduces excessive value overestimation, which we address through detached value learning that steers value estimates toward in-distribution actions that achieve high return in the offline dataset. We demonstrate that DEAS consistently outperforms baselines on complex, long-horizon tasks from OGBench and can be applied to enhance the performance of large-scale Vision-Language-Action models that predict action sequences, significantly boosting performance in both RoboCasa Kitchen simulation tasks and real-world manipulation tasks.

## 개요
오프라인 강화 학습(Offline RL)은 비용이 많이 드는 온라인 상호작용 없이 지능형 에이전트를 훈련할 수 있는 매력적인 패러다임을 제공합니다. 그러나 현재 접근 방식은 복잡하고 장기적인 순차적 의사 결정에 여전히 어려움을 겪고 있습니다. 본 연구에서는 행동 시퀀스를 활용한 가치 학습을 위한 간단하면서도 효과적인 오프라인 RL 프레임워크인 DEtached value learning with Action Sequence (DEAS)를 소개합니다. 이러한 시간적으로 확장된 행동은 단일 단계 행동보다 더 풍부한 정보를 제공하며, 반-마르코프 결정 과정 Q-러닝을 통해 옵션 프레임워크로 해석될 수 있어, 한 번에 더 긴 시퀀스를 고려함으로써 효과적인 계획 지평을 단축시킵니다. 그러나 액터-크리틱 알고리즘에서 이러한 시퀀스를 직접 채택하면 과도한 가치 과대평가가 발생하며, 이를 분리된 가치 학습(detached value learning)을 통해 해결하여 오프라인 데이터셋에서 높은 보상을 달성하는 분포 내 행동으로 가치 추정을 유도합니다. 우리는 DEAS가 OGBench의 복잡하고 장기적인 작업에서 기준 모델을 일관되게 능가하며, 행동 시퀀스를 예측하는 대규모 비전-언어-행동 모델의 성능을 향상시키는 데 적용될 수 있음을 입증하여, RoboCasa Kitchen 시뮬레이션 작업과 실제 조작 작업 모두에서 성능을 크게 향상시킵니다.

## 핵심 내용
오프라인 강화 학습(Offline RL)은 비용이 많이 드는 온라인 상호작용 없이 지능형 에이전트를 훈련할 수 있는 매력적인 패러다임을 제공합니다. 그러나 현재 접근 방식은 복잡하고 장기적인 순차적 의사 결정에 여전히 어려움을 겪고 있습니다. 본 연구에서는 행동 시퀀스를 활용한 가치 학습을 위한 간단하면서도 효과적인 오프라인 RL 프레임워크인 DEtached value learning with Action Sequence (DEAS)를 소개합니다. 이러한 시간적으로 확장된 행동은 단일 단계 행동보다 더 풍부한 정보를 제공하며, 반-마르코프 결정 과정 Q-러닝을 통해 옵션 프레임워크로 해석될 수 있어, 한 번에 더 긴 시퀀스를 고려함으로써 효과적인 계획 지평을 단축시킵니다. 그러나 액터-크리틱 알고리즘에서 이러한 시퀀스를 직접 채택하면 과도한 가치 과대평가가 발생하며, 이를 분리된 가치 학습(detached value learning)을 통해 해결하여 오프라인 데이터셋에서 높은 보상을 달성하는 분포 내 행동으로 가치 추정을 유도합니다. 우리는 DEAS가 OGBench의 복잡하고 장기적인 작업에서 기준 모델을 일관되게 능가하며, 행동 시퀀스를 예측하는 대규모 비전-언어-행동 모델의 성능을 향상시키는 데 적용될 수 있음을 입증하여, RoboCasa Kitchen 시뮬레이션 작업과 실제 조작 작업 모두에서 성능을 크게 향상시킵니다.

## 参考
- http://arxiv.org/abs/2510.07730v1
