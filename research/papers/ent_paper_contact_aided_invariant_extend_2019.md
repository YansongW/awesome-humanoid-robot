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
  zh: Contact-Aided Invariant Extended Kalman Filtering for Robot State Estimation is a 2019 work on state estimation for
    humanoid robots.
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1904.09251v2.
sources:
- id: src_001
  type: paper
  title: Contact-Aided Invariant Extended Kalman Filtering for Robot State Estimation (arXiv)
  url: https://arxiv.org/abs/1904.09251
  date: '2019'
  accessed_at: '2026-07-01'
---
## 概述
Legged robots require knowledge of pose and velocity in order to maintain stability and execute walking paths. Current solutions either rely on vision data, which is susceptible to environmental and lighting conditions, or fusion of kinematic and contact data with measurements from an inertial measurement unit (IMU). In this work, we develop a contact-aided invariant extended Kalman filter (InEKF) using the theory of Lie groups and invariant observer design. This filter combines contact-inertial dynamics with forward kinematic corrections to estimate pose and velocity along with all current contact points. We show that the error dynamics follows a log-linear autonomous differential equation with several important consequences: (a) the observable state variables can be rendered convergent with a domain of attraction that is independent of the system's trajectory; (b) unlike the standard EKF, neither the linearized error dynamics nor the linearized observation model depend on the current state estimate, which (c) leads to improved convergence properties and (d) a local observability matrix that is consistent with the underlying nonlinear system. Furthermore, we demonstrate how to include IMU biases, add/remove contacts, and formulate both world-centric and robo-centric versions. We compare the convergence of the proposed InEKF with the commonly used quaternion-based EKF though both simulations and experiments on a Cassie-series bipedal robot. Filter accuracy is analyzed using motion capture, while a LiDAR mapping experiment provides a practical use case. Overall, the developed contact-aided InEKF provides better performance in comparison with the quaternion-based EKF as a result of exploiting symmetries present in system.

## 核心内容
Legged robots require knowledge of pose and velocity in order to maintain stability and execute walking paths. Current solutions either rely on vision data, which is susceptible to environmental and lighting conditions, or fusion of kinematic and contact data with measurements from an inertial measurement unit (IMU). In this work, we develop a contact-aided invariant extended Kalman filter (InEKF) using the theory of Lie groups and invariant observer design. This filter combines contact-inertial dynamics with forward kinematic corrections to estimate pose and velocity along with all current contact points. We show that the error dynamics follows a log-linear autonomous differential equation with several important consequences: (a) the observable state variables can be rendered convergent with a domain of attraction that is independent of the system's trajectory; (b) unlike the standard EKF, neither the linearized error dynamics nor the linearized observation model depend on the current state estimate, which (c) leads to improved convergence properties and (d) a local observability matrix that is consistent with the underlying nonlinear system. Furthermore, we demonstrate how to include IMU biases, add/remove contacts, and formulate both world-centric and robo-centric versions. We compare the convergence of the proposed InEKF with the commonly used quaternion-based EKF though both simulations and experiments on a Cassie-series bipedal robot. Filter accuracy is analyzed using motion capture, while a LiDAR mapping experiment provides a practical use case. Overall, the developed contact-aided InEKF provides better performance in comparison with the quaternion-based EKF as a result of exploiting symmetries present in system.

## 参考
- http://arxiv.org/abs/1904.09251v2

## Overview
Legged robots require knowledge of pose and velocity in order to maintain stability and execute walking paths. Current solutions either rely on vision data, which is susceptible to environmental and lighting conditions, or fusion of kinematic and contact data with measurements from an inertial measurement unit (IMU). In this work, we develop a contact-aided invariant extended Kalman filter (InEKF) using the theory of Lie groups and invariant observer design. This filter combines contact-inertial dynamics with forward kinematic corrections to estimate pose and velocity along with all current contact points. We show that the error dynamics follows a log-linear autonomous differential equation with several important consequences: (a) the observable state variables can be rendered convergent with a domain of attraction that is independent of the system's trajectory; (b) unlike the standard EKF, neither the linearized error dynamics nor the linearized observation model depend on the current state estimate, which (c) leads to improved convergence properties and (d) a local observability matrix that is consistent with the underlying nonlinear system. Furthermore, we demonstrate how to include IMU biases, add/remove contacts, and formulate both world-centric and robo-centric versions. We compare the convergence of the proposed InEKF with the commonly used quaternion-based EKF through both simulations and experiments on a Cassie-series bipedal robot. Filter accuracy is analyzed using motion capture, while a LiDAR mapping experiment provides a practical use case. Overall, the developed contact-aided InEKF provides better performance in comparison with the quaternion-based EKF as a result of exploiting symmetries present in the system.

