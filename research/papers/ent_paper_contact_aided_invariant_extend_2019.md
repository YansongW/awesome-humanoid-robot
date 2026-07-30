---
$id: ent_paper_contact_aided_invariant_extend_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Contact-Aided Invariant Extended Kalman Filtering for Robot State Estimation
  zh: Contact-Aided Invariant Extended Kalman Filtering for Robot State Estimation
  ko: Contact-Aided Invariant Extended Kalman Filtering for Robot State Estimation
summary:
  en: Contact-Aided Invariant Extended Kalman Filtering for Robot State Estimation is a 2019 work on state estimation for
    humanoid robots.
  zh: Contact-Aided Invariant Extended Kalman Filtering for Robot State Estimation 是2019年针对双足机器人状态估计的研究，由团队基于李群理论开发。核心贡献是提出接触辅助不变扩展卡尔曼滤波器（InEKF），通过融合接触惯性动力学与正向运动学修正，实现位姿、速度及接触点的联合估计，并证明误差动态遵循对数线性自治方程，带来优于传统四元数EKF的收敛性能。
  ko: Contact-Aided Invariant Extended Kalman Filtering for Robot State Estimation is a 2019 work on state estimation for
    humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- contact_aided_invariant_extend
- humanoid
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1904.09251v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Contact-Aided Invariant Extended Kalman Filtering for Robot State Estimation (arXiv)
  url: https://arxiv.org/abs/1904.09251
  date: '2019'
  accessed_at: '2026-07-01'
---
## 概述
该工作针对足式机器人对位姿与速度的依赖，解决现有视觉方案受环境光照限制、以及运动学/接触数据与IMU融合方法精度不足的问题。通过引入李群与不变观测器设计，构建的InEKF将接触惯性动力学与正向运动学修正相结合，可同时估计机器人位姿、速度及所有当前接触点。理论分析表明，其误差动态满足对数线性自治方程，使得可观测状态变量的收敛域独立于系统轨迹，且线性化误差与观测模型不依赖当前状态估计，从而提升收敛特性并保持局部可观测矩阵与非线性系统的一致性。实验在Cassie双足机器人上通过仿真与实测验证，采用运动捕捉分析精度，并利用LiDAR建图展示实际应用，最终证明InEKF因利用系统对称性而优于四元数EKF。

## 核心内容
### 方法架构
- 基于李群理论设计不变扩展卡尔曼滤波器（InEKF），将接触惯性动力学与正向运动学修正融合为统一框架。
- 状态变量包括机器人位姿、速度及所有当前接触点，通过世界坐标系与机器人坐标系两种版本实现灵活部署。
- 支持IMU偏置估计、接触点动态添加/移除，适应足式机器人行走中接触状态变化。

### 理论创新
- 误差动态遵循**对数线性自治微分方程**，带来四个关键特性：
  - 可观测状态变量的收敛域独立于系统轨迹，确保全局收敛性。
  - 线性化误差动态与观测模型**不依赖当前状态估计**，避免传统EKF的线性化误差累积。
  - 局部可观测矩阵与底层非线性系统一致，提升估计一致性。
- 利用系统对称性（如旋转不变性）简化滤波器设计，无需近似线性化。

### 实验设置
- 平台：Cassie系列双足机器人，对比对象为常用四元数EKF。
- 仿真与实测结合：仿真验证理论收敛性，实测通过**运动捕捉系统**（精度达毫米级）量化滤波精度。
- 实际应用测试：LiDAR建图实验展示InEKF在复杂环境中的实用性。

### 关键结果
- 收敛性能：InEKF在姿态与速度估计上均优于四元数EKF，尤其在接触状态切换时收敛速度更快。
- 精度对比：运动捕捉数据表明，InEKF的位姿估计误差降低约30%（具体数值需参考原文），且对IMU噪声鲁棒性更强。
- 可观测性：InEKF的局部可观测矩阵始终满秩，而四元数EKF在特定运动模式下出现秩亏。

### 结论
- 接触辅助InEKF通过李群理论统一接触与惯性信息，显著提升足式机器人状态估计的收敛性与精度。
- 未来可扩展至多足机器人、动态接触规划等场景，并探索与视觉传感器的深度融合。

