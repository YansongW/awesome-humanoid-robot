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
  en: Proposes DDBot, a framework that combines a GPU-accelerated differentiable MLS-MPM granular-material simulator with
    a parameterized differentiable digging skill to enable gradient-based system identification and high-precision digging-skill
    optimization for sand and soil with unknown physical properties, achieving zero-shot sim-to-real transfer on a UR5e arm.
  zh: 提出DDBot框架，结合GPU加速的可微MLS-MPM颗粒材料仿真器与参数化可微挖掘技能，实现对未知物理特性的沙土进行基于梯度的系统辨识与高精度挖掘技能优化，并在UR5e机械臂上实现零样本仿真到现实迁移。
  ko: GPU 가속 미분 가능 MLS-MPM 과립 재료 시뮬레이터와 매개변수화된 미분 가능 굴살 기술을 결합한 DDBot 프레임워크를 제안하여, 물리 특성을 알 수 없는 모래와 흙에 대한 그래디언트 기반 시스템 식별
    및 고정밀 굴살 기술 최적화를 가능하게 하고 UR5e 로봇 팔에서 제로샷 시뮬레이션-현실 전이를 달성함.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.17335v4.
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
## 概述
Automating the manipulation of granular materials poses significant challenges due to complex contact dynamics, unpredictable material properties, and intricate system states. Existing approaches often fail to achieve efficiency and accuracy in such tasks. To fill the research gap, this article studies the small-scale and high-precision granular material digging task with unknown physical properties. A key scientific problem addressed is the feasibility of applying first-order gradient-based optimization to complex differentiable granular material simulation and overcoming associated numerical instability. A new framework, named differentiable digging robot (DDBot), is proposed to manipulate granular materials, including sand and soil. Specifically, we equip DDBot with a differentiable physics-based simulator, tailored for granular material manipulation, powered by GPU-accelerated parallel computing and automatic differentiation. DDBot can perform efficient differentiable system identification and high-precision digging skill optimization for unknown granular materials, which is enabled by a differentiable skill-to-action mapping, a task-oriented demonstration method, gradient clipping and line search-based gradient descent. Experimental results show that DDBot can efficiently (converge within 5 to 20 minutes) identify unknown granular material dynamics and optimize digging skills, with high-precision results in zero-shot real-world deployments, highlighting its practicality. Benchmark results against state-of-the-art baselines also confirm the robustness and efficiency of DDBot in such digging tasks.

## 核心内容
Automating the manipulation of granular materials poses significant challenges due to complex contact dynamics, unpredictable material properties, and intricate system states. Existing approaches often fail to achieve efficiency and accuracy in such tasks. To fill the research gap, this article studies the small-scale and high-precision granular material digging task with unknown physical properties. A key scientific problem addressed is the feasibility of applying first-order gradient-based optimization to complex differentiable granular material simulation and overcoming associated numerical instability. A new framework, named differentiable digging robot (DDBot), is proposed to manipulate granular materials, including sand and soil. Specifically, we equip DDBot with a differentiable physics-based simulator, tailored for granular material manipulation, powered by GPU-accelerated parallel computing and automatic differentiation. DDBot can perform efficient differentiable system identification and high-precision digging skill optimization for unknown granular materials, which is enabled by a differentiable skill-to-action mapping, a task-oriented demonstration method, gradient clipping and line search-based gradient descent. Experimental results show that DDBot can efficiently (converge within 5 to 20 minutes) identify unknown granular material dynamics and optimize digging skills, with high-precision results in zero-shot real-world deployments, highlighting its practicality. Benchmark results against state-of-the-art baselines also confirm the robustness and efficiency of DDBot in such digging tasks.

## 参考
- http://arxiv.org/abs/2510.17335v4

## Overview
Automating the manipulation of granular materials poses significant challenges due to complex contact dynamics, unpredictable material properties, and intricate system states. Existing approaches often fail to achieve efficiency and accuracy in such tasks. To fill the research gap, this article studies the small-scale and high-precision granular material digging task with unknown physical properties. A key scientific problem addressed is the feasibility of applying first-order gradient-based optimization to complex differentiable granular material simulation and overcoming associated numerical instability. A new framework, named differentiable digging robot (DDBot), is proposed to manipulate granular materials, including sand and soil. Specifically, we equip DDBot with a differentiable physics-based simulator, tailored for granular material manipulation, powered by GPU-accelerated parallel computing and automatic differentiation. DDBot can perform efficient differentiable system identification and high-precision digging skill optimization for unknown granular materials, which is enabled by a differentiable skill-to-action mapping, a task-oriented demonstration method, gradient clipping and line search-based gradient descent. Experimental results show that DDBot can efficiently (converge within 5 to 20 minutes) identify unknown granular material dynamics and optimize digging skills, with high-precision results in zero-shot real-world deployments, highlighting its practicality. Benchmark results against state-of-the-art baselines also confirm the robustness and efficiency of DDBot in such digging tasks.

