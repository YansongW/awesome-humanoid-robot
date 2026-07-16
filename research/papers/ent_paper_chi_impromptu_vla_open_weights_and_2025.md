---
$id: ent_paper_chi_impromptu_vla_open_weights_and_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models'
  zh: Impromptu VLA
  ko: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models'
summary:
  en: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (Impromptu VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AIR, Tsinghua University, Bosch Research, IIIS, Tsinghua
    University, and published at NIPS25.'
  zh: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (Impromptu VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AIR, Tsinghua University, Bosch Research, IIIS, Tsinghua
    University, and published at NIPS25.'
  ko: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (Impromptu VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AIR, Tsinghua University, Bosch Research, IIIS, Tsinghua
    University, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- impromptu_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.23757v1.
sources:
- id: src_001
  type: paper
  title: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2505.23757
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Impromptu VLA source
  url: https://doi.org/10.48550/arXiv.2505.23757
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models for autonomous driving show promise but falter in unstructured corner case scenarios, largely due to a scarcity of targeted benchmarks. To address this, we introduce Impromptu VLA. Our core contribution is the Impromptu VLA Dataset: over 80,000 meticulously curated video clips, distilled from over 2M source clips sourced from 8 open-source large-scale datasets. This dataset is built upon our novel taxonomy of four challenging unstructured categories and features rich, planning-oriented question-answering annotations and action trajectories. Crucially, experiments demonstrate that VLAs trained with our dataset achieve substantial performance gains on established benchmarks--improving closed-loop NeuroNCAP scores and collision rates, and reaching near state-of-the-art L2 accuracy in open-loop nuScenes trajectory prediction. Furthermore, our Q&A suite serves as an effective diagnostic, revealing clear VLM improvements in perception, prediction, and planning. Our code, data and models are available at https://github.com/ahydchh/Impromptu-VLA.

## 核心内容
Vision-Language-Action (VLA) models for autonomous driving show promise but falter in unstructured corner case scenarios, largely due to a scarcity of targeted benchmarks. To address this, we introduce Impromptu VLA. Our core contribution is the Impromptu VLA Dataset: over 80,000 meticulously curated video clips, distilled from over 2M source clips sourced from 8 open-source large-scale datasets. This dataset is built upon our novel taxonomy of four challenging unstructured categories and features rich, planning-oriented question-answering annotations and action trajectories. Crucially, experiments demonstrate that VLAs trained with our dataset achieve substantial performance gains on established benchmarks--improving closed-loop NeuroNCAP scores and collision rates, and reaching near state-of-the-art L2 accuracy in open-loop nuScenes trajectory prediction. Furthermore, our Q&A suite serves as an effective diagnostic, revealing clear VLM improvements in perception, prediction, and planning. Our code, data and models are available at https://github.com/ahydchh/Impromptu-VLA.

## 参考
- http://arxiv.org/abs/2505.23757v1

## Overview
Vision-Language-Action (VLA) models for autonomous driving show promise but falter in unstructured corner case scenarios, largely due to a scarcity of targeted benchmarks. To address this, we introduce Impromptu VLA. Our core contribution is the Impromptu VLA Dataset: over 80,000 meticulously curated video clips, distilled from over 2M source clips sourced from 8 open-source large-scale datasets. This dataset is built upon our novel taxonomy of four challenging unstructured categories and features rich, planning-oriented question-answering annotations and action trajectories. Crucially, experiments demonstrate that VLAs trained with our dataset achieve substantial performance gains on established benchmarks--improving closed-loop NeuroNCAP scores and collision rates, and reaching near state-of-the-art L2 accuracy in open-loop nuScenes trajectory prediction. Furthermore, our Q&A suite serves as an effective diagnostic, revealing clear VLM improvements in perception, prediction, and planning. Our code, data and models are available at https://github.com/ahydchh/Impromptu-VLA.

## Content
Vision-Language-Action (VLA) models for autonomous driving show promise but falter in unstructured corner case scenarios, largely due to a scarcity of targeted benchmarks. To address this, we introduce Impromptu VLA. Our core contribution is the Impromptu VLA Dataset: over 80,000 meticulously curated video clips, distilled from over 2M source clips sourced from 8 open-source large-scale datasets. This dataset is built upon our novel taxonomy of four challenging unstructured categories and features rich, planning-oriented question-answering annotations and action trajectories. Crucially, experiments demonstrate that VLAs trained with our dataset achieve substantial performance gains on established benchmarks--improving closed-loop NeuroNCAP scores and collision rates, and reaching near state-of-the-art L2 accuracy in open-loop nuScenes trajectory prediction. Furthermore, our Q&A suite serves as an effective diagnostic, revealing clear VLM improvements in perception, prediction, and planning. Our code, data and models are available at https://github.com/ahydchh/Impromptu-VLA.

## 개요
자율주행을 위한 Vision-Language-Action (VLA) 모델은 가능성을 보여주지만, 비정형 코너 케이스 시나리오에서는 주로 타겟 벤치마크 부족으로 인해 성능이 저하됩니다. 이를 해결하기 위해 우리는 Impromptu VLA를 소개합니다. 핵심 기여는 Impromptu VLA 데이터셋입니다: 8개의 오픈소스 대규모 데이터셋에서 추출한 200만 개 이상의 소스 클립에서 정제된 80,000개 이상의 정성적으로 선별된 비디오 클립으로 구성됩니다. 이 데이터셋은 네 가지 도전적인 비정형 카테고리에 대한 새로운 분류 체계를 기반으로 구축되었으며, 풍부한 계획 중심의 질문-응답 주석과 행동 궤적을 특징으로 합니다. 결정적으로, 실험 결과 우리 데이터셋으로 훈련된 VLA는 기존 벤치마크에서 상당한 성능 향상을 달성하여 폐루프 NeuroNCAP 점수와 충돌률을 개선하고, 개루프 nuScenes 궤적 예측에서 최첨단에 가까운 L2 정확도에 도달했습니다. 또한, Q&A 세트는 효과적인 진단 도구로 작용하여 인식, 예측 및 계획에서 명확한 VLM 개선을 드러냅니다. 코드, 데이터 및 모델은 https://github.com/ahydchh/Impromptu-VLA에서 확인할 수 있습니다.

## 핵심 내용
자율주행을 위한 Vision-Language-Action (VLA) 모델은 가능성을 보여주지만, 비정형 코너 케이스 시나리오에서는 주로 타겟 벤치마크 부족으로 인해 성능이 저하됩니다. 이를 해결하기 위해 우리는 Impromptu VLA를 소개합니다. 핵심 기여는 Impromptu VLA 데이터셋입니다: 8개의 오픈소스 대규모 데이터셋에서 추출한 200만 개 이상의 소스 클립에서 정제된 80,000개 이상의 정성적으로 선별된 비디오 클립으로 구성됩니다. 이 데이터셋은 네 가지 도전적인 비정형 카테고리에 대한 새로운 분류 체계를 기반으로 구축되었으며, 풍부한 계획 중심의 질문-응답 주석과 행동 궤적을 특징으로 합니다. 결정적으로, 실험 결과 우리 데이터셋으로 훈련된 VLA는 기존 벤치마크에서 상당한 성능 향상을 달성하여 폐루프 NeuroNCAP 점수와 충돌률을 개선하고, 개루프 nuScenes 궤적 예측에서 최첨단에 가까운 L2 정확도에 도달했습니다. 또한, Q&A 세트는 효과적인 진단 도구로 작용하여 인식, 예측 및 계획에서 명확한 VLM 개선을 드러냅니다. 코드, 데이터 및 모델은 https://github.com/ahydchh/Impromptu-VLA에서 확인할 수 있습니다.
