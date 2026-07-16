---
$id: ent_paper_intelligence_06_a_vla_that_learns_from_expe_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'π0.6*: a VLA That Learns From Experience'
  zh: π0.6*
  ko: 'π0.6*: a VLA That Learns From Experience'
summary:
  en: 'π0.6*: a VLA That Learns From Experience (π0.6*), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Physical Intelligence.'
  zh: 'π0.6*: a VLA That Learns From Experience (π0.6*), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Physical Intelligence.'
  ko: 'π0.6*: a VLA That Learns From Experience (π0.6*), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Physical Intelligence.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- '06'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14759v2.
sources:
- id: src_001
  type: paper
  title: 'π0.6*: a VLA That Learns From Experience (arXiv)'
  url: https://arxiv.org/abs/2511.14759
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: π0.6* source
  url: https://doi.org/10.48550/arXiv.2511.14759
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We study how vision-language-action (VLA) models can improve through real-world deployments via reinforcement learning (RL). We present a general-purpose method, RL with Experience and Corrections via Advantage-conditioned Policies (RECAP), that provides for RL training of VLAs via advantage conditioning. Our method incorporates heterogeneous data into the self-improvement process, including demonstrations, data from on-policy collection, and expert teleoperated interventions provided during autonomous execution. RECAP starts by pre-training a generalist VLA with offline RL, which we call $π^{*}_{0.6}$, that can then be specialized to attain high performance on downstream tasks through on-robot data collection. We show that the $π^{*}_{0.6}$ model trained with the full RECAP method can fold laundry in real homes, reliably assemble boxes, and make espresso drinks using a professional espresso machine. On some of the hardest tasks, RECAP more than doubles task throughput and roughly halves the task failure rate.

## 核心内容
We study how vision-language-action (VLA) models can improve through real-world deployments via reinforcement learning (RL). We present a general-purpose method, RL with Experience and Corrections via Advantage-conditioned Policies (RECAP), that provides for RL training of VLAs via advantage conditioning. Our method incorporates heterogeneous data into the self-improvement process, including demonstrations, data from on-policy collection, and expert teleoperated interventions provided during autonomous execution. RECAP starts by pre-training a generalist VLA with offline RL, which we call $π^{*}_{0.6}$, that can then be specialized to attain high performance on downstream tasks through on-robot data collection. We show that the $π^{*}_{0.6}$ model trained with the full RECAP method can fold laundry in real homes, reliably assemble boxes, and make espresso drinks using a professional espresso machine. On some of the hardest tasks, RECAP more than doubles task throughput and roughly halves the task failure rate.

## 参考
- http://arxiv.org/abs/2511.14759v2

## Overview
We study how vision-language-action (VLA) models can improve through real-world deployments via reinforcement learning (RL). We present a general-purpose method, RL with Experience and Corrections via Advantage-conditioned Policies (RECAP), that provides for RL training of VLAs via advantage conditioning. Our method incorporates heterogeneous data into the self-improvement process, including demonstrations, data from on-policy collection, and expert teleoperated interventions provided during autonomous execution. RECAP starts by pre-training a generalist VLA with offline RL, which we call $π^{*}_{0.6}$, that can then be specialized to attain high performance on downstream tasks through on-robot data collection. We show that the $π^{*}_{0.6}$ model trained with the full RECAP method can fold laundry in real homes, reliably assemble boxes, and make espresso drinks using a professional espresso machine. On some of the hardest tasks, RECAP more than doubles task throughput and roughly halves the task failure rate.

## Content
We study how vision-language-action (VLA) models can improve through real-world deployments via reinforcement learning (RL). We present a general-purpose method, RL with Experience and Corrections via Advantage-conditioned Policies (RECAP), that provides for RL training of VLAs via advantage conditioning. Our method incorporates heterogeneous data into the self-improvement process, including demonstrations, data from on-policy collection, and expert teleoperated interventions provided during autonomous execution. RECAP starts by pre-training a generalist VLA with offline RL, which we call $π^{*}_{0.6}$, that can then be specialized to attain high performance on downstream tasks through on-robot data collection. We show that the $π^{*}_{0.6}$ model trained with the full RECAP method can fold laundry in real homes, reliably assemble boxes, and make espresso drinks using a professional espresso machine. On some of the hardest tasks, RECAP more than doubles task throughput and roughly halves the task failure rate.

## 개요
우리는 강화 학습(RL)을 통해 실제 배포 환경에서 비전-언어-행동(VLA) 모델이 어떻게 개선될 수 있는지 연구합니다. 우리는 이점 조건화 정책을 통한 경험 및 수정 기반 RL(RECAP)이라는 범용 방법을 제시하며, 이는 이점 조건화를 통해 VLA의 RL 훈련을 가능하게 합니다. 우리의 방법은 시연, 온-폴리시 수집 데이터, 자율 실행 중 제공되는 전문가 원격 조작 개입 등 이질적인 데이터를 자기 개선 과정에 통합합니다. RECAP은 오프라인 RL로 일반주의 VLA를 사전 훈련하는 것으로 시작하며, 이를 $π^{*}_{0.6}$라고 부릅니다. 이 모델은 로봇 데이터 수집을 통해 하위 작업에서 높은 성능을 달성하도록 특화될 수 있습니다. 우리는 전체 RECAP 방법으로 훈련된 $π^{*}_{0.6}$ 모델이 실제 가정에서 세탁물을 접고, 상자를 안정적으로 조립하며, 전문 에스프레소 머신을 사용해 에스프레소 음료를 만들 수 있음을 보여줍니다. 가장 어려운 작업 중 일부에서는 RECAP이 작업 처리량을 두 배 이상 늘리고 작업 실패율을 대략 절반으로 줄입니다.

## 핵심 내용
우리는 강화 학습(RL)을 통해 실제 배포 환경에서 비전-언어-행동(VLA) 모델이 어떻게 개선될 수 있는지 연구합니다. 우리는 이점 조건화 정책을 통한 경험 및 수정 기반 RL(RECAP)이라는 범용 방법을 제시하며, 이는 이점 조건화를 통해 VLA의 RL 훈련을 가능하게 합니다. 우리의 방법은 시연, 온-폴리시 수집 데이터, 자율 실행 중 제공되는 전문가 원격 조작 개입 등 이질적인 데이터를 자기 개선 과정에 통합합니다. RECAP은 오프라인 RL로 일반주의 VLA를 사전 훈련하는 것으로 시작하며, 이를 $π^{*}_{0.6}$라고 부릅니다. 이 모델은 로봇 데이터 수집을 통해 하위 작업에서 높은 성능을 달성하도록 특화될 수 있습니다. 우리는 전체 RECAP 방법으로 훈련된 $π^{*}_{0.6}$ 모델이 실제 가정에서 세탁물을 접고, 상자를 안정적으로 조립하며, 전문 에스프레소 머신을 사용해 에스프레소 음료를 만들 수 있음을 보여줍니다. 가장 어려운 작업 중 일부에서는 RECAP이 작업 처리량을 두 배 이상 늘리고 작업 실패율을 대략 절반으로 줄입니다.
