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
  zh: Don't Blind Your VLA (Don't Blind Your VLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Cognitive AI Lab, IAI MIPT.
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.25616v1.
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
The growing success of Vision-Language-Action (VLA) models stems from the promise that pretrained Vision-Language Models (VLMs) can endow agents with transferable world knowledge and vision-language (VL) grounding, laying a foundation for action models with broader generalization. Yet when these VLMs are adapted to the action modality, it remains unclear to what extent their original VL representations and knowledge are preserved. In this work, we conduct a systematic study of representation retention during VLA fine-tuning, showing that naive action fine-tuning leads to degradation of visual representations. To characterize and measure these effects, we probe VLA's hidden representations and analyze attention maps, further, we design a set of targeted tasks and methods that contrast VLA models with their counterpart VLMs, isolating changes in VL capabilities induced by action fine-tuning. We further evaluate a range of strategies for aligning visual representations and introduce a simple yet effective method that mitigates degradation and yields improved generalization to out-of-distribution (OOD) scenarios. Taken together, our analysis clarifies the trade-off between action fine-tuning and the degradation of VL representations and highlights practical approaches to recover inherited VL capabilities. Code is publicly available: https://blind-vla-paper.github.io

## 核心内容
The growing success of Vision-Language-Action (VLA) models stems from the promise that pretrained Vision-Language Models (VLMs) can endow agents with transferable world knowledge and vision-language (VL) grounding, laying a foundation for action models with broader generalization. Yet when these VLMs are adapted to the action modality, it remains unclear to what extent their original VL representations and knowledge are preserved. In this work, we conduct a systematic study of representation retention during VLA fine-tuning, showing that naive action fine-tuning leads to degradation of visual representations. To characterize and measure these effects, we probe VLA's hidden representations and analyze attention maps, further, we design a set of targeted tasks and methods that contrast VLA models with their counterpart VLMs, isolating changes in VL capabilities induced by action fine-tuning. We further evaluate a range of strategies for aligning visual representations and introduce a simple yet effective method that mitigates degradation and yields improved generalization to out-of-distribution (OOD) scenarios. Taken together, our analysis clarifies the trade-off between action fine-tuning and the degradation of VL representations and highlights practical approaches to recover inherited VL capabilities. Code is publicly available: https://blind-vla-paper.github.io

## 参考
- http://arxiv.org/abs/2510.25616v1

## Overview
The growing success of Vision-Language-Action (VLA) models stems from the promise that pretrained Vision-Language Models (VLMs) can endow agents with transferable world knowledge and vision-language (VL) grounding, laying a foundation for action models with broader generalization. Yet when these VLMs are adapted to the action modality, it remains unclear to what extent their original VL representations and knowledge are preserved. In this work, we conduct a systematic study of representation retention during VLA fine-tuning, showing that naive action fine-tuning leads to degradation of visual representations. To characterize and measure these effects, we probe VLA's hidden representations and analyze attention maps, further, we design a set of targeted tasks and methods that contrast VLA models with their counterpart VLMs, isolating changes in VL capabilities induced by action fine-tuning. We further evaluate a range of strategies for aligning visual representations and introduce a simple yet effective method that mitigates degradation and yields improved generalization to out-of-distribution (OOD) scenarios. Taken together, our analysis clarifies the trade-off between action fine-tuning and the degradation of VL representations and highlights practical approaches to recover inherited VL capabilities. Code is publicly available: https://blind-vla-paper.github.io

