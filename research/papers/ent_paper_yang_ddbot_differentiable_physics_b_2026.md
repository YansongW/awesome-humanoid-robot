---
$id: ent_paper_yang_ddbot_differentiable_physics_b_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DDBot: Differentiable Physics-based Digging Robot for Unknown Granular Materials'
  zh: DDBot：面向未知颗粒材料的可微物理挖掘机器人
  ko: 'DDBot: 미분 가능 물리 기반 미지 입자 재료 굴삭 로봇'
summary:
  en: DDBot is a differentiable physics-based framework for small-scale, high-precision
    robotic digging of sand and soil with unknown material properties. It combines
    a GPU-accelerated MLS-MPM simulator, a differentiable digging skill, target-oriented
    demonstrations, and gradient clipping with line-search gradient descent to enable
    efficient system identification and zero-shot sim-to-real skill optimization.
  zh: DDBot是一个面向未知物理特性沙土材料的小规模高精度机器人挖掘框架，结合GPU加速的MLS-MPM可微物理仿真器、可微挖掘技能、面向目标的示教以及梯度裁剪与线搜索梯度下降，实现高效的系统辨识和零样本仿真到现实的技能优化。
  ko: DDBot는 미지의 물리적 특성을 가진 모래와 흙의 소규모 고정밀 로봇 굴삭을 위한 미분 가능 물리 기반 프레임워크로, GPU 가속 MLS-MPM
    시뮬레이터, 미분 가능 굴삭 스킬, 목표 지향 시연, 그리고 그래디언트 클리핑과 선 탐색 기반 그래디언트 강하를 결합하여 효율적인 시스템 식별과
    제로샷 시뮬레이션-투-리얼 스킬 최적화를 수행한다.
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
- sim_to_real
- system_identification
- skill_optimization
- mls_mpm
- digging_robot
- robot_manipulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the arXiv full text; requires human review before full
    verification.
sources:
- id: src_001
  type: paper
  title: 'DDBot: Differentiable Physics-based Digging Robot for Unknown Granular Materials'
  url: https://arxiv.org/abs/2510.17335
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

DDBot addresses small-scale, high-precision robotic digging of granular materials such as sand and soil whose physical properties are unknown. The framework centers on a GPU-accelerated differentiable physics simulator tailored for granular manipulation, which is built upon the Moving Least Squares Material Point Method (MLS-MPM) with St. Venant-Kirchhoff (SVK) hyperelasticity and Drucker-Prager (DP) plasticity. By backpropagating gradients through the simulator, DDBot simultaneously identifies unknown material parameters and optimizes a low-dimensional differentiable digging skill, using target-oriented demonstrations as initialization and gradient-stabilization techniques to handle exploding gradients and rugged loss landscapes.

The real-world system consists of a UR5e robotic arm fitted with a 3D-printed shovel, a Zivid Medium One+ depth camera for capturing surface point clouds, and ROS/MoveIt! for robot communication and motion planning. The optimized digging skills are transferred to the physical robot without any real-world adaptation (zero-shot sim-to-real transfer), achieving location and depth errors below 6 mm and area error around 10.8 cm² for both sand and soil. Optimization typically converges within 5 to 20 minutes depending on initialization quality.

## Key Contributions

- First efficient, high-fidelity differentiable physics simulator specifically designed for granular material manipulation.
- DDBot framework enabling gradient-based system identification and high-precision digging skill optimization for unknown granular materials.
- Differentiable digging skill parameterization, target-oriented demonstrations, and gradient stabilization techniques (gradient clipping and line search).
- Real-world validation on a UR5e robot with soil and sand, achieving sub-centimeter zero-shot sim-to-real digging accuracy.

## Relevance to Humanoid Robotics

Although the experiments use a UR5e industrial arm rather than a full humanoid, the methods are directly relevant to humanoid robotics. Construction, agriculture, and excavation are key application areas for humanoid robots, and these tasks require precise manipulation of granular materials such as soil and sand. The differentiable simulation, system identification, and sim-to-real skill optimization pipeline presented in DDBot provide a transferable recipe for equipping humanoid platforms with precision digging and material-handling capabilities in unstructured outdoor environments.
