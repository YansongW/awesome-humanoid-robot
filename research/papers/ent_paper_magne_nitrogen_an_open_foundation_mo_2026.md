---
$id: ent_paper_magne_nitrogen_an_open_foundation_mo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NitroGen: An Open Foundation Model for Generalist Gaming Agents'
  zh: NitroGen
  ko: 'NitroGen: An Open Foundation Model for Generalist Gaming Agents'
summary:
  en: 'NitroGen: An Open Foundation Model for Generalist Gaming Agents (NitroGen), is a 2026 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, Stanford, Caltech, UChicago, UT Austin.'
  zh: NitroGen 是 NVIDIA、Stanford、Caltech、UChicago、UT Austin 于 2026 年提出的视觉-动作基础模型，专为通用游戏智能体设计。其核心贡献在于构建了包含 40,000 小时、覆盖 1,000
    余款游戏的互联网规模视频-动作数据集，并实现了跨游戏泛化能力，在未见过的游戏中任务成功率相对提升最高达 52%。
  ko: 'NitroGen: An Open Foundation Model for Generalist Gaming Agents (NitroGen), is a 2026 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, Stanford, Caltech, UChicago, UT Austin.'
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
- nitrogen
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.02427v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'NitroGen: An Open Foundation Model for Generalist Gaming Agents (arXiv)'
  url: https://arxiv.org/abs/2601.02427
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
NitroGen 是一个面向通用游戏智能体的视觉-动作基础模型，训练数据来自超过 1,000 款游戏的 40,000 小时游戏视频。该模型通过三个关键创新实现跨游戏泛化：自动从公开游戏视频中提取玩家动作构建大规模数据集、设计多游戏基准环境评估泛化能力、以及采用统一视觉-动作模型进行大规模行为克隆。实验表明，NitroGen 在 3D 动作游戏的战斗场景、2D 平台游戏的高精度控制以及程序生成世界的探索任务中均表现优异，且能有效迁移至未见游戏，任务成功率相比从头训练的模型提升最高达 52%。研究团队已开源数据集、评估套件与模型权重。

## 核心内容
### 方法
NitroGen 采用统一的视觉-动作模型架构，通过大规模行为克隆进行训练。其核心数据构建方法为：从公开游戏视频中自动提取玩家动作，形成互联网规模的视频-动作数据集。该数据集包含 40,000 小时、覆盖 1,000 余款游戏的 gameplay 视频。

### 架构
模型为视觉-动作基础模型，直接以游戏画面作为输入，输出对应的动作指令。训练过程不依赖游戏引擎或内部状态信息，仅通过视觉观察与动作序列的映射关系学习。

### 实验设置
- **训练数据**：40,000 小时 gameplay 视频，涵盖 1,000+ 款游戏
- **基准环境**：专门设计的多游戏基准环境，用于测量跨游戏泛化能力
- **对比方法**：与从头训练的模型进行对比

### 关键结果
- 在 3D 动作游戏的战斗场景中表现优异
- 在 2D 平台游戏中实现高精度控制
- 在程序生成世界中具备探索能力
- **跨游戏迁移**：在未见过的游戏中，任务成功率相对提升最高达 52%

### 结论
NitroGen 证明了通过大规模行为克隆训练视觉-动作模型，能够实现通用游戏智能体的跨游戏泛化能力。研究团队已开源数据集、评估套件与模型权重，以推动通用具身智能体的研究发展。

## Overview
We introduce NitroGen, a vision-action foundation model for generalist gaming agents that is trained on 40,000 hours of gameplay videos across more than 1,000 games. We incorporate three key ingredients: 1) an internet-scale video-action dataset constructed by automatically extracting player actions from publicly available gameplay videos, 2) a multi-game benchmark environment that can measure cross-game generalization, and 3) a unified vision-action model trained with large-scale behavior cloning. NitroGen exhibits strong competence across diverse domains, including combat encounters in 3D action games, high-precision control in 2D platformers, and exploration in procedurally generated worlds. It transfers effectively to unseen games, achieving up to 52% relative improvement in task success rates over models trained from scratch. We release the dataset, evaluation suite, and model weights to advance research on generalist embodied agents.

## 개요
우리는 1,000개 이상의 게임에서 40,000시간의 게임플레이 비디오로 훈련된 범용 게임 에이전트를 위한 비전-행동 기반 모델인 NitroGen을 소개합니다. 우리는 세 가지 핵심 요소를 통합했습니다: 1) 공개된 게임플레이 비디오에서 플레이어 행동을 자동으로 추출하여 구축한 인터넷 규모의 비디오-행동 데이터셋, 2) 교차 게임 일반화를 측정할 수 있는 다중 게임 벤치마크 환경, 3) 대규모 행동 복제로 훈련된 통합 비전-행동 모델입니다. NitroGen은 3D 액션 게임의 전투, 2D 플랫포머의 고정밀 제어, 절차적으로 생성된 세계의 탐험 등 다양한 도메인에서 뛰어난 능력을 보여줍니다. 보지 못한 게임에도 효과적으로 전이되어, 처음부터 훈련된 모델 대비 작업 성공률에서 최대 52%의 상대적 향상을 달성합니다. 우리는 범용 임베디드 에이전트 연구를 발전시키기 위해 데이터셋, 평가 스위트, 모델 가중치를 공개합니다.

## 핵심 내용
우리는 1,000개 이상의 게임에서 40,000시간의 게임플레이 비디오로 훈련된 범용 게임 에이전트를 위한 비전-행동 기반 모델인 NitroGen을 소개합니다. 우리는 세 가지 핵심 요소를 통합했습니다: 1) 공개된 게임플레이 비디오에서 플레이어 행동을 자동으로 추출하여 구축한 인터넷 규모의 비디오-행동 데이터셋, 2) 교차 게임 일반화를 측정할 수 있는 다중 게임 벤치마크 환경, 3) 대규모 행동 복제로 훈련된 통합 비전-행동 모델입니다. NitroGen은 3D 액션 게임의 전투, 2D 플랫포머의 고정밀 제어, 절차적으로 생성된 세계의 탐험 등 다양한 도메인에서 뛰어난 능력을 보여줍니다. 보지 못한 게임에도 효과적으로 전이되어, 처음부터 훈련된 모델 대비 작업 성공률에서 최대 52%의 상대적 향상을 달성합니다. 우리는 범용 임베디드 에이전트 연구를 발전시키기 위해 데이터셋, 평가 스위트, 모델 가중치를 공개합니다.

## 参考
- http://arxiv.org/abs/2601.02427v1
