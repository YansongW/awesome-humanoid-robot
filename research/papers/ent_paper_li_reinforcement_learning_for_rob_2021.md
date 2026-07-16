---
$id: ent_paper_li_reinforcement_learning_for_rob_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Learning for Robust Parameterized Locomotion Control of Bipedal Robots
  zh: 用于双足机器人鲁棒参数化运动控制的强化学习
  ko: 이족 보행 로봇의 강건한 매개변수화 보행 제어를 위한 강화학습
summary:
  en: Presents a model-free reinforcement learning framework that combines an HZD gait library with PPO and curriculum-based
    dynamics randomization to train robust sim-to-real locomotion policies for the Cassie bipedal robot, enabling tracking
    of target walking velocity, height, and yaw without residual control.
  zh: 提出一种无模型强化学习框架，将混合零动态（HZD）步态库与PPO及课程式动力学随机化结合，在仿真中训练可迁移到真实Cassie双足机器人的鲁棒运动策略，实现无需残差控制的目标行走速度、高度与偏航跟踪。
  ko: HZD 보행 라이브러리와 PPO 및 커리큘럼 기반 동역학 랜덤화를 결합한 모델-프리 강화학습 프레임워크를 제안하여, Cassie 실제 이족 로봇으로 시뮬레이션-투-리얼 전이가 가능한 강건한 보행 정책을 학습하고
    잔차 제어 없이 목표 보행 속도·높이·선회를 추적한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- reinforcement_learning
- bipedal_locomotion
- sim_to_real
- domain_randomization
- proximal_policy_optimization
- hybrid_zero_dynamics
- cassie
- locomotion_control
- robot_locomotion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2103.14295v1.
sources:
- id: src_001
  type: paper
  title: Reinforcement Learning for Robust Parameterized Locomotion Control of Bipedal Robots
  url: https://arxiv.org/abs/2103.14295
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Developing robust walking controllers for bipedal robots is a challenging endeavor. Traditional model-based locomotion controllers require simplifying assumptions and careful modelling; any small errors can result in unstable control. To address these challenges for bipedal locomotion, we present a model-free reinforcement learning framework for training robust locomotion policies in simulation, which can then be transferred to a real bipedal Cassie robot. To facilitate sim-to-real transfer, domain randomization is used to encourage the policies to learn behaviors that are robust across variations in system dynamics. The learned policies enable Cassie to perform a set of diverse and dynamic behaviors, while also being more robust than traditional controllers and prior learning-based methods that use residual control. We demonstrate this on versatile walking behaviors such as tracking a target walking velocity, walking height, and turning yaw.

## 核心内容
Developing robust walking controllers for bipedal robots is a challenging endeavor. Traditional model-based locomotion controllers require simplifying assumptions and careful modelling; any small errors can result in unstable control. To address these challenges for bipedal locomotion, we present a model-free reinforcement learning framework for training robust locomotion policies in simulation, which can then be transferred to a real bipedal Cassie robot. To facilitate sim-to-real transfer, domain randomization is used to encourage the policies to learn behaviors that are robust across variations in system dynamics. The learned policies enable Cassie to perform a set of diverse and dynamic behaviors, while also being more robust than traditional controllers and prior learning-based methods that use residual control. We demonstrate this on versatile walking behaviors such as tracking a target walking velocity, walking height, and turning yaw.

## 参考
- http://arxiv.org/abs/2103.14295v1

## Overview
Developing robust walking controllers for bipedal robots is a challenging endeavor. Traditional model-based locomotion controllers require simplifying assumptions and careful modelling; any small errors can result in unstable control. To address these challenges for bipedal locomotion, we present a model-free reinforcement learning framework for training robust locomotion policies in simulation, which can then be transferred to a real bipedal Cassie robot. To facilitate sim-to-real transfer, domain randomization is used to encourage the policies to learn behaviors that are robust across variations in system dynamics. The learned policies enable Cassie to perform a set of diverse and dynamic behaviors, while also being more robust than traditional controllers and prior learning-based methods that use residual control. We demonstrate this on versatile walking behaviors such as tracking a target walking velocity, walking height, and turning yaw.

## Content
Developing robust walking controllers for bipedal robots is a challenging endeavor. Traditional model-based locomotion controllers require simplifying assumptions and careful modelling; any small errors can result in unstable control. To address these challenges for bipedal locomotion, we present a model-free reinforcement learning framework for training robust locomotion policies in simulation, which can then be transferred to a real bipedal Cassie robot. To facilitate sim-to-real transfer, domain randomization is used to encourage the policies to learn behaviors that are robust across variations in system dynamics. The learned policies enable Cassie to perform a set of diverse and dynamic behaviors, while also being more robust than traditional controllers and prior learning-based methods that use residual control. We demonstrate this on versatile walking behaviors such as tracking a target walking velocity, walking height, and turning yaw.

## 개요
이족 보행 로봇을 위한 강건한 보행 제어기를 개발하는 것은 도전적인 과제입니다. 전통적인 모델 기반 보행 제어기는 단순화된 가정과 세심한 모델링을 필요로 하며, 작은 오류라도 불안정한 제어로 이어질 수 있습니다. 이러한 이족 보행의 문제를 해결하기 위해, 우리는 시뮬레이션에서 강건한 보행 정책을 학습시키고 이를 실제 이족 보행 로봇 Cassie에 전이할 수 있는 모델 프리 강화 학습 프레임워크를 제시합니다. 시뮬레이션-실제 전이를 용이하게 하기 위해, 도메인 무작위화를 사용하여 시스템 동역학의 변동에 걸쳐 강건한 행동을 학습하도록 정책을 유도합니다. 학습된 정책은 Cassie가 다양하고 역동적인 행동을 수행할 수 있게 하며, 전통적인 제어기나 잔여 제어를 사용하는 이전의 학습 기반 방법보다 더 강건합니다. 우리는 목표 보행 속도, 보행 높이 및 회전 요(yaw) 추적과 같은 다양한 보행 행동에서 이를 입증합니다.

## 핵심 내용
이족 보행 로봇을 위한 강건한 보행 제어기를 개발하는 것은 도전적인 과제입니다. 전통적인 모델 기반 보행 제어기는 단순화된 가정과 세심한 모델링을 필요로 하며, 작은 오류라도 불안정한 제어로 이어질 수 있습니다. 이러한 이족 보행의 문제를 해결하기 위해, 우리는 시뮬레이션에서 강건한 보행 정책을 학습시키고 이를 실제 이족 보행 로봇 Cassie에 전이할 수 있는 모델 프리 강화 학습 프레임워크를 제시합니다. 시뮬레이션-실제 전이를 용이하게 하기 위해, 도메인 무작위화를 사용하여 시스템 동역학의 변동에 걸쳐 강건한 행동을 학습하도록 정책을 유도합니다. 학습된 정책은 Cassie가 다양하고 역동적인 행동을 수행할 수 있게 하며, 전통적인 제어기나 잔여 제어를 사용하는 이전의 학습 기반 방법보다 더 강건합니다. 우리는 목표 보행 속도, 보행 높이 및 회전 요(yaw) 추적과 같은 다양한 보행 행동에서 이를 입증합니다.
