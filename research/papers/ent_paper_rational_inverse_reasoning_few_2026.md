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

