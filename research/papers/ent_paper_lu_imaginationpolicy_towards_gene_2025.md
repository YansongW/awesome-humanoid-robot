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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.20841v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (921 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.20841v1

## 개요
전통적인 모듈식 흐름과 달리, 엔드투엔드 학습은 모듈 간 정보 손실과 특징 불일치 문제를 피할 수 있습니다. 그러나 대규모 실제 배포에서 기존의 엔드투엔드 신경망(대형 VLM/VLA 기반 모델 포함)의 성능은 여전히 부족합니다. 이를 위해 ImaginationPolicy는 CoMOK 동작 표현을 제안하며, 이는 엔드투엔드로 훈련 가능하고 표준 엔드이펙터 포즈 표현을 확장하여 다양한 조작 작업을 통일된 방식으로 지원합니다. 방향성 키포인트 설계는 모델이 다양한 모양과 크기의 객체에 자연스럽게 일반화되도록 하면서 서브센티미터 정밀도를 달성합니다.

## 핵심 내용
### 방법
ImaginationPolicy의 핵심 혁신은 **Chain of Moving Oriented Keypoints (CoMOK)** 동작 표현입니다. 이 표현은 로봇 조작 동작을 방향 정보를 포함한 일련의 키포인트 궤적으로 분해하며, 신경망의 출력 목표로 엔드투엔드 훈련됩니다.

- **통일성**: CoMOK는 표준 엔드이펙터 포즈 표현을 확장하여 파지, 배치, 밀기/당기기 등 다양한 조작 작업을 통일된 프레임워크로 지원할 수 있습니다.
- **일반화**: 방향성 키포인트 설계는 모델이 특정 객체에 재훈련 없이 다양한 모양과 크기의 객체에 적응할 수 있게 합니다.
- **정밀도**: 실험 결과, 이 방법은 서브센티미터(sub-centimeter) 수준의 조작 정밀도를 달성할 수 있습니다.
- **다중 작업 처리**: CoMOK는 다단계 작업, 다중 모드 로봇 행동, 변형 가능한 객체 조작을 자연스럽게 처리할 수 있습니다.

### 실험 설정
- **시뮬레이션 실험**: 다양한 작업 유형과 객체 범주를 포함한 여러 표준 로봇 조작 벤치마크에서 광범위하게 테스트되었습니다.
- **하드웨어 실험**: 실제 로봇 플랫폼에서 변형 가능한 객체(예: 천, 로프) 조작을 포함한 방법의 유효성을 검증했습니다.

### 주요 결과
- 시뮬레이션 환경에서 ImaginationPolicy는 다양한 작업에서 기존 엔드투엔드 방법보다 성공률이 현저히 우수했습니다.
- 실제 하드웨어 실험에서 모델은 보지 못한 객체와 장면을 처리할 수 있는 우수한 일반화 능력을 보여주었습니다.
- 표준 엔드이펙터 포즈 기반 방법과 비교하여 CoMOK는 정밀도와 작업 성공률 모두에서 뚜렷한 향상을 보였습니다.

### 결론
ImaginationPolicy는 CoMOK 동작 표현을 통해 엔드투엔드 로봇 조작 정책의 일반화 가능성, 정밀도, 신뢰성에서 중요한 진전을 이루었습니다. 이 방법은 특히 높은 정밀도와 유연성이 필요한 복잡한 조작 시나리오에 적합한 대규모 실제 배포의 새로운 가능성을 제공합니다.
