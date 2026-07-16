---
$id: ent_paper_rational_inverse_reasoning_few_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Rational Inverse Reasoning: Few-Shot Imitation by Inferring Intent through Planning'
  zh: 'Rational Inverse Reasoning: Few-Shot Imitation by Inferring Intent through Planning'
  ko: 'Rational Inverse Reasoning: Few-Shot Imitation by Inferring Intent through Planning'
summary:
  en: 'arXiv:2508.08983v2 Announce Type: replace Abstract: Humans can learn a new manipulation task from one or two demonstrations
    and then perform it in a new room, with new objects, under new constraints. Modern robot imitation learning, in contrast,
    typically needs hundreds to thousands of demonstrations and still degrades under modest shifts in layout, geometry, object
    set or task constraints. We argue this gap is not just about data, but also about the level of abstraction at which learning
    occurs; generalization requires inferring the latent intent underlying why a demonstrator behaved in a certain way, rather
    than reproducing how they moved. We present Rational Inverse Reasoning (RIR), which casts few-shot imitation as inference
    over latent explanation programs: compact, executable descriptions of intent that map an object-centric scene to a structured
    task-and-motion-planning (TAMP) specification of goals, subgoals and constraints. A vision-language model proposes candidate
    programs, and a hierarchical planner supplies a bounded-rational likelihood. By combining VLM program proposals, and planner-grounded
    feedback, RIR iteratively refines the candidate set to approximate a posterior over concise, executable programs. On a
    2D reasoning benchmark and a real Franka FR3, RIR recovers transferable task structure from as little as one demonstration.
    Generalizing to substantially new layouts and object sets, RIR outperforms VLM-planning baselines that lack explicit rationality
    and planning-grounded inference, increasing downstream success rate by $34$ and $28$ percentage points in the one- and
    three-shot settings.'
  zh: 'arXiv:2508.08983v2 Announce Type: replace Abstract: Humans can learn a new manipulation task from one or two demonstrations
    and then perform it in a new room, with new objects, under new constraints. Modern robot imitation learning, in contrast,
    typically needs hundreds to thousands of demonstrations and still degrades under modest shifts in layout, geometry, object
    set or task constraints. We argue this gap is not just about data, but also about the level of abstraction at which learning
    occurs; generalization requires inferring the latent intent underlying why a demonstrator behaved in a certain way, rather
    than reproducing how they moved. We present Rational Inverse Reasoning (RIR), which casts few-shot imitation as inference
    over latent explanation programs: compact, executable descriptions of intent that map an object-centric scene to a structured
    task-and-motion-planning (TAMP) specification of goals, subgoals and constraints. A vision-language model proposes candidate
    programs, and a hierarchical planner supplies a bounded-rational likelihood. By combining VLM program proposals, and planner-grounded
    feedback, RIR iteratively refines the candidate set to approximate a posterior over concise, executable programs. On a
    2D reasoning benchmark and a real Franka FR3, RIR recovers transferable task structure from as little as one demonstration.
    Generalizing to substantially new layouts and object sets, RIR outperforms VLM-planning baselines that lack explicit rationality
    and planning-grounded inference, increasing downstream success rate by $34$ and $28$ percentage points in the one- and
    three-shot settings.'
  ko: 'arXiv:2508.08983v2 Announce Type: replace Abstract: Humans can learn a new manipulation task from one or two demonstrations
    and then perform it in a new room, with new objects, under new constraints. Modern robot imitation learning, in contrast,
    typically needs hundreds to thousands of demonstrations and still degrades under modest shifts in layout, geometry, object
    set or task constraints. We argue this gap is not just about data, but also about the level of abstraction at which learning
    occurs; generalization requires inferring the latent intent underlying why a demonstrator behaved in a certain way, rather
    than reproducing how they moved. We present Rational Inverse Reasoning (RIR), which casts few-shot imitation as inference
    over latent explanation programs: compact, executable descriptions of intent that map an object-centric scene to a structured
    task-and-motion-planning (TAMP) specification of goals, subgoals and constraints. A vision-language model proposes candidate
    programs, and a hierarchical planner supplies a bounded-rational likelihood. By combining VLM program proposals, and planner-grounded
    feedback, RIR iteratively refines the candidate set to approximate a posterior over concise, executable programs. On a
    2D reasoning benchmark and a real Franka FR3, RIR recovers transferable task structure from as little as one demonstration.
    Generalizing to substantially new layouts and object sets, RIR outperforms VLM-planning baselines that lack explicit rationality
    and planning-grounded inference, increasing downstream success rate by $34$ and $28$ percentage points in the one- and
    three-shot settings.'
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
- rational_inverse_reasoning
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.08983v2.
sources:
- id: src_001
  type: paper
  title: 'Rational Inverse Reasoning: Few-Shot Imitation by Inferring Intent through Planning (arXiv)'
  url: https://arxiv.org/abs/2508.08983
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Humans can learn a new manipulation task from one or two demonstrations and then perform it in a new room, with new objects, under new constraints. Modern robot imitation learning, in contrast, typically needs hundreds to thousands of demonstrations and still degrades under modest shifts in layout, geometry, object set or task constraints. We argue this gap is not just about data, but also about the level of abstraction at which learning occurs; generalization requires inferring the latent intent underlying why a demonstrator behaved in a certain way, rather than reproducing how they moved. We present Rational Inverse Reasoning (RIR), which casts few-shot imitation as inference over latent explanation programs: compact, executable descriptions of intent that map an object-centric scene to a structured task-and-motion-planning (TAMP) specification of goals, subgoals and constraints. A vision-language model proposes candidate programs, and a hierarchical planner supplies a bounded-rational likelihood. By combining VLM program proposals, and planner-grounded feedback, RIR iteratively refines the candidate set to approximate a posterior over concise, executable programs. On a 2D reasoning benchmark and a real Franka FR3, RIR recovers transferable task structure from as little as one demonstration. Generalizing to substantially new layouts and object sets, RIR outperforms VLM-planning baselines that lack explicit rationality and planning-grounded inference, increasing downstream success rate by $34$ and $28$ percentage points in the one- and three-shot settings.

