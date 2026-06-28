---
$id: ent_paper_yang_ddbot_differentiable_physics_b_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DDBot: Differentiable Physics-based Digging Robot for Unknown Granular Materials'
  zh: DDBot：面向未知颗粒材料的可微物理挖掘机器人
  ko: 'DDBot: 미지의 과립 재료를 위한 미분 가능 물리 기반 굴살 로봇'
summary:
  en: Proposes DDBot, a framework that combines a GPU-accelerated differentiable MLS-MPM
    granular-material simulator with a parameterized differentiable digging skill
    to enable gradient-based system identification and high-precision digging-skill
    optimization for sand and soil with unknown physical properties, achieving zero-shot
    sim-to-real transfer on a UR5e arm.
  zh: 提出DDBot框架，结合GPU加速的可微MLS-MPM颗粒材料仿真器与参数化可微挖掘技能，实现对未知物理特性的沙土进行基于梯度的系统辨识与高精度挖掘技能优化，并在UR5e机械臂上实现零样本仿真到现实迁移。
  ko: GPU 가속 미분 가능 MLS-MPM 과립 재료 시뮬레이터와 매개변수화된 미분 가능 굴살 기술을 결합한 DDBot 프레임워크를 제안하여,
    물리 특성을 알 수 없는 모래와 흙에 대한 그래디언트 기반 시스템 식별 및 고정밀 굴살 기술 최적화를 가능하게 하고 UR5e 로봇 팔에서 제로샷
    시뮬레이션-현실 전이를 달성함.
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
- differentiable_physics
- granular_material_manipulation
- digging_skill_optimization
- sim_to_real
- system_identification
- mls_mpm
- robotic_digging
- ur5e
- gpu_accelerated_simulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review of
    the full paper before verification.
sources:
- id: src_001
  type: paper
  title: 'DDBot: Differentiable Physics-based Digging Robot for Unknown Granular Materials'
  url: https://arxiv.org/abs/2510.17335
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

DDBot addresses the challenge of automating small-scale, high-precision digging in granular materials such as sand and soil whose physical properties are unknown. The work is motivated by the inefficiency and inaccuracy of existing robotic approaches when faced with complex contact dynamics, unpredictable material properties, and intricate system states. The core proposal is a differentiable physics-based framework that tightly couples simulation and skill optimization so that gradients can propagate from task objectives back to both material parameters and digging actions.

The framework's simulator is a GPU-accelerated Moving Least Squares Material Point Method (MLS-MPM) model tailored for granular manipulation. It represents the material using St. Venant-Kirchhoff (SVK) elasticity combined with Drucker-Prager plasticity, enabling it to capture the elastic and failure behavior of sand and soil. To make long-horizon optimization feasible, the authors introduce gradient stabilization techniques including gradient clipping and a line-search-based gradient descent procedure. A parameterized differentiable digging skill is then optimized end-to-end against target-oriented demonstrations.

Real-world validation is performed on a UR5e robotic arm equipped with a 3D-printed shovel and a Zivid Medium One+ camera, housed in a wooden container. The system achieves zero-shot sim-to-real transfer with location and depth errors below 6 mm. The authors also benchmark DDBot against trajectory optimization, CMA-MAE, and goal-conditioned SAC, reporting superior robustness and efficiency.

## Key Contributions

- First differentiable physics simulator specifically tailored for efficient, high-fidelity granular material manipulation.
- DDBot framework enabling gradient-based system identification and high-precision digging-skill optimisation for unknown sand and soil.
- Gradient stabilisation techniques (gradient clipping and line search) that make first-order optimisation feasible for long-horizon granular dynamics.
- Real-world zero-shot sim-to-real deployment on a UR5e arm, with location and depth errors below 6 mm.
- Benchmarking against trajectory optimisation, CMA-MAE, and goal-conditioned SAC, showing superior robustness and efficiency.

## Relevance to Humanoid Robotics

Automated precision digging and soil handling is a necessary capability for humanoid robots deployed at scale in agriculture, greenhouse planting, construction, disaster rescue, and extraterrestrial exploration. The differentiable simulation and optimization methods introduced in DDBot are not specific to a particular manipulator; in principle, the same gradients and skill representations can be transferred to humanoid hands or end-effectors that must interact with loose, deformable terrain. As humanoids move from flat floors into unstructured outdoor and agricultural environments, the ability to identify unknown material parameters online and optimize digging actions with millimeter-level accuracy becomes a foundational manipulation skill.
