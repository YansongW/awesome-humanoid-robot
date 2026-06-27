---
$id: ent_paper_kaushik_adaptive_prior_selection_for_r_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Adaptive Prior Selection for Repertoire-based Online Adaptation in Robotics
  zh: 机器人中基于技能库的在线自适应的自适应先验选择
  ko: 로봇 공학에서 레퍼토리 기반 온라인 적응을 위한 적응형 사전 선택
summary:
  en: This paper introduces APROL, an algorithm that maintains multiple MAP-Elites
    behavioral repertoires as simulation priors and selects the most suitable prior
    online using Gaussian-process transformation models and a MAP/UCB action-selection
    criterion. It enables reset-free adaptation to damage and environmental changes,
    and is shown to outperform single-prior and RTE baselines on simulated object
    pushing and hexapod locomotion, with validation on a real damaged hexapod.
  zh: 本文提出了APROL算法，该算法维护多个作为仿真先验的MAP-Elites行为技能库，并通过高斯过程变换模型与MAP/UCB动作选择准则在线选择最合适的先验。它实现了无重置的损坏与环境变化适应，在模拟推物与六足运动任务上优于单先验和RTE基线，并在真实损坏六足机器人上进行了验证。
  ko: 본 논문은 여러 MAP-Elites 행동 레퍼토리를 시뮬레이션 사전 정보로 유지하고, 가우시안 프로세스 변환 모델과 MAP/UCB 행동
    선택 기준을 통해 온라인으로 가장 적절한 사전 정보를 선택하는 APROL 알고리즘을 제안한다. 이는 재설정 없는 손상 및 환경 변화 적응을
    가능하게 하며, 모의 물체 밀기와 육족 보행 과제에서 단일 사전 정보 및 RTE 기준보다 우수한 성능을 보이고, 실제 손상된 육족 로봇에서
    검증되었다.
domains:
- 07_ai_models_algorithms
- 03_manufacturing_processes
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- repertoire_based_learning
- online_adaptation
- map_elites
- gaussian_process
- reset_free_learning
- damage_recovery
- simulation_prior
- behavioral_repertoire
- robot_adaptation
- aprol
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; requires human review
    against the full paper before verification.
sources:
- id: src_001
  type: paper
  title: Adaptive Prior Selection for Repertoire-based Online Adaptation in Robotics
  url: https://arxiv.org/abs/1907.07029
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Repertoire-based learning typically pre-trains a single diverse policy repertoire in simulation and then selects policies online for adaptation. This paper relaxes the assumption that one prior is sufficient by generating multiple repertoires that anticipate distinct situations—such as different damage conditions or terrain types—and adaptively selecting the most useful prior at runtime. The proposed APROL algorithm (Adaptive Prior selection for Repertoire-based Online Learning) combines a Gaussian-process transformation model per repertoire, using the repertoire's expected transitions as a non-constant prior mean, with a Maximum A Posteriori (MAP) action-selection criterion and an Upper Confidence Bound (UCB) term for prior selection.

APROL is evaluated on two simulated tasks: pushing unknown objects of varying shapes and sizes with a robotic arm, and goal-reaching locomotion with a damaged hexapod. The experiments compare APROL against Reset-free Trial and Error (RTE) and several single-repertoire baselines. APROL reaches satisfactory behavior in less interaction time than the baselines. The authors also transfer the method to a real damaged hexapod that must avoid obstacles while reaching a goal, demonstrating that the approach can close the sim-to-real gap for rapid damage recovery.

## Key Contributions

- Proposes APROL, which adaptively selects the most suitable repertoire prior among many for online robot adaptation.
- Extends repertoire-based learning from a single prior to multiple priors for reset-free, non-episodic adaptation.
- Learns Gaussian-process-based task-space transformation models using each repertoire as a non-constant prior mean-function.
- Demonstrates faster interaction-time adaptation than single-prior and no-learning baselines on simulated object pushing and hexapod locomotion.
- Validates the approach on a real damaged hexapod robot performing obstacle-avoidance goal reaching.

## Relevance to Humanoid Robotics

Humanoid robots deployed in factories, warehouses, or service settings must continue operating despite unexpected hardware faults, surface changes, or environmental disturbances. APROL's ability to switch among pre-computed simulation priors and rapidly identify compensatory policies without resetting the robot maps directly onto the reliability and uptime requirements of humanoid systems. Because it is reset-free and data-efficient, it is well suited to physical humanoid platforms where trials are costly and downtime must be minimized. The paper does not demonstrate the method on a humanoid, but the damage-recovery and prior-selection concepts transfer to legged and manipulation subsystems common in humanoids.
