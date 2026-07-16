---
$id: ent_paper_heracles_bridging_precise_trac_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Heracles: Bridging Precise Tracking and Generative Synthesis for General Humanoid Control'
  zh: 偏离参考轨迹时，继续追踪可能是错的
  ko: 'Heracles: Bridging Precise Tracking and Generative Synthesis for General Humanoid Control'
summary:
  en: 'Heracles: Bridging Precise Tracking and Generative Synthesis for General Humanoid Control is a knowledge node related
    to paper in the humanoid robot value chain.'
  zh: Achieving general-purpose humanoid control requires a delicate balance between the precise execution of commanded motions
    and the flexible, anthropomorphic adaptability needed to recover from unpredictable environmental perturbations. Current
    general controllers predominantly formulate motion control as a rigid reference-tracking problem. While effective in nominal
    conditions, these trackers often exhibit brittle, non-anthropomorphic failure modes under severe disturbances, lacking
    the generative adaptability inherent to human motor control. To overcome this limitation, we propose Heracles, a novel
    state-conditioned diffusion middleware that bridges precise motion tracking and generative synthesis. Rather than relying
    on rigid tracking paradigms or complex explicit mode-switching, Heracles
  ko: 'Heracles: Bridging Precise Tracking and Generative Synthesis for General Humanoid Control is a knowledge node related
    to paper in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- compliance
- contact_rich
- fall_recovery
- load_carrying
- safety
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.27756v2.
sources:
- id: src_001
  type: paper
  title: 'Heracles: Bridging Precise Tracking and Generative Synthesis for General Humanoid Control (arXiv)'
  url: https://arxiv.org/abs/2603.27756
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 偏离参考轨迹时，继续追踪可能是错的 project page
  url: https://heracles-humanoid-control.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Achieving general-purpose humanoid control requires a delicate balance between the precise execution of commanded motions and the flexible, anthropomorphic adaptability needed to recover from unpredictable environmental perturbations. Current general controllers predominantly formulate motion control as a rigid reference-tracking problem. While effective in nominal conditions, these trackers often exhibit brittle, non-anthropomorphic failure modes under severe disturbances, lacking the generative adaptability inherent to human motor control. To overcome this limitation, we propose Heracles, a novel state-conditioned diffusion middleware that bridges precise motion tracking and generative synthesis. Rather than relying on rigid tracking paradigms or complex explicit mode-switching, Heracles operates as an intermediary layer between high-level reference motions and low-level physics trackers. By conditioning on the robot's real-time state, the diffusion model implicitly adapts its behavior: it approximates an identity map when the state closely aligns with the reference, preserving zero-shot tracking fidelity. Conversely, when encountering significant state deviations, it seamlessly transitions into a generative synthesizer to produce natural, anthropomorphic recovery trajectories. Our framework demonstrates that integrating generative priors into the control loop not only significantly enhances robustness against extreme perturbations but also elevates humanoid control from a rigid tracking paradigm to an open-ended, generative general-purpose architecture.

## 核心内容
Achieving general-purpose humanoid control requires a delicate balance between the precise execution of commanded motions and the flexible, anthropomorphic adaptability needed to recover from unpredictable environmental perturbations. Current general controllers predominantly formulate motion control as a rigid reference-tracking problem. While effective in nominal conditions, these trackers often exhibit brittle, non-anthropomorphic failure modes under severe disturbances, lacking the generative adaptability inherent to human motor control. To overcome this limitation, we propose Heracles, a novel state-conditioned diffusion middleware that bridges precise motion tracking and generative synthesis. Rather than relying on rigid tracking paradigms or complex explicit mode-switching, Heracles operates as an intermediary layer between high-level reference motions and low-level physics trackers. By conditioning on the robot's real-time state, the diffusion model implicitly adapts its behavior: it approximates an identity map when the state closely aligns with the reference, preserving zero-shot tracking fidelity. Conversely, when encountering significant state deviations, it seamlessly transitions into a generative synthesizer to produce natural, anthropomorphic recovery trajectories. Our framework demonstrates that integrating generative priors into the control loop not only significantly enhances robustness against extreme perturbations but also elevates humanoid control from a rigid tracking paradigm to an open-ended, generative general-purpose architecture.

## 参考
- http://arxiv.org/abs/2603.27756v2

## Overview
Achieving general-purpose humanoid control requires a delicate balance between the precise execution of commanded motions and the flexible, anthropomorphic adaptability needed to recover from unpredictable environmental perturbations. Current general controllers predominantly formulate motion control as a rigid reference-tracking problem. While effective in nominal conditions, these trackers often exhibit brittle, non-anthropomorphic failure modes under severe disturbances, lacking the generative adaptability inherent to human motor control. To overcome this limitation, we propose Heracles, a novel state-conditioned diffusion middleware that bridges precise motion tracking and generative synthesis. Rather than relying on rigid tracking paradigms or complex explicit mode-switching, Heracles operates as an intermediary layer between high-level reference motions and low-level physics trackers. By conditioning on the robot's real-time state, the diffusion model implicitly adapts its behavior: it approximates an identity map when the state closely aligns with the reference, preserving zero-shot tracking fidelity. Conversely, when encountering significant state deviations, it seamlessly transitions into a generative synthesizer to produce natural, anthropomorphic recovery trajectories. Our framework demonstrates that integrating generative priors into the control loop not only significantly enhances robustness against extreme perturbations but also elevates humanoid control from a rigid tracking paradigm to an open-ended, generative general-purpose architecture.

