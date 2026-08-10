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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.07100v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (810 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2606.07100v2

## 개요
VLA 모델은 대규모 고품질 데이터에 의존하지만, 실제 로봇 행동 데이터셋은 부족하다. LAM은 시각적 역학에서 잠재 행동 표현을 학습하여 추가적인 감독을 제공하지만, 둘은 일반적으로 분리되어 훈련되어 LAM이 VLA 훈련에서 접지(grounding)가 부족하고, VLA는 고정된 LAM 표현에 제한된다. LARA는 표현 정렬을 통해 공동 최적화를 구현하여, LAM이 행동 궤적으로부터 학습하여 허위 시각적 변화를 피하게 하고, 동시에 VLA는 LAM의 전방 역학에 의해 정규화되어 무효 궤적의 환각을 줄인다. 이 방법은 사전 훈련, 사후 훈련 강화 및 LAM 정제에 적용 가능하며, 세 가지 시뮬레이션과 하나의 실제 로봇 조작 벤치마크에서 각각 평균 약 10%, 5%, 15%의 향상을 달성한다.

## 핵심 내용
### 방법 개요
LARA는 표현 정렬을 통해 LAM과 VLA를 공동 최적화하는 플러그 앤 플레이 프레임워크이다. 핵심 메커니즘은 다음과 같다:
- **양방향 정규화**: LAM은 훈련 중 행동 궤적을 활용하여 시각적 역학만으로 학습할 때 발생하는 허위 변화를 피한다. VLA는 LAM이 학습한 전방 역학에 의해 정규화되어 기능적으로 무효한 궤적의 환각을 줄인다.
- **공동 최적화**: LAM과 VLA는 훈련 과정에서 서로 업데이트되며, 독립적으로 훈련되거나 한쪽 표현이 고정되지 않는다.

### 실험 설정
- **벤치마크**: 3개의 시뮬레이션 환경(구체적인 이름은 본문에 나열되지 않음)과 1개의 정교하게 설계된 실제 로봇 조작 벤치마크에서 평가된다.
- **적용 시나리오**: LARA의 세 가지 시나리오에서의 효과를 검증한다:
  - **사전 훈련**: 처음부터 LAM과 VLA를 공동 훈련한다.
  - **사후 훈련 강화**: 사전 훈련된 VLA 모델을 미세 조정하여 강화한다.
  - **LAM 정제**: 기존 LAM 표현을 최적화한다.

### 주요 결과
- **성능 향상**: 시뮬레이션 및 실제 벤치마크에서 LARA는 평균 약:
  - 사전 훈련 시나리오: ~10%
  - 사후 훈련 강화 시나리오: ~5%
  - LAM 정제 시나리오: ~15%
- **결론**: LARA는 표현 정렬을 통해 LAM과 VLA의 분리 훈련 문제를 해결하여 양방향 이점을 구현하고, 로봇 조작 작업의 성능을 크게 향상시킨다.
