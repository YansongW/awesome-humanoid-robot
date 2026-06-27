---
$id: ent_paper_finn_one_shot_visual_imitation_lear_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: One-Shot Visual Imitation Learning via Meta-Learning
  zh: 基于元学习的一次视觉模仿学习
  ko: 메타러닝을 통한 원샷 시각 모방 학습
summary:
  en: Extends model-agnostic meta-learning (MAML) to imitation learning, enabling
    a robot to acquire new vision-based manipulation skills from a single demonstration
    via one or a few gradient updates.
  zh: 将模型无关元学习（MAML）扩展到模仿学习，使机器人能够通过一次或少量梯度更新，从单次演示中学会新的基于视觉的操作技能。
  ko: 모델 무관 메타러닝(MAML)을 모방 학습으로 확장하여, 로봇이 단 하나의 시연을 통해 한 번 또는 소수의 그래디언트 업데이트로 새로운
    비전 기반 조작 기술을 습득할 수 있게 함.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- one_shot_imitation
- meta_learning
- meta_imitation_learning
- visual_imitation
- imitation_learning
- convolutional_neural_network
- spatial_soft_argmax
- bias_transformation
- manipulation
- pr2
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: One-Shot Visual Imitation Learning via Meta-Learning
  url: https://arxiv.org/abs/1709.04905
  date: '2017'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper proposes a meta-imitation learning method that combines meta-learning with behavioral cloning so that a robot can adapt to a new manipulation task from a single visual demonstration. The approach extends model-agnostic meta-learning (MAML) to imitation learning: during meta-training, the policy parameters are optimized so that a small number of gradient steps on one demonstration of a new task produce good performance on another demonstration of the same task. The authors evaluate the method on planar reaching, table-top pushing, and real-world object placing, showing that it scales to raw pixel inputs and outperforms recurrent contextual baselines in data efficiency.

The core algorithm is presented in Algorithm 1 ("Meta-Imitation Learning with MAML"). It samples a batch of tasks, draws two demonstrations per task, performs an inner gradient update on the first demonstration, and updates the meta-parameters using the loss on the second demonstration. The policy architecture is a convolutional neural network with strided convolutions, spatial soft-argmax feature extraction, layer normalization, and fully-connected layers. The authors also introduce a bias transformation and a two-head architecture to improve adaptation.

## Key Contributions

- First demonstration of one-shot imitation learning from raw pixels using gradient-based meta-learning.
- Extension of MAML to imitation learning, making the approach parameter-efficient and scalable to vision inputs.
- Bias transformation and two-head architecture that meta-learn a loss function, enabling one-shot adaptation without expert actions at test time.
- Empirical evaluation on simulated reaching, simulated pushing built on OpenAI Gym PusherEnv with MuJoCo, and real-world placing with a 7-DoF PR2 robot arm.

## Relevance to Humanoid Robotics

The paper explicitly frames its goal as enabling robots to be generalists that can quickly acquire a wide variety of skills in complex unstructured environments. This capability is directly relevant to humanoid robots, which must operate in diverse real-world settings where collecting large task-specific datasets is impractical. By learning to learn from a single visual demonstration, the method supports scalable training and flexible deployment of humanoid manipulation skills. Although the experiments use a single PR2 arm rather than a full humanoid, the vision-based, end-to-end, one-shot skill-acquisition paradigm is a foundational building block for generalist humanoid systems.
