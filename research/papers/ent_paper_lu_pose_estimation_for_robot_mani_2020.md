---
$id: ent_paper_lu_pose_estimation_for_robot_mani_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Pose Estimation for Robot Manipulators via Keypoint Optimization and Sim-to-Real Transfer
  zh: 基于关键点优化与仿真到现实迁移的机器人操纵臂姿态估计
  ko: 키포인트 최적화 및 시뮬레이션-실제 전이를 통한 로봇 매니퓰레이터 자세 추정
summary:
  en: This paper proposes an iterative keypoint optimization algorithm that selects 3D keypoints on robotic manipulators to
    maximize 2D detection and 3D localization accuracy, trains a DeepLabCut-based detector on synthetic CoppeliaSim data,
    and transfers it to real images via domain randomization for camera-to-robot calibration and tool tracking.
  zh: 本文提出了一种迭代式关键点优化算法，用于在机器人操作臂上选择能最大化二维检测和三维定位精度的三维关键点；该算法在 CoppeliaSim 合成数据上训练基于 DeepLabCut 的检测器，并通过域随机化将其迁移到真实图像，实现相机到机器人标定与工具跟踪。
  ko: 본 논문은 로봇 매니퓰레이터 상에서 2D 검출 및 3D 위치 추정 정확도를 극대화하는 3D 키포인트를 선택하는 반복적 키포인트 최적화 알고리즘을 제안한다. CoppeliaSim 합성 데이터로 DeepLabCut
    기반 검출기를 학습하고 도메인 랜덤화를 통해 실제 이미지로 전이하여 카메라-로봇 캘리브레이션과 도구 추적을 수행한다.
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
- keypoint_optimization
- sim_to_real_transfer
- domain_randomization
- pose_estimation
- robot_calibration
- surgical_tool_tracking
- deeplabcut
- coppeliasim
- visual_perception
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2010.08054v3.
sources:
- id: src_001
  type: paper
  title: Pose Estimation for Robot Manipulators via Keypoint Optimization and Sim-to-Real Transfer
  url: https://arxiv.org/abs/2010.08054
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Keypoint detection is an essential building block for many robotic applications like motion capture and pose estimation. Historically, keypoints are detected using uniquely engineered markers such as checkerboards or fiducials. More recently, deep learning methods have been explored as they have the ability to detect user-defined keypoints in a marker-less manner. However, different manually selected keypoints can have uneven performance when it comes to detection and localization. An example of this can be found on symmetric robotic tools where DNN detectors cannot solve the correspondence problem correctly. In this work, we propose a new and autonomous way to define the keypoint locations that overcomes these challenges. The approach involves finding the optimal set of keypoints on robotic manipulators for robust visual detection and localization. Using a robotic simulator as a medium, our algorithm utilizes synthetic data for DNN training, and the proposed algorithm is used to optimize the selection of keypoints through an iterative approach. The results show that when using the optimized keypoints, the detection performance of the DNNs improved significantly. We further use the optimized keypoints for real robotic applications by using domain randomization to bridge the reality gap between the simulator and the physical world. The physical world experiments show how the proposed method can be applied to the wide-breadth of robotic applications that require visual feedback, such as camera-to-robot calibration, robotic tool tracking, and end-effector pose estimation.

## 核心内容
Keypoint detection is an essential building block for many robotic applications like motion capture and pose estimation. Historically, keypoints are detected using uniquely engineered markers such as checkerboards or fiducials. More recently, deep learning methods have been explored as they have the ability to detect user-defined keypoints in a marker-less manner. However, different manually selected keypoints can have uneven performance when it comes to detection and localization. An example of this can be found on symmetric robotic tools where DNN detectors cannot solve the correspondence problem correctly. In this work, we propose a new and autonomous way to define the keypoint locations that overcomes these challenges. The approach involves finding the optimal set of keypoints on robotic manipulators for robust visual detection and localization. Using a robotic simulator as a medium, our algorithm utilizes synthetic data for DNN training, and the proposed algorithm is used to optimize the selection of keypoints through an iterative approach. The results show that when using the optimized keypoints, the detection performance of the DNNs improved significantly. We further use the optimized keypoints for real robotic applications by using domain randomization to bridge the reality gap between the simulator and the physical world. The physical world experiments show how the proposed method can be applied to the wide-breadth of robotic applications that require visual feedback, such as camera-to-robot calibration, robotic tool tracking, and end-effector pose estimation.

## 参考
- http://arxiv.org/abs/2010.08054v3

## Overview
Keypoint detection is an essential building block for many robotic applications like motion capture and pose estimation. Historically, keypoints are detected using uniquely engineered markers such as checkerboards or fiducials. More recently, deep learning methods have been explored as they have the ability to detect user-defined keypoints in a marker-less manner. However, different manually selected keypoints can have uneven performance when it comes to detection and localization. An example of this can be found on symmetric robotic tools where DNN detectors cannot solve the correspondence problem correctly. In this work, we propose a new and autonomous way to define the keypoint locations that overcomes these challenges. The approach involves finding the optimal set of keypoints on robotic manipulators for robust visual detection and localization. Using a robotic simulator as a medium, our algorithm utilizes synthetic data for DNN training, and the proposed algorithm is used to optimize the selection of keypoints through an iterative approach. The results show that when using the optimized keypoints, the detection performance of the DNNs improved significantly. We further use the optimized keypoints for real robotic applications by using domain randomization to bridge the reality gap between the simulator and the physical world. The physical world experiments show how the proposed method can be applied to the wide-breadth of robotic applications that require visual feedback, such as camera-to-robot calibration, robotic tool tracking, and end-effector pose estimation.

