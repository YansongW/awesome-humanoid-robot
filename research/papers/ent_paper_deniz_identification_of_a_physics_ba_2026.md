---
$id: ent_paper_deniz_identification_of_a_physics_ba_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Identification of a Physics-Based Electrical Power Consumption Model for the
    Unitree G1 Humanoid Arm
  zh: Unitree G1人形机器人手臂基于物理的电力消耗模型辨识
  ko: Unitree G1 휴머노이드 팔의 물리 기반 전력 소비 모델 식별
summary:
  en: This paper presents a physics-based, linear-in-parameters electrical power consumption
    model for the seven-degree-of-freedom left arm of the Unitree G1 humanoid robot,
    combining actuator loss terms, a baseline-torque correction, and pairwise joint-speed
    interaction terms, and validates it on 943 physical-robot trajectories.
  zh: 本文提出了一个基于物理的、参数线性的Unitree G1人形机器人七自由度左臂电力消耗模型，结合了执行器损耗项、基线扭矩修正和成对关节速度交互项，并在943条物理机器人轨迹上进行了验证。
  ko: 본 논문은 Unitree G1 휴머노이드 로봇의 7자유도 왼팔 전력 소비를 위한 물리 기반 선형-매개변수 모델을 제시하며, 액추에이터 손실
    항, 기준 토크 보정 및 쌍별 관절 속도 상호작용 항을 포함하여 943개의 실제 로봇 궤적에서 검증합니다.
domains:
- 07_ai_models_algorithms
- 06_design_engineering
- 02_components
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- power_consumption_model
- unitree_g1
- humanoid_arm
- energy_aware_planning
- physics_based_model
- parameter_identification
- battery_management
- thermal_monitoring
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text verification
    needed before final acceptance.; approved by human reviewer.
sources:
- id: src_001
  type: paper
  title: Identification of a Physics-Based Electrical Power Consumption Model for
    the Unitree G1 Humanoid Arm
  url: https://arxiv.org/abs/2606.15915
  date: '2026'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_robot_system_unitree_g1
  relationship: integrates
  description:
    en: The experimental platform and subject of the power consumption model.
    zh: 功耗模型的实验平台和研究对象。
    ko: 전력 소비 모델의 실험 플랫폼 및 연구 대상.
- id: ent_component_bldc_motor
  relationship: integrates
  description:
    en: Actuator technology used in the Unitree G1 arm joints.
    zh: Unitree G1手臂关节中使用的执行器技术。
    ko: Unitree G1 팔 관절에 사용되는 액추에이터 기술.
- id: ent_component_harmonic_drive_reducer
  relationship: integrates
  description:
    en: Transmission component in the arm joints, whose asymmetric acceleration/braking
      behaviour is noted.
    zh: 手臂关节中的传动部件，其加速/制动非对称行为被提及。
    ko: 팔 관절의 변속 부품으로 가속/제동 비대칭 거동이 언급됨.
- id: ent_component_unitree_dex3_1_hand
  relationship: integrates
  description:
    en: End-effector mounted on the left arm during experiments.
    zh: 实验中安装在左臂末端的执行器。
    ko: 실험 중 왼팔에 장착된 엔드 이펙터.
- id: ent_component_battery_management_system
  relationship: integrates
  description:
    en: Onboard system providing electrical power measurements used for model identification.
    zh: 为模型辨识提供电力测量的车载系统。
    ko: 모델 식별에 사용되는 전력 측정을 제공하는 온보드 시스템.
- id: ent_component_main_board_power_sensor
  relationship: integrates
  description:
    en: Sensor used to collect onboard power data for regression.
    zh: 用于采集回归用功率数据的车载传感器。
    ko: 회귀 분석용 전력 데이터 수집에 사용된 센서.
theoretical_depth:
- system
---




# Identification of a Physics-Based Electrical Power Consumption Model for the Unitree G1 Humanoid Arm

## 抽象

> **生活实例**：它就像为汽车建立的油耗模型——不是只看速度，而是综合考虑发动机损耗、路况、上下坡和空调负载，预测不同驾驶方式会消耗多少油。

> **自然语言逻辑**：这篇论文为 Unitree G1 的七自由度左臂建立了一个基于物理的线性参数电力消耗模型，综合了执行器损耗、重力补偿扭矩和成对关节速度交互项；它能在真实机器人轨迹上准确预测功耗，为能量感知运动规划、电池管理和热监控提供可解释的模型基础。

## Overview

This paper addresses the lack of physics-based electrical power consumption models for modern humanoid robot arms. It develops a linear-in-parameters model for the seven-degree-of-freedom left arm of the Unitree G1 humanoid robot. The model integrates actuator loss terms with a baseline-torque correction that captures variations in gravity-compensation load, allowing it to predict negative net power trajectories that occur during deceleration or lowering motions. Pairwise joint-speed interaction terms are added to account for power coupling when multiple joints move simultaneously.

Parameters are identified from experimental data collected on a physical Unitree G1 robot using onboard power measurements as the regression target. The identification dataset comprises 897 trajectories that include single-joint and coordinated multi-joint motions at multiple speed levels. Validation on 46 additional trajectories executed at previously unseen speeds yields an R2 of 0.965, indicating strong generalisation beyond the identification conditions. The trajectory-level aggregation methodology is specifically designed to handle low-rate onboard power sensors.

Analysis of the identified parameters reveals distinct power-consumption characteristics across the arm joints. Viscous friction dominates the shoulder pitch and all three wrist joints, copper losses dominate the shoulder yaw and elbow joints, and the shoulder roll joint is uniquely dominated by Coulomb friction.

## Key Contributions

- Physics-based linear-in-parameters electrical power model for all seven joints of the Unitree G1 left arm.
- Baseline-torque correction that captures gravity-compensation load changes and predicts negative net power trajectories.
- Pairwise joint-speed interaction terms that model power coupling during simultaneous multi-joint motion.
- Trajectory-level aggregation methodology enabling robust parameter identification from low-rate onboard power sensors.
- Experimental validation on 943 physical-robot trajectories with strong generalisation to unseen speeds (R2 = 0.965 on validation set; R2 = 0.933 on identification set with RMSE = 1.07 W).

## Relevance to Humanoid Robotics

Accurate prediction of electrical power consumption is essential for energy-aware motion planning, battery management, and thermal monitoring in battery-powered humanoid robots. By providing an interpretable and efficiently identifiable model for a commercial humanoid arm, this work supports the scalable deployment of humanoid robots in real-world applications where energy efficiency and operational uptime are critical. The methodology is also potentially transferable to other torque-controlled robotic systems beyond the Unitree G1.
