---
$id: ent_paper_fallenstein_reflective_oracles_a_foundatio_2015
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Reflective Oracles: A Foundation for Classical Game Theory'
  zh: 反射预言机：经典博弈论的基础
  ko: '반사적 오라클: 고전적 게임 이론의 기초'
summary:
  en: Introduces probabilistic reflective oracles that enable oracle machines to answer queries about other machines sharing
    the same oracle, and shows that causal decision-theoretic agents using such oracles play Nash equilibria when embedded
    in a shared environment.
  zh: 经典博弈论把玩家当作特殊存在，本文引入“反射型”预言机，使带相同预言机的图灵机智能体可在共享环境中把对手建模为环境的普通部分，从而用因果决策理论定义理性智能体，并证明这些智能体交互时会形成纳什均衡。
  ko: 동일한 오라클을 공유하는 기계들의 출력에 대한 질문에 답할 수 있는 확률적 반사적 오라클을 도입하고, 이러한 오라클을 사용하는 인과적 의사결정 이론 에이전트가 공유 환경에서 상호작용할 때 내쉬 균형을 형성함을
    보인다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- reflective_oracles
- game_theory
- multi_agent
- causal_decision_theory
- nash_equilibrium
- decision_theory
- foundations
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1508.04145v1; frontmatter repaired
    by scripts/repair_broken_frontmatter.py.
sources:
- id: src_001
  type: paper
  title: 'Reflective Oracles: A Foundation for Classical Game Theory'
  url: https://arxiv.org/abs/1508.04145
  date: '2015'
  accessed_at: '2026-06-27'
theoretical_depth:
- formalism
- method
---

## 概述
Classical game theory treats players as special---a description of a game contains a full, explicit enumeration of all players---even though in the real world, "players" are no more fundamentally special than rocks or clouds. It isn't trivial to find a decision-theoretic foundation for game theory in which an agent's coplayers are a non-distinguished part of the agent's environment. Attempts to model both players and the environment as Turing machines, for example, fail for standard diagonalization reasons. In this paper, we introduce a "reflective" type of oracle, which is able to answer questions about the outputs of oracle machines with access to the same oracle. These oracles avoid diagonalization by answering some queries randomly. We show that machines with access to a reflective oracle can be used to define rational agents using causal decision theory. These agents model their environment as a probabilistic oracle machine, which may contain other agents as a non-distinguished part. We show that if such agents interact, they will play a Nash equilibrium, with the randomization in mixed strategies coming from the randomization in the oracle's answers. This can be seen as providing a foundation for classical game theory in which players aren't special.

## 核心内容
Classical game theory treats players as special---a description of a game contains a full, explicit enumeration of all players---even though in the real world, "players" are no more fundamentally special than rocks or clouds. It isn't trivial to find a decision-theoretic foundation for game theory in which an agent's coplayers are a non-distinguished part of the agent's environment. Attempts to model both players and the environment as Turing machines, for example, fail for standard diagonalization reasons. In this paper, we introduce a "reflective" type of oracle, which is able to answer questions about the outputs of oracle machines with access to the same oracle. These oracles avoid diagonalization by answering some queries randomly. We show that machines with access to a reflective oracle can be used to define rational agents using causal decision theory. These agents model their environment as a probabilistic oracle machine, which may contain other agents as a non-distinguished part. We show that if such agents interact, they will play a Nash equilibrium, with the randomization in mixed strategies coming from the randomization in the oracle's answers. This can be seen as providing a foundation for classical game theory in which players aren't special.

## 参考
- https://arxiv.org/abs/1508.04145

## Overview
Classical game theory treats players as special---a description of a game contains a full, explicit enumeration of all players---even though in the real world, "players" are no more fundamentally special than rocks or clouds. It isn't trivial to find a decision-theoretic foundation for game theory in which an agent's coplayers are a non-distinguished part of the agent's environment. Attempts to model both players and the environment as Turing machines, for example, fail for standard diagonalization reasons. In this paper, we introduce a "reflective" type of oracle, which is able to answer questions about the outputs of oracle machines with access to the same oracle. These oracles avoid diagonalization by answering some queries randomly. We show that machines with access to a reflective oracle can be used to define rational agents using causal decision theory. These agents model their environment as a probabilistic oracle machine, which may contain other agents as a non-distinguished part. We show that if such agents interact, they will play a Nash equilibrium, with the randomization in mixed strategies coming from the randomization in the oracle's answers. This can be seen as providing a foundation for classical game theory in which players aren't special.

