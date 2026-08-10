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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.20717v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (941 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.20717v1

## 개요
전통적인 휴머노이드 로봇은 장시간 고동적 운동 추적을 수행할 때, 절대 관절 명령이 모델과 실제 시스템 간의 불일치를 보상할 수 없어 오차가 누적되며 실패합니다. RobotDancing은 강화 학습을 통해 잔차 관절 목표를 예측하여 동역학 편차를 명시적으로 수정하는 간단하고 확장 가능한 프레임워크를 제안합니다. 이 파이프라인은 훈련, sim-to-sim 검증, 제로샷 sim-to-real 배포를 포함한 엔드투엔드 설계를 채택하며, 통합된 관측, 보상, 하이퍼파라미터 설정을 사용하는 단일 단계 RL 설정을 사용합니다. 주요 평가는 Unitree G1 로봇에서 수행되었으며, 리타게팅된 LAFAN1 댄스 시퀀스를 사용하고 H1/H1-2 로봇에서 전이 능력을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
- **잔차 동작 예측**: 핵심 아이디어는 RL 정책이 절대 관절 위치 대신 잔차 관절 목표를 출력하도록 하는 것입니다. 이러한 잔차 목표는 참조 운동에서 생성된 기준 관절 명령에 중첩되어 동역학 모델과 실제 시스템 간의 불일치를 명시적으로 보상합니다.
- **엔드투엔드 파이프라인**: 전체 프레임워크는 로봇 상태, 참조 운동 특징 등을 포함한 통합된 관측 공간, 보상 함수, 하이퍼파라미터 설정을 사용하는 단일 단계 RL 훈련을 채택합니다. 훈련 완료 후 추가 미세 조정 없이 직접 sim-to-sim 검증 및 제로샷 sim-to-real 배포를 수행합니다.

### 실험 설정
- **하드웨어 플랫폼**: 주요 평가는 Unitree G1 휴머노이드 로봇에서 수행되었으며, H1/H1-2 로봇에서 크로스 플랫폼 전이 능력을 검증했습니다.
- **운동 데이터**: 리타게팅된 LAFAN1 댄스 시퀀스를 참조 운동으로 사용하며, 점프, 회전, 옆돌기 등의 고동적 동작을 포함합니다.
- **훈련 설정**: 통합된 관측, 보상, 하이퍼파라미터 설정을 채택하여 프레임워크의 단순성과 확장성을 보장합니다.

### 주요 결과
- **장시간 추적**: RobotDancing은 점프, 회전, 옆돌기 등의 복잡한 동작을 포함한 수 분간의 고에너지 행동을 추적할 수 있으며, 오차가 시간에 따라 누적되지 않습니다.
- **제로샷 전이**: 시뮬레이션 환경에서 실제 하드웨어로 직접 배포하며, 어떠한 조정 없이도 고품질 운동 추적을 달성합니다.
- **크로스 플랫폼 검증**: H1/H1-2 로봇에서 프레임워크의 전이 능력을 성공적으로 검증하여 우수한 일반화 성능을 보여줍니다.

### 결론
RobotDancing은 잔차 동작 RL 프레임워크를 통해 휴머노이드 로봇의 장시간 고동적 운동 추적에서의 오차 누적 문제를 효과적으로 해결하며, 시뮬레이션에서 실제 세계로의 제로샷 배포를 구현하여 물리적 캐릭터 애니메이션에 간단하고 견고한 솔루션을 제공합니다.
