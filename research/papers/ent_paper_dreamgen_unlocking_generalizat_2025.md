---
$id: ent_paper_dreamgen_unlocking_generalizat_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories'
  zh: 'DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories'
  ko: 'DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories'
summary:
  en: 'DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories is a 2025 work on manipulation for
    humanoid robots.'
  zh: DreamGen 是 NVIDIA 在 2025 年提出的机器人策略训练流水线，通过视频世界模型生成神经轨迹（合成机器人数据），使类人机器人仅需单一环境中的单任务遥操作数据，即可泛化执行 22 种新行为。其核心创新在于利用图像到视频生成模型适配目标机器人形态，并借助潜在动作模型或逆动力学模型从视频中恢复伪动作序列。
  ko: 'DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories is a 2025 work on manipulation for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dreamgen
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.12705v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories (arXiv)'
  url: https://arxiv.org/abs/2505.12705
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
DreamGen 是一个四阶段流水线，旨在解决机器人学习中的行为与环境泛化难题。它利用最先进的图像到视频生成模型，将其适配到目标机器人形态，生成逼真的合成视频，涵盖熟悉或新颖任务在多样化环境中的执行过程。由于生成模型仅输出视频，DreamGen 通过潜在动作模型或逆动力学模型（IDM）从视频中恢复伪动作序列。实验表明，类人机器人仅需在单一环境中收集一个拾取-放置任务的遥操作数据，即可在已知与未知环境中执行 22 种新行为。为系统评估该流水线，作者还提出了 DreamGen Bench 视频生成基准，其性能与下游策略成功率高度相关。

## 核心内容
### 方法架构
DreamGen 采用四阶段流水线：
1. **视频世界模型适配**：基于现有图像到视频生成模型（如扩散模型），通过微调使其适配目标机器人形态，生成逼真的合成视频。
2. **合成视频生成**：输入任务描述与环境图像，模型输出包含机器人执行动作的连续视频帧。
3. **伪动作恢复**：由于生成模型仅输出视频，需通过两种方式提取动作序列：
   - **潜在动作模型**：从视频帧间差异推断隐含动作。
   - **逆动力学模型（IDM）**：直接根据相邻帧预测动作。
4. **策略训练**：将恢复的伪动作序列与原始视频数据结合，训练机器人策略。

### 实验设置与关键数字
- **机器人平台**：类人机器人，仅需在单一环境中收集一个拾取-放置任务的遥操作数据。
- **泛化能力**：机器人可执行 22 种新行为，涵盖已知与未知环境。
- **基准评估**：DreamGen Bench 视频生成基准显示，其性能与下游策略成功率的相关系数显著高于传统指标。

### 结论
DreamGen 证明了通过合成视频数据生成神经轨迹，可大幅降低机器人学习对人工数据采集的依赖，为规模化训练通用机器人策略提供了新方向。代码已开源。

## Overview
We introduce DreamGen, a simple yet highly effective 4-stage pipeline for training robot policies that generalize across behaviors and environments through neural trajectories - synthetic robot data generated from video world models. DreamGen leverages state-of-the-art image-to-video generative models, adapting them to the target robot embodiment to produce photorealistic synthetic videos of familiar or novel tasks in diverse environments. Since these models generate only videos, we recover pseudo-action sequences using either a latent action model or an inverse-dynamics model (IDM). Despite its simplicity, DreamGen unlocks strong behavior and environment generalization: a humanoid robot can perform 22 new behaviors in both seen and unseen environments, while requiring teleoperation data from only a single pick-and-place task in one environment. To evaluate the pipeline systematically, we introduce DreamGen Bench, a video generation benchmark that shows a strong correlation between benchmark performance and downstream policy success. Our work establishes a promising new axis for scaling robot learning well beyond manual data collection. Code available at https://github.com/NVIDIA/GR00T-Dreams.

## 개요
DreamGen은 비디오 월드 모델에서 생성된 합성 로봇 데이터인 신경 궤적(neural trajectories)을 통해 행동과 환경 전반에 걸쳐 일반화되는 로봇 정책을 훈련하기 위한 간단하면서도 매우 효과적인 4단계 파이프라인을 소개합니다. DreamGen은 최첨단 이미지-비디오 생성 모델을 활용하여 대상 로봇 구현체에 맞게 조정함으로써 다양한 환경에서 익숙하거나 새로운 작업의 사실적인 합성 비디오를 생성합니다. 이러한 모델은 비디오만 생성하므로, 잠재 행동 모델(latent action model) 또는 역동역학 모델(IDM)을 사용하여 의사 행동 시퀀스를 복구합니다. 단순함에도 불구하고 DreamGen은 강력한 행동 및 환경 일반화를 가능하게 합니다: 휴머노이드 로봇이 하나의 환경에서 단일 픽 앤 플레이스 작업에 대한 원격 조작 데이터만 필요로 하면서, 본 환경과 미지 환경 모두에서 22가지 새로운 행동을 수행할 수 있습니다. 파이프라인을 체계적으로 평가하기 위해, 벤치마크 성능과 다운스트림 정책 성공 간의 강한 상관관계를 보여주는 비디오 생성 벤치마크인 DreamGen Bench를 소개합니다. 우리의 연구는 수동 데이터 수집을 훨씬 넘어서는 로봇 학습 확장을 위한 유망한 새로운 축을 확립합니다. 코드는 https://github.com/NVIDIA/GR00T-Dreams에서 확인할 수 있습니다.

## 핵심 내용
DreamGen은 비디오 월드 모델에서 생성된 합성 로봇 데이터인 신경 궤적(neural trajectories)을 통해 행동과 환경 전반에 걸쳐 일반화되는 로봇 정책을 훈련하기 위한 간단하면서도 매우 효과적인 4단계 파이프라인을 소개합니다. DreamGen은 최첨단 이미지-비디오 생성 모델을 활용하여 대상 로봇 구현체에 맞게 조정함으로써 다양한 환경에서 익숙하거나 새로운 작업의 사실적인 합성 비디오를 생성합니다. 이러한 모델은 비디오만 생성하므로, 잠재 행동 모델(latent action model) 또는 역동역학 모델(IDM)을 사용하여 의사 행동 시퀀스를 복구합니다. 단순함에도 불구하고 DreamGen은 강력한 행동 및 환경 일반화를 가능하게 합니다: 휴머노이드 로봇이 하나의 환경에서 단일 픽 앤 플레이스 작업에 대한 원격 조작 데이터만 필요로 하면서, 본 환경과 미지 환경 모두에서 22가지 새로운 행동을 수행할 수 있습니다. 파이프라인을 체계적으로 평가하기 위해, 벤치마크 성능과 다운스트림 정책 성공 간의 강한 상관관계를 보여주는 비디오 생성 벤치마크인 DreamGen Bench를 소개합니다. 우리의 연구는 수동 데이터 수집을 훨씬 넘어서는 로봇 학습 확장을 위한 유망한 새로운 축을 확립합니다. 코드는 https://github.com/NVIDIA/GR00T-Dreams에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2505.12705v2