## Content
Classical game theory treats players as special---a description of a game contains a full, explicit enumeration of all players---even though in the real world, "players" are no more fundamentally special than rocks or clouds. It isn't trivial to find a decision-theoretic foundation for game theory in which an agent's coplayers are a non-distinguished part of the agent's environment. Attempts to model both players and the environment as Turing machines, for example, fail for standard diagonalization reasons. In this paper, we introduce a "reflective" type of oracle, which is able to answer questions about the outputs of oracle machines with access to the same oracle. These oracles avoid diagonalization by answering some queries randomly. We show that machines with access to a reflective oracle can be used to define rational agents using causal decision theory. These agents model their environment as a probabilistic oracle machine, which may contain other agents as a non-distinguished part. We show that if such agents interact, they will play a Nash equilibrium, with the randomization in mixed strategies coming from the randomization in the oracle's answers. This can be seen as providing a foundation for classical game theory in which players aren't special.

## 개요
고전적 게임 이론은 플레이어를 특별하게 취급합니다. 게임에 대한 설명에는 모든 플레이어가 완전하고 명시적으로 열거되어 있지만, 현실 세계에서 "플레이어"는 근본적으로 바위나 구름보다 특별하지 않습니다. 에이전트의 공동 플레이어가 에이전트 환경의 구별되지 않는 일부인 게임 이론에 대한 결정 이론적 기초를 찾는 것은 쉽지 않습니다. 예를 들어, 플레이어와 환경을 모두 튜링 기계로 모델링하려는 시도는 표준적인 대각선 논법의 이유로 실패합니다. 본 논문에서는 동일한 오라클에 접근하는 오라클 기계의 출력에 대한 질문에 답할 수 있는 "반사적" 유형의 오라클을 소개합니다. 이러한 오라클은 일부 질문에 무작위로 답변함으로써 대각선 논법을 피합니다. 반사적 오라클에 접근하는 기계가 인과적 결정 이론을 사용하여 합리적 에이전트를 정의하는 데 사용될 수 있음을 보여줍니다. 이러한 에이전트는 환경을 확률적 오라클 기계로 모델링하며, 이 기계에는 다른 에이전트가 구별되지 않는 일부로 포함될 수 있습니다. 이러한 에이전트가 상호작용할 경우, 혼합 전략의 무작위화가 오라클 답변의 무작위화에서 비롯된 내쉬 균형을 플레이한다는 것을 보여줍니다. 이는 플레이어가 특별하지 않은 고전적 게임 이론의 기초를 제공하는 것으로 볼 수 있습니다.

## 핵심 내용
고전적 게임 이론은 플레이어를 특별하게 취급합니다. 게임에 대한 설명에는 모든 플레이어가 완전하고 명시적으로 열거되어 있지만, 현실 세계에서 "플레이어"는 근본적으로 바위나 구름보다 특별하지 않습니다. 에이전트의 공동 플레이어가 에이전트 환경의 구별되지 않는 일부인 게임 이론에 대한 결정 이론적 기초를 찾는 것은 쉽지 않습니다. 예를 들어, 플레이어와 환경을 모두 튜링 기계로 모델링하려는 시도는 표준적인 대각선 논법의 이유로 실패합니다. 본 논문에서는 동일한 오라클에 접근하는 오라클 기계의 출력에 대한 질문에 답할 수 있는 "반사적" 유형의 오라클을 소개합니다. 이러한 오라클은 일부 질문에 무작위로 답변함으로써 대각선 논법을 피합니다. 반사적 오라클에 접근하는 기계가 인과적 결정 이론을 사용하여 합리적 에이전트를 정의하는 데 사용될 수 있음을 보여줍니다. 이러한 에이전트는 환경을 확률적 오라클 기계로 모델링하며, 이 기계에는 다른 에이전트가 구별되지 않는 일부로 포함될 수 있습니다. 이러한 에이전트가 상호작용할 경우, 혼합 전략의 무작위화가 오라클 답변의 무작위화에서 비롯된 내쉬 균형을 플레이한다는 것을 보여줍니다. 이는 플레이어가 특별하지 않은 고전적 게임 이론의 기초를 제공하는 것으로 볼 수 있습니다.
