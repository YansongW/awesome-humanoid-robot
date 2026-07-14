---
$id: ent_paper_jiang_cpg_based_manipulation_with_mu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: CPG-Based Manipulation with Multi-Module Origami Robot Surface
  zh: 基于中枢模式发生器的多模块折纸机器人表面操作
  ko: CPG 기반 다중 모듈 종이 접기 로봇 표면 조작
summary:
  en: This paper presents a CPG-based motion generator combined with simulation-based Bayesian optimization to control a 5×5
    multi-module origami robotic surface (Ori-Pixel) for manipulating objects ranging from centimeters to meters in size with
    varying stiffness and shape.
  zh: 本文提出了一种基于中枢模式发生器（CPG）的运动生成器，结合基于仿真的贝叶斯优化方法，控制5×5多模块折纸机器人表面（Ori-Pixel），以操作尺寸从厘米到米、刚度与形状各异的物体。
  ko: 본 논문은 시뮬레이션 기반 베이지안 최적화와 결합된 CPG 기반 운동 생성기를 제안하여 5×5 다중 모듈 종이 접기 로봇 표면(Ori-Pixel)을 제어하여 크기와 강도, 형태가 다양한 센티미터에서 미터 크기의
    물체를 조작한다.
domains:
- 02_components
- 07_ai_models_algorithms
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- cpg
- origami_robot
- robotic_surface
- distributed_manipulation
- sim_to_real
- bayesian_optimization
- reconfigurable_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.19218v1.
sources:
- id: src_001
  type: paper
  title: CPG-Based Manipulation with Multi-Module Origami Robot Surface
  url: https://arxiv.org/abs/2502.19218
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Robotic manipulators often face challenges in handling objects of different sizes and materials, limiting their effectiveness in practical applications. This issue is particularly pronounced when manipulating meter-scale objects or those with varying stiffness, as traditional gripping techniques and strategies frequently prove inadequate. In this letter, we introduce a novel surface-based multi-module robotic manipulation framework that utilizes a Central Pattern Generator (CPG)-based motion generator, combined with a simulation-based optimization method to determine the optimal manipulation parameters for a multi-module origami robotic surface (Ori-Pixel). This approach allows for the manipulation of objects ranging from centimeters to meters in size, with varying stiffness and shape. The optimized CPG parameters are tested through both dynamic simulations and a series of prototype experiments involving a wide range of objects differing in size, weight, shape, and material, demonstrating robust manipulation capabilities.

## 核心内容
Robotic manipulators often face challenges in handling objects of different sizes and materials, limiting their effectiveness in practical applications. This issue is particularly pronounced when manipulating meter-scale objects or those with varying stiffness, as traditional gripping techniques and strategies frequently prove inadequate. In this letter, we introduce a novel surface-based multi-module robotic manipulation framework that utilizes a Central Pattern Generator (CPG)-based motion generator, combined with a simulation-based optimization method to determine the optimal manipulation parameters for a multi-module origami robotic surface (Ori-Pixel). This approach allows for the manipulation of objects ranging from centimeters to meters in size, with varying stiffness and shape. The optimized CPG parameters are tested through both dynamic simulations and a series of prototype experiments involving a wide range of objects differing in size, weight, shape, and material, demonstrating robust manipulation capabilities.

## 参考
- http://arxiv.org/abs/2502.19218v1

