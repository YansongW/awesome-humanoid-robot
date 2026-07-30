---
$id: ent_paper_genmo_a_generalist_model_for_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GENMO: A GENeralist Model for Human MOtion'
  zh: 'GENMO: A GENeralist Model for Human MOtion'
  ko: 'GENMO: A GENeralist Model for Human MOtion'
summary:
  en: 'GENMO: A GENeralist Model for Human MOtion is a 2025 work on human motion analysis and synthesis for humanoid robots.'
  zh: GENMO 是 2025 年提出的统一人体运动通用模型，由研究团队开发，核心贡献在于将运动估计与运动生成整合为单一框架。该模型通过将运动估计重构为受约束的运动生成，并利用回归与扩散的协同作用，实现了精确的全局运动估计与多样化的运动生成。
  ko: 'GENMO: A GENeralist Model for Human MOtion is a 2025 work on human motion analysis and synthesis for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- genmo
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.01425v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'GENMO: A GENeralist Model for Human MOtion (arXiv)'
  url: https://arxiv.org/abs/2505.01425
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'GENMO: A GENeralist Model for Human MOtion project page'
  url: https://research.nvidia.com/labs/dair/genmo/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
传统人体运动建模将运动生成与估计视为独立任务，分别使用专用模型处理。GENMO 打破了这一界限，通过将运动估计重新定义为受观测信号约束的运动生成，实现了两者的统一。模型利用回归与扩散的协同效应，在保证运动估计精度的同时，支持多样化的运动生成。此外，GENMO 引入估计引导的训练目标，利用带有 2D 标注和文本描述的真实世界视频数据增强生成多样性。其新颖的架构能够处理可变长度运动及混合多模态条件（文本、音频、视频），在不同时间间隔提供灵活控制。

## 核心内容
### 方法
- **统一框架**：GENMO 的核心思想是将运动估计重新表述为受约束的运动生成，即输出运动必须精确满足观测到的条件信号（如视频、文本或音频）。
- **回归与扩散协同**：模型结合回归的精确性与扩散的多样性，实现全局运动估计与多样化生成的平衡。
- **估计引导训练**：利用带有 2D 标注和文本描述的真实世界视频数据，通过估计引导的训练目标增强生成多样性。

### 架构
- **可变长度处理**：架构支持处理不同长度的运动序列，适应多种输入条件。
- **多模态条件融合**：模型能够同时处理文本、音频、视频等混合多模态条件，并在不同时间间隔提供灵活控制。

### 实验设置与关键数字
- **任务覆盖**：GENMO 在多个运动任务上验证有效性，包括运动估计与生成。
- **性能提升**：在遮挡等挑战性条件下，生成先验显著改善了运动估计质量；同时，多样化视频数据增强了生成能力。
- **统一模型优势**：实验表明，GENMO 作为通用框架，在单一模型中成功处理多种人体运动任务，避免了维护多个专用模型的成本。

### 结论
GENMO 通过统一运动估计与生成，展示了协同效益：生成先验提升估计鲁棒性，而视频数据增强生成多样性。该模型为人体运动分析与人形机器人应用提供了高效、灵活的解决方案。

## Overview
Human motion modeling traditionally separates motion generation and estimation into distinct tasks with specialized models. Motion generation models focus on creating diverse, realistic motions from inputs like text, audio, or keyframes, while motion estimation models aim to reconstruct accurate motion trajectories from observations like videos. Despite sharing underlying representations of temporal dynamics and kinematics, this separation limits knowledge transfer between tasks and requires maintaining separate models. We present GENMO, a unified Generalist Model for Human Motion that bridges motion estimation and generation in a single framework. Our key insight is to reformulate motion estimation as constrained motion generation, where the output motion must precisely satisfy observed conditioning signals. Leveraging the synergy between regression and diffusion, GENMO achieves accurate global motion estimation while enabling diverse motion generation. We also introduce an estimation-guided training objective that exploits in-the-wild videos with 2D annotations and text descriptions to enhance generative diversity. Furthermore, our novel architecture handles variable-length motions and mixed multimodal conditions (text, audio, video) at different time intervals, offering flexible control. This unified approach creates synergistic benefits: generative priors improve estimated motions under challenging conditions like occlusions, while diverse video data enhances generation capabilities. Extensive experiments demonstrate GENMO's effectiveness as a generalist framework that successfully handles multiple human motion tasks within a single model.

