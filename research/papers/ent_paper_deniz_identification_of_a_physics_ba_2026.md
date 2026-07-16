---
$id: ent_paper_deniz_identification_of_a_physics_ba_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Identification of a Physics-Based Electrical Power Consumption Model for the Unitree G1 Humanoid Arm
  zh: Unitree G1人形机器人手臂基于物理的电力消耗模型辨识
  ko: Unitree G1 휴머노이드 팔의 물리 기반 전력 소비 모델 식별
summary:
  en: This paper presents a physics-based, linear-in-parameters electrical power consumption model for the seven-degree-of-freedom
    left arm of the Unitree G1 humanoid robot, combining actuator loss terms, a baseline-torque correction, and pairwise joint-speed
    interaction terms, and validates it on 943 physical-robot trajectories.
  zh: 本文提出了一个基于物理的、参数线性的Unitree G1人形机器人七自由度左臂电力消耗模型，结合了执行器损耗项、基线扭矩修正和成对关节速度交互项，并在943条物理机器人轨迹上进行了验证。
  ko: 본 논문은 Unitree G1 휴머노이드 로봇의 7자유도 왼팔 전력 소비를 위한 물리 기반 선형-매개변수 모델을 제시하며, 액추에이터 손실 항, 기준 토크 보정 및 쌍별 관절 속도 상호작용 항을 포함하여 943개의
    실제 로봇 궤적에서 검증합니다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.15915v1.
sources:
- id: src_001
  type: paper
  title: Identification of a Physics-Based Electrical Power Consumption Model for the Unitree G1 Humanoid Arm
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
    en: Transmission component in the arm joints, whose asymmetric acceleration/braking behaviour is noted.
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
## 概述
Accurate prediction of electrical power consumption is essential for energy-aware motion planning, battery management, and thermal monitoring in battery-powered humanoid robots. This letter presents a physics-based, linear-in-parameters model for the electrical power consumption of the seven-degree-of-freedom left arm of the Unitree~G1 humanoid robot. The proposed formulation combines actuator loss terms with a baseline-torque correction that captures changes in gravity-compensation load and enables accurate prediction of negative net power trajectories. Pairwise interaction terms are introduced to model power coupling during simultaneous multi-joint motion. Model parameters are identified from experimental data collected on a physical Unitree~G1 using onboard power measurements as the regression target. Across 897 trajectories covering single-joint and coordinated arm motions at multiple speed levels, the identified model achieves $R^2 = 0.933$ with an RMSE of 1.07 (W). Validation on 46 trajectories executed at previously unseen speeds yields $R^2 = 0.965$, demonstrating strong generalisation beyond the identification dataset. Analysis of the identified parameters reveals distinct power-consumption characteristics across the arm, with viscous friction dominating most joints (shoulder pitch and all three wrist joints), copper losses dominating shoulder yaw and the elbow, and shoulder roll uniquely dominated by Coulomb friction.

## 核心内容
Accurate prediction of electrical power consumption is essential for energy-aware motion planning, battery management, and thermal monitoring in battery-powered humanoid robots. This letter presents a physics-based, linear-in-parameters model for the electrical power consumption of the seven-degree-of-freedom left arm of the Unitree~G1 humanoid robot. The proposed formulation combines actuator loss terms with a baseline-torque correction that captures changes in gravity-compensation load and enables accurate prediction of negative net power trajectories. Pairwise interaction terms are introduced to model power coupling during simultaneous multi-joint motion. Model parameters are identified from experimental data collected on a physical Unitree~G1 using onboard power measurements as the regression target. Across 897 trajectories covering single-joint and coordinated arm motions at multiple speed levels, the identified model achieves $R^2 = 0.933$ with an RMSE of 1.07 (W). Validation on 46 trajectories executed at previously unseen speeds yields $R^2 = 0.965$, demonstrating strong generalisation beyond the identification dataset. Analysis of the identified parameters reveals distinct power-consumption characteristics across the arm, with viscous friction dominating most joints (shoulder pitch and all three wrist joints), copper losses dominating shoulder yaw and the elbow, and shoulder roll uniquely dominated by Coulomb friction.

## 参考
- http://arxiv.org/abs/2606.15915v1

## Overview
Accurate prediction of electrical power consumption is essential for energy-aware motion planning, battery management, and thermal monitoring in battery-powered humanoid robots. This letter presents a physics-based, linear-in-parameters model for the electrical power consumption of the seven-degree-of-freedom left arm of the Unitree~G1 humanoid robot. The proposed formulation combines actuator loss terms with a baseline-torque correction that captures changes in gravity-compensation load and enables accurate prediction of negative net power trajectories. Pairwise interaction terms are introduced to model power coupling during simultaneous multi-joint motion. Model parameters are identified from experimental data collected on a physical Unitree~G1 using onboard power measurements as the regression target. Across 897 trajectories covering single-joint and coordinated arm motions at multiple speed levels, the identified model achieves $R^2 = 0.933$ with an RMSE of 1.07 (W). Validation on 46 trajectories executed at previously unseen speeds yields $R^2 = 0.965$, demonstrating strong generalisation beyond the identification dataset. Analysis of the identified parameters reveals distinct power-consumption characteristics across the arm, with viscous friction dominating most joints (shoulder pitch and all three wrist joints), copper losses dominating shoulder yaw and the elbow, and shoulder roll uniquely dominated by Coulomb friction.

