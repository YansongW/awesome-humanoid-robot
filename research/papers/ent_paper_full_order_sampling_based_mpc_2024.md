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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.15610v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (794 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2409.15610v1

## 개요
족형 로봇의 전차수 동역학 모델의 고차원 비볼록 최적화 문제에 대해, 기존 NMPC 방법은 주로 축소 모델에 국한되어 있으며, 샘플링 기반 MPC는 비연속 문제를 처리할 수 있지만 높은 분산의 차선해 문제가 존재한다. DIAL-MPC는 확산 모델의 어닐링 메커니즘을 혁신적으로 융합하여, 이론 분석을 통해 MPPI와 단일 단계 확산 간의 수학적 연결을 확립하고, 전역 탐색과 국소 수렴을 동시에 고려한 반복 최적화 알고리즘을 설계했다. 사족 로봇 실험에서 이 방법은 토크 수준 제어 작업에서 뚜렷한 우위를 보여주었다: 표준 MPPI의 추적 오차가 1/13.4로 압축되었고, 훈련 없이 등반 성능이 RL 정책보다 50% 높았으며, 부하가 있는 정밀 점프 제어를 최초로 구현했다.

## 핵심 내용
### 방법 구조
- **핵심 메커니즘**: DIAL-MPC는 확산 모델의 어닐링 과정을 샘플링 기반 MPC에 도입하여, 노이즈 분산을 점진적으로 낮춤으로써 전역 탐색에서 국소 수렴으로의 부드러운 전환을 실현한다
- **이론적 기반**: MPPI(Model Predictive Path Integral Control)의 손실 경관 분석을 기반으로, MPPI와 단일 단계 확산 과정 간의 수학적 등가 관계를 확립한다
- **알고리즘 흐름**: 온라인 반복 최적화 시, 각 제어 주기 내에서 어닐링 전략을 포함한 다중 라운드의 샘플링-평가-재샘플링 루프를 실행한다

### 실험 설정
- **제어 대상**: 사족 로봇 토크 수준 제어, 기본 운동, 등반, 점프 등의 작업 포함
- **비교 기준**: 표준 MPPI, 강화 학습 정책(RL)
- **하드웨어 플랫폼**: 실제 사족 로봇 플랫폼, 부하 점프 실험 포함

### 주요 성능 데이터
- **추적 오차**: 표준 MPPI 대비 13.4배 감소
- **등반 작업**: 훈련 없이 성공률이 RL 정책보다 50% 높음
- **점프 능력**: 실제 사족 로봇의 부하가 있는 정밀 점프를 최초로 구현
- **실시간성**: 완전한 사족 동역학 모델에서 사전 훈련 없이 실시간 최적화 구현

### 결론
DIAL-MPC는 훈련이 필요 없는 최초의 실시간 전차수 사족 동역학 최적화 방법으로, 확산형 어닐링 메커니즘을 통해 고차원 비볼록 최적화 문제를 효과적으로 해결하며, 토크 수준 제어 작업에서 전역 탐색 능력과 국소 수렴 정밀도를 동시에 달성하여 족형 로봇의 전신 제어에 새로운 패러다임을 제공한다.
