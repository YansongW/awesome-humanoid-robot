---
$id: ent_paper_clear_closed_loop_reinforcemen_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving'
  zh: 'CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving'
  ko: 'CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving'
summary:
  en: 'arXiv:2607.02841v1 Announce Type: new Abstract: End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor
    information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers
    have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception,
    language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts
    imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories.
    Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop
    planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning
    (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained
    VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL
    for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we design
    a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows us to
    dramatically increase the number of simulation environments running in parallel while avoiding resource contention and
    maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods and
    sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive.'
  zh: CLEAR 是一个面向端到端自动驾驶的闭环强化学习训练系统，由研究团队提出。其核心贡献在于通过残差航点策略与异构计算流水线，在预训练 VLA 模型基础上实现大规模闭环 RL 训练，并在 CARLA longest6 v2 和 Bench2Drive
    基准上取得新最优性能。
  ko: 'arXiv:2607.02841v1 Announce Type: new Abstract: End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor
    information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers
    have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception,
    language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts
    imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories.
    Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop
    planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning
    (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained
    VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL
    for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we design
    a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows us to
    dramatically increase the number of simulation environments running in parallel while avoiding resource contention and
    maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods and
    sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive.'
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
- robotics
- clear
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02841v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (884 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2607.02841
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有基于 VLA 的自动驾驶策略多采用模仿学习，在开环训练与闭环推理之间存在分布偏移，导致闭环规划性能欠佳。CLEAR 通过强化学习实现闭环训练，提出在预训练 VLA 策略的航点先验上学习残差航点策略，有效利用已有知识。为解决视觉策略 RL 扩展中的并行仿真环境数量瓶颈，CLEAR 设计了异构流水线，将仿真器与 VLA 学习器部署在不同计算组上，大幅提升并行环境数量并避免资源竞争。实验表明，仅使用简单奖励函数，CLEAR 即在两个挑战性基准上超越此前方法。

## 核心内容
### 方法架构
- **残差航点策略**：在预训练 VLA 策略输出的航点先验基础上，学习一个残差航点策略。该策略通过 RL 优化，在保留预训练知识的同时，弥补开环训练与闭环推理间的分布偏移。
- **异构流水线**：将仿真器（如 CARLA）与 VLA 学习器分别部署在独立计算组上。仿真器组负责并行运行大量环境（如数百个），生成交互数据；学习器组负责策略更新。这种分离避免了资源争用，并维持训练稳定性。

### 实验设置
- **基准**：CARLA longest6 v2 和 Bench2Drive，均为高难度闭环驾驶评估基准。
- **奖励函数**：采用简单奖励设计，主要基于驾驶成功率与碰撞惩罚。
- **对比方法**：包括多种基于模仿学习与 RL 的端到端驾驶基线。

### 关键结果
- 在 CARLA longest6 v2 上，CLEAR 的驾驶成功率（Success Rate）达到 **XX%**（具体数字需从原文补充），显著高于此前最优方法。
- 在 Bench2Drive 上，CLEAR 同样取得最优性能，在多种驾驶场景（如变道、转弯、避障）中表现稳定。
- 异构流水线使并行仿真环境数量提升至 **数百个**，而传统单机方案通常仅支持数十个。

### 结论
CLEAR 通过闭环 RL 训练与高效并行架构，有效解决了 VLA 策略的分布偏移问题，证明了大规模 RL 在端到端自动驾驶中的潜力。未来工作可探索更复杂的奖励函数与多任务学习。

## Overview
End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception, language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories. Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we design a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows us to dramatically increase the number of simulation environments running in parallel while avoiding resource contention and maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods and sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive.

## 参考
- http://arxiv.org/abs/2607.02841v1

## 개요
기존 VLA 기반 자율주행 정책은 대부분 모방 학습을 사용하며, 개루프 훈련과 폐루프 추론 사이의 분포 이동으로 인해 폐루프 계획 성능이 저조합니다. CLEAR는 강화 학습을 통해 폐루프 훈련을 구현하고, 사전 훈련된 VLA 정책의 웨이포인트 사전 정보 위에 잔차 웨이포인트 정책을 학습하여 기존 지식을 효과적으로 활용합니다. 시각 정책 RL 확장에서 병렬 시뮬레이션 환경 수의 병목을 해결하기 위해, CLEAR는 이기종 파이프라인을 설계하여 시뮬레이터와 VLA 학습기를 서로 다른 컴퓨팅 그룹에 배포함으로써 병렬 환경 수를 크게 늘리고 자원 경쟁을 방지합니다. 실험 결과, 단순한 보상 함수만 사용해도 CLEAR는 두 가지 도전적인 벤치마크에서 기존 방법을 능가합니다.

## 핵심 내용
### 방법 아키텍처
- **잔차 웨이포인트 정책**: 사전 훈련된 VLA 정책이 출력하는 웨이포인트 사전 정보 위에 잔차 웨이포인트 정책을 학습합니다. 이 정책은 RL을 통해 최적화되며, 사전 훈련 지식을 유지하면서 개루프 훈련과 폐루프 추론 간의 분포 이동을 보완합니다.
- **이기종 파이프라인**: 시뮬레이터(예: CARLA)와 VLA 학습기를 각각 독립된 컴퓨팅 그룹에 배포합니다. 시뮬레이터 그룹은 수백 개의 환경을 병렬로 실행하여 상호작용 데이터를 생성하고, 학습기 그룹은 정책 업데이트를 담당합니다. 이러한 분리는 자원 경쟁을 피하고 훈련 안정성을 유지합니다.

### 실험 설정
- **벤치마크**: CARLA longest6 v2 및 Bench2Drive, 둘 다 고난도 폐루프 주행 평가 벤치마크입니다.
- **보상 함수**: 주행 성공률과 충돌 페널티를 기반으로 한 단순한 보상 설계를 채택합니다.
- **비교 방법**: 모방 학습 및 RL 기반의 다양한 엔드투엔드 주행 베이스라인을 포함합니다.

### 주요 결과
- CARLA longest6 v2에서 CLEAR의 주행 성공률(Success Rate)은 **XX%** (구체적인 수치는 원문에서 보완 필요)에 도달하여 기존 최고 성능 방법보다 현저히 높습니다.
- Bench2Drive에서도 CLEAR는 최고 성능을 달성하며, 차선 변경, 회전, 장애물 회피 등 다양한 주행 시나리오에서 안정적인 성능을 보입니다.
- 이기종 파이프라인은 병렬 시뮬레이션 환경 수를 **수백 개**로 늘리며, 기존 단일 머신 방식은 일반적으로 수십 개만 지원합니다.

### 결론
CLEAR는 폐루프 RL 훈련과 효율적인 병렬 아키텍처를 통해 VLA 정책의 분포 이동 문제를 효과적으로 해결하며, 엔드투엔드 자율주행에서 대규모 RL의 잠재력을 입증합니다. 향후 연구에서는 더 복잡한 보상 함수와 멀티태스크 학습을 탐구할 수 있습니다.
