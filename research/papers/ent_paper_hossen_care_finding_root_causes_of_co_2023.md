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
  en: CARE is a causality-based method that learns a causal graphical model from observational
    robot traces to diagnose root causes of functional faults caused by misconfigurations,
    evaluated on Husky, Turtlebot 3, and Gazebo.
  zh: CARE 是一种基于因果推理的方法，从观测机器人轨迹中学习因果图模型，以诊断由错误配置导致的功能故障的根本原因，并在 Husky、Turtlebot 3
    和 Gazebo 上进行了评估。
  ko: CARE는 관찰된 로봇 추적 데이터로부터 인과 그래프 모델을 학습하여 잘못된 구성으로 인한 기능적 결함의 근본 원인을 진단하는 인과 기반
    방법으로, Husky, Turtlebot 3 및 Gazebo에서 평가되었다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: 'CARE: Finding Root Causes of Configuration Issues in Highly-Configurable
    Robots'
  url: https://arxiv.org/abs/2301.07690
  date: '2023'
  accessed_at: '2026-06-27'
  doi: 10.5281/zenodo.7529716
theoretical_depth:
- method
---

## Overview

Robotic systems can expose hundreds or thousands of interacting software and hardware configuration options, and incorrect settings can produce functional faults. Diagnosing such faults is hard because the configuration space grows combinatorially, configuration options interact non-trivially, and confounding variables obscure cause-effect relationships. This paper introduces CARE (CAusal REasoning for configuration issues), a method that frames root-cause diagnosis as a causal inference problem. CARE first learns a causal graphical model from observational robot traces using Fast Causal Inference (FCI) augmented with entropy-based edge resolution. It then extracts causal paths from each configuration option to the affected performance objective and ranks the options by their average causal effect, producing a ranked list of the most likely root-cause configurations. The approach is evaluated on both physical robots (Clearpath Husky UGV and Turtlebot 3) and in the Gazebo simulator.

## Key Contributions

- Propose CARE, a causality-based framework for finding root causes of configuration bugs in robotic systems.
- Learn causal models from observational data and rank configuration options by their average causal effect on performance objectives.
- Evaluate CARE on simulated and physical Husky and Turtlebot 3 robots, achieving 95% accuracy in root-cause diagnosis.
- Show that causal models learned in simulation transfer to different physical robot platforms.

## Relevance to Humanoid Robotics

Mass-produced and deployed humanoid robots are highly configurable systems whose behavior depends on tightly coupled software and hardware parameters, including control gains, gait parameters, sensor calibrations, safety thresholds, and middleware settings. Misconfiguration of any of these can cause field failures, increase debugging time, and require expensive rework during scale-up. CARE's causal root-cause analysis provides a principled way to identify which configuration options are responsible for observed functional faults, which could reduce downtime and accelerate validation pipelines for humanoid platforms. The demonstrated transfer of causal models from simulation to multiple physical platforms is also directly relevant to humanoid development, where physical testing is costly and simulation-based diagnosis is attractive.
