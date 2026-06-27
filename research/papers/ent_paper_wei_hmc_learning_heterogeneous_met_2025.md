---
$id: ent_paper_wei_hmc_learning_heterogeneous_met_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation'
  zh: HMC：面向接触密集型移动操作任务的异构元控制学习
  ko: 'HMC: 접촉이 풍부한 로코 매니퓰레이션을 위한 이종 메타 제어 학습'
summary:
  en: HMC introduces a torque-space meta-controller that continuously blends position,
    impedance, and hybrid force-position actions, learned by a heterogeneous Mixture-of-Experts
    policy and validated on a Unitree G1 humanoid for contact-rich loco-manipulation.
  zh: HMC 提出一种在力矩空间连续融合位置、阻抗和力/位混合控制的异构元控制框架，通过异构混合专家策略学习，并在 Unitree G1 人形机器人上验证了接触密集型移动操作任务。
  ko: HMC는 토크 공간에서 위치, 임피던스, 힘-위치 혼합 제어를 연속적으로 혼합하는 이종 메타 제어 프레임워크를 제안하며, 이종 혼합 전문가
    정책으로 학습하고 Unitree G1 휴머노이드에서 접촉이 풍부한 로코 매니퓰레이션을 검증했다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- loco_manipulation
- contact_rich_manipulation
- force_control
- impedance_control
- hybrid_force_position_control
- mixture_of_experts
- meta_control
- teleoperation
- unitree_g1
- real_world_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the provided abstract and metadata. Independent full-text
    review is needed before promotion to verified.
sources:
- id: src_001
  type: paper
  title: 'HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation'
  url: https://arxiv.org/abs/2511.14756
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
related_entities:
- id: ent_robot_system_unitree_g1
  relationship: evaluates_on
  description:
    en: The paper evaluates the HMC framework on a real Unitree G1 humanoid robot.
    zh: 该论文在真实的 Unitree G1 人形机器人上验证了 HMC 框架。
    ko: 해당 논문은 실제 Unitree G1 휴머노이드 로봇에서 HMC 프레임워크를 평가했다.
---

## Overview

HMC (Heterogeneous Meta-Control) is a learning and control framework designed for contact-rich loco-manipulation on real humanoid robots. It addresses the limitation of purely positional controllers, which often fail when interaction dynamics vary due to contact, compliance, or payload changes. The core idea is to treat multiple control modalities—position, impedance, and hybrid force-position—as experts that can be continuously blended in torque space through a unified interface called HMC-Controller.

To learn when and how to blend these modalities, the authors propose HMC-Policy, a heterogeneous policy architecture that uses soft Mixture-of-Experts routing. The routing mechanism is trained in two stages: first on large-scale position-only teleoperation data, then fine-tuned on smaller, force-aware multi-expert demonstrations. This design aims to avoid expert collapse and to enable smooth transitions between control modalities during execution.

The framework is validated on a real Unitree G1 humanoid equipped with an Intel RealSense D435i camera and using the OpenTV teleoperation system for data collection. Experiments include compliant table wiping, bottle lifting, and drawer opening, with reported improvements of over 50% relative to baseline methods.

## Key Contributions

- HMC-Controller: a unified torque-space interface that continuously blends position, impedance, and hybrid force-position control profiles for both teleoperation and policy deployment.
- HMC-Policy: a heterogeneous policy architecture with soft Mixture-of-Experts routing to avoid expert collapse and enable smooth transitions between control modalities.
- A two-stage pretrain-finetune learning procedure that leverages abundant position-only data before fine-tuning on scarce force-aware demonstrations.
- Real-world validation on a Unitree G1 humanoid across contact-rich tasks including wiping, bottle lifting, and drawer opening.

## Relevance to Humanoid Robotics

The work is directly relevant to humanoid deployment because it targets a key gap in real-world operation: adaptive, force-aware control during contact-rich manipulation while locomoting. Humanoid robots must interact with diverse, uncertain environments, and pure position tracking is often insufficient for tasks that require compliance or controlled contact forces. HMC provides a learning-based method for selecting and blending low-level control behaviors on a real humanoid platform.

By demonstrating over 50% relative improvement on physically realistic tasks such as compliant wiping and drawer opening, the paper supports the broader goal of moving humanoid robots from controlled laboratory settings toward robust industrial or service applications.
