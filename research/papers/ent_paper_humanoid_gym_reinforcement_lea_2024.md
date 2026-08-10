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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2404.05695v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (740 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2404.05695v2

## Overview
Humanoid-Gym provides an easy-to-use reinforcement learning framework specifically designed for training locomotion skills for humanoid robots. The framework is built on Nvidia Isaac Gym and integrates a sim-to-sim module from Isaac Gym to Mujoco, allowing users to verify the robustness and generalization capabilities of trained policies across different physical simulation environments. The framework has been validated in real-world settings on RobotEra's XBot-S (1.2m tall) and XBot-L (1.65m tall) humanoid robots, successfully achieving zero-shot sim-to-real transfer.

## Content
### Method
Humanoid-Gym employs a reinforcement learning framework based on Nvidia Isaac Gym, focusing on training locomotion skills for humanoid robots. The framework integrates a sim-to-sim module from Isaac Gym to Mujoco, ensuring the robustness and generalization of policies across different physical simulation environments.

### Architecture
- Built on Nvidia Isaac Gym, providing an efficient parallel simulation environment.
- Integrates a sim-to-sim framework, supporting transfer validation from Isaac Gym to Mujoco.
- Supports zero-shot sim-to-real transfer without additional fine-tuning.

### Experimental Setup
- Validated on RobotEra's XBot-S (1.2m tall) and XBot-L (1.65m tall) humanoid robots.
- In real-world tests, policies were transferred directly from simulation without any adjustments.

### Key Figures
- XBot-S height: 1.2m
- XBot-L height: 1.65m
- Zero-shot transfer success rate: not explicitly specified, but the framework has been validated as effective.

### Conclusion
Humanoid-Gym provides an efficient and easy-to-use reinforcement learning framework that successfully achieves zero-shot sim-to-real transfer for humanoid robot locomotion skills. The open-source code and project website offer researchers a convenient foundation for reproduction and extension.

## 개요
Humanoid-Gym은 휴머노이드 로봇의 운동 기술 훈련을 위해 특별히 설계된 사용하기 쉬운 강화 학습 프레임워크를 제공합니다. 이 프레임워크는 Nvidia Isaac Gym을 기반으로 구축되었으며, Isaac Gym에서 Mujoco로의 시뮬레이션 간 전환 모듈을 통합하여 사용자가 다양한 물리 시뮬레이션 환경에서 훈련된 정책의 견고성과 일반화 능력을 검증할 수 있게 합니다. 이 프레임워크는 RobotEra의 XBot-S(1.2m 높이) 및 XBot-L(1.65m 높이) 휴머노이드 로봇에서 실제 환경 검증을 거쳐 제로샷 시뮬레이션-실제 전환을 성공적으로 구현했습니다.

## 핵심 내용
### 방법
Humanoid-Gym은 Nvidia Isaac Gym 기반의 강화 학습 프레임워크를 채택하여 휴머노이드 로봇의 운동 기술 훈련에 중점을 둡니다. 프레임워크는 Isaac Gym에서 Mujoco로의 시뮬레이션 간 전환 모듈을 통합하여 다양한 물리 시뮬레이션 환경에서 정책의 견고성과 일반화 능력을 보장합니다.

### 아키텍처
- Nvidia Isaac Gym을 기반으로 구축되어 고효율 병렬 시뮬레이션 환경을 제공합니다.
- sim-to-sim 프레임워크를 통합하여 Isaac Gym에서 Mujoco로의 전환 검증을 지원합니다.
- 추가 미세 조정 없이 제로샷 시뮬레이션-실제 전환을 지원합니다.

### 실험 설정
- RobotEra의 XBot-S(1.2m 높이) 및 XBot-L(1.65m 높이) 휴머노이드 로봇에서 검증되었습니다.
- 실제 환경 테스트에서 정책은 시뮬레이션에서 직접 전환되었으며 어떠한 조정도 이루어지지 않았습니다.

### 주요 수치
- XBot-S 높이: 1.2m
- XBot-L 높이: 1.65m
- 제로샷 전환 성공률: 명시적으로 제공되지는 않았지만 프레임워크의 유효성은 검증되었습니다.

### 결론
Humanoid-Gym은 효율적이고 사용하기 쉬운 강화 학습 프레임워크를 제공하여 휴머노이드 로봇 운동 기술의 제로샷 시뮬레이션-실제 전환을 성공적으로 구현했습니다. 이 프레임워크의 오픈 소스 코드와 프로젝트 웹사이트는 연구자들에게 편리한 재현 및 확장 기반을 제공합니다.
