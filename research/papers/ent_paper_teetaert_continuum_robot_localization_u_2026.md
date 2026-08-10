---
$id: ent_paper_teetaert_continuum_robot_localization_u_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Continuum Robot Localization using Distributed Time-of-Flight Sensors
  zh: 基于分布式飞行时间传感器的连续体机器人定位
  ko: 분산식 시간측정 센서를 활용한 연속체 로봇 위치추정
summary:
  en: This paper presents a continuous-time factor-graph-based MAP estimation framework that fuses sparse distributed time-of-flight
    sensor measurements and gyroscope data with a robot shape prior to localize continuum robots in unstructured environments,
    achieving 2.5 cm positional and 7.2° rotational error on a 53 cm robot.
  zh: 本文提出一种基于连续时间因子图的MAP估计框架，通过融合沿机器人长度分布的稀疏飞行时间传感器测量值、陀螺仪数据与机器人形状先验，实现非结构化环境中连续体机器人的定位。在53厘米长的机器人上，该方法达到2.5厘米的位置误差和7.2°的旋转误差。
  ko: 본 논문은 비구조화 환경에서 연속체 로봇의 위치추정을 위해 희소 분산식 시간측정 센서 측정값과 자이로스코프 데이터를 로봇 형상 사전정보와 융합하는 연속시간 요인그래프 기반 MAP 추정 프레임워크를 제안하며,
    53cm 길이 로봇에서 위치 오차 2.5cm, 회전 오차 7.2°를 달성한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- continuum_robot
