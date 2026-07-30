---
$id: ent_paper_physically_grounded_3d_generat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
  zh: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
  ko: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
summary:
  en: 'arXiv:2604.09100v2 Announce Type: replace-cross Abstract: We propose a multimodal, physically grounded approach for
    metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware
    3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the
    posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded
    regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact
    latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining
    on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility
    masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and
    differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the
    reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure
    estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines
    geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves
    completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only
    baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different
    from those used during training.'
  zh: 本文提出一种多模态物理驱动方法，用于在严重手部遮挡下进行公制尺度无模态物体重建与位姿估计。该方法由团队利用本体感知提供手部姿态几何，结合多点触觉约束物体表面位置，并通过Structure-VAE与条件流匹配扩散模型实现物理一致的重建。实验表明，相比纯视觉基线，该方法显著提升遮挡区域补全质量，并成功迁移至真实人形机器人。
  ko: 'arXiv:2604.09100v2 Announce Type: replace-cross Abstract: We propose a multimodal, physically grounded approach for
    metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware
    3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the
    posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded
    regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact
    latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining
    on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility
    masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and
    differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the
    reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure
    estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines
    geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves
    completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only
    baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different
    from those used during training.'
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
- physically_grounded_3d_generat
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.09100v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
  url: https://arxiv.org/abs/2604.09100
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有遮挡感知3D生成方法仅依赖视觉信号，在严重手部遮挡下难以准确重建物体。本文创新性地引入物理交互信号：本体感知提供手部姿态几何，多点触觉约束物体表面位置，从而减少遮挡区域的歧义。方法采用姿态感知、相机对齐的有符号距离场（SDF）表示物体结构，并通过Structure-VAE学习紧凑隐空间。在该隐空间中训练条件流匹配扩散模型，先以纯视觉图像预训练，再在遮挡操作场景中微调，同时以可见RGB证据、遮挡/可见性掩码、手部隐表示和触觉信息为条件。关键创新在于微调和推理阶段引入基于物理的目标函数与可微解码器引导，以减少手-物体穿插并确保重建表面与接触观测对齐。仿真实验证明，相比纯视觉基线，加入本体感知和触觉显著提升遮挡补全质量，并生成正确真实尺度的物理合理重建；模型还成功迁移至使用不同末端执行器的真实人形机器人。

## 核心内容
### 方法架构
- **多模态输入**：结合可见RGB图像、遮挡/可见性掩码、手部隐表示（来自本体感知）和触觉信息。
- **物体表示**：采用姿态感知、相机对齐的SDF，通过Structure-VAE学习紧凑隐空间。
- **生成模型**：在隐空间中训练条件流匹配扩散模型，先以纯视觉图像预训练，再在遮挡操作场景中微调。
- **物理约束**：微调和推理阶段引入基于物理的目标函数与可微解码器引导，减少手-物体穿插，确保重建表面与接触观测对齐。

### 实验设置
- **仿真环境**：在模拟场景中评估，对比纯视觉基线方法。
- **真实迁移**：将模型部署至真实人形机器人，使用与训练时不同的末端执行器。
- **评估指标**：关注遮挡区域补全质量、物理合理性（如穿插程度）和公制尺度准确性。

### 关键结果
- **遮挡补全**：加入本体感知和触觉后，遮挡区域补全质量显著优于纯视觉基线。
- **物理合理性**：生成的重建在正确真实尺度下具有物理合理性，手-物体穿插大幅减少。
- **迁移能力**：模型成功泛化至不同末端执行器的真实机器人，验证了方法的鲁棒性。

### 结论
本文证明物理交互信号（本体感知与多点触觉）能有效解决严重手部遮挡下的3D重建问题，生成公制尺度、物理一致的结构估计，并自然集成至现有两阶段重建流水线。

## Overview
We propose a multimodal, physically grounded approach for metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware 3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different from those used during training.

## Overview
We propose a multimodal, physically grounded approach for metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware 3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and differentiable decoder-guidance during finetuning and inference to reduce hand–object interpenetration and to align the reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different from those used during training.

## Content
We propose a multimodal, physically grounded approach for metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware 3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and differentiable decoder-guidance during finetuning and inference to reduce hand–object interpenetration and to align the reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different from those used during training.

