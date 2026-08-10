---
$id: ent_paper_zhang_coc_vla_delving_into_adversari_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model'
  zh: CoC-VLA
  ko: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model'
summary:
  en: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model (CoC-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University,
    National University of Singapore, University of Science and Technology of China, and published at NIPS25.'
  zh: CoC-VLA 是 2025 年由兰州大学、新加坡国立大学和中国科学技术大学联合提出的视觉-语言-动作大模型，发表于 NIPS25。其核心贡献在于提出一种 VLM 引导的端到端对抗迁移框架，将长尾场景处理能力从仿真环境迁移至真实部署。关键创新包括基于因果链的视觉-语言模型（CoC
    VLM）架构和对抗性判别器训练策略。
  ko: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model (CoC-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University,
    National University of Singapore, University of Science and Technology of China, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- coc_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19914v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (620 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model (arXiv)'
  url: https://arxiv.org/abs/2511.19914
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CoC-VLA source
  url: https://doi.org/10.48550/arXiv.2511.19914
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有自动驾驶方法通常仅依赖真实数据或仿真数据，难以有效融合两者优势。CoC-VLA 通过教师-学生 VLM 模型与对抗判别器协同工作，教师模型在仿真数据上预训练，学生模型在真实数据上预训练，判别器则通过对抗训练促使学生模型习得教师模型的长尾场景处理能力。该框架采用端到端文本适配器整合时序信息，并支持链式推理以理解复杂驾驶逻辑。

## 核心内容
### 方法架构
- **整体框架**：包含教师 VLM 模型、学生 VLM 模型和判别器三部分。教师模型在仿真数据集上预训练，学生模型在真实数据集上预训练，判别器通过对抗训练实现能力迁移。
- **基础架构**：教师和学生模型共享名为 Chain-of-Causality Visual-Language Model (CoC VLM) 的基座架构，该架构通过端到端文本适配器整合时序信息，支持链式推理以推断复杂驾驶逻辑。

### 实验设置
- **数据来源**：教师模型使用仿真数据（针对罕见或困难场景），学生模型使用真实数据（适合工业部署）。
- **训练策略**：采用新型反向传播策略，通过对抗性训练使判别器促进学生模型从仿真环境向真实环境迁移长尾处理能力。

### 关键结论
- 现有方法通常仅依赖单一数据源，CoC-VLA 通过对抗迁移有效融合仿真与真实数据的互补优势。
- 该框架在长尾场景（如细微人类行为、交通事故、违规驾驶模式）中展现出更强的推理与可解释性。

## Overview
Autonomous driving represents a prominent application of artificial intelligence. Recent approaches have shifted from focusing solely on common scenarios to addressing complex, long-tail situations such as subtle human behaviors, traffic accidents, and non-compliant driving patterns. Given the demonstrated capabilities of large language models (LLMs) in understanding visual and natural language inputs and following instructions, recent methods have integrated LLMs into autonomous driving systems to enhance reasoning, interpretability, and performance across diverse scenarios. However, existing methods typically rely either on real-world data, which is suitable for industrial deployment, or on simulation data tailored to rare or hard case scenarios. Few approaches effectively integrate the complementary advantages of both data sources. To address this limitation, we propose a novel VLM-guided, end-to-end adversarial transfer framework for autonomous driving that transfers long-tail handling capabilities from simulation to real-world deployment, named CoC-VLA. The framework comprises a teacher VLM model, a student VLM model, and a discriminator. Both the teacher and student VLM models utilize a shared base architecture, termed the Chain-of-Causality Visual-Language Model (CoC VLM), which integrates temporal information via an end-to-end text adapter. This architecture supports chain-of-thought reasoning to infer complex driving logic. The teacher and student VLM models are pre-trained separately on simulated and real-world datasets. The discriminator is trained adversarially to facilitate the transfer of long-tail handling capabilities from simulated to real-world environments by the student VLM model, using a novel backpropagation strategy.

## 参考
- http://arxiv.org/abs/2511.19914v1

## 개요
기존 자율주행 방법은 일반적으로 실제 데이터나 시뮬레이션 데이터 중 하나에만 의존하여, 두 데이터의 장점을 효과적으로 융합하기 어렵습니다. CoC-VLA는 교사-학생 VLM 모델과 적대적 판별기가 협력하여 작동하며, 교사 모델은 시뮬레이션 데이터로 사전 학습되고, 학생 모델은 실제 데이터로 사전 학습되며, 판별기는 적대적 훈련을 통해 학생 모델이 교사 모델의 긴 꼬리(long-tail) 시나리오 처리 능력을 습득하도록 유도합니다. 이 프레임워크는 종단 간 텍스트 어댑터를 사용하여 시계열 정보를 통합하고, 체인 추론을 지원하여 복잡한 운전 논리를 이해합니다.

## 핵심 내용
### 방법 아키텍처
- **전체 프레임워크**: 교사 VLM 모델, 학생 VLM 모델, 판별기의 세 부분으로 구성됩니다. 교사 모델은 시뮬레이션 데이터셋으로 사전 학습되고, 학생 모델은 실제 데이터셋으로 사전 학습되며, 판별기는 적대적 훈련을 통해 능력 전이를 구현합니다.
- **기본 아키텍처**: 교사와 학생 모델은 Chain-of-Causality Visual-Language Model (CoC VLM)이라는 기본 아키텍처를 공유하며, 이 아키텍처는 종단 간 텍스트 어댑터를 통해 시계열 정보를 통합하고, 체인 추론을 지원하여 복잡한 운전 논리를 추론합니다.

### 실험 설정
- **데이터 출처**: 교사 모델은 시뮬레이션 데이터(드물거나 어려운 시나리오 대상)를 사용하고, 학생 모델은 실제 데이터(산업 배포에 적합)를 사용합니다.
- **훈련 전략**: 새로운 역전파 전략을 채택하여, 적대적 훈련을 통해 판별기가 학생 모델이 시뮬레이션 환경에서 실제 환경으로 긴 꼬리 처리 능력을 전이하도록 촉진합니다.

### 핵심 결론
- 기존 방법은 일반적으로 단일 데이터 소스에만 의존하지만, CoC-VLA는 적대적 전이를 통해 시뮬레이션과 실제 데이터의 상호 보완적 장점을 효과적으로 융합합니다.
- 이 프레임워크는 긴 꼬리 시나리오(예: 미세한 인간 행동, 교통 사고, 위반 운전 패턴)에서 더 강력한 추론 및 설명 가능성을 보여줍니다.
