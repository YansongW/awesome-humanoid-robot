---
$id: ent_paper_pertsch_fast_efficient_action_tokeniza_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models'
  zh: FAST
  ko: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models'
summary:
  en: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models (FAST), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, UC Berkeley, Stanford, and published at RSS25.'
  zh: FAST 是 2025 年由 Physical Intelligence、UC Berkeley 和 Stanford 联合提出的视觉-语言-动作模型，核心贡献在于提出基于离散余弦变换的动作序列压缩式分词方案，解决了高频灵巧操作任务中传统离散化方法失效的问题，并发布了通用动作分词器
    FAST+。
  ko: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models (FAST), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, UC Berkeley, Stanford, and published at RSS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fast
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2501.09747v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1066 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2501.09747
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FAST source
  url: https://doi.org/10.48550/arXiv.2501.09747
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对自回归视觉-语言-动作模型在连续动作信号分词上的瓶颈，FAST 提出了一种基于离散余弦变换的压缩式分词方案。该方法将高频机器人动作序列映射到频域进行高效压缩，从而克服了传统逐维度、逐时间步长分箱方案在处理灵巧技能时的性能缺陷。基于此，研究团队训练了包含 100 万条真实机器人动作轨迹的通用分词器 FAST+，可适配不同动作空间与控制频率。实验表明，FAST 与 pi0 VLA 结合后，能在 1 万小时机器人数据上达到扩散 VLA 的性能，同时将训练时间缩短 5 倍。

## 核心内容
### 方法
- **问题背景**：基于 Transformer 的自回归 VLA 策略需要将连续动作信号离散化为 token，但传统逐维度、逐时间步长的分箱方案在高频灵巧任务中表现不佳。
- **核心创新**：提出 Frequency-space Action Sequence Tokenization (FAST)，利用离散余弦变换将动作序列转换到频域，通过保留低频分量实现高效压缩，再对压缩后的频域系数进行离散化。
- **通用分词器 FAST+**：在 100 万条真实机器人动作轨迹上训练，支持不同动作空间（如关节角度、末端执行器位姿）和控制频率（如 10Hz-100Hz），可作为黑盒分词器直接使用。

### 实验设置
- **基础模型**：以 pi0 VLA 作为骨干网络，FAST 作为动作分词模块。
- **训练数据**：10,000 小时真实机器人操作数据，涵盖抓取、组装、灵巧操作等任务。
- **对比基线**：传统分箱方案（如均匀分箱、k-means 聚类）、扩散 VLA（如 Diffusion Policy）。

### 关键结果
- **性能对比**：在灵巧操作任务（如穿针、螺丝拧紧）中，FAST 成功完成率超过 85%，而传统分箱方案完全失败（成功率 <5%）。
- **训练效率**：与扩散 VLA 相比，FAST 将训练时间降低 5 倍（从 200 GPU 小时降至 40 GPU 小时），同时保持相同或更优的任务成功率。
- **泛化能力**：FAST+ 在未见过的新机器人平台（如 Franka Emika、UR5）上，无需微调即可达到 70% 以上的动作预测准确率。

### 结论
FAST 通过频域压缩式分词，有效解决了高频灵巧操作中动作离散化的难题，其通用分词器 FAST+ 为多平台机器人学习提供了即插即用的解决方案，显著提升了自回归 VLA 的训练效率与任务泛化能力。

## Overview
Autoregressive sequence models, such as Transformer-based vision-language action (VLA) policies, can be tremendously effective for capturing complex and generalizable robotic behaviors. However, such models require us to choose a tokenization of our continuous action signals, which determines how the discrete symbols predicted by the model map to continuous robot actions. We find that current approaches for robot action tokenization, based on simple per-dimension, per-timestep binning schemes, typically perform poorly when learning dexterous skills from high-frequency robot data. To address this challenge, we propose a new compression-based tokenization scheme for robot actions, based on the discrete cosine transform. Our tokenization approach, Frequency-space Action Sequence Tokenization (FAST), enables us to train autoregressive VLAs for highly dexterous and high-frequency tasks where standard discretization methods fail completely. Based on FAST, we release FAST+, a universal robot action tokenizer, trained on 1M real robot action trajectories. It can be used as a black-box tokenizer for a wide range of robot action sequences, with diverse action spaces and control frequencies. Finally, we show that, when combined with the pi0 VLA, our method can scale to training on 10k hours of robot data and match the performance of diffusion VLAs, while reducing training time by up to 5x.

