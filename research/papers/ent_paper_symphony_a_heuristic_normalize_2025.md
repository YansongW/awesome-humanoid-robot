---
$id: ent_paper_symphony_a_heuristic_normalize_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots'
  zh: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots'
  ko: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots'
summary:
  en: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots
    is a 2025 work on locomotion for humanoid robots.'
  zh: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots
    is a 2025 work on locomotion for humanoid robots.'
  ko: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots
    is a 2025 work on locomotion for humanoid robots.'
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
- symphony
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.10477v8.
sources:
- id: src_001
  type: paper
  title: 'Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots
    (arXiv)'
  url: https://arxiv.org/abs/2512.10477
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In our work we implicitly suggest that it is a misconception to think that humans learn fast. The learning process takes time. Babies start learning to move in the restricted fluid environment of the womb. Children are often limited by underdeveloped body. Even adults are not allowed to participate in complex competitions right away. However, with robots, when learning from scratch, we often don't have the privilege of waiting for tens of millions of steps. "Swaddling" regularization is responsible for restraining an agent in rapid but unstable development penalizing action strength in a specific way not affecting actions directly. The Symphony, Transitional-policy Deterministic Actor and Critic algorithm, is a concise combination of different ideas for possibility of training humanoid robots from scratch with Sample Efficiency, Sample Proximity and Safety of Actions in mind. It is well known that continuous increase in Gaussian noise without appropriate smoothing is harmful for motors and gearboxes. Compared to Stochastic algorithms, we set limited parametric noise and promote a reduced strength of actions, safely increasing entropy, since the actions are submerged in weaker noise. When actions require more extreme values, actions rise above the weak noise. Training becomes empirically much safer for both the environment around and the robot's mechanisms. We use Fading Replay Buffer: using a fixed formula containing the hyperbolic tangent, we adjust the batch sampling probability: the memory contains a recent memory and a long-term memory trail. Fading Replay Buffer allows us to use Temporal Advantage when we improve the current Critic Network prediction compared to the exponential moving average. Temporal Advantage allows us to update the Actor and Critic in one pass, as well as combine the Actor and Critic in one Object and implement their Losses in one line.

## 核心内容
In our work we implicitly suggest that it is a misconception to think that humans learn fast. The learning process takes time. Babies start learning to move in the restricted fluid environment of the womb. Children are often limited by underdeveloped body. Even adults are not allowed to participate in complex competitions right away. However, with robots, when learning from scratch, we often don't have the privilege of waiting for tens of millions of steps. "Swaddling" regularization is responsible for restraining an agent in rapid but unstable development penalizing action strength in a specific way not affecting actions directly. The Symphony, Transitional-policy Deterministic Actor and Critic algorithm, is a concise combination of different ideas for possibility of training humanoid robots from scratch with Sample Efficiency, Sample Proximity and Safety of Actions in mind. It is well known that continuous increase in Gaussian noise without appropriate smoothing is harmful for motors and gearboxes. Compared to Stochastic algorithms, we set limited parametric noise and promote a reduced strength of actions, safely increasing entropy, since the actions are submerged in weaker noise. When actions require more extreme values, actions rise above the weak noise. Training becomes empirically much safer for both the environment around and the robot's mechanisms. We use Fading Replay Buffer: using a fixed formula containing the hyperbolic tangent, we adjust the batch sampling probability: the memory contains a recent memory and a long-term memory trail. Fading Replay Buffer allows us to use Temporal Advantage when we improve the current Critic Network prediction compared to the exponential moving average. Temporal Advantage allows us to update the Actor and Critic in one pass, as well as combine the Actor and Critic in one Object and implement their Losses in one line.

## 参考
- http://arxiv.org/abs/2512.10477v8