## 核心内容
Humans can learn a new manipulation task from one or two demonstrations and then perform it in a new room, with new objects, under new constraints. Modern robot imitation learning, in contrast, typically needs hundreds to thousands of demonstrations and still degrades under modest shifts in layout, geometry, object set or task constraints. We argue this gap is not just about data, but also about the level of abstraction at which learning occurs; generalization requires inferring the latent intent underlying why a demonstrator behaved in a certain way, rather than reproducing how they moved. We present Rational Inverse Reasoning (RIR), which casts few-shot imitation as inference over latent explanation programs: compact, executable descriptions of intent that map an object-centric scene to a structured task-and-motion-planning (TAMP) specification of goals, subgoals and constraints. A vision-language model proposes candidate programs, and a hierarchical planner supplies a bounded-rational likelihood. By combining VLM program proposals, and planner-grounded feedback, RIR iteratively refines the candidate set to approximate a posterior over concise, executable programs. On a 2D reasoning benchmark and a real Franka FR3, RIR recovers transferable task structure from as little as one demonstration. Generalizing to substantially new layouts and object sets, RIR outperforms VLM-planning baselines that lack explicit rationality and planning-grounded inference, increasing downstream success rate by $34$ and $28$ percentage points in the one- and three-shot settings.

## 参考
- http://arxiv.org/abs/2508.08983v2

## Overview
Humans can learn a new manipulation task from one or two demonstrations and then perform it in a new room, with new objects, under new constraints. Modern robot imitation learning, in contrast, typically needs hundreds to thousands of demonstrations and still degrades under modest shifts in layout, geometry, object set or task constraints. We argue this gap is not just about data, but also about the level of abstraction at which learning occurs; generalization requires inferring the latent intent underlying why a demonstrator behaved in a certain way, rather than reproducing how they moved. We present Rational Inverse Reasoning (RIR), which casts few-shot imitation as inference over latent explanation programs: compact, executable descriptions of intent that map an object-centric scene to a structured task-and-motion-planning (TAMP) specification of goals, subgoals and constraints. A vision-language model proposes candidate programs, and a hierarchical planner supplies a bounded-rational likelihood. By combining VLM program proposals, and planner-grounded feedback, RIR iteratively refines the candidate set to approximate a posterior over concise, executable programs. On a 2D reasoning benchmark and a real Franka FR3, RIR recovers transferable task structure from as little as one demonstration. Generalizing to substantially new layouts and object sets, RIR outperforms VLM-planning baselines that lack explicit rationality and planning-grounded inference, increasing downstream success rate by $34$ and $28$ percentage points in the one- and three-shot settings.

