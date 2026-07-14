---
$id: ent_paper_hossen_care_finding_root_causes_of_co_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CARE: Finding Root Causes of Configuration Issues in Highly-Configurable Robots'
  zh: CARE：在高度可配置机器人中查找配置问题的根本原因
  ko: 'CARE: 고도로 구성 가능한 로봇의 구성 문제 근본 원인 탐지'
summary:
  en: CARE is a causality-based method that learns a causal graphical model from observational robot traces to diagnose root
    causes of functional faults caused by misconfigurations, evaluated on Husky, Turtlebot 3, and Gazebo.
  zh: CARE 是一种基于因果推理的方法，从观测机器人轨迹中学习因果图模型，以诊断由错误配置导致的功能故障的根本原因，并在 Husky、Turtlebot 3 和 Gazebo 上进行了评估。
  ko: CARE는 관찰된 로봇 추적 데이터로부터 인과 그래프 모델을 학습하여 잘못된 구성으로 인한 기능적 결함의 근본 원인을 진단하는 인과 기반 방법으로, Husky, Turtlebot 3 및 Gazebo에서 평가되었다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 04_assembly_integration_testing
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- causal_inference
- root_cause_analysis
- configuration_diagnosis
- robot_configuration
- sim_to_real_transfer
- ros
- fast_causal_inference
- functional_fault_diagnosis
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2301.07690v2.
sources:
- id: src_001
  type: paper
  title: 'CARE: Finding Root Causes of Configuration Issues in Highly-Configurable Robots'
  url: https://arxiv.org/abs/2301.07690
  date: '2023'
  accessed_at: '2026-06-27'
  doi: 10.5281/zenodo.7529716
theoretical_depth:
- method
---
## 概述
Robotic systems have subsystems with a combinatorially large configuration space and hundreds or thousands of possible software and hardware configuration options interacting non-trivially. The configurable parameters are set to target specific objectives, but they can cause functional faults when incorrectly configured. Finding the root cause of such faults is challenging due to the exponentially large configuration space and the dependencies between the robot's configuration settings and performance. This paper proposes CaRE -- a method for diagnosing the root cause of functional faults through the lens of causality. CaRE abstracts the causal relationships between various configuration options and the robot's performance objectives by learning a causal structure and estimating the causal effects of options on robot performance indicators. We demonstrate CaRE's efficacy by finding the root cause of the observed functional faults and validating the diagnosed root cause by conducting experiments in both physical robots (Husky and Turtlebot 3) and in simulation (Gazebo). Furthermore, we demonstrate that the causal models learned from robots in simulation (e.g., Husky in Gazebo) are transferable to physical robots across different platforms (e.g., Husky and Turtlebot 3).

## 核心内容
Robotic systems have subsystems with a combinatorially large configuration space and hundreds or thousands of possible software and hardware configuration options interacting non-trivially. The configurable parameters are set to target specific objectives, but they can cause functional faults when incorrectly configured. Finding the root cause of such faults is challenging due to the exponentially large configuration space and the dependencies between the robot's configuration settings and performance. This paper proposes CaRE -- a method for diagnosing the root cause of functional faults through the lens of causality. CaRE abstracts the causal relationships between various configuration options and the robot's performance objectives by learning a causal structure and estimating the causal effects of options on robot performance indicators. We demonstrate CaRE's efficacy by finding the root cause of the observed functional faults and validating the diagnosed root cause by conducting experiments in both physical robots (Husky and Turtlebot 3) and in simulation (Gazebo). Furthermore, we demonstrate that the causal models learned from robots in simulation (e.g., Husky in Gazebo) are transferable to physical robots across different platforms (e.g., Husky and Turtlebot 3).

## 参考
- http://arxiv.org/abs/2301.07690v2

