---
$id: ent_paper_implicit_bezier_motion_model_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Implicit Bézier Motion Model for Precise Spatial and Temporal Control
  zh: Implicit Bézier Motion Model for Precise Spatial and Temporal Control
  ko: Implicit Bézier Motion Model for Precise Spatial and Temporal Control
summary:
  en: Implicit Bézier Motion Model for Precise Spatial and Temporal Control is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
  zh: Implicit Bézier Motion Model for Precise Spatial and Temporal Control is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
  ko: Implicit Bézier Motion Model for Precise Spatial and Temporal Control is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- implicit_bezier_motion_model_f
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://studios.disneyresearch.com/2025/12/03/implicit-bezier-motion-model-for-precise-spatial-and-temporal-control/.
sources:
- id: src_001
  type: website
  title: Implicit Bézier Motion Model for Precise Spatial and Temporal Control project page
  url: https://studios.disneyresearch.com/2025/12/03/implicit-bezier-motion-model-for-precise-spatial-and-temporal-control/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Luca Vögeli (DisneyResearch|Studios) Dhruv Agrawal (ETH Zurich, DisneyResearch|Studios) Martin Guay (DisneyResearch|Studios) Dominik Borer (DisneyResearch|Studios) Robert Sumner (DisneyResearch|Studios) Jakob Buhmann (DisneyResearch|Studios) Creating high-quality character animation remains an intricate and cumbersome process that requires skill, training, and craftsmanship to master. Recently, diffusion models have unlocked the ability to generate diverse movements from high-level condition signals such as text. For artist-friendly control, motion diffusion leveraging Bézier curves have been shown to allow precise joint-level conditioning. Yet, these works have been limited to joints at a fixed temporal stride, while animators require more temporal flexibility when keyframing or manipulating tangents to achieve animation principles such as easing in & out. In this work, we introduce a new Implicit Bézier Motion Model (IBMM), which during training is exposed to all possible configurations of control points, enabling control at arbitrary timings. This allows both precise and sparse joint-level control, anywhere in time and for any joint. In addition, we introduce a new quantitative measure of ease-in and -out, which leads to a novel condition over the motion generation process to reflect this artistic principle.

## 核心内容
Luca Vögeli (DisneyResearch|Studios) Dhruv Agrawal (ETH Zurich, DisneyResearch|Studios) Martin Guay (DisneyResearch|Studios) Dominik Borer (DisneyResearch|Studios) Robert Sumner (DisneyResearch|Studios) Jakob Buhmann (DisneyResearch|Studios) Creating high-quality character animation remains an intricate and cumbersome process that requires skill, training, and craftsmanship to master. Recently, diffusion models have unlocked the ability to generate diverse movements from high-level condition signals such as text. For artist-friendly control, motion diffusion leveraging Bézier curves have been shown to allow precise joint-level conditioning. Yet, these works have been limited to joints at a fixed temporal stride, while animators require more temporal flexibility when keyframing or manipulating tangents to achieve animation principles such as easing in & out. In this work, we introduce a new Implicit Bézier Motion Model (IBMM), which during training is exposed to all possible configurations of control points, enabling control at arbitrary timings. This allows both precise and sparse joint-level control, anywhere in time and for any joint. In addition, we introduce a new quantitative measure of ease-in and -out, which leads to a novel condition over the motion generation process to reflect this artistic principle.

## 参考
- https://studios.disneyresearch.com/2025/12/03/implicit-bezier-motion-model-for-precise-spatial-and-temporal-control/

## Overview
Luca Vögeli (DisneyResearch|Studios) Dhruv Agrawal (ETH Zurich, DisneyResearch|Studios) Martin Guay (DisneyResearch|Studios) Dominik Borer (DisneyResearch|Studios) Robert Sumner (DisneyResearch|Studios) Jakob Buhmann (DisneyResearch|Studios) Creating high-quality character animation remains an intricate and cumbersome process that requires skill, training, and craftsmanship to master. Recently, diffusion models have unlocked the ability to generate diverse movements from high-level condition signals such as text. For artist-friendly control, motion diffusion leveraging Bézier curves have been shown to allow precise joint-level conditioning. Yet, these works have been limited to joints at a fixed temporal stride, while animators require more temporal flexibility when keyframing or manipulating tangents to achieve animation principles such as easing in & out. In this work, we introduce a new Implicit Bézier Motion Model (IBMM), which during training is exposed to all possible configurations of control points, enabling control at arbitrary timings. This allows both precise and sparse joint-level control, anywhere in time and for any joint. In addition, we introduce a new quantitative measure of ease-in and -out, which leads to a novel condition over the motion generation process to reflect this artistic principle.

