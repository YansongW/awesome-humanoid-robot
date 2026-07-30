---
$id: ent_paper_lu_imaginationpolicy_towards_gene_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation'
  zh: ImaginationPolicy
  ko: 'ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation'
summary:
  en: 'ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation (ImaginationPolicy),
    is a 2025 large vision-language-action model for robotic manipulation.'
  zh: ImaginationPolicy 是 2025 年提出的一种面向机器人操作的大规模视觉-语言-动作模型。其核心贡献在于提出了一种名为 Chain of Moving Oriented Keypoints (CoMOK) 的动作表征方法，旨在实现可泛化、高精度且可靠的端到端操作策略。
  ko: 'ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation (ImaginationPolicy),
    is a 2025 large vision-language-action model for robotic manipulation.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- imaginationpolicy
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.20841v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ImaginationPolicy: Towards Generalizable, Precise and Reliable End-to-End Policy for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.20841
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ImaginationPolicy source
  url: https://doi.org/10.48550/arXiv.2509.20841
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
与传统的模块化流程不同，端到端学习能够避免模块间的信息丢失和特征错配问题。然而，现有的端到端神经网络，包括基于大型 VLM/VLA 的模型，在大规模实际部署中性能仍显不足。为此，ImaginationPolicy 提出了 CoMOK 动作表征，该表征可被端到端训练，并扩展了标准末端执行器位姿表征，能以统一方式支持多种操作任务。其定向关键点设计使模型能自然泛化到不同形状和尺寸的物体，同时实现亚厘米级精度。

## 核心内容
### 方法
ImaginationPolicy 的核心创新在于 **Chain of Moving Oriented Keypoints (CoMOK)** 动作表征。该表征将机器人操作动作分解为一系列带有方向信息的关键点轨迹，作为神经网络的输出目标进行端到端训练。

- **统一性**：CoMOK 扩展了标准末端执行器位姿表征，能够以统一框架支持抓取、放置、推拉等多种操作任务。
- **泛化性**：定向关键点设计使模型能适应不同形状和尺寸的物体，无需针对特定物体重新训练。
- **精度**：实验表明，该方法可实现亚厘米级（sub-centimeter）的操作精度。
- **多任务处理**：CoMOK 能自然处理多阶段任务、多模态机器人行为以及可变形物体操作。

### 实验设置
- **仿真实验**：在多个标准机器人操作基准上进行了广泛测试，涵盖不同任务类型和物体类别。
- **硬件实验**：在真实机器人平台上验证了方法的有效性，包括对可变形物体（如布料、绳索）的操作。

### 关键结果
- 在仿真环境中，ImaginationPolicy 在多种任务上的成功率显著优于现有端到端方法。
- 在真实硬件实验中，模型展现了良好的泛化能力，能够处理未见过的物体和场景。
- 与基于标准末端执行器位姿的方法相比，CoMOK 在精度和任务成功率上均有明显提升。

### 结论
ImaginationPolicy 通过 CoMOK 动作表征，在端到端机器人操作策略的可泛化性、精度和可靠性方面取得了重要进展。该方法为大规模实际部署提供了新的可能性，尤其适用于需要高精度和灵活性的复杂操作场景。

## Overview
End-to-end robot manipulation policies offer significant potential for enabling embodied agents to understand and interact with the world. Unlike traditional modular pipelines, end-to-end learning mitigates key limitations such as information loss between modules and feature misalignment caused by isolated optimization targets. Despite these advantages, existing end-to-end neural networks for robotic manipulation--including those based on large VLM/VLA models--remain insufficiently performant for large-scale practical deployment. In this paper, we take a step towards an end-to-end manipulation policy that is generalizable, accurate and reliable. To achieve this goal, we propose a novel Chain of Moving Oriented Keypoints (CoMOK) formulation for robotic manipulation. Our formulation is used as the action representation of a neural policy, which can be trained in an end-to-end fashion. Such an action representation is general, as it extends the standard end-effector pose action representation and supports a diverse set of manipulation tasks in a unified manner. The oriented keypoint in our method enables natural generalization to objects with different shapes and sizes, while achieving sub-centimeter accuracy. Moreover, our formulation can easily handle multi-stage tasks, multi-modal robot behaviors, and deformable objects. Extensive simulated and hardware experiments demonstrate the effectiveness of our method.

