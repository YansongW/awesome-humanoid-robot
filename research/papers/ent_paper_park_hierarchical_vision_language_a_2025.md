---
$id: ent_paper_park_hierarchical_vision_language_a_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hierarchical Vision Language Action Model Using Success and Failure Demonstrations
  zh: VINE
  ko: Hierarchical Vision Language Action Model Using Success and Failure Demonstrations
summary:
  en: Hierarchical Vision Language Action Model Using Success and Failure Demonstrations (VINE), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Korea University, KAIST, Seoul National University, NAVER AI Lab.
  zh: Hierarchical Vision Language Action Model Using Success and Failure Demonstrations (VINE), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Korea University, KAIST, Seoul National University, NAVER AI Lab.
  ko: Hierarchical Vision Language Action Model Using Success and Failure Demonstrations (VINE), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Korea University, KAIST, Seoul National University, NAVER AI Lab.
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
- robotic_manipulation
- vine
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.03913v1.
sources:
- id: src_001
  type: paper
  title: Hierarchical Vision Language Action Model Using Success and Failure Demonstrations (arXiv)
  url: https://arxiv.org/abs/2512.03913
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VINE source
  url: https://doi.org/10.48550/arXiv.2512.03913
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Prior Vision-Language-Action (VLA) models are typically trained on teleoperated successful demonstrations, while discarding numerous failed attempts that occur naturally during data collection. However, these failures encode where and how policies can be fragile, information that can be exploited to improve robustness. We address this problem by leveraging mixed-quality datasets to learn failure-aware reasoning at planning time. We introduce VINE, a hierarchical vision-language-action model that separates high-level reasoning (System 2) from low-level control (System 1) under a hierarchical reinforcement learning formalism, making failures usable as a structured learning signal rather than noisy supervision. System 2 performs feasibility-guided tree search over a 2D scene-graph abstraction: it proposes subgoal transitions, predicts success probabilities from both successes and failures, and prunes brittle branches before execution, effectively casting plan evaluation as feasibility scoring. The selected subgoal sequence is then passed to System 1, which executes low-level actions without modifying the agent's core skills. Trained entirely from offline teleoperation data, VINE integrates negative experience directly into the decision loop. Across challenging manipulation tasks, this approach consistently improves success rates and robustness, demonstrating that failure data is an essential resource for converting the broad competence of VLAs into robust execution.

## 核心内容
Prior Vision-Language-Action (VLA) models are typically trained on teleoperated successful demonstrations, while discarding numerous failed attempts that occur naturally during data collection. However, these failures encode where and how policies can be fragile, information that can be exploited to improve robustness. We address this problem by leveraging mixed-quality datasets to learn failure-aware reasoning at planning time. We introduce VINE, a hierarchical vision-language-action model that separates high-level reasoning (System 2) from low-level control (System 1) under a hierarchical reinforcement learning formalism, making failures usable as a structured learning signal rather than noisy supervision. System 2 performs feasibility-guided tree search over a 2D scene-graph abstraction: it proposes subgoal transitions, predicts success probabilities from both successes and failures, and prunes brittle branches before execution, effectively casting plan evaluation as feasibility scoring. The selected subgoal sequence is then passed to System 1, which executes low-level actions without modifying the agent's core skills. Trained entirely from offline teleoperation data, VINE integrates negative experience directly into the decision loop. Across challenging manipulation tasks, this approach consistently improves success rates and robustness, demonstrating that failure data is an essential resource for converting the broad competence of VLAs into robust execution.

## 参考
- http://arxiv.org/abs/2512.03913v1

## Overview
Prior Vision-Language-Action (VLA) models are typically trained on teleoperated successful demonstrations, while discarding numerous failed attempts that occur naturally during data collection. However, these failures encode where and how policies can be fragile, information that can be exploited to improve robustness. We address this problem by leveraging mixed-quality datasets to learn failure-aware reasoning at planning time. We introduce VINE, a hierarchical vision-language-action model that separates high-level reasoning (System 2) from low-level control (System 1) under a hierarchical reinforcement learning formalism, making failures usable as a structured learning signal rather than noisy supervision. System 2 performs feasibility-guided tree search over a 2D scene-graph abstraction: it proposes subgoal transitions, predicts success probabilities from both successes and failures, and prunes brittle branches before execution, effectively casting plan evaluation as feasibility scoring. The selected subgoal sequence is then passed to System 1, which executes low-level actions without modifying the agent's core skills. Trained entirely from offline teleoperation data, VINE integrates negative experience directly into the decision loop. Across challenging manipulation tasks, this approach consistently improves success rates and robustness, demonstrating that failure data is an essential resource for converting the broad competence of VLAs into robust execution.

