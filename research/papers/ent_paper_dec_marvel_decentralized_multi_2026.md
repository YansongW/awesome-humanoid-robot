---
$id: ent_paper_dec_marvel_decentralized_multi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under Budget Constraints'
  zh: 'Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under Budget Constraints'
  ko: 'Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under Budget Constraints'
summary:
  en: 'arXiv:2607.09060v1 Announce Type: new Abstract: Multi-UAV exploration is often constrained by unreliable communication,
    limited field-of-view sensing (e.g., lightweight onboard camera), and finite travel budgets that require each robot to
    reserve enough budget to return to its base. We present Dec-MARVEL, a decentralized budget-aware exploration framework
    for communication-free teams with directional sensing. Rather than exchanging maps, goals, or messages, each robot coordinates
    through its incidental observations: any teammate trajectory within its field of view serves as a coordination signal.
    A graph-attention actor fuses local frontier geometry, teammate motion, and budget features to select return-feasible
    waypoint-heading actions. The actor is trained with phase-conditioned critics, a training-only task-oriented privileged
    critic, and a mixture-based budget curriculum. Across 900 held-out trials spanning three team sizes (2, 4, 8 robots) and
    three travel budgets (720, 800, 1024 meters) against four baselines, Dec-MARVEL achieves the highest or tied-highest exploration
    rate and lowest sensing overlap across all nine team-size budget configurations. Under our tightest 720m budget, it reaches
    53%, 94%, and 100% success for 2, 4, and 8 robots, versus 37%, 83%, and 99% for the strongest baseline. Physical-robot
    experiments demonstrate successful sim-to-real transfer and real-world deployment of Dec-MARVEL.'
  zh: Dec-MARVEL 是一个面向无通信多无人机团队的分散式预算感知探索框架。其核心贡献在于利用每个机器人视野内的队友轨迹作为隐式协调信号，并采用图注意力网络融合局部前沿几何、队友运动与预算特征，从而在无通信条件下选择可返回基地的航点-航向动作。该框架在
    900 次保留试验中，于三种团队规模（2、4、8 机器人）和三种旅行预算（720、800、1024 米）下，均实现了最高或并列最高的探索率与最低的感知重叠。
  ko: 'arXiv:2607.09060v1 Announce Type: new Abstract: Multi-UAV exploration is often constrained by unreliable communication,
    limited field-of-view sensing (e.g., lightweight onboard camera), and finite travel budgets that require each robot to
    reserve enough budget to return to its base. We present Dec-MARVEL, a decentralized budget-aware exploration framework
    for communication-free teams with directional sensing. Rather than exchanging maps, goals, or messages, each robot coordinates
    through its incidental observations: any teammate trajectory within its field of view serves as a coordination signal.
    A graph-attention actor fuses local frontier geometry, teammate motion, and budget features to select return-feasible
    waypoint-heading actions. The actor is trained with phase-conditioned critics, a training-only task-oriented privileged
    critic, and a mixture-based budget curriculum. Across 900 held-out trials spanning three team sizes (2, 4, 8 robots) and
    three travel budgets (720, 800, 1024 meters) against four baselines, Dec-MARVEL achieves the highest or tied-highest exploration
    rate and lowest sensing overlap across all nine team-size budget configurations. Under our tightest 720m budget, it reaches
    53%, 94%, and 100% success for 2, 4, and 8 robots, versus 37%, 83%, and 99% for the strongest baseline. Physical-robot
    experiments demonstrate successful sim-to-real transfer and real-world deployment of Dec-MARVEL.'
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
- dec_marvel
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09060v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under Budget Constraints (arXiv)'
  url: https://arxiv.org/abs/2607.09060
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Dec-MARVEL 解决了多无人机探索中通信不可靠、视野受限以及有限旅行预算（需预留返程能量）的挑战。它不依赖地图、目标或消息交换，而是通过每个机器人视野内偶然观察到的队友轨迹作为协调信号。其核心是一个图注意力演员网络，该网络融合局部前沿几何、队友运动与预算特征，以选择可返回基地的航点-航向动作。训练过程采用阶段条件评论家、仅用于训练的任务导向特权评论家以及基于混合的预算课程。在涵盖三种团队规模和三种预算的 900 次试验中，Dec-MARVEL 在所有九种配置下均优于四种基线方法，尤其在 720 米最紧预算下，2、4、8 机器人的成功率分别达到 53%、94% 和 100%。实物机器人实验验证了其从仿真到现实的成功迁移与部署。

## 核心内容
### 方法概述
Dec-MARVEL 的核心思想是利用“偶然观察”实现无通信协调：每个机器人将其视野内观察到的任何队友轨迹作为隐式协调信号，从而避免显式地图或消息交换。该框架采用图注意力网络（graph-attention actor）作为动作选择器，其输入特征包括：
- **局部前沿几何**：机器人当前视野内的未探索区域边界信息。
- **队友运动**：视野内观察到的队友轨迹，用于推断其意图。
- **预算特征**：当前剩余旅行预算，确保所选动作可返回基地。

### 训练策略
演员网络通过以下机制进行训练：
- **阶段条件评论家（phase-conditioned critics）**：根据探索阶段调整奖励信号。
- **任务导向特权评论家（task-oriented privileged critic）**：仅在训练时使用，提供基于全局信息的额外监督。
- **基于混合的预算课程（mixture-based budget curriculum）**：逐步增加预算约束的难度，提升模型在紧预算下的鲁棒性。