## Content
Accurate prediction of electrical power consumption is essential for energy-aware motion planning, battery management, and thermal monitoring in battery-powered humanoid robots. This letter presents a physics-based, linear-in-parameters model for the electrical power consumption of the seven-degree-of-freedom left arm of the Unitree~G1 humanoid robot. The proposed formulation combines actuator loss terms with a baseline-torque correction that captures changes in gravity-compensation load and enables accurate prediction of negative net power trajectories. Pairwise interaction terms are introduced to model power coupling during simultaneous multi-joint motion. Model parameters are identified from experimental data collected on a physical Unitree~G1 using onboard power measurements as the regression target. Across 897 trajectories covering single-joint and coordinated arm motions at multiple speed levels, the identified model achieves $R^2 = 0.933$ with an RMSE of 1.07 (W). Validation on 46 trajectories executed at previously unseen speeds yields $R^2 = 0.965$, demonstrating strong generalisation beyond the identification dataset. Analysis of the identified parameters reveals distinct power-consumption characteristics across the arm, with viscous friction dominating most joints (shoulder pitch and all three wrist joints), copper losses dominating shoulder yaw and the elbow, and shoulder roll uniquely dominated by Coulomb friction.

## 개요
배터리로 구동되는 휴머노이드 로봇의 에너지 인식 모션 계획, 배터리 관리 및 열 모니터링을 위해서는 전력 소비량의 정확한 예측이 필수적입니다. 본 논문에서는 Unitree~G1 휴머노이드 로봇의 7자유도 왼팔에 대한 물리 기반 선형 파라미터 모델을 제시합니다. 제안된 공식은 액추에이터 손실 항과 중력 보상 부하 변화를 포착하는 기준 토크 보정을 결합하여 음의 순 전력 궤적을 정확히 예측할 수 있게 합니다. 또한, 다중 관절 동시 움직임 시 전력 결합을 모델링하기 위해 쌍별 상호작용 항을 도입했습니다. 모델 파라미터는 실제 Unitree~G1에서 수집된 실험 데이터를 기반으로 식별되었으며, 온보드 전력 측정값을 회귀 목표로 사용했습니다. 단일 관절 및 여러 속도 수준에서의 조정된 팔 움직임을 포함하는 897개 궤적에 대해 식별된 모델은 RMSE 1.07(W)에서 $R^2 = 0.933$을 달성했습니다. 이전에 보지 못한 속도로 실행된 46개 궤적에 대한 검증에서는 $R^2 = 0.965$를 보여, 식별 데이터셋을 넘어선 강력한 일반화 능력을 입증했습니다. 식별된 파라미터 분석 결과, 팔 전체에 걸쳐 뚜렷한 전력 소비 특성이 나타났으며, 점성 마찰이 대부분의 관절(어깨 피치 및 세 손목 관절)을 지배하고, 구리 손실이 어깨 요와 팔꿈치를 지배하며, 어깨 롤은 쿨롱 마찰이 유일하게 지배하는 것으로 나타났습니다.

## 핵심 내용
배터리로 구동되는 휴머노이드 로봇의 에너지 인식 모션 계획, 배터리 관리 및 열 모니터링을 위해서는 전력 소비량의 정확한 예측이 필수적입니다. 본 논문에서는 Unitree~G1 휴머노이드 로봇의 7자유도 왼팔에 대한 물리 기반 선형 파라미터 모델을 제시합니다. 제안된 공식은 액추에이터 손실 항과 중력 보상 부하 변화를 포착하는 기준 토크 보정을 결합하여 음의 순 전력 궤적을 정확히 예측할 수 있게 합니다. 또한, 다중 관절 동시 움직임 시 전력 결합을 모델링하기 위해 쌍별 상호작용 항을 도입했습니다. 모델 파라미터는 실제 Unitree~G1에서 수집된 실험 데이터를 기반으로 식별되었으며, 온보드 전력 측정값을 회귀 목표로 사용했습니다. 단일 관절 및 여러 속도 수준에서의 조정된 팔 움직임을 포함하는 897개 궤적에 대해 식별된 모델은 RMSE 1.07(W)에서 $R^2 = 0.933$을 달성했습니다. 이전에 보지 못한 속도로 실행된 46개 궤적에 대한 검증에서는 $R^2 = 0.965$를 보여, 식별 데이터셋을 넘어선 강력한 일반화 능력을 입증했습니다. 식별된 파라미터 분석 결과, 팔 전체에 걸쳐 뚜렷한 전력 소비 특성이 나타났으며, 점성 마찰이 대부분의 관절(어깨 피치 및 세 손목 관절)을 지배하고, 구리 손실이 어깨 요와 팔꿈치를 지배하며, 어깨 롤은 쿨롱 마찰이 유일하게 지배하는 것으로 나타났습니다.
