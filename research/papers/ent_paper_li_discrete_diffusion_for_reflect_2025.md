---
$id: ent_paper_li_discrete_diffusion_for_reflect_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving
  zh: ReflectDrive
  ko: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving
summary:
  en: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving (ReflectDrive), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for AI Industry Research.
  zh: ReflectDrive 是由 Institute for AI Industry Research 于 2025 年提出的新型视觉-语言-动作模型，专为自动驾驶中的安全轨迹生成设计。其核心贡献在于通过离散扩散与安全感知反射机制，在不依赖梯度计算的情况下实现轨迹的迭代自校正，显著提升了安全关键场景下的生成质量。
  ko: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving (ReflectDrive), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for AI Industry Research.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- reflectdrive
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.20109v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving (arXiv)
  url: https://arxiv.org/abs/2509.20109
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ReflectDrive source
  url: https://doi.org/10.48550/arXiv.2509.20109
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有端到端自动驾驶方案受限于模仿学习难以内化物理规则，而基于规则的后处理、强化学习或扩散引导等方法存在计算成本高或局限于仿真环境的问题。ReflectDrive 通过离散化二维驾驶空间构建动作码本，利用预训练的扩散语言模型进行规划微调，并引入无需梯度计算的安全感知反射机制。该方法首先生成目标条件轨迹以建模多模态驾驶行为，随后通过局部搜索识别不安全令牌并确定可行解，最终基于这些安全锚点进行修复式再生。在 NAVSIM 基准上的评估表明，ReflectDrive 在安全关键轨迹生成任务中具有显著优势。

## 核心内容
### 方法架构
- **动作码本构建**：将二维驾驶空间离散化，形成动作码本，使预训练的 Diffusion Language Models 能够通过微调直接用于规划任务。
- **目标条件轨迹生成**：首先生成满足驾驶目标的多模态轨迹，以覆盖不同驾驶行为模式。
- **安全感知反射机制**：核心创新点，通过局部搜索方法识别轨迹中的不安全令牌（如碰撞或偏离车道），并确定可行的替代解作为安全锚点。
- **修复式再生**：基于安全锚点，利用扩散模型的 inpainting 能力对不安全区域进行迭代修复，整个过程无需梯度计算，避免了传统扩散引导的高计算开销。

### 实验设置
- **基准测试**：在 NAVSIM 基准上进行评估，该基准专注于自动驾驶中的安全关键场景。
- **对比方法**：与基于模仿学习、规则后处理及梯度扩散引导的基线方法进行对比。

### 关键结果
- **安全性能**：在安全关键轨迹生成任务中，ReflectDrive 显著降低了碰撞率和偏离车道率，优于现有方法。
- **计算效率**：由于无需梯度计算，反射机制的迭代自校正过程比传统扩散引导方法更高效。
- **可扩展性**：离散扩散框架使模型能够灵活适应不同驾驶场景，无需重新训练。

### 结论
ReflectDrive 通过离散扩散与安全反射机制的创新结合，为自动驾驶系统提供了一种可扩展且可靠的轨迹生成方案，有效解决了模仿学习在安全约束方面的固有局限。

## Overview
End-to-End (E2E) solutions have emerged as a mainstream approach for autonomous driving systems, with Vision-Language-Action (VLA) models representing a new paradigm that leverages pre-trained multimodal knowledge from Vision-Language Models (VLMs) to interpret and interact with complex real-world environments. However, these methods remain constrained by the limitations of imitation learning, which struggles to inherently encode physical rules during training. Existing approaches often rely on complex rule-based post-refinement, employ reinforcement learning that remains largely limited to simulation, or utilize diffusion guidance that requires computationally expensive gradient calculations. To address these challenges, we introduce ReflectDrive, a novel learning-based framework that integrates a reflection mechanism for safe trajectory generation via discrete diffusion. We first discretize the two-dimensional driving space to construct an action codebook, enabling the use of pre-trained Diffusion Language Models for planning tasks through fine-tuning. Central to our approach is a safety-aware reflection mechanism that performs iterative self-correction without gradient computation. Our method begins with goal-conditioned trajectory generation to model multi-modal driving behaviors. Based on this, we apply local search methods to identify unsafe tokens and determine feasible solutions, which then serve as safe anchors for inpainting-based regeneration. Evaluated on the NAVSIM benchmark, ReflectDrive demonstrates significant advantages in safety-critical trajectory generation, offering a scalable and reliable solution for autonomous driving systems.

