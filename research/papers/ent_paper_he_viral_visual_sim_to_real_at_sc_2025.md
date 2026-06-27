---
$id: ent_paper_he_viral_visual_sim_to_real_at_sc_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation'
  zh: VIRAL：面向人形机器人移动操作的大规模视觉仿真到现实迁移
  ko: 'VIRAL: 인간형 로봇 로코-매니퓰레이션을 위한 대규모 비전 시뮬레이션-투-리얼'
summary:
  en: VIRAL is a visual sim-to-real framework that trains a privileged RL teacher
    for humanoid loco-manipulation entirely in simulation and distills it into an
    RGB-only student policy, enabling zero-shot deployment on a Unitree G1 humanoid.
  zh: VIRAL 是一种视觉仿真到现实迁移框架，仅在仿真中训练特权强化学习教师策略，并将其蒸馏为仅依赖 RGB 图像的学生策略，从而实现宇树 G1 人形机器人移动操作技能的零样本真实部署。
  ko: VIRAL은 시뮬레이션에서 특권 RL 교사 정책을 학습하고 RGB 전용 학생 정책으로 증류하여 인간형 로봇의 로코-매니퓰레이션 기술을 실제
    하드웨어에 제로샷으로 배포하는 비전 기반 시뮬-투-리얼 프레임워크이다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- visual_sim_to_real
- loco_manipulation
- humanoid_robotics
- teacher_student_distillation
- domain_randomization
- rgb_policy
- zero_shot_transfer
- unitree_g1
- whole_body_control
- dagger_behavior_cloning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the full arXiv HTML text; requires human review before
    final verification.
sources:
- id: src_001
  type: paper
  title: 'VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2511.15200
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

A key barrier to real-world humanoid robots is the lack of autonomous loco-manipulation skills that tightly coordinate locomotion and object manipulation under onboard perception over long horizons. VIRAL addresses this by learning humanoid loco-manipulation entirely in simulation and deploying the resulting policy zero-shot to real hardware. It follows a teacher-student design: a privileged RL teacher with access to full state learns long-horizon walking, placing, grasping, and turning behaviors using a delta action space and reference-state initialization on top of a pretrained whole-body controller.

The vision-based student observes only RGB images and robot proprioception. It is distilled from the teacher via large-scale simulation with tiled rendering, scaling to 64 GPUs, using a mixture of online DAgger and behavior cloning and a DINOv3 vision backbone. To close the sim-to-real gap, VIRAL applies extensive visual domain randomization over lighting, materials, camera parameters, image quality, and sensor delays, together with real-to-sim alignment of the dexterous hands and cameras. Deployed on a Unitree G1 with an Intel RealSense D435i, the RGB policy performs continuous loco-manipulation for up to 54 cycles without any real-world fine-tuning and generalizes across spatial and appearance variations.

## Key Contributions

- Teacher-student visual sim-to-real framework for humanoid loco-manipulation.
- Large-scale visual simulation with tiled rendering scaling up to 64 GPUs for reliable vision-based distillation.
- Delta action space and reference-state initialization to stabilize long-horizon RL.
- Extensive visual domain randomization plus real-to-sim alignment of dexterous hands and cameras.
- Zero-shot deployment on Unitree G1 achieving 54 continuous loco-manipulation cycles.

## Relevance to Humanoid Robotics

VIRAL is highly relevant to humanoid robotics because it provides a scalable, simulation-first pipeline for autonomous RGB-based loco-manipulation without requiring costly per-task real-world teleoperation data. By showing that compute scale, careful action representations, and systematic visual randomization together enable zero-shot hardware transfer, it offers a practical path toward mass deployment of general-purpose humanoid systems. The work also identifies the remaining coverage gaps in physics, task generation, reward engineering, and dexterous hardware that must be solved to broaden applicability.
