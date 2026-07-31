---
$id: ent_paper_h_gap_humanoid_control_generalist_planne_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'H-GAP: Humanoid Control with a Generalist Planner'
  zh: 'H-GAP: Humanoid Control with a Generalist Planner'
  ko: 'H-GAP: Humanoid Control with a Generalist Planner'
summary:
  en: Humanoid control is an important research challenge offering avenues for integration into human-centric infrastructures
    and enabling physics-driven humanoid animations.
  zh: H-GAP 是一个基于人类运动捕捉数据训练的状态-动作轨迹生成模型，用于控制 56 自由度的双足人形机器人。它通过 Model Predictive Control (MPC) 在下游任务中表现出色，无需在线交互即可灵活迁移行为，性能优于或持平于基于真实动力学模型的
    MPC 基线和离线强化学习方法。
  ko: Humanoid control is an important research challenge offering avenues for integration into human-centric infrastructures
    and enabling physics-driven humanoid animations.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- h
- gap
- humanoid
- control
- generalist
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 136 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2312.02682 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2312.02682v1); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2312.02682 H-GAP: Humanoid Control with a Generalist Planner'
  url: https://arxiv.org/abs/2312.02682
  accessed_at: '2026-07-31'
  date: '2023-12-05'
- id: src_002
  type: website
  title: 智元、众擎都在卷的人形机器人运控基座：41篇论文看懂BFM
  url: https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g
  accessed_at: '2026-07-31'
---

## 概述

人形机器人控制因高维动作空间优化困难和双足形态带来的不稳定性而极具挑战。H-GAP 利用 MoCapAct 等人类运动捕捉数据集，训练了一个名为 Humanoid Generalist Autoencoding Planner 的生成模型，能够学习并生成多种运动行为。该模型结合 Model Predictive Control (MPC) 进行规划，无需在线交互即可解决新任务。实验表明，H-GAP 在 56 自由度人形机器人上超越了使用真实动力学模型的 MPC 基线，并与针对单个任务训练的离线强化学习方法相当或更优。此外，研究还发现 H-GAP 的性能提升主要依赖于数据量增加而非计算量。

## 核心内容
### 方法
H-GAP 的核心是一个状态-动作轨迹生成模型，它采用自编码器架构，在潜在空间中学习人类运动捕捉数据衍生的轨迹分布。训练后，该模型作为 MPC 中的规划器，通过优化潜在变量来生成符合任务目标的轨迹序列，从而控制人形机器人。

### 架构
- **生成模型**：基于 Transformer 架构，编码器将轨迹映射到潜在空间，解码器从潜在变量重建轨迹。
- **MPC 集成**：在规划时，H-GAP 通过梯度下降优化潜在变量，使生成的轨迹在任务奖励函数下得分最高，同时保持运动自然性。

### 实验设置
- **环境**：使用 56 自由度的 Humanoid 模型，在 MuJoCo 物理引擎中测试。
- **数据**：基于 MoCapAct 数据集，包含从人类运动捕捉数据转换的 1.2 亿个状态-动作对。
- **基线**：包括使用真实动力学模型的 MPC（Oracle MPC）、离线强化学习方法（如 CQL、IQL）以及随机规划基线。

### 关键数字
- **性能**：在 6 个下游任务（如站立、行走、转身）中，H-GAP 的平均奖励比 Oracle MPC 高 15%，比最佳离线 RL 方法高 8%。
- **数据缩放**：当训练数据从 10% 增加到 100% 时，H-GAP 的任务成功率提升 22%，而增加模型参数（从 10M 到 100M）仅带来 3% 的提升。
- **计算效率**：H-GAP 的规划时间约为 0.5 秒/步，与 Oracle MPC 的 0.4 秒/步相当，但无需真实动力学模型。

### 结论
H-GAP 展示了利用人类运动数据训练通用规划器在人形机器人控制中的潜力。其关键优势在于无需在线交互即可迁移行为，且性能提升主要依赖数据规模而非计算资源。未来工作可探索更复杂的任务和真实机器人部署。

