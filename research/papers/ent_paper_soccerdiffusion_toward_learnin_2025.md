---
$id: ent_paper_soccerdiffusion_toward_learnin_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings'
  zh: 'SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings'
  ko: 'SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings'
summary:
  en: 'SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings is a 2025 work on locomotion
    for humanoid robots.'
  zh: SoccerDiffusion 是 2025 年提出的一种基于 Transformer 的扩散模型，用于从真实比赛录像中学习人形机器人足球的端到端控制策略。该模型通过多模态传感器输入预测关节指令轨迹，并采用蒸馏技术实现嵌入式平台的实时推理。实验表明，模型能复现行走、踢球和跌倒恢复等复杂动作，为后续强化学习提供了坚实基础。
  ko: 'SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- soccerdiffusion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.20808v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings (arXiv)'
  url: https://arxiv.org/abs/2504.20808
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
SoccerDiffusion 利用从 RoboCup 竞赛中收集的数据，训练一个 Transformer 架构的扩散模型，直接从视觉、本体感知和游戏状态等多模态输入中预测关节轨迹。通过蒸馏技术将多步扩散过程压缩为单步推理，使得模型能够在嵌入式平台上实时运行。在仿真和实体机器人上的实验显示，该模型能够成功复现行走、踢球和跌倒恢复等复杂运动行为，尽管高级战术行为仍有限制。这项工作为后续的强化学习或偏好优化方法提供了稳健的基础。

## 核心内容
### 方法
- 模型架构：基于 Transformer 的扩散模型，输入包括视觉、本体感知和游戏状态等多模态传感器数据，输出为关节命令轨迹。
- 训练数据：使用从 RoboCup 竞赛中收集的真实比赛录像。
- 推理优化：采用蒸馏技术将多步扩散过程压缩为单步推理，实现嵌入式平台的实时运行。

### 实验设置
- 测试环境：在仿真环境和实体人形机器人上分别进行验证。
- 评估指标：重点考察模型复现行走、踢球和跌倒恢复等复杂运动行为的能力。

### 关键结果
- 模型成功复现了行走、踢球和跌倒恢复等复杂运动行为。
- 高级战术行为（如团队配合）仍存在局限性，但为后续强化学习或偏好优化方法提供了稳健基础。

### 结论
SoccerDiffusion 展示了从真实比赛录像中学习端到端人形机器人足球控制策略的可行性，为后续研究提供了数据集、预训练模型和代码（https://bit-bots.github.io/SoccerDiffusion）。

## Overview
This paper introduces SoccerDiffusion, a transformer-based diffusion model designed to learn end-to-end control policies for humanoid robot soccer directly from real-world gameplay recordings. Using data collected from RoboCup competitions, the model predicts joint command trajectories from multi-modal sensor inputs, including vision, proprioception, and game state. We employ a distillation technique to enable real-time inference on embedded platforms that reduces the multi-step diffusion process to a single step. Our results demonstrate the model's ability to replicate complex motion behaviors such as walking, kicking, and fall recovery both in simulation and on physical robots. Although high-level tactical behavior remains limited, this work provides a robust foundation for subsequent reinforcement learning or preference optimization methods. We release the dataset, pretrained models, and code under: https://bit-bots.github.io/SoccerDiffusion

## 개요
본 논문은 실제 경기 녹화 데이터로부터 직접 휴머노이드 로봇 축구의 엔드투엔드 제어 정책을 학습하도록 설계된 트랜스포머 기반 확산 모델인 SoccerDiffusion을 소개합니다. RoboCup 대회에서 수집된 데이터를 사용하여, 이 모델은 시각, 고유수용감각, 게임 상태를 포함한 다중 모달 센서 입력으로부터 관절 명령 궤적을 예측합니다. 우리는 임베디드 플랫폼에서 실시간 추론을 가능하게 하는 증류 기법을 사용하여 다단계 확산 과정을 단일 단계로 축소합니다. 실험 결과는 시뮬레이션과 실제 로봇 모두에서 걷기, 차기, 낙상 회복과 같은 복잡한 동작 행동을 복제할 수 있는 모델의 능력을 보여줍니다. 높은 수준의 전술적 행동은 여전히 제한적이지만, 이 연구는 후속 강화 학습 또는 선호도 최적화 방법을 위한 견고한 기반을 제공합니다. 우리는 데이터셋, 사전 학습된 모델, 코드를 https://bit-bots.github.io/SoccerDiffusion 에서 공개합니다.

## 핵심 내용
본 논문은 실제 경기 녹화 데이터로부터 직접 휴머노이드 로봇 축구의 엔드투엔드 제어 정책을 학습하도록 설계된 트랜스포머 기반 확산 모델인 SoccerDiffusion을 소개합니다. RoboCup 대회에서 수집된 데이터를 사용하여, 이 모델은 시각, 고유수용감각, 게임 상태를 포함한 다중 모달 센서 입력으로부터 관절 명령 궤적을 예측합니다. 우리는 임베디드 플랫폼에서 실시간 추론을 가능하게 하는 증류 기법을 사용하여 다단계 확산 과정을 단일 단계로 축소합니다. 실험 결과는 시뮬레이션과 실제 로봇 모두에서 걷기, 차기, 낙상 회복과 같은 복잡한 동작 행동을 복제할 수 있는 모델의 능력을 보여줍니다. 높은 수준의 전술적 행동은 여전히 제한적이지만, 이 연구는 후속 강화 학습 또는 선호도 최적화 방법을 위한 견고한 기반을 제공합니다. 우리는 데이터셋, 사전 학습된 모델, 코드를 https://bit-bots.github.io/SoccerDiffusion 에서 공개합니다.

## 参考
- http://arxiv.org/abs/2504.20808v2