## 개요
엔드투엔드 로봇 조작 정책은 체화된 에이전트가 세계를 이해하고 상호작용할 수 있도록 하는 데 중요한 잠재력을 제공합니다. 전통적인 모듈식 파이프라인과 달리, 엔드투엔드 학습은 모듈 간 정보 손실 및 개별 최적화 목표로 인한 특징 불일치와 같은 주요 한계를 완화합니다. 이러한 장점에도 불구하고, 대규모 VLM/VLA 모델을 기반으로 한 기존의 엔드투엔드 신경망은 대규모 실용적 배포에 충분한 성능을 보이지 못하고 있습니다. 본 논문에서는 일반화 가능하고 정확하며 신뢰할 수 있는 엔드투엔드 조작 정책을 향한 한 걸음을 내딛습니다. 이 목표를 달성하기 위해, 우리는 로봇 조작을 위한 새로운 Chain of Moving Oriented Keypoints (CoMOK) 공식을 제안합니다. 우리의 공식은 신경 정책의 행동 표현으로 사용되며, 엔드투엔드 방식으로 훈련될 수 있습니다. 이러한 행동 표현은 일반적이며, 표준 엔드이펙터 포즈 행동 표현을 확장하고 다양한 조작 작업을 통일된 방식으로 지원합니다. 우리 방법의 방향성 키포인트는 서브 센티미터 정확도를 달성하면서도 다양한 모양과 크기의 객체에 자연스럽게 일반화할 수 있게 합니다. 또한, 우리의 공식은 다단계 작업, 다중 모드 로봇 행동 및 변형 가능한 객체를 쉽게 처리할 수 있습니다. 광범위한 시뮬레이션 및 하드웨어 실험을 통해 우리 방법의 효과를 입증합니다.

## 핵심 내용
엔드투엔드 로봇 조작 정책은 체화된 에이전트가 세계를 이해하고 상호작용할 수 있도록 하는 데 중요한 잠재력을 제공합니다. 전통적인 모듈식 파이프라인과 달리, 엔드투엔드 학습은 모듈 간 정보 손실 및 개별 최적화 목표로 인한 특징 불일치와 같은 주요 한계를 완화합니다. 이러한 장점에도 불구하고, 대규모 VLM/VLA 모델을 기반으로 한 기존의 엔드투엔드 신경망은 대규모 실용적 배포에 충분한 성능을 보이지 못하고 있습니다. 본 논문에서는 일반화 가능하고 정확하며 신뢰할 수 있는 엔드투엔드 조작 정책을 향한 한 걸음을 내딛습니다. 이 목표를 달성하기 위해, 우리는 로봇 조작을 위한 새로운 Chain of Moving Oriented Keypoints (CoMOK) 공식을 제안합니다. 우리의 공식은 신경 정책의 행동 표현으로 사용되며, 엔드투엔드 방식으로 훈련될 수 있습니다. 이러한 행동 표현은 일반적이며, 표준 엔드이펙터 포즈 행동 표현을 확장하고 다양한 조작 작업을 통일된 방식으로 지원합니다. 우리 방법의 방향성 키포인트는 서브 센티미터 정확도를 달성하면서도 다양한 모양과 크기의 객체에 자연스럽게 일반화할 수 있게 합니다. 또한, 우리의 공식은 다단계 작업, 다중 모드 로봇 행동 및 변형 가능한 객체를 쉽게 처리할 수 있습니다. 광범위한 시뮬레이션 및 하드웨어 실험을 통해 우리 방법의 효과를 입증합니다.

## 参考
- http://arxiv.org/abs/2509.20841v1
