---
$id: ent_paper_hung_nora_15_a_vision_language_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Nora-1.5: A vision-language-action model trained using world model-and action-based preference rewards'
  zh: NORA-1.5
  ko: 'Nora-1.5: A vision-language-action model trained using world model-and action-based preference rewards'
summary:
  en: 'Nora-1.5: A vision-language-action model trained using world model-and action-based preference rewards (NORA-1.5),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University,
    Singapore University of Technology and Design, University of Antwerp, Queen Mary University of London.'
  zh: 'Nora-1.5: A vision-language-action model trained using world model-and action-based preference rewards (NORA-1.5),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University,
    Singapore University of Technology and Design, University of Antwerp, Queen Mary University of London.'
  ko: 'Nora-1.5: A vision-language-action model trained using world model-and action-based preference rewards (NORA-1.5),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University,
    Singapore University of Technology and Design, University of Antwerp, Queen Mary University of London.'
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
- nora_15
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14659v1.
sources:
- id: src_001
  type: paper
  title: 'Nora-1.5: A vision-language-action model trained using world model-and action-based preference rewards (arXiv)'
  url: https://arxiv.org/abs/2511.14659
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: NORA-1.5 source
  url: https://doi.org/10.48550/arXiv.2511.14659
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision--language--action (VLA) models have recently shown promising performance on a variety of embodied tasks, yet they still fall short in reliability and generalization, especially when deployed across different embodiments or real-world environments. In this work, we introduce NORA-1.5, a VLA model built from the pre-trained NORA backbone by adding to it a flow-matching-based action expert. This architectural enhancement alone yields substantial performance gains, enabling NORA-1.5 to outperform NORA and several state-of-the-art VLA models across both simulated and real-world benchmarks. To further improve robustness and task success, we develop a set of reward models for post-training VLA policies. Our rewards combine (i) an action-conditioned world model (WM) that evaluates whether generated actions lead toward the desired goal, and (ii) a deviation-from-ground-truth heuristic that distinguishes good actions from poor ones. Using these reward signals, we construct preference datasets and adapt NORA-1.5 to target embodiments through direct preference optimization (DPO). Extensive evaluations show that reward-driven post-training consistently improves performance in both simulation and real-robot settings, demonstrating significant VLA model-reliability gains through simple yet effective reward models. Our findings highlight NORA-1.5 and reward-guided post-training as a viable path toward more dependable embodied agents suitable for real-world deployment.

## 核心内容
Vision--language--action (VLA) models have recently shown promising performance on a variety of embodied tasks, yet they still fall short in reliability and generalization, especially when deployed across different embodiments or real-world environments. In this work, we introduce NORA-1.5, a VLA model built from the pre-trained NORA backbone by adding to it a flow-matching-based action expert. This architectural enhancement alone yields substantial performance gains, enabling NORA-1.5 to outperform NORA and several state-of-the-art VLA models across both simulated and real-world benchmarks. To further improve robustness and task success, we develop a set of reward models for post-training VLA policies. Our rewards combine (i) an action-conditioned world model (WM) that evaluates whether generated actions lead toward the desired goal, and (ii) a deviation-from-ground-truth heuristic that distinguishes good actions from poor ones. Using these reward signals, we construct preference datasets and adapt NORA-1.5 to target embodiments through direct preference optimization (DPO). Extensive evaluations show that reward-driven post-training consistently improves performance in both simulation and real-robot settings, demonstrating significant VLA model-reliability gains through simple yet effective reward models. Our findings highlight NORA-1.5 and reward-guided post-training as a viable path toward more dependable embodied agents suitable for real-world deployment.

## 参考
- http://arxiv.org/abs/2511.14659v1

## Overview
Vision–language–action (VLA) models have recently shown promising performance on a variety of embodied tasks, yet they still fall short in reliability and generalization, especially when deployed across different embodiments or real-world environments. In this work, we introduce NORA-1.5, a VLA model built from the pre-trained NORA backbone by adding to it a flow-matching-based action expert. This architectural enhancement alone yields substantial performance gains, enabling NORA-1.5 to outperform NORA and several state-of-the-art VLA models across both simulated and real-world benchmarks. To further improve robustness and task success, we develop a set of reward models for post-training VLA policies. Our rewards combine (i) an action-conditioned world model (WM) that evaluates whether generated actions lead toward the desired goal, and (ii) a deviation-from-ground-truth heuristic that distinguishes good actions from poor ones. Using these reward signals, we construct preference datasets and adapt NORA-1.5 to target embodiments through direct preference optimization (DPO). Extensive evaluations show that reward-driven post-training consistently improves performance in both simulation and real-robot settings, demonstrating significant VLA model-reliability gains through simple yet effective reward models. Our findings highlight NORA-1.5 and reward-guided post-training as a viable path toward more dependable embodied agents suitable for real-world deployment.

