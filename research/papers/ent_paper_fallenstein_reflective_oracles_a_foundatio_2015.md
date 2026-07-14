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
  zh: 引入概率性反射预言机，使预言机机器能够回答共享同一预言机的其他机器的输出查询，并证明使用此类预言机的因果决策理论智能体在共享环境中交互时会达成纳什均衡。
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1508.04145v1.
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
Classical game theory treats players as special---a description of a game contains a full, explicit enumeration of all players---even though in the real world, "players" are no more fundamentally special than rocks or clouds. It isn't trivial to find a decision-theoretic foundation for game theory in which an agent's coplayers are a non-distinguished part of the agent's environment. Attempts to model both players and the environment as Turing machines, for example, fail for standard diagonalization reasons.   In this paper, we introduce a "reflective" type of oracle, which is able to answer questions about the outputs of oracle machines with access to the same oracle. These oracles avoid diagonalization by answering some queries randomly. We show that machines with access to a reflective oracle can be used to define rational agents using causal decision theory. These agents model their environment as a probabilistic oracle machine, which may contain other agents as a non-distinguished part.   We show that if such agents interact, they will play a Nash equilibrium, with the randomization in mixed strategies coming from the randomization in the oracle's answers. This can be seen as providing a foundation for classical game theory in which players aren't special.

## 核心内容
Classical game theory treats players as special---a description of a game contains a full, explicit enumeration of all players---even though in the real world, "players" are no more fundamentally special than rocks or clouds. It isn't trivial to find a decision-theoretic foundation for game theory in which an agent's coplayers are a non-distinguished part of the agent's environment. Attempts to model both players and the environment as Turing machines, for example, fail for standard diagonalization reasons.   In this paper, we introduce a "reflective" type of oracle, which is able to answer questions about the outputs of oracle machines with access to the same oracle. These oracles avoid diagonalization by answering some queries randomly. We show that machines with access to a reflective oracle can be used to define rational agents using causal decision theory. These agents model their environment as a probabilistic oracle machine, which may contain other agents as a non-distinguished part.   We show that if such agents interact, they will play a Nash equilibrium, with the randomization in mixed strategies coming from the randomization in the oracle's answers. This can be seen as providing a foundation for classical game theory in which players aren't special.

## 参考
- http://arxiv.org/abs/1508.04145v1

