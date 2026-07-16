---
$id: ent_paper_lin_physbrain_human_egocentric_dat_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence'
  zh: PhysBrain
  ko: 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence'
summary:
  en: 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence (PhysBrain), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    The Hong Kong University of Science and Technology (Guangzhou), Zhongguancun Academy, Zhongguancun Institute of Artificial
    Intelligence, DeepCybo, Harbin Institute of Technology.'
  zh: 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence (PhysBrain), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    The Hong Kong University of Science and Technology (Guangzhou), Zhongguancun Academy, Zhongguancun Institute of Artificial
    Intelligence, DeepCybo, Harbin Institute of Technology.'
  ko: 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence (PhysBrain), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    The Hong Kong University of Science and Technology (Guangzhou), Zhongguancun Academy, Zhongguancun Institute of Artificial
    Intelligence, DeepCybo, Harbin Institute of Technology.'
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
- physbrain
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.16793v2.
sources:
- id: src_001
  type: paper
  title: 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence (arXiv)'
  url: https://arxiv.org/abs/2512.16793
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: PhysBrain source
  url: https://doi.org/10.48550/arXiv.2512.16793
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robotic generalization relies on physical intelligence: the ability to reason about state changes, contact-rich interactions, and long-horizon planning under egocentric perception and action. Vision Language Models (VLMs) are essential to Vision-Language-Action (VLA) systems, but the reliance on third-person training data creates a viewpoint gap for humanoid robots. Collecting massive robot-centric data is an ideal but impractical solution due to cost and diversity constraints. Conversely, human egocentric videos offer a highly scalable data source with rich interaction context, yet the embodiment mismatch prevents the direct application. To bridge this gap, we propose an Egocentric2Embodiment Translation Pipeline that transforms raw human egocentric videos into multi-level, schema-driven embodiment supervision with enforced evidence grounding and temporal consistency, enabling the construction of the Egocentric2Embodiment dataset (E2E-3M) at scale. An egocentric-aware embodied brain, termed PhysBrain, is obtained by training on the E2E-3M dataset. PhysBrain exhibits substantially improved egocentric understanding, particularly for planning. It provides an egocentric-aware initialization that enables more sample-efficient VLA fine-tuning and higher success rates, demonstrating effective transfer from human egocentric supervision to downstream robot control.

## 核心内容
Robotic generalization relies on physical intelligence: the ability to reason about state changes, contact-rich interactions, and long-horizon planning under egocentric perception and action. Vision Language Models (VLMs) are essential to Vision-Language-Action (VLA) systems, but the reliance on third-person training data creates a viewpoint gap for humanoid robots. Collecting massive robot-centric data is an ideal but impractical solution due to cost and diversity constraints. Conversely, human egocentric videos offer a highly scalable data source with rich interaction context, yet the embodiment mismatch prevents the direct application. To bridge this gap, we propose an Egocentric2Embodiment Translation Pipeline that transforms raw human egocentric videos into multi-level, schema-driven embodiment supervision with enforced evidence grounding and temporal consistency, enabling the construction of the Egocentric2Embodiment dataset (E2E-3M) at scale. An egocentric-aware embodied brain, termed PhysBrain, is obtained by training on the E2E-3M dataset. PhysBrain exhibits substantially improved egocentric understanding, particularly for planning. It provides an egocentric-aware initialization that enables more sample-efficient VLA fine-tuning and higher success rates, demonstrating effective transfer from human egocentric supervision to downstream robot control.

## 参考
- http://arxiv.org/abs/2512.16793v2

## Overview
Robotic generalization relies on physical intelligence: the ability to reason about state changes, contact-rich interactions, and long-horizon planning under egocentric perception and action. Vision Language Models (VLMs) are essential to Vision-Language-Action (VLA) systems, but the reliance on third-person training data creates a viewpoint gap for humanoid robots. Collecting massive robot-centric data is an ideal but impractical solution due to cost and diversity constraints. Conversely, human egocentric videos offer a highly scalable data source with rich interaction context, yet the embodiment mismatch prevents the direct application. To bridge this gap, we propose an Egocentric2Embodiment Translation Pipeline that transforms raw human egocentric videos into multi-level, schema-driven embodiment supervision with enforced evidence grounding and temporal consistency, enabling the construction of the Egocentric2Embodiment dataset (E2E-3M) at scale. An egocentric-aware embodied brain, termed PhysBrain, is obtained by training on the E2E-3M dataset. PhysBrain exhibits substantially improved egocentric understanding, particularly for planning. It provides an egocentric-aware initialization that enables more sample-efficient VLA fine-tuning and higher success rates, demonstrating effective transfer from human egocentric supervision to downstream robot control.