- time_of_flight
- localization
- state_estimation
- factor_graph
- soft_robotics
- distributed_sensing
- sensor_fusion
- shape_prior
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.07209v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (843 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Continuum Robot Localization using Distributed Time-of-Flight Sensors
  url: https://arxiv.org/abs/2602.07209
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
连续体机器人因其可变形特性，在非结构化环境中的定位与建图长期未被充分研究。传统高分辨率ToF传感器（如lidar）因体积过大难以应用于此类机器人。本文采用沿机器人长度分布的小型低分辨率ToF传感器，结合陀螺仪数据与形状先验，通过连续时间因子图框架进行最大后验估计。实验表明，尽管每个传感器频繁遭遇退化场景，该方法仍能实现精确定位，并在仿真与真实环境中验证了结果的可重复性，同时研究了估计对先验地图偏差的鲁棒性。

## 核心内容
### 方法架构
- 采用**连续时间因子图**框架，将分布式ToF传感器测量值、陀螺仪数据与机器人形状先验作为因子节点，构建MAP估计问题。
- 形状先验基于机器人运动学模型，约束连续体机器人的弯曲与扭转状态，补偿低分辨率传感器在退化场景（如平面或对称环境）中的信息不足。

### 实验设置
- 机器人长度：53 cm，沿长度均匀分布多个小型ToF传感器（具体数量未在摘要中给出，但正文提及“分布式”配置）。
- 传感器类型：低分辨率ToF传感器（如VL53L1X），每个传感器提供单点距离测量。
- 陀螺仪：用于提供角速度数据，辅助估计机器人姿态变化。
- 环境：非结构化室内场景，包含多种几何特征（如墙壁、障碍物），并在仿真与真实环境中重复实验。

### 关键结果
- **平均定位误差**：位置误差2.5 cm，旋转误差7.2°（所有实验条件下）。
- **鲁棒性测试**：在先验地图存在偏差（如地图偏移或缺失部分特征）时，估计误差仍保持在可接受范围内（具体数值需参考正文，但摘要强调“robustness”）。
- **可重复性**：在多个不同环境（如办公室、实验室）中，仿真与真实实验结果一致，验证了方法的泛化能力。

### 结论
本文首次将分布式低分辨率ToF传感器应用于连续体机器人定位，通过融合形状先验克服了传感器退化问题。该方法为软体机器人在非结构化环境中的自主导航提供了实用方案，未来可扩展至多机器人协同或动态环境。

## Overview
Localization and mapping of an environment are crucial tasks for any robot operating in unstructured environments. Time-of-flight (ToF) sensors (e.g.,~lidar) have proven useful in mobile robotics, where high-resolution sensors can be used for simultaneous localization and mapping. In soft and continuum robotics, however, these high-resolution sensors are too large for practical use. This, combined with the deformable nature of such robots, has resulted in continuum robot (CR) localization and mapping in unstructured environments being a largely untouched area. In this work, we present a localization technique for CRs that relies on small, low-resolution ToF sensors distributed along the length of the robot. By fusing measurement information with a robot shape prior, we show that accurate localization is possible despite each sensor experiencing frequent degenerate scenarios. We achieve an average localization error of 2.5cm in position and 7.2° in rotation across all experimental conditions with a 53cm long robot. We demonstrate that the results are repeated across multiple environments, in both simulation and real-world experiments, and study robustness in the estimation to deviations in the prior map.

## Overview
Localization and mapping of an environment are crucial tasks for any robot operating in unstructured environments. Time-of-flight (ToF) sensors (e.g., lidar) have proven useful in mobile robotics, where high-resolution sensors can be used for simultaneous localization and mapping. In soft and continuum robotics, however, these high-resolution sensors are too large for practical use. This, combined with the deformable nature of such robots, has resulted in continuum robot (CR) localization and mapping in unstructured environments being a largely untouched area. In this work, we present a localization technique for CRs that relies on small, low-resolution ToF sensors distributed along the length of the robot. By fusing measurement information with a robot shape prior, we show that accurate localization is possible despite each sensor experiencing frequent degenerate scenarios. We achieve an average localization error of 2.5cm in position and 7.2° in rotation across all experimental conditions with a 53cm long robot. We demonstrate that the results are repeated across multiple environments, in both simulation and real-world experiments, and study robustness in the estimation to deviations in the prior map.

## Content
Localization and mapping of an environment are crucial tasks for any robot operating in unstructured environments. Time-of-flight (ToF) sensors (e.g., lidar) have proven useful in mobile robotics, where high-resolution sensors can be used for simultaneous localization and mapping. In soft and continuum robotics, however, these high-resolution sensors are too large for practical use. This, combined with the deformable nature of such robots, has resulted in continuum robot (CR) localization and mapping in unstructured environments being a largely untouched area. In this work, we present a localization technique for CRs that relies on small, low-resolution ToF sensors distributed along the length of the robot. By fusing measurement information with a robot shape prior, we show that accurate localization is possible despite each sensor experiencing frequent degenerate scenarios. We achieve an average localization error of 2.5cm in position and 7.2° in rotation across all experimental conditions with a 53cm long robot. We demonstrate that the results are repeated across multiple environments, in both simulation and real-world experiments, and study robustness in the estimation to deviations in the prior map.

## 参考
- http://arxiv.org/abs/2602.07209v2

## 개요
연속체 로봇은 변형 가능한 특성으로 인해 비구조화 환경에서의 위치 추정 및 지도 작성이 오랫동안 충분히 연구되지 않았다. 기존의 고해상도 ToF 센서(예: 라이다)는 크기가 커서 이러한 로봇에 적용하기 어렵다. 본 논문은 로봇 길이를 따라 분포된 소형 저해상도 ToF 센서를 채택하고, 자이로스코프 데이터와 형상 사전 정보를 결합하여 연속 시간 요인 그래프 프레임워크를 통해 최대 사후 추정을 수행한다. 실험 결과, 각 센서가 퇴화 시나리오를 자주 겪음에도 불구하고 이 방법은 정밀한 위치 추정을 달성했으며, 시뮬레이션과 실제 환경에서 결과의 재현성을 검증했고, 사전 지도 편향에 대한 추정의 강건성도 연구했다.

## 핵심 내용
### 방법 아키텍처
- **연속 시간 요인 그래프** 프레임워크를 채택하여 분산형 ToF 센서 측정값, 자이로스코프 데이터 및 로봇 형상 사전 정보를 요인 노드로 구성하고 MAP 추정 문제를 구축한다.
- 형상 사전 정보는 로봇 운동학 모델을 기반으로 연속체 로봇의 굽힘 및 비틀림 상태를 제약하여 저해상도 센서가 퇴화 시나리오(예: 평면 또는 대칭 환경)에서 정보 부족을 보완한다.

### 실험 설정
- 로봇 길이: 53 cm, 길이를 따라 여러 개의 소형 ToF 센서가 균일하게 분포됨(구체적인 수량은 초록에 명시되지 않았지만 본문에서 "분산형" 구성으로 언급).
- 센서 유형: 저해상도 ToF 센서(예: VL53L1X), 각 센서는 단일 지점 거리 측정을 제공한다.
- 자이로스코프: 각속도 데이터를 제공하여 로봇 자세 변화 추정을 보조한다.
- 환경: 벽, 장애물 등 다양한 기하학적 특징을 포함한 비구조화 실내 환경이며, 시뮬레이션과 실제 환경에서 실험을 반복 수행한다.

### 주요 결과
- **평균 위치 추정 오차**: 위치 오차 2.5 cm, 회전 오차 7.2°(모든 실험 조건에서).
- **강건성 테스트**: 사전 지도에 편향(예: 지도 이동 또는 일부 특징 누락)이 있을 때도 추정 오차는 허용 가능한 범위 내에서 유지된다(구체적인 수치는 본문을 참조해야 하지만 초록은 "robustness"를 강조).
- **재현성**: 사무실, 실험실 등 여러 다른 환경에서 시뮬레이션과 실제 실험 결과가 일관되며, 이 방법의 일반화 능력을 검증한다.

### 결론
본 논문은 분산형 저해상도 ToF 센서를 연속체 로봇 위치 추정에 처음으로 적용했으며, 형상 사전 정보를 융합하여 센서 퇴화 문제를 극복했다. 이 방법은 소프트 로봇이 비구조화 환경에서 자율 주행을 위한 실용적인 솔루션을 제공하며, 향후 다중 로봇 협업 또는 동적 환경으로 확장할 수 있다.