## Content
Automating the manipulation of granular materials poses significant challenges due to complex contact dynamics, unpredictable material properties, and intricate system states. Existing approaches often fail to achieve efficiency and accuracy in such tasks. To fill the research gap, this article studies the small-scale and high-precision granular material digging task with unknown physical properties. A key scientific problem addressed is the feasibility of applying first-order gradient-based optimization to complex differentiable granular material simulation and overcoming associated numerical instability. A new framework, named differentiable digging robot (DDBot), is proposed to manipulate granular materials, including sand and soil. Specifically, we equip DDBot with a differentiable physics-based simulator, tailored for granular material manipulation, powered by GPU-accelerated parallel computing and automatic differentiation. DDBot can perform efficient differentiable system identification and high-precision digging skill optimization for unknown granular materials, which is enabled by a differentiable skill-to-action mapping, a task-oriented demonstration method, gradient clipping and line search-based gradient descent. Experimental results show that DDBot can efficiently (converge within 5 to 20 minutes) identify unknown granular material dynamics and optimize digging skills, with high-precision results in zero-shot real-world deployments, highlighting its practicality. Benchmark results against state-of-the-art baselines also confirm the robustness and efficiency of DDBot in such digging tasks.

## 개요
입상 재료의 조작 자동화는 복잡한 접촉 역학, 예측 불가능한 재료 특성, 그리고 정교한 시스템 상태로 인해 상당한 도전 과제를 제기합니다. 기존 접근 방식은 이러한 작업에서 효율성과 정확성을 달성하는 데 종종 실패합니다. 이러한 연구 공백을 메우기 위해, 본 논문은 물리적 특성이 알려지지 않은 소규모 고정밀 입상 재료 굴착 작업을 연구합니다. 해결해야 할 핵심 과학적 문제는 1차 기울기 기반 최적화를 복잡한 미분 가능 입상 재료 시뮬레이션에 적용하고 관련 수치적 불안정성을 극복하는 가능성입니다. 모래와 흙을 포함한 입상 재료를 조작하기 위해 DDBot(Differentiable Digging Robot)이라는 새로운 프레임워크가 제안됩니다. 구체적으로, DDBot에는 GPU 가속 병렬 컴퓨팅과 자동 미분을 기반으로 하는 입상 재료 조작에 특화된 미분 가능 물리 기반 시뮬레이터가 탑재됩니다. DDBot은 미분 가능한 기술-행동 매핑, 작업 지향 시연 방법, 기울기 클리핑 및 라인 탐색 기반 경사 하강법을 통해 알려지지 않은 입상 재료에 대한 효율적인 미분 가능 시스템 식별과 고정밀 굴착 기술 최적화를 수행할 수 있습니다. 실험 결과는 DDBot이 알려지지 않은 입상 재료 역학을 효율적으로(5~20분 내 수렴) 식별하고 굴착 기술을 최적화할 수 있으며, 제로샷 실제 환경 배치에서 고정밀 결과를 보여줌으로써 실용성을 강조합니다. 최첨단 기준선과의 벤치마크 결과는 또한 이러한 굴착 작업에서 DDBot의 견고성과 효율성을 확인합니다.

## 핵심 내용
입상 재료의 조작 자동화는 복잡한 접촉 역학, 예측 불가능한 재료 특성, 그리고 정교한 시스템 상태로 인해 상당한 도전 과제를 제기합니다. 기존 접근 방식은 이러한 작업에서 효율성과 정확성을 달성하는 데 종종 실패합니다. 이러한 연구 공백을 메우기 위해, 본 논문은 물리적 특성이 알려지지 않은 소규모 고정밀 입상 재료 굴착 작업을 연구합니다. 해결해야 할 핵심 과학적 문제는 1차 기울기 기반 최적화를 복잡한 미분 가능 입상 재료 시뮬레이션에 적용하고 관련 수치적 불안정성을 극복하는 가능성입니다. 모래와 흙을 포함한 입상 재료를 조작하기 위해 DDBot(Differentiable Digging Robot)이라는 새로운 프레임워크가 제안됩니다. 구체적으로, DDBot에는 GPU 가속 병렬 컴퓨팅과 자동 미분을 기반으로 하는 입상 재료 조작에 특화된 미분 가능 물리 기반 시뮬레이터가 탑재됩니다. DDBot은 미분 가능한 기술-행동 매핑, 작업 지향 시연 방법, 기울기 클리핑 및 라인 탐색 기반 경사 하강법을 통해 알려지지 않은 입상 재료에 대한 효율적인 미분 가능 시스템 식별과 고정밀 굴착 기술 최적화를 수행할 수 있습니다. 실험 결과는 DDBot이 알려지지 않은 입상 재료 역학을 효율적으로(5~20분 내 수렴) 식별하고 굴착 기술을 최적화할 수 있으며, 제로샷 실제 환경 배치에서 고정밀 결과를 보여줌으로써 실용성을 강조합니다. 최첨단 기준선과의 벤치마크 결과는 또한 이러한 굴착 작업에서 DDBot의 견고성과 효율성을 확인합니다.
