---
$id: ent_paper_success_in_humanoid_reinforcem_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Success in Humanoid Reinforcement Learning under Partial Observation
  zh: Success in Humanoid Reinforcement Learning under Partial Observation
  ko: Success in Humanoid Reinforcement Learning under Partial Observation
summary:
  en: Success in Humanoid Reinforcement Learning under Partial Observation is a 2025 work on locomotion for humanoid robots.
  zh: Success in Humanoid Reinforcement Learning under Partial Observation is a 2025 work on locomotion for humanoid robots.
  ko: Success in Humanoid Reinforcement Learning under Partial Observation is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- success_in_humanoid_reinforcem
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.18883v1.
sources:
- id: src_001
  type: paper
  title: Success in Humanoid Reinforcement Learning under Partial Observation (arXiv)
  url: https://arxiv.org/abs/2507.18883
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning has been widely applied to robotic control, but effective policy learning under partial observability remains a major challenge, especially in high-dimensional tasks like humanoid locomotion. To date, no prior work has demonstrated stable training of humanoid policies with incomplete state information in the benchmark Gymnasium Humanoid-v4 environment. The objective in this environment is to walk forward as fast as possible without falling, with rewards provided for staying upright and moving forward, and penalties incurred for excessive actions and external contact forces. This research presents the first successful instance of learning under partial observability in this environment. The learned policy achieves performance comparable to state-of-the-art results with full state access, despite using only one-third to two-thirds of the original states. Moreover, the policy exhibits adaptability to robot properties, such as variations in body part masses. The key to this success is a novel history encoder that processes a fixed-length sequence of past observations in parallel. Integrated into a standard model-free algorithm, the encoder enables performance on par with fully observed baselines. We hypothesize that it reconstructs essential contextual information from recent observations, thereby enabling robust decision-making.

## 核心内容
Reinforcement learning has been widely applied to robotic control, but effective policy learning under partial observability remains a major challenge, especially in high-dimensional tasks like humanoid locomotion. To date, no prior work has demonstrated stable training of humanoid policies with incomplete state information in the benchmark Gymnasium Humanoid-v4 environment. The objective in this environment is to walk forward as fast as possible without falling, with rewards provided for staying upright and moving forward, and penalties incurred for excessive actions and external contact forces. This research presents the first successful instance of learning under partial observability in this environment. The learned policy achieves performance comparable to state-of-the-art results with full state access, despite using only one-third to two-thirds of the original states. Moreover, the policy exhibits adaptability to robot properties, such as variations in body part masses. The key to this success is a novel history encoder that processes a fixed-length sequence of past observations in parallel. Integrated into a standard model-free algorithm, the encoder enables performance on par with fully observed baselines. We hypothesize that it reconstructs essential contextual information from recent observations, thereby enabling robust decision-making.

## 参考
- http://arxiv.org/abs/2507.18883v1

## Overview
Reinforcement learning has been widely applied to robotic control, but effective policy learning under partial observability remains a major challenge, especially in high-dimensional tasks like humanoid locomotion. To date, no prior work has demonstrated stable training of humanoid policies with incomplete state information in the benchmark Gymnasium Humanoid-v4 environment. The objective in this environment is to walk forward as fast as possible without falling, with rewards provided for staying upright and moving forward, and penalties incurred for excessive actions and external contact forces. This research presents the first successful instance of learning under partial observability in this environment. The learned policy achieves performance comparable to state-of-the-art results with full state access, despite using only one-third to two-thirds of the original states. Moreover, the policy exhibits adaptability to robot properties, such as variations in body part masses. The key to this success is a novel history encoder that processes a fixed-length sequence of past observations in parallel. Integrated into a standard model-free algorithm, the encoder enables performance on par with fully observed baselines. We hypothesize that it reconstructs essential contextual information from recent observations, thereby enabling robust decision-making.

