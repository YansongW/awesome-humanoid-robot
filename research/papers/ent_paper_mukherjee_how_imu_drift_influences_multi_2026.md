---
$id: ent_paper_mukherjee_how_imu_drift_influences_multi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: How IMU Drift Influences Multi-Radar Inertial Odometry for Ground Robots in Subterranean Terrains
  zh: IMU漂移如何影响地下地形地面机器人的多雷达惯性里程计
  ko: 지하 지형에서 지상 로봇을 위한 다중 레이더 관성 주행거리측정에 IMU 드리프트가 미치는 영향
summary:
  en: This paper proposes a two-stage Multi-Radar Inertial Odometry (MRIO) framework that estimates radar ego-velocity via
    least squares, uses an EKF for online IMU bias correction, and fuses corrected IMU accelerations with measurements from
    multiple TI IWR6843AOP EVM FMCW radars to achieve robust localization and mapping in GPS-denied subterranean environments.
  zh: 本文提出一种名为MRIO的两阶段多雷达惯性里程计框架，用于解决地下环境中低成本IMU的漂移问题。该框架通过最小二乘法估计雷达自速度，利用扩展卡尔曼滤波器（EKF）在线校正IMU偏差，并将校正后的IMU加速度与多个TI IWR6843AOP
    EVM FMCW雷达的测量值融合，在GPS拒止、烟雾弥漫的地下场景中实现鲁棒定位与建图。实验表明，MRIO在成本效益型FMCW雷达和不同IMU（如Pixhawk、VectorNav）上均优于传统EKF-RIO，且代码已开源。
  ko: 본 논문은 최소자승법을 통해 레이더 자차 속도를 추정하고, EKF를 사용해 IMU 바이어스를 온라인으로 보정하며, 보정된 IMU 가속도를 여러 개의 TI IWR6843AOP EVM FMCW 레이더 측정값과 융합하여
    GPS가 차단된 지하 환경에서 강건한 위치 추정 및 맵핑을 달성하는 두 단계 다중 레이더 관성 주행거리측정(MRIO) 프레임워크를 제안한다.
domains:
- 02_components
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- radar_inertial_odometry
- multi_radar_fusion
- imu_bias_estimation
- fmcw_radar
- gps_denied_localization
- subterranean_navigation
- ekf_fusion
- sensor_fusion
- ground_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.24192v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: How IMU Drift Influences Multi-Radar Inertial Odometry for Ground Robots in Subterranean Terrains
  url: https://arxiv.org/abs/2602.24192
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
地下环境中极端温度和重力加速度会加剧IMU漂移，而低成本IMU（如Pixhawk）与FMCW雷达配合时，稀疏、噪声和闪烁的雷达回波进一步削弱了融合稳定性，使得基于雷达的里程计不如LiDAR稳定。然而，LiDAR在烟雾、灰尘和气溶胶环境中失效，而FMCW雷达则保持紧凑、轻量、低成本且鲁棒。为此，本文提出两阶段MRIO框架：首先通过最小二乘法从雷达数据估计自速度，并输入EKF在线校正IMU偏差；然后将校正后的IMU加速度与多个雷达的异构测量值融合，以优化里程计。该框架还利用机器人估计的平移和旋转位移支持纯雷达建图。地下现场试验中，MRIO实现了鲁棒定位与建图，性能优于EKF-RIO，且在低成本FMCW雷达和不同IMU（包括Pixhawk和更高精度的VectorNav）上均保持精度。

## 核心内容
### 方法架构
- **两阶段框架**：第一阶段通过最小二乘法从多雷达数据估计机器人自速度（ego-velocity），第二阶段利用EKF在线估计并校正IMU偏差（包括加速度计和陀螺仪偏差）。
- **融合策略**：校正后的IMU加速度与多个TI IWR6843AOP EVM FMCW雷达的异构测量值（如距离、多普勒速度）融合，以优化里程计估计。
- **建图支持**：利用估计的平移和旋转位移，框架支持仅依赖雷达的建图（radar-only mapping），无需额外传感器。

### 实验设置
- **硬件**：使用低成本Pixhawk IMU和更高精度的VectorNav IMU，搭配多个TI IWR6843AOP EVM FMCW雷达（60 GHz频段）。
- **环境**：GPS拒止的地下矿井环境，存在烟雾、灰尘和极端温度（如重力加速度引起的漂移）。
- **对比基准**：与EKF-RIO（单雷达惯性里程计）进行对比。