## Content
Luca Vögeli (DisneyResearch|Studios) Dhruv Agrawal (ETH Zurich, DisneyResearch|Studios) Martin Guay (DisneyResearch|Studios) Dominik Borer (DisneyResearch|Studios) Robert Sumner (DisneyResearch|Studios) Jakob Buhmann (DisneyResearch|Studios) Creating high-quality character animation remains an intricate and cumbersome process that requires skill, training, and craftsmanship to master. Recently, diffusion models have unlocked the ability to generate diverse movements from high-level condition signals such as text. For artist-friendly control, motion diffusion leveraging Bézier curves have been shown to allow precise joint-level conditioning. Yet, these works have been limited to joints at a fixed temporal stride, while animators require more temporal flexibility when keyframing or manipulating tangents to achieve animation principles such as easing in & out. In this work, we introduce a new Implicit Bézier Motion Model (IBMM), which during training is exposed to all possible configurations of control points, enabling control at arbitrary timings. This allows both precise and sparse joint-level control, anywhere in time and for any joint. In addition, we introduce a new quantitative measure of ease-in and -out, which leads to a novel condition over the motion generation process to reflect this artistic principle.

## 개요
Luca Vögeli (DisneyResearch|Studios) Dhruv Agrawal (ETH Zurich, DisneyResearch|Studios) Martin Guay (DisneyResearch|Studios) Dominik Borer (DisneyResearch|Studios) Robert Sumner (DisneyResearch|Studios) Jakob Buhmann (DisneyResearch|Studios) 고품질 캐릭터 애니메이션을 제작하는 것은 숙련도, 훈련, 그리고 장인 정신이 필요한 복잡하고 까다로운 과정으로 남아 있습니다. 최근 확산 모델은 텍스트와 같은 고수준 조건 신호로부터 다양한 움직임을 생성할 수 있는 능력을 열어주었습니다. 아티스트 친화적인 제어를 위해, 베지어 곡선을 활용한 모션 확산은 정밀한 관절 수준의 조건화를 가능하게 하는 것으로 입증되었습니다. 그러나 이러한 연구들은 고정된 시간 간격의 관절에만 국한되어 있었으며, 애니메이터는 키프레임을 설정하거나 탄젠트를 조작하여 이징 인 & 아웃과 같은 애니메이션 원칙을 구현할 때 더 많은 시간적 유연성을 필요로 합니다. 본 연구에서는 훈련 중 제어점의 모든 가능한 구성을 노출시켜 임의의 타이밍에서 제어를 가능하게 하는 새로운 암시적 베지어 모션 모델(IBMM)을 소개합니다. 이를 통해 시간과 관절에 관계없이 정밀하고 희소한 관절 수준의 제어가 가능합니다. 또한, 이징 인 및 아웃에 대한 새로운 정량적 측정을 도입하여, 이 예술적 원칙을 반영하는 모션 생성 과정에 대한 새로운 조건을 제시합니다.

## 핵심 내용
Luca Vögeli (DisneyResearch|Studios) Dhruv Agrawal (ETH Zurich, DisneyResearch|Studios) Martin Guay (DisneyResearch|Studios) Dominik Borer (DisneyResearch|Studios) Robert Sumner (DisneyResearch|Studios) Jakob Buhmann (DisneyResearch|Studios) 고품질 캐릭터 애니메이션을 제작하는 것은 숙련도, 훈련, 그리고 장인 정신이 필요한 복잡하고 까다로운 과정으로 남아 있습니다. 최근 확산 모델은 텍스트와 같은 고수준 조건 신호로부터 다양한 움직임을 생성할 수 있는 능력을 열어주었습니다. 아티스트 친화적인 제어를 위해, 베지어 곡선을 활용한 모션 확산은 정밀한 관절 수준의 조건화를 가능하게 하는 것으로 입증되었습니다. 그러나 이러한 연구들은 고정된 시간 간격의 관절에만 국한되어 있었으며, 애니메이터는 키프레임을 설정하거나 탄젠트를 조작하여 이징 인 & 아웃과 같은 애니메이션 원칙을 구현할 때 더 많은 시간적 유연성을 필요로 합니다. 본 연구에서는 훈련 중 제어점의 모든 가능한 구성을 노출시켜 임의의 타이밍에서 제어를 가능하게 하는 새로운 암시적 베지어 모션 모델(IBMM)을 소개합니다. 이를 통해 시간과 관절에 관계없이 정밀하고 희소한 관절 수준의 제어가 가능합니다. 또한, 이징 인 및 아웃에 대한 새로운 정량적 측정을 도입하여, 이 예술적 원칙을 반영하는 모션 생성 과정에 대한 새로운 조건을 제시합니다.