### 实验设置与结果
- **实验规模**：900 次保留试验，覆盖三种团队规模（2、4、8 机器人）和三种旅行预算（720、800、1024 米）。
- **基线对比**：与四种基线方法比较，Dec-MARVEL 在所有九种团队规模-预算配置下均达到最高或并列最高的探索率，以及最低的感知重叠。
- **关键数字**：
  - 在 720 米最紧预算下，2、4、8 机器人的成功率分别为 53%、94% 和 100%，而最强基线仅为 37%、83% 和 99%。
  - 在 800 米和 1024 米预算下，Dec-MARVEL 同样保持领先。
- **实物验证**：实物机器人实验成功实现了从仿真到现实的迁移，验证了 Dec-MARVEL 在真实环境中的部署可行性。

## Overview
Multi-UAV exploration is often constrained by unreliable communication, limited field-of-view sensing (e.g., lightweight onboard camera), and finite travel budgets that require each robot to reserve enough budget to return to its base. We present Dec-MARVEL, a decentralized budget-aware exploration framework for communication-free teams with directional sensing. Rather than exchanging maps, goals, or messages, each robot coordinates through its incidental observations: any teammate trajectory within its field of view serves as a coordination signal. A graph-attention actor fuses local frontier geometry, teammate motion, and budget features to select return-feasible waypoint-heading actions. The actor is trained with phase-conditioned critics, a training-only task-oriented privileged critic, and a mixture-based budget curriculum. Across 900 held-out trials spanning three team sizes (2, 4, 8 robots) and three travel budgets (720, 800, 1024 meters) against four baselines, Dec-MARVEL achieves the highest or tied-highest exploration rate and lowest sensing overlap across all nine team-size budget configurations. Under our tightest 720m budget, it reaches 53%, 94%, and 100% success for 2, 4, and 8 robots, versus 37%, 83%, and 99% for the strongest baseline. Physical-robot experiments demonstrate successful sim-to-real transfer and real-world deployment of Dec-MARVEL.

## 개요
다중 UAV 탐사는 종종 신뢰할 수 없는 통신, 제한된 시야 센싱(예: 경량 온보드 카메라), 그리고 각 로봇이 기지로 돌아갈 충분한 예산을 확보해야 하는 유한 이동 예산에 의해 제약을 받습니다. 본 논문에서는 방향성 센싱을 사용하는 통신 없는 팀을 위한 분산형 예산 인식 탐사 프레임워크인 Dec-MARVEL을 제시합니다. 각 로봇은 지도, 목표 또는 메시지를 교환하는 대신 우연한 관찰을 통해 협력합니다. 즉, 시야 내에 있는 동료의 궤적이 협력 신호 역할을 합니다. 그래프 어텐션 액터는 로컬 프론티어 기하학, 동료 움직임 및 예산 특징을 융합하여 복귀 가능한 웨이포인트-헤딩 행동을 선택합니다. 액터는 단계 조건부 비평가, 훈련 전용 작업 지향 특권 비평가, 그리고 혼합 기반 예산 커리큘럼으로 훈련됩니다. 세 가지 팀 규모(2, 4, 8대 로봇)와 세 가지 이동 예산(720, 800, 1024미터)을 포함한 900개의 보류된 시험에서 네 가지 기준선과 비교했을 때, Dec-MARVEL은 모든 9가지 팀 규모-예산 구성에서 가장 높거나 동등한 탐사율과 가장 낮은 센싱 중복을 달성합니다. 가장 엄격한 720m 예산 하에서 2, 4, 8대 로봇에 대해 각각 53%, 94%, 100%의 성공률을 기록하며, 이는 가장 강력한 기준선의 37%, 83%, 99%와 대비됩니다. 실제 로봇 실험을 통해 Dec-MARVEL의 시뮬레이션-실제 전환 및 실제 환경 배치 성공을 입증합니다.

## 핵심 내용
다중 UAV 탐사는 종종 신뢰할 수 없는 통신, 제한된 시야 센싱(예: 경량 온보드 카메라), 그리고 각 로봇이 기지로 돌아갈 충분한 예산을 확보해야 하는 유한 이동 예산에 의해 제약을 받습니다. 본 논문에서는 방향성 센싱을 사용하는 통신 없는 팀을 위한 분산형 예산 인식 탐사 프레임워크인 Dec-MARVEL을 제시합니다. 각 로봇은 지도, 목표 또는 메시지를 교환하는 대신 우연한 관찰을 통해 협력합니다. 즉, 시야 내에 있는 동료의 궤적이 협력 신호 역할을 합니다. 그래프 어텐션 액터는 로컬 프론티어 기하학, 동료 움직임 및 예산 특징을 융합하여 복귀 가능한 웨이포인트-헤딩 행동을 선택합니다. 액터는 단계 조건부 비평가, 훈련 전용 작업 지향 특권 비평가, 그리고 혼합 기반 예산 커리큘럼으로 훈련됩니다. 세 가지 팀 규모(2, 4, 8대 로봇)와 세 가지 이동 예산(720, 800, 1024미터)을 포함한 900개의 보류된 시험에서 네 가지 기준선과 비교했을 때, Dec-MARVEL은 모든 9가지 팀 규모-예산 구성에서 가장 높거나 동등한 탐사율과 가장 낮은 센싱 중복을 달성합니다. 가장 엄격한 720m 예산 하에서 2, 4, 8대 로봇에 대해 각각 53%, 94%, 100%의 성공률을 기록하며, 이는 가장 강력한 기준선의 37%, 83%, 99%와 대비됩니다. 실제 로봇 실험을 통해 Dec-MARVEL의 시뮬레이션-실제 전환 및 실제 환경 배치 성공을 입증합니다.

## 参考
- http://arxiv.org/abs/2607.09060v2