## Content
Vision–language–action (VLA) models have recently shown promising performance on a variety of embodied tasks, yet they still fall short in reliability and generalization, especially when deployed across different embodiments or real-world environments. In this work, we introduce NORA-1.5, a VLA model built from the pre-trained NORA backbone by adding to it a flow-matching-based action expert. This architectural enhancement alone yields substantial performance gains, enabling NORA-1.5 to outperform NORA and several state-of-the-art VLA models across both simulated and real-world benchmarks. To further improve robustness and task success, we develop a set of reward models for post-training VLA policies. Our rewards combine (i) an action-conditioned world model (WM) that evaluates whether generated actions lead toward the desired goal, and (ii) a deviation-from-ground-truth heuristic that distinguishes good actions from poor ones. Using these reward signals, we construct preference datasets and adapt NORA-1.5 to target embodiments through direct preference optimization (DPO). Extensive evaluations show that reward-driven post-training consistently improves performance in both simulation and real-robot settings, demonstrating significant VLA model-reliability gains through simple yet effective reward models. Our findings highlight NORA-1.5 and reward-guided post-training as a viable path toward more dependable embodied agents suitable for real-world deployment.

## 개요
Vision--language--action (VLA) 모델은 최근 다양한 구현 작업에서 유망한 성능을 보여주고 있지만, 특히 다른 구현체나 실제 환경에 배포될 때 신뢰성과 일반화 측면에서 여전히 부족함을 드러내고 있습니다. 본 연구에서는 사전 학습된 NORA 백본에 흐름 매칭 기반의 행동 전문가(flow-matching-based action expert)를 추가하여 구축한 VLA 모델인 NORA-1.5를 소개합니다. 이러한 아키텍처 개선만으로도 상당한 성능 향상을 가져와, NORA-1.5는 시뮬레이션 및 실제 환경 벤치마크 모두에서 NORA와 여러 최신 VLA 모델을 능가합니다. 견고성과 작업 성공률을 더욱 향상시키기 위해, VLA 정책의 사후 학습을 위한 보상 모델 세트를 개발했습니다. 우리의 보상은 (i) 생성된 행동이 목표 방향으로 이어지는지 평가하는 행동 조건부 세계 모델(WM)과 (ii) 좋은 행동과 나쁜 행동을 구분하는 실제 값과의 편차 휴리스틱(deviation-from-ground-truth heuristic)을 결합합니다. 이러한 보상 신호를 사용하여 선호도 데이터셋을 구축하고, 직접 선호도 최적화(DPO)를 통해 NORA-1.5를 대상 구현체에 적응시킵니다. 광범위한 평가 결과, 보상 기반 사후 학습이 시뮬레이션 및 실제 로봇 환경 모두에서 일관되게 성능을 향상시키며, 간단하면서도 효과적인 보상 모델을 통해 VLA 모델의 신뢰성이 크게 향상됨을 보여줍니다. 본 연구 결과는 NORA-1.5와 보상 기반 사후 학습이 실제 환경 배포에 적합한 더 신뢰할 수 있는 구현 에이전트를 위한 실행 가능한 경로임을 강조합니다.

## 핵심 내용
Vision--language--action (VLA) 모델은 최근 다양한 구현 작업에서 유망한 성능을 보여주고 있지만, 특히 다른 구현체나 실제 환경에 배포될 때 신뢰성과 일반화 측면에서 여전히 부족함을 드러내고 있습니다. 본 연구에서는 사전 학습된 NORA 백본에 흐름 매칭 기반의 행동 전문가(flow-matching-based action expert)를 추가하여 구축한 VLA 모델인 NORA-1.5를 소개합니다. 이러한 아키텍처 개선만으로도 상당한 성능 향상을 가져와, NORA-1.5는 시뮬레이션 및 실제 환경 벤치마크 모두에서 NORA와 여러 최신 VLA 모델을 능가합니다. 견고성과 작업 성공률을 더욱 향상시키기 위해, VLA 정책의 사후 학습을 위한 보상 모델 세트를 개발했습니다. 우리의 보상은 (i) 생성된 행동이 목표 방향으로 이어지는지 평가하는 행동 조건부 세계 모델(WM)과 (ii) 좋은 행동과 나쁜 행동을 구분하는 실제 값과의 편차 휴리스틱(deviation-from-ground-truth heuristic)을 결합합니다. 이러한 보상 신호를 사용하여 선호도 데이터셋을 구축하고, 직접 선호도 최적화(DPO)를 통해 NORA-1.5를 대상 구현체에 적응시킵니다. 광범위한 평가 결과, 보상 기반 사후 학습이 시뮬레이션 및 실제 로봇 환경 모두에서 일관되게 성능을 향상시키며, 간단하면서도 효과적인 보상 모델을 통해 VLA 모델의 신뢰성이 크게 향상됨을 보여줍니다. 본 연구 결과는 NORA-1.5와 보상 기반 사후 학습이 실제 환경 배포에 적합한 더 신뢰할 수 있는 구현 에이전트를 위한 실행 가능한 경로임을 강조합니다.
