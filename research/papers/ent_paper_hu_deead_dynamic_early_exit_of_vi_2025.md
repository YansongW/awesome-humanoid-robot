---
$id: ent_paper_hu_deead_dynamic_early_exit_of_vi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving'
  zh: DeeAD
  ko: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving'
summary:
  en: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving (DeeAD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by City University of Hongkong, Mohamed bin Zayed University of Artificial
    Intelligence.'
  zh: DeeAD 是香港城市大学和穆罕默德·本·扎耶德人工智能大学于 2025 年提出的免训练、动作引导的早期退出框架，旨在加速视觉-语言-动作模型在自动驾驶中的推理。其核心创新在于通过评估中间轨迹的物理可行性来动态终止推理，而非依赖置信度分数，在
    Bench2Drive 基准上实现了高达 28% 的 Transformer 层稀疏性和 29% 的延迟降低，同时保持规划质量与安全性。
  ko: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving (DeeAD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by City University of Hongkong, Mohamed bin Zayed University of Artificial
    Intelligence.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- deead
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.20720v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (783 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2511.20720
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DeeAD source
  url: https://doi.org/10.48550/arXiv.2511.20720
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
DeeAD 针对 VLA 模型因深层 Transformer 堆叠导致的推理延迟问题，提出了一种无需重新训练的早期退出机制。该框架通过将预测轨迹与轻量级规划先验（如导航或低精度规划）进行对齐，并在可容忍偏差（<2 米）内终止推理，从而避免不必要的计算。此外，DeeAD 引入了一个多跳控制器，根据分数变化率自适应地跳过冗余层，进一步提升效率。实验表明，该方法可无缝集成到 ORION 等现有 VLA 模型中，在 Bench2Drive 基准上显著减少计算开销，同时不牺牲规划性能。

## 核心内容
### 方法概述
DeeAD 的核心是一个训练免费的早期退出框架，其关键组件包括：
- **动作引导的早期退出**：在推理过程中，模型会生成中间轨迹，DeeAD 通过评估这些轨迹与轻量级规划先验（如 Navigation 或 Low-precision Planning）的物理可行性来决定是否提前终止。当预测轨迹与先验的偏差小于 2 米时，推理即停止。
- **多跳控制器**：该控制器根据分数变化率动态跳过冗余的 Transformer 层，从而在保持性能的同时减少计算量。

### 实验设置与结果
- **基准测试**：在 Bench2Drive 基准上进行评估，该基准专注于自动驾驶规划任务。
- **性能提升**：DeeAD 实现了高达 28% 的 Transformer 层稀疏性（即跳过层数比例）和 29% 的推理延迟降低。
- **质量保障**：尽管计算开销大幅减少，但规划质量和安全性指标与原始 VLA 模型（如 ORION）相比未出现显著下降。

### 结论
DeeAD 提供了一种高效、无需重新训练的解决方案，可显著加速 VLA 模型在自动驾驶中的推理过程，同时保持规划性能。其动态早期退出机制为实时自动驾驶系统提供了实用价值。

## Overview
Vision-Language Action (VLA) models unify perception, reasoning, and trajectory generation for autonomous driving, but suffer from significant inference latency due to deep transformer stacks. We present DeeAD, a training-free, action-guided early-exit framework that accelerates VLA planning by evaluating the physical feasibility of intermediate trajectories. Instead of relying on confidence scores, DeeAD terminates inference when predicted trajectories align with lightweight planning priors (e.g., Navigation or Low-precision Planning) within a tolerable deviation (<2m). To improve efficiency, we introduce a multi-hop controller that adaptively skips redundant layers based on the change rate of scores. DeeAD integrates into existing VLA models, such as ORION, without requiring retraining. Experiments on the Bench2Drive benchmark demonstrate up to 28% transformer-layer sparsity and 29% latency reduction, while preserving planning quality and safety.

## 参考
- http://arxiv.org/abs/2511.20720v1

## 개요
DeeAD는 VLA 모델의 깊은 Transformer 적층으로 인한 추론 지연 문제를 해결하기 위해, 재훈련이 필요 없는 조기 종료 메커니즘을 제안한다. 이 프레임워크는 예측 궤적을 경량 계획 사전(예: 내비게이션 또는 저정밀 계획)과 정렬하고, 허용 가능한 편차(<2m) 내에서 추론을 종료하여 불필요한 계산을 방지한다. 또한, DeeAD는 점수 변화율에 따라 중복 레이어를 적응형으로 건너뛰는 멀티홉 컨트롤러를 도입하여 효율성을 더욱 향상시킨다. 실험에 따르면, 이 방법은 ORION과 같은 기존 VLA 모델에 원활하게 통합될 수 있으며, Bench2Drive 벤치마크에서 계획 성능을 희생하지 않으면서 계산 오버헤드를 크게 줄인다.

## 핵심 내용
### 방법 개요
DeeAD의 핵심은 훈련이 필요 없는 조기 종료 프레임워크이며, 주요 구성 요소는 다음과 같다:
- **동작 기반 조기 종료**: 추론 과정에서 모델은 중간 궤적을 생성하며, DeeAD는 이러한 궤적과 경량 계획 사전(예: 내비게이션 또는 저정밀 계획)의 물리적 타당성을 평가하여 조기 종료 여부를 결정한다. 예측 궤적과 사전의 편차가 2m 미만이면 추론이 중단된다.
- **멀티홉 컨트롤러**: 이 컨트롤러는 점수 변화율에 따라 중복 Transformer 레이어를 동적으로 건너뛰어 성능을 유지하면서 계산량을 줄인다.

### 실험 설정 및 결과
- **벤치마크 테스트**: 자율주행 계획 작업에 초점을 맞춘 Bench2Drive 벤치마크에서 평가가 수행되었다.
- **성능 향상**: DeeAD는 최대 28%의 Transformer 레이어 희소성(즉, 건너뛴 레이어 비율)과 29%의 추론 지연 감소를 달성했다.
- **품질 보장**: 계산 오버헤드가 크게 줄었음에도 불구하고, 계획 품질과 안전 지표는 원래 VLA 모델(예: ORION)과 비교하여 유의미한 저하가 나타나지 않았다.

### 결론
DeeAD는 자율주행에서 VLA 모델의 추론을 크게 가속화하면서 계획 성능을 유지하는 효율적이고 재훈련이 필요 없는 솔루션을 제공한다. 동적 조기 종료 메커니즘은 실시간 자율주행 시스템에 실용적 가치를 제공한다.
