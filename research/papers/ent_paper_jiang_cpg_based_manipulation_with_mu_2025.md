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
  en: This paper presents a CPG-based motion generator combined with simulation-based
    Bayesian optimization to control a 5×5 multi-module origami robotic surface (Ori-Pixel)
    for manipulating objects ranging from centimeters to meters in size with varying
    stiffness and shape.
  zh: 本文提出了一种基于中枢模式发生器（CPG）的运动生成器，结合基于仿真的贝叶斯优化方法，控制5×5多模块折纸机器人表面（Ori-Pixel），以操作尺寸从厘米到米、刚度与形状各异的物体。
  ko: 본 논문은 시뮬레이션 기반 베이지안 최적화와 결합된 CPG 기반 운동 생성기를 제안하여 5×5 다중 모듈 종이 접기 로봇 표면(Ori-Pixel)을
    제어하여 크기와 강도, 형태가 다양한 센티미터에서 미터 크기의 물체를 조작한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full paper not independently read.
    Citation text for relationships should be confirmed against the PDF.
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

## Overview

Traditional robotic grippers and arm-based manipulators are often limited when handling objects that differ substantially in size, stiffness, shape, and material, particularly at meter scales or with highly flexible objects. To address this, the authors propose a surface-based multi-module robotic manipulation framework centered on a 5×5 origami robotic surface called Ori-Pixel. The framework is driven by a Central Pattern Generator (CPG)-based motion generator, which coordinates the cyclic actuation of multiple surface modules to produce collective manipulation behaviors such as fast translation, smooth translation, and in-plane rotation.

The CPG parameters for a given object and manipulation mode are selected through a simulation-based Bayesian hyperparameter optimization process. The optimizer searches over CPG settings to maximize a task-specific objective, and the resulting parameters are then transferred to the physical prototype. The authors validate the approach through dynamic simulations and physical experiments on a diverse set of objects, including acrylic plates, wood plates, foam cylinders, fabric, and a straw hat, demonstrating manipulation across centimeter-to-meter scales and a range of stiffness values.

The hardware platform uses the Canfield parallel origami robot as the basic building block of each Ori-Pixel module, actuated by Dynamixel XL-320 servo motors. The modular origami structure allows each tile to deform in a controlled way, and the CPG coordinates phase and amplitude relationships among tiles to generate global motion patterns.

## Key Contributions

- A novel CPG-based motion generator for multi-module robot-surface manipulation, enabling collective manipulation modes for objects of diverse sizes and stiffness.
- A simulation-based optimization framework for selecting optimal CPG parameters across different object settings and manipulation modes (fast, smooth, rotational).
- Validation through dynamic simulations and prototype experiments demonstrating robust manipulation of objects with varying sizes, shapes, and stiffness.

## Relevance to Humanoid Robotics

Although the work focuses on a specialized surface-manipulation platform rather than a full humanoid robot, it is relevant to humanoid robotics because distributed, adaptive manipulation is a core subsystem capability. Humanoid robots must handle objects of varying size, compliance, and shape during assistive or industrial tasks, and the CPG-based coordination approach demonstrated here could inform design of torso, belly, or hand-mounted distributed manipulators. The sim-to-real optimization pipeline is also transferable to humanoid subsystems where many actuated degrees of freedom must be coordinated to manipulate large or deformable objects.
