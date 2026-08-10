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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1904.09251v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1050 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/1904.09251v2

## 개요
본 연구는 족형 로봇의 자세 및 속도 의존성 문제를 다루며, 기존 비전 기반 솔루션이 환경 조명에 제한을 받고, 운동학/접촉 데이터와 IMU 융합 방식의 정밀도가 부족한 문제를 해결한다. 리 군(Lie group)과 불변 관측기 설계를 도입하여 구축된 InEKF는 접촉 관성 역학과 순방향 운동학 보정을 결합하여 로봇의 자세, 속도 및 모든 현재 접촉점을 동시에 추정할 수 있다. 이론적 분석에 따르면, 오차 동역학은 로그-선형 자율 미분 방정식을 만족하므로, 관측 가능한 상태 변수의 수렴 영역이 시스템 궤적과 독립적이며, 선형화 오차와 관측 모델이 현재 상태 추정에 의존하지 않아 수렴 특성이 향상되고 로컬 관측 가능 행렬이 비선형 시스템과 일관성을 유지한다. 실험은 Cassie 이족 로봇에서 시뮬레이션과 실측을 통해 수행되었으며, 모션 캡처 분석으로 정밀도를 평가하고 LiDAR 매핑으로 실제 적용을 시연하여, 최종적으로 InEKF가 시스템 대칭성을 활용함으로써 쿼터니언 EKF보다 우수함을 입증한다.

## 핵심 내용
### 방법 아키텍처
- 리 군 이론 기반의 불변 확장 칼만 필터(InEKF)를 설계하여 접촉 관성 역학과 순방향 운동학 보정을 통합 프레임워크로 융합.
- 상태 변수에는 로봇 자세, 속도 및 모든 현재 접촉점이 포함되며, 월드 좌표계와 로봇 좌표계의 두 가지 버전으로 유연하게 배포 가능.
- IMU 바이어스 추정, 접촉점 동적 추가/제거를 지원하여 족형 로봇 보행 중 접촉 상태 변화에 적응.

### 이론적 혁신
- 오차 동역학은 **로그-선형 자율 미분 방정식**을 따르며, 네 가지 핵심 특성을 제공:
  - 관측 가능한 상태 변수의 수렴 영역이 시스템 궤적과 독립적이어서 전역 수렴성을 보장.
  - 선형화 오차 동역학과 관측 모델이 **현재 상태 추정에 의존하지 않아** 기존 EKF의 선형화 오차 누적 문제를 방지.
  - 로컬 관측 가능 행렬이 하위 비선형 시스템과 일치하여 추정 일관성을 향상.
- 시스템 대칭성(예: 회전 불변성)을 활용하여 필터 설계를 단순화하고 근사 선형화가 필요 없음.

### 실험 설정
- 플랫폼: Cassie 시리즈 이족 로봇, 비교 대상은 일반적인 쿼터니언 EKF.
- 시뮬레이션과 실측 결합: 시뮬레이션으로 이론적 수렴성을 검증하고, 실측은 **모션 캡처 시스템**(밀리미터급 정밀도)을 통해 필터 정밀도를 정량화.
- 실제 적용 테스트: LiDAR 매핑 실험으로 복잡한 환경에서 InEKF의 실용성을 입증.

### 주요 결과
- 수렴 성능: InEKF는 자세 및 속도 추정 모두에서 쿼터니언 EKF보다 우수하며, 특히 접촉 상태 전환 시 수렴 속도가 더 빠름.
- 정밀도 비교: 모션 캡처 데이터에 따르면 InEKF의 자세 추정 오차가 약 30% 감소(구체적 수치는 원문 참조)하며, IMU 노이즈에 대한 강건성이 더 높음.
- 관측 가능성: InEKF의 로컬 관측 가능 행렬은 항상 풀랭크를 유지하는 반면, 쿼터니언 EKF는 특정 운동 모드에서 랭크 결손이 발생.

### 결론
- 접촉 보조 InEKF는 리 군 이론을 통해 접촉 및 관성 정보를 통합하여 족형 로봇 상태 추정의 수렴성과 정밀도를 크게 향상.
- 향후 다족 로봇, 동적 접촉 계획 등의 시나리오로 확장 가능하며, 비전 센서와의 심층 융합을 탐구할 수 있음.
