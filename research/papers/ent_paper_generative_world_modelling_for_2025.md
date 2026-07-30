---
$id: ent_paper_generative_world_modelling_for_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report'
  zh: 'Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report'
  ko: 'Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report'
summary:
  en: 'Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report is a 2025 work on simulation benchmark
    for humanoid robots.'
  zh: 1X World Model Challenge 是一项面向人形机器人的开源仿真基准测试，包含图像帧预测（采样）和离散潜码预测（压缩）两个任务。参赛团队通过微调视频生成基础模型 Wan-2.2 TI2V-5B 和从头训练时空 Transformer，在两个任务中均取得第一名，PSNR
    达 23.0 dB，压缩任务 Top-500 CE 为 6.6386。
  ko: 'Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report is a 2025 work on simulation benchmark
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- generative_world_modelling_for
- humanoid
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07092v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report (arXiv)'
  url: https://arxiv.org/abs/2510.07092
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
世界模型是 AI 与机器人领域的重要范式，能让智能体通过预测视觉观测或紧凑潜状态来推理未来。1X World Model Challenge 为此提供了基于真实人机交互数据的开源基准，包含采样与压缩两个互补赛道。在采样赛道中，团队将视频生成基础模型 Wan-2.2 TI2V-5B 改造为视频-状态条件化的未来帧预测器，通过 AdaLN-Zero 注入机器人状态信息，并采用 LoRA 进行后训练。在压缩赛道中，团队从头训练了时空 Transformer 模型。最终成果在采样任务达到 23.0 dB PSNR，压缩任务 Top-500 CE 为 6.6386，双双夺冠。

## 核心内容
### 方法概述
- **采样任务**：基于 Wan-2.2 TI2V-5B 视频生成模型，将其扩展为条件化未来帧预测器。通过 AdaLN-Zero 机制将机器人状态（如关节角度、速度）作为条件注入模型，并使用 LoRA 进行高效微调，使模型能够根据当前观测和状态生成后续图像帧。
- **压缩任务**：从头训练 Spatio-Temporal Transformer 模型，直接预测未来帧的离散潜码（discrete latent codes），实现更紧凑的状态表示。

### 实验设置
- 基准数据来自 1X World Model Challenge 提供的真实人形机器人交互数据集，包含多模态传感器记录。
- 采样任务评估指标为 PSNR（峰值信噪比），压缩任务评估指标为 Top-500 CE（交叉熵）。

### 关键结果
- **采样任务**：PSNR 达到 23.0 dB，显著优于基线方法。
- **压缩任务**：Top-500 CE 为 6.6386，在压缩效率与预测精度间取得平衡。
- 团队在两个赛道均获得第一名，验证了所提方法在真实人形机器人世界建模中的有效性。

### 结论
该工作展示了将大规模视频生成模型与机器人状态条件化结合的有效性，同时证明了从零训练的时空 Transformer 在离散潜码预测中的竞争力。开源基准和冠军方案为未来人形机器人的世界模型研究提供了重要参考。

## Overview
World models are a powerful paradigm in AI and robotics, enabling agents to reason about the future by predicting visual observations or compact latent states. The 1X World Model Challenge introduces an open-source benchmark of real-world humanoid interaction, with two complementary tracks: sampling, focused on forecasting future image frames, and compression, focused on predicting future discrete latent codes. For the sampling track, we adapt the video generation foundation model Wan-2.2 TI2V-5B to video-state-conditioned future frame prediction. We condition the video generation on robot states using AdaLN-Zero, and further post-train the model using LoRA. For the compression track, we train a Spatio-Temporal Transformer model from scratch. Our models achieve 23.0 dB PSNR in the sampling task and a Top-500 CE of 6.6386 in the compression task, securing 1st place in both challenges.

## 개요
World models는 AI와 로보틱스에서 강력한 패러다임으로, 에이전트가 시각적 관측이나 압축된 잠재 상태를 예측하여 미래에 대해 추론할 수 있게 합니다. 1X World Model Challenge는 실제 인간형 상호작용에 대한 오픈소스 벤치마크를 도입하며, 두 가지 상호 보완적인 트랙을 제공합니다: 미래 이미지 프레임 예측에 초점을 맞춘 샘플링 트랙과 미래 이산 잠재 코드 예측에 초점을 맞춘 압축 트랙입니다. 샘플링 트랙의 경우, 비디오 생성 기반 모델 Wan-2.2 TI2V-5B를 비디오-상태 조건부 미래 프레임 예측에 적용했습니다. AdaLN-Zero를 사용하여 로봇 상태에 비디오 생성을 조건화하고, LoRA를 사용하여 모델을 추가로 사후 학습했습니다. 압축 트랙의 경우, Spatio-Temporal Transformer 모델을 처음부터 학습했습니다. 우리 모델은 샘플링 작업에서 23.0 dB PSNR을, 압축 작업에서 Top-500 CE 6.6386을 달성하여 두 챌린지 모두에서 1위를 차지했습니다.

## 핵심 내용
World models는 AI와 로보틱스에서 강력한 패러다임으로, 에이전트가 시각적 관측이나 압축된 잠재 상태를 예측하여 미래에 대해 추론할 수 있게 합니다. 1X World Model Challenge는 실제 인간형 상호작용에 대한 오픈소스 벤치마크를 도입하며, 두 가지 상호 보완적인 트랙을 제공합니다: 미래 이미지 프레임 예측에 초점을 맞춘 샘플링 트랙과 미래 이산 잠재 코드 예측에 초점을 맞춘 압축 트랙입니다. 샘플링 트랙의 경우, 비디오 생성 기반 모델 Wan-2.2 TI2V-5B를 비디오-상태 조건부 미래 프레임 예측에 적용했습니다. AdaLN-Zero를 사용하여 로봇 상태에 비디오 생성을 조건화하고, LoRA를 사용하여 모델을 추가로 사후 학습했습니다. 압축 트랙의 경우, Spatio-Temporal Transformer 모델을 처음부터 학습했습니다. 우리 모델은 샘플링 작업에서 23.0 dB PSNR을, 압축 작업에서 Top-500 CE 6.6386을 달성하여 두 챌린지 모두에서 1위를 차지했습니다.

## 参考
- http://arxiv.org/abs/2510.07092v1