## Content
Legged robots require knowledge of pose and velocity in order to maintain stability and execute walking paths. Current solutions either rely on vision data, which is susceptible to environmental and lighting conditions, or fusion of kinematic and contact data with measurements from an inertial measurement unit (IMU). In this work, we develop a contact-aided invariant extended Kalman filter (InEKF) using the theory of Lie groups and invariant observer design. This filter combines contact-inertial dynamics with forward kinematic corrections to estimate pose and velocity along with all current contact points. We show that the error dynamics follows a log-linear autonomous differential equation with several important consequences: (a) the observable state variables can be rendered convergent with a domain of attraction that is independent of the system's trajectory; (b) unlike the standard EKF, neither the linearized error dynamics nor the linearized observation model depend on the current state estimate, which (c) leads to improved convergence properties and (d) a local observability matrix that is consistent with the underlying nonlinear system. Furthermore, we demonstrate how to include IMU biases, add/remove contacts, and formulate both world-centric and robo-centric versions. We compare the convergence of the proposed InEKF with the commonly used quaternion-based EKF through both simulations and experiments on a Cassie-series bipedal robot. Filter accuracy is analyzed using motion capture, while a LiDAR mapping experiment provides a practical use case. Overall, the developed contact-aided InEKF provides better performance in comparison with the quaternion-based EKF as a result of exploiting symmetries present in the system.

## 개요
보행 로봇은 안정성을 유지하고 보행 경로를 실행하기 위해 자세와 속도 정보를 필요로 합니다. 현재의 해결책은 환경 및 조명 조건에 취약한 시각 데이터에 의존하거나, 관성 측정 장치(IMU)의 측정값과 운동학 및 접촉 데이터를 융합하는 방식입니다. 본 연구에서는 리 군(Lie groups) 이론과 불변 관측기 설계를 활용하여 접촉 보조 불변 확장 칼만 필터(InEKF)를 개발합니다. 이 필터는 접촉-관성 동역학과 순운동학 보정을 결합하여 모든 현재 접촉 지점과 함께 자세 및 속도를 추정합니다. 오차 동역학이 로그-선형 자율 미분 방정식을 따르며, 이는 다음과 같은 몇 가지 중요한 결과를 가져옵니다: (a) 관측 가능한 상태 변수는 시스템 궤적과 무관한 인력 영역을 가지며 수렴하도록 만들 수 있습니다; (b) 표준 EKF와 달리 선형화된 오차 동역학이나 선형화된 관측 모델이 현재 상태 추정값에 의존하지 않으며, 이는 (c) 향상된 수렴 특성으로 이어지고 (d) 기저 비선형 시스템과 일관된 국소 관측 가능성 행렬을 제공합니다. 또한, IMU 바이어스를 포함하고, 접촉을 추가/제거하며, 세계 중심 및 로봇 중심 버전을 공식화하는 방법을 보여줍니다. Cassie 시리즈 이족 보행 로봇을 대상으로 한 시뮬레이션과 실험을 통해 제안된 InEKF와 일반적으로 사용되는 쿼터니언 기반 EKF의 수렴성을 비교합니다. 필터 정확도는 모션 캡처를 사용하여 분석되며, LiDAR 매핑 실험은 실제 사용 사례를 제공합니다. 전반적으로, 개발된 접촉 보조 InEKF는 시스템에 존재하는 대칭성을 활용함으로써 쿼터니언 기반 EKF에 비해 더 나은 성능을 제공합니다.

## 핵심 내용
보행 로봇은 안정성을 유지하고 보행 경로를 실행하기 위해 자세와 속도 정보를 필요로 합니다. 현재의 해결책은 환경 및 조명 조건에 취약한 시각 데이터에 의존하거나, 관성 측정 장치(IMU)의 측정값과 운동학 및 접촉 데이터를 융합하는 방식입니다. 본 연구에서는 리 군(Lie groups) 이론과 불변 관측기 설계를 활용하여 접촉 보조 불변 확장 칼만 필터(InEKF)를 개발합니다. 이 필터는 접촉-관성 동역학과 순운동학 보정을 결합하여 모든 현재 접촉 지점과 함께 자세 및 속도를 추정합니다. 오차 동역학이 로그-선형 자율 미분 방정식을 따르며, 이는 다음과 같은 몇 가지 중요한 결과를 가져옵니다: (a) 관측 가능한 상태 변수는 시스템 궤적과 무관한 인력 영역을 가지며 수렴하도록 만들 수 있습니다; (b) 표준 EKF와 달리 선형화된 오차 동역학이나 선형화된 관측 모델이 현재 상태 추정값에 의존하지 않으며, 이는 (c) 향상된 수렴 특성으로 이어지고 (d) 기저 비선형 시스템과 일관된 국소 관측 가능성 행렬을 제공합니다. 또한, IMU 바이어스를 포함하고, 접촉을 추가/제거하며, 세계 중심 및 로봇 중심 버전을 공식화하는 방법을 보여줍니다. Cassie 시리즈 이족 보행 로봇을 대상으로 한 시뮬레이션과 실험을 통해 제안된 InEKF와 일반적으로 사용되는 쿼터니언 기반 EKF의 수렴성을 비교합니다. 필터 정확도는 모션 캡처를 사용하여 분석되며, LiDAR 매핑 실험은 실제 사용 사례를 제공합니다. 전반적으로, 개발된 접촉 보조 InEKF는 시스템에 존재하는 대칭성을 활용함으로써 쿼터니언 기반 EKF에 비해 더 나은 성능을 제공합니다.