## Overview
In our work we implicitly suggest that it is a misconception to think that humans learn fast. The learning process takes time. Babies start learning to move in the restricted fluid environment of the womb. Children are often limited by underdeveloped body. Even adults are not allowed to participate in complex competitions right away. However, with robots, when learning from scratch, we often don't have the privilege of waiting for tens of millions of steps. "Swaddling" regularization is responsible for restraining an agent in rapid but unstable development penalizing action strength in a specific way not affecting actions directly. The Symphony, Transitional-policy Deterministic Actor and Critic algorithm, is a concise combination of different ideas for possibility of training humanoid robots from scratch with Sample Efficiency, Sample Proximity and Safety of Actions in mind. It is well known that continuous increase in Gaussian noise without appropriate smoothing is harmful for motors and gearboxes. Compared to Stochastic algorithms, we set limited parametric noise and promote a reduced strength of actions, safely increasing entropy, since the actions are submerged in weaker noise. When actions require more extreme values, actions rise above the weak noise. Training becomes empirically much safer for both the environment around and the robot's mechanisms. We use Fading Replay Buffer: using a fixed formula containing the hyperbolic tangent, we adjust the batch sampling probability: the memory contains a recent memory and a long-term memory trail. Fading Replay Buffer allows us to use Temporal Advantage when we improve the current Critic Network prediction compared to the exponential moving average. Temporal Advantage allows us to update the Actor and Critic in one pass, as well as combine the Actor and Critic in one Object and implement their Losses in one line.

## Content
In our work we implicitly suggest that it is a misconception to think that humans learn fast. The learning process takes time. Babies start learning to move in the restricted fluid environment of the womb. Children are often limited by underdeveloped body. Even adults are not allowed to participate in complex competitions right away. However, with robots, when learning from scratch, we often don't have the privilege of waiting for tens of millions of steps. "Swaddling" regularization is responsible for restraining an agent in rapid but unstable development penalizing action strength in a specific way not affecting actions directly. The Symphony, Transitional-policy Deterministic Actor and Critic algorithm, is a concise combination of different ideas for possibility of training humanoid robots from scratch with Sample Efficiency, Sample Proximity and Safety of Actions in mind. It is well known that continuous increase in Gaussian noise without appropriate smoothing is harmful for motors and gearboxes. Compared to Stochastic algorithms, we set limited parametric noise and promote a reduced strength of actions, safely increasing entropy, since the actions are submerged in weaker noise. When actions require more extreme values, actions rise above the weak noise. Training becomes empirically much safer for both the environment around and the robot's mechanisms. We use Fading Replay Buffer: using a fixed formula containing the hyperbolic tangent, we adjust the batch sampling probability: the memory contains a recent memory and a long-term memory trail. Fading Replay Buffer allows us to use Temporal Advantage when we improve the current Critic Network prediction compared to the exponential moving average. Temporal Advantage allows us to update the Actor and Critic in one pass, as well as combine the Actor and Critic in one Object and implement their Losses in one line.

