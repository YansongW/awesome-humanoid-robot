---
$id: ent_paper_won_dual_stream_diffusion_for_worl_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model
  zh: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model
  ko: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model
summary:
  en: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model (Dual-Stream Diffusion for World-Model
    Augmented Vision-Language-Action Model), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by KAIST, RLWRLD.
  zh: DUST 是由 KAIST 和 RLWRLD 提出的 2025 年大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于通过双流扩散 Transformer 架构，在联合预测状态与动作时弥合模态差异，并引入异步采样方法提升推理性能。在模拟和真实任务中，DUST
    相比现有基线方法取得了显著性能提升。
  ko: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model (Dual-Stream Diffusion for World-Model
    Augmented Vision-Language-Action Model), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by KAIST, RLWRLD.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dual_stream_diffusion_for_worl
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.27607v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model (arXiv)
  url: https://arxiv.org/abs/2510.27607
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model source
  url: https://doi.org/10.48550/arXiv.2510.27607
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
DUST 框架通过双流扩散 Transformer 设计，分别维护视觉、语言和动作的独立模态流，同时允许跨模态知识共享。它采用独立噪声扰动和解耦流匹配损失来学习模态间的因果关系，并引入异步采样方法对动作和视觉令牌进行推理时缩放。在 RoboCasa 和 GR-1 等模拟基准上，DUST 相比最先进的 VLA 和世界模型基线方法实现了最高 6% 的性能提升，推理时缩放额外带来 2-5% 的改进。在 Franka Research 3 真实机器人任务中，DUST 的成功率比基线方法高出 10%。

## 核心内容
### 方法架构
- **双流扩散 Transformer**：DUST 的核心是维持视觉、语言和动作的独立模态流，同时通过交叉注意力机制实现跨模态知识共享，避免模态差异导致的联合预测困难。
- **独立噪声扰动与解耦流匹配损失**：对每个模态流施加独立的噪声扰动，并使用解耦的流匹配损失来学习跨模态因果关系，从而更有效地建模状态与动作的联合分布。
- **异步采样方法**：在推理时，对动作令牌和视觉令牌采用异步采样策略，通过调整采样步数或顺序来提升生成质量，实现推理时计算缩放。

### 实验设置与关键结果
- **模拟基准**：在 RoboCasa 和 GR-1 等模拟环境中，DUST 相比最先进的 VLA 和世界模型基线方法（如 RT-2、UniPi）实现了最高 6% 的性能提升。推理时缩放额外带来 2-5% 的改进。
- **真实世界任务**：使用 Franka Research 3 机械臂进行真实操作任务，DUST 的成功率比基线方法高出 10%，验证了其在真实场景中的有效性。
- **迁移学习能力**：DUST 支持通过无动作视频进行预训练，以及使用异构机器人数据集和人类数据集进行联合训练，展示了强大的迁移学习能力。

### 结论
DUST 通过双流扩散框架有效解决了 VLA 模型与世界模型联合预测中的模态差异问题，在模拟和真实任务中均取得了显著性能提升，并具备良好的迁移学习能力。

## Overview
Augmenting vision-language-action models (VLAs) with world models is promising for robotic policy learning but faces challenges in jointly predicting states and actions due to the modality gap. To address this, we propose DUal-STream diffusion (DUST), a world-model augmented VLA framework featuring a multimodal diffusion transformer that maintains separate modality streams while enabling cross-modal knowledge sharing. In addition, DUST utilizes independent noise perturbations and a decoupled flow matching loss to learn cross-modal causal relationships. We further introduce an asynchronous sampling method for action and vision tokens that enhances performance through inference-time scaling. Experimental results on simulated benchmarks like RoboCasa and GR-1 show that DUST achieves up to 6% gains over state-of-the-art VLA and world-modeling baselines, with inference-time scaling providing an additional 2-5% improvement. In real-world tasks using the Franka Research 3, DUST outperforms baselines by 10% in success rate. Finally, we demonstrate that DUST enables effective transfer learning through both pretraining on action-free videos and joint-training with heterogeneous robot and human datasets.

## 개요
비전-언어-행동 모델(VLA)에 월드 모델을 통합하는 것은 로봇 정책 학습에 유망하지만, 모달리티 차이로 인해 상태와 행동을 공동으로 예측하는 데 어려움이 있습니다. 이를 해결하기 위해, 우리는 DUal-STream diffusion (DUST)을 제안합니다. 이는 개별 모달리티 스트림을 유지하면서 교차 모달 지식 공유를 가능하게 하는 다중 모달 확산 트랜스포머를 특징으로 하는 월드 모델 기반 VLA 프레임워크입니다. 또한, DUST는 독립적인 노이즈 섭동과 분리된 흐름 매칭 손실을 활용하여 교차 모달 인과 관계를 학습합니다. 나아가, 행동 및 비전 토큰에 대한 비동기 샘플링 방법을 도입하여 추론 시간 스케일링을 통해 성능을 향상시킵니다. RoboCasa 및 GR-1과 같은 시뮬레이션 벤치마크에서의 실험 결과, DUST는 최신 VLA 및 월드 모델링 기준선 대비 최대 6%의 성능 향상을 달성했으며, 추론 시간 스케일링은 추가로 2-5%의 개선을 제공합니다. Franka Research 3를 사용한 실제 작업에서 DUST는 기준선 대비 성공률에서 10% 더 우수한 성능을 보였습니다. 마지막으로, DUST가 행동 없는 비디오에 대한 사전 학습과 이종 로봇 및 인간 데이터셋을 사용한 공동 학습을 통해 효과적인 전이 학습을 가능하게 함을 입증합니다.

## 핵심 내용
비전-언어-행동 모델(VLA)에 월드 모델을 통합하는 것은 로봇 정책 학습에 유망하지만, 모달리티 차이로 인해 상태와 행동을 공동으로 예측하는 데 어려움이 있습니다. 이를 해결하기 위해, 우리는 DUal-STream diffusion (DUST)을 제안합니다. 이는 개별 모달리티 스트림을 유지하면서 교차 모달 지식 공유를 가능하게 하는 다중 모달 확산 트랜스포머를 특징으로 하는 월드 모델 기반 VLA 프레임워크입니다. 또한, DUST는 독립적인 노이즈 섭동과 분리된 흐름 매칭 손실을 활용하여 교차 모달 인과 관계를 학습합니다. 나아가, 행동 및 비전 토큰에 대한 비동기 샘플링 방법을 도입하여 추론 시간 스케일링을 통해 성능을 향상시킵니다. RoboCasa 및 GR-1과 같은 시뮬레이션 벤치마크에서의 실험 결과, DUST는 최신 VLA 및 월드 모델링 기준선 대비 최대 6%의 성능 향상을 달성했으며, 추론 시간 스케일링은 추가로 2-5%의 개선을 제공합니다. Franka Research 3를 사용한 실제 작업에서 DUST는 기준선 대비 성공률에서 10% 더 우수한 성능을 보였습니다. 마지막으로, DUST가 행동 없는 비디오에 대한 사전 학습과 이종 로봇 및 인간 데이터셋을 사용한 공동 학습을 통해 효과적인 전이 학습을 가능하게 함을 입증합니다.

## 参考
- http://arxiv.org/abs/2510.27607v3
