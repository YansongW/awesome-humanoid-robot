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
  zh: Symphony 是一种针对人形机器人运动控制的新型强化学习算法，由研究团队于2025年提出。其核心贡献在于通过“襁褓正则化”、衰减回放缓冲区和时间优势机制，实现了从零开始高效、安全地训练人形机器人，并显著提升了样本效率与动作安全性。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.10477v8. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (947 chars, DeepSeek).'
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
该算法挑战了“人类学习速度快”的常见认知，指出婴儿和儿童的学习过程漫长且受限于身体发育，而机器人训练无法等待数千万步的迭代。Symphony 算法通过“襁褓正则化”约束智能体在快速但不稳定的发展中的动作强度，同时结合有限参数噪声与动作强度抑制，安全地增加熵值，避免对电机和齿轮箱造成损害。其衰减回放缓冲区利用双曲正切公式调整批次采样概率，融合近期记忆与长期记忆轨迹，并借助时间优势机制实现演员与评论家网络的一步更新，将损失函数整合为单行代码。

## 核心内容
### 核心思想与动机
- 人类学习并非天生高效：婴儿在子宫的受限流体环境中开始学习运动，儿童受限于未发育完全的身体，成年人也无法立即参与复杂竞赛。机器人从零学习时，无法等待数千万步的迭代。
- 传统强化学习在机器人训练中面临样本效率低、动作不稳定、硬件易损等问题。

### 算法架构：Symphony
- **襁褓正则化**：通过特定方式惩罚动作强度，但不直接影响动作本身，从而约束智能体在快速但不稳定的发展中的行为，类似于婴儿被襁褓包裹以限制过度活动。
- **有限参数噪声与动作强度抑制**：与随机算法不同，Symphony 设置有限的参数噪声，并促进动作强度降低。当动作需要极端值时，其信号会超越弱噪声，从而安全地增加熵值。训练对环境和机器人机械结构均更安全。
- **衰减回放缓冲区**：使用包含双曲正切的固定公式调整批次采样概率。缓冲区同时包含近期记忆和长期记忆轨迹，使算法能利用时间优势。
- **时间优势机制**：通过比较当前评论家网络预测与指数移动平均，计算时间优势。该机制允许演员与评论家网络在一次前向传播中同时更新，并将两者整合为同一对象，损失函数仅需一行代码实现。

### 实验设置与关键结果
- 实验针对人形机器人从零开始的运动控制任务。
- 关键指标：样本效率（Sample Efficiency）、样本邻近性（Sample Proximity）、动作安全性（Safety of Actions）。
- 与随机算法对比，Symphony 在训练过程中显著降低了电机和齿轮箱的机械磨损风险。
- 衰减回放缓冲区与时间优势的结合，使算法在单次更新中同时优化演员和评论家网络，大幅提升训练效率。

## Overview
In our work we implicitly suggest that it is a misconception to think that humans learn fast. The learning process takes time. Babies start learning to move in the restricted fluid environment of the womb. Children are often limited by underdeveloped body. Even adults are not allowed to participate in complex competitions right away. However, with robots, when learning from scratch, we often don't have the privilege of waiting for tens of millions of steps. "Swaddling" regularization is responsible for restraining an agent in rapid but unstable development penalizing action strength in a specific way not affecting actions directly. The Symphony, Transitional-policy Deterministic Actor and Critic algorithm, is a concise combination of different ideas for possibility of training humanoid robots from scratch with Sample Efficiency, Sample Proximity and Safety of Actions in mind. It is well known that continuous increase in Gaussian noise without appropriate smoothing is harmful for motors and gearboxes. Compared to Stochastic algorithms, we set limited parametric noise and promote a reduced strength of actions, safely increasing entropy, since the actions are submerged in weaker noise. When actions require more extreme values, actions rise above the weak noise. Training becomes empirically much safer for both the environment around and the robot's mechanisms. We use Fading Replay Buffer: using a fixed formula containing the hyperbolic tangent, we adjust the batch sampling probability: the memory contains a recent memory and a long-term memory trail. Fading Replay Buffer allows us to use Temporal Advantage when we improve the current Critic Network prediction compared to the exponential moving average. Temporal Advantage allows us to update the Actor and Critic in one pass, as well as combine the Actor and Critic in one Object and implement their Losses in one line.

