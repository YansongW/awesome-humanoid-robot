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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.27607v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (870 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2510.27607v3

## 개요
DUST 프레임워크는 이중 스트림 확산 Transformer 설계를 통해 시각, 언어 및 행동의 독립적인 모달리티 스트림을 각각 유지하면서도 모달리티 간 지식 공유를 가능하게 합니다. 이는 독립적인 노이즈 섭동과 분리된 흐름 일치 손실을 사용하여 모달리티 간의 인과 관계를 학습하고, 비동기 샘플링 방법을 도입하여 추론 시 행동 및 시각 토큰을 확장합니다. RoboCasa 및 GR-1과 같은 시뮬레이션 벤치마크에서 DUST는 최첨단 VLA 및 세계 모델 기준 방법 대비 최대 6%의 성능 향상을 달성했으며, 추론 시 확장은 추가로 2-5%의 개선을 제공합니다. Franka Research 3 실제 로봇 작업에서 DUST의 성공률은 기준 방법보다 10% 높습니다.

## 핵심 내용
### 방법 아키텍처
- **이중 스트림 확산 Transformer**: DUST의 핵심은 시각, 언어 및 행동의 독립적인 모달리티 스트림을 유지하면서 교차 주의 메커니즘을 통해 모달리티 간 지식 공유를 실현하여 모달리티 차이로 인한 공동 예측 어려움을 방지합니다.
- **독립 노이즈 섭동 및 분리된 흐름 일치 손실**: 각 모달리티 스트림에 독립적인 노이즈 섭동을 적용하고, 분리된 흐름 일치 손실을 사용하여 모달리티 간 인과 관계를 학습함으로써 상태와 행동의 결합 분포를 더 효과적으로 모델링합니다.
- **비동기 샘플링 방법**: 추론 시 행동 토큰과 시각 토큰에 비동기 샘플링 전략을 적용하여 샘플링 단계 수나 순서를 조정함으로써 생성 품질을 향상시키고 추론 시 계산 확장을 구현합니다.

### 실험 설정 및 주요 결과
- **시뮬레이션 벤치마크**: RoboCasa 및 GR-1과 같은 시뮬레이션 환경에서 DUST는 최첨단 VLA 및 세계 모델 기준 방법(예: RT-2, UniPi) 대비 최대 6%의 성능 향상을 달성했습니다. 추론 시 확장은 추가로 2-5%의 개선을 제공합니다.
- **실제 세계 작업**: Franka Research 3 로봇 팔을 사용한 실제 조작 작업에서 DUST의 성공률은 기준 방법보다 10% 높아 실제 시나리오에서의 효과를 검증했습니다.
- **전이 학습 능력**: DUST는 행동 없는 비디오를 통한 사전 학습과 이종 로봇 데이터 세트 및 인간 데이터 세트를 사용한 공동 학습을 지원하여 강력한 전이 학습 능력을 보여줍니다.

### 결론
DUST는 이중 스트림 확산 프레임워크를 통해 VLA 모델과 세계 모델의 공동 예측에서 발생하는 모달리티 차이 문제를 효과적으로 해결했으며, 시뮬레이션 및 실제 작업 모두에서 상당한 성능 향상을 달성하고 우수한 전이 학습 능력을 갖추고 있습니다.
