---
$id: ent_paper_anchorvla_bridging_discrete_de_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning'
  zh: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning'
  ko: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning'
summary:
  en: 'arXiv:2607.03182v1 Announce Type: new Abstract: Autonomous driving planning requires translating navigation intent,
    traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action
    models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level
    semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory
    prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation
    with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action
    alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose
    AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit
    interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation
    represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than
    a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the
    selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making.
    By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences,
    AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous
    generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art
    Success Rate of 77.28 and a competitive Driving Score of 89.92.'
  zh: 'arXiv:2607.03182v1 Announce Type: new Abstract: Autonomous driving planning requires translating navigation intent,
    traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action
    models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level
    semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory
    prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation
    with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action
    alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose
    AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit
    interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation
    represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than
    a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the
    selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making.
    By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences,
    AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous
    generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art
    Success Rate of 77.28 and a competitive Driving Score of 89.92.'
  ko: 'arXiv:2607.03182v1 Announce Type: new Abstract: Autonomous driving planning requires translating navigation intent,
    traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action
    models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level
    semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory
    prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation
    with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action
    alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose
    AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit
    interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation
    represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than
    a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the
    selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making.
    By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences,
    AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous
    generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art
    Success Rate of 77.28 and a competitive Driving Score of 89.92.'
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
- anchorvla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03182v1.
sources:
- id: src_001
  type: paper
  title: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning (arXiv)'
  url: https://arxiv.org/abs/2607.03182
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Autonomous driving planning requires translating navigation intent, traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making. By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences, AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art Success Rate of 77.28 and a competitive Driving Score of 89.92.

## 核心内容
Autonomous driving planning requires translating navigation intent, traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making. By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences, AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art Success Rate of 77.28 and a competitive Driving Score of 89.92.

## 参考
- http://arxiv.org/abs/2607.03182v1

## Overview
Autonomous driving planning requires translating navigation intent, traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making. By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences, AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art Success Rate of 77.28 and a competitive Driving Score of 89.92.

## Content
Autonomous driving planning requires translating navigation intent, traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making. By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences, AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art Success Rate of 77.28 and a competitive Driving Score of 89.92.

## 개요
자율 주행 계획은 내비게이션 의도, 교통 규칙, 동적 상호작용 및 언어 명령을 실행 가능한 연속 궤적으로 변환해야 합니다. Vision-Language-Action 모델은 장기 꼬리 일반화, 상식 추론, 고수준 의미 이해 및 설명 가능성을 개선하기 위해 주행 계획에 도입되었습니다. 그러나 기존 VLA 계획자는 주로 계획 헤드 기반 궤적 예측 또는 전체 궤적 자기회귀 생성 방식을 따릅니다. 전자는 VLA 추론으로 연속 궤적 생성을 약하게만 제약하는 반면, 후자는 정보 밀도가 낮은 좌표 토큰의 긴 시퀀스에 의존하여 의미-행동 정렬을 어렵게 만들고 이산화 오류와 비효율적인 추론을 초래합니다. 이러한 한계를 해결하기 위해, 우리는 고수준 VLA 추론과 연속 궤적 실행 사이의 명시적 인터페이스로 궤적 패턴 앵커를 사용하는 계층적 결정 앵커 기반 VLA 계획 프레임워크인 AnchorVLA를 제안합니다. 구체적으로, Decision-as-Anchor Representation은 앵커 토큰으로 행동 수준의 주행 결정을 표현하며, 각 토큰은 단일 좌표점이 아닌 전체 로컬 운동 패턴을 인코딩합니다. 그런 다음 Decision-Anchored Residual Flow는 선택된 앵커 정의 잔차 공간에서 세분화된 연속 궤적을 생성하여 고수준 결정 이후의 다중 모드 실행 개선을 포착합니다. 앵커에 대한 압축적이고 의미론적으로 의미 있는 추론을 통해 웨이포인트 시퀀스를 자기회귀적으로 생성하는 대신, AnchorVLA는 LLM 기반 의사 결정을 유지하면서 추론 효율성, 의미-행동 정렬 및 연속 생성 유연성을 개선합니다. Bench2Drive 폐쇄 루프 벤치마크 실험에서 AnchorVLA는 최첨단 성공률 77.28과 경쟁력 있는 주행 점수 89.92를 달성합니다.

## 핵심 내용
자율 주행 계획은 내비게이션 의도, 교통 규칙, 동적 상호작용 및 언어 명령을 실행 가능한 연속 궤적으로 변환해야 합니다. Vision-Language-Action 모델은 장기 꼬리 일반화, 상식 추론, 고수준 의미 이해 및 설명 가능성을 개선하기 위해 주행 계획에 도입되었습니다. 그러나 기존 VLA 계획자는 주로 계획 헤드 기반 궤적 예측 또는 전체 궤적 자기회귀 생성 방식을 따릅니다. 전자는 VLA 추론으로 연속 궤적 생성을 약하게만 제약하는 반면, 후자는 정보 밀도가 낮은 좌표 토큰의 긴 시퀀스에 의존하여 의미-행동 정렬을 어렵게 만들고 이산화 오류와 비효율적인 추론을 초래합니다. 이러한 한계를 해결하기 위해, 우리는 고수준 VLA 추론과 연속 궤적 실행 사이의 명시적 인터페이스로 궤적 패턴 앵커를 사용하는 계층적 결정 앵커 기반 VLA 계획 프레임워크인 AnchorVLA를 제안합니다. 구체적으로, Decision-as-Anchor Representation은 앵커 토큰으로 행동 수준의 주행 결정을 표현하며, 각 토큰은 단일 좌표점이 아닌 전체 로컬 운동 패턴을 인코딩합니다. 그런 다음 Decision-Anchored Residual Flow는 선택된 앵커 정의 잔차 공간에서 세분화된 연속 궤적을 생성하여 고수준 결정 이후의 다중 모드 실행 개선을 포착합니다. 앵커에 대한 압축적이고 의미론적으로 의미 있는 추론을 통해 웨이포인트 시퀀스를 자기회귀적으로 생성하는 대신, AnchorVLA는 LLM 기반 의사 결정을 유지하면서 추론 효율성, 의미-행동 정렬 및 연속 생성 유연성을 개선합니다. Bench2Drive 폐쇄 루프 벤치마크 실험에서 AnchorVLA는 최첨단 성공률 77.28과 경쟁력 있는 주행 점수 89.92를 달성합니다.