## 개요
본 연구에서는 인간이 빠르게 학습한다는 생각이 오해임을 암시합니다. 학습 과정에는 시간이 필요합니다. 아기들은 자궁이라는 제한된 유체 환경에서 움직이는 법을 배우기 시작합니다. 아이들은 종종 미성숙한 신체로 인해 제약을 받습니다. 심지어 성인도 복잡한 경기에 즉시 참여할 수 없습니다. 그러나 로봇의 경우, 처음부터 학습할 때 수천만 스텝을 기다릴 특권이 없는 경우가 많습니다. "포대기(Swaddling)" 정규화는 급속하지만 불안정한 발전 과정에서 에이전트를 제한하며, 행동 강도에 특정 방식으로 패널티를 부여하되 행동 자체에는 직접 영향을 미치지 않습니다. Symphony, 즉 전이 정책 결정론적 행위자 및 비평가(Transitional-policy Deterministic Actor and Critic) 알고리즘은 샘플 효율성, 샘플 근접성 및 행동 안전성을 고려하여 휴머노이드 로봇을 처음부터 훈련할 가능성을 위한 다양한 아이디어의 간결한 조합입니다. 적절한 평활화 없이 가우시안 노이즈를 지속적으로 증가시키는 것이 모터와 기어박스에 해롭다는 것은 잘 알려져 있습니다. 확률적 알고리즘과 비교하여, 우리는 제한된 파라미터 노이즈를 설정하고 행동 강도를 줄여 안전하게 엔트로피를 증가시킵니다. 이는 행동이 약한 노이즈에 잠기기 때문입니다. 행동이 더 극단적인 값을 필요로 할 때, 행동은 약한 노이즈 위로 올라갑니다. 훈련은 주변 환경과 로봇 메커니즘 모두에 대해 경험적으로 훨씬 더 안전해집니다. 우리는 페이딩 리플레이 버퍼(Fading Replay Buffer)를 사용합니다: 하이퍼볼릭 탄젠트를 포함한 고정된 공식을 사용하여 배치 샘플링 확률을 조정합니다. 메모리는 최근 메모리와 장기 메모리 흔적을 포함합니다. 페이딩 리플레이 버퍼를 통해 지수 이동 평균과 비교하여 현재 비평가 네트워크 예측을 개선할 때 시간적 이점(Temporal Advantage)을 사용할 수 있습니다. 시간적 이점을 통해 행위자와 비평가를 한 번에 업데이트하고, 행위자와 비평가를 하나의 객체로 결합하며, 손실 함수를 한 줄로 구현할 수 있습니다.

## 핵심 내용
본 연구에서는 인간이 빠르게 학습한다는 생각이 오해임을 암시합니다. 학습 과정에는 시간이 필요합니다. 아기들은 자궁이라는 제한된 유체 환경에서 움직이는 법을 배우기 시작합니다. 아이들은 종종 미성숙한 신체로 인해 제약을 받습니다. 심지어 성인도 복잡한 경기에 즉시 참여할 수 없습니다. 그러나 로봇의 경우, 처음부터 학습할 때 수천만 스텝을 기다릴 특권이 없는 경우가 많습니다. "포대기(Swaddling)" 정규화는 급속하지만 불안정한 발전 과정에서 에이전트를 제한하며, 행동 강도에 특정 방식으로 패널티를 부여하되 행동 자체에는 직접 영향을 미치지 않습니다. Symphony, 즉 전이 정책 결정론적 행위자 및 비평가(Transitional-policy Deterministic Actor and Critic) 알고리즘은 샘플 효율성, 샘플 근접성 및 행동 안전성을 고려하여 휴머노이드 로봇을 처음부터 훈련할 가능성을 위한 다양한 아이디어의 간결한 조합입니다. 적절한 평활화 없이 가우시안 노이즈를 지속적으로 증가시키는 것이 모터와 기어박스에 해롭다는 것은 잘 알려져 있습니다. 확률적 알고리즘과 비교하여, 우리는 제한된 파라미터 노이즈를 설정하고 행동 강도를 줄여 안전하게 엔트로피를 증가시킵니다. 이는 행동이 약한 노이즈에 잠기기 때문입니다. 행동이 더 극단적인 값을 필요로 할 때, 행동은 약한 노이즈 위로 올라갑니다. 훈련은 주변 환경과 로봇 메커니즘 모두에 대해 경험적으로 훨씬 더 안전해집니다. 우리는 페이딩 리플레이 버퍼(Fading Replay Buffer)를 사용합니다: 하이퍼볼릭 탄젠트를 포함한 고정된 공식을 사용하여 배치 샘플링 확률을 조정합니다. 메모리는 최근 메모리와 장기 메모리 흔적을 포함합니다. 페이딩 리플레이 버퍼를 통해 지수 이동 평균과 비교하여 현재 비평가 네트워크 예측을 개선할 때 시간적 이점(Temporal Advantage)을 사용할 수 있습니다. 시간적 이점을 통해 행위자와 비평가를 한 번에 업데이트하고, 행위자와 비평가를 하나의 객체로 결합하며, 손실 함수를 한 줄로 구현할 수 있습니다.