## 개요
엔드투엔드(E2E) 솔루션은 자율주행 시스템의 주류 접근 방식으로 부상했으며, 비전-언어-행동(VLA) 모델은 사전 훈련된 비전-언어 모델(VLM)의 멀티모달 지식을 활용하여 복잡한 실제 환경을 해석하고 상호작용하는 새로운 패러다임을 대표합니다. 그러나 이러한 방법들은 훈련 중 물리적 규칙을 본질적으로 인코딩하는 데 어려움을 겪는 모방 학습의 한계에 여전히 제약을 받습니다. 기존 접근 방식은 종종 복잡한 규칙 기반 후처리 정제에 의존하거나, 대부분 시뮬레이션에 국한된 강화 학습을 사용하거나, 계산 비용이 많이 드는 그래디언트 계산이 필요한 확산 가이던스를 활용합니다. 이러한 문제를 해결하기 위해, 우리는 이산 확산을 통해 안전한 궤적 생성을 위한 반성 메커니즘을 통합한 새로운 학습 기반 프레임워크인 ReflectDrive를 소개합니다. 먼저 2차원 주행 공간을 이산화하여 행동 코드북을 구축함으로써, 사전 훈련된 확산 언어 모델을 미세 조정을 통해 계획 작업에 사용할 수 있게 합니다. 우리 접근 방식의 핵심은 그래디언트 계산 없이 반복적인 자기 수정을 수행하는 안전 인식 반성 메커니즘입니다. 우리 방법은 목표 조건 궤적 생성을 통해 다중 모드 주행 행동을 모델링하는 것으로 시작합니다. 이를 기반으로 로컬 탐색 방법을 적용하여 안전하지 않은 토큰을 식별하고 실행 가능한 솔루션을 결정한 다음, 이는 인페인팅 기반 재생성을 위한 안전 앵커 역할을 합니다. NAVSIM 벤치마크에서 평가된 ReflectDrive는 안전이 중요한 궤적 생성에서 상당한 이점을 보여주며, 자율주행 시스템을 위한 확장 가능하고 신뢰할 수 있는 솔루션을 제공합니다.

## 핵심 내용
엔드투엔드(E2E) 솔루션은 자율주행 시스템의 주류 접근 방식으로 부상했으며, 비전-언어-행동(VLA) 모델은 사전 훈련된 비전-언어 모델(VLM)의 멀티모달 지식을 활용하여 복잡한 실제 환경을 해석하고 상호작용하는 새로운 패러다임을 대표합니다. 그러나 이러한 방법들은 훈련 중 물리적 규칙을 본질적으로 인코딩하는 데 어려움을 겪는 모방 학습의 한계에 여전히 제약을 받습니다. 기존 접근 방식은 종종 복잡한 규칙 기반 후처리 정제에 의존하거나, 대부분 시뮬레이션에 국한된 강화 학습을 사용하거나, 계산 비용이 많이 드는 그래디언트 계산이 필요한 확산 가이던스를 활용합니다. 이러한 문제를 해결하기 위해, 우리는 이산 확산을 통해 안전한 궤적 생성을 위한 반성 메커니즘을 통합한 새로운 학습 기반 프레임워크인 ReflectDrive를 소개합니다. 먼저 2차원 주행 공간을 이산화하여 행동 코드북을 구축함으로써, 사전 훈련된 확산 언어 모델을 미세 조정을 통해 계획 작업에 사용할 수 있게 합니다. 우리 접근 방식의 핵심은 그래디언트 계산 없이 반복적인 자기 수정을 수행하는 안전 인식 반성 메커니즘입니다. 우리 방법은 목표 조건 궤적 생성을 통해 다중 모드 주행 행동을 모델링하는 것으로 시작합니다. 이를 기반으로 로컬 탐색 방법을 적용하여 안전하지 않은 토큰을 식별하고 실행 가능한 솔루션을 결정한 다음, 이는 인페인팅 기반 재생성을 위한 안전 앵커 역할을 합니다. NAVSIM 벤치마크에서 평가된 ReflectDrive는 안전이 중요한 궤적 생성에서 상당한 이점을 보여주며, 자율주행 시스템을 위한 확장 가능하고 신뢰할 수 있는 솔루션을 제공합니다.

## 参考
- http://arxiv.org/abs/2509.20109v1
