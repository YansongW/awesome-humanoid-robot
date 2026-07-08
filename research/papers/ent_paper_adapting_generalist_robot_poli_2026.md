---
$id: ent_paper_adapting_generalist_robot_poli_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Adapting Generalist Robot Policies with Semantic Reinforcement Learning
  zh: Adapting Generalist Robot Policies with Semantic Reinforcement Learning
  ko: ''
summary:
  en: "arXiv:2606.31958v1 Announce Type: new \nAbstract: Generalist robot policies\
    \ learn a diverse repertoire of behaviors from large-scale pretraining. In principle,\
    \ this makes them excellent priors for downstream adaptation via reinforcement\
    \ learning (RL). In practice, however, standard RL methods leveraging this prior\
    \ optimize directly over robot actions, requiring the base policy's action distribution\
    \ to be close to that of a performant policy from the start. This assumption breaks\
    \ down for complex or long-horizon tasks that fall outside the pretraining distribution.\
    \ Our key insight is that, for sufficiently expressive generalist policies, language\
    \ prompts are an effective alternative space for learning to solve such tasks:\
    \ modulating language inputs elicits skills already within the policy's repertoire,\
    \ which can be composed to solve tasks beyond its zero-shot capabilities. We propose\
    \ Semantic Action Reinforcement Learning (SARL), which learns to optimize this\
    \ prompt space through online interaction, treating the generalist policy as a\
    \ controllable skill prior. Importantly, leveraging pretrained skills rather than\
    \ learning new ones from scratch yields structured, semantically meaningful exploration\
    \ and highly efficient online improvement, and learning to modulate prompts through\
    \ experience grounds them in induced real-world behaviors for robust task-solving.\
    \ Across real-world settings and simulated benchmarks, we show SARL unlocks fundamentally\
    \ new capabilities -- adapting VLA behavior to solve complex, long-horizon tasks\
    \ -- and significantly outperforms existing approaches for improving robot behavior\
    \ in deployment."
  zh: "arXiv:2606.31958v1 Announce Type: new \nAbstract: Generalist robot policies\
    \ learn a diverse repertoire of behaviors from large-scale pretraining. In principle,\
    \ this makes them excellent priors for downstream adaptation via reinforcement\
    \ learning (RL). In practice, however, standard RL methods leveraging this prior\
    \ optimize directly over robot actions, requiring the base policy's action distribution\
    \ to be close to that of a performant policy from the start. This assumption breaks\
    \ down for complex or long-horizon tasks that fall outside the pretraining distribution.\
    \ Our key insight is that, for sufficiently expressive generalist policies, language\
    \ prompts are an effective alternative space for learning to solve such tasks:\
    \ modulating language inputs elicits skills already within the policy's repertoire,\
    \ which can be composed to solve tasks beyond its zero-shot capabilities. We propose\
    \ Semantic Action Reinforcement Learning (SARL), which learns to optimize this\
    \ prompt space through online interaction, treating the generalist policy as a\
    \ controllable skill prior. Importantly, leveraging pretrained skills rather than\
    \ learning new ones from scratch yields structured, semantically meaningful exploration\
    \ and highly efficient online improvement, and learning to modulate prompts through\
    \ experience grounds them in induced real-world behaviors for robust task-solving.\
    \ Across real-world settings and simulated benchmarks, we show SARL unlocks fundamentally\
    \ new capabilities -- adapting VLA behavior to solve complex, long-horizon tasks\
    \ -- and significantly outperforms existing approaches for improving robot behavior\
    \ in deployment."
  ko: ''
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- adapting_generalist_robot_poli
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported from arXiv cs.RO RSS feed.
sources:
- id: src_001
  type: paper
  title: Adapting Generalist Robot Policies with Semantic Reinforcement Learning
  url: https://arxiv.org/abs/2606.31958
  date: '2026'
  accessed_at: '2026-07-01'
---

arXiv:2606.31958v1 Announce Type: new 
Abstract: Generalist robot policies learn a diverse repertoire of behaviors from large-scale pretraining. In principle, this makes them excellent priors for downstream adaptation via reinforcement learning (RL). In practice, however, standard RL methods leveraging this prior optimize directly over robot actions, requiring the base policy's action distribution to be close to that of a performant policy from the start. This assumption breaks down for complex or long-horizon tasks that fall outside the pretraining distribution. Our key insight is that, for sufficiently expressive generalist policies, language prompts are an effective alternative space for learning to solve such tasks: modulating language inputs elicits skills already within the policy's repertoire, which can be composed to solve tasks beyond its zero-shot capabilities. We propose Semantic Action Reinforcement Learning (SARL), which learns to optimize this prompt space through online interaction, treating the generalist policy as a controllable skill prior. Importantly, leveraging pretrained skills rather than learning new ones from scratch yields structured, semantically meaningful exploration and highly efficient online improvement, and learning to modulate prompts through experience grounds them in induced real-world behaviors for robust task-solving. Across real-world settings and simulated benchmarks, we show SARL unlocks fundamentally new capabilities -- adapting VLA behavior to solve complex, long-horizon tasks -- and significantly outperforms existing approaches for improving robot behavior in deployment.
