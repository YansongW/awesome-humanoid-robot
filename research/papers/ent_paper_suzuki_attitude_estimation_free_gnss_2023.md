---
$id: ent_paper_suzuki_attitude_estimation_free_gnss_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Attitude-Estimation-Free GNSS and IMU Integration
  zh: 无需姿态估计的GNSS/IMU融合定位
  ko: 자세 추정 없는 GNSS/IMU 통합 위치 추정
summary:
  en: Proposes an optimization-based GNSS/IMU integration method that avoids attitude estimation by using acceleration-magnitude
    and velocity-vector angular-change constraints, reducing calibration sensitivity and improving robustness to multipath
    and GNSS outages.
  zh: 提出了一种基于优化的GNSS/IMU融合定位方法，仅利用加速度计幅值与速度矢量角度变化约束来避免姿态估计，从而降低对IMU安装标定的敏感性，并提升多路径与GNSS中断时的鲁棒性。
  ko: 가속도계 크기와 속도 벡터 각도 변화 제약만을 사용하여 자세 추정 없이 GNSS/IMU를 융합하는 최적화 기반 위치 추정 방법을 제안하여 IMU 장착 오차에 둔감하고 다중경로·GNSS 단절에 강건함을 보였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- gnss_imu_fusion
- outdoor_localization
- sensor_fusion
- attitude_free_estimation
- factor_graph
- multipath_robustness
- localization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2304.10142v2.
sources:
- id: src_001
  type: paper
  title: Attitude-Estimation-Free GNSS and IMU Integration
  url: https://arxiv.org/abs/2304.10142
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
A global navigation satellite system (GNSS) is a sensor that can acquire 3D position and velocity in an earth-fixed coordinate system and is widely used for outdoor position estimation of robots and vehicles. Various GNSS/inertial measurement unit (IMU) integration methods have been proposed to improve the accuracy and availability of GNSS positioning. However, all these methods require the addition of a 3D attitude to the estimated state to fuse the IMU data. In this study, we propose a new optimization-based positioning method for combining GNSS and IMU that does not require attitude estimation. The proposed method uses two types of constraints: one is a constraint between states using only the magnitude of the 3D acceleration observed by an accelerometer, and the other is a constraint on the angle between the velocity vectors using the angular change measured by a gyroscope. The evaluation results with the simulation data show that the proposed method maintains the position estimation accuracy even when the IMU mounting position error increases and improves the accuracy when the GNSS observations contain multipath errors or missing data. The proposed method could improve positioning accuracy in experiments using IMUs acquired in real environments.

## 核心内容
A global navigation satellite system (GNSS) is a sensor that can acquire 3D position and velocity in an earth-fixed coordinate system and is widely used for outdoor position estimation of robots and vehicles. Various GNSS/inertial measurement unit (IMU) integration methods have been proposed to improve the accuracy and availability of GNSS positioning. However, all these methods require the addition of a 3D attitude to the estimated state to fuse the IMU data. In this study, we propose a new optimization-based positioning method for combining GNSS and IMU that does not require attitude estimation. The proposed method uses two types of constraints: one is a constraint between states using only the magnitude of the 3D acceleration observed by an accelerometer, and the other is a constraint on the angle between the velocity vectors using the angular change measured by a gyroscope. The evaluation results with the simulation data show that the proposed method maintains the position estimation accuracy even when the IMU mounting position error increases and improves the accuracy when the GNSS observations contain multipath errors or missing data. The proposed method could improve positioning accuracy in experiments using IMUs acquired in real environments.

## 参考
- http://arxiv.org/abs/2304.10142v2

## Overview
A global navigation satellite system (GNSS) is a sensor that can acquire 3D position and velocity in an earth-fixed coordinate system and is widely used for outdoor position estimation of robots and vehicles. Various GNSS/inertial measurement unit (IMU) integration methods have been proposed to improve the accuracy and availability of GNSS positioning. However, all these methods require the addition of a 3D attitude to the estimated state to fuse the IMU data. In this study, we propose a new optimization-based positioning method for combining GNSS and IMU that does not require attitude estimation. The proposed method uses two types of constraints: one is a constraint between states using only the magnitude of the 3D acceleration observed by an accelerometer, and the other is a constraint on the angle between the velocity vectors using the angular change measured by a gyroscope. The evaluation results with the simulation data show that the proposed method maintains the position estimation accuracy even when the IMU mounting position error increases and improves the accuracy when the GNSS observations contain multipath errors or missing data. The proposed method could improve positioning accuracy in experiments using IMUs acquired in real environments.

