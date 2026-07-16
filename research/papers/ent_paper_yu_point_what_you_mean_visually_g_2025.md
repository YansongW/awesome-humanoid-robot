---
$id: ent_paper_yu_point_what_you_mean_visually_g_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Point What You Mean: Visually Grounded Instruction Policy'
  zh: Point-VLA
  ko: 'Point What You Mean: Visually Grounded Instruction Policy'
summary:
  en: 'Point What You Mean: Visually Grounded Instruction Policy (Point-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Tongji University, Shanghai Jiao Tong University, Spirit AI, Tsinghua University.'
  zh: 'Point What You Mean: Visually Grounded Instruction Policy (Point-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Tongji University, Shanghai Jiao Tong University, Spirit AI, Tsinghua University.'
  ko: 'Point What You Mean: Visually Grounded Instruction Policy (Point-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Tongji University, Shanghai Jiao Tong University, Spirit AI, Tsinghua University.'
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
- point_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.18933v2.
sources:
- id: src_001
  type: paper
  title: 'Point What You Mean: Visually Grounded Instruction Policy (arXiv)'
  url: https://arxiv.org/abs/2512.18933
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Point-VLA source
  url: https://doi.org/10.48550/arXiv.2512.18933
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models align vision and language with embodied control, but their object referring ability remains limited when relying solely on text prompt, especially in cluttered or out-of-distribution (OOD) scenes. In this study, we introduce the Point-VLA, a plug-and-play policy that augments language instructions with explicit visual cues (e.g., bounding boxes) to resolve referential ambiguity and enable precise object-level grounding. To efficiently scale visually grounded datasets, we further develop an automatic data annotation pipeline requiring minimal human effort. We evaluate Point-VLA on diverse real-world referring tasks and observe consistently stronger performance than text-only instruction VLAs, particularly in cluttered or unseen-object scenarios, with robust generalization. These results demonstrate that Point-VLA effectively resolves object referring ambiguity through pixel-level visual grounding, achieving more generalizable embodied control.

## 核心内容
Vision-Language-Action (VLA) models align vision and language with embodied control, but their object referring ability remains limited when relying solely on text prompt, especially in cluttered or out-of-distribution (OOD) scenes. In this study, we introduce the Point-VLA, a plug-and-play policy that augments language instructions with explicit visual cues (e.g., bounding boxes) to resolve referential ambiguity and enable precise object-level grounding. To efficiently scale visually grounded datasets, we further develop an automatic data annotation pipeline requiring minimal human effort. We evaluate Point-VLA on diverse real-world referring tasks and observe consistently stronger performance than text-only instruction VLAs, particularly in cluttered or unseen-object scenarios, with robust generalization. These results demonstrate that Point-VLA effectively resolves object referring ambiguity through pixel-level visual grounding, achieving more generalizable embodied control.

## 参考
- http://arxiv.org/abs/2512.18933v2

## Overview
Vision-Language-Action (VLA) models align vision and language with embodied control, but their object referring ability remains limited when relying solely on text prompt, especially in cluttered or out-of-distribution (OOD) scenes. In this study, we introduce the Point-VLA, a plug-and-play policy that augments language instructions with explicit visual cues (e.g., bounding boxes) to resolve referential ambiguity and enable precise object-level grounding. To efficiently scale visually grounded datasets, we further develop an automatic data annotation pipeline requiring minimal human effort. We evaluate Point-VLA on diverse real-world referring tasks and observe consistently stronger performance than text-only instruction VLAs, particularly in cluttered or unseen-object scenarios, with robust generalization. These results demonstrate that Point-VLA effectively resolves object referring ambiguity through pixel-level visual grounding, achieving more generalizable embodied control.

## Content
Vision-Language-Action (VLA) models align vision and language with embodied control, but their object referring ability remains limited when relying solely on text prompt, especially in cluttered or out-of-distribution (OOD) scenes. In this study, we introduce the Point-VLA, a plug-and-play policy that augments language instructions with explicit visual cues (e.g., bounding boxes) to resolve referential ambiguity and enable precise object-level grounding. To efficiently scale visually grounded datasets, we further develop an automatic data annotation pipeline requiring minimal human effort. We evaluate Point-VLA on diverse real-world referring tasks and observe consistently stronger performance than text-only instruction VLAs, particularly in cluttered or unseen-object scenarios, with robust generalization. These results demonstrate that Point-VLA effectively resolves object referring ambiguity through pixel-level visual grounding, achieving more generalizable embodied control.

## 개요
Vision-Language-Action (VLA) 모델은 시각 및 언어를 임베디드 제어와 정렬하지만, 텍스트 프롬프트에만 의존할 경우 객체 참조 능력이 제한적이며, 특히 복잡하거나 분포 외(OOD) 장면에서 그러합니다. 본 연구에서는 Point-VLA를 소개합니다. 이는 플러그 앤 플레이 정책으로, 명시적 시각적 단서(예: 경계 상자)를 언어 명령에 추가하여 참조 모호성을 해결하고 정밀한 객체 수준의 근거를 가능하게 합니다. 시각적으로 근거된 데이터셋을 효율적으로 확장하기 위해, 최소한의 인간 노력만 필요한 자동 데이터 주석 파이프라인을 추가로 개발했습니다. 다양한 실제 참조 작업에서 Point-VLA를 평가한 결과, 텍스트 전용 명령 VLA보다 일관되게 더 강력한 성능을 관찰했으며, 특히 복잡하거나 보지 못한 객체 시나리오에서 강력한 일반화를 보였습니다. 이러한 결과는 Point-VLA가 픽셀 수준의 시각적 근거를 통해 객체 참조 모호성을 효과적으로 해결하여 더 일반화 가능한 임베디드 제어를 달성함을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 시각 및 언어를 임베디드 제어와 정렬하지만, 텍스트 프롬프트에만 의존할 경우 객체 참조 능력이 제한적이며, 특히 복잡하거나 분포 외(OOD) 장면에서 그러합니다. 본 연구에서는 Point-VLA를 소개합니다. 이는 플러그 앤 플레이 정책으로, 명시적 시각적 단서(예: 경계 상자)를 언어 명령에 추가하여 참조 모호성을 해결하고 정밀한 객체 수준의 근거를 가능하게 합니다. 시각적으로 근거된 데이터셋을 효율적으로 확장하기 위해, 최소한의 인간 노력만 필요한 자동 데이터 주석 파이프라인을 추가로 개발했습니다. 다양한 실제 참조 작업에서 Point-VLA를 평가한 결과, 텍스트 전용 명령 VLA보다 일관되게 더 강력한 성능을 관찰했으며, 특히 복잡하거나 보지 못한 객체 시나리오에서 강력한 일반화를 보였습니다. 이러한 결과는 Point-VLA가 픽셀 수준의 시각적 근거를 통해 객체 참조 모호성을 효과적으로 해결하여 더 일반화 가능한 임베디드 제어를 달성함을 보여줍니다.
