---
$id: ent_paper_bi_motus_a_unified_latent_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Motus: A Unified Latent Action World Model'
  zh: Motus
  ko: 'Motus: A Unified Latent Action World Model'
summary:
  en: 'Motus: A Unified Latent Action World Model (Motus), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Bosch, Tsinghua University, Peking University, Horizon Robotics.'
  zh: Motus 是2025年由博世、清华大学、北京大学和地平线机器人联合提出的大型视觉-语言-动作世界模型。其核心贡献在于通过 Mixture-of-Transformer 架构统一了理解、视频生成和动作三个专家模块，并利用光流学习潜在动作，实现了从大规模异构数据中预训练。实验表明，Motus
    在仿真和真实场景中均显著优于现有方法。
  ko: 'Motus: A Unified Latent Action World Model (Motus), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Bosch, Tsinghua University, Peking University, Horizon Robotics.'
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
- motus
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.13030v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1007 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Motus: A Unified Latent Action World Model (arXiv)'
  url: https://arxiv.org/abs/2512.13030
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Motus source
  url: https://doi.org/10.48550/arXiv.2512.13030
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Motus 旨在解决当前具身智能体因模型碎片化而无法统一多模态生成能力的问题。它采用 Mixture-of-Transformer 架构整合理解、视频生成和动作三个专家，并借鉴 UniDiffuser 调度器实现世界模型、视觉-语言-动作模型、逆动力学模型等多种建模模式的灵活切换。通过光流提取像素级“增量动作”，Motus 构建了三阶段训练流程和六层数据金字塔，实现了大规模动作预训练。在仿真环境中，Motus 相比 X-VLA 提升 15%，相比 Pi0.5 提升 45%；在真实场景中，性能提升幅度达 11% 至 48%。

## 核心内容
### 方法架构
Motus 的核心是 **Mixture-of-Transformer (MoT)** 架构，它集成了三个专家模块：
- **理解专家**：负责感知与语义理解。
- **视频生成专家**：负责未来帧预测与世界建模。
- **动作专家**：负责生成控制指令。

这三个专家通过 **UniDiffuser 风格调度器** 协同工作，支持五种建模模式：
- 世界模型
- 视觉-语言-动作模型
- 逆动力学模型
- 视频生成模型
- 视频-动作联合预测模型

### 潜在动作学习
Motus 利用 **光流** 提取像素级的“增量动作”（delta action），将连续帧间的运动信息编码为潜在动作表示。这一设计使得模型能够从大规模、异构的机器人操作数据中学习通用的动作先验。

### 训练流程
采用 **三阶段训练流水线** 与 **六层数据金字塔**：
1. **阶段一**：在低层数据（如静态图像、文本）上预训练理解与视频生成专家。
2. **阶段二**：引入光流数据，训练潜在动作编码器与动作专家。
3. **阶段三**：在高层数据（如真实机器人操作轨迹）上进行联合微调，优化所有模块的协同能力。

### 实验设置与结果
- **仿真环境**：在标准机器人操作基准上测试，Motus 相比 X-VLA 提升 **15%**，相比 Pi0.5 提升 **45%**。
- **真实场景**：在多种真实机器人操作任务中，Motus 的性能提升范围为 **11% 至 48%**。
- **关键结论**：统一建模所有功能（理解、预测、控制）与先验（视觉、语言、动作）能够显著提升下游机器人任务的表现，验证了碎片化模型整合的有效性。

## Overview
While a general embodied agent must function as a unified system, current methods are built on isolated models for understanding, world modeling, and control. This fragmentation prevents unifying multimodal generative capabilities and hinders learning from large-scale, heterogeneous data. In this paper, we propose Motus, a unified latent action world model that leverages existing general pretrained models and rich, sharable motion information. Motus introduces a Mixture-of-Transformer (MoT) architecture to integrate three experts (i.e., understanding, video generation, and action) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (i.e., world models, vision-language-action models, inverse dynamics models, video generation models, and video-action joint prediction models). Motus further leverages the optical flow to learn latent actions and adopts a recipe with three-phase training pipeline and six-layer data pyramid, thereby extracting pixel-level "delta action" and enabling large-scale action pretraining. Experiments show that Motus achieves superior performance against state-of-the-art methods in both simulation (a +15% improvement over X-VLA and a +45% improvement over Pi0.5) and real-world scenarios(improved by +11~48%), demonstrating unified modeling of all functionalities and priors significantly benefits downstream robotic tasks.

## Overview
While a general embodied agent must function as a unified system, current methods are built on isolated models for understanding, world modeling, and control. This fragmentation prevents unifying multimodal generative capabilities and hinders learning from large-scale, heterogeneous data. In this paper, we propose Motus, a unified latent action world model that leverages existing general pretrained models and rich, sharable motion information. Motus introduces a Mixture-of-Transformer (MoT) architecture to integrate three experts (i.e., understanding, video generation, and action) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (i.e., world models, vision-language-action models, inverse dynamics models, video generation models, and video-action joint prediction models). Motus further leverages the optical flow to learn latent actions and adopts a recipe with three-phase training pipeline and six-layer data pyramid, thereby extracting pixel-level "delta action" and enabling large-scale action pretraining. Experiments show that Motus achieves superior performance against state-of-the-art methods in both simulation (a +15% improvement over X-VLA and a +45% improvement over Pi0.5) and real-world scenarios (improved by +11~48%), demonstrating unified modeling of all functionalities and priors significantly benefits downstream robotic tasks.

