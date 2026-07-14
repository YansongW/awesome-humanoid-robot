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
  en: VIRAL is a visual sim-to-real framework that trains a privileged RL teacher for humanoid loco-manipulation entirely
    in simulation and distills it into an RGB-only student policy, enabling zero-shot deployment on a Unitree G1 humanoid.
  zh: VIRAL 是一种视觉仿真到现实迁移框架，仅在仿真中训练特权强化学习教师策略，并将其蒸馏为仅依赖 RGB 图像的学生策略，从而实现宇树 G1 人形机器人移动操作技能的零样本真实部署。
  ko: VIRAL은 시뮬레이션에서 특권 RL 교사 정책을 학습하고 RGB 전용 학생 정책으로 증류하여 인간형 로봇의 로코-매니퓰레이션 기술을 실제 하드웨어에 제로샷으로 배포하는 비전 기반 시뮬-투-리얼 프레임워크이다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.15200v2.
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
## 概述
A key barrier to the real-world deployment of humanoid robots is the lack of autonomous loco-manipulation skills. We introduce VIRAL, a visual sim-to-real framework that learns humanoid loco-manipulation entirely in simulation and deploys it zero-shot to real hardware. VIRAL follows a teacher-student design: a privileged RL teacher, operating on full state, learns long-horizon loco-manipulation using a delta action space and reference state initialization. A vision-based student policy is then distilled from the teacher via large-scale simulation with tiled rendering, trained with a mixture of online DAgger and behavior cloning. We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. To bridge the sim-to-real gap, VIRAL combines large-scale visual domain randomization over lighting, materials, camera parameters, image quality, and sensor delays--with real-to-sim alignment of the dexterous hands and cameras. Deployed on a Unitree G1 humanoid, the resulting RGB-based policy performs continuous loco-manipulation for up to 54 cycles, generalizing to diverse spatial and appearance variations without any real-world fine-tuning, and approaching expert-level teleoperation performance. Extensive ablations dissect the key design choices required to make RGB-based humanoid loco-manipulation work in practice.

## 核心内容
A key barrier to the real-world deployment of humanoid robots is the lack of autonomous loco-manipulation skills. We introduce VIRAL, a visual sim-to-real framework that learns humanoid loco-manipulation entirely in simulation and deploys it zero-shot to real hardware. VIRAL follows a teacher-student design: a privileged RL teacher, operating on full state, learns long-horizon loco-manipulation using a delta action space and reference state initialization. A vision-based student policy is then distilled from the teacher via large-scale simulation with tiled rendering, trained with a mixture of online DAgger and behavior cloning. We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. To bridge the sim-to-real gap, VIRAL combines large-scale visual domain randomization over lighting, materials, camera parameters, image quality, and sensor delays--with real-to-sim alignment of the dexterous hands and cameras. Deployed on a Unitree G1 humanoid, the resulting RGB-based policy performs continuous loco-manipulation for up to 54 cycles, generalizing to diverse spatial and appearance variations without any real-world fine-tuning, and approaching expert-level teleoperation performance. Extensive ablations dissect the key design choices required to make RGB-based humanoid loco-manipulation work in practice.

## 参考
- http://arxiv.org/abs/2511.15200v2

