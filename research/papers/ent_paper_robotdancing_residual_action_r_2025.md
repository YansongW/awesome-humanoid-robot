---
$id: ent_paper_robotdancing_residual_action_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking'
  zh: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking'
  ko: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking'
summary:
  en: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking is a 2025 work on physics-based
    character animation for humanoid robots.'
  zh: RobotDancing 是 2025 年提出的一种用于人形机器人长时域高动态运动跟踪的残差动作强化学习框架。该工作由研究团队基于 Unitree G1 机器人开发，核心贡献在于通过预测残差关节目标来显式补偿动力学模型与真实系统之间的不匹配，从而在零样本迁移下实现多分钟高能量动作（跳跃、旋转、侧手翻）的鲁棒跟踪。
  ko: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking is a 2025 work on physics-based
    character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- physics_based
- robotdancing
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.20717v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking (arXiv)'
  url: https://arxiv.org/abs/2509.20717
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
传统人形机器人在执行长时域高动态运动跟踪时，由于绝对关节指令无法补偿模型与真实系统之间的不匹配，导致误差累积而失效。RobotDancing 提出一种简单且可扩展的框架，通过强化学习预测残差关节目标来显式修正动力学偏差。该流水线采用端到端设计，包括训练、sim-to-sim 验证和零样本 sim-to-real 部署，并使用统一的观测、奖励和超参数配置的单阶段 RL 设置。主要评估在 Unitree G1 机器人上进行，使用重新定向的 LAFAN1 舞蹈序列，并在 H1/H1-2 机器人上验证了迁移能力。

## 核心内容
### 方法架构
- **残差动作预测**：核心思想是让 RL 策略输出残差关节目标，而非绝对关节位置。这些残差目标叠加在参考运动生成的基准关节指令上，从而显式补偿动力学模型与真实系统之间的不匹配。
- **端到端流水线**：整个框架采用单阶段 RL 训练，使用统一的观测空间（包括机器人状态、参考运动特征等）、奖励函数和超参数配置。训练完成后，直接进行 sim-to-sim 验证和零样本 sim-to-real 部署，无需额外微调。

### 实验设置
- **硬件平台**：主要评估在 Unitree G1 人形机器人上进行，并在 H1/H1-2 机器人上验证了跨平台迁移能力。
- **运动数据**：使用重新定向的 LAFAN1 舞蹈序列作为参考运动，包含跳跃、旋转、侧手翻等高动态动作。
- **训练配置**：采用统一的观测、奖励和超参数配置，确保框架的简单性和可扩展性。

### 关键结果
- **长时域跟踪**：RobotDancing 能够跟踪多分钟的高能量行为，包括跳跃、旋转和侧手翻等复杂动作，且误差不随时间累积。
- **零样本迁移**：从仿真环境直接部署到真实硬件，无需任何调整，即可实现高质量的运动跟踪。
- **跨平台验证**：在 H1/H1-2 机器人上成功验证了框架的迁移能力，表明其具有良好的泛化性。

### 结论
RobotDancing 通过残差动作 RL 框架有效解决了人形机器人长时域高动态运动跟踪中的误差累积问题，实现了从仿真到真实世界的零样本部署，为物理角色动画提供了简单且鲁棒的解决方案。

## Overview
Long-horizon, high-dynamic motion tracking on humanoids remains brittle because absolute joint commands cannot compensate model-plant mismatch, leading to error accumulation. We propose RobotDancing, a simple, scalable framework that predicts residual joint targets to explicitly correct dynamics discrepancies. The pipeline is end-to-end--training, sim-to-sim validation, and zero-shot sim-to-real--and uses a single-stage reinforcement learning (RL) setup with a unified observation, reward, and hyperparameter configuration. We evaluate primarily on Unitree G1 with retargeted LAFAN1 dance sequences and validate transfer on H1/H1-2. RobotDancing can track multi-minute, high-energy behaviors (jumps, spins, cartwheels) and deploys zero-shot to hardware with high motion tracking quality.

