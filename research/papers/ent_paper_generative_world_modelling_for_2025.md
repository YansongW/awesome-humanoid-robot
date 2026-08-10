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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07092v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (908 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2510.07092v1

## 개요
세계 모델은 AI와 로봇 분야의 중요한 패러다임으로, 에이전트가 시각적 관측 또는 컴팩트한 잠재 상태를 예측하여 미래를 추론할 수 있게 한다. 1X World Model Challenge는 이를 위해 실제 인간-로봇 상호작용 데이터를 기반으로 한 오픈소스 벤치마크를 제공하며, 샘플링과 압축이라는 두 가지 상호 보완적인 트랙을 포함한다. 샘플링 트랙에서 팀은 비디오 생성 기반 모델 Wan-2.2 TI2V-5B를 비디오-상태 조건화된 미래 프레임 예측기로 개조하고, AdaLN-Zero를 통해 로봇 상태 정보를 주입하며, LoRA를 사용하여 사후 훈련을 수행했다. 압축 트랙에서는 처음부터 시공간 Transformer 모델을 훈련했다. 최종 결과는 샘플링 작업에서 23.0 dB PSNR, 압축 작업에서 Top-500 CE 6.6386을 달성하여 두 트랙 모두에서 우승했다.

## 핵심 내용
### 방법 개요
- **샘플링 작업**: Wan-2.2 TI2V-5B 비디오 생성 모델을 기반으로, 이를 조건화된 미래 프레임 예측기로 확장했다. AdaLN-Zero 메커니즘을 통해 로봇 상태(예: 관절 각도, 속도)를 조건으로 모델에 주입하고, LoRA를 사용하여 효율적인 미세 조정을 수행함으로써 모델이 현재 관측과 상태를 기반으로 후속 이미지 프레임을 생성할 수 있게 했다.
- **압축 작업**: 처음부터 Spatio-Temporal Transformer 모델을 훈련하여 미래 프레임의 이산 잠재 코드(discrete latent codes)를 직접 예측함으로써 더 컴팩트한 상태 표현을 구현했다.

### 실험 설정
- 벤치마크 데이터는 1X World Model Challenge에서 제공하는 실제 인간형 로봇 상호작용 데이터 세트에서 비롯되었으며, 다중 모달 센서 기록을 포함한다.
- 샘플링 작업의 평가 지표는 PSNR(피크 신호 대 잡음비)이고, 압축 작업의 평가 지표는 Top-500 CE(교차 엔트로피)이다.

### 주요 결과
- **샘플링 작업**: PSNR이 23.0 dB에 도달하여 기준 방법보다 현저히 우수했다.
- **압축 작업**: Top-500 CE가 6.6386으로, 압축 효율과 예측 정확도 사이의 균형을 달성했다.
- 팀은 두 트랙 모두에서 1위를 차지하여 제안된 방법이 실제 인간형 로봇 세계 모델링에서의 효과성을 검증했다.

### 결론
이 작업은 대규모 비디오 생성 모델과 로봇 상태 조건화의 결합 효과를 보여주었으며, 처음부터 훈련된 시공간 Transformer가 이산 잠재 코드 예측에서 경쟁력을 가짐을 입증했다. 오픈소스 벤치마크와 우승 솔루션은 미래 인간형 로봇의 세계 모델 연구에 중요한 참고 자료를 제공한다.
