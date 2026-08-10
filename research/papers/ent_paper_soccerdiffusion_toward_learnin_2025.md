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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.20808v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (658 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2504.20808v2

## 개요
SoccerDiffusion은 RoboCup 대회에서 수집된 데이터를 활용하여, Transformer 아키텍처 기반의 확산 모델을 훈련하고, 시각, 고유수용감각, 게임 상태 등 다중 모달 입력에서 직접 관절 궤적을 예측합니다. 증류 기술을 통해 다단계 확산 과정을 단일 단계 추론으로 압축하여, 모델이 임베디드 플랫폼에서 실시간으로 실행될 수 있게 합니다. 시뮬레이션 및 실제 로봇 실험에서, 이 모델은 걷기, 공 차기, 낙상 회복과 같은 복잡한 운동 행동을 성공적으로 재현할 수 있음을 보여주었지만, 고급 전술 행동에는 여전히 한계가 있습니다. 이 작업은 후속 강화 학습 또는 선호 최적화 방법에 견고한 기반을 제공합니다.

## 핵심 내용
### 방법
- 모델 아키텍처: Transformer 기반의 확산 모델로, 입력에는 시각, 고유수용감각, 게임 상태 등 다중 모달 센서 데이터가 포함되며, 출력은 관절 명령 궤적입니다.
- 훈련 데이터: RoboCup 대회에서 수집된 실제 경기 녹화를 사용합니다.
- 추론 최적화: 증류 기술을 사용하여 다단계 확산 과정을 단일 단계 추론으로 압축하여, 임베디드 플랫폼에서 실시간 실행을 구현합니다.

### 실험 설정
- 테스트 환경: 시뮬레이션 환경과 실제 휴머노이드 로봇에서 각각 검증을 수행합니다.
- 평가 지표: 걷기, 공 차기, 낙상 회복과 같은 복잡한 운동 행동을 재현하는 모델의 능력에 중점을 둡니다.

### 주요 결과
- 모델은 걷기, 공 차기, 낙상 회복과 같은 복잡한 운동 행동을 성공적으로 재현했습니다.
- 고급 전술 행동(예: 팀워크)에는 여전히 한계가 있지만, 후속 강화 학습 또는 선호 최적화 방법에 견고한 기반을 제공합니다.

### 결론
SoccerDiffusion은 실제 경기 녹화에서 엔드투엔드 휴머노이드 축구 제어 정책을 학습하는 가능성을 보여주며, 후속 연구를 위해 데이터셋, 사전 훈련 모델 및 코드(https://bit-bots.github.io/SoccerDiffusion)를 제공합니다.
