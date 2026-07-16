---
$id: ent_paper_end_to_end_humanoid_robot_safe_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy
  zh: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy
  ko: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy
summary:
  en: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy is a 2025 work on locomotion for humanoid robots.
  zh: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy is a 2025 work on locomotion for humanoid robots.
  ko: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- end_to_end_humanoid_robot_safe
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.07611v1.
sources:
- id: src_001
  type: paper
  title: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy (arXiv)
  url: https://arxiv.org/abs/2508.07611
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The deployment of humanoid robots in unstructured, human-centric environments requires navigation capabilities that extend beyond simple locomotion to include robust perception, provable safety, and socially aware behavior. Current reinforcement learning approaches are often limited by blind controllers that lack environmental awareness or by vision-based systems that fail to perceive complex 3D obstacles. In this work, we present an end-to-end locomotion policy that directly maps raw, spatio-temporal LiDAR point clouds to motor commands, enabling robust navigation in cluttered dynamic scenes. We formulate the control problem as a Constrained Markov Decision Process (CMDP) to formally separate safety from task objectives. Our key contribution is a novel methodology that translates the principles of Control Barrier Functions (CBFs) into costs within the CMDP, allowing a model-free Penalized Proximal Policy Optimization (P3O) to enforce safety constraints during training. Furthermore, we introduce a set of comfort-oriented rewards, grounded in human-robot interaction research, to promote motions that are smooth, predictable, and less intrusive. We demonstrate the efficacy of our framework through a successful sim-to-real transfer to a physical humanoid robot, which exhibits agile and safe navigation around both static and dynamic 3D obstacles.

## 核心内容
The deployment of humanoid robots in unstructured, human-centric environments requires navigation capabilities that extend beyond simple locomotion to include robust perception, provable safety, and socially aware behavior. Current reinforcement learning approaches are often limited by blind controllers that lack environmental awareness or by vision-based systems that fail to perceive complex 3D obstacles. In this work, we present an end-to-end locomotion policy that directly maps raw, spatio-temporal LiDAR point clouds to motor commands, enabling robust navigation in cluttered dynamic scenes. We formulate the control problem as a Constrained Markov Decision Process (CMDP) to formally separate safety from task objectives. Our key contribution is a novel methodology that translates the principles of Control Barrier Functions (CBFs) into costs within the CMDP, allowing a model-free Penalized Proximal Policy Optimization (P3O) to enforce safety constraints during training. Furthermore, we introduce a set of comfort-oriented rewards, grounded in human-robot interaction research, to promote motions that are smooth, predictable, and less intrusive. We demonstrate the efficacy of our framework through a successful sim-to-real transfer to a physical humanoid robot, which exhibits agile and safe navigation around both static and dynamic 3D obstacles.

## 参考
- http://arxiv.org/abs/2508.07611v1

## Overview
The deployment of humanoid robots in unstructured, human-centric environments requires navigation capabilities that extend beyond simple locomotion to include robust perception, provable safety, and socially aware behavior. Current reinforcement learning approaches are often limited by blind controllers that lack environmental awareness or by vision-based systems that fail to perceive complex 3D obstacles. In this work, we present an end-to-end locomotion policy that directly maps raw, spatio-temporal LiDAR point clouds to motor commands, enabling robust navigation in cluttered dynamic scenes. We formulate the control problem as a Constrained Markov Decision Process (CMDP) to formally separate safety from task objectives. Our key contribution is a novel methodology that translates the principles of Control Barrier Functions (CBFs) into costs within the CMDP, allowing a model-free Penalized Proximal Policy Optimization (P3O) to enforce safety constraints during training. Furthermore, we introduce a set of comfort-oriented rewards, grounded in human-robot interaction research, to promote motions that are smooth, predictable, and less intrusive. We demonstrate the efficacy of our framework through a successful sim-to-real transfer to a physical humanoid robot, which exhibits agile and safe navigation around both static and dynamic 3D obstacles.

