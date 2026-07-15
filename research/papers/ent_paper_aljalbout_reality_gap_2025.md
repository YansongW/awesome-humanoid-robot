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


