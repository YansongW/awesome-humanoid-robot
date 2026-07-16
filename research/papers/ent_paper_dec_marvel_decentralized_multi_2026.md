---
$id: ent_paper_dec_marvel_decentralized_multi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under Budget Constraints'
  zh: 'Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under Budget Constraints'
  ko: 'Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under Budget Constraints'
summary:
  en: 'arXiv:2607.09060v1 Announce Type: new Abstract: Multi-UAV exploration is often constrained by unreliable communication,
    limited field-of-view sensing (e.g., lightweight onboard camera), and finite travel budgets that require each robot to
    reserve enough budget to return to its base. We present Dec-MARVEL, a decentralized budget-aware exploration framework
    for communication-free teams with directional sensing. Rather than exchanging maps, goals, or messages, each robot coordinates
    through its incidental observations: any teammate trajectory within its field of view serves as a coordination signal.
    A graph-attention actor fuses local frontier geometry, teammate motion, and budget features to select return-feasible
    waypoint-heading actions. The actor is trained with phase-conditioned critics, a training-only task-oriented privileged
    critic, and a mixture-based budget curriculum. Across 900 held-out trials spanning three team sizes (2, 4, 8 robots) and
    three travel budgets (720, 800, 1024 meters) against four baselines, Dec-MARVEL achieves the highest or tied-highest exploration
    rate and lowest sensing overlap across all nine team-size budget configurations. Under our tightest 720m budget, it reaches
    53%, 94%, and 100% success for 2, 4, and 8 robots, versus 37%, 83%, and 99% for the strongest baseline. Physical-robot
    experiments demonstrate successful sim-to-real transfer and real-world deployment of Dec-MARVEL.'
  zh: 'arXiv:2607.09060v1 Announce Type: new Abstract: Multi-UAV exploration is often constrained by unreliable communication,
    limited field-of-view sensing (e.g., lightweight onboard camera), and finite travel budgets that require each robot to
    reserve enough budget to return to its base. We present Dec-MARVEL, a decentralized budget-aware exploration framework
    for communication-free teams with directional sensing. Rather than exchanging maps, goals, or messages, each robot coordinates
    through its incidental observations: any teammate trajectory within its field of view serves as a coordination signal.
    A graph-attention actor fuses local frontier geometry, teammate motion, and budget features to select return-feasible
    waypoint-heading actions. The actor is trained with phase-conditioned critics, a training-only task-oriented privileged
    critic, and a mixture-based budget curriculum. Across 900 held-out trials spanning three team sizes (2, 4, 8 robots) and
    three travel budgets (720, 800, 1024 meters) against four baselines, Dec-MARVEL achieves the highest or tied-highest exploration
    rate and lowest sensing overlap across all nine team-size budget configurations. Under our tightest 720m budget, it reaches
    53%, 94%, and 100% success for 2, 4, and 8 robots, versus 37%, 83%, and 99% for the strongest baseline. Physical-robot
    experiments demonstrate successful sim-to-real transfer and real-world deployment of Dec-MARVEL.'
  ko: 'arXiv:2607.09060v1 Announce Type: new Abstract: Multi-UAV exploration is often constrained by unreliable communication,
    limited field-of-view sensing (e.g., lightweight onboard camera), and finite travel budgets that require each robot to
    reserve enough budget to return to its base. We present Dec-MARVEL, a decentralized budget-aware exploration framework
    for communication-free teams with directional sensing. Rather than exchanging maps, goals, or messages, each robot coordinates
    through its incidental observations: any teammate trajectory within its field of view serves as a coordination signal.
    A graph-attention actor fuses local frontier geometry, teammate motion, and budget features to select return-feasible
    waypoint-heading actions. The actor is trained with phase-conditioned critics, a training-only task-oriented privileged
    critic, and a mixture-based budget curriculum. Across 900 held-out trials spanning three team sizes (2, 4, 8 robots) and
    three travel budgets (720, 800, 1024 meters) against four baselines, Dec-MARVEL achieves the highest or tied-highest exploration
    rate and lowest sensing overlap across all nine team-size budget configurations. Under our tightest 720m budget, it reaches
    53%, 94%, and 100% success for 2, 4, and 8 robots, versus 37%, 83%, and 99% for the strongest baseline. Physical-robot
    experiments demonstrate successful sim-to-real transfer and real-world deployment of Dec-MARVEL.'
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
- dec_marvel
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09060v2.
sources:
- id: src_001
  type: paper
  title: 'Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under Budget Constraints (arXiv)'
  url: https://arxiv.org/abs/2607.09060
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Multi-UAV exploration is often constrained by unreliable communication, limited field-of-view sensing (e.g., lightweight onboard camera), and finite travel budgets that require each robot to reserve enough budget to return to its base. We present Dec-MARVEL, a decentralized budget-aware exploration framework for communication-free teams with directional sensing. Rather than exchanging maps, goals, or messages, each robot coordinates through its incidental observations: any teammate trajectory within its field of view serves as a coordination signal. A graph-attention actor fuses local frontier geometry, teammate motion, and budget features to select return-feasible waypoint-heading actions. The actor is trained with phase-conditioned critics, a training-only task-oriented privileged critic, and a mixture-based budget curriculum. Across 900 held-out trials spanning three team sizes (2, 4, 8 robots) and three travel budgets (720, 800, 1024 meters) against four baselines, Dec-MARVEL achieves the highest or tied-highest exploration rate and lowest sensing overlap across all nine team-size budget configurations. Under our tightest 720m budget, it reaches 53%, 94%, and 100% success for 2, 4, and 8 robots, versus 37%, 83%, and 99% for the strongest baseline. Physical-robot experiments demonstrate successful sim-to-real transfer and real-world deployment of Dec-MARVEL.

