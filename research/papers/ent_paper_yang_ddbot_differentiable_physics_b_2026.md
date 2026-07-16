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

## Overview
Automating the manipulation of granular materials poses significant challenges due to complex contact dynamics, unpredictable material properties, and intricate system states. Existing approaches often fail to achieve efficiency and accuracy in such tasks. To fill the research gap, this article studies the small-scale and high-precision granular material digging task with unknown physical properties. A key scientific problem addressed is the feasibility of applying first-order gradient-based optimization to complex differentiable granular material simulation and overcoming associated numerical instability. A new framework, named differentiable digging robot (DDBot), is proposed to manipulate granular materials, including sand and soil. Specifically, we equip DDBot with a differentiable physics-based simulator, tailored for granular material manipulation, powered by GPU-accelerated parallel computing and automatic differentiation. DDBot can perform efficient differentiable system identification and high-precision digging skill optimization for unknown granular materials, which is enabled by a differentiable skill-to-action mapping, a task-oriented demonstration method, gradient clipping and line search-based gradient descent. Experimental results show that DDBot can efficiently (converge within 5 to 20 minutes) identify unknown granular material dynamics and optimize digging skills, with high-precision results in zero-shot real-world deployments, highlighting its practicality. Benchmark results against state-of-the-art baselines also confirm the robustness and efficiency of DDBot in such digging tasks.

## Content
Automating the manipulation of granular materials poses significant challenges due to complex contact dynamics, unpredictable material properties, and intricate system states. Existing approaches often fail to achieve efficiency and accuracy in such tasks. To fill the research gap, this article studies the small-scale and high-precision granular material digging task with unknown physical properties. A key scientific problem addressed is the feasibility of applying first-order gradient-based optimization to complex differentiable granular material simulation and overcoming associated numerical instability. A new framework, named differentiable digging robot (DDBot), is proposed to manipulate granular materials, including sand and soil. Specifically, we equip DDBot with a differentiable physics-based simulator, tailored for granular material manipulation, powered by GPU-accelerated parallel computing and automatic differentiation. DDBot can perform efficient differentiable system identification and high-precision digging skill optimization for unknown granular materials, which is enabled by a differentiable skill-to-action mapping, a task-oriented demonstration method, gradient clipping and line search-based gradient descent. Experimental results show that DDBot can efficiently (converge within 5 to 20 minutes) identify unknown granular material dynamics and optimize digging skills, with high-precision results in zero-shot real-world deployments, highlighting its practicality. Benchmark results against state-of-the-art baselines also confirm the robustness and efficiency of DDBot in such digging tasks.

## 개요
입상 재료의 조작 자동화는 복잡한 접촉 역학, 예측 불가능한 재료 특성, 그리고 복잡한 시스템 상태로 인해 상당한 어려움을 야기합니다. 기존 접근 방식은 이러한 작업에서 효율성과 정확성을 달성하지 못하는 경우가 많습니다. 이러한 연구 공백을 메우기 위해, 본 논문은 물리적 특성이 알려지지 않은 소규모 고정밀 입상 재료 굴착 작업을 연구합니다. 다루는 주요 과학적 문제는 1차 기울기 기반 최적화를 복잡한 미분 가능 입상 재료 시뮬레이션에 적용하고 관련 수치적 불안정성을 극복하는 가능성입니다. 모래와 흙을 포함한 입상 재료를 조작하기 위해 DDBot(Differentiable Digging Robot)이라는 새로운 프레임워크가 제안됩니다. 구체적으로, DDBot에는 GPU 가속 병렬 컴퓨팅과 자동 미분으로 구동되는 입상 재료 조작에 특화된 미분 가능 물리 기반 시뮬레이터가 탑재됩니다. DDBot은 미분 가능한 기술-행동 매핑, 작업 지향 시연 방법, 기울기 클리핑 및 라인 탐색 기반 기울기 하강법을 통해 알려지지 않은 입상 재료에 대한 효율적인 미분 가능 시스템 식별과 고정밀 굴착 기술 최적화를 수행할 수 있습니다. 실험 결과는 DDBot이 알려지지 않은 입상 재료 역학을 효율적으로(5~20분 내에 수렴) 식별하고 굴착 기술을 최적화할 수 있으며, 제로샷 실제 환경 배치에서 고정밀 결과를 보여줌으로써 실용성을 강조합니다. 최첨단 기준선과의 벤치마크 결과는 이러한 굴착 작업에서 DDBot의 견고성과 효율성을 확인합니다.

## 핵심 내용
입상 재료의 조작 자동화는 복잡한 접촉 역학, 예측 불가능한 재료 특성, 그리고 복잡한 시스템 상태로 인해 상당한 어려움을 야기합니다. 기존 접근 방식은 이러한 작업에서 효율성과 정확성을 달성하지 못하는 경우가 많습니다. 이러한 연구 공백을 메우기 위해, 본 논문은 물리적 특성이 알려지지 않은 소규모 고정밀 입상 재료 굴착 작업을 연구합니다. 다루는 주요 과학적 문제는 1차 기울기 기반 최적화를 복잡한 미분 가능 입상 재료 시뮬레이션에 적용하고 관련 수치적 불안정성을 극복하는 가능성입니다. 모래와 흙을 포함한 입상 재료를 조작하기 위해 DDBot(Differentiable Digging Robot)이라는 새로운 프레임워크가 제안됩니다. 구체적으로, DDBot에는 GPU 가속 병렬 컴퓨팅과 자동 미분으로 구동되는 입상 재료 조작에 특화된 미분 가능 물리 기반 시뮬레이터가 탑재됩니다. DDBot은 미분 가능한 기술-행동 매핑, 작업 지향 시연 방법, 기울기 클리핑 및 라인 탐색 기반 기울기 하강법을 통해 알려지지 않은 입상 재료에 대한 효율적인 미분 가능 시스템 식별과 고정밀 굴착 기술 최적화를 수행할 수 있습니다. 실험 결과는 DDBot이 알려지지 않은 입상 재료 역학을 효율적으로(5~20분 내에 수렴) 식별하고 굴착 기술을 최적화할 수 있으며, 제로샷 실제 환경 배치에서 고정밀 결과를 보여줌으로써 실용성을 강조합니다. 최첨단 기준선과의 벤치마크 결과는 이러한 굴착 작업에서 DDBot의 견고성과 효율성을 확인합니다.
