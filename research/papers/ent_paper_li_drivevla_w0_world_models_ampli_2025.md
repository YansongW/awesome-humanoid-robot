---
$id: ent_paper_li_drivevla_w0_world_models_ampli_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving'
  zh: DriveVLA-W0
  ko: 'DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving'
summary:
  en: 'DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving (DriveVLA-W0), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Yinwang Intelligent Technology Co. Ltd., NLPR, Institute of Automation,
    Chinese Academy of Sciences (CASIA).'
  zh: DriveVLA-W0 是由银翼智能科技有限公司、中国科学院自动化研究所模式识别国家重点实验室（NLPR）于 2025 年提出的视觉-语言-动作（VLA）模型训练范式。其核心贡献在于通过世界模型预测未来图像，生成密集自监督信号以弥补
    VLA 模型在稀疏动作监督下的“监督赤字”，从而显著提升驾驶智能的泛化能力。
  ko: 'DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving (DriveVLA-W0), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Yinwang Intelligent Technology Co. Ltd., NLPR, Institute of Automation,
    Chinese Academy of Sciences (CASIA).'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- drivevla_w0
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.12796v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (787 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2510.12796
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DriveVLA-W0 source
  url: https://doi.org/10.48550/arXiv.2510.12796
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
DriveVLA-W0 针对 VLA 模型在自动驾驶中因稀疏低维动作监督导致表征能力利用不足的问题，提出利用世界模型预测未来图像作为辅助任务。该范式通过生成密集自监督信号，迫使模型学习驾驶环境的底层动态规律。研究团队为两种主流 VLA 架构分别设计了对应的世界模型：基于离散视觉 token 的自回归世界模型，以及基于连续视觉特征的扩散世界模型。在 NAVSIM v1/v2 基准测试和规模扩大 680 倍的内部数据集上，DriveVLA-W0 显著优于 BEV 和 VLA 基线方法，并展现出数据规模扩大时性能增益加速的特性。

## 核心内容
### 方法架构
- **核心问题**：VLA 模型在大规模数据训练时存在“监督赤字”，即模型容量远大于稀疏动作标签所能提供的监督信号，导致表征能力未被充分利用。
- **解决方案**：引入世界模型预测未来图像作为辅助任务，生成密集自监督信号，迫使模型学习驾驶环境的动态演化规律。
- **双架构适配**：
  - 对于使用离散视觉 token 的 VLA 模型，采用自回归世界模型进行未来帧预测。
  - 对于基于连续视觉特征的 VLA 模型，采用扩散世界模型进行未来帧生成。

### 轻量级动作专家
- 在通过世界模型学习到丰富表征后，引入轻量级动作专家模块，专门处理动作预测任务，以降低推理延迟，满足实时部署需求。

### 实验设置与结果
- **基准测试**：在 NAVSIM v1/v2 基准上进行评估，同时使用规模扩大 680 倍的内部数据集进行验证。
- **性能对比**：DriveVLA-W0 显著优于 BEV 基线方法和传统 VLA 基线方法。
- **数据缩放定律**：关键发现是 DriveVLA-W0 放大了数据缩放定律，即随着训练数据集规模增大，性能增益呈现加速趋势，而非线性增长。

## Overview
Scaling Vision-Language-Action (VLA) models on large-scale data offers a promising path to achieving a more generalized driving intelligence. However, VLA models are limited by a ``supervision deficit'': the vast model capacity is supervised by sparse, low-dimensional actions, leaving much of their representational power underutilized. To remedy this, we propose \textbf{DriveVLA-W0}, a training paradigm that employs world modeling to predict future images. This task generates a dense, self-supervised signal that compels the model to learn the underlying dynamics of the driving environment. We showcase the paradigm's versatility by instantiating it for two dominant VLA archetypes: an autoregressive world model for VLAs that use discrete visual tokens, and a diffusion world model for those operating on continuous visual features. Building on the rich representations learned from world modeling, we introduce a lightweight action expert to address the inference latency for real-time deployment. Extensive experiments on the NAVSIM v1/v2 benchmark and a 680x larger in-house dataset demonstrate that DriveVLA-W0 significantly outperforms BEV and VLA baselines. Crucially, it amplifies the data scaling law, showing that performance gains accelerate as the training dataset size increases.

## Overview
Scaling Vision-Language-Action (VLA) models on large-scale data offers a promising path to achieving a more generalized driving intelligence. However, VLA models are limited by a "supervision deficit": the vast model capacity is supervised by sparse, low-dimensional actions, leaving much of their representational power underutilized. To remedy this, we propose **DriveVLA-W0**, a training paradigm that employs world modeling to predict future images. This task generates a dense, self-supervised signal that compels the model to learn the underlying dynamics of the driving environment. We showcase the paradigm's versatility by instantiating it for two dominant VLA archetypes: an autoregressive world model for VLAs that use discrete visual tokens, and a diffusion world model for those operating on continuous visual features. Building on the rich representations learned from world modeling, we introduce a lightweight action expert to address the inference latency for real-time deployment. Extensive experiments on the NAVSIM v1/v2 benchmark and a 680x larger in-house dataset demonstrate that DriveVLA-W0 significantly outperforms BEV and VLA baselines. Crucially, it amplifies the data scaling law, showing that performance gains accelerate as the training dataset size increases.

## Content
Scaling Vision-Language-Action (VLA) models on large-scale data offers a promising path to achieving a more generalized driving intelligence. However, VLA models are limited by a "supervision deficit": the vast model capacity is supervised by sparse, low-dimensional actions, leaving much of their representational power underutilized. To remedy this, we propose **DriveVLA-W0**, a training paradigm that employs world modeling to predict future images. This task generates a dense, self-supervised signal that compels the model to learn the underlying dynamics of the driving environment. We showcase the paradigm's versatility by instantiating it for two dominant VLA archetypes: an autoregressive world model for VLAs that use discrete visual tokens, and a diffusion world model for those operating on continuous visual features. Building on the rich representations learned from world modeling, we introduce a lightweight action expert to address the inference latency for real-time deployment. Extensive experiments on the NAVSIM v1/v2 benchmark and a 680x larger in-house dataset demonstrate that DriveVLA-W0 significantly outperforms BEV and VLA baselines. Crucially, it amplifies the data scaling law, showing that performance gains accelerate as the training dataset size increases.

## 参考
- http://arxiv.org/abs/2510.12796v2

## 개요
DriveVLA-W0는 자율주행에서 VLA 모델이 희소하고 저차원적인 동작 감독으로 인해 표현 능력을 충분히 활용하지 못하는 문제를 해결하기 위해, 세계 모델을 활용한 미래 이미지 예측을 보조 작업으로 제안한다. 이 패러다임은 밀집된 자기 지도 신호를 생성하여 모델이 주행 환경의 기저 동적 규칙을 학습하도록 강제한다. 연구팀은 두 가지 주요 VLA 아키텍처에 각각 대응하는 세계 모델을 설계했다: 이산 시각 토큰 기반의 자기회귀 세계 모델과 연속 시각 특징 기반의 확산 세계 모델이다. NAVSIM v1/v2 벤치마크와 680배 확장된 내부 데이터셋에서 DriveVLA-W0는 BEV 및 VLA 기준 방법보다 현저히 우수한 성능을 보였으며, 데이터 규모가 확장될수록 성능 이득이 가속화되는 특성을 입증했다.

## 핵심 내용
### 방법 아키텍처
- **핵심 문제**: VLA 모델은 대규모 데이터 훈련 시 '감독 적자(supervision deficit)'를 겪는다. 즉, 모델 용량이 희소한 동작 라벨이 제공할 수 있는 감독 신호보다 훨씬 커서 표현 능력이 충분히 활용되지 못한다.
- **해결 방안**: 세계 모델을 도입하여 미래 이미지 예측을 보조 작업으로 사용하고, 밀집된 자기 지도 신호를 생성하여 모델이 주행 환경의 동적 진화 규칙을 학습하도록 강제한다.
- **이중 아키텍처 적응**:
  - 이산 시각 토큰을 사용하는 VLA 모델의 경우, 자기회귀 세계 모델을 통해 미래 프레임을 예측한다.
  - 연속 시각 특징 기반의 VLA 모델의 경우, 확산 세계 모델을 통해 미래 프레임을 생성한다.

### 경량 동작 전문가
- 세계 모델을 통해 풍부한 표현을 학습한 후, 경량 동작 전문가 모듈을 도입하여 동작 예측 작업을 전담 처리함으로써 추론 지연을 줄이고 실시간 배포 요구 사항을 충족한다.

### 실험 설정 및 결과
- **벤치마크 테스트**: NAVSIM v1/v2 벤치마크에서 평가를 수행하고, 680배 확장된 내부 데이터셋으로 검증을 진행했다.
- **성능 비교**: DriveVLA-W0는 BEV 기준 방법과 기존 VLA 기준 방법보다 현저히 우수한 성능을 보였다.
- **데이터 스케일링 법칙**: 핵심 발견은 DriveVLA-W0가 데이터 스케일링 법칙을 증폭시킨다는 점이다. 즉, 훈련 데이터셋 규모가 커질수록 성능 이득이 선형적 증가가 아닌 가속화되는 추세를 보인다.