## 核心内容
Multi-UAV exploration is often constrained by unreliable communication, limited field-of-view sensing (e.g., lightweight onboard camera), and finite travel budgets that require each robot to reserve enough budget to return to its base. We present Dec-MARVEL, a decentralized budget-aware exploration framework for communication-free teams with directional sensing. Rather than exchanging maps, goals, or messages, each robot coordinates through its incidental observations: any teammate trajectory within its field of view serves as a coordination signal. A graph-attention actor fuses local frontier geometry, teammate motion, and budget features to select return-feasible waypoint-heading actions. The actor is trained with phase-conditioned critics, a training-only task-oriented privileged critic, and a mixture-based budget curriculum. Across 900 held-out trials spanning three team sizes (2, 4, 8 robots) and three travel budgets (720, 800, 1024 meters) against four baselines, Dec-MARVEL achieves the highest or tied-highest exploration rate and lowest sensing overlap across all nine team-size budget configurations. Under our tightest 720m budget, it reaches 53%, 94%, and 100% success for 2, 4, and 8 robots, versus 37%, 83%, and 99% for the strongest baseline. Physical-robot experiments demonstrate successful sim-to-real transfer and real-world deployment of Dec-MARVEL.

## 参考
- http://arxiv.org/abs/2607.09060v2

## Overview
Multi-UAV exploration is often constrained by unreliable communication, limited field-of-view sensing (e.g., lightweight onboard camera), and finite travel budgets that require each robot to reserve enough budget to return to its base. We present Dec-MARVEL, a decentralized budget-aware exploration framework for communication-free teams with directional sensing. Rather than exchanging maps, goals, or messages, each robot coordinates through its incidental observations: any teammate trajectory within its field of view serves as a coordination signal. A graph-attention actor fuses local frontier geometry, teammate motion, and budget features to select return-feasible waypoint-heading actions. The actor is trained with phase-conditioned critics, a training-only task-oriented privileged critic, and a mixture-based budget curriculum. Across 900 held-out trials spanning three team sizes (2, 4, 8 robots) and three travel budgets (720, 800, 1024 meters) against four baselines, Dec-MARVEL achieves the highest or tied-highest exploration rate and lowest sensing overlap across all nine team-size budget configurations. Under our tightest 720m budget, it reaches 53%, 94%, and 100% success for 2, 4, and 8 robots, versus 37%, 83%, and 99% for the strongest baseline. Physical-robot experiments demonstrate successful sim-to-real transfer and real-world deployment of Dec-MARVEL.