## Content
The deployment of humanoid robots in unstructured, human-centric environments requires navigation capabilities that extend beyond simple locomotion to include robust perception, provable safety, and socially aware behavior. Current reinforcement learning approaches are often limited by blind controllers that lack environmental awareness or by vision-based systems that fail to perceive complex 3D obstacles. In this work, we present an end-to-end locomotion policy that directly maps raw, spatio-temporal LiDAR point clouds to motor commands, enabling robust navigation in cluttered dynamic scenes. We formulate the control problem as a Constrained Markov Decision Process (CMDP) to formally separate safety from task objectives. Our key contribution is a novel methodology that translates the principles of Control Barrier Functions (CBFs) into costs within the CMDP, allowing a model-free Penalized Proximal Policy Optimization (P3O) to enforce safety constraints during training. Furthermore, we introduce a set of comfort-oriented rewards, grounded in human-robot interaction research, to promote motions that are smooth, predictable, and less intrusive. We demonstrate the efficacy of our framework through a successful sim-to-real transfer to a physical humanoid robot, which exhibits agile and safe navigation around both static and dynamic 3D obstacles.

## 개요
인간 중심의 비정형 환경에서 휴머노이드 로봇을 배치하려면 단순한 이동을 넘어 강건한 인지, 증명 가능한 안전성, 사회적 인식 행동을 포함하는 항법 능력이 필요합니다. 현재의 강화 학습 접근법은 환경 인식이 부족한 블라인드 제어기나 복잡한 3D 장애물을 인식하지 못하는 비전 기반 시스템에 의해 종종 제한됩니다. 본 연구에서는 원시 시공간 LiDAR 포인트 클라우드를 모터 명령에 직접 매핑하는 종단간 보행 정책을 제시하여 혼잡한 동적 환경에서 강건한 항법을 가능하게 합니다. 제어 문제를 제약 마르코프 결정 과정(CMDP)으로 공식화하여 안전성과 작업 목표를 공식적으로 분리합니다. 주요 기여는 제어 장벽 함수(CBF)의 원리를 CMDP 내 비용으로 변환하는 새로운 방법론으로, 모델 프리 Penalized Proximal Policy Optimization(P3O)이 훈련 중 안전 제약을 강제하도록 합니다. 또한 인간-로봇 상호작용 연구에 기반한 편안함 지향 보상 세트를 도입하여 부드럽고 예측 가능하며 덜 방해가 되는 움직임을 촉진합니다. 물리적 휴머노이드 로봇으로의 시뮬레이션-실제 전환 성공을 통해 프레임워크의 효용성을 입증하며, 정적 및 동적 3D 장애물 주변에서 민첩하고 안전한 항법을 보여줍니다.

## 핵심 내용
인간 중심의 비정형 환경에서 휴머노이드 로봇을 배치하려면 단순한 이동을 넘어 강건한 인지, 증명 가능한 안전성, 사회적 인식 행동을 포함하는 항법 능력이 필요합니다. 현재의 강화 학습 접근법은 환경 인식이 부족한 블라인드 제어기나 복잡한 3D 장애물을 인식하지 못하는 비전 기반 시스템에 의해 종종 제한됩니다. 본 연구에서는 원시 시공간 LiDAR 포인트 클라우드를 모터 명령에 직접 매핑하는 종단간 보행 정책을 제시하여 혼잡한 동적 환경에서 강건한 항법을 가능하게 합니다. 제어 문제를 제약 마르코프 결정 과정(CMDP)으로 공식화하여 안전성과 작업 목표를 공식적으로 분리합니다. 주요 기여는 제어 장벽 함수(CBF)의 원리를 CMDP 내 비용으로 변환하는 새로운 방법론으로, 모델 프리 Penalized Proximal Policy Optimization(P3O)이 훈련 중 안전 제약을 강제하도록 합니다. 또한 인간-로봇 상호작용 연구에 기반한 편안함 지향 보상 세트를 도입하여 부드럽고 예측 가능하며 덜 방해가 되는 움직임을 촉진합니다. 물리적 휴머노이드 로봇으로의 시뮬레이션-실제 전환 성공을 통해 프레임워크의 효용성을 입증하며, 정적 및 동적 3D 장애물 주변에서 민첩하고 안전한 항법을 보여줍니다.
