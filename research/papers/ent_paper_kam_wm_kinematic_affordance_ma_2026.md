---
$id: ent_paper_kam_wm_kinematic_affordance_ma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation'
  zh: 'KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation'
  ko: 'KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation'
summary:
  en: 'arXiv:2607.04652v1 Announce Type: new Abstract: Learning manipulation from few demonstrations requires visual priors
    that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation
    masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a
    frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video
    backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned
    interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion
    policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average
    success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively.
    Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information
    beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide
    a useful first-order visual prior for control without the test-time cost of future rollout.'
  zh: KAM-WM 是一个用于机器人操作的框架，由研究团队提出，能从冻结的潜在视频世界模型中提取粗粒度的方向性交互线索。其核心贡献在于通过 Flow Matching 图像到视频骨干网络的一次查询，将单步潜在速度解释为运动学可操作度图（KAM），为扩散策略提供任务条件化的交互区域和粗略运动结构。在
    LIBERO 和 RoboTwin2.0 基准上，KAM-WM 分别达到 90.6% 和 65.7%/22.4% 的成功率，验证了冻结视频模型作为控制先验的有效性。
  ko: 'arXiv:2607.04652v1 Announce Type: new Abstract: Learning manipulation from few demonstrations requires visual priors
    that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation
    masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a
    frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video
    backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned
    interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion
    policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average
    success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively.
    Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information
    beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide
    a useful first-order visual prior for control without the test-time cost of future rollout.'
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
- kam_wm
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04652v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1115 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.04652
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
KAM-WM 框架旨在解决少样本机器人操作学习中的视觉先验问题，不仅关注交互位置，还关注交互的起始方式。它利用一个冻结的潜在视频世界模型，通过 Flow Matching 图像到视频骨干网络的一次查询，将单步潜在速度解释为运动学可操作度图（KAM），从而提供任务条件化的交互区域和粗略运动结构。一个轻量级的 Perceiver 将 KAM 压缩为令牌，与 RGB 观测和本体感觉一起条件化扩散策略。在 LIBERO 和 RoboTwin2.0 基准上的实验表明，KAM-WM 取得了显著性能，其中在 LIBERO 上平均成功率达到 90.6%，在 RoboTwin2.0 的 Easy 和 Hard 设置中分别达到 65.7% 和 22.4% 的成功率。与零阶掩码先验的对比实验表明，部分性能提升来源于方向信息，而不仅仅是空间定位。

## 核心内容
### 方法概述
KAM-WM 的核心思想是从一个冻结的潜在视频世界模型中提取粗粒度的方向性交互线索，无需进行 rollout 或世界模型微调。具体而言，它通过一次查询 Flow Matching 图像到视频骨干网络，将单步潜在速度解释为运动学可操作度图（KAM）。KAM 提供了任务条件化的交互区域和粗略运动结构，弥补了静态先验（如分割掩码）仅编码交互位置而忽略交互起始方式的不足。

### 架构细节
- **潜在视频世界模型**：使用一个冻结的模型，不进行 rollout 或微调，仅通过单步潜在速度提供方向性线索。
- **Flow Matching 骨干网络**：图像到视频的骨干网络，一次查询即可生成 KAM。
- **Perceiver 压缩器**：轻量级模块，将 KAM 压缩为令牌，与 RGB 观测和本体感觉一起输入扩散策略。
- **扩散策略**：以 KAM 令牌、RGB 观测和本体感觉为条件，生成操作动作。

### 实验设置与结果
- **基准测试**：在 LIBERO 和 RoboTwin2.0 上进行评估。
- **LIBERO 结果**：平均成功率达到 90.6%。
- **RoboTwin2.0 结果**：在 Easy 设置中成功率为 65.7%，在 Hard 设置中成功率为 22.4%。
- **对比实验**：与零阶掩码先验（仅提供空间定位）进行对比，结果表明 KAM-WM 的性能提升部分来源于方向信息，而不仅仅是空间定位。