## Content
Keypoint detection is an essential building block for many robotic applications like motion capture and pose estimation. Historically, keypoints are detected using uniquely engineered markers such as checkerboards or fiducials. More recently, deep learning methods have been explored as they have the ability to detect user-defined keypoints in a marker-less manner. However, different manually selected keypoints can have uneven performance when it comes to detection and localization. An example of this can be found on symmetric robotic tools where DNN detectors cannot solve the correspondence problem correctly. In this work, we propose a new and autonomous way to define the keypoint locations that overcomes these challenges. The approach involves finding the optimal set of keypoints on robotic manipulators for robust visual detection and localization. Using a robotic simulator as a medium, our algorithm utilizes synthetic data for DNN training, and the proposed algorithm is used to optimize the selection of keypoints through an iterative approach. The results show that when using the optimized keypoints, the detection performance of the DNNs improved significantly. We further use the optimized keypoints for real robotic applications by using domain randomization to bridge the reality gap between the simulator and the physical world. The physical world experiments show how the proposed method can be applied to the wide-breadth of robotic applications that require visual feedback, such as camera-to-robot calibration, robotic tool tracking, and end-effector pose estimation.

## 개요
키포인트 감지는 모션 캡처 및 자세 추정과 같은 많은 로봇 응용 분야에서 필수적인 구성 요소입니다. 역사적으로 키포인트는 체커보드나 기준 마커와 같은 특수하게 설계된 마커를 사용하여 감지되었습니다. 최근에는 마커 없이 사용자 정의 키포인트를 감지할 수 있는 딥러닝 방법이 탐구되고 있습니다. 그러나 수동으로 선택된 서로 다른 키포인트는 감지 및 위치 파악 성능이 고르지 않을 수 있습니다. 이러한 예는 대칭형 로봇 도구에서 DNN 감지기가 대응 문제를 올바르게 해결하지 못하는 경우에서 찾을 수 있습니다. 본 연구에서는 이러한 문제를 극복하기 위해 키포인트 위치를 정의하는 새롭고 자율적인 방법을 제안합니다. 이 접근법은 강건한 시각적 감지 및 위치 파악을 위해 로봇 매니퓰레이터에서 최적의 키포인트 집합을 찾는 것을 포함합니다. 로봇 시뮬레이터를 매개체로 사용하여, 우리의 알고리즘은 DNN 훈련을 위해 합성 데이터를 활용하며, 제안된 알고리즘은 반복적 접근을 통해 키포인트 선택을 최적화하는 데 사용됩니다. 결과는 최적화된 키포인트를 사용할 때 DNN의 감지 성능이 크게 향상됨을 보여줍니다. 또한 시뮬레이터와 물리적 세계 간의 현실 격차를 해소하기 위해 도메인 무작위화를 사용하여 최적화된 키포인트를 실제 로봇 응용 분야에 적용합니다. 물리적 세계 실험은 제안된 방법이 카메라-로봇 캘리브레이션, 로봇 도구 추적 및 엔드 이펙터 자세 추정과 같은 시각적 피드백이 필요한 다양한 로봇 응용 분야에 적용될 수 있음을 보여줍니다.

## 핵심 내용
키포인트 감지는 모션 캡처 및 자세 추정과 같은 많은 로봇 응용 분야에서 필수적인 구성 요소입니다. 역사적으로 키포인트는 체커보드나 기준 마커와 같은 특수하게 설계된 마커를 사용하여 감지되었습니다. 최근에는 마커 없이 사용자 정의 키포인트를 감지할 수 있는 딥러닝 방법이 탐구되고 있습니다. 그러나 수동으로 선택된 서로 다른 키포인트는 감지 및 위치 파악 성능이 고르지 않을 수 있습니다. 이러한 예는 대칭형 로봇 도구에서 DNN 감지기가 대응 문제를 올바르게 해결하지 못하는 경우에서 찾을 수 있습니다. 본 연구에서는 이러한 문제를 극복하기 위해 키포인트 위치를 정의하는 새롭고 자율적인 방법을 제안합니다. 이 접근법은 강건한 시각적 감지 및 위치 파악을 위해 로봇 매니퓰레이터에서 최적의 키포인트 집합을 찾는 것을 포함합니다. 로봇 시뮬레이터를 매개체로 사용하여, 우리의 알고리즘은 DNN 훈련을 위해 합성 데이터를 활용하며, 제안된 알고리즘은 반복적 접근을 통해 키포인트 선택을 최적화하는 데 사용됩니다. 결과는 최적화된 키포인트를 사용할 때 DNN의 감지 성능이 크게 향상됨을 보여줍니다. 또한 시뮬레이터와 물리적 세계 간의 현실 격차를 해소하기 위해 도메인 무작위화를 사용하여 최적화된 키포인트를 실제 로봇 응용 분야에 적용합니다. 물리적 세계 실험은 제안된 방법이 카메라-로봇 캘리브레이션, 로봇 도구 추적 및 엔드 이펙터 자세 추정과 같은 시각적 피드백이 필요한 다양한 로봇 응용 분야에 적용될 수 있음을 보여줍니다.
