---
$id: ent_paper_mahapatra_3d_printed_cable_driven_contin_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '3D printed cable-driven continuum robots with generally routed cables: modeling
    and experiments'
  zh: 具有一般布线方式的3D打印缆索驱动连续体机器人：建模与实验
  ko: '일반적인 케이블 라우팅을 가진 3D 프린팅 케이블 구동 연속체 로봇: 모델링 및 실험'
summary:
  en: Compares a discrete optimization-based kinematic model with a Cosserat-rod static
    model for six general cable routings of a 3D-printed continuum robot, validates
    predictions within 2% of robot length, and demonstrates a three-fingered gripper.
  zh: 对3D打印连续体机器人的六种一般缆索布线方式，比较基于离散优化的运动学模型与Cosserat杆静力学模型，验证理论预测误差在机器人长度的2%以内，并展示了三指夹持器。
  ko: 3D 프린팅 연속체 로봇의 6가지 일반적인 케이블 라우팅에 대해 이산 최적화 기반 운동학 모델과 Cosserat 막대 정적 모델을 비교하고,
    이론 예측이 로봇 길이의 2% 이내임을 검증하며, 3지 그리퍼를 시연한다.
domains:
- 02_components
- 06_design_engineering
- 03_manufacturing_processes
layers:
- midstream
functional_roles:
- knowledge
- component
- system
tags:
- continuum_robot
- cable_driven_robot
- soft_robotics
- 3d_printing
- gripper
- robotic_finger
- cosserat_rod
- kinematic_modeling
- abs
- additive_manufacturing
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from arXiv full text (2003.04593); requires human review before
    verification.
sources:
- id: src_001
  type: paper
  title: '3D printed cable-driven continuum robots with generally routed cables: modeling
    and experiments'
  url: https://arxiv.org/abs/2003.04593
  date: '2020'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
- system
---

## Overview

This 2020 arXiv paper by Soumya Kanti Mahapatra, Ashwin K. P., and Ashitava Ghosal investigates cable-driven continuum robots (CCRs) whose cables follow general routings rather than the usual straight or helical paths. The authors compare two modeling strategies: a discrete optimization-based kinematic approach that discretizes the backbone into virtual four-bar linkages and minimizes coupler-angle error, and a static Cosserat-rod approach that treats the backbone as a continuous elastic curve subject to cable forces. They fabricate a 3D-printed prototype from ABS with a 180 mm backbone, 3 mm diameter, ten spacer discs, and fishing-wire cables, and test six routing configurations (I–VI) including straight, helical, and arbitrary paths under a 400 g cable load.

Numerical results were obtained in MATLAB: the optimization solution averaged 2.5 s while the Cosserat shooting-method solution averaged 10.5 s on a 3.1 GHz Intel processor. Superimposing simulated backbone poses on photographed prototypes showed that both models tracked the actual shape closely. The maximum error along the backbone remained below 3.6 mm for every routing, which is less than 2% of the 180 mm total length. The authors also assemble a three-fingered gripper in which each finger is a generally routed CCR with a thin foam pad at the tip, and demonstrate gripping and manipulating small spherical and cubical objects.

## Key Contributions

- Experimental and theoretical deformation analysis for six distinct cable routings (I–VI), including straight, helical, and arbitrary general paths.
- Side-by-side comparison of a discrete optimization-based kinematic model using four-bar linkage discretization and a static Cosserat-rod model solved with a shooting method.
- Experimental validation on a 3D-printed ABS continuum robot prototype showing backbone pose error below 2% of the total robot length for both modeling approaches.
- Design and demonstration of a three-fingered gripper using 3D-printed generally routed continuum fingers, including gripping and manipulation of spherical and cubical objects.

## Relevance to Humanoid Robotics

Compliant, cable-driven continuum fingers provide lightweight, low-cost soft robotic end-effectors that can be integrated into humanoid hands and arms for delicate manipulation. The 3D-printed fabrication route enables rapid prototyping and customization of finger modules, which is valuable for iterating humanoid end-effector designs. The validated kinematic and static modeling methods can inform the design and control of soft manipulators in humanoid robots, especially where safe contact and adaptive grasping are required.
