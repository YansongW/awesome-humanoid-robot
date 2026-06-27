---
$id: ent_paper_bao_sim_to_real_transfer_in_deep_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion
  zh: 双足运动深度强化学习中的仿真到现实迁移
  ko: 이족 보행 심층 강화학습의 시뮬레이션-현실 전이
summary:
  en: This survey chapter examines how deep reinforcement learning policies for bipedal
    locomotion can be transferred from simulation to real robots. It maps the sources
    of the sim-to-real gap and organizes mitigation strategies around model-centric
    fidelity improvements and policy hardening through robustness training and online
    adaptation.
  zh: 本综述章节研究如何将双足运动的深度强化学习策略从仿真迁移到真实机器人。它梳理了仿真-现实差距的来源，并从模型中心的保真度提升以及通过鲁棒性训练和在线自适应强化策略两个角度组织缓解方法。
  ko: 본 서베이 장에서는 이족 보행을 위한 심층 강화학습 정책을 시뮬레이션에서 실제 로봇으로 전이하는 방법을 다룬다. 시뮬-리얼 간극의 원인을
    정리하고, 모델 중심의 충실도 향상과 강건성 훈련 및 온라인 적응을 통한 정책 강화라는 두 축으로 해결책을 조직한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- deep_reinforcement_learning
- bipedal_locomotion
- domain_randomization
- system_identification
- residual_dynamics_learning
- teacher_student_learning
- online_adaptation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text review and exact
    citation locations require human verification.
sources:
- id: src_001
  type: paper
  title: Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion
  url: https://arxiv.org/abs/2511.06465
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This chapter frames the problem of transferring deep reinforcement learning (DRL) policies for bipedal locomotion from simulation to physical hardware. It first contextualizes the challenge within end-to-end and hierarchical control architectures, then diagnoses the "curse of simulation" by identifying primary gap sources: robot dynamics, contact and terrain modeling, actuation, state estimation, and numerical solvers. Building on this diagnosis, the authors organize solutions along two complementary axes: improving the simulator's physical fidelity and hardening the policy against residual mismatches.

## Key Contributions

- Taxonomy of end-to-end and hierarchical DRL control architectures for bipedal locomotion.
- Diagnostic analysis of sim-to-real gap sources: robot dynamics, actuation, contact/terrain, sensing, and numerical solvers.
- Organization of sim-to-real methods into three levers: pre-training alignment, training for robustness, and post-deployment adaptation.
- Synthesis of practical guidelines and a roadmap toward real-world mastery via adaptive digital twins and lifelong learning.

## Relevance to Humanoid Robotics

Bipedal locomotion is a foundational capability for humanoid robots intended to operate in human-centric environments. Reliable sim-to-real transfer reduces the need for expensive and risky hardware training, accelerates controller iteration, and supports scalable deployment of mass-produced humanoids. The chapter's framework therefore has direct industry relevance for lowering the cost and improving the robustness of humanoid walking controllers.
