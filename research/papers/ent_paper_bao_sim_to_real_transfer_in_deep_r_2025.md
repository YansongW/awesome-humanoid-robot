---
$id: ent_paper_bao_sim_to_real_transfer_in_deep_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion
  zh: 双足运动深度强化学习中的仿真到现实迁移
  ko: 이족 보행 심층 강화학습의 시뮬레이션-현실 전이
summary:
  en: This survey chapter examines how deep reinforcement learning policies for bipedal locomotion can be transferred from
    simulation to real robots. It maps the sources of the sim-to-real gap and organizes mitigation strategies around model-centric
    fidelity improvements and policy hardening through robustness training and online adaptation.
  zh: 本文综述了双足机器人深度强化学习策略从仿真到真实环境的迁移问题。作者分析了仿真与现实差距的主要来源，并围绕提升仿真模型保真度和增强策略鲁棒性两种互补策略，系统梳理了缓解方法。
  ko: 본 서베이 장에서는 이족 보행을 위한 심층 강화학습 정책을 시뮬레이션에서 실제 로봇으로 전이하는 방법을 다룬다. 시뮬-리얼 간극의 원인을 정리하고, 모델 중심의 충실도 향상과 강건성 훈련 및 온라인 적응을 통한
    정책 강화라는 두 축으로 해결책을 조직한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- deep_reinforcement_learning
- bipedal_locomotion
- domain_randomization
- system_identification
- residual_dynamics_learning
- teacher_student_learning
- online_adaptation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.06465v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion
  url: https://arxiv.org/abs/2511.06465
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该章节聚焦双足机器人深度强化学习中的“仿真到现实”迁移挑战。首先剖析了仿真与现实差距的四大根源：机器人动力学、接触建模、状态估计和数值求解器。在此基础上，提出了两种互补的解决思路：一是通过提升仿真模型的物理保真度来缩小差距；二是通过鲁棒性训练和在线适应来增强策略对模型误差的容忍度。最后，章节将两种思路整合为一个战略框架，为开发可靠的迁移方案提供了清晰路线图。

## 核心内容
### 核心问题与差距分析
- 双足机器人DRL策略面临“仿真诅咒”，即仿真环境与真实世界之间的系统性偏差。
- 差距主要来源于四个方面：机器人动力学参数不准确、接触/摩擦建模简化、状态估计噪声、以及数值求解器精度限制。

### 两大缓解策略
#### 1. 模型中心策略（缩小差距）
- 通过提高仿真器的物理保真度来减少迁移误差，例如更精确的动力学参数标定、接触模型校准。
- 具体方法包括系统辨识、随机化物理参数（domain randomization）等。

#### 2. 策略硬化策略（增强鲁棒性）
- 在仿真中通过鲁棒性训练（如对抗扰动、随机化环境参数）使策略对模型误差不敏感。
- 部署后通过在线适应（如模型预测控制、自适应参数调整）持续修正策略行为。

### 战略框架与结论
- 章节最终将两种策略整合为分层框架：先通过模型中心方法缩小基础差距，再通过策略硬化处理剩余不确定性。
- 该框架为双足机器人sim-to-real迁移提供了可操作的评估与开发路线图，强调两种方法需协同使用而非对立。

## Overview
This chapter addresses the critical challenge of simulation-to-reality (sim-to-real) transfer for deep reinforcement learning (DRL) in bipedal locomotion. After contextualizing the problem within various control architectures, we dissect the ``curse of simulation'' by analyzing the primary sources of sim-to-real gap: robot dynamics, contact modeling, state estimation, and numerical solvers. Building on this diagnosis, we structure the solutions around two complementary philosophies. The first is to shrink the gap through model-centric strategies that systematically improve the simulator's physical fidelity. The second is to harden the policy, a complementary approach that uses in-simulation robustness training and post-deployment adaptation to make the policy inherently resilient to model inaccuracies. The chapter concludes by synthesizing these philosophies into a strategic framework, providing a clear roadmap for developing and evaluating robust sim-to-real solutions.