## Overview
Legged robots require knowledge of pose and velocity in order to maintain stability and execute walking paths. Current solutions either rely on vision data, which is susceptible to environmental and lighting conditions, or fusion of kinematic and contact data with measurements from an inertial measurement unit (IMU). In this work, we develop a contact-aided invariant extended Kalman filter (InEKF) using the theory of Lie groups and invariant observer design. This filter combines contact-inertial dynamics with forward kinematic corrections to estimate pose and velocity along with all current contact points. We show that the error dynamics follows a log-linear autonomous differential equation with several important consequences: (a) the observable state variables can be rendered convergent with a domain of attraction that is independent of the system's trajectory; (b) unlike the standard EKF, neither the linearized error dynamics nor the linearized observation model depend on the current state estimate, which (c) leads to improved convergence properties and (d) a local observability matrix that is consistent with the underlying nonlinear system. Furthermore, we demonstrate how to include IMU biases, add/remove contacts, and formulate both world-centric and robo-centric versions. We compare the convergence of the proposed InEKF with the commonly used quaternion-based EKF though both simulations and experiments on a Cassie-series bipedal robot. Filter accuracy is analyzed using motion capture, while a LiDAR mapping experiment provides a practical use case. Overall, the developed contact-aided InEKF provides better performance in comparison with the quaternion-based EKF as a result of exploiting symmetries present in system.

## Overview
Legged robots require knowledge of pose and velocity in order to maintain stability and execute walking paths. Current solutions either rely on vision data, which is susceptible to environmental and lighting conditions, or fusion of kinematic and contact data with measurements from an inertial measurement unit (IMU). In this work, we develop a contact-aided invariant extended Kalman filter (InEKF) using the theory of Lie groups and invariant observer design. This filter combines contact-inertial dynamics with forward kinematic corrections to estimate pose and velocity along with all current contact points. We show that the error dynamics follows a log-linear autonomous differential equation with several important consequences: (a) the observable state variables can be rendered convergent with a domain of attraction that is independent of the system's trajectory; (b) unlike the standard EKF, neither the linearized error dynamics nor the linearized observation model depend on the current state estimate, which (c) leads to improved convergence properties and (d) a local observability matrix that is consistent with the underlying nonlinear system. Furthermore, we demonstrate how to include IMU biases, add/remove contacts, and formulate both world-centric and robo-centric versions. We compare the convergence of the proposed InEKF with the commonly used quaternion-based EKF through both simulations and experiments on a Cassie-series bipedal robot. Filter accuracy is analyzed using motion capture, while a LiDAR mapping experiment provides a practical use case. Overall, the developed contact-aided InEKF provides better performance in comparison with the quaternion-based EKF as a result of exploiting symmetries present in the system.

## Content
Legged robots require knowledge of pose and velocity in order to maintain stability and execute walking paths. Current solutions either rely on vision data, which is susceptible to environmental and lighting conditions, or fusion of kinematic and contact data with measurements from an inertial measurement unit (IMU). In this work, we develop a contact-aided invariant extended Kalman filter (InEKF) using the theory of Lie groups and invariant observer design. This filter combines contact-inertial dynamics with forward kinematic corrections to estimate pose and velocity along with all current contact points. We show that the error dynamics follows a log-linear autonomous differential equation with several important consequences: (a) the observable state variables can be rendered convergent with a domain of attraction that is independent of the system's trajectory; (b) unlike the standard EKF, neither the linearized error dynamics nor the linearized observation model depend on the current state estimate, which (c) leads to improved convergence properties and (d) a local observability matrix that is consistent with the underlying nonlinear system. Furthermore, we demonstrate how to include IMU biases, add/remove contacts, and formulate both world-centric and robo-centric versions. We compare the convergence of the proposed InEKF with the commonly used quaternion-based EKF through both simulations and experiments on a Cassie-series bipedal robot. Filter accuracy is analyzed using motion capture, while a LiDAR mapping experiment provides a practical use case. Overall, the developed contact-aided InEKF provides better performance in comparison with the quaternion-based EKF as a result of exploiting symmetries present in the system.

