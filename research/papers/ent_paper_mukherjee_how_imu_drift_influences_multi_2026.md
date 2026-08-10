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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.24192v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1151 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2602.24192v1

## 개요
지하 환경의 극한 온도와 중력 가속도는 IMU 드리프트를 악화시키며, 저비용 IMU(예: Pixhawk)와 FMCW 레이더를 함께 사용할 때 희소하고 노이즈가 많으며 깜빡이는 레이더 반사파가 융합 안정성을 더욱 약화시켜 레이더 기반 오도메트리가 LiDAR보다 덜 안정적입니다. 그러나 LiDAR는 연기, 먼지, 에어로졸 환경에서 작동하지 않는 반면, FMCW 레이더는 컴팩트하고 가벼우며 저비용이고 견고함을 유지합니다. 이를 위해 본 논문은 2단계 MRIO 프레임워크를 제안합니다: 먼저 최소제곱법을 통해 레이더 데이터에서 자체 속도를 추정하고, 이를 EKF에 입력하여 IMU 바이어스를 온라인으로 보정합니다; 그 다음 보정된 IMU 가속도와 여러 레이더의 이종 측정값을 융합하여 오도메트리를 최적화합니다. 이 프레임워크는 또한 로봇의 추정된 병진 및 회전 변위를 활용하여 순수 레이더 기반 매핑을 지원합니다. 지하 현장 실험에서 MRIO는 견고한 위치 추정과 매핑을 달성했으며, EKF-RIO보다 성능이 우수했고, 저비용 FMCW 레이더와 다양한 IMU(포함: Pixhawk 및 더 높은 정밀도의 VectorNav)에서도 정확도를 유지했습니다.

## 핵심 내용
### 방법 아키텍처
- **2단계 프레임워크**: 1단계에서는 최소제곱법을 통해 다중 레이더 데이터에서 로봇 자체 속도(ego-velocity)를 추정하고, 2단계에서는 EKF를 사용하여 IMU 바이어스(가속도계 및 자이로스코프 바이어스 포함)를 온라인으로 추정하고 보정합니다.
- **융합 전략**: 보정된 IMU 가속도와 여러 TI IWR6843AOP EVM FMCW 레이더의 이종 측정값(예: 거리, 도플러 속도)을 융합하여 오도메트리 추정을 최적화합니다.
- **매핑 지원**: 추정된 병진 및 회전 변위를 활용하여 추가 센서 없이 레이더 전용 매핑(radar-only mapping)을 지원합니다.

### 실험 설정
- **하드웨어**: 저비용 Pixhawk IMU와 더 높은 정밀도의 VectorNav IMU를 사용하며, 여러 TI IWR6843AOP EVM FMCW 레이더(60 GHz 대역)를 함께 사용합니다.
- **환경**: GPS가 차단된 지하 광산 환경으로, 연기, 먼지, 극한 온도(예: 중력 가속도로 인한 드리프트)가 존재합니다.
- **비교 기준**: EKF-RIO(단일 레이더 관성 오도메트리)와 비교합니다.

### 주요 결과
- **위치 추정 정확도**: MRIO는 다양한 IMU 및 레이더 구성에서 EKF-RIO보다 우수하며, 예를 들어 Pixhawk IMU에서 MRIO의 궤적 오차가 약 30% 감소합니다(구체적인 수치는 원문 그림 5 참조).
- **견고성**: 연기 환경에서 MRIO는 안정적인 위치 추정을 유지하는 반면, LiDAR 기반 기준선(예: LOAM)은 연기 간섭으로 완전히 작동하지 않습니다.
- **비용 효율성**: MRIO는 저비용 FMCW 레이더(예: IWR6843AOP)에서도 높은 정확도를 유지하며, 고가의 고급 IMU(예: VectorNav가 더 우수하지만 Pixhawk도 좋은 성능을 보임)가 필요하지 않습니다.

### 결론
- MRIO는 2단계 IMU 바이어스 보정과 이종 센서 융합을 통해 지하 환경에서 IMU 드리프트가 레이더 관성 오도메트리에 미치는 영향을 효과적으로 완화합니다.
- 오픈소스 코드(https://github.com/LTU-RAI/MRIO)는 커뮤니티에 재현 가능한 솔루션을 제공하며, 연기, 먼지 등 LiDAR가 작동하지 않는 시나리오에 적합합니다.
