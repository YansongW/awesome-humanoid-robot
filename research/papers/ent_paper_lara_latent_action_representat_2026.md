---
$id: ent_paper_lara_latent_action_representat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LARA: Latent Action Representation Alignment for Vision-Language-Action Models'
  zh: 'LARA: Latent Action Representation Alignment for Vision-Language-Action Models'
  ko: 'LARA: Latent Action Representation Alignment for Vision-Language-Action Models'
summary:
  en: 'arXiv:2606.07100v2 Announce Type: replace-cross Abstract: Visual-language action (VLA) models enable robots to predict
    actions directly from observations and language instructions, but their performance depends on large-scale, high-quality
    data and is limited by the scarcity of real-world robot action datasets. To facilitate VLA model learning with abundant
    unlabeled human videos, Latent Action Models (LAM) learn latent action representations from visual dynamics to provide
    additional supervision for VLA learning. However, LAM and VLA are typically trained separately, leaving LAM ungrounded
    during VLA training and VLA models constrained by frozen LAM representations. To address these issues, we propose Latent
    Action Representation Alignment (LARA), a plug-and-play framework that jointly optimizes LAM and VLA via representation
    alignment. This enables reciprocal benefits where LAMs learn with action trajectories to avoid spurious visual changes,
    while VLAs are regularized by forward dynamics learned within LAMs to reduce hallucinations of functionally ineffective
    trajectories. We demonstrate LARA versatility and effectiveness for pre-training, post-training enhancement of pre-trained
    VLA models, and LAM refinement, achieving an average of ~10%, ~5%, and ~15% improvement over 3 simulation and 1 meticulously
    designed real-world robotic manipulation benchmarks.'
  zh: LARA 是一种即插即用的框架，由研究团队提出，用于联合优化 Latent Action Models (LAM) 与 Vision-Language-Action (VLA) 模型。其核心贡献是通过表征对齐，使 LAM 利用动作轨迹避免虚假视觉变化，同时
    VLA 借助 LAM 的前向动力学正则化减少无效轨迹的幻觉，在仿真和真实机器人操作基准上平均提升约 10%、5% 和 15%。
  ko: 'arXiv:2606.07100v2 Announce Type: replace-cross Abstract: Visual-language action (VLA) models enable robots to predict
    actions directly from observations and language instructions, but their performance depends on large-scale, high-quality
    data and is limited by the scarcity of real-world robot action datasets. To facilitate VLA model learning with abundant
    unlabeled human videos, Latent Action Models (LAM) learn latent action representations from visual dynamics to provide
    additional supervision for VLA learning. However, LAM and VLA are typically trained separately, leaving LAM ungrounded
    during VLA training and VLA models constrained by frozen LAM representations. To address these issues, we propose Latent
    Action Representation Alignment (LARA), a plug-and-play framework that jointly optimizes LAM and VLA via representation
    alignment. This enables reciprocal benefits where LAMs learn with action trajectories to avoid spurious visual changes,
    while VLAs are regularized by forward dynamics learned within LAMs to reduce hallucinations of functionally ineffective
    trajectories. We demonstrate LARA versatility and effectiveness for pre-training, post-training enhancement of pre-trained
    VLA models, and LAM refinement, achieving an average of ~10%, ~5%, and ~15% improvement over 3 simulation and 1 meticulously
    designed real-world robotic manipulation benchmarks.'
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
- lara
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.07100v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'LARA: Latent Action Representation Alignment for Vision-Language-Action Models'
  url: https://arxiv.org/abs/2606.07100
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
VLA 模型依赖大规模高质量数据，但真实机器人动作数据集稀缺。LAM 通过从视觉动态中学习潜在动作表征来提供额外监督，但两者通常分开训练，导致 LAM 在 VLA 训练中缺乏接地，VLA 受限于冻结的 LAM 表征。LARA 通过表征对齐实现联合优化，使 LAM 从动作轨迹中学习以避免虚假视觉变化，同时 VLA 被 LAM 的前向动力学正则化以减少无效轨迹的幻觉。该方法适用于预训练、后训练增强以及 LAM 精炼，在三个仿真和一个真实世界机器人操作基准上分别取得约 10%、5% 和 15% 的平均提升。

## 核心内容
### 方法概述
LARA 是一个即插即用框架，通过表征对齐联合优化 LAM 和 VLA。其核心机制包括：
- **双向正则化**：LAM 在训练中利用动作轨迹，避免仅从视觉动态中学习时产生的虚假变化；VLA 则被 LAM 学习的前向动力学正则化，减少对功能无效轨迹的幻觉。
- **联合优化**：LAM 和 VLA 在训练过程中相互更新，而非独立训练或冻结一方表征。

### 实验设置
- **基准测试**：在 3 个仿真环境（具体名称未在正文中列出）和 1 个精心设计的真实世界机器人操作基准上进行评估。
- **应用场景**：验证了 LARA 在三种场景下的有效性：
  - **预训练**：从头开始联合训练 LAM 和 VLA。
  - **后训练增强**：对预训练的 VLA 模型进行微调增强。
  - **LAM 精炼**：优化已有的 LAM 表征。