## 参考
- http://arxiv.org/abs/2512.10477v8

## 개요
이 알고리즘은 "인간의 학습 속도가 빠르다"는 일반적인 인식을 반박하며, 유아와 아동의 학습 과정은 길고 신체 발달에 제약을 받는다는 점을 지적한다. 로봇 훈련은 수천만 스텝의 반복을 기다릴 수 없다. Symphony 알고리즘은 "포대기 정규화(襁褓正则化)"를 통해 빠르지만 불안정한 발달 과정에서 에이전트의 행동 강도를 제약하며, 유한 파라미터 노이즈와 행동 강도 억제를 결합해 안전하게 엔트로피를 증가시키고 모터와 기어박스의 손상을 방지한다. 감쇠 리플레이 버퍼는 쌍곡탄젠트 공식을 사용해 배치 샘플링 확률을 조정하며, 최근 기억과 장기 기억 궤적을 융합하고, 시간 우위 메커니즘을 통해 액터와 크리틱 네트워크의 단일 스텝 업데이트를 구현하여 손실 함수를 한 줄의 코드로 통합한다.

## 핵심 내용
### 핵심 아이디어와 동기
- 인간의 학습은 본래 효율적이지 않다: 유아는 자궁 내 제한된 유체 환경에서 운동 학습을 시작하며, 아동은 미성숙한 신체에 제약을 받고, 성인도 즉시 복잡한 경기에 참여할 수 없다. 로봇이 처음부터 학습할 때 수천만 스텝의 반복을 기다릴 수 없다.
- 전통적인 강화 학습은 로봇 훈련에서 샘플 효율성 저하, 불안정한 행동, 하드웨어 손상 가능성 등의 문제를 겪는다.

### 알고리즘 아키텍처: Symphony
- **포대기 정규화**: 특정 방식으로 행동 강도를 페널티하지만 행동 자체에는 직접 영향을 주지 않아, 빠르지만 불안정한 발달 과정에서 에이전트의 행동을 제약한다. 이는 유아가 과도한 활동을 제한하기 위해 포대기에 싸이는 것과 유사하다.
- **유한 파라미터 노이즈와 행동 강도 억제**: 무작위 알고리즘과 달리 Symphony는 유한한 파라미터 노이즈를 설정하고 행동 강도 감소를 촉진한다. 행동이 극단적인 값을 필요로 할 때 그 신호는 약한 노이즈를 초과하여 안전하게 엔트로피를 증가시킨다. 훈련은 환경과 로봇 기계 구조 모두에 더 안전하다.
- **감쇠 리플레이 버퍼**: 쌍곡탄젠트를 포함한 고정 공식을 사용해 배치 샘플링 확률을 조정한다. 버퍼는 최근 기억과 장기 기억 궤적을 동시에 포함하여 알고리즘이 시간 우위를 활용할 수 있게 한다.
- **시간 우위 메커니즘**: 현재 크리틱 네트워크 예측과 지수 이동 평균을 비교하여 시간 우위를 계산한다. 이 메커니즘은 액터와 크리틱 네트워크가 단일 전방 전파에서 동시에 업데이트되도록 하며, 둘을 동일한 객체로 통합하여 손실 함수를 한 줄의 코드로 구현한다.

### 실험 설정과 주요 결과
- 실험은 휴머노이드 로봇의 처음부터 시작하는 운동 제어 작업을 대상으로 한다.
- 주요 지표: 샘플 효율성(Sample Efficiency), 샘플 근접성(Sample Proximity), 행동 안전성(Safety of Actions).
- 무작위 알고리즘과 비교하여 Symphony는 훈련 과정에서 모터와 기어박스의 기계적 마모 위험을 크게 줄였다.
- 감쇠 리플레이 버퍼와 시간 우위의 결합은 알고리즘이 단일 업데이트에서 액터와 크리틱 네트워크를 동시에 최적화하여 훈련 효율성을 크게 향상시킨다.
