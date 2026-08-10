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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.01425v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (802 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2505.01425v1

## 개요
전통적인 인간 동작 모델링은 동작 생성과 추정을 독립적인 작업으로 간주하여 각각 전용 모델로 처리했습니다. GENMO는 이러한 경계를 허물고, 동작 추정을 관측 신호에 제약된 동작 생성으로 재정의하여 두 작업을 통합합니다. 이 모델은 회귀와 확산의 시너지 효과를 활용하여 동작 추정 정확도를 보장하면서도 다양한 동작 생성을 지원합니다. 또한, GENMO는 추정 유도 훈련 목표를 도입하여 2D 주석과 텍스트 설명이 포함된 실제 세계 비디오 데이터를 활용해 생성 다양성을 강화합니다. 그 참신한 아키텍처는 가변 길이 동작 및 혼합 다중 모달 조건(텍스트, 오디오, 비디오)을 처리할 수 있으며, 다양한 시간 간격에서 유연한 제어를 제공합니다.

## 핵심 내용
### 방법
- **통합 프레임워크**: GENMO의 핵심 아이디어는 동작 추정을 제약된 동작 생성으로 재정의하는 것입니다. 즉, 출력 동작은 관측된 조건 신호(예: 비디오, 텍스트, 오디오)를 정확히 충족해야 합니다.
- **회귀와 확산의 시너지**: 이 모델은 회귀의 정확성과 확산의 다양성을 결합하여 전역 동작 추정과 다양한 생성 간의 균형을 실현합니다.
- **추정 유도 훈련**: 2D 주석과 텍스트 설명이 포함된 실제 세계 비디오 데이터를 활용하여 추정 유도 훈련 목표를 통해 생성 다양성을 강화합니다.

### 아키텍처
- **가변 길이 처리**: 아키텍처는 다양한 길이의 동작 시퀀스를 처리할 수 있어 여러 입력 조건에 적응합니다.
- **다중 모달 조건 융합**: 모델은 텍스트, 오디오, 비디오 등 혼합 다중 모달 조건을 동시에 처리할 수 있으며, 다양한 시간 간격에서 유연한 제어를 제공합니다.

### 실험 설정 및 주요 수치
- **작업 범위**: GENMO는 동작 추정 및 생성을 포함한 여러 동작 작업에서 유효성을 검증했습니다.
- **성능 향상**: 폐색과 같은 도전적인 조건에서 생성 사전 정보가 동작 추정 품질을 크게 개선했으며, 다양한 비디오 데이터가 생성 능력을 강화했습니다.
- **통합 모델의 장점**: 실험 결과, GENMO는 범용 프레임워크로서 단일 모델에서 여러 인간 동작 작업을 성공적으로 처리하여 여러 전용 모델을 유지하는 비용을 피할 수 있음을 보여주었습니다.

### 결론
GENMO는 동작 추정과 생성을 통합함으로써 시너지 효과를 입증했습니다: 생성 사전 정보는 추정 견고성을 향상시키고, 비디오 데이터는 생성 다양성을 강화합니다. 이 모델은 인간 동작 분석 및 휴머노이드 로봇 응용을 위한 효율적이고 유연한 솔루션을 제공합니다.