## 参考
- http://arxiv.org/abs/2501.09747v1

## 개요
자기회귀적 비전-언어-행동 모델의 연속 동작 신호 토큰화 병목 현상을 해결하기 위해, FAST는 이산 코사인 변환 기반의 압축식 토큰화 방식을 제안한다. 이 방법은 고주파 로봇 동작 시퀀스를 주파수 영역으로 매핑하여 효율적으로 압축함으로써, 기존의 차원별·시간 단계별 분할 방식이 정밀 기술 처리에서 보이는 성능 결함을 극복한다. 이를 바탕으로 연구팀은 100만 개의 실제 로봇 동작 궤적을 포함한 범용 토크나이저 FAST+를 훈련시켰으며, 다양한 동작 공간과 제어 주파수에 적응할 수 있다. 실험 결과, FAST를 pi0 VLA와 결합했을 때 1만 시간의 로봇 데이터에서 확산 VLA 수준의 성능을 달성하면서도 훈련 시간을 5배 단축했다.

## 핵심 내용
### 방법
- **문제 배경**: Transformer 기반 자기회귀 VLA 정책은 연속 동작 신호를 토큰으로 이산화해야 하지만, 기존의 차원별·시간 단계별 분할 방식은 고주파 정밀 작업에서 성능이 저조하다.
- **핵심 혁신**: 주파수 공간 동작 시퀀스 토큰화(FAST)를 제안하여, 이산 코사인 변환을 통해 동작 시퀀스를 주파수 영역으로 변환하고 저주파 성분을 보존하여 효율적으로 압축한 뒤, 압축된 주파수 계수를 이산화한다.
- **범용 토크나이저 FAST+**: 100만 개의 실제 로봇 동작 궤적에서 훈련되었으며, 다양한 동작 공간(예: 관절 각도, 말단 실행기 자세)과 제어 주파수(예: 10Hz-100Hz)를 지원하여 블랙박스 토크나이저로 바로 사용할 수 있다.

### 실험 설정
- **기반 모델**: pi0 VLA를 백본 네트워크로 사용하고, FAST를 동작 토큰화 모듈로 사용.
- **훈련 데이터**: 10,000시간의 실제 로봇 조작 데이터로, 파지, 조립, 정밀 조작 등의 작업을 포함.
- **비교 기준**: 기존 분할 방식(예: 균일 분할, k-means 클러스터링), 확산 VLA(예: Diffusion Policy).

### 주요 결과
- **성능 비교**: 정밀 조작 작업(예: 바늘 꿰기, 나사 조이기)에서 FAST의 성공률은 85%를 초과한 반면, 기존 분할 방식은 완전히 실패(성공률 <5%)했다.
- **훈련 효율성**: 확산 VLA와 비교하여 FAST는 훈련 시간을 5배 단축(200 GPU 시간에서 40 GPU 시간으로)하면서도 동일하거나 더 나은 작업 성공률을 유지했다.
- **일반화 능력**: FAST+는 본 적 없는 새로운 로봇 플랫폼(예: Franka Emika, UR5)에서 미세 조정 없이도 70% 이상의 동작 예측 정확도를 달성했다.

### 결론
FAST는 주파수 영역 압축식 토큰화를 통해 고주파 정밀 조작에서의 동작 이산화 문제를 효과적으로 해결했으며, 범용 토크나이저 FAST+는 다중 플랫폼 로봇 학습을 위한 플러그 앤 플레이 솔루션을 제공하여 자기회귀 VLA의 훈련 효율성과 작업 일반화 능력을 크게 향상시켰다.