## Content
Robotic generalization relies on physical intelligence: the ability to reason about state changes, contact-rich interactions, and long-horizon planning under egocentric perception and action. Vision Language Models (VLMs) are essential to Vision-Language-Action (VLA) systems, but the reliance on third-person training data creates a viewpoint gap for humanoid robots. Collecting massive robot-centric data is an ideal but impractical solution due to cost and diversity constraints. Conversely, human egocentric videos offer a highly scalable data source with rich interaction context, yet the embodiment mismatch prevents the direct application. To bridge this gap, we propose an Egocentric2Embodiment Translation Pipeline that transforms raw human egocentric videos into multi-level, schema-driven embodiment supervision with enforced evidence grounding and temporal consistency, enabling the construction of the Egocentric2Embodiment dataset (E2E-3M) at scale. An egocentric-aware embodied brain, termed PhysBrain, is obtained by training on the E2E-3M dataset. PhysBrain exhibits substantially improved egocentric understanding, particularly for planning. It provides an egocentric-aware initialization that enables more sample-efficient VLA fine-tuning and higher success rates, demonstrating effective transfer from human egocentric supervision to downstream robot control.

## 개요
로봇 일반화는 물리적 지능, 즉 자기중심적 지각과 행동 하에서 상태 변화, 접촉이 많은 상호작용, 장기적 계획을 추론하는 능력에 의존합니다. Vision Language Models(VLM)은 Vision-Language-Action(VLA) 시스템에 필수적이지만, 제3자 훈련 데이터에 의존함으로써 휴머노이드 로봇에 대한 시점 격차가 발생합니다. 대규모 로봇 중심 데이터를 수집하는 것은 비용과 다양성 제약으로 인해 이상적이지만 비현실적인 해결책입니다. 반면, 인간의 자기중심적 비디오는 풍부한 상호작용 맥락을 가진 확장성이 높은 데이터 소스를 제공하지만, 구현체 불일치로 인해 직접 적용이 불가능합니다. 이러한 격차를 해소하기 위해, 우리는 원시 인간 자기중심적 비디오를 증거 기반 및 시간적 일관성이 강화된 다중 수준의 스키마 기반 구현체 감독으로 변환하는 Egocentric2Embodiment Translation Pipeline을 제안하며, 이를 통해 Egocentric2Embodiment 데이터셋(E2E-3M)을 대규모로 구축할 수 있습니다. E2E-3M 데이터셋으로 훈련된 자기중심적 인식 구현체 두뇌인 PhysBrain은 특히 계획에서 크게 향상된 자기중심적 이해를 보여줍니다. PhysBrain은 자기중심적 인식 초기화를 제공하여 더 샘플 효율적인 VLA 미세 조정과 더 높은 성공률을 가능하게 하며, 인간 자기중심적 감독에서 하위 로봇 제어로의 효과적인 전이를 입증합니다.

## 핵심 내용
로봇 일반화는 물리적 지능, 즉 자기중심적 지각과 행동 하에서 상태 변화, 접촉이 많은 상호작용, 장기적 계획을 추론하는 능력에 의존합니다. Vision Language Models(VLM)은 Vision-Language-Action(VLA) 시스템에 필수적이지만, 제3자 훈련 데이터에 의존함으로써 휴머노이드 로봇에 대한 시점 격차가 발생합니다. 대규모 로봇 중심 데이터를 수집하는 것은 비용과 다양성 제약으로 인해 이상적이지만 비현실적인 해결책입니다. 반면, 인간의 자기중심적 비디오는 풍부한 상호작용 맥락을 가진 확장성이 높은 데이터 소스를 제공하지만, 구현체 불일치로 인해 직접 적용이 불가능합니다. 이러한 격차를 해소하기 위해, 우리는 원시 인간 자기중심적 비디오를 증거 기반 및 시간적 일관성이 강화된 다중 수준의 스키마 기반 구현체 감독으로 변환하는 Egocentric2Embodiment Translation Pipeline을 제안하며, 이를 통해 Egocentric2Embodiment 데이터셋(E2E-3M)을 대규모로 구축할 수 있습니다. E2E-3M 데이터셋으로 훈련된 자기중심적 인식 구현체 두뇌인 PhysBrain은 특히 계획에서 크게 향상된 자기중심적 이해를 보여줍니다. PhysBrain은 자기중심적 인식 초기화를 제공하여 더 샘플 효율적인 VLA 미세 조정과 더 높은 성공률을 가능하게 하며, 인간 자기중심적 감독에서 하위 로봇 제어로의 효과적인 전이를 입증합니다.