## Content
Reinforcement learning has been widely applied to robotic control, but effective policy learning under partial observability remains a major challenge, especially in high-dimensional tasks like humanoid locomotion. To date, no prior work has demonstrated stable training of humanoid policies with incomplete state information in the benchmark Gymnasium Humanoid-v4 environment. The objective in this environment is to walk forward as fast as possible without falling, with rewards provided for staying upright and moving forward, and penalties incurred for excessive actions and external contact forces. This research presents the first successful instance of learning under partial observability in this environment. The learned policy achieves performance comparable to state-of-the-art results with full state access, despite using only one-third to two-thirds of the original states. Moreover, the policy exhibits adaptability to robot properties, such as variations in body part masses. The key to this success is a novel history encoder that processes a fixed-length sequence of past observations in parallel. Integrated into a standard model-free algorithm, the encoder enables performance on par with fully observed baselines. We hypothesize that it reconstructs essential contextual information from recent observations, thereby enabling robust decision-making.

## 개요
강화 학습은 로봇 제어에 널리 적용되어 왔지만, 부분 관측 가능성 하에서의 효과적인 정책 학습은 특히 인간형 보행과 같은 고차원 작업에서 여전히 주요 과제로 남아 있습니다. 현재까지 Gymnasium Humanoid-v4 벤치마크 환경에서 불완전한 상태 정보를 사용하여 인간형 정책의 안정적인 훈련을 입증한 선행 연구는 없습니다. 이 환경의 목표는 넘어지지 않고 최대한 빠르게 앞으로 걷는 것이며, 똑바로 서서 앞으로 이동하는 데 보상이 주어지고 과도한 행동 및 외부 접촉 힘에 대해 패널티가 부과됩니다. 본 연구는 이 환경에서 부분 관측 가능성 하의 학습에 성공한 첫 번째 사례를 제시합니다. 학습된 정책은 원래 상태의 1/3에서 2/3만 사용함에도 불구하고 완전한 상태 접근이 가능한 최신 결과와 유사한 성능을 달성합니다. 또한, 정책은 신체 부위 질량 변화와 같은 로봇 속성에 대한 적응성을 보여줍니다. 이러한 성공의 핵심은 과거 관측값의 고정 길이 시퀀스를 병렬로 처리하는 새로운 히스토리 인코더입니다. 표준 모델 프리 알고리즘에 통합된 이 인코더는 완전 관측 기준선과 동등한 성능을 가능하게 합니다. 우리는 이 인코더가 최근 관측값으로부터 필수적인 맥락 정보를 재구성하여 강건한 의사 결정을 가능하게 한다고 가정합니다.

## 핵심 내용
강화 학습은 로봇 제어에 널리 적용되어 왔지만, 부분 관측 가능성 하에서의 효과적인 정책 학습은 특히 인간형 보행과 같은 고차원 작업에서 여전히 주요 과제로 남아 있습니다. 현재까지 Gymnasium Humanoid-v4 벤치마크 환경에서 불완전한 상태 정보를 사용하여 인간형 정책의 안정적인 훈련을 입증한 선행 연구는 없습니다. 이 환경의 목표는 넘어지지 않고 최대한 빠르게 앞으로 걷는 것이며, 똑바로 서서 앞으로 이동하는 데 보상이 주어지고 과도한 행동 및 외부 접촉 힘에 대해 패널티가 부과됩니다. 본 연구는 이 환경에서 부분 관측 가능성 하의 학습에 성공한 첫 번째 사례를 제시합니다. 학습된 정책은 원래 상태의 1/3에서 2/3만 사용함에도 불구하고 완전한 상태 접근이 가능한 최신 결과와 유사한 성능을 달성합니다. 또한, 정책은 신체 부위 질량 변화와 같은 로봇 속성에 대한 적응성을 보여줍니다. 이러한 성공의 핵심은 과거 관측값의 고정 길이 시퀀스를 병렬로 처리하는 새로운 히스토리 인코더입니다. 표준 모델 프리 알고리즘에 통합된 이 인코더는 완전 관측 기준선과 동등한 성능을 가능하게 합니다. 우리는 이 인코더가 최근 관측값으로부터 필수적인 맥락 정보를 재구성하여 강건한 의사 결정을 가능하게 한다고 가정합니다.