### 关键结果
- **性能提升**：在仿真和真实基准上，LARA 平均提升约：
  - 预训练场景：~10%
  - 后训练增强场景：~5%
  - LAM 精炼场景：~15%
- **结论**：LARA 通过表征对齐解决了 LAM 与 VLA 分离训练的问题，实现了双向收益，显著提升了机器人操作任务的性能。

## Overview
Visual-language action (VLA) models enable robots to predict actions directly from observations and language instructions, but their performance depends on large-scale, high-quality data and is limited by the scarcity of real-world robot action datasets. To facilitate VLA model learning with abundant unlabeled human videos, Latent Action Models (LAM) learn latent action representations from visual dynamics to provide additional supervision for VLA learning. However, LAM and VLA are typically trained separately, leaving LAM ungrounded during VLA training and VLA models constrained by frozen LAM representations. To address these issues, we propose Latent Action Representation Alignment (LARA), a plug-and-play framework that jointly optimizes LAM and VLA via representation alignment. This enables reciprocal benefits where LAMs learn with action trajectories to avoid spurious visual changes, while VLAs are regularized by forward dynamics learned within LAMs to reduce hallucinations of functionally ineffective trajectories. We demonstrate LARA versatility and effectiveness for pre-training, post-training enhancement of pre-trained VLA models, and LAM refinement, achieving an average of ~10%, ~5%, and ~15% improvement over 3 simulation and 1 meticulously designed real-world robotic manipulation benchmarks.

## 개요
Visual-language action (VLA) 모델은 로봇이 관찰 및 언어 명령으로부터 직접 행동을 예측할 수 있게 하지만, 그 성능은 대규모 고품질 데이터에 의존하며 실제 로봇 행동 데이터셋의 부족으로 제한됩니다. 풍부한 레이블이 없는 인간 비디오를 활용한 VLA 모델 학습을 촉진하기 위해, Latent Action Models (LAM)은 시각적 역학으로부터 잠재 행동 표현을 학습하여 VLA 학습에 추가적인 지도 신호를 제공합니다. 그러나 LAM과 VLA는 일반적으로 별도로 훈련되어, VLA 훈련 중 LAM이 근거를 잃고 VLA 모델이 고정된 LAM 표현에 의해 제약을 받습니다. 이러한 문제를 해결하기 위해, 우리는 표현 정렬을 통해 LAM과 VLA를 공동으로 최적화하는 플러그 앤 플레이 프레임워크인 Latent Action Representation Alignment (LARA)를 제안합니다. 이를 통해 LAM이 행동 궤적을 학습하여 허위 시각적 변화를 피하고, VLA가 LAM 내에서 학습된 순방향 역학에 의해 정규화되어 기능적으로 비효율적인 궤적의 환각을 줄이는 상호 이점이 가능해집니다. 우리는 LARA의 사전 훈련, 사전 훈련된 VLA 모델의 사후 훈련 강화, LAM 개선에 대한 다재다능함과 효과를 입증하며, 3개의 시뮬레이션 및 1개의 정교하게 설계된 실제 로봇 조작 벤치마크에서 평균 약 10%, 5%, 15%의 성능 향상을 달성했습니다.

## 핵심 내용
Visual-language action (VLA) 모델은 로봇이 관찰 및 언어 명령으로부터 직접 행동을 예측할 수 있게 하지만, 그 성능은 대규모 고품질 데이터에 의존하며 실제 로봇 행동 데이터셋의 부족으로 제한됩니다. 풍부한 레이블이 없는 인간 비디오를 활용한 VLA 모델 학습을 촉진하기 위해, Latent Action Models (LAM)은 시각적 역학으로부터 잠재 행동 표현을 학습하여 VLA 학습에 추가적인 지도 신호를 제공합니다. 그러나 LAM과 VLA는 일반적으로 별도로 훈련되어, VLA 훈련 중 LAM이 근거를 잃고 VLA 모델이 고정된 LAM 표현에 의해 제약을 받습니다. 이러한 문제를 해결하기 위해, 우리는 표현 정렬을 통해 LAM과 VLA를 공동으로 최적화하는 플러그 앤 플레이 프레임워크인 Latent Action Representation Alignment (LARA)를 제안합니다. 이를 통해 LAM이 행동 궤적을 학습하여 허위 시각적 변화를 피하고, VLA가 LAM 내에서 학습된 순방향 역학에 의해 정규화되어 기능적으로 비효율적인 궤적의 환각을 줄이는 상호 이점이 가능해집니다. 우리는 LARA의 사전 훈련, 사전 훈련된 VLA 모델의 사후 훈련 강화, LAM 개선에 대한 다재다능함과 효과를 입증하며, 3개의 시뮬레이션 및 1개의 정교하게 설계된 실제 로봇 조작 벤치마크에서 평균 약 10%, 5%, 15%의 성능 향상을 달성했습니다.

## 参考
- http://arxiv.org/abs/2606.07100v2