## Content
Prior Vision-Language-Action (VLA) models are typically trained on teleoperated successful demonstrations, while discarding numerous failed attempts that occur naturally during data collection. However, these failures encode where and how policies can be fragile, information that can be exploited to improve robustness. We address this problem by leveraging mixed-quality datasets to learn failure-aware reasoning at planning time. We introduce VINE, a hierarchical vision-language-action model that separates high-level reasoning (System 2) from low-level control (System 1) under a hierarchical reinforcement learning formalism, making failures usable as a structured learning signal rather than noisy supervision. System 2 performs feasibility-guided tree search over a 2D scene-graph abstraction: it proposes subgoal transitions, predicts success probabilities from both successes and failures, and prunes brittle branches before execution, effectively casting plan evaluation as feasibility scoring. The selected subgoal sequence is then passed to System 1, which executes low-level actions without modifying the agent's core skills. Trained entirely from offline teleoperation data, VINE integrates negative experience directly into the decision loop. Across challenging manipulation tasks, this approach consistently improves success rates and robustness, demonstrating that failure data is an essential resource for converting the broad competence of VLAs into robust execution.

## 개요
기존의 Vision-Language-Action (VLA) 모델은 일반적으로 원격 조작 성공 시연 데이터로 학습되며, 데이터 수집 과정에서 자연스럽게 발생하는 수많은 실패 시도는 폐기됩니다. 그러나 이러한 실패는 정책이 취약할 수 있는 위치와 방식을 인코딩하며, 이 정보는 강건성을 개선하는 데 활용될 수 있습니다. 우리는 혼합 품질 데이터셋을 활용하여 계획 시점에서 실패 인식 추론을 학습함으로써 이 문제를 해결합니다. 우리는 계층적 강화 학습 형식 아래에서 고수준 추론(System 2)과 저수준 제어(System 1)를 분리하는 계층적 비전-언어-행동 모델인 VINE을 소개합니다. 이를 통해 실패를 잡음이 있는 감독 신호가 아닌 구조화된 학습 신호로 사용할 수 있게 됩니다. System 2는 2D 장면 그래프 추상화에 대해 실행 가능성 기반 트리 검색을 수행합니다: 하위 목표 전환을 제안하고, 성공과 실패 모두에서 성공 확률을 예측하며, 실행 전에 취약한 분기를 제거하여 계획 평가를 실행 가능성 점수화로 전환합니다. 선택된 하위 목표 시퀀스는 System 1에 전달되며, System 1은 에이전트의 핵심 기술을 수정하지 않고 저수준 행동을 실행합니다. 오프라인 원격 조작 데이터로 완전히 학습된 VINE은 부정적 경험을 의사 결정 루프에 직접 통합합니다. 다양한 까다로운 조작 작업에서 이 접근 방식은 성공률과 강건성을 일관되게 개선하며, 실패 데이터가 VLA의 광범위한 능력을 강건한 실행으로 전환하는 데 필수적인 자원임을 입증합니다.

## 핵심 내용
기존의 Vision-Language-Action (VLA) 모델은 일반적으로 원격 조작 성공 시연 데이터로 학습되며, 데이터 수집 과정에서 자연스럽게 발생하는 수많은 실패 시도는 폐기됩니다. 그러나 이러한 실패는 정책이 취약할 수 있는 위치와 방식을 인코딩하며, 이 정보는 강건성을 개선하는 데 활용될 수 있습니다. 우리는 혼합 품질 데이터셋을 활용하여 계획 시점에서 실패 인식 추론을 학습함으로써 이 문제를 해결합니다. 우리는 계층적 강화 학습 형식 아래에서 고수준 추론(System 2)과 저수준 제어(System 1)를 분리하는 계층적 비전-언어-행동 모델인 VINE을 소개합니다. 이를 통해 실패를 잡음이 있는 감독 신호가 아닌 구조화된 학습 신호로 사용할 수 있게 됩니다. System 2는 2D 장면 그래프 추상화에 대해 실행 가능성 기반 트리 검색을 수행합니다: 하위 목표 전환을 제안하고, 성공과 실패 모두에서 성공 확률을 예측하며, 실행 전에 취약한 분기를 제거하여 계획 평가를 실행 가능성 점수화로 전환합니다. 선택된 하위 목표 시퀀스는 System 1에 전달되며, System 1은 에이전트의 핵심 기술을 수정하지 않고 저수준 행동을 실행합니다. 오프라인 원격 조작 데이터로 완전히 학습된 VINE은 부정적 경험을 의사 결정 루프에 직접 통합합니다. 다양한 까다로운 조작 작업에서 이 접근 방식은 성공률과 강건성을 일관되게 개선하며, 실패 데이터가 VLA의 광범위한 능력을 강건한 실행으로 전환하는 데 필수적인 자원임을 입증합니다.