## 개요
본 연구는 심한 손 가림(hand occlusion) 상황에서 미터법 스케일의 아모달(amodal) 객체 재구성 및 자세 추정을 위한 다중 모달, 물리 기반 접근법을 제안합니다. 시각에만 의존하는 기존의 가림 인식 3D 생성 방법과 달리, 우리는 물리적 상호작용 신호를 활용합니다: 고유수용감각(proprioception)은 손의 자세 기하학을 제공하고, 다중 접촉 터치는 객체 표면이 위치해야 할 곳을 제약하여 가려진 영역의 모호성을 줄입니다. 객체 구조를 자세 인식, 카메라 정렬 부호 거리 필드(SDF)로 표현하고 Structure-VAE로 컴팩트한 잠재 공간을 학습합니다. 이 잠재 공간에서 조건부 흐름 매칭 확산 모델을 훈련하며, 시각 전용 이미지로 사전 훈련하고 가려진 조작 장면에서 미세 조정합니다. 이때 가시적인 RGB 증거, 가림/가시성 마스크, 손 잠재 표현, 촉각 정보를 조건으로 사용합니다. 핵심적으로, 미세 조정 및 추론 중 물리 기반 목표와 미분 가능 디코더 가이던스를 통합하여 손-객체 간 침투를 줄이고 재구성된 표면을 접촉 관측과 정렬합니다. 본 방법은 미터법, 물리적으로 일관된 구조 추정치를 생성하므로, 하위 모듈이 기하학을 정제하고 외관을 예측하는 기존의 2단계 재구성 파이프라인에 자연스럽게 통합됩니다. 시뮬레이션 실험에서 고유수용감각과 터치를 추가하면 가림 하에서 완성도가 크게 향상되고, 시각 전용 기준선과 비교하여 올바른 실제 세계 스케일에서 물리적으로 그럴듯한 재구성을 제공함을 보여줍니다. 또한, 훈련 중 사용된 것과 다른 엔드 이펙터를 가진 실제 인간형 로봇에 모델을 배포하여 전이 가능성을 검증합니다.

## 핵심 내용
본 연구는 심한 손 가림 상황에서 미터법 스케일의 아모달 객체 재구성 및 자세 추정을 위한 다중 모달, 물리 기반 접근법을 제안합니다. 시각에만 의존하는 기존의 가림 인식 3D 생성 방법과 달리, 우리는 물리적 상호작용 신호를 활용합니다: 고유수용감각은 손의 자세 기하학을 제공하고, 다중 접촉 터치는 객체 표면이 위치해야 할 곳을 제약하여 가려진 영역의 모호성을 줄입니다. 객체 구조를 자세 인식, 카메라 정렬 부호 거리 필드(SDF)로 표현하고 Structure-VAE로 컴팩트한 잠재 공간을 학습합니다. 이 잠재 공간에서 조건부 흐름 매칭 확산 모델을 훈련하며, 시각 전용 이미지로 사전 훈련하고 가려진 조작 장면에서 미세 조정합니다. 이때 가시적인 RGB 증거, 가림/가시성 마스크, 손 잠재 표현, 촉각 정보를 조건으로 사용합니다. 핵심적으로, 미세 조정 및 추론 중 물리 기반 목표와 미분 가능 디코더 가이던스를 통합하여 손-객체 간 침투를 줄이고 재구성된 표면을 접촉 관측과 정렬합니다. 본 방법은 미터법, 물리적으로 일관된 구조 추정치를 생성하므로, 하위 모듈이 기하학을 정제하고 외관을 예측하는 기존의 2단계 재구성 파이프라인에 자연스럽게 통합됩니다. 시뮬레이션 실험에서 고유수용감각과 터치를 추가하면 가림 하에서 완성도가 크게 향상되고, 시각 전용 기준선과 비교하여 올바른 실제 세계 스케일에서 물리적으로 그럴듯한 재구성을 제공함을 보여줍니다. 또한, 훈련 중 사용된 것과 다른 엔드 이펙터를 가진 실제 인간형 로봇에 모델을 배포하여 전이 가능성을 검증합니다.

## 参考
- http://arxiv.org/abs/2604.09100v2
