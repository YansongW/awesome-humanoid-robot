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