## Content
The growing success of Vision-Language-Action (VLA) models stems from the promise that pretrained Vision-Language Models (VLMs) can endow agents with transferable world knowledge and vision-language (VL) grounding, laying a foundation for action models with broader generalization. Yet when these VLMs are adapted to the action modality, it remains unclear to what extent their original VL representations and knowledge are preserved. In this work, we conduct a systematic study of representation retention during VLA fine-tuning, showing that naive action fine-tuning leads to degradation of visual representations. To characterize and measure these effects, we probe VLA's hidden representations and analyze attention maps, further, we design a set of targeted tasks and methods that contrast VLA models with their counterpart VLMs, isolating changes in VL capabilities induced by action fine-tuning. We further evaluate a range of strategies for aligning visual representations and introduce a simple yet effective method that mitigates degradation and yields improved generalization to out-of-distribution (OOD) scenarios. Taken together, our analysis clarifies the trade-off between action fine-tuning and the degradation of VL representations and highlights practical approaches to recover inherited VL capabilities. Code is publicly available: https://blind-vla-paper.github.io

## 개요
Vision-Language-Action(VLA) 모델의 성장은 사전 훈련된 Vision-Language Model(VLM)이 에이전트에 전이 가능한 세계 지식과 시각-언어(VL) 기반을 부여하여 더 넓은 일반화를 갖춘 행동 모델의 기반을 마련할 수 있다는 가능성에서 비롯됩니다. 그러나 이러한 VLM이 행동 모달리티에 적응될 때, 원래의 VL 표현과 지식이 어느 정도 보존되는지는 여전히 불분명합니다. 본 연구에서는 VLA 미세 조정 중 표현 보존에 대한 체계적인 연구를 수행하여, 단순한 행동 미세 조정이 시각 표현의 저하를 초래함을 보여줍니다. 이러한 효과를 특성화하고 측정하기 위해 VLA의 은닉 표현을 조사하고 어텐션 맵을 분석하며, 나아가 VLA 모델과 해당 VLM을 대조하는 일련의 목표 작업과 방법을 설계하여 행동 미세 조정으로 인한 VL 능력 변화를 분리합니다. 또한 시각 표현을 정렬하기 위한 다양한 전략을 평가하고, 저하를 완화하고 분포 외(OOD) 시나리오에 대한 일반화를 개선하는 간단하면서도 효과적인 방법을 소개합니다. 종합적으로, 본 분석은 행동 미세 조정과 VL 표현 저하 간의 상충 관계를 명확히 하고, 상속된 VL 능력을 회복하기 위한 실용적인 접근법을 강조합니다. 코드는 공개적으로 이용 가능합니다: https://blind-vla-paper.github.io

## 핵심 내용
Vision-Language-Action(VLA) 모델의 성장은 사전 훈련된 Vision-Language Model(VLM)이 에이전트에 전이 가능한 세계 지식과 시각-언어(VL) 기반을 부여하여 더 넓은 일반화를 갖춘 행동 모델의 기반을 마련할 수 있다는 가능성에서 비롯됩니다. 그러나 이러한 VLM이 행동 모달리티에 적응될 때, 원래의 VL 표현과 지식이 어느 정도 보존되는지는 여전히 불분명합니다. 본 연구에서는 VLA 미세 조정 중 표현 보존에 대한 체계적인 연구를 수행하여, 단순한 행동 미세 조정이 시각 표현의 저하를 초래함을 보여줍니다. 이러한 효과를 특성화하고 측정하기 위해 VLA의 은닉 표현을 조사하고 어텐션 맵을 분석하며, 나아가 VLA 모델과 해당 VLM을 대조하는 일련의 목표 작업과 방법을 설계하여 행동 미세 조정으로 인한 VL 능력 변화를 분리합니다. 또한 시각 표현을 정렬하기 위한 다양한 전략을 평가하고, 저하를 완화하고 분포 외(OOD) 시나리오에 대한 일반화를 개선하는 간단하면서도 효과적인 방법을 소개합니다. 종합적으로, 본 분석은 행동 미세 조정과 VL 표현 저하 간의 상충 관계를 명확히 하고, 상속된 VL 능력을 회복하기 위한 실용적인 접근법을 강조합니다. 코드는 공개적으로 이용 가능합니다: https://blind-vla-paper.github.io
