---
$id: ent_paper_mask2real_wm_segmentation_mask_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models'
  zh: 'Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models'
  ko: 'Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models'
summary:
  en: 'arXiv:2607.04546v1 Announce Type: new Abstract: Action-conditioned world models allow robots to predict the future
    consequences of candidate actions without additional physical interaction, supporting policy evaluation, planning, and
    data augmentation. We present Mask2Real-WM, a two-stage action-conditioned world model for dexterous manipulation that
    decouples pixel prediction into a dynamics model and a rendering model. The dynamics model predicts future segmentation
    masks from past masks and 23-DoF action sequences. The rendering model maps the predicted masks to photorealistic RGB
    using a ControlNet-augmented Stable Video Diffusion backbone. The smaller sim-to-real gap in segmentation space enables
    the dynamics model to benefit from large-scale pretraining on over 50 h of synthetic simulation data, followed by fine-tuning
    on fewer than 2.5 h of real demonstrations. Experiments on a dexterous pick-and-place benchmark show that mask conditioning
    and simulation pretraining are both required for per-DoF action controllability across all 23 degrees of freedom. In contrast,
    monolithic baselines capture broad hand and end-effector trajectories but do not reliably reflect fine-grained, per-joint
    action effects.'
  zh: Mask2Real-WM 是一个两阶段动作条件世界模型，专为灵巧操作设计，由研究团队提出。其核心贡献在于将像素预测解耦为动力学模型和渲染模型，利用分割掩码作为仿真到现实的桥梁，并通过超过50小时仿真数据预训练和少于2.5小时真实数据微调，实现了对23个自由度的精细动作控制。
  ko: 'arXiv:2607.04546v1 Announce Type: new Abstract: Action-conditioned world models allow robots to predict the future
    consequences of candidate actions without additional physical interaction, supporting policy evaluation, planning, and
    data augmentation. We present Mask2Real-WM, a two-stage action-conditioned world model for dexterous manipulation that
    decouples pixel prediction into a dynamics model and a rendering model. The dynamics model predicts future segmentation
    masks from past masks and 23-DoF action sequences. The rendering model maps the predicted masks to photorealistic RGB
    using a ControlNet-augmented Stable Video Diffusion backbone. The smaller sim-to-real gap in segmentation space enables
    the dynamics model to benefit from large-scale pretraining on over 50 h of synthetic simulation data, followed by fine-tuning
    on fewer than 2.5 h of real demonstrations. Experiments on a dexterous pick-and-place benchmark show that mask conditioning
    and simulation pretraining are both required for per-DoF action controllability across all 23 degrees of freedom. In contrast,
    monolithic baselines capture broad hand and end-effector trajectories but do not reliably reflect fine-grained, per-joint
    action effects.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- mask2real_wm
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04546v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (879 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models (arXiv)'
  url: https://arxiv.org/abs/2607.04546
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Mask2Real-WM 通过将像素预测分解为两个独立模块来解决灵巧操作中的世界模型构建难题。动力学模型基于历史分割掩码和23自由度动作序列预测未来掩码，而渲染模型则利用 ControlNet 增强的 Stable Video Diffusion 骨干网络将预测掩码转换为逼真的 RGB 图像。由于分割空间的仿真到现实差距较小，动力学模型可以在大量仿真数据上预训练，再通过少量真实演示数据微调。在灵巧抓取与放置基准测试中，该方法在所有23个自由度上均实现了每自由度动作可控性，而传统整体模型只能捕捉粗略的手部和末端执行器轨迹。

## 核心内容
### 方法架构
Mask2Real-WM 采用两阶段解耦设计：
- **动力学模型**：输入历史分割掩码和23自由度动作序列，输出未来分割掩码。该模型在分割空间操作，利用其较小的仿真到现实差距，先在超过50小时的合成仿真数据上大规模预训练，再在少于2.5小时的真实演示数据上微调。
- **渲染模型**：以 ControlNet 增强的 Stable Video Diffusion 为骨干网络，将动力学模型预测的分割掩码映射为逼真的 RGB 图像，实现从抽象掩码到视觉外观的转换。

### 实验设置与关键结果
- **基准测试**：在灵巧抓取与放置任务上评估，涉及23个自由度的精细控制。
- **关键发现**：
  - 掩码条件（mask conditioning）和仿真预训练（simulation pretraining）两者缺一不可，共同实现了对所有23个自由度的每自由度动作可控性。
  - 相比之下，整体式基线模型（monolithic baselines）只能捕捉粗略的手部和末端执行器轨迹，无法可靠反映细粒度的每关节动作效果。
- **数据效率**：仅需2.5小时真实演示数据即可完成微调，大幅降低了对真实数据量的依赖。

### 结论
Mask2Real-WM 通过分割掩码作为仿真到现实的桥梁，有效解决了灵巧操作中世界模型的动作可控性问题，为高自由度精细操作提供了可行方案。

## Overview
Action-conditioned world models allow robots to predict the future consequences of candidate actions without additional physical interaction, supporting policy evaluation, planning, and data augmentation. We present Mask2Real-WM, a two-stage action-conditioned world model for dexterous manipulation that decouples pixel prediction into a dynamics model and a rendering model. The dynamics model predicts future segmentation masks from past masks and 23-DoF action sequences. The rendering model maps the predicted masks to photorealistic RGB using a ControlNet-augmented Stable Video Diffusion backbone. The smaller sim-to-real gap in segmentation space enables the dynamics model to benefit from large-scale pretraining on over 50 h of synthetic simulation data, followed by fine-tuning on fewer than 2.5 h of real demonstrations. Experiments on a dexterous pick-and-place benchmark show that mask conditioning and simulation pretraining are both required for per-DoF action controllability across all 23 degrees of freedom. In contrast, monolithic baselines capture broad hand and end-effector trajectories but do not reliably reflect fine-grained, per-joint action effects.

## 参考
- http://arxiv.org/abs/2607.04546v1

## 개요
Mask2Real-WM은 픽셀 예측을 두 개의 독립적인 모듈로 분해하여 정교한 조작(dexterous manipulation)에서의 세계 모델 구축 문제를 해결합니다. 동역학 모델은 과거 분할 마스크와 23자유도 행동 시퀀스를 기반으로 미래 마스크를 예측하며, 렌더링 모델은 ControlNet으로 강화된 Stable Video Diffusion 백본을 활용하여 예측된 마스크를 사실적인 RGB 이미지로 변환합니다. 분할 공간의 시뮬레이션-실제 격차가 작기 때문에, 동역학 모델은 대량의 시뮬레이션 데이터로 사전 학습한 후 소량의 실제 시연 데이터로 미세 조정할 수 있습니다. 정교한 파지 및 배치 벤치마크에서 이 방법은 모든 23개 자유도에 대해 자유도별 행동 제어 가능성을 달성한 반면, 기존의 통합 모델은 대략적인 손과 말단 실행기 궤적만 포착할 수 있었습니다.

## 핵심 내용
### 방법 아키텍처
Mask2Real-WM은 2단계 분리 설계를 채택합니다:
- **동역학 모델**: 과거 분할 마스크와 23자유도 행동 시퀀스를 입력으로 받아 미래 분할 마스크를 출력합니다. 이 모델은 분할 공간에서 작동하며, 시뮬레이션-실제 격차가 작은 특성을 활용하여 먼저 50시간 이상의 합성 시뮬레이션 데이터로 대규모 사전 학습을 수행한 후, 2.5시간 미만의 실제 시연 데이터로 미세 조정합니다.
- **렌더링 모델**: ControlNet으로 강화된 Stable Video Diffusion을 백본으로 사용하여 동역학 모델이 예측한 분할 마스크를 사실적인 RGB 이미지로 매핑하며, 추상적인 마스크에서 시각적 외관으로의 변환을 구현합니다.

### 실험 설정 및 주요 결과
- **벤치마크**: 정교한 파지 및 배치 작업에서 평가되었으며, 23개 자유도의 정밀 제어를 포함합니다.
- **주요 발견**:
  - 마스크 조건화(mask conditioning)와 시뮬레이션 사전 학습(simulation pretraining)은 둘 다 필수적이며, 함께 작용하여 모든 23개 자유도에 대한 자유도별 행동 제어 가능성을 달성합니다.
  - 대조적으로, 통합형 기준 모델(monolithic baselines)은 대략적인 손과 말단 실행기 궤적만 포착할 수 있으며, 세분화된 관절별 행동 효과를 신뢰할 수 있게 반영하지 못합니다.
- **데이터 효율성**: 미세 조정에 단 2.5시간의 실제 시연 데이터만 필요하여 실제 데이터 양에 대한 의존도를 크게 줄입니다.

### 결론
Mask2Real-WM은 분할 마스크를 시뮬레이션-실제 브리지로 사용하여 정교한 조작에서 세계 모델의 행동 제어 가능성 문제를 효과적으로 해결하며, 고자유도 정밀 조작을 위한 실현 가능한 솔루션을 제공합니다.