## 개요
인간 동작 모델링은 전통적으로 동작 생성과 추정을 별개의 작업으로 분리하여 각각에 특화된 모델을 사용해 왔습니다. 동작 생성 모델은 텍스트, 오디오, 키프레임 등의 입력으로부터 다양하고 사실적인 동작을 생성하는 데 초점을 맞추는 반면, 동작 추정 모델은 비디오와 같은 관찰 데이터로부터 정확한 동작 궤적을 재구성하는 것을 목표로 합니다. 시간적 역학과 운동학의 기본 표현을 공유함에도 불구하고, 이러한 분리는 작업 간 지식 전달을 제한하고 별도의 모델을 유지해야 하는 단점이 있습니다. 본 논문에서는 동작 추정과 생성을 단일 프레임워크로 연결하는 통합된 인간 동작 제너럴리스트 모델인 GENMO를 제안합니다. 핵심 통찰은 동작 추정을 제약 조건이 있는 동작 생성으로 재정의하여, 출력 동작이 관찰된 조건 신호를 정확히 충족하도록 하는 것입니다. 회귀와 확산 간의 시너지를 활용하여 GENMO는 정확한 전역 동작 추정을 달성하는 동시에 다양한 동작 생성을 가능하게 합니다. 또한, 2D 주석과 텍스트 설명이 포함된 실제 비디오를 활용하는 추정 유도 학습 목표를 도입하여 생성 다양성을 향상시킵니다. 더 나아가, 새로운 아키텍처는 가변 길이 동작과 다양한 시간 간격의 혼합 다중 모달 조건(텍스트, 오디오, 비디오)을 처리하여 유연한 제어를 제공합니다. 이러한 통합 접근 방식은 시너지 효과를 창출합니다: 생성적 사전 지식은 폐색과 같은 까다로운 조건에서 추정 동작을 개선하고, 다양한 비디오 데이터는 생성 능력을 향상시킵니다. 광범위한 실험을 통해 GENMO가 단일 모델 내에서 여러 인간 동작 작업을 성공적으로 처리하는 제너럴리스트 프레임워크로서의 효과성을 입증합니다.

## 핵심 내용
인간 동작 모델링은 전통적으로 동작 생성과 추정을 별개의 작업으로 분리하여 각각에 특화된 모델을 사용해 왔습니다. 동작 생성 모델은 텍스트, 오디오, 키프레임 등의 입력으로부터 다양하고 사실적인 동작을 생성하는 데 초점을 맞추는 반면, 동작 추정 모델은 비디오와 같은 관찰 데이터로부터 정확한 동작 궤적을 재구성하는 것을 목표로 합니다. 시간적 역학과 운동학의 기본 표현을 공유함에도 불구하고, 이러한 분리는 작업 간 지식 전달을 제한하고 별도의 모델을 유지해야 하는 단점이 있습니다. 본 논문에서는 동작 추정과 생성을 단일 프레임워크로 연결하는 통합된 인간 동작 제너럴리스트 모델인 GENMO를 제안합니다. 핵심 통찰은 동작 추정을 제약 조건이 있는 동작 생성으로 재정의하여, 출력 동작이 관찰된 조건 신호를 정확히 충족하도록 하는 것입니다. 회귀와 확산 간의 시너지를 활용하여 GENMO는 정확한 전역 동작 추정을 달성하는 동시에 다양한 동작 생성을 가능하게 합니다. 또한, 2D 주석과 텍스트 설명이 포함된 실제 비디오를 활용하는 추정 유도 학습 목표를 도입하여 생성 다양성을 향상시킵니다. 더 나아가, 새로운 아키텍처는 가변 길이 동작과 다양한 시간 간격의 혼합 다중 모달 조건(텍스트, 오디오, 비디오)을 처리하여 유연한 제어를 제공합니다. 이러한 통합 접근 방식은 시너지 효과를 창출합니다: 생성적 사전 지식은 폐색과 같은 까다로운 조건에서 추정 동작을 개선하고, 다양한 비디오 데이터는 생성 능력을 향상시킵니다. 광범위한 실험을 통해 GENMO가 단일 모델 내에서 여러 인간 동작 작업을 성공적으로 처리하는 제너럴리스트 프레임워크로서의 효과성을 입증합니다.

## 参考
- http://arxiv.org/abs/2505.01425v1
