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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07730v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (924 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2510.07730v1

## 개요
DEAS는 복잡한 장기 순차 결정에서의 오프라인 강화 학습 과제를 해결하기 위해 간결하고 효과적인 프레임워크를 제안합니다. 이는 단일 단계 행동이 아닌 행동 시퀀스를 통해 가치 학습을 수행하며, 반-마르코프 결정 프로세스 Q-러닝을 통해 행동 시퀀스를 옵션으로 해석하여 유효 계획 지평을 단축합니다. 행동 시퀀스를 직접 사용할 때 발생하는 과대평가 문제를 해결하기 위해, DEAS는 분리 가치 학습을 도입하여 가치 추정을 오프라인 데이터셋 내 고수익 분포 내 행동으로 유도합니다. 실험 결과, DEAS는 OGBench의 복잡한 장기 과제에서 기준선보다 지속적으로 우수한 성능을 보였으며, 행동 시퀀스를 예측하는 대규모 Vision-Language-Action 모델의 RoboCasa Kitchen 시뮬레이션 및 실제 조작 작업에서의 성능을 향상시킬 수 있음을 확인했습니다.

## 핵심 내용
### 방법
- DEAS의 핵심 아이디어는 시간적으로 확장된 행동(행동 시퀀스)을 오프라인 강화 학습의 가치 학습 과정에 도입하는 것입니다. 이러한 시퀀스는 단일 단계 행동보다 더 풍부한 정보를 포함하며, 반-마르코프 결정 프로세스 Q-러닝을 통해 옵션 프레임워크에서 해석될 수 있어, 더 긴 시퀀스를 한 번에 고려함으로써 유효 계획 지평을 줄입니다.
- 행동 시퀀스를 직접 사용하면 actor-critic 알고리즘에서 과도한 가치 과대평가가 발생합니다. DEAS는 분리 가치 학습을 통해 이 문제를 해결하며, 가치 추정을 오프라인 데이터셋에서 고수익을 달성하는 분포 내 행동으로 유도합니다.

### 실험 설정
- OGBench의 복잡한 장기 과제에서 DEAS를 평가하고 기준선 방법과 비교합니다.
- DEAS를 행동 시퀀스를 예측하는 대규모 Vision-Language-Action 모델에 적용하여 RoboCasa Kitchen 시뮬레이션 작업 및 실제 세계 조작 작업에서 테스트합니다.

### 주요 결과
- DEAS는 OGBench 작업에서 기준선 방법보다 지속적으로 우수한 성능을 보입니다.
- RoboCasa Kitchen 시뮬레이션 작업에서 DEAS는 Vision-Language-Action 모델의 성능을 크게 향상시킵니다.
- 실제 세계 조작 작업에서도 DEAS는 상당한 성능 향상을 가져옵니다.

### 결론
DEAS는 행동 시퀀스와 분리 가치 학습을 통해 장기 과제에서 오프라인 강화 학습에 효과적이고 확장 가능한 솔루션을 제공하며, 기존 대규모 Vision-Language-Action 모델의 실제 조작 능력을 강화할 수 있습니다.
