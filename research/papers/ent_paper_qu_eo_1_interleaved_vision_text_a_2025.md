---
$id: ent_paper_qu_eo_1_interleaved_vision_text_a_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EO-1: Interleaved Vision-Text-Action Pretraining for General Robot Control'
  zh: EO-1
  ko: 'EO-1: Interleaved Vision-Text-Action Pretraining for General Robot Control'
summary:
  en: 'EO-1: Interleaved Vision-Text-Action Pretraining for General Robot Control (EO-1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Harbin Institute of Technology (Shenzhen).'
  zh: EO-1 是哈尔滨工业大学（深圳）于 2025 年提出的大型视觉-语言-动作模型，旨在实现通用机器人操控。其核心贡献在于通过交错式视觉-文本-动作预训练，在统一架构中融合多模态输入与动作生成，并配套发布了包含 150 万样本的高质量数据集
    EO-Data1.5M。
  ko: 'EO-1: Interleaved Vision-Text-Action Pretraining for General Robot Control (EO-1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Harbin Institute of Technology (Shenzhen).'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- eo_1
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.21112v5. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'EO-1: Interleaved Vision-Text-Action Pretraining for General Robot Control (arXiv)'
  url: https://arxiv.org/abs/2508.21112
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EO-1 source
  url: https://doi.org/10.48550/arXiv.2508.21112
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
EO-1 模型由 EO-Robotics 项目推出，其设计基于两大支柱：一是能够无差别处理图像、文本、视频和动作的统一架构，二是强调交错式视觉-文本-动作理解的大规模数据集 EO-Data1.5M。该模型通过自回归解码与流匹配去噪的协同训练，实现了无缝的机器人动作生成与多模态具身推理。实验表明，交错式学习范式在多种长时程、灵巧操控任务中展现出强大的开放世界理解与泛化能力。

## 核心内容
### 模型架构
- EO-1 采用统一架构，可无差别处理图像、文本、视频和动作四种模态输入。
- 该架构通过自回归解码（auto-regressive decoding）与流匹配去噪（flow matching denoising）的协同训练，在 EO-Data1.5M 数据集上实现端到端学习。

### 数据集 EO-Data1.5M
- 包含超过 150 万样本，重点强调交错式视觉-文本-动作理解（interleaved vision-text-action comprehension）。
- 数据构造策略旨在提升模型在开放世界中的推理与泛化能力。

### 实验设置与结果
- 在多种长时程（long-horizon）、灵巧操控（dexterous manipulation）任务上进行验证，涵盖多个具身形态（multiple embodiments）。
- 实验证明交错式视觉-文本-动作学习能有效提升开放世界理解与泛化性能。

### 结论
- EO-1 通过交错式预训练范式，在通用机器人控制中实现了优于现有 VLA 模型的多模态推理与动作生成能力。
- 项目页面提供更多细节：https://eo-robotics.ai/eo-1

## Overview
The human ability to seamlessly perform multimodal reasoning and physical interaction in the open world is a core goal for general purpose embodied intelligent systems. Recent vision-language-action (VLA) models, which are co-trained on large-scale robot and visual-text data, have demonstrated notable progress in general robot control. However, they still fail to achieve human-level flexibility in interleaved reasoning and interaction. In this work, we introduce EO-Robotics, consists of EO-1 model and EO-Data1.5M dataset. EO-1 is a unified embodied foundation model that achieves superior performance in multimodal embodied reasoning and robot control through interleaved vision-text-action pre-training. The development of EO-1 is based on two key pillars: (i) a unified architecture that processes multimodal inputs indiscriminately (image, text, video, and action), and (ii) a massive, high-quality multimodal embodied reasoning dataset, EO-Data1.5M, which contains over 1.5 million samples with emphasis on interleaved vision-text-action comprehension. EO-1 is trained through synergies between auto-regressive decoding and flow matching denoising on EO-Data1.5M, enabling seamless robot action generation and multimodal embodied reasoning. Extensive experiments demonstrate the effectiveness of interleaved vision-text-action learning for open-world understanding and generalization, validated through a variety of long-horizon, dexterous manipulation tasks across multiple embodiments. This paper details the architecture of EO-1, the data construction strategy of EO-Data1.5M, and the training methodology, offering valuable insights for developing advanced embodied foundation models. Project Page: https://eo-robotics.ai/eo-1.