## Content
Achieving general-purpose humanoid control requires a delicate balance between the precise execution of commanded motions and the flexible, anthropomorphic adaptability needed to recover from unpredictable environmental perturbations. Current general controllers predominantly formulate motion control as a rigid reference-tracking problem. While effective in nominal conditions, these trackers often exhibit brittle, non-anthropomorphic failure modes under severe disturbances, lacking the generative adaptability inherent to human motor control. To overcome this limitation, we propose Heracles, a novel state-conditioned diffusion middleware that bridges precise motion tracking and generative synthesis. Rather than relying on rigid tracking paradigms or complex explicit mode-switching, Heracles operates as an intermediary layer between high-level reference motions and low-level physics trackers. By conditioning on the robot's real-time state, the diffusion model implicitly adapts its behavior: it approximates an identity map when the state closely aligns with the reference, preserving zero-shot tracking fidelity. Conversely, when encountering significant state deviations, it seamlessly transitions into a generative synthesizer to produce natural, anthropomorphic recovery trajectories. Our framework demonstrates that integrating generative priors into the control loop not only significantly enhances robustness against extreme perturbations but also elevates humanoid control from a rigid tracking paradigm to an open-ended, generative general-purpose architecture.

## 개요
범용 휴머노이드 제어를 달성하려면 명령된 동작의 정밀한 실행과 예측할 수 없는 환경 교란으로부터 회복하는 데 필요한 유연하고 인간형 적응 능력 사이의 섬세한 균형이 필요합니다. 현재의 범용 컨트롤러는 대부분 동작 제어를 엄격한 참조 추적 문제로 공식화합니다. 정상 조건에서는 효과적이지만, 이러한 추적기는 심각한 교란 하에서 취약하고 비인간형 실패 모드를 보이며, 인간의 운동 제어에 내재된 생성적 적응 능력이 부족합니다. 이 한계를 극복하기 위해, 우리는 정밀한 동작 추적과 생성적 합성을 연결하는 새로운 상태 조건 확산 미들웨어인 Heracles를 제안합니다. Heracles는 엄격한 추적 패러다임이나 복잡한 명시적 모드 전환에 의존하지 않고, 고수준 참조 동작과 저수준 물리 추적기 사이의 중간 계층으로 작동합니다. 로봇의 실시간 상태에 조건을 둠으로써, 확산 모델은 암묵적으로 행동을 적응시킵니다: 상태가 참조와 밀접하게 일치할 때는 항등 맵에 가깝게 동작하여 제로샷 추적 충실도를 유지합니다. 반대로, 상당한 상태 편차가 발생할 때는 자연스럽고 인간형 회복 궤적을 생성하는 생성적 합성기로 원활하게 전환됩니다. 우리의 프레임워크는 생성적 사전 지식을 제어 루프에 통합함으로써 극단적인 교란에 대한 견고성을 크게 향상시킬 뿐만 아니라 휴머노이드 제어를 엄격한 추적 패러다임에서 개방형 생성적 범용 아키텍처로 끌어올린다는 것을 보여줍니다.

## 핵심 내용
범용 휴머노이드 제어를 달성하려면 명령된 동작의 정밀한 실행과 예측할 수 없는 환경 교란으로부터 회복하는 데 필요한 유연하고 인간형 적응 능력 사이의 섬세한 균형이 필요합니다. 현재의 범용 컨트롤러는 대부분 동작 제어를 엄격한 참조 추적 문제로 공식화합니다. 정상 조건에서는 효과적이지만, 이러한 추적기는 심각한 교란 하에서 취약하고 비인간형 실패 모드를 보이며, 인간의 운동 제어에 내재된 생성적 적응 능력이 부족합니다. 이 한계를 극복하기 위해, 우리는 정밀한 동작 추적과 생성적 합성을 연결하는 새로운 상태 조건 확산 미들웨어인 Heracles를 제안합니다. Heracles는 엄격한 추적 패러다임이나 복잡한 명시적 모드 전환에 의존하지 않고, 고수준 참조 동작과 저수준 물리 추적기 사이의 중간 계층으로 작동합니다. 로봇의 실시간 상태에 조건을 둠으로써, 확산 모델은 암묵적으로 행동을 적응시킵니다: 상태가 참조와 밀접하게 일치할 때는 항등 맵에 가깝게 동작하여 제로샷 추적 충실도를 유지합니다. 반대로, 상당한 상태 편차가 발생할 때는 자연스럽고 인간형 회복 궤적을 생성하는 생성적 합성기로 원활하게 전환됩니다. 우리의 프레임워크는 생성적 사전 지식을 제어 루프에 통합함으로써 극단적인 교란에 대한 견고성을 크게 향상시킬 뿐만 아니라 휴머노이드 제어를 엄격한 추적 패러다임에서 개방형 생성적 범용 아키텍처로 끌어올린다는 것을 보여줍니다.
