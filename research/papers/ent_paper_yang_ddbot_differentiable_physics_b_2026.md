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
  en: DDBot is a differentiable physics-based framework for small-scale, high-precision robotic digging of sand and soil with
    unknown material properties. It combines a GPU-accelerated MLS-MPM simulator, a differentiable digging skill, target-oriented
    demonstrations, and gradient clipping with line-search gradient descent to enable efficient system identification and
    zero-shot sim-to-real skill optimization.
  zh: DDBot是一个面向未知物理特性沙土材料的小规模高精度机器人挖掘框架，结合GPU加速的MLS-MPM可微物理仿真器、可微挖掘技能、面向目标的示教以及梯度裁剪与线搜索梯度下降，实现高效的系统辨识和零样本仿真到现实的技能优化。
  ko: DDBot는 미지의 물리적 특성을 가진 모래와 흙의 소규모 고정밀 로봇 굴삭을 위한 미분 가능 물리 기반 프레임워크로, GPU 가속 MLS-MPM 시뮬레이터, 미분 가능 굴삭 스킬, 목표 지향 시연, 그리고
    그래디언트 클리핑과 선 탐색 기반 그래디언트 강하를 결합하여 효율적인 시스템 식별과 제로샷 시뮬레이션-투-리얼 스킬 최적화를 수행한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.17335v4.
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
## 概述
Automating the manipulation of granular materials poses significant challenges due to complex contact dynamics, unpredictable material properties, and intricate system states. Existing approaches often fail to achieve efficiency and accuracy in such tasks. To fill the research gap, this article studies the small-scale and high-precision granular material digging task with unknown physical properties. A key scientific problem addressed is the feasibility of applying first-order gradient-based optimization to complex differentiable granular material simulation and overcoming associated numerical instability. A new framework, named differentiable digging robot (DDBot), is proposed to manipulate granular materials, including sand and soil. Specifically, we equip DDBot with a differentiable physics-based simulator, tailored for granular material manipulation, powered by GPU-accelerated parallel computing and automatic differentiation. DDBot can perform efficient differentiable system identification and high-precision digging skill optimization for unknown granular materials, which is enabled by a differentiable skill-to-action mapping, a task-oriented demonstration method, gradient clipping and line search-based gradient descent. Experimental results show that DDBot can efficiently (converge within 5 to 20 minutes) identify unknown granular material dynamics and optimize digging skills, with high-precision results in zero-shot real-world deployments, highlighting its practicality. Benchmark results against state-of-the-art baselines also confirm the robustness and efficiency of DDBot in such digging tasks.

## 核心内容
Automating the manipulation of granular materials poses significant challenges due to complex contact dynamics, unpredictable material properties, and intricate system states. Existing approaches often fail to achieve efficiency and accuracy in such tasks. To fill the research gap, this article studies the small-scale and high-precision granular material digging task with unknown physical properties. A key scientific problem addressed is the feasibility of applying first-order gradient-based optimization to complex differentiable granular material simulation and overcoming associated numerical instability. A new framework, named differentiable digging robot (DDBot), is proposed to manipulate granular materials, including sand and soil. Specifically, we equip DDBot with a differentiable physics-based simulator, tailored for granular material manipulation, powered by GPU-accelerated parallel computing and automatic differentiation. DDBot can perform efficient differentiable system identification and high-precision digging skill optimization for unknown granular materials, which is enabled by a differentiable skill-to-action mapping, a task-oriented demonstration method, gradient clipping and line search-based gradient descent. Experimental results show that DDBot can efficiently (converge within 5 to 20 minutes) identify unknown granular material dynamics and optimize digging skills, with high-precision results in zero-shot real-world deployments, highlighting its practicality. Benchmark results against state-of-the-art baselines also confirm the robustness and efficiency of DDBot in such digging tasks.

## 参考
- http://arxiv.org/abs/2510.17335v4

