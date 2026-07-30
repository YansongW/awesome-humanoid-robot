---
$id: ent_paper_humanoid_gym_reinforcement_lea_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer'
  zh: 'Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer'
  ko: 'Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer'
summary:
  en: 'Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer is a 2024 work on simulation
    benchmark for humanoid robots, with open-source code available.'
  zh: Humanoid-Gym 是一个基于 Nvidia Isaac Gym 的强化学习框架，由 RobotEra 团队开发，用于训练人形机器人的运动技能。其核心贡献在于实现了从仿真到真实环境的零样本迁移，并在 XBot-S 和 XBot-L
    两款人形机器人上得到验证。
  ko: 'Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer is a 2024 work on simulation
    benchmark for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- humanoid
- humanoid_gym
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2404.05695v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer (arXiv)'
  url: https://arxiv.org/abs/2404.05695
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer project page'
  url: https://sites.google.com/view/humanoid-gym/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid-Gym 提供了一个易于使用的强化学习框架，专门针对人形机器人的运动技能训练。该框架基于 Nvidia Isaac Gym 构建，并集成了从 Isaac Gym 到 Mujoco 的仿真到仿真模块，允许用户在不同物理仿真环境中验证训练策略的鲁棒性和泛化能力。该框架在 RobotEra 的 XBot-S（1.2米高）和 XBot-L（1.65米高）人形机器人上进行了真实环境验证，成功实现了零样本仿真到真实迁移。

## 核心内容
### 方法
Humanoid-Gym 采用基于 Nvidia Isaac Gym 的强化学习框架，专注于训练人形机器人的运动技能。框架集成了从 Isaac Gym 到 Mujoco 的仿真到仿真模块，确保策略在不同物理仿真环境中的鲁棒性和泛化能力。

### 架构
- 基于 Nvidia Isaac Gym 构建，提供高效的并行仿真环境。
- 集成 sim-to-sim 框架，支持从 Isaac Gym 到 Mujoco 的迁移验证。
- 支持零样本仿真到真实迁移，无需额外微调。

### 实验设置
- 在 RobotEra 的 XBot-S（1.2米高）和 XBot-L（1.65米高）人形机器人上进行验证。
- 真实环境测试中，策略直接从仿真迁移，未进行任何调整。

### 关键数字
- XBot-S 高度：1.2米
- XBot-L 高度：1.65米
- 零样本迁移成功率：未明确给出，但框架已验证有效。

### 结论
Humanoid-Gym 提供了一个高效且易于使用的强化学习框架，成功实现了人形机器人运动技能的零样本仿真到真实迁移。该框架的开源代码和项目网站为研究人员提供了便利的复现和扩展基础。

## Overview
Humanoid-Gym is an easy-to-use reinforcement learning (RL) framework based on Nvidia Isaac Gym, designed to train locomotion skills for humanoid robots, emphasizing zero-shot transfer from simulation to the real-world environment. Humanoid-Gym also integrates a sim-to-sim framework from Isaac Gym to Mujoco that allows users to verify the trained policies in different physical simulations to ensure the robustness and generalization of the policies. This framework is verified by RobotEra's XBot-S (1.2-meter tall humanoid robot) and XBot-L (1.65-meter tall humanoid robot) in a real-world environment with zero-shot sim-to-real transfer. The project website and source code can be found at: https://sites.google.com/view/humanoid-gym/.

## 개요
Humanoid-Gym은 Nvidia Isaac Gym 기반의 사용하기 쉬운 강화 학습(RL) 프레임워크로, 휴머노이드 로봇의 보행 기술 훈련을 위해 설계되었으며, 시뮬레이션에서 실제 환경으로의 제로샷 전이를 강조합니다. Humanoid-Gym은 또한 Isaac Gym에서 Mujoco로의 sim-to-sim 프레임워크를 통합하여 사용자가 다양한 물리 시뮬레이션에서 훈련된 정책을 검증함으로써 정책의 견고성과 일반화를 보장할 수 있도록 합니다. 이 프레임워크는 RobotEra의 XBot-S(1.2미터 높이의 휴머노이드 로봇)와 XBot-L(1.65미터 높이의 휴머노이드 로봇)을 통해 실제 환경에서 제로샷 sim-to-real 전이로 검증되었습니다. 프로젝트 웹사이트와 소스 코드는 다음에서 확인할 수 있습니다: https://sites.google.com/view/humanoid-gym/.

## 핵심 내용
Humanoid-Gym은 Nvidia Isaac Gym 기반의 사용하기 쉬운 강화 학습(RL) 프레임워크로, 휴머노이드 로봇의 보행 기술 훈련을 위해 설계되었으며, 시뮬레이션에서 실제 환경으로의 제로샷 전이를 강조합니다. Humanoid-Gym은 또한 Isaac Gym에서 Mujoco로의 sim-to-sim 프레임워크를 통합하여 사용자가 다양한 물리 시뮬레이션에서 훈련된 정책을 검증함으로써 정책의 견고성과 일반화를 보장할 수 있도록 합니다. 이 프레임워크는 RobotEra의 XBot-S(1.2미터 높이의 휴머노이드 로봇)와 XBot-L(1.65미터 높이의 휴머노이드 로봇)을 통해 실제 환경에서 제로샷 sim-to-real 전이로 검증되었습니다. 프로젝트 웹사이트와 소스 코드는 다음에서 확인할 수 있습니다: https://sites.google.com/view/humanoid-gym/.

## 参考
- http://arxiv.org/abs/2404.05695v2