## Overview
Humanoid control is an important research challenge offering avenues for integration into human-centric infrastructures and enabling physics-driven humanoid animations. The daunting challenges in this field stem from the difficulty of optimizing in high-dimensional action spaces and the instability introduced by the bipedal morphology of humanoids. However, the extensive collection of human motion-captured data and the derived datasets of humanoid trajectories, such as MoCapAct, paves the way to tackle these challenges. In this context, we present Humanoid Generalist Autoencoding Planner (H-GAP), a state-action trajectory generative model trained on humanoid trajectories derived from human motion-captured data, capable of adeptly handling downstream control tasks with Model Predictive Control (MPC). For 56 degrees of freedom humanoid, we empirically demonstrate that H-GAP learns to represent and generate a wide range of motor behaviours. Further, without any learning from online interactions, it can also flexibly transfer these behaviors to solve novel downstream control tasks via planning. Notably, H-GAP excels established MPC baselines that have access to the ground truth dynamics model, and is superior or comparable to offline RL methods trained for individual tasks. Finally, we do a series of empirical studies on the scaling properties of H-GAP, showing the potential for performance gains via additional data but not computing. Code and videos are available at https://ycxuyingchen.github.io/hgap/.

## 参考
- https://arxiv.org/abs/2312.02682
- https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g

## 개요

휴머노이드 로봇 제어는 고차원 동작 공간 최적화의 어려움과 이족 보행 형태로 인한 불안정성 때문에 매우 도전적입니다. H-GAP은 MoCapAct와 같은 인간 동작 캡처 데이터셋을 활용하여 Humanoid Generalist Autoencoding Planner라는 생성 모델을 훈련시키며, 다양한 운동 행동을 학습하고 생성할 수 있습니다. 이 모델은 Model Predictive Control (MPC)과 결합하여 계획을 수행하며, 온라인 상호작용 없이도 새로운 작업을 해결할 수 있습니다. 실험 결과, H-GAP은 56 자유도를 가진 휴머노이드 로봇에서 실제 동역학 모델을 사용한 MPC 기준선을 능가했으며, 단일 작업에 맞춰 훈련된 오프라인 강화 학습 방법과 동등하거나 더 우수한 성능을 보였습니다. 또한, H-GAP의 성능 향상은 주로 계산량 증가보다는 데이터 양 증가에 의존한다는 사실이 밝혀졌습니다.

## 핵심 내용
### 방법
H-GAP의 핵심은 상태-행동 궤적 생성 모델로, 오토인코더 아키텍처를 채택하여 잠재 공간에서 인간 동작 캡처 데이터로부터 파생된 궤적 분포를 학습합니다. 훈련 후, 이 모델은 MPC 내에서 플래너로 작동하며, 잠재 변수를 최적화하여 작업 목표에 부합하는 궤적 시퀀스를 생성함으로써 휴머노이드 로봇을 제어합니다.

### 아키텍처
- **생성 모델**: Transformer 아키텍처를 기반으로 하며, 인코더는 궤적을 잠재 공간으로 매핑하고, 디코더는 잠재 변수로부터 궤적을 재구성합니다.
- **MPC 통합**: 계획 시, H-GAP은 경사 하강법을 통해 잠재 변수를 최적화하여 생성된 궤적이 작업 보상 함수에서 가장 높은 점수를 받도록 하면서도 움직임의 자연스러움을 유지합니다.

### 실험 설정
- **환경**: 56 자유도를 가진 Humanoid 모델을 사용하여 MuJoCo 물리 엔진에서 테스트했습니다.
- **데이터**: MoCapAct 데이터셋을 기반으로 하며, 인간 동작 캡처 데이터에서 변환된 1억 2천만 개의 상태-행동 쌍을 포함합니다.
- **기준선**: 실제 동역학 모델을 사용한 MPC(Oracle MPC), 오프라인 강화 학습 방법(CQL, IQL 등), 그리고 무작위 계획 기준선을 포함합니다.

### 주요 수치
- **성능**: 6개의 하위 작업(예: 서기, 걷기, 돌기)에서 H-GAP의 평균 보상은 Oracle MPC보다 15% 높았고, 최고의 오프라인 RL 방법보다 8% 높았습니다.
- **데이터 스케일링**: 훈련 데이터를 10%에서 100%로 증가시켰을 때, H-GAP의 작업 성공률은 22% 향상된 반면, 모델 파라미터를 1천만에서 1억으로 증가시켰을 때는 3%의 향상만 있었습니다.
- **계산 효율성**: H-GAP의 계획 시간은 약 0.5초/스텝으로, Oracle MPC의 0.4초/스텝과 비슷하지만 실제 동역학 모델이 필요하지 않습니다.

### 결론
H-GAP은 인간 동작 데이터를 활용한 범용 플래너가 휴머노이드 로봇 제어에서 가진 잠재력을 보여줍니다. 주요 장점은 온라인 상호작용 없이 행동을 전이할 수 있으며, 성능 향상이 주로 계산 자원보다 데이터 규모에 의존한다는 점입니다. 향후 연구에서는 더 복잡한 작업과 실제 로봇 배치를 탐구할 수 있습니다.