## Overview
This chapter addresses the critical challenge of simulation-to-reality (sim-to-real) transfer for deep reinforcement learning (DRL) in bipedal locomotion. After contextualizing the problem within various control architectures, we dissect the "curse of simulation" by analyzing the primary sources of sim-to-real gap: robot dynamics, contact modeling, state estimation, and numerical solvers. Building on this diagnosis, we structure the solutions around two complementary philosophies. The first is to shrink the gap through model-centric strategies that systematically improve the simulator's physical fidelity. The second is to harden the policy, a complementary approach that uses in-simulation robustness training and post-deployment adaptation to make the policy inherently resilient to model inaccuracies. The chapter concludes by synthesizing these philosophies into a strategic framework, providing a clear roadmap for developing and evaluating robust sim-to-real solutions.

## Content
This chapter addresses the critical challenge of simulation-to-reality (sim-to-real) transfer for deep reinforcement learning (DRL) in bipedal locomotion. After contextualizing the problem within various control architectures, we dissect the "curse of simulation" by analyzing the primary sources of sim-to-real gap: robot dynamics, contact modeling, state estimation, and numerical solvers. Building on this diagnosis, we structure the solutions around two complementary philosophies. The first is to shrink the gap through model-centric strategies that systematically improve the simulator's physical fidelity. The second is to harden the policy, a complementary approach that uses in-simulation robustness training and post-deployment adaptation to make the policy inherently resilient to model inaccuracies. The chapter concludes by synthesizing these philosophies into a strategic framework, providing a clear roadmap for developing and evaluating robust sim-to-real solutions.

## 개요
이 장에서는 이족 보행에서 심층 강화 학습(DRL)의 시뮬레이션-현실(sim-to-real) 전환의 중요한 과제를 다룹니다. 다양한 제어 아키텍처 내에서 문제를 맥락화한 후, 로봇 동역학, 접촉 모델링, 상태 추정 및 수치 해석기 등 시뮬레이션-현실 격차의 주요 원인을 분석하여 '시뮬레이션의 저주'를 해부합니다. 이 진단을 바탕으로 두 가지 상호 보완적인 철학을 중심으로 해결책을 구성합니다. 첫 번째는 시뮬레이터의 물리적 충실도를 체계적으로 개선하는 모델 중심 전략을 통해 격차를 줄이는 것입니다. 두 번째는 정책을 강화하는 접근 방식으로, 시뮬레이션 내 강건성 훈련과 배포 후 적응을 통해 정책이 모델 부정확성에 본질적으로 저항력을 갖도록 만듭니다. 이 장은 이러한 철학을 전략적 프레임워크로 종합하여 강건한 시뮬레이션-현실 솔루션을 개발하고 평가하기 위한 명확한 로드맵을 제시하며 마무리됩니다.

## 핵심 내용
이 장에서는 이족 보행에서 심층 강화 학습(DRL)의 시뮬레이션-현실(sim-to-real) 전환의 중요한 과제를 다룹니다. 다양한 제어 아키텍처 내에서 문제를 맥락화한 후, 로봇 동역학, 접촉 모델링, 상태 추정 및 수치 해석기 등 시뮬레이션-현실 격차의 주요 원인을 분석하여 '시뮬레이션의 저주'를 해부합니다. 이 진단을 바탕으로 두 가지 상호 보완적인 철학을 중심으로 해결책을 구성합니다. 첫 번째는 시뮬레이터의 물리적 충실도를 체계적으로 개선하는 모델 중심 전략을 통해 격차를 줄이는 것입니다. 두 번째는 정책을 강화하는 접근 방식으로, 시뮬레이션 내 강건성 훈련과 배포 후 적응을 통해 정책이 모델 부정확성에 본질적으로 저항력을 갖도록 만듭니다. 이 장은 이러한 철학을 전략적 프레임워크로 종합하여 강건한 시뮬레이션-현실 솔루션을 개발하고 평가하기 위한 명확한 로드맵을 제시하며 마무리됩니다.

## 参考
- http://arxiv.org/abs/2511.06465v1
