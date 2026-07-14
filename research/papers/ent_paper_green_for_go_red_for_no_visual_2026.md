---
$id: ent_paper_green_for_go_red_for_no_visual_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies'
  zh: 'Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies'
  ko: 'Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies'
summary:
  en: "arXiv:2607.05122v1 Announce Type: cross \nAbstract: Vision-language-action (VLA) models enable robot navigation from\
    \ natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations.\
    \ This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time\
    \ segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using\
    \ SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using\
    \ OmniVLA on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest\
    \ waypoint, depending on the instruction length. The benefits are greater for long instructions than for short instructions,\
    \ and grounding provides little improvement for image goals. Normalized error analysis indicates that grounding primarily\
    \ acts as a trajectory length regularizer, reducing the predicted path length by 30% without improving per-unit-distance\
    \ reasoning. Our results indicate that visual grounding offers a simple, computationally inexpensive method to improve\
    \ VLA navigation without model retraining, although it cannot compensate for missing training signals in out-of-distribution\
    \ instructions."
  zh: "arXiv:2607.05122v1 Announce Type: cross \nAbstract: Vision-language-action (VLA) models enable robot navigation from\
    \ natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations.\
    \ This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time\
    \ segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using\
    \ SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using\
    \ OmniVLA on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest\
    \ waypoint, depending on the instruction length. The benefits are greater for long instructions than for short instructions,\
    \ and grounding provides little improvement for image goals. Normalized error analysis indicates that grounding primarily\
    \ acts as a trajectory length regularizer, reducing the predicted path length by 30% without improving per-unit-distance\
    \ reasoning. Our results indicate that visual grounding offers a simple, computationally inexpensive method to improve\
    \ VLA navigation without model retraining, although it cannot compensate for missing training signals in out-of-distribution\
    \ instructions."
  ko: "arXiv:2607.05122v1 Announce Type: cross \nAbstract: Vision-language-action (VLA) models enable robot navigation from\
    \ natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations.\
    \ This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time\
    \ segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using\
    \ SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using\
    \ OmniVLA on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest\
    \ waypoint, depending on the instruction length. The benefits are greater for long instructions than for short instructions,\
    \ and grounding provides little improvement for image goals. Normalized error analysis indicates that grounding primarily\
    \ acts as a trajectory length regularizer, reducing the predicted path length by 30% without improving per-unit-distance\
    \ reasoning. Our results indicate that visual grounding offers a simple, computationally inexpensive method to improve\
    \ VLA navigation without model retraining, although it cannot compensate for missing training signals in out-of-distribution\
    \ instructions."
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- green_for_go_red_for_no
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.05122v1.
sources:
- id: src_001
  type: paper
  title: 'Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies (arXiv)'
  url: https://arxiv.org/abs/2607.05122
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Vision-language-action (VLA) models enable robot navigation from natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations. This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using OmniVLA on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest waypoint, depending on the instruction length. The benefits are greater for long instructions than for short instructions, and grounding provides little improvement for image goals. Normalized error analysis indicates that grounding primarily acts as a trajectory length regularizer, reducing the predicted path length by 30% without improving per-unit-distance reasoning. Our results indicate that visual grounding offers a simple, computationally inexpensive method to improve VLA navigation without model retraining, although it cannot compensate for missing training signals in out-of-distribution instructions.

## 核心内容
Vision-language-action (VLA) models enable robot navigation from natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations. This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using OmniVLA on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest waypoint, depending on the instruction length. The benefits are greater for long instructions than for short instructions, and grounding provides little improvement for image goals. Normalized error analysis indicates that grounding primarily acts as a trajectory length regularizer, reducing the predicted path length by 30% without improving per-unit-distance reasoning. Our results indicate that visual grounding offers a simple, computationally inexpensive method to improve VLA navigation without model retraining, although it cannot compensate for missing training signals in out-of-distribution instructions.

## 参考
- http://arxiv.org/abs/2607.05122v1

