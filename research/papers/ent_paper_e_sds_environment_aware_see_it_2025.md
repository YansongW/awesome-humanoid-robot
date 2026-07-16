---
$id: ent_paper_e_sds_environment_aware_see_it_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion'
  zh: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion'
  ko: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion'
summary:
  en: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.'
  zh: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.'
  ko: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- e_sds
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.16446v1.
sources:
- id: src_001
  type: paper
  title: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid
    Locomotion (arXiv)'
  url: https://arxiv.org/abs/2512.16446
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language models (VLMs) show promise in automating reward design in humanoid locomotion, which could eliminate the need for tedious manual engineering. However, current VLM-based methods are essentially "blind", as they lack the environmental perception required to navigate complex terrain. We present E-SDS (Environment-aware See it, Do it, Sorted), a framework that closes this perception gap. E-SDS integrates VLMs with real-time terrain sensor analysis to automatically generate reward functions that facilitate training of robust perceptive locomotion policies, grounded by example videos. Evaluated on a Unitree G1 humanoid across four distinct terrains (simple, gaps, obstacles, stairs), E-SDS uniquely enabled successful stair descent, while policies trained with manually-designed rewards or a non-perceptive automated baseline were unable to complete the task. In all terrains, E-SDS also reduced velocity tracking error by 51.9-82.6%. Our framework reduces the human effort of reward design from days to less than two hours while simultaneously producing more robust and capable locomotion policies.

## 核心内容
Vision-language models (VLMs) show promise in automating reward design in humanoid locomotion, which could eliminate the need for tedious manual engineering. However, current VLM-based methods are essentially "blind", as they lack the environmental perception required to navigate complex terrain. We present E-SDS (Environment-aware See it, Do it, Sorted), a framework that closes this perception gap. E-SDS integrates VLMs with real-time terrain sensor analysis to automatically generate reward functions that facilitate training of robust perceptive locomotion policies, grounded by example videos. Evaluated on a Unitree G1 humanoid across four distinct terrains (simple, gaps, obstacles, stairs), E-SDS uniquely enabled successful stair descent, while policies trained with manually-designed rewards or a non-perceptive automated baseline were unable to complete the task. In all terrains, E-SDS also reduced velocity tracking error by 51.9-82.6%. Our framework reduces the human effort of reward design from days to less than two hours while simultaneously producing more robust and capable locomotion policies.

## 参考
- http://arxiv.org/abs/2512.16446v1

## Overview
Vision-language models (VLMs) show promise in automating reward design in humanoid locomotion, which could eliminate the need for tedious manual engineering. However, current VLM-based methods are essentially "blind", as they lack the environmental perception required to navigate complex terrain. We present E-SDS (Environment-aware See it, Do it, Sorted), a framework that closes this perception gap. E-SDS integrates VLMs with real-time terrain sensor analysis to automatically generate reward functions that facilitate training of robust perceptive locomotion policies, grounded by example videos. Evaluated on a Unitree G1 humanoid across four distinct terrains (simple, gaps, obstacles, stairs), E-SDS uniquely enabled successful stair descent, while policies trained with manually-designed rewards or a non-perceptive automated baseline were unable to complete the task. In all terrains, E-SDS also reduced velocity tracking error by 51.9-82.6%. Our framework reduces the human effort of reward design from days to less than two hours while simultaneously producing more robust and capable locomotion policies.

## Content
Vision-language models (VLMs) show promise in automating reward design in humanoid locomotion, which could eliminate the need for tedious manual engineering. However, current VLM-based methods are essentially "blind", as they lack the environmental perception required to navigate complex terrain. We present E-SDS (Environment-aware See it, Do it, Sorted), a framework that closes this perception gap. E-SDS integrates VLMs with real-time terrain sensor analysis to automatically generate reward functions that facilitate training of robust perceptive locomotion policies, grounded by example videos. Evaluated on a Unitree G1 humanoid across four distinct terrains (simple, gaps, obstacles, stairs), E-SDS uniquely enabled successful stair descent, while policies trained with manually-designed rewards or a non-perceptive automated baseline were unable to complete the task. In all terrains, E-SDS also reduced velocity tracking error by 51.9-82.6%. Our framework reduces the human effort of reward design from days to less than two hours while simultaneously producing more robust and capable locomotion policies.

## 개요
Vision-language models (VLMs)는 인간형 로코모션에서 보상 설계를 자동화하는 가능성을 보여주며, 이는 지루한 수동 엔지니어링의 필요성을 없앨 수 있습니다. 그러나 현재 VLM 기반 방법은 본질적으로 "맹목적"이며, 복잡한 지형을 탐색하는 데 필요한 환경 인식 능력이 부족합니다. 우리는 이러한 인식 격차를 해소하는 프레임워크인 E-SDS (Environment-aware See it, Do it, Sorted)를 제시합니다. E-SDS는 VLM을 실시간 지형 센서 분석과 통합하여, 예시 비디오를 기반으로 강건한 인식 기반 로코모션 정책 훈련을 촉진하는 보상 함수를 자동으로 생성합니다. Unitree G1 인간형 로봇을 네 가지 다른 지형(단순, 간격, 장애물, 계단)에서 평가한 결과, E-SDS는 유일하게 계단 하강을 성공적으로 수행했으며, 수동 설계 보상이나 비인식 자동 기준선으로 훈련된 정책은 작업을 완료하지 못했습니다. 모든 지형에서 E-SDS는 속도 추적 오차를 51.9-82.6% 감소시켰습니다. 우리의 프레임워크는 보상 설계에 필요한 인간의 노력을 며칠에서 2시간 미만으로 줄이면서도 더 강건하고 능력 있는 로코모션 정책을 생성합니다.

## 핵심 내용
Vision-language models (VLMs)는 인간형 로코모션에서 보상 설계를 자동화하는 가능성을 보여주며, 이는 지루한 수동 엔지니어링의 필요성을 없앨 수 있습니다. 그러나 현재 VLM 기반 방법은 본질적으로 "맹목적"이며, 복잡한 지형을 탐색하는 데 필요한 환경 인식 능력이 부족합니다. 우리는 이러한 인식 격차를 해소하는 프레임워크인 E-SDS (Environment-aware See it, Do it, Sorted)를 제시합니다. E-SDS는 VLM을 실시간 지형 센서 분석과 통합하여, 예시 비디오를 기반으로 강건한 인식 기반 로코모션 정책 훈련을 촉진하는 보상 함수를 자동으로 생성합니다. Unitree G1 인간형 로봇을 네 가지 다른 지형(단순, 간격, 장애물, 계단)에서 평가한 결과, E-SDS는 유일하게 계단 하강을 성공적으로 수행했으며, 수동 설계 보상이나 비인식 자동 기준선으로 훈련된 정책은 작업을 완료하지 못했습니다. 모든 지형에서 E-SDS는 속도 추적 오차를 51.9-82.6% 감소시켰습니다. 우리의 프레임워크는 보상 설계에 필요한 인간의 노력을 며칠에서 2시간 미만으로 줄이면서도 더 강건하고 능력 있는 로코모션 정책을 생성합니다.
