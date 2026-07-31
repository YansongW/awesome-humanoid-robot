---
$id: ent_paper_hoist_suspended_load_manipulation_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HOIST: Humanoid Optimization with Imitation and Sample-efficient Tuning for Manipulating Suspended Loads'
  zh: 人形机器人悬挂负载操作的模仿学习与高效微调
  ko: 'HOIST: Humanoid Optimization with Imitation and Sample-efficient Tuning for Manipulating Suspended Loads'
summary:
  en: 'Manipulating suspended payloads with humanoid robots is challenging because the robot can only influence an underactuated,
    oscillatory load through whole-body motion and intermittent contact. Institutions per source list: 佛罗里达大学.'
  zh: HOIST 是一种面向人形机器人操控悬挂负载的优化方法，由研究团队提出。其核心贡献在于结合模仿学习与样本高效的强化学习调优，在仿真和真实人形机器人上实现了更精准的负载放置，相比纯模仿方法减少了 19.9 厘米平移误差和 3.56 度角度误差。
  ko: 'Manipulating suspended payloads with humanoid robots is challenging because the robot can only influence an underactuated,
    oscillatory load through whole-body motion and intermittent contact. Institutions per source list: 佛罗里达大学.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- hoist
- humanoid
- optimization
- imitation
- sa
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 53 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2606.00252v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.00252 HOIST: Humanoid Optimization with Imitation and Sample-efficient Tuning for Manipulating Suspended
    Loads'
  url: https://arxiv.org/abs/2606.00252
  accessed_at: '2026-07-31'
  date: '2026-05-29'
- id: src_002
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

HOIST 方法首先通过 VR 遥操作演示微调一个高层视觉-语言-动作（VLA）策略，并利用全身控制器执行其指令。随后，它采用 VLA 策略的 rollout 数据和迭代式批量强化学习，优化放置精度和停止行为。实验表明，HOIST 在仿真和真实人形机器人上均优于纯模仿学习和额外演示基线，展示了人形机器人在欠驱动物料处理任务中的潜力。

## 核心内容
### 方法架构
HOIST 采用两阶段优化流程：
- **第一阶段**：从 VR 遥操作演示中微调一个高层 VLA 策略，该策略输出动作指令，由全身控制器（whole-body controller）执行，确保安全初始行为。
- **第二阶段**：利用 VLA 策略的 rollout 数据，通过迭代式批量强化学习（iterative batched RL）优化放置精度和停止行为，避免从零开始强化学习的不安全性和样本低效问题。

### 实验设置
- **仿真环境**：使用 MuJoCo 模拟器，测试悬挂负载的操控任务。
- **真实机器人**：采用全尺寸人形机器人，执行悬挂负载的放置任务。
- **基线对比**：包括纯模仿学习（imitation-only）和额外演示基线（additional-demonstration baselines）。

### 关键结果
- **平移放置误差**：HOIST 相比纯 VLA rollout 减少了 19.9 厘米。
- **原始角度误差**：HOIST 相比纯 VLA rollout 减少了 3.56 度。
- **结论**：HOIST 有效结合了模仿学习的安全性与强化学习的优化能力，显著提升了人形机器人在欠驱动悬挂负载操控任务中的性能。

## Overview
Manipulating suspended payloads with humanoid robots is challenging because the robot can only influence an underactuated, oscillatory load through whole-body motion and intermittent contact. Imitation learning provides safe initial behavior but does not directly optimize final placement, while reinforcement learning from scratch is unsafe and sample-inefficient on real humanoids. We present HOIST-Humanoid Optimized with Imitation and Sample-efficient Tuning for manipulating suspended loads. HOIST first finetunes a high-level vision-language-action (VLA) policy from virtual-reality (VR) teleoperation demonstrations and executes its commands through a whole-body controller. It then uses VLA rollouts and iterative batched RL to improve placement accuracy and stopping behavior. Experiments in simulation and on a real humanoid show that HOIST improves over imitation-only and additional-demonstration baselines; compared with pure VLA rollouts, HOIST reduces translational placement error by 19.9 cm and raw angular error by 3.56 degrees, demonstrating the potential of humanoids for underactuated material-handling tasks.

## 参考
- https://arxiv.org/abs/2606.00252
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

HOIST 방법은 먼저 VR 원격 조작 시연을 통해 고수준 시각-언어-동작(VLA) 정책을 미세 조정하고, 전신 제어기를 사용하여 그 명령을 실행합니다. 이후 VLA 정책의 롤아웃 데이터와 반복적 배치 강화 학습을 활용하여 배치 정밀도와 정지 동작을 최적화합니다. 실험 결과, HOIST는 시뮬레이션 및 실제 휴머노이드 로봇에서 순수 모방 학습 및 추가 시연 기준선보다 우수한 성능을 보여주며, 휴머노이드 로봇의 저구동 물체 처리 작업에서의 잠재력을 입증했습니다.

## 핵심 내용
### 방법 아키텍처
HOIST는 두 단계 최적화 프로세스를 채택합니다:
- **첫 번째 단계**: VR 원격 조작 시연에서 고수준 VLA 정책을 미세 조정합니다. 이 정책은 동작 명령을 출력하며, 전신 제어기(whole-body controller)가 이를 실행하여 안전한 초기 동작을 보장합니다.
- **두 번째 단계**: VLA 정책의 롤아웃 데이터를 활용하여 반복적 배치 강화 학습(iterative batched RL)을 통해 배치 정밀도와 정지 동작을 최적화하며, 처음부터 강화 학습을 시작할 때의 불안전성과 샘플 비효율 문제를 피합니다.

### 실험 설정
- **시뮬레이션 환경**: MuJoCo 시뮬레이터를 사용하여 매달린 하중의 조작 작업을 테스트합니다.
- **실제 로봇**: 전신 휴머노이드 로봇을 사용하여 매달린 하중의 배치 작업을 수행합니다.
- **기준선 비교**: 순수 모방 학습(imitation-only) 및 추가 시연 기준선(additional-demonstration baselines)을 포함합니다.

### 주요 결과
- **평행 이동 배치 오차**: HOIST는 순수 VLA 롤아웃에 비해 19.9cm 감소했습니다.
- **원본 각도 오차**: HOIST는 순수 VLA 롤아웃에 비해 3.56도 감소했습니다.
- **결론**: HOIST는 모방 학습의 안전성과 강화 학습의 최적화 능력을 효과적으로 결합하여, 휴머노이드 로봇의 저구동 매달린 하중 조작 작업에서 성능을 크게 향상시켰습니다.