### 结论
在评估的设置中，冻结的视频模型能够提供有用的第一阶视觉先验用于控制，且无需测试时的未来 rollout 成本。KAM-WM 通过提取方向性交互线索，显著提升了少样本操作学习的性能。

## Overview
Learning manipulation from few demonstrations requires visual priors that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively. Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide a useful first-order visual prior for control without the test-time cost of future rollout.

## 参考
- http://arxiv.org/abs/2607.04652v1

## 개요
KAM-WM 프레임워크는 소표본 로봇 조작 학습에서의 시각적 사전 정보 문제를 해결하는 것을 목표로 하며, 상호작용 위치뿐만 아니라 상호작용의 시작 방식에도 주목합니다. 이는 고정된 잠재 비디오 세계 모델을 활용하여 Flow Matching 이미지-비디오 백본 네트워크의 단일 쿼리를 통해 단일 단계 잠재 속도를 운동학적 조작 가능성 맵(KAM)으로 해석함으로써, 작업 조건화된 상호작용 영역과 대략적인 운동 구조를 제공합니다. 경량 Perceiver는 KAM을 토큰으로 압축하고, RGB 관측 및 고유 감각과 함께 확산 정책을 조건화합니다. LIBERO 및 RoboTwin2.0 벤치마크에서의 실험은 KAM-WM이显著한 성능을 달성했음을 보여주며, LIBERO에서 평균 성공률 90.6%, RoboTwin2.0의 Easy 및 Hard 설정에서 각각 65.7% 및 22.4%의 성공률을 기록했습니다. 0차 마스크 사전 정보와의 대조 실험은 성능 향상의 일부가 공간적 위치 파악뿐만 아니라 방향 정보에서 비롯됨을 시사합니다.

## 핵심 내용
### 방법 개요
KAM-WM의 핵심 아이디어는 고정된 잠재 비디오 세계 모델에서 rollout이나 세계 모델 미세 조정 없이 조립도(coarse-grained)의 방향성 상호작용 단서를 추출하는 것입니다. 구체적으로, Flow Matching 이미지-비디오 백본 네트워크를 한 번 쿼리하여 단일 단계 잠재 속도를 운동학적 조작 가능성 맵(KAM)으로 해석합니다. KAM은 작업 조건화된 상호작용 영역과 대략적인 운동 구조를 제공하여, 분할 마스크와 같은 정적 사전 정보가 상호작용 위치만 인코딩하고 상호작용 시작 방식을 무시하는 한계를 보완합니다.

### 아키텍처 세부 사항
- **잠재 비디오 세계 모델**: rollout이나 미세 조정 없이 고정된 모델을 사용하며, 단일 단계 잠재 속도를 통해 방향성 단서만 제공합니다.
- **Flow Matching 백본 네트워크**: 이미지-비디오 백본 네트워크로, 한 번의 쿼리로 KAM을 생성합니다.
- **Perceiver 압축기**: 경량 모듈로, KAM을 토큰으로 압축하여 RGB 관측 및 고유 감각과 함께 확산 정책에 입력합니다.
- **확산 정책**: KAM 토큰, RGB 관측 및 고유 감각을 조건으로 조작 동작을 생성합니다.

### 실험 설정 및 결과
- **벤치마크 테스트**: LIBERO 및 RoboTwin2.0에서 평가를 수행했습니다.
- **LIBERO 결과**: 평균 성공률 90.6%를 달성했습니다.
- **RoboTwin2.0 결과**: Easy 설정에서 성공률 65.7%, Hard 설정에서 성공률 22.4%를 기록했습니다.
- **대조 실험**: 공간적 위치 파악만 제공하는 0차 마스크 사전 정보와 비교한 결과, KAM-WM의 성능 향상은 공간적 위치 파악뿐만 아니라 방향 정보에서 부분적으로 비롯됨을 보여줍니다.

### 결론
평가된 설정에서 고정된 비디오 모델은 테스트 시 미래 rollout 비용 없이 제어에 유용한 1차 시각적 사전 정보를 제공할 수 있습니다. KAM-WM은 방향성 상호작용 단서를 추출함으로써 소표본 조작 학습의 성능을显著히 향상시킵니다.
