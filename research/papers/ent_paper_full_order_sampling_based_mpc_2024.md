---
$id: ent_paper_full_order_sampling_based_mpc_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing
  zh: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing
  ko: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing
summary:
  en: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: DIAL-MPC 是一种基于采样的模型预测控制框架，通过扩散式退火过程实现足式机器人的全阶动力学实时优化。该工作由相关研究团队于2024年提出，核心贡献在于将扩散模型的退火思想引入MPC，在无需训练的情况下将标准MPPI的跟踪误差降低13.4倍，并在攀爬任务中超越强化学习策略50%。
  ko: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- full_order_sampling_based_mpc
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.15610v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing (arXiv)
  url: https://arxiv.org/abs/2409.15610
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
针对足式机器人全阶动力学模型的高维非凸优化难题，现有NMPC方法多局限于降阶模型，而采样类MPC虽能处理非连续问题却存在高方差次优解。DIAL-MPC创新性地融合扩散模型退火机制，通过理论分析建立MPPI与单步扩散的数学联系，设计出兼顾全局探索与局部收敛的迭代优化算法。在四足机器人实验中，该方法在扭矩级控制任务中展现出显著优势：标准MPPI的跟踪误差被压缩至1/13.4，无训练条件下攀爬性能超越RL策略50%，并首次实现带负载的精准跳跃控制。

## 核心内容
### 方法架构
- **核心机制**：DIAL-MPC将扩散模型的退火过程引入采样型MPC，通过逐步降低噪声方差实现从全局探索到局部收敛的平滑过渡
- **理论支撑**：基于MPPI（Model Predictive Path Integral Control）的损失景观分析，建立MPPI与单步扩散过程的数学等价关系
- **算法流程**：在线迭代优化时，每个控制周期内执行多轮带退火策略的采样-评估-重采样循环

### 实验设置
- **控制对象**：四足机器人扭矩级控制，包含基础运动、攀爬、跳跃等任务
- **对比基准**：标准MPPI、强化学习策略（RL）
- **硬件平台**：真实四足机器人平台，含负载跳跃实验

### 关键性能数据
- **跟踪误差**：相比标准MPPI降低13.4倍
- **攀爬任务**：无训练条件下成功率比RL策略高50%
- **跳跃能力**：首次实现真实四足机器人带负载精准跳跃
- **实时性**：在完整四足动力学模型上实现实时优化，无需预训练

### 结论
DIAL-MPC作为首个无需训练的实时全阶四足动力学优化方法，通过扩散式退火机制有效解决了高维非凸优化难题，在扭矩级控制任务中同时实现了全局搜索能力和局部收敛精度，为足式机器人全身控制提供了新范式。

## Overview
Due to high dimensionality and non-convexity, real-time optimal control using full-order dynamics models for legged robots is challenging. Therefore, Nonlinear Model Predictive Control (NMPC) approaches are often limited to reduced-order models. Sampling-based MPC has shown potential in nonconvex even discontinuous problems, but often yields suboptimal solutions with high variance, which limits its applications in high-dimensional locomotion. This work introduces DIAL-MPC (Diffusion-Inspired Annealing for Legged MPC), a sampling-based MPC framework with a novel diffusion-style annealing process. Such an annealing process is supported by the theoretical landscape analysis of Model Predictive Path Integral Control (MPPI) and the connection between MPPI and single-step diffusion. Algorithmically, DIAL-MPC iteratively refines solutions online and achieves both global coverage and local convergence. In quadrupedal torque-level control tasks, DIAL-MPC reduces the tracking error of standard MPPI by $13.4$ times and outperforms reinforcement learning (RL) policies by $50\%$ in challenging climbing tasks without any training. In particular, DIAL-MPC enables precise real-world quadrupedal jumping with payload. To the best of our knowledge, DIAL-MPC is the first training-free method that optimizes over full-order quadruped dynamics in real-time.

## 개요
고차원성과 비볼록성으로 인해, 보행 로봇의 전차수 동역학 모델을 사용한 실시간 최적 제어는 어렵습니다. 따라서 비선형 모델 예측 제어(NMPC) 접근법은 종종 축소 차수 모델로 제한됩니다. 샘플링 기반 MPC는 비볼록, 심지어 불연속적인 문제에서 잠재력을 보여주었지만, 높은 분산을 가진 차선의 해를 산출하는 경우가 많아 고차원 보행에서의 응용이 제한됩니다. 본 연구는 DIAL-MPC(Diffusion-Inspired Annealing for Legged MPC)를 소개합니다. 이는 새로운 확산 스타일 어닐링 과정을 갖춘 샘플링 기반 MPC 프레임워크입니다. 이러한 어닐링 과정은 모델 예측 경로 적분 제어(MPPI)의 이론적 지형 분석과 MPPI와 단일 단계 확산 간의 연결에 의해 뒷받침됩니다. 알고리즘적으로, DIAL-MPC는 온라인에서 반복적으로 해를 개선하며 전역적 탐색과 지역적 수렴을 모두 달성합니다. 사족 보행 로봇의 토크 수준 제어 작업에서 DIAL-MPC는 표준 MPPI의 추적 오차를 $13.4$배 줄이고, 훈련 없이도 어려운 등반 작업에서 강화 학습(RL) 정책보다 $50\%$ 더 나은 성능을 보입니다. 특히, DIAL-MPC는 페이로드를 실은 정밀한 실제 사족 보행 로봇 점프를 가능하게 합니다. 우리가 아는 한, DIAL-MPC는 실시간으로 전차수 사족 보행 동역학을 최적화하는 최초의 훈련 없는 방법입니다.

## 핵심 내용
고차원성과 비볼록성으로 인해, 보행 로봇의 전차수 동역학 모델을 사용한 실시간 최적 제어는 어렵습니다. 따라서 비선형 모델 예측 제어(NMPC) 접근법은 종종 축소 차수 모델로 제한됩니다. 샘플링 기반 MPC는 비볼록, 심지어 불연속적인 문제에서 잠재력을 보여주었지만, 높은 분산을 가진 차선의 해를 산출하는 경우가 많아 고차원 보행에서의 응용이 제한됩니다. 본 연구는 DIAL-MPC(Diffusion-Inspired Annealing for Legged MPC)를 소개합니다. 이는 새로운 확산 스타일 어닐링 과정을 갖춘 샘플링 기반 MPC 프레임워크입니다. 이러한 어닐링 과정은 모델 예측 경로 적분 제어(MPPI)의 이론적 지형 분석과 MPPI와 단일 단계 확산 간의 연결에 의해 뒷받침됩니다. 알고리즘적으로, DIAL-MPC는 온라인에서 반복적으로 해를 개선하며 전역적 탐색과 지역적 수렴을 모두 달성합니다. 사족 보행 로봇의 토크 수준 제어 작업에서 DIAL-MPC는 표준 MPPI의 추적 오차를 $13.4$배 줄이고, 훈련 없이도 어려운 등반 작업에서 강화 학습(RL) 정책보다 $50\%$ 더 나은 성능을 보입니다. 특히, DIAL-MPC는 페이로드를 실은 정밀한 실제 사족 보행 로봇 점프를 가능하게 합니다. 우리가 아는 한, DIAL-MPC는 실시간으로 전차수 사족 보행 동역학을 최적화하는 최초의 훈련 없는 방법입니다.

## 参考
- http://arxiv.org/abs/2409.15610v1
