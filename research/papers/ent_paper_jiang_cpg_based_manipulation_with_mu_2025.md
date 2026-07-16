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

## Overview
Robotic manipulators often face challenges in handling objects of different sizes and materials, limiting their effectiveness in practical applications. This issue is particularly pronounced when manipulating meter-scale objects or those with varying stiffness, as traditional gripping techniques and strategies frequently prove inadequate. In this letter, we introduce a novel surface-based multi-module robotic manipulation framework that utilizes a Central Pattern Generator (CPG)-based motion generator, combined with a simulation-based optimization method to determine the optimal manipulation parameters for a multi-module origami robotic surface (Ori-Pixel). This approach allows for the manipulation of objects ranging from centimeters to meters in size, with varying stiffness and shape. The optimized CPG parameters are tested through both dynamic simulations and a series of prototype experiments involving a wide range of objects differing in size, weight, shape, and material, demonstrating robust manipulation capabilities.

## Content
Robotic manipulators often face challenges in handling objects of different sizes and materials, limiting their effectiveness in practical applications. This issue is particularly pronounced when manipulating meter-scale objects or those with varying stiffness, as traditional gripping techniques and strategies frequently prove inadequate. In this letter, we introduce a novel surface-based multi-module robotic manipulation framework that utilizes a Central Pattern Generator (CPG)-based motion generator, combined with a simulation-based optimization method to determine the optimal manipulation parameters for a multi-module origami robotic surface (Ori-Pixel). This approach allows for the manipulation of objects ranging from centimeters to meters in size, with varying stiffness and shape. The optimized CPG parameters are tested through both dynamic simulations and a series of prototype experiments involving a wide range of objects differing in size, weight, shape, and material, demonstrating robust manipulation capabilities.

## 개요
로봇 매니퓰레이터는 다양한 크기와 재질의 물체를 다루는 데 종종 어려움을 겪으며, 이는 실제 응용에서 그 효과성을 제한합니다. 특히 미터 단위의 물체나 강성이 다양한 물체를 조작할 때 이러한 문제가 두드러지며, 전통적인 파지 기술과 전략은 종종 부적합합니다. 본 논문에서는 중앙 패턴 생성기(CPG) 기반 동작 생성기를 활용하고, 시뮬레이션 기반 최적화 방법을 결합하여 다중 모듈 오리가미 로봇 표면(Ori-Pixel)의 최적 조작 파라미터를 결정하는 새로운 표면 기반 다중 모듈 로봇 조작 프레임워크를 소개합니다. 이 접근 방식은 센티미터에서 미터 단위까지의 크기와 다양한 강성 및 형태를 가진 물체를 조작할 수 있게 합니다. 최적화된 CPG 파라미터는 동적 시뮬레이션과 크기, 무게, 형태, 재질이 다양한 광범위한 물체를 대상으로 한 일련의 프로토타입 실험을 통해 테스트되었으며, 강력한 조작 능력을 입증했습니다.

## 핵심 내용
로봇 매니퓰레이터는 다양한 크기와 재질의 물체를 다루는 데 종종 어려움을 겪으며, 이는 실제 응용에서 그 효과성을 제한합니다. 특히 미터 단위의 물체나 강성이 다양한 물체를 조작할 때 이러한 문제가 두드러지며, 전통적인 파지 기술과 전략은 종종 부적합합니다. 본 논문에서는 중앙 패턴 생성기(CPG) 기반 동작 생성기를 활용하고, 시뮬레이션 기반 최적화 방법을 결합하여 다중 모듈 오리가미 로봇 표면(Ori-Pixel)의 최적 조작 파라미터를 결정하는 새로운 표면 기반 다중 모듈 로봇 조작 프레임워크를 소개합니다. 이 접근 방식은 센티미터에서 미터 단위까지의 크기와 다양한 강성 및 형태를 가진 물체를 조작할 수 있게 합니다. 최적화된 CPG 파라미터는 동적 시뮬레이션과 크기, 무게, 형태, 재질이 다양한 광범위한 물체를 대상으로 한 일련의 프로토타입 실험을 통해 테스트되었으며, 강력한 조작 능력을 입증했습니다.