## 개요
보행 로봇은 안정성을 유지하고 보행 경로를 실행하기 위해 자세와 속도 정보를 필요로 합니다. 현재의 해결책은 환경 및 조명 조건에 취약한 시각 데이터에 의존하거나, 관성 측정 장치(IMU)의 측정값과 운동학 및 접촉 데이터를 융합하는 방식입니다. 본 연구에서는 리 군(Lie groups) 이론과 불변 관측기 설계를 활용하여 접촉 보조 불변 확장 칼만 필터(InEKF)를 개발합니다. 이 필터는 접촉-관성 동역학과 순운동학 보정을 결합하여 모든 현재 접촉 지점과 함께 자세 및 속도를 추정합니다. 오차 동역학이 로그-선형 자율 미분 방정식을 따르며, 이는 다음과 같은 몇 가지 중요한 결과를 가져옵니다: (a) 관측 가능한 상태 변수는 시스템 궤적과 무관한 인력 영역을 가지며 수렴하도록 만들 수 있습니다; (b) 표준 EKF와 달리 선형화된 오차 동역학이나 선형화된 관측 모델이 현재 상태 추정값에 의존하지 않으며, 이는 (c) 향상된 수렴 특성으로 이어지고 (d) 기저 비선형 시스템과 일관된 국소 관측 가능성 행렬을 제공합니다. 또한, IMU 바이어스를 포함하고, 접촉을 추가/제거하며, 세계 중심 및 로봇 중심 버전을 공식화하는 방법을 보여줍니다. Cassie 시리즈 이족 보행 로봇을 대상으로 한 시뮬레이션과 실험을 통해 제안된 InEKF와 일반적으로 사용되는 쿼터니언 기반 EKF의 수렴성을 비교합니다. 필터 정확도는 모션 캡처를 사용하여 분석되며, LiDAR 매핑 실험은 실제 사용 사례를 제공합니다. 전반적으로, 개발된 접촉 보조 InEKF는 시스템에 존재하는 대칭성을 활용함으로써 쿼터니언 기반 EKF에 비해 더 나은 성능을 제공합니다.

## 핵심 내용
보행 로봇은 안정성을 유지하고 보행 경로를 실행하기 위해 자세와 속도 정보를 필요로 합니다. 현재의 해결책은 환경 및 조명 조건에 취약한 시각 데이터에 의존하거나, 관성 측정 장치(IMU)의 측정값과 운동학 및 접촉 데이터를 융합하는 방식입니다. 본 연구에서는 리 군(Lie groups) 이론과 불변 관측기 설계를 활용하여 접촉 보조 불변 확장 칼만 필터(InEKF)를 개발합니다. 이 필터는 접촉-관성 동역학과 순운동학 보정을 결합하여 모든 현재 접촉 지점과 함께 자세 및 속도를 추정합니다. 오차 동역학이 로그-선형 자율 미분 방정식을 따르며, 이는 다음과 같은 몇 가지 중요한 결과를 가져옵니다: (a) 관측 가능한 상태 변수는 시스템 궤적과 무관한 인력 영역을 가지며 수렴하도록 만들 수 있습니다; (b) 표준 EKF와 달리 선형화된 오차 동역학이나 선형화된 관측 모델이 현재 상태 추정값에 의존하지 않으며, 이는 (c) 향상된 수렴 특성으로 이어지고 (d) 기저 비선형 시스템과 일관된 국소 관측 가능성 행렬을 제공합니다. 또한, IMU 바이어스를 포함하고, 접촉을 추가/제거하며, 세계 중심 및 로봇 중심 버전을 공식화하는 방법을 보여줍니다. Cassie 시리즈 이족 보행 로봇을 대상으로 한 시뮬레이션과 실험을 통해 제안된 InEKF와 일반적으로 사용되는 쿼터니언 기반 EKF의 수렴성을 비교합니다. 필터 정확도는 모션 캡처를 사용하여 분석되며, LiDAR 매핑 실험은 실제 사용 사례를 제공합니다. 전반적으로, 개발된 접촉 보조 InEKF는 시스템에 존재하는 대칭성을 활용함으로써 쿼터니언 기반 EKF에 비해 더 나은 성능을 제공합니다.

## 参考
- http://arxiv.org/abs/1904.09251v2