## 개요
인간이 개방된 세계에서 다중 모드 추론과 물리적 상호작용을 원활하게 수행하는 능력은 범용 임베디드 지능형 시스템의 핵심 목표입니다. 최근 대규모 로봇 및 시각-텍스트 데이터로 공동 학습된 VLA(Vision-Language-Action) 모델은 일반 로봇 제어에서 주목할 만한 진전을 보여주었습니다. 그러나 여전히 교차된 추론과 상호작용에서 인간 수준의 유연성을 달성하지 못하고 있습니다. 본 연구에서는 EO-1 모델과 EO-Data1.5M 데이터셋으로 구성된 EO-Robotics를 소개합니다. EO-1은 교차된 시각-텍스트-행동 사전 학습을 통해 다중 모드 임베디드 추론 및 로봇 제어에서 뛰어난 성능을 달성하는 통합 임베디드 기반 모델입니다. EO-1의 개발은 두 가지 핵심 기반에 의존합니다: (i) 다중 모드 입력(이미지, 텍스트, 비디오, 행동)을 차별 없이 처리하는 통합 아키텍처, (ii) 교차된 시각-텍스트-행동 이해에 중점을 둔 150만 개 이상의 샘플을 포함하는 대규모 고품질 다중 모드 임베디드 추론 데이터셋 EO-Data1.5M입니다. EO-1은 EO-Data1.5M에서 자기회귀 디코딩과 흐름 매칭 잡음 제거 간의 시너지를 통해 학습되어 원활한 로봇 행동 생성 및 다중 모드 임베디드 추론을 가능하게 합니다. 광범위한 실험을 통해 교차된 시각-텍스트-행동 학습이 개방형 세계 이해 및 일반화에 효과적임을 입증했으며, 이는 다양한 임베디드 환경에서의 장기적이고 정밀한 조작 작업을 통해 검증되었습니다. 본 논문은 EO-1의 아키텍처, EO-Data1.5M의 데이터 구축 전략, 그리고 훈련 방법론을 상세히 설명하여 고급 임베디드 기반 모델 개발에 귀중한 통찰력을 제공합니다. 프로젝트 페이지: https://eo-robotics.ai/eo-1.

## 핵심 내용
인간이 개방된 세계에서 다중 모드 추론과 물리적 상호작용을 원활하게 수행하는 능력은 범용 임베디드 지능형 시스템의 핵심 목표입니다. 최근 대규모 로봇 및 시각-텍스트 데이터로 공동 학습된 VLA(Vision-Language-Action) 모델은 일반 로봇 제어에서 주목할 만한 진전을 보여주었습니다. 그러나 여전히 교차된 추론과 상호작용에서 인간 수준의 유연성을 달성하지 못하고 있습니다. 본 연구에서는 EO-1 모델과 EO-Data1.5M 데이터셋으로 구성된 EO-Robotics를 소개합니다. EO-1은 교차된 시각-텍스트-행동 사전 학습을 통해 다중 모드 임베디드 추론 및 로봇 제어에서 뛰어난 성능을 달성하는 통합 임베디드 기반 모델입니다. EO-1의 개발은 두 가지 핵심 기반에 의존합니다: (i) 다중 모드 입력(이미지, 텍스트, 비디오, 행동)을 차별 없이 처리하는 통합 아키텍처, (ii) 교차된 시각-텍스트-행동 이해에 중점을 둔 150만 개 이상의 샘플을 포함하는 대규모 고품질 다중 모드 임베디드 추론 데이터셋 EO-Data1.5M입니다. EO-1은 EO-Data1.5M에서 자기회귀 디코딩과 흐름 매칭 잡음 제거 간의 시너지를 통해 학습되어 원활한 로봇 행동 생성 및 다중 모드 임베디드 추론을 가능하게 합니다. 광범위한 실험을 통해 교차된 시각-텍스트-행동 학습이 개방형 세계 이해 및 일반화에 효과적임을 입증했으며, 이는 다양한 임베디드 환경에서의 장기적이고 정밀한 조작 작업을 통해 검증되었습니다. 본 논문은 EO-1의 아키텍처, EO-Data1.5M의 데이터 구축 전략, 그리고 훈련 방법론을 상세히 설명하여 고급 임베디드 기반 모델 개발에 귀중한 통찰력을 제공합니다. 프로젝트 페이지: https://eo-robotics.ai/eo-1.

## 参考
- http://arxiv.org/abs/2508.21112v5