## Content
Humans can learn a new manipulation task from one or two demonstrations and then perform it in a new room, with new objects, under new constraints. Modern robot imitation learning, in contrast, typically needs hundreds to thousands of demonstrations and still degrades under modest shifts in layout, geometry, object set or task constraints. We argue this gap is not just about data, but also about the level of abstraction at which learning occurs; generalization requires inferring the latent intent underlying why a demonstrator behaved in a certain way, rather than reproducing how they moved. We present Rational Inverse Reasoning (RIR), which casts few-shot imitation as inference over latent explanation programs: compact, executable descriptions of intent that map an object-centric scene to a structured task-and-motion-planning (TAMP) specification of goals, subgoals and constraints. A vision-language model proposes candidate programs, and a hierarchical planner supplies a bounded-rational likelihood. By combining VLM program proposals, and planner-grounded feedback, RIR iteratively refines the candidate set to approximate a posterior over concise, executable programs. On a 2D reasoning benchmark and a real Franka FR3, RIR recovers transferable task structure from as little as one demonstration. Generalizing to substantially new layouts and object sets, RIR outperforms VLM-planning baselines that lack explicit rationality and planning-grounded inference, increasing downstream success rate by $34$ and $28$ percentage points in the one- and three-shot settings.

## 개요
인간은 한두 번의 시연을 통해 새로운 조작 작업을 학습하고, 새로운 방, 새로운 물체, 새로운 제약 조건 하에서 이를 수행할 수 있습니다. 반면, 현대 로봇 모방 학습은 일반적으로 수백에서 수천 번의 시연이 필요하며, 레이아웃, 기하학, 물체 세트 또는 작업 제약 조건의 약간의 변화에도 성능이 저하됩니다. 우리는 이러한 격차가 단순히 데이터의 문제가 아니라 학습이 이루어지는 추상화 수준의 문제라고 주장합니다. 일반화를 위해서는 시연자가 특정 방식으로 행동한 이유에 대한 잠재적 의도를 추론해야 하며, 단순히 움직임을 재현하는 것이 아닙니다. 우리는 합리적 역추론(RIR)을 제안합니다. 이는 소수 샷 모방을 잠재적 설명 프로그램에 대한 추론으로 간주합니다. 즉, 객체 중심 장면을 목표, 하위 목표 및 제약 조건의 구조화된 작업 및 동작 계획(TAMP) 사양으로 매핑하는 간결하고 실행 가능한 의도 설명입니다. 비전-언어 모델이 후보 프로그램을 제안하고, 계층적 계획자가 제한된 합리적 가능성을 제공합니다. VLM 프로그램 제안과 계획 기반 피드백을 결합하여 RIR은 후보 세트를 반복적으로 정제하여 간결하고 실행 가능한 프로그램에 대한 사후 분포를 근사화합니다. 2D 추론 벤치마크와 실제 Franka FR3에서 RIR은 단 한 번의 시연으로도 전이 가능한 작업 구조를 복구합니다. 새로운 레이아웃과 물체 세트로 일반화할 때, RIR은 명시적 합리성과 계획 기반 추론이 부족한 VLM 계획 기준선을 능가하며, 1회 및 3회 설정에서 하류 성공률을 각각 $34$ 및 $28$ 퍼센트 포인트 향상시킵니다.

## 핵심 내용
인간은 한두 번의 시연을 통해 새로운 조작 작업을 학습하고, 새로운 방, 새로운 물체, 새로운 제약 조건 하에서 이를 수행할 수 있습니다. 반면, 현대 로봇 모방 학습은 일반적으로 수백에서 수천 번의 시연이 필요하며, 레이아웃, 기하학, 물체 세트 또는 작업 제약 조건의 약간의 변화에도 성능이 저하됩니다. 우리는 이러한 격차가 단순히 데이터의 문제가 아니라 학습이 이루어지는 추상화 수준의 문제라고 주장합니다. 일반화를 위해서는 시연자가 특정 방식으로 행동한 이유에 대한 잠재적 의도를 추론해야 하며, 단순히 움직임을 재현하는 것이 아닙니다. 우리는 합리적 역추론(RIR)을 제안합니다. 이는 소수 샷 모방을 잠재적 설명 프로그램에 대한 추론으로 간주합니다. 즉, 객체 중심 장면을 목표, 하위 목표 및 제약 조건의 구조화된 작업 및 동작 계획(TAMP) 사양으로 매핑하는 간결하고 실행 가능한 의도 설명입니다. 비전-언어 모델이 후보 프로그램을 제안하고, 계층적 계획자가 제한된 합리적 가능성을 제공합니다. VLM 프로그램 제안과 계획 기반 피드백을 결합하여 RIR은 후보 세트를 반복적으로 정제하여 간결하고 실행 가능한 프로그램에 대한 사후 분포를 근사화합니다. 2D 추론 벤치마크와 실제 Franka FR3에서 RIR은 단 한 번의 시연으로도 전이 가능한 작업 구조를 복구합니다. 새로운 레이아웃과 물체 세트로 일반화할 때, RIR은 명시적 합리성과 계획 기반 추론이 부족한 VLM 계획 기준선을 능가하며, 1회 및 3회 설정에서 하류 성공률을 각각 $34$ 및 $28$ 퍼센트 포인트 향상시킵니다.
