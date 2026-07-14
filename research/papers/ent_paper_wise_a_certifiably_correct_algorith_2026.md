---
$id: ent_paper_wise_a_certifiably_correct_algorith_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Certifiably Correct Algorithm for Generalized Robot-World and Hand-Eye Calibration
  zh: 广义机器人-世界与手眼校准的可认证正确算法
  ko: 일반화된 로봇-월드 및 핸드-아이 보정을 위한 인증 가능한 정확한 알고리즘
summary:
  en: Presents a fast, certifiably globally optimal algorithm for generalized robot-world and hand-eye calibration that jointly
    estimates multiple sensor and target poses, including scale-free monocular cameras, via a tight semidefinite programming
    relaxation of a maximum-likelihood QCQP over SE(3).
  zh: 提出一种快速且可证明全局最优的广义机器人-世界与手眼校准算法，通过对 SE(3) 上最大似然 QCQP 的紧半定规划松弛，联合估计多个传感器与目标位姿，包括无尺度单目相机。
  ko: SE(3) 상 최대우도 QCQP에 대한 긴밀한 SDP 완화를 통해 여러 센서와 대상 자세를 공동으로 추정하고 스케일-프리 단안 카메라를 포함하는 일반화된 로봇-월드 및 핸드-아이 보정을 위한 빠르고 인증 가능한
    전역 최적 알고리즘을 제시한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 04_assembly_integration_testing
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- extrinsic_calibration
- hand_eye_calibration
- robot_world_calibration
- semidefinite_programming
- qcqp
- global_optimality
- certifiable_perception
- monocular_camera
- multi_sensor_fusion
- se3_estimation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.23045v2.
sources:
- id: src_001
  type: paper
  title: A Certifiably Correct Algorithm for Generalized Robot-World and Hand-Eye Calibration
  url: https://arxiv.org/abs/2507.23045
  date: '2026'
  accessed_at: '2026-06-28'
  doi: 10.1177/ToBeAssigned
theoretical_depth:
- method
---
## 概述
Automatic extrinsic sensor calibration is a fundamental problem for multi-sensor platforms. Reliable and general-purpose solutions should be computationally efficient, require few assumptions about the structure of the sensing environment, and demand little effort from human operators. In this work, we introduce a fast and certifiably globally optimal algorithm for solving a generalized formulation of the robot-world and hand-eye calibration (RWHEC) problem. The formulation of RWHEC presented is "generalized" in that it supports the simultaneous estimation of multiple sensor and target poses, and permits the use of monocular cameras that, alone, are unable to measure the scale of their environments. In addition to demonstrating our method's superior performance over existing solutions through extensive simulated and real experiments, we derive novel identifiability criteria and establish a priori guarantees of global optimality for problem instances with bounded measurement errors. As part of our analysis, we propose a new constraint qualification for nonlinear programs with redundant constraints; this constraint qualification is of independent interest for establishing the exactness of SDP relaxations of QCQPs that have been tightened through the addition of redundant constraints. Finally, we provide a free and open-source implementation of our algorithms and experiments.

## 核心内容
Automatic extrinsic sensor calibration is a fundamental problem for multi-sensor platforms. Reliable and general-purpose solutions should be computationally efficient, require few assumptions about the structure of the sensing environment, and demand little effort from human operators. In this work, we introduce a fast and certifiably globally optimal algorithm for solving a generalized formulation of the robot-world and hand-eye calibration (RWHEC) problem. The formulation of RWHEC presented is "generalized" in that it supports the simultaneous estimation of multiple sensor and target poses, and permits the use of monocular cameras that, alone, are unable to measure the scale of their environments. In addition to demonstrating our method's superior performance over existing solutions through extensive simulated and real experiments, we derive novel identifiability criteria and establish a priori guarantees of global optimality for problem instances with bounded measurement errors. As part of our analysis, we propose a new constraint qualification for nonlinear programs with redundant constraints; this constraint qualification is of independent interest for establishing the exactness of SDP relaxations of QCQPs that have been tightened through the addition of redundant constraints. Finally, we provide a free and open-source implementation of our algorithms and experiments.

## 参考
- http://arxiv.org/abs/2507.23045v2

