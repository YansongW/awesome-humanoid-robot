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
  en: Extends model-agnostic meta-learning (MAML) to imitation learning, enabling a robot to acquire new vision-based manipulation
    skills from a single demonstration via one or a few gradient updates.
  zh: 将模型无关元学习（MAML）扩展到模仿学习，使机器人能够通过一次或少量梯度更新，从单次演示中学会新的基于视觉的操作技能。
  ko: 모델 무관 메타러닝(MAML)을 모방 학습으로 확장하여, 로봇이 단 하나의 시연을 통해 한 번 또는 소수의 그래디언트 업데이트로 새로운 비전 기반 조작 기술을 습득할 수 있게 함.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1709.04905v1.
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
## 概述
In order for a robot to be a generalist that can perform a wide range of jobs, it must be able to acquire a wide variety of skills quickly and efficiently in complex unstructured environments. High-capacity models such as deep neural networks can enable a robot to represent complex skills, but learning each skill from scratch then becomes infeasible. In this work, we present a meta-imitation learning method that enables a robot to learn how to learn more efficiently, allowing it to acquire new skills from just a single demonstration. Unlike prior methods for one-shot imitation, our method can scale to raw pixel inputs and requires data from significantly fewer prior tasks for effective learning of new skills. Our experiments on both simulated and real robot platforms demonstrate the ability to learn new tasks, end-to-end, from a single visual demonstration.

## 核心内容
In order for a robot to be a generalist that can perform a wide range of jobs, it must be able to acquire a wide variety of skills quickly and efficiently in complex unstructured environments. High-capacity models such as deep neural networks can enable a robot to represent complex skills, but learning each skill from scratch then becomes infeasible. In this work, we present a meta-imitation learning method that enables a robot to learn how to learn more efficiently, allowing it to acquire new skills from just a single demonstration. Unlike prior methods for one-shot imitation, our method can scale to raw pixel inputs and requires data from significantly fewer prior tasks for effective learning of new skills. Our experiments on both simulated and real robot platforms demonstrate the ability to learn new tasks, end-to-end, from a single visual demonstration.

## 参考
- http://arxiv.org/abs/1709.04905v1

