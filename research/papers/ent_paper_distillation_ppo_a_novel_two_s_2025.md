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

## Overview
In recent years, humanoid robots have garnered significant attention from both academia and industry due to their high adaptability to environments and human-like characteristics. With the rapid advancement of reinforcement learning, substantial progress has been made in the walking control of humanoid robots. However, existing methods still face challenges when dealing with complex environments and irregular terrains. In the field of perceptive locomotion, existing approaches are generally divided into two-stage methods and end-to-end methods. Two-stage methods first train a teacher policy in a simulated environment and then use distillation techniques, such as DAgger, to transfer the privileged information learned as latent features or actions to the student policy. End-to-end methods, on the other hand, forgo the learning of privileged information and directly learn policies from a partially observable Markov decision process (POMDP) through reinforcement learning. However, due to the lack of supervision from a teacher policy, end-to-end methods often face difficulties in training and exhibit unstable performance in real-world applications. This paper proposes an innovative two-stage perceptive locomotion framework that combines the advantages of teacher policies learned in a fully observable Markov decision process (MDP) to regularize and supervise the student policy. At the same time, it leverages the characteristics of reinforcement learning to ensure that the student policy can continue to learn in a POMDP, thereby enhancing the model's upper bound. Our experimental results demonstrate that our two-stage training framework achieves higher training efficiency and stability in simulated environments, while also exhibiting better robustness and generalization capabilities in real-world applications.

## Content
In recent years, humanoid robots have garnered significant attention from both academia and industry due to their high adaptability to environments and human-like characteristics. With the rapid advancement of reinforcement learning, substantial progress has been made in the walking control of humanoid robots. However, existing methods still face challenges when dealing with complex environments and irregular terrains. In the field of perceptive locomotion, existing approaches are generally divided into two-stage methods and end-to-end methods. Two-stage methods first train a teacher policy in a simulated environment and then use distillation techniques, such as DAgger, to transfer the privileged information learned as latent features or actions to the student policy. End-to-end methods, on the other hand, forgo the learning of privileged information and directly learn policies from a partially observable Markov decision process (POMDP) through reinforcement learning. However, due to the lack of supervision from a teacher policy, end-to-end methods often face difficulties in training and exhibit unstable performance in real-world applications. This paper proposes an innovative two-stage perceptive locomotion framework that combines the advantages of teacher policies learned in a fully observable Markov decision process (MDP) to regularize and supervise the student policy. At the same time, it leverages the characteristics of reinforcement learning to ensure that the student policy can continue to learn in a POMDP, thereby enhancing the model's upper bound. Our experimental results demonstrate that our two-stage training framework achieves higher training efficiency and stability in simulated environments, while also exhibiting better robustness and generalization capabilities in real-world applications.

## 개요
최근 몇 년간 인간형 로봇은 환경에 대한 높은 적응성과 인간과 유사한 특성으로 인해 학계와 산업계에서 큰 주목을 받고 있습니다. 강화 학습의 급속한 발전과 함께 인간형 로봇의 보행 제어에서 상당한 진전이 이루어졌습니다. 그러나 기존 방법들은 복잡한 환경과 불규칙한 지형을 다룰 때 여전히 어려움에 직면하고 있습니다. 지각적 보행 분야에서 기존 접근법은 일반적으로 2단계 방법과 엔드투엔드 방법으로 나뉩니다. 2단계 방법은 먼저 시뮬레이션 환경에서 교사 정책을 훈련한 다음 DAgger와 같은 증류 기술을 사용하여 학습된 특권 정보를 잠재 특징이나 행동으로 학생 정책에 전달합니다. 반면 엔드투엔드 방법은 특권 정보 학습을 포기하고 부분 관찰 가능 마르코프 결정 과정(POMDP)에서 강화 학습을 통해 직접 정책을 학습합니다. 그러나 교사 정책의 감독 부족으로 인해 엔드투엔드 방법은 종종 훈련에 어려움을 겪고 실제 응용에서 불안정한 성능을 보입니다. 본 논문은 완전 관찰 가능 마르코프 결정 과정(MDP)에서 학습된 교사 정책의 장점을 결합하여 학생 정책을 정규화하고 감독하는 혁신적인 2단계 지각적 보행 프레임워크를 제안합니다. 동시에 강화 학습의 특성을 활용하여 학생 정책이 POMDP에서 계속 학습할 수 있도록 보장함으로써 모델의 상한을 향상시킵니다. 실험 결과는 우리의 2단계 훈련 프레임워크가 시뮬레이션 환경에서 더 높은 훈련 효율성과 안정성을 달성할 뿐만 아니라 실제 응용에서 더 나은 강건성과 일반화 능력을 보여줌을 입증합니다.

## 핵심 내용
최근 몇 년간 인간형 로봇은 환경에 대한 높은 적응성과 인간과 유사한 특성으로 인해 학계와 산업계에서 큰 주목을 받고 있습니다. 강화 학습의 급속한 발전과 함께 인간형 로봇의 보행 제어에서 상당한 진전이 이루어졌습니다. 그러나 기존 방법들은 복잡한 환경과 불규칙한 지형을 다룰 때 여전히 어려움에 직면하고 있습니다. 지각적 보행 분야에서 기존 접근법은 일반적으로 2단계 방법과 엔드투엔드 방법으로 나뉩니다. 2단계 방법은 먼저 시뮬레이션 환경에서 교사 정책을 훈련한 다음 DAgger와 같은 증류 기술을 사용하여 학습된 특권 정보를 잠재 특징이나 행동으로 학생 정책에 전달합니다. 반면 엔드투엔드 방법은 특권 정보 학습을 포기하고 부분 관찰 가능 마르코프 결정 과정(POMDP)에서 강화 학습을 통해 직접 정책을 학습합니다. 그러나 교사 정책의 감독 부족으로 인해 엔드투엔드 방법은 종종 훈련에 어려움을 겪고 실제 응용에서 불안정한 성능을 보입니다. 본 논문은 완전 관찰 가능 마르코프 결정 과정(MDP)에서 학습된 교사 정책의 장점을 결합하여 학생 정책을 정규화하고 감독하는 혁신적인 2단계 지각적 보행 프레임워크를 제안합니다. 동시에 강화 학습의 특성을 활용하여 학생 정책이 POMDP에서 계속 학습할 수 있도록 보장함으로써 모델의 상한을 향상시킵니다. 실험 결과는 우리의 2단계 훈련 프레임워크가 시뮬레이션 환경에서 더 높은 훈련 효율성과 안정성을 달성할 뿐만 아니라 실제 응용에서 더 나은 강건성과 일반화 능력을 보여줌을 입증합니다.
