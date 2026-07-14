---
$id: ent_paper_quantum_deep_reinforcement_lea_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Quantum deep reinforcement learning for humanoid robot navigation task
  zh: Quantum deep reinforcement learning for humanoid robot navigation task
  ko: Quantum deep reinforcement learning for humanoid robot navigation task
summary:
  en: Quantum deep reinforcement learning for humanoid robot navigation task is a 2025 work on navigation for humanoid robots.
  zh: Quantum deep reinforcement learning for humanoid robot navigation task is a 2025 work on navigation for humanoid robots.
  ko: Quantum deep reinforcement learning for humanoid robot navigation task is a 2025 work on navigation for humanoid robots.
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
- navigation
- quantum_deep_reinforcement_lea
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.11388v1.
sources:
- id: src_001
  type: paper
  title: Quantum deep reinforcement learning for humanoid robot navigation task (arXiv)
  url: https://arxiv.org/abs/2509.11388
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Classical reinforcement learning (RL) methods often struggle in complex, high-dimensional environments because of their extensive parameter requirements and challenges posed by stochastic, non-deterministic settings. This study introduces quantum deep reinforcement learning (QDRL) to train humanoid agents efficiently. While previous quantum RL models focused on smaller environments, such as wheeled robots and robotic arms, our work pioneers the application of QDRL to humanoid robotics, specifically in environments with substantial observation and action spaces, such as MuJoCo's Humanoid-v4 and Walker2d-v4. Using parameterized quantum circuits, we explored a hybrid quantum-classical setup to directly navigate high-dimensional state spaces, bypassing traditional mapping and planning. By integrating quantum computing with deep RL, we aim to develop models that can efficiently learn complex navigation tasks in humanoid robots. We evaluated the performance of the Soft Actor-Critic (SAC) in classical RL against its quantum implementation. The results show that the quantum SAC achieves an 8% higher average return (246.40) than the classical SAC (228.36) after 92% fewer steps, highlighting the accelerated learning potential of quantum computing in RL tasks.

## 核心内容
Classical reinforcement learning (RL) methods often struggle in complex, high-dimensional environments because of their extensive parameter requirements and challenges posed by stochastic, non-deterministic settings. This study introduces quantum deep reinforcement learning (QDRL) to train humanoid agents efficiently. While previous quantum RL models focused on smaller environments, such as wheeled robots and robotic arms, our work pioneers the application of QDRL to humanoid robotics, specifically in environments with substantial observation and action spaces, such as MuJoCo's Humanoid-v4 and Walker2d-v4. Using parameterized quantum circuits, we explored a hybrid quantum-classical setup to directly navigate high-dimensional state spaces, bypassing traditional mapping and planning. By integrating quantum computing with deep RL, we aim to develop models that can efficiently learn complex navigation tasks in humanoid robots. We evaluated the performance of the Soft Actor-Critic (SAC) in classical RL against its quantum implementation. The results show that the quantum SAC achieves an 8% higher average return (246.40) than the classical SAC (228.36) after 92% fewer steps, highlighting the accelerated learning potential of quantum computing in RL tasks.

## 参考
- http://arxiv.org/abs/2509.11388v1

