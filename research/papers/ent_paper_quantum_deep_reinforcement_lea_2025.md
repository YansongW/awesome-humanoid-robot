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

## Overview
Classical reinforcement learning (RL) methods often struggle in complex, high-dimensional environments because of their extensive parameter requirements and challenges posed by stochastic, non-deterministic settings. This study introduces quantum deep reinforcement learning (QDRL) to train humanoid agents efficiently. While previous quantum RL models focused on smaller environments, such as wheeled robots and robotic arms, our work pioneers the application of QDRL to humanoid robotics, specifically in environments with substantial observation and action spaces, such as MuJoCo's Humanoid-v4 and Walker2d-v4. Using parameterized quantum circuits, we explored a hybrid quantum-classical setup to directly navigate high-dimensional state spaces, bypassing traditional mapping and planning. By integrating quantum computing with deep RL, we aim to develop models that can efficiently learn complex navigation tasks in humanoid robots. We evaluated the performance of the Soft Actor-Critic (SAC) in classical RL against its quantum implementation. The results show that the quantum SAC achieves an 8% higher average return (246.40) than the classical SAC (228.36) after 92% fewer steps, highlighting the accelerated learning potential of quantum computing in RL tasks.

## Content
Classical reinforcement learning (RL) methods often struggle in complex, high-dimensional environments because of their extensive parameter requirements and challenges posed by stochastic, non-deterministic settings. This study introduces quantum deep reinforcement learning (QDRL) to train humanoid agents efficiently. While previous quantum RL models focused on smaller environments, such as wheeled robots and robotic arms, our work pioneers the application of QDRL to humanoid robotics, specifically in environments with substantial observation and action spaces, such as MuJoCo's Humanoid-v4 and Walker2d-v4. Using parameterized quantum circuits, we explored a hybrid quantum-classical setup to directly navigate high-dimensional state spaces, bypassing traditional mapping and planning. By integrating quantum computing with deep RL, we aim to develop models that can efficiently learn complex navigation tasks in humanoid robots. We evaluated the performance of the Soft Actor-Critic (SAC) in classical RL against its quantum implementation. The results show that the quantum SAC achieves an 8% higher average return (246.40) than the classical SAC (228.36) after 92% fewer steps, highlighting the accelerated learning potential of quantum computing in RL tasks.

## 개요
고전적 강화 학습(RL) 방법은 복잡하고 고차원적인 환경에서 방대한 파라미터 요구와 확률적·비결정론적 환경이 제기하는 어려움으로 인해 종종 어려움을 겪습니다. 본 연구는 휴머노이드 에이전트를 효율적으로 훈련하기 위해 양자 심층 강화 학습(QDRL)을 도입합니다. 이전의 양자 RL 모델은 바퀴 달린 로봇이나 로봇 팔과 같은 소규모 환경에 초점을 맞춘 반면, 우리의 연구는 특히 MuJoCo의 Humanoid-v4 및 Walker2d-v4와 같이 관찰 및 행동 공간이 큰 환경에서 QDRL을 휴머노이드 로보틱스에 적용하는 선구적인 작업입니다. 파라미터화된 양자 회로를 사용하여 전통적인 매핑 및 계획을 우회하고 고차원 상태 공간을 직접 탐색하는 하이브리드 양자-고전 설정을 탐구했습니다. 양자 컴퓨팅과 심층 RL을 통합함으로써 휴머노이드 로봇에서 복잡한 탐색 작업을 효율적으로 학습할 수 있는 모델을 개발하는 것을 목표로 합니다. 고전적 RL에서의 Soft Actor-Critic(SAC) 성능을 양자 구현과 비교 평가했습니다. 결과는 양자 SAC가 고전적 SAC(228.36)보다 92% 적은 스텝 후에 8% 더 높은 평균 수익(246.40)을 달성하여 RL 작업에서 양자 컴퓨팅의 가속화된 학습 잠재력을 강조합니다.

## 핵심 내용
고전적 강화 학습(RL) 방법은 복잡하고 고차원적인 환경에서 방대한 파라미터 요구와 확률적·비결정론적 환경이 제기하는 어려움으로 인해 종종 어려움을 겪습니다. 본 연구는 휴머노이드 에이전트를 효율적으로 훈련하기 위해 양자 심층 강화 학습(QDRL)을 도입합니다. 이전의 양자 RL 모델은 바퀴 달린 로봇이나 로봇 팔과 같은 소규모 환경에 초점을 맞춘 반면, 우리의 연구는 특히 MuJoCo의 Humanoid-v4 및 Walker2d-v4와 같이 관찰 및 행동 공간이 큰 환경에서 QDRL을 휴머노이드 로보틱스에 적용하는 선구적인 작업입니다. 파라미터화된 양자 회로를 사용하여 전통적인 매핑 및 계획을 우회하고 고차원 상태 공간을 직접 탐색하는 하이브리드 양자-고전 설정을 탐구했습니다. 양자 컴퓨팅과 심층 RL을 통합함으로써 휴머노이드 로봇에서 복잡한 탐색 작업을 효율적으로 학습할 수 있는 모델을 개발하는 것을 목표로 합니다. 고전적 RL에서의 Soft Actor-Critic(SAC) 성능을 양자 구현과 비교 평가했습니다. 결과는 양자 SAC가 고전적 SAC(228.36)보다 92% 적은 스텝 후에 8% 더 높은 평균 수익(246.40)을 달성하여 RL 작업에서 양자 컴퓨팅의 가속화된 학습 잠재력을 강조합니다.
