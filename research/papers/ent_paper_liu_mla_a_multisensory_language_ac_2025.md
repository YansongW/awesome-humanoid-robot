---
$id: ent_paper_liu_mla_a_multisensory_language_ac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation'
  zh: MLA
  ko: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation'
summary:
  en: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation (MLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia
    Information Processing, School of Computer Science, Peking University, Beijing Innovation Center of Humanoid Robotics,
    Chinese University of Hong Kong.'
  zh: MLA（Multisensory Language-Action Model）是由北京大学多媒体信息处理国家重点实验室、计算机学院、北京人形机器人创新中心及香港中文大学联合提出的2025年大型视觉-语言-动作模型。其核心贡献在于通过无编码器多模态对齐方案和未来多感官生成后训练策略，使机器人能协同感知2D图像、3D点云与触觉信号，并在复杂接触密集型真实世界任务中超越现有2D和3D
    VLA方法12%和24%。
  ko: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation (MLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia
    Information Processing, School of Computer Science, Peking University, Beijing Innovation Center of Humanoid Robotics,
    Chinese University of Hong Kong.'
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
- mla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.26642v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (694 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.26642
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MLA source
  url: https://doi.org/10.48550/arXiv.2509.26642
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有VLA模型主要依赖视觉和语言生成动作，但缺乏对机器人专用多感官信息的综合理解，难以应对空间物理世界的复杂交互。MLA模型通过创新性地将大语言模型本身作为感知模块，直接对齐2D图像、3D点云和触觉令牌的位置对应关系，无需传统编码器。此外，MLA引入未来多感官生成后训练策略，使其能推理语义、几何和交互信息，为动作生成提供更鲁棒的条件。实验表明，MLA在复杂接触密集型真实任务中显著优于先前最优方法，并展现出对未见配置的泛化能力。

## 核心内容
### 方法架构
MLA模型的核心创新包括两部分：
- **无编码器多模态对齐方案**：摒弃传统编码器，直接利用大语言模型作为感知模块，通过位置对应关系对齐2D图像、3D点云和触觉令牌，实现异构感官模态的协同感知。
- **未来多感官生成后训练策略**：在预训练后引入该策略，使模型能推理未来时刻的语义、几何和交互信息，从而增强对物理动力学的理解，为动作生成提供更丰富的条件。

### 实验设置与关键结果
- **任务类型**：复杂、接触密集的真实世界机器人操作任务。
- **性能对比**：MLA在相同任务上，相比之前最优的2D VLA方法提升12%，相比3D VLA方法提升24%。
- **泛化能力**：在未见配置（如新物体位置、新工具形状）下，MLA仍保持稳定性能，验证了其多感官理解对物理世界建模的有效性。

### 结论
MLA通过多感官协同感知与未来预测，弥补了现有VLA模型在空间物理理解上的不足，为接触密集型机器人操作提供了更鲁棒的解决方案。其无编码器对齐方案和未来生成策略为多模态机器人学习提供了新范式。

## Overview
Vision-language-action models (VLAs) have shown generalization capabilities in robotic manipulation tasks by inheriting from vision-language models (VLMs) and learning action generation. Most VLA models focus on interpreting vision and language to generate actions, whereas robots must perceive and interact within the spatial-physical world. This gap highlights the need for a comprehensive understanding of robotic-specific multisensory information, which is crucial for achieving complex and contact-rich control. To this end, we introduce a multisensory language-action (MLA) model that collaboratively perceives heterogeneous sensory modalities and predicts future multisensory objectives to facilitate physical world modeling. Specifically, to enhance perceptual representations, we propose an encoder-free multimodal alignment scheme that innovatively repurposes the large language model itself as a perception module, directly interpreting multimodal cues by aligning 2D images, 3D point clouds, and tactile tokens through positional correspondence. To further enhance MLA's understanding of physical dynamics, we design a future multisensory generation post-training strategy that enables MLA to reason about semantic, geometric, and interaction information, providing more robust conditions for action generation. For evaluation, the MLA model outperforms the previous state-of-the-art 2D and 3D VLA methods by 12% and 24% in complex, contact-rich real-world tasks, respectively, while also demonstrating improved generalization to unseen configurations.

## 参考
- http://arxiv.org/abs/2509.26642v2

## 개요
기존 VLA 모델은 주로 시각과 언어를 기반으로 동작을 생성하지만, 로봇 전용 다중 감각 정보에 대한 종합적 이해가 부족하여 공간적 물리 세계의 복잡한 상호작용을 처리하기 어렵습니다. MLA 모델은 대형 언어 모델 자체를 혁신적으로 지각 모듈로 활용하여, 전통적인 인코더 없이 2D 이미지, 3D 포인트 클라우드 및 촉각 토큰의 위치 대응 관계를 직접 정렬합니다. 또한, MLA는 미래 다중 감각 생성 후훈련 전략을 도입하여 의미, 기하 및 상호작용 정보를 추론할 수 있게 하여 동작 생성에 더 견고한 조건을 제공합니다. 실험 결과, MLA는 복잡한 접촉 집약적 실제 작업에서 이전 최적 방법보다 현저히 우수하며, 보지 못한 구성에 대한 일반화 능력을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
MLA 모델의 핵심 혁신은 두 부분으로 구성됩니다:
- **인코더 없는 다중 모달 정렬 방식**: 전통적인 인코더를 버리고 대형 언어 모델을 직접 지각 모듈로 사용하여, 위치 대응 관계를 통해 2D 이미지, 3D 포인트 클라우드 및 촉각 토큰을 정렬함으로써 이질적 감각 양식의 협력적 지각을 실현합니다.
- **미래 다중 감각 생성 후훈련 전략**: 사전 훈련 후 이 전략을 도입하여 모델이 미래 시점의 의미, 기하 및 상호작용 정보를 추론할 수 있게 하여 물리 역학에 대한 이해를 강화하고 동작 생성에 더 풍부한 조건을 제공합니다.

### 실험 설정 및 주요 결과
- **작업 유형**: 복잡하고 접촉이 집약적인 실제 로봇 조작 작업.
- **성능 비교**: MLA는 동일한 작업에서 이전 최적의 2D VLA 방법보다 12% 향상되었고, 3D VLA 방법보다 24% 향상되었습니다.
- **일반화 능력**: 보지 못한 구성(예: 새로운 물체 위치, 새로운 도구 형태)에서도 MLA는 안정적인 성능을 유지하여, 다중 감각 이해가 물리 세계 모델링에 효과적임을 검증합니다.

### 결론
MLA는 다중 감각 협력 지각과 미래 예측을 통해 기존 VLA 모델의 공간 물리 이해 부족을 보완하여, 접촉 집약적 로봇 조작에 더 견고한 솔루션을 제공합니다. 인코더 없는 정렬 방식과 미래 생성 전략은 다중 모달 로봇 학습에 새로운 패러다임을 제시합니다.
