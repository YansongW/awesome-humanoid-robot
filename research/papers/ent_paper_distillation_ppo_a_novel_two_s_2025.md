---
$id: ent_paper_distillation_ppo_a_novel_two_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Distillation-PPO: A Novel Two-Stage RL Framework for Humanoid Robot Perceptive Locomotion'
  zh: 'Distillation-PPO: A Novel Two-Stage RL Framework for Humanoid Robot Perceptive Locomotion'
  ko: 'Distillation-PPO: A Novel Two-Stage RL Framework for Humanoid Robot Perceptive Locomotion'
summary:
  en: 'Distillation-PPO: A Novel Two-Stage RL Framework for Humanoid Robot Perceptive Locomotion is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'Distillation-PPO: A Novel Two-Stage RL Framework for Humanoid Robot Perceptive Locomotion is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'Distillation-PPO: A Novel Two-Stage RL Framework for Humanoid Robot Perceptive Locomotion is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- distillation_ppo
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.08299v1.
sources:
- id: src_001
  type: paper
  title: 'Distillation-PPO: A Novel Two-Stage RL Framework for Humanoid Robot Perceptive Locomotion (arXiv)'
  url: https://arxiv.org/abs/2503.08299
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In recent years, humanoid robots have garnered significant attention from both academia and industry due to their high adaptability to environments and human-like characteristics. With the rapid advancement of reinforcement learning, substantial progress has been made in the walking control of humanoid robots. However, existing methods still face challenges when dealing with complex environments and irregular terrains. In the field of perceptive locomotion, existing approaches are generally divided into two-stage methods and end-to-end methods. Two-stage methods first train a teacher policy in a simulated environment and then use distillation techniques, such as DAgger, to transfer the privileged information learned as latent features or actions to the student policy. End-to-end methods, on the other hand, forgo the learning of privileged information and directly learn policies from a partially observable Markov decision process (POMDP) through reinforcement learning. However, due to the lack of supervision from a teacher policy, end-to-end methods often face difficulties in training and exhibit unstable performance in real-world applications. This paper proposes an innovative two-stage perceptive locomotion framework that combines the advantages of teacher policies learned in a fully observable Markov decision process (MDP) to regularize and supervise the student policy. At the same time, it leverages the characteristics of reinforcement learning to ensure that the student policy can continue to learn in a POMDP, thereby enhancing the model's upper bound. Our experimental results demonstrate that our two-stage training framework achieves higher training efficiency and stability in simulated environments, while also exhibiting better robustness and generalization capabilities in real-world applications.

## 核心内容
In recent years, humanoid robots have garnered significant attention from both academia and industry due to their high adaptability to environments and human-like characteristics. With the rapid advancement of reinforcement learning, substantial progress has been made in the walking control of humanoid robots. However, existing methods still face challenges when dealing with complex environments and irregular terrains. In the field of perceptive locomotion, existing approaches are generally divided into two-stage methods and end-to-end methods. Two-stage methods first train a teacher policy in a simulated environment and then use distillation techniques, such as DAgger, to transfer the privileged information learned as latent features or actions to the student policy. End-to-end methods, on the other hand, forgo the learning of privileged information and directly learn policies from a partially observable Markov decision process (POMDP) through reinforcement learning. However, due to the lack of supervision from a teacher policy, end-to-end methods often face difficulties in training and exhibit unstable performance in real-world applications. This paper proposes an innovative two-stage perceptive locomotion framework that combines the advantages of teacher policies learned in a fully observable Markov decision process (MDP) to regularize and supervise the student policy. At the same time, it leverages the characteristics of reinforcement learning to ensure that the student policy can continue to learn in a POMDP, thereby enhancing the model's upper bound. Our experimental results demonstrate that our two-stage training framework achieves higher training efficiency and stability in simulated environments, while also exhibiting better robustness and generalization capabilities in real-world applications.

## 参考
- http://arxiv.org/abs/2503.08299v1