## Overview
Long-horizon, high-dynamic motion tracking on humanoids remains brittle because absolute joint commands cannot compensate model-plant mismatch, leading to error accumulation. We propose RobotDancing, a simple, scalable framework that predicts residual joint targets to explicitly correct dynamics discrepancies. The pipeline is end-to-end—training, sim-to-sim validation, and zero-shot sim-to-real—and uses a single-stage reinforcement learning (RL) setup with a unified observation, reward, and hyperparameter configuration. We evaluate primarily on Unitree G1 with retargeted LAFAN1 dance sequences and validate transfer on H1/H1-2. RobotDancing can track multi-minute, high-energy behaviors (jumps, spins, cartwheels) and deploys zero-shot to hardware with high motion tracking quality.

## Content
Long-horizon, high-dynamic motion tracking on humanoids remains brittle because absolute joint commands cannot compensate model-plant mismatch, leading to error accumulation. We propose RobotDancing, a simple, scalable framework that predicts residual joint targets to explicitly correct dynamics discrepancies. The pipeline is end-to-end—training, sim-to-sim validation, and zero-shot sim-to-real—and uses a single-stage reinforcement learning (RL) setup with a unified observation, reward, and hyperparameter configuration. We evaluate primarily on Unitree G1 with retargeted LAFAN1 dance sequences and validate transfer on H1/H1-2. RobotDancing can track multi-minute, high-energy behaviors (jumps, spins, cartwheels) and deploys zero-shot to hardware with high motion tracking quality.

## 개요
휴머노이드의 장시간 고동적 모션 추적은 절대 관절 명령이 모델-플랜트 불일치를 보상하지 못해 오차가 누적되면서 여전히 취약합니다. 우리는 RobotDancing을 제안합니다. 이는 동역학적 불일치를 명시적으로 보정하기 위해 잔여 관절 목표를 예측하는 간단하고 확장 가능한 프레임워크입니다. 파이프라인은 종단 간(end-to-end) 학습, 시뮬-시뮬 검증, 제로샷 시뮬-실제 전이로 구성되며, 통합된 관찰, 보상 및 하이퍼파라미터 구성을 갖춘 단일 단계 강화 학습(RL) 설정을 사용합니다. 주로 Unitree G1에서 리타겟팅된 LAFAN1 댄스 시퀀스를 평가하고 H1/H1-2에서 전이를 검증합니다. RobotDancing은 수 분간 지속되는 고에너지 동작(점프, 회전, 공중제비)을 추적할 수 있으며, 높은 모션 추적 품질로 하드웨어에 제로샷 배포가 가능합니다.

## 핵심 내용
휴머노이드의 장시간 고동적 모션 추적은 절대 관절 명령이 모델-플랜트 불일치를 보상하지 못해 오차가 누적되면서 여전히 취약합니다. 우리는 RobotDancing을 제안합니다. 이는 동역학적 불일치를 명시적으로 보정하기 위해 잔여 관절 목표를 예측하는 간단하고 확장 가능한 프레임워크입니다. 파이프라인은 종단 간(end-to-end) 학습, 시뮬-시뮬 검증, 제로샷 시뮬-실제 전이로 구성되며, 통합된 관찰, 보상 및 하이퍼파라미터 구성을 갖춘 단일 단계 강화 학습(RL) 설정을 사용합니다. 주로 Unitree G1에서 리타겟팅된 LAFAN1 댄스 시퀀스를 평가하고 H1/H1-2에서 전이를 검증합니다. RobotDancing은 수 분간 지속되는 고에너지 동작(점프, 회전, 공중제비)을 추적할 수 있으며, 높은 모션 추적 품질로 하드웨어에 제로샷 배포가 가능합니다.

## 参考
- http://arxiv.org/abs/2509.20717v1