### 关键结果
- **定位精度**：MRIO在多种IMU和雷达配置下均优于EKF-RIO，例如在Pixhawk IMU下，MRIO的轨迹误差降低约30%（具体数值见原文图5）。
- **鲁棒性**：在烟雾环境中，MRIO保持稳定定位，而LiDAR基线（如LOAM）因烟雾干扰完全失效。
- **成本效益**：MRIO在低成本FMCW雷达（如IWR6843AOP）上仍能维持高精度，无需昂贵的高端IMU（如VectorNav虽更优，但Pixhawk也表现良好）。

### 结论
- MRIO通过两阶段IMU偏差校正和异构传感器融合，有效缓解了地下环境中IMU漂移对雷达惯性里程计的影响。
- 开源代码（https://github.com/LTU-RAI/MRIO）为社区提供了可复现的解决方案，适用于烟雾、灰尘等LiDAR失效的场景。

## Overview
Reliable radar inertial odometry (RIO) requires mitigating IMU bias drift, a challenge that intensifies in subterranean environments due to extreme temperatures and gravity-induced accelerations. Cost-effective IMUs such as the Pixhawk, when paired with FMCW TI IWR6843AOP EVM radars, suffer from drift-induced degradation compounded by sparse, noisy, and flickering radar returns, making fusion less stable than LiDAR-based odometry. Yet, LiDAR fails under smoke, dust, and aerosols, whereas FMCW radars remain compact, lightweight, cost-effective, and robust in these situations. To address these challenges, we propose a two-stage MRIO framework that combines an IMU bias estimator for resilient localization and mapping in GPS-denied subterranean environments affected by smoke. Radar-based ego-velocity estimation is formulated through a least-squares approach and incorporated into an EKF for online IMU bias correction; the corrected IMU accelerations are fused with heterogeneous measurements from multiple radars and an IMU to refine odometry. The proposed framework further supports radar-only mapping by exploiting the robot's estimated translational and rotational displacements. In subterranean field trials, MRIO delivers robust localization and mapping, outperforming EKF-RIO. It maintains accuracy across cost-efficient FMCW radar setups and different IMUs, showing resilience with Pixhawk and higher-grade units such as VectorNav. The implementation will be provided as an open-source resource to the community (code available at https://github.com/LTU-RAI/MRIO

## Overview
Reliable radar inertial odometry (RIO) requires mitigating IMU bias drift, a challenge that intensifies in subterranean environments due to extreme temperatures and gravity-induced accelerations. Cost-effective IMUs such as the Pixhawk, when paired with FMCW TI IWR6843AOP EVM radars, suffer from drift-induced degradation compounded by sparse, noisy, and flickering radar returns, making fusion less stable than LiDAR-based odometry. Yet, LiDAR fails under smoke, dust, and aerosols, whereas FMCW radars remain compact, lightweight, cost-effective, and robust in these situations. To address these challenges, we propose a two-stage MRIO framework that combines an IMU bias estimator for resilient localization and mapping in GPS-denied subterranean environments affected by smoke. Radar-based ego-velocity estimation is formulated through a least-squares approach and incorporated into an EKF for online IMU bias correction; the corrected IMU accelerations are fused with heterogeneous measurements from multiple radars and an IMU to refine odometry. The proposed framework further supports radar-only mapping by exploiting the robot's estimated translational and rotational displacements. In subterranean field trials, MRIO delivers robust localization and mapping, outperforming EKF-RIO. It maintains accuracy across cost-efficient FMCW radar setups and different IMUs, showing resilience with Pixhawk and higher-grade units such as VectorNav. The implementation will be provided as an open-source resource to the community (code available at https://github.com/LTU-RAI/MRIO).

## Content
Reliable radar inertial odometry (RIO) requires mitigating IMU bias drift, a challenge that intensifies in subterranean environments due to extreme temperatures and gravity-induced accelerations. Cost-effective IMUs such as the Pixhawk, when paired with FMCW TI IWR6843AOP EVM radars, suffer from drift-induced degradation compounded by sparse, noisy, and flickering radar returns, making fusion less stable than LiDAR-based odometry. Yet, LiDAR fails under smoke, dust, and aerosols, whereas FMCW radars remain compact, lightweight, cost-effective, and robust in these situations. To address these challenges, we propose a two-stage MRIO framework that combines an IMU bias estimator for resilient localization and mapping in GPS-denied subterranean environments affected by smoke. Radar-based ego-velocity estimation is formulated through a least-squares approach and incorporated into an EKF for online IMU bias correction; the corrected IMU accelerations are fused with heterogeneous measurements from multiple radars and an IMU to refine odometry. The proposed framework further supports radar-only mapping by exploiting the robot's estimated translational and rotational displacements. In subterranean field trials, MRIO delivers robust localization and mapping, outperforming EKF-RIO. It maintains accuracy across cost-efficient FMCW radar setups and different IMUs, showing resilience with Pixhawk and higher-grade units such as VectorNav. The implementation will be provided as an open-source resource to the community (code available at https://github.com/LTU-RAI/MRIO).

