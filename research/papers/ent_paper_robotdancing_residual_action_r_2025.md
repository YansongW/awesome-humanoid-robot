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
  zh: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking is a 2025 work on physics-based
    character animation for humanoid robots.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.20717v1.
sources:
- id: src_001
  type: paper
  title: 'RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking (arXiv)'
  url: https://arxiv.org/abs/2509.20717
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Long-horizon, high-dynamic motion tracking on humanoids remains brittle because absolute joint commands cannot compensate model-plant mismatch, leading to error accumulation. We propose RobotDancing, a simple, scalable framework that predicts residual joint targets to explicitly correct dynamics discrepancies. The pipeline is end-to-end--training, sim-to-sim validation, and zero-shot sim-to-real--and uses a single-stage reinforcement learning (RL) setup with a unified observation, reward, and hyperparameter configuration. We evaluate primarily on Unitree G1 with retargeted LAFAN1 dance sequences and validate transfer on H1/H1-2. RobotDancing can track multi-minute, high-energy behaviors (jumps, spins, cartwheels) and deploys zero-shot to hardware with high motion tracking quality.

## 核心内容
Long-horizon, high-dynamic motion tracking on humanoids remains brittle because absolute joint commands cannot compensate model-plant mismatch, leading to error accumulation. We propose RobotDancing, a simple, scalable framework that predicts residual joint targets to explicitly correct dynamics discrepancies. The pipeline is end-to-end--training, sim-to-sim validation, and zero-shot sim-to-real--and uses a single-stage reinforcement learning (RL) setup with a unified observation, reward, and hyperparameter configuration. We evaluate primarily on Unitree G1 with retargeted LAFAN1 dance sequences and validate transfer on H1/H1-2. RobotDancing can track multi-minute, high-energy behaviors (jumps, spins, cartwheels) and deploys zero-shot to hardware with high motion tracking quality.

## 参考
- http://arxiv.org/abs/2509.20717v1

## Overview
Long-horizon, high-dynamic motion tracking on humanoids remains brittle because absolute joint commands cannot compensate model-plant mismatch, leading to error accumulation. We propose RobotDancing, a simple, scalable framework that predicts residual joint targets to explicitly correct dynamics discrepancies. The pipeline is end-to-end—training, sim-to-sim validation, and zero-shot sim-to-real—and uses a single-stage reinforcement learning (RL) setup with a unified observation, reward, and hyperparameter configuration. We evaluate primarily on Unitree G1 with retargeted LAFAN1 dance sequences and validate transfer on H1/H1-2. RobotDancing can track multi-minute, high-energy behaviors (jumps, spins, cartwheels) and deploys zero-shot to hardware with high motion tracking quality.

## Content
Long-horizon, high-dynamic motion tracking on humanoids remains brittle because absolute joint commands cannot compensate model-plant mismatch, leading to error accumulation. We propose RobotDancing, a simple, scalable framework that predicts residual joint targets to explicitly correct dynamics discrepancies. The pipeline is end-to-end—training, sim-to-sim validation, and zero-shot sim-to-real—and uses a single-stage reinforcement learning (RL) setup with a unified observation, reward, and hyperparameter configuration. We evaluate primarily on Unitree G1 with retargeted LAFAN1 dance sequences and validate transfer on H1/H1-2. RobotDancing can track multi-minute, high-energy behaviors (jumps, spins, cartwheels) and deploys zero-shot to hardware with high motion tracking quality.

## 개요
휴머노이드의 장시간 고동적 모션 추적은 절대 관절 명령이 모델-플랜트 불일치를 보상하지 못해 오차가 누적되면서 여전히 취약합니다. 우리는 RobotDancing을 제안합니다. 이는 동역학적 불일치를 명시적으로 보정하기 위해 잔여 관절 목표를 예측하는 간단하고 확장 가능한 프레임워크입니다. 파이프라인은 종단 간(end-to-end) 학습, 시뮬-시뮬 검증, 제로샷 시뮬-실제 전이로 구성되며, 통합된 관찰, 보상 및 하이퍼파라미터 구성을 갖춘 단일 단계 강화 학습(RL) 설정을 사용합니다. 주로 Unitree G1에서 리타겟팅된 LAFAN1 댄스 시퀀스를 평가하고 H1/H1-2에서 전이를 검증합니다. RobotDancing은 수 분간 지속되는 고에너지 동작(점프, 회전, 공중제비)을 추적할 수 있으며, 높은 모션 추적 품질로 하드웨어에 제로샷 배포가 가능합니다.

## 핵심 내용
휴머노이드의 장시간 고동적 모션 추적은 절대 관절 명령이 모델-플랜트 불일치를 보상하지 못해 오차가 누적되면서 여전히 취약합니다. 우리는 RobotDancing을 제안합니다. 이는 동역학적 불일치를 명시적으로 보정하기 위해 잔여 관절 목표를 예측하는 간단하고 확장 가능한 프레임워크입니다. 파이프라인은 종단 간(end-to-end) 학습, 시뮬-시뮬 검증, 제로샷 시뮬-실제 전이로 구성되며, 통합된 관찰, 보상 및 하이퍼파라미터 구성을 갖춘 단일 단계 강화 학습(RL) 설정을 사용합니다. 주로 Unitree G1에서 리타겟팅된 LAFAN1 댄스 시퀀스를 평가하고 H1/H1-2에서 전이를 검증합니다. RobotDancing은 수 분간 지속되는 고에너지 동작(점프, 회전, 공중제비)을 추적할 수 있으며, 높은 모션 추적 품질로 하드웨어에 제로샷 배포가 가능합니다.