## Content
While a general embodied agent must function as a unified system, current methods are built on isolated models for understanding, world modeling, and control. This fragmentation prevents unifying multimodal generative capabilities and hinders learning from large-scale, heterogeneous data. In this paper, we propose Motus, a unified latent action world model that leverages existing general pretrained models and rich, sharable motion information. Motus introduces a Mixture-of-Transformer (MoT) architecture to integrate three experts (i.e., understanding, video generation, and action) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (i.e., world models, vision-language-action models, inverse dynamics models, video generation models, and video-action joint prediction models). Motus further leverages the optical flow to learn latent actions and adopts a recipe with three-phase training pipeline and six-layer data pyramid, thereby extracting pixel-level "delta action" and enabling large-scale action pretraining. Experiments show that Motus achieves superior performance against state-of-the-art methods in both simulation (a +15% improvement over X-VLA and a +45% improvement over Pi0.5) and real-world scenarios (improved by +11~48%), demonstrating unified modeling of all functionalities and priors significantly benefits downstream robotic tasks.

## 参考
- http://arxiv.org/abs/2512.13030v2

## 개요
Motus는 현재 임베디드 에이전트가 모델 파편화로 인해 다중 모드 생성 능력을 통합하지 못하는 문제를 해결하는 것을 목표로 합니다. Mixture-of-Transformer 아키텍처를 채택하여 이해, 비디오 생성, 행동 세 가지 전문가를 통합하고, UniDiffuser 스케줄러를 참고하여 세계 모델, 비전-언어-행동 모델, 역동역학 모델 등 다양한 모델링 모드를 유연하게 전환합니다. 광학 흐름을 통해 픽셀 수준의 "증분 행동"을 추출하여, Motus는 3단계 훈련 프로세스와 6계층 데이터 피라미드를 구축하여 대규모 행동 사전 훈련을 실현합니다. 시뮬레이션 환경에서 Motus는 X-VLA 대비 15%, Pi0.5 대비 45% 향상되었으며, 실제 시나리오에서는 성능 향상 폭이 11%에서 48%에 달합니다.

## 핵심 내용
### 방법 아키텍처
Motus의 핵심은 **Mixture-of-Transformer (MoT)** 아키텍처로, 세 가지 전문가 모듈을 통합합니다:
- **이해 전문가**: 지각 및 의미 이해를 담당합니다.
- **비디오 생성 전문가**: 미래 프레임 예측 및 세계 모델링을 담당합니다.
- **행동 전문가**: 제어 명령 생성을 담당합니다.

이 세 가지 전문가는 **UniDiffuser 스타일 스케줄러**를 통해 협력하며, 다섯 가지 모델링 모드를 지원합니다:
- 세계 모델
- 비전-언어-행동 모델
- 역동역학 모델
- 비디오 생성 모델
- 비디오-행동 공동 예측 모델

### 잠재 행동 학습
Motus는 **광학 흐름**을 활용하여 픽셀 수준의 "증분 행동"(delta action)을 추출하고, 연속 프레임 간의 운동 정보를 잠재 행동 표현으로 인코딩합니다. 이 설계를 통해 모델은 대규모의 이질적인 로봇 조작 데이터에서 일반적인 행동 사전을 학습할 수 있습니다.

### 훈련 프로세스
**3단계 훈련 파이프라인**과 **6계층 데이터 피라미드**를 채택합니다:
1. **1단계**: 저계층 데이터(예: 정적 이미지, 텍스트)에서 이해 및 비디오 생성 전문가를 사전 훈련합니다.
2. **2단계**: 광학 흐름 데이터를 도입하여 잠재 행동 인코더와 행동 전문가를 훈련합니다.
3. **3단계**: 고계층 데이터(예: 실제 로봇 조작 궤적)에서 공동 미세 조정을 수행하여 모든 모듈의 협력 능력을 최적화합니다.

### 실험 설정 및 결과
- **시뮬레이션 환경**: 표준 로봇 조작 벤치마크에서 테스트한 결과, Motus는 X-VLA 대비 **15%**, Pi0.5 대비 **45%** 향상되었습니다.
- **실제 시나리오**: 다양한 실제 로봇 조작 작업에서 Motus의 성능 향상 범위는 **11%에서 48%**입니다.
- **핵심 결론**: 모든 기능(이해, 예측, 제어)과 사전(비전, 언어, 행동)을 통합적으로 모델링하면 하위 로봇 작업의 성능이 크게 향상되어, 파편화된 모델 통합의 효과를 검증합니다.