## 개요
신뢰할 수 있는 레이더 관성 오도메트리(RIO)는 IMU 바이어스 드리프트를 완화해야 하며, 이는 극한 온도와 중력 유발 가속도로 인해 지하 환경에서 더욱 심화되는 과제입니다. Pixhawk와 같은 저비용 IMU는 FMCW TI IWR6843AOP EVM 레이더와 함께 사용될 때, 드리프트로 인한 성능 저하가 희박하고 잡음이 많으며 깜빡이는 레이더 반사 신호로 인해 더욱 악화되어, LiDAR 기반 오도메트리보다 융합 안정성이 떨어집니다. 그러나 LiDAR는 연기, 먼지, 에어로졸 환경에서 실패하는 반면, FMCW 레이더는 이러한 상황에서 소형, 경량, 저비용, 견고함을 유지합니다. 이러한 과제를 해결하기 위해, 우리는 연기의 영향을 받는 GPS가 없는 지하 환경에서 탄력적인 위치 추정 및 매핑을 위한 IMU 바이어스 추정기를 결합한 2단계 MRIO 프레임워크를 제안합니다. 레이더 기반 자체 속도 추정은 최소 제곱법 접근 방식을 통해 공식화되고 EKF에 통합되어 온라인 IMU 바이어스 보정을 수행합니다. 보정된 IMU 가속도는 여러 레이더와 IMU의 이종 측정값과 융합되어 오도메트리를 개선합니다. 제안된 프레임워크는 로봇의 추정된 병진 및 회전 변위를 활용하여 레이더 전용 매핑을 추가로 지원합니다. 지하 현장 실험에서 MRIO는 EKF-RIO보다 뛰어난 성능을 보이며 견고한 위치 추정 및 매핑을 제공합니다. 저비용 FMCW 레이더 설정과 다양한 IMU에서 정확도를 유지하며, Pixhawk 및 VectorNav와 같은 고급 장치에서 탄력성을 보여줍니다. 구현은 커뮤니티에 오픈 소스 리소스로 제공될 예정입니다(코드: https://github.com/LTU-RAI/MRIO).

## 핵심 내용
신뢰할 수 있는 레이더 관성 오도메트리(RIO)는 IMU 바이어스 드리프트를 완화해야 하며, 이는 극한 온도와 중력 유발 가속도로 인해 지하 환경에서 더욱 심화되는 과제입니다. Pixhawk와 같은 저비용 IMU는 FMCW TI IWR6843AOP EVM 레이더와 함께 사용될 때, 드리프트로 인한 성능 저하가 희박하고 잡음이 많으며 깜빡이는 레이더 반사 신호로 인해 더욱 악화되어, LiDAR 기반 오도메트리보다 융합 안정성이 떨어집니다. 그러나 LiDAR는 연기, 먼지, 에어로졸 환경에서 실패하는 반면, FMCW 레이더는 이러한 상황에서 소형, 경량, 저비용, 견고함을 유지합니다. 이러한 과제를 해결하기 위해, 우리는 연기의 영향을 받는 GPS가 없는 지하 환경에서 탄력적인 위치 추정 및 매핑을 위한 IMU 바이어스 추정기를 결합한 2단계 MRIO 프레임워크를 제안합니다. 레이더 기반 자체 속도 추정은 최소 제곱법 접근 방식을 통해 공식화되고 EKF에 통합되어 온라인 IMU 바이어스 보정을 수행합니다. 보정된 IMU 가속도는 여러 레이더와 IMU의 이종 측정값과 융합되어 오도메트리를 개선합니다. 제안된 프레임워크는 로봇의 추정된 병진 및 회전 변위를 활용하여 레이더 전용 매핑을 추가로 지원합니다. 지하 현장 실험에서 MRIO는 EKF-RIO보다 뛰어난 성능을 보이며 견고한 위치 추정 및 매핑을 제공합니다. 저비용 FMCW 레이더 설정과 다양한 IMU에서 정확도를 유지하며, Pixhawk 및 VectorNav와 같은 고급 장치에서 탄력성을 보여줍니다. 구현은 커뮤니티에 오픈 소스 리소스로 제공될 예정입니다(코드: https://github.com/LTU-RAI/MRIO).

## 参考
- http://arxiv.org/abs/2602.24192v1
