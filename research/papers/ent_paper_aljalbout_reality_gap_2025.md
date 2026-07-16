---
$id: ent_paper_aljalbout_reality_gap_2025
$schema: ../../../../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'The Reality Gap in Robotics: Challenges, Solutions, and Best Practices'
  zh: 机器人中的现实鸿沟：挑战、解决方案与最佳实践
  ko: '로보틱스의 현실 격차: 과제, 해결책 및 모범 사례'
summary:
  en: A 2025 survey that maps the sim-to-real reality gap into perception and action-dynamics discrepancies, and reviews mitigation
    strategies including domain randomization, system identification, and sim-real co-training.
  zh: Machine learning has facilitated significant advancements across various robotics domains, including navigation, locomotion,
    and manipulation. Many such achievements have been driven by the extensive use of simulation as a critical tool for training
    and testing robotic systems prior to their deployment in real-world environments. However, simulations consist of abstractions
    and approximations that inevitably introduce discrepancies between simulated and real environments, known as the reality
    gap. These discrepancies significantly hinder the successful transfer of systems from simulation to th
  ko: 2025년 서베이로, 시뮬레이션-현실 간 현실 격차를 지각 및 동작 역학 불일치로 분류하고 도메인 랜덤화, 시스템 식별, 시뮬-현실 공동 학습 등 완화 전략을 검토함.
domains:
- 07_ai_models_algorithms
- 02_components
- 08_software_middleware
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- reality_gap
- survey
- domain_randomization
- system_identification
- physics_simulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.20808v1.
sources:
- id: src_paper_aljalbout_reality_gap_2025
  type: paper
  title: 'The Reality Gap in Robotics: Challenges, Solutions, and Best Practices'
  url: https://arxiv.org/abs/2510.20808
  date: '2025-10-23'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---

## 概述
Machine learning has facilitated significant advancements across various robotics domains, including navigation, locomotion, and manipulation. Many such achievements have been driven by the extensive use of simulation as a critical tool for training and testing robotic systems prior to their deployment in real-world environments. However, simulations consist of abstractions and approximations that inevitably introduce discrepancies between simulated and real environments, known as the reality gap. These discrepancies significantly hinder the successful transfer of systems from simulation to the real world. Closing this gap remains one of the most pressing challenges in robotics. Recent advances in sim-to-real transfer have demonstrated promising results across various platforms, including locomotion, navigation, and manipulation. By leveraging techniques such as domain randomization, real-to-sim transfer, state and action abstractions, and sim-real co-training, many works have overcome the reality gap. However, challenges persist, and a deeper understanding of the reality gap's root causes and solutions is necessary. In this survey, we present a comprehensive overview of the sim-to-real landscape, highlighting the causes, solutions, and evaluation metrics for the reality gap and sim-to-real transfer.

## 核心内容
Machine learning has facilitated significant advancements across various robotics domains, including navigation, locomotion, and manipulation. Many such achievements have been driven by the extensive use of simulation as a critical tool for training and testing robotic systems prior to their deployment in real-world environments. However, simulations consist of abstractions and approximations that inevitably introduce discrepancies between simulated and real environments, known as the reality gap. These discrepancies significantly hinder the successful transfer of systems from simulation to the real world. Closing this gap remains one of the most pressing challenges in robotics. Recent advances in sim-to-real transfer have demonstrated promising results across various platforms, including locomotion, navigation, and manipulation. By leveraging techniques such as domain randomization, real-to-sim transfer, state and action abstractions, and sim-real co-training, many works have overcome the reality gap. However, challenges persist, and a deeper understanding of the reality gap's root causes and solutions is necessary. In this survey, we present a comprehensive overview of the sim-to-real landscape, highlighting the causes, solutions, and evaluation metrics for the reality gap and sim-to-real transfer.

## 参考
- http://arxiv.org/abs/2510.20808v1

## Overview
Machine learning has facilitated significant advancements across various robotics domains, including navigation, locomotion, and manipulation. Many such achievements have been driven by the extensive use of simulation as a critical tool for training and testing robotic systems prior to their deployment in real-world environments. However, simulations consist of abstractions and approximations that inevitably introduce discrepancies between simulated and real environments, known as the reality gap. These discrepancies significantly hinder the successful transfer of systems from simulation to the real world. Closing this gap remains one of the most pressing challenges in robotics. Recent advances in sim-to-real transfer have demonstrated promising results across various platforms, including locomotion, navigation, and manipulation. By leveraging techniques such as domain randomization, real-to-sim transfer, state and action abstractions, and sim-real co-training, many works have overcome the reality gap. However, challenges persist, and a deeper understanding of the reality gap's root causes and solutions is necessary. In this survey, we present a comprehensive overview of the sim-to-real landscape, highlighting the causes, solutions, and evaluation metrics for the reality gap and sim-to-real transfer.

