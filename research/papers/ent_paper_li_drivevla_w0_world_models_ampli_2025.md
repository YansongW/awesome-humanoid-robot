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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.12796v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
대규모 데이터에서 Vision-Language-Action(VLA) 모델을 확장하는 것은 보다 일반화된 주행 지능을 달성하기 위한 유망한 경로를 제공합니다. 그러나 VLA 모델은 "감독 결핍(supervision deficit)"이라는 한계를 가집니다: 방대한 모델 용량이 희소하고 저차원적인 행동(action)으로 감독되어, 표현력의 상당 부분이 제대로 활용되지 못합니다. 이를 해결하기 위해, 우리는 **DriveVLA-W0**를 제안합니다. 이는 세계 모델링(world modeling)을 활용하여 미래 이미지를 예측하는 훈련 패러다임입니다. 이 작업은 밀집된 자기 지도 신호(self-supervised signal)를 생성하여 모델이 주행 환경의 근본적인 역학(dynamics)을 학습하도록 강제합니다. 우리는 이 패러다임의 다재다능함을 두 가지 주요 VLA 유형에 적용하여 보여줍니다: 이산 시각 토큰(discrete visual tokens)을 사용하는 VLA를 위한 자기회귀 세계 모델(autoregressive world model)과 연속 시각 특징(continuous visual features)에서 작동하는 VLA를 위한 확산 세계 모델(diffusion world model)입니다. 세계 모델링에서 학습된 풍부한 표현을 기반으로, 실시간 배포를 위한 추론 지연 시간(inference latency)을 해결하기 위해 경량 행동 전문가(lightweight action expert)를 도입합니다. NAVSIM v1/v2 벤치마크와 680배 더 큰 사내 데이터셋(in-house dataset)에서의 광범위한 실험은 DriveVLA-W0가 BEV 및 VLA 기준선(baselines)을 크게 능가함을 보여줍니다. 결정적으로, 이는 데이터 스케일링 법칙(data scaling law)을 강화하여 훈련 데이터셋 크기가 증가함에 따라 성능 향상이 가속화됨을 나타냅니다.

## 핵심 내용
대규모 데이터에서 Vision-Language-Action(VLA) 모델을 확장하는 것은 보다 일반화된 주행 지능을 달성하기 위한 유망한 경로를 제공합니다. 그러나 VLA 모델은 "감독 결핍(supervision deficit)"이라는 한계를 가집니다: 방대한 모델 용량이 희소하고 저차원적인 행동(action)으로 감독되어, 표현력의 상당 부분이 제대로 활용되지 못합니다. 이를 해결하기 위해, 우리는 **DriveVLA-W0**를 제안합니다. 이는 세계 모델링(world modeling)을 활용하여 미래 이미지를 예측하는 훈련 패러다임입니다. 이 작업은 밀집된 자기 지도 신호(self-supervised signal)를 생성하여 모델이 주행 환경의 근본적인 역학(dynamics)을 학습하도록 강제합니다. 우리는 이 패러다임의 다재다능함을 두 가지 주요 VLA 유형에 적용하여 보여줍니다: 이산 시각 토큰(discrete visual tokens)을 사용하는 VLA를 위한 자기회귀 세계 모델(autoregressive world model)과 연속 시각 특징(continuous visual features)에서 작동하는 VLA를 위한 확산 세계 모델(diffusion world model)입니다. 세계 모델링에서 학습된 풍부한 표현을 기반으로, 실시간 배포를 위한 추론 지연 시간(inference latency)을 해결하기 위해 경량 행동 전문가(lightweight action expert)를 도입합니다. NAVSIM v1/v2 벤치마크와 680배 더 큰 사내 데이터셋(in-house dataset)에서의 광범위한 실험은 DriveVLA-W0가 BEV 및 VLA 기준선(baselines)을 크게 능가함을 보여줍니다. 결정적으로, 이는 데이터 스케일링 법칙(data scaling law)을 강화하여 훈련 데이터셋 크기가 증가함에 따라 성능 향상이 가속화됨을 나타냅니다.

## 参考
- http://arxiv.org/abs/2510.12796v2