## Content
Multi-UAV exploration is often constrained by unreliable communication, limited field-of-view sensing (e.g., lightweight onboard camera), and finite travel budgets that require each robot to reserve enough budget to return to its base. We present Dec-MARVEL, a decentralized budget-aware exploration framework for communication-free teams with directional sensing. Rather than exchanging maps, goals, or messages, each robot coordinates through its incidental observations: any teammate trajectory within its field of view serves as a coordination signal. A graph-attention actor fuses local frontier geometry, teammate motion, and budget features to select return-feasible waypoint-heading actions. The actor is trained with phase-conditioned critics, a training-only task-oriented privileged critic, and a mixture-based budget curriculum. Across 900 held-out trials spanning three team sizes (2, 4, 8 robots) and three travel budgets (720, 800, 1024 meters) against four baselines, Dec-MARVEL achieves the highest or tied-highest exploration rate and lowest sensing overlap across all nine team-size budget configurations. Under our tightest 720m budget, it reaches 53%, 94%, and 100% success for 2, 4, and 8 robots, versus 37%, 83%, and 99% for the strongest baseline. Physical-robot experiments demonstrate successful sim-to-real transfer and real-world deployment of Dec-MARVEL.

## 개요
다중 UAV 탐사는 종종 신뢰할 수 없는 통신, 제한된 시야 센싱(예: 경량 온보드 카메라), 그리고 각 로봇이 기지로 돌아갈 충분한 예산을 확보해야 하는 유한 이동 예산에 의해 제약을 받습니다. 본 논문에서는 방향성 센싱을 사용하는 통신 없는 팀을 위한 분산형 예산 인식 탐사 프레임워크인 Dec-MARVEL을 제시합니다. 각 로봇은 지도, 목표 또는 메시지를 교환하는 대신 우연한 관찰을 통해 협력합니다. 즉, 시야 내에 있는 동료의 궤적이 협력 신호 역할을 합니다. 그래프 어텐션 액터는 로컬 프론티어 기하학, 동료 움직임 및 예산 특징을 융합하여 복귀 가능한 웨이포인트-헤딩 행동을 선택합니다. 액터는 단계 조건부 비평가, 훈련 전용 작업 지향 특권 비평가, 그리고 혼합 기반 예산 커리큘럼으로 훈련됩니다. 세 가지 팀 규모(2, 4, 8대 로봇)와 세 가지 이동 예산(720, 800, 1024미터)을 포함한 900개의 보류된 시험에서 네 가지 기준선과 비교했을 때, Dec-MARVEL은 모든 9가지 팀 규모-예산 구성에서 가장 높거나 동등한 탐사율과 가장 낮은 센싱 중복을 달성합니다. 가장 엄격한 720m 예산 하에서 2, 4, 8대 로봇에 대해 각각 53%, 94%, 100%의 성공률을 기록하며, 이는 가장 강력한 기준선의 37%, 83%, 99%와 대비됩니다. 실제 로봇 실험을 통해 Dec-MARVEL의 시뮬레이션-실제 전환 및 실제 환경 배치 성공을 입증합니다.

## 핵심 내용
다중 UAV 탐사는 종종 신뢰할 수 없는 통신, 제한된 시야 센싱(예: 경량 온보드 카메라), 그리고 각 로봇이 기지로 돌아갈 충분한 예산을 확보해야 하는 유한 이동 예산에 의해 제약을 받습니다. 본 논문에서는 방향성 센싱을 사용하는 통신 없는 팀을 위한 분산형 예산 인식 탐사 프레임워크인 Dec-MARVEL을 제시합니다. 각 로봇은 지도, 목표 또는 메시지를 교환하는 대신 우연한 관찰을 통해 협력합니다. 즉, 시야 내에 있는 동료의 궤적이 협력 신호 역할을 합니다. 그래프 어텐션 액터는 로컬 프론티어 기하학, 동료 움직임 및 예산 특징을 융합하여 복귀 가능한 웨이포인트-헤딩 행동을 선택합니다. 액터는 단계 조건부 비평가, 훈련 전용 작업 지향 특권 비평가, 그리고 혼합 기반 예산 커리큘럼으로 훈련됩니다. 세 가지 팀 규모(2, 4, 8대 로봇)와 세 가지 이동 예산(720, 800, 1024미터)을 포함한 900개의 보류된 시험에서 네 가지 기준선과 비교했을 때, Dec-MARVEL은 모든 9가지 팀 규모-예산 구성에서 가장 높거나 동등한 탐사율과 가장 낮은 센싱 중복을 달성합니다. 가장 엄격한 720m 예산 하에서 2, 4, 8대 로봇에 대해 각각 53%, 94%, 100%의 성공률을 기록하며, 이는 가장 강력한 기준선의 37%, 83%, 99%와 대비됩니다. 실제 로봇 실험을 통해 Dec-MARVEL의 시뮬레이션-실제 전환 및 실제 환경 배치 성공을 입증합니다.