## Content
A global navigation satellite system (GNSS) is a sensor that can acquire 3D position and velocity in an earth-fixed coordinate system and is widely used for outdoor position estimation of robots and vehicles. Various GNSS/inertial measurement unit (IMU) integration methods have been proposed to improve the accuracy and availability of GNSS positioning. However, all these methods require the addition of a 3D attitude to the estimated state to fuse the IMU data. In this study, we propose a new optimization-based positioning method for combining GNSS and IMU that does not require attitude estimation. The proposed method uses two types of constraints: one is a constraint between states using only the magnitude of the 3D acceleration observed by an accelerometer, and the other is a constraint on the angle between the velocity vectors using the angular change measured by a gyroscope. The evaluation results with the simulation data show that the proposed method maintains the position estimation accuracy even when the IMU mounting position error increases and improves the accuracy when the GNSS observations contain multipath errors or missing data. The proposed method could improve positioning accuracy in experiments using IMUs acquired in real environments.

## 개요
GNSS(Global Navigation Satellite System)는 지구 고정 좌표계에서 3차원 위치와 속도를 획득할 수 있는 센서로, 로봇 및 차량의 실외 위치 추정에 널리 사용됩니다. GNSS 측위의 정확도와 가용성을 향상시키기 위해 다양한 GNSS/관성 측정 장치(IMU) 통합 방법이 제안되었습니다. 그러나 이러한 모든 방법은 IMU 데이터를 융합하기 위해 추정 상태에 3차원 자세를 추가해야 합니다. 본 연구에서는 자세 추정이 필요 없는 GNSS와 IMU 결합을 위한 새로운 최적화 기반 측위 방법을 제안합니다. 제안된 방법은 두 가지 유형의 제약 조건을 사용합니다. 하나는 가속도계에서 관찰된 3차원 가속도의 크기만을 사용하는 상태 간 제약 조건이고, 다른 하나는 자이로스코프로 측정된 각도 변화를 이용한 속도 벡터 간 각도 제약 조건입니다. 시뮬레이션 데이터를 통한 평가 결과, 제안된 방법은 IMU 장착 위치 오차가 증가하더라도 위치 추정 정확도를 유지하며, GNSS 관측값에 다중 경로 오차나 데이터 누락이 있을 때 정확도를 향상시킵니다. 제안된 방법은 실제 환경에서 획득한 IMU를 사용한 실험에서 측위 정확도를 개선할 수 있습니다.

## 핵심 내용
GNSS(Global Navigation Satellite System)는 지구 고정 좌표계에서 3차원 위치와 속도를 획득할 수 있는 센서로, 로봇 및 차량의 실외 위치 추정에 널리 사용됩니다. GNSS 측위의 정확도와 가용성을 향상시키기 위해 다양한 GNSS/관성 측정 장치(IMU) 통합 방법이 제안되었습니다. 그러나 이러한 모든 방법은 IMU 데이터를 융합하기 위해 추정 상태에 3차원 자세를 추가해야 합니다. 본 연구에서는 자세 추정이 필요 없는 GNSS와 IMU 결합을 위한 새로운 최적화 기반 측위 방법을 제안합니다. 제안된 방법은 두 가지 유형의 제약 조건을 사용합니다. 하나는 가속도계에서 관찰된 3차원 가속도의 크기만을 사용하는 상태 간 제약 조건이고, 다른 하나는 자이로스코프로 측정된 각도 변화를 이용한 속도 벡터 간 각도 제약 조건입니다. 시뮬레이션 데이터를 통한 평가 결과, 제안된 방법은 IMU 장착 위치 오차가 증가하더라도 위치 추정 정확도를 유지하며, GNSS 관측값에 다중 경로 오차나 데이터 누락이 있을 때 정확도를 향상시킵니다. 제안된 방법은 실제 환경에서 획득한 IMU를 사용한 실험에서 측위 정확도를 개선할 수 있습니다.