## Content
Machine learning has facilitated significant advancements across various robotics domains, including navigation, locomotion, and manipulation. Many such achievements have been driven by the extensive use of simulation as a critical tool for training and testing robotic systems prior to their deployment in real-world environments. However, simulations consist of abstractions and approximations that inevitably introduce discrepancies between simulated and real environments, known as the reality gap. These discrepancies significantly hinder the successful transfer of systems from simulation to the real world. Closing this gap remains one of the most pressing challenges in robotics. Recent advances in sim-to-real transfer have demonstrated promising results across various platforms, including locomotion, navigation, and manipulation. By leveraging techniques such as domain randomization, real-to-sim transfer, state and action abstractions, and sim-real co-training, many works have overcome the reality gap. However, challenges persist, and a deeper understanding of the reality gap's root causes and solutions is necessary. In this survey, we present a comprehensive overview of the sim-to-real landscape, highlighting the causes, solutions, and evaluation metrics for the reality gap and sim-to-real transfer.

## 개요
머신러닝은 내비게이션, 로코모션, 매니퓰레이션 등 다양한 로보틱스 분야에서 상당한 발전을 촉진했습니다. 이러한 성과 중 상당수는 실제 환경에 배치되기 전에 로봇 시스템을 훈련하고 테스트하는 핵심 도구로서 시뮬레이션의 광범위한 사용에 의해 주도되었습니다. 그러나 시뮬레이션은 추상화와 근사치로 구성되어 있어 시뮬레이션 환경과 실제 환경 간의 차이, 즉 현실 격차(reality gap)를 필연적으로 초래합니다. 이러한 차이는 시스템이 시뮬레이션에서 실제 세계로 성공적으로 이전되는 것을 크게 저해합니다. 이 격차를 해소하는 것은 로보틱스에서 가장 시급한 과제 중 하나로 남아 있습니다. 최근 시뮬레이션-실제 전환(sim-to-real transfer)의 발전은 로코모션, 내비게이션, 매니퓰레이션을 포함한 다양한 플랫폼에서 유망한 결과를 보여주었습니다. 도메인 무작위화(domain randomization), 실제-시뮬레이션 전환(real-to-sim transfer), 상태 및 행동 추상화(state and action abstractions), 시뮬레이션-실제 공동 훈련(sim-real co-training)과 같은 기술을 활용하여 많은 연구가 현실 격차를 극복했습니다. 그러나 여전히 과제가 남아 있으며, 현실 격차의 근본 원인과 해결책에 대한 더 깊은 이해가 필요합니다. 본 설문조사에서는 시뮬레이션-실제 전환 환경에 대한 포괄적인 개요를 제시하며, 현실 격차와 시뮬레이션-실제 전환의 원인, 해결책 및 평가 지표를 강조합니다.

## 핵심 내용
머신러닝은 내비게이션, 로코모션, 매니퓰레이션 등 다양한 로보틱스 분야에서 상당한 발전을 촉진했습니다. 이러한 성과 중 상당수는 실제 환경에 배치되기 전에 로봇 시스템을 훈련하고 테스트하는 핵심 도구로서 시뮬레이션의 광범위한 사용에 의해 주도되었습니다. 그러나 시뮬레이션은 추상화와 근사치로 구성되어 있어 시뮬레이션 환경과 실제 환경 간의 차이, 즉 현실 격차(reality gap)를 필연적으로 초래합니다. 이러한 차이는 시스템이 시뮬레이션에서 실제 세계로 성공적으로 이전되는 것을 크게 저해합니다. 이 격차를 해소하는 것은 로보틱스에서 가장 시급한 과제 중 하나로 남아 있습니다. 최근 시뮬레이션-실제 전환(sim-to-real transfer)의 발전은 로코모션, 내비게이션, 매니퓰레이션을 포함한 다양한 플랫폼에서 유망한 결과를 보여주었습니다. 도메인 무작위화(domain randomization), 실제-시뮬레이션 전환(real-to-sim transfer), 상태 및 행동 추상화(state and action abstractions), 시뮬레이션-실제 공동 훈련(sim-real co-training)과 같은 기술을 활용하여 많은 연구가 현실 격차를 극복했습니다. 그러나 여전히 과제가 남아 있으며, 현실 격차의 근본 원인과 해결책에 대한 더 깊은 이해가 필요합니다. 본 설문조사에서는 시뮬레이션-실제 전환 환경에 대한 포괄적인 개요를 제시하며, 현실 격차와 시뮬레이션-실제 전환의 원인, 해결책 및 평가 지표를 강조합니다.
