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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.12705v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (808 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2505.12705v2

## 개요
DreamGen은 로봇 학습에서의 행동 및 환경 일반화 문제를 해결하기 위해 설계된 4단계 파이프라인입니다. 최첨단 이미지-투-비디오 생성 모델을 활용하여 목표 로봇 형태에 적응시키고, 다양한 환경에서 익숙하거나 새로운 작업의 실행을 포함하는 사실적인 합성 비디오를 생성합니다. 생성 모델은 비디오만 출력하므로, DreamGen은 잠재 행동 모델 또는 역동역학 모델(IDM)을 통해 비디오에서 의사 행동 시퀀스를 복구합니다. 실험에 따르면, 인간형 로봇이 단일 환경에서 하나의 픽 앤 플레이스 작업에 대한 원격 조작 데이터만 수집하면, 알려진 환경과 알려지지 않은 환경에서 22가지 새로운 행동을 수행할 수 있습니다. 이 파이프라인을 체계적으로 평가하기 위해, 저자들은 또한 DreamGen Bench 비디오 생성 벤치마크를 제안했으며, 그 성능은 하위 정책 성공률과 높은 상관관계를 보입니다.

## 핵심 내용
### 방법 아키텍처
DreamGen은 4단계 파이프라인을 채택합니다:
1. **비디오 세계 모델 적응**: 기존 이미지-투-비디오 생성 모델(예: 확산 모델)을 기반으로, 미세 조정을 통해 목표 로봇 형태에 적응시키고 사실적인 합성 비디오를 생성합니다.
2. **합성 비디오 생성**: 작업 설명과 환경 이미지를 입력하면, 모델은 로봇의 행동 실행을 포함한 연속 비디오 프레임을 출력합니다.
3. **의사 행동 복구**: 생성 모델은 비디오만 출력하므로, 두 가지 방법으로 행동 시퀀스를 추출해야 합니다:
   - **잠재 행동 모델**: 비디오 프레임 간 차이에서 암시적 행동을 추론합니다.
   - **역동역학 모델(IDM)**: 인접 프레임을 기반으로 직접 행동을 예측합니다.
4. **정책 훈련**: 복구된 의사 행동 시퀀스를 원본 비디오 데이터와 결합하여 로봇 정책을 훈련합니다.

### 실험 설정 및 주요 수치
- **로봇 플랫폼**: 인간형 로봇으로, 단일 환경에서 하나의 픽 앤 플레이스 작업에 대한 원격 조작 데이터만 필요합니다.
- **일반화 능력**: 로봇은 알려진 환경과 알려지지 않은 환경을 포함한 22가지 새로운 행동을 수행할 수 있습니다.
- **벤치마크 평가**: DreamGen Bench 비디오 생성 벤치마크는 하위 정책 성공률과의 상관 계수가 전통적인 지표보다 유의미하게 높음을 보여줍니다.

### 결론
DreamGen은 합성 비디오 데이터를 통한 신경 궤적 생성이 로봇 학습에서 수동 데이터 수집에 대한 의존도를 크게 줄일 수 있음을 입증하며, 범용 로봇 정책의 대규모 훈련을 위한 새로운 방향을 제시합니다. 코드는 오픈소스로 공개되었습니다.
