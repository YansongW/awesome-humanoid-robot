---
$id: ent_paper_kurenkov_dont_blind_your_vla_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Don't Blind Your VLA
  zh: Don't Blind Your VLA
  ko: Don't Blind Your VLA
summary:
  en: Don't Blind Your VLA (Don't Blind Your VLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Cognitive AI Lab, IAI MIPT.
  zh: Don't Blind Your VLA 是 2025 年由 Cognitive AI Lab, IAI MIPT 提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于系统性地揭示了 VLA 模型在动作微调过程中视觉表征退化的现象，并提出了一种简单有效的缓解方法，从而提升模型在分布外场景下的泛化能力。
  ko: Don't Blind Your VLA (Don't Blind Your VLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Cognitive AI Lab, IAI MIPT.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dont_blind_your_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.25616v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Don't Blind Your VLA (arXiv)
  url: https://arxiv.org/abs/2510.25616
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Don't Blind Your VLA source
  url: https://doi.org/10.48550/arXiv.2510.25616
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究指出，尽管预训练的视觉-语言模型（VLM）能为机器人赋予可迁移的世界知识与视觉-语言基础，但在将其适配到动作模态时，原始表征会因动作微调而退化。作者通过探测隐藏表征与分析注意力图，设计了一系列对比任务来量化这种退化，并评估了多种对齐策略。最终提出的方法能有效抑制退化，并显著改善模型在未见过的场景中的表现。

## 核心内容
### 研究背景与问题
Vision-Language-Action (VLA) 模型依赖预训练的 Vision-Language Models (VLMs) 提供可迁移的世界知识与视觉-语言基础。然而，当 VLM 被微调以适应动作模态时，其原始的视觉-语言表征与知识是否被保留尚不明确。

### 核心发现
- **表征退化**：通过系统研究，作者发现**朴素的动作微调会导致视觉表征显著退化**。
- **量化方法**：通过探测 VLA 的隐藏表征、分析注意力图，并设计一组对比任务（将 VLA 模型与其对应的 VLM 进行对比），作者隔离并量化了动作微调引起的视觉-语言能力变化。

### 解决方案
- **策略评估**：作者评估了多种视觉表征对齐策略。
- **有效方法**：提出一种**简单且有效的方法**，能够缓解表征退化，并提升模型在**分布外（OOD）场景**下的泛化能力。

### 结论
该工作阐明了动作微调与视觉-语言表征退化之间的权衡关系，并提供了恢复继承的视觉-语言能力的实用方法。代码已开源：https://blind-vla-paper.github.io

## Overview
The growing success of Vision-Language-Action (VLA) models stems from the promise that pretrained Vision-Language Models (VLMs) can endow agents with transferable world knowledge and vision-language (VL) grounding, laying a foundation for action models with broader generalization. Yet when these VLMs are adapted to the action modality, it remains unclear to what extent their original VL representations and knowledge are preserved. In this work, we conduct a systematic study of representation retention during VLA fine-tuning, showing that naive action fine-tuning leads to degradation of visual representations. To characterize and measure these effects, we probe VLA's hidden representations and analyze attention maps, further, we design a set of targeted tasks and methods that contrast VLA models with their counterpart VLMs, isolating changes in VL capabilities induced by action fine-tuning. We further evaluate a range of strategies for aligning visual representations and introduce a simple yet effective method that mitigates degradation and yields improved generalization to out-of-distribution (OOD) scenarios. Taken together, our analysis clarifies the trade-off between action fine-tuning and the degradation of VL representations and highlights practical approaches to recover inherited VL capabilities. Code is publicly available: https://blind-vla-paper.github.io

## 개요
Vision-Language-Action(VLA) 모델의 성장은 사전 훈련된 Vision-Language Model(VLM)이 에이전트에 전이 가능한 세계 지식과 시각-언어(VL) 기반을 부여하여 더 넓은 일반화를 갖춘 행동 모델의 기반을 마련할 수 있다는 가능성에서 비롯됩니다. 그러나 이러한 VLM이 행동 모달리티에 적응될 때, 원래의 VL 표현과 지식이 어느 정도 보존되는지는 여전히 불분명합니다. 본 연구에서는 VLA 미세 조정 중 표현 보존에 대한 체계적인 연구를 수행하여, 단순한 행동 미세 조정이 시각 표현의 저하를 초래함을 보여줍니다. 이러한 효과를 특성화하고 측정하기 위해 VLA의 은닉 표현을 조사하고 어텐션 맵을 분석하며, 나아가 VLA 모델과 해당 VLM을 대조하는 일련의 목표 작업과 방법을 설계하여 행동 미세 조정으로 인한 VL 능력 변화를 분리합니다. 또한 시각 표현을 정렬하기 위한 다양한 전략을 평가하고, 저하를 완화하고 분포 외(OOD) 시나리오에 대한 일반화를 개선하는 간단하면서도 효과적인 방법을 소개합니다. 종합적으로, 본 분석은 행동 미세 조정과 VL 표현 저하 간의 상충 관계를 명확히 하고, 상속된 VL 능력을 회복하기 위한 실용적인 접근법을 강조합니다. 코드는 공개적으로 이용 가능합니다: https://blind-vla-paper.github.io

## 핵심 내용
Vision-Language-Action(VLA) 모델의 성장은 사전 훈련된 Vision-Language Model(VLM)이 에이전트에 전이 가능한 세계 지식과 시각-언어(VL) 기반을 부여하여 더 넓은 일반화를 갖춘 행동 모델의 기반을 마련할 수 있다는 가능성에서 비롯됩니다. 그러나 이러한 VLM이 행동 모달리티에 적응될 때, 원래의 VL 표현과 지식이 어느 정도 보존되는지는 여전히 불분명합니다. 본 연구에서는 VLA 미세 조정 중 표현 보존에 대한 체계적인 연구를 수행하여, 단순한 행동 미세 조정이 시각 표현의 저하를 초래함을 보여줍니다. 이러한 효과를 특성화하고 측정하기 위해 VLA의 은닉 표현을 조사하고 어텐션 맵을 분석하며, 나아가 VLA 모델과 해당 VLM을 대조하는 일련의 목표 작업과 방법을 설계하여 행동 미세 조정으로 인한 VL 능력 변화를 분리합니다. 또한 시각 표현을 정렬하기 위한 다양한 전략을 평가하고, 저하를 완화하고 분포 외(OOD) 시나리오에 대한 일반화를 개선하는 간단하면서도 효과적인 방법을 소개합니다. 종합적으로, 본 분석은 행동 미세 조정과 VL 표현 저하 간의 상충 관계를 명확히 하고, 상속된 VL 능력을 회복하기 위한 실용적인 접근법을 강조합니다. 코드는 공개적으로 이용 가능합니다: https://blind-vla-paper.github.io

## 参考
- http://arxiv.org/abs/2510.25616v1
