---
$id: ent_component_inertial_measurement_unit_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Inertial Measurement Unit
  zh: 惯性测量单元
  ko: Inertial Measurement Unit
summary:
  en: Torso/hip-mounted sensor fusing accelerometer and gyroscope for balance and state estimation.
  zh: Analog Devices ADIS16475 微型 MEMS 惯性测量单元 / Analog Devices ADIS16475 Miniature MEMS IMU
  ko: 몸통/엉덩이에 장착된 가속도계 및 자이로스코프를 융합한 균형 및 상태 추정 센서.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- balance
- component
- imu
- sensor
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from kg/entities/ent_component_analog_devices_adis16475.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Inertial Measurement Unit
  url: https://en.wikipedia.org/wiki/Inertial_measurement_unit
  date: '2024'
  accessed_at: '2026-07-02'
---

## 概述
惯性测量单元是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## Analog Devices ADIS16475 微型 MEMS 惯性测量单元 / Analog Devices ADIS16475 Miniature MEMS IMU

### 概述

ADIS16475 是 Analog Devices 推出的精密、微型 MEMS 惯性测量单元（IMU），集成三轴陀螺仪与三轴加速度计，并内置温度传感器、信号调理、校准与数字滤波功能。该器件出厂前对每个传感器进行灵敏度、偏置、轴向对准、线性加速度（陀螺偏置）及撞击中心（加速度计位置）标定，可在宽温范围内提供高精度的六自由度惯性测量，适用于机器人、无人机、自动驾驶、工业稳定平台及导航系统等应用。

### 工作原理与技术架构

ADIS16475 采用 ADI iSensor 技术平台，核心架构包括：

1. **MEMS 惯性敏感单元**：三轴陀螺仪与三轴加速度计共用同一封装，通过精密微机械结构感知角速度与比力。
2. **信号调理与动态补偿**：每个传感器通道集成低噪声放大、滤波与 A/D 转换，工厂标定数据用于温度、非线性、轴间耦合及 $g$ 敏感补偿。
3. **内部处理器与寄存器**：通过 SPI 接口输出角速度、加速度、温度、增量角（delta angle）与增量速度（delta velocity）等数据。
4. **自检与同步**：支持按需自测试、Flash 自检、数据就绪指示及外部同步模式（direct/pulse/scaled/output）。

关键精度指标：

- **角随机游走（ARW）**：$0.15°/\sqrt{\text{hr}}$，表征陀螺角度积分噪声：
  $$
  \sigma_\theta(t) = \text{ARW} \cdot \sqrt{t}
  $$
- **运行中偏置稳定性**：陀螺仪典型值 $2°/\text{hr}$，加速度计 $3.6~\mu g$。
- **轴间对准误差**：$\pm 0.1°$，显著降低多传感器融合时的安装对准工作量。

### 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 传感器类型 | 6 轴 IMU（3 轴陀螺仪 + 3 轴加速度计）| ADI datasheet |
| 封装 | 44-ball BGA，约 11 mm × 15 mm × 11 mm | ADI datasheet |
| 陀螺仪量程 | ±125 °/s、±500 °/s、±2000 °/s（可选）| ADI datasheet |
| 加速度计量程 | ±8 g | ADI datasheet |
| 运行中陀螺偏置稳定性 | 2 °/hr（典型）| ADI datasheet |
| 角随机游走 | 0.15 °/√hr | ADI datasheet |
| 加速度计运行偏置稳定性 | 3.6 μg | ADI datasheet |
| 轴间对准误差 | ±0.1° | ADI datasheet |
| 输出数据 | 角速度、加速度、温度、delta angle、delta velocity | ADI datasheet |
| 接口 | SPI | ADI datasheet |
| 供电电压 | 3.0 V – 3.6 V | ADI datasheet |
| 工作电流 | 约 44 mA（典型）|  distributor |
| 工作温度 | −40 °C ~ +105 °C | ADI datasheet |
| 校准温度范围 | −40 °C ~ +85 °C | ADI datasheet |
| 抗冲击 | 2000 g | ADI datasheet |
| 价格 | 未公开 | - |

### 应用场景

- **人形机器人姿态估计**：为躯干、足部或头部提供高频惯性参考，与视觉、关节编码器融合实现稳定姿态估计。
- **无人机飞控**：用于姿态稳定、航向保持及导航解算。
- **自动驾驶与机器人导航**：与 GNSS/ LiDAR/ 视觉融合，提供高动态下的位姿推算。
- **工业稳定平台**：摄像头、天线、机械臂末端的主动减振与稳定控制。
- **精密仪器与测绘**：惯性测量、振动分析与运动捕捉。

### 供应链关系

- **上游**：MEMS 晶圆、ASIC 芯片、BGA 封装基板、精密电阻电容、温补算法 IP。
- **制造商**：Analog Devices 通过关系 `ent_company_analog_devices -- manufactures --> ent_component_analog_devices_adis16475` 记录于知识图谱。
- **下游**：机器人 OEM、无人机、自动驾驶平台、工业自动化、航空航天、医疗设备。主要竞争对手包括 Bosch Sensortec、STMicroelectronics、TDK InvenSense、Honeywell 等。

### 来源与验证

主要参数来自 Analog Devices 官方 ADIS16475 datasheet（Rev. C）及 DigiKey 授权分销商页面。陀螺仪量程、偏置稳定性、ARW、轴间对准误差、供电与温度范围等关键指标均在官方 datasheet 中明确。价格未公开。

## 参考
- [Inertial Measurement Unit](https://en.wikipedia.org/wiki/Inertial_measurement_unit)
- 项目 Wiki：kg/entities/ent_component_analog_devices_adis16475.md

## Overview
Inertial measurement units are important components in the field of humanoid robots. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Analog Devices ADIS16475 Miniature MEMS IMU

### Overview

The ADIS16475 is a precision, miniature MEMS inertial measurement unit (IMU) from Analog Devices, integrating a three-axis gyroscope and a three-axis accelerometer, along with built-in temperature sensors, signal conditioning, calibration, and digital filtering. Each sensor is factory-calibrated for sensitivity, bias, axial alignment, linear acceleration (gyroscope bias), and impact center (accelerometer position), providing high-precision six-degree-of-freedom inertial measurements over a wide temperature range. It is suitable for applications such as robotics, drones, autonomous driving, industrial stabilization platforms, and navigation systems.

### Working Principle and Technical Architecture

The ADIS16475 utilizes the ADI iSensor technology platform, with a core architecture including:

1. **MEMS Inertial Sensing Elements**: The three-axis gyroscope and three-axis accelerometer share the same package, sensing angular velocity and specific force through precision micromechanical structures.
2. **Signal Conditioning and Dynamic Compensation**: Each sensor channel integrates low-noise amplification, filtering, and A/D conversion. Factory calibration data is used for temperature, nonlinearity, cross-axis coupling, and $g$-sensitivity compensation.
3. **Internal Processor and Registers**: Outputs data such as angular velocity, acceleration, temperature, delta angle, and delta velocity via the SPI interface.
4. **Self-Test and Synchronization**: Supports on-demand self-test, flash self-test, data-ready indication, and external synchronization modes (direct/pulse/scaled/output).

Key accuracy specifications:

- **Angular Random Walk (ARW)**: $0.15°/\sqrt{\text{hr}}$, characterizing gyroscope angle integration noise:
  $$
  \sigma_\theta(t) = \text{ARW} \cdot \sqrt{t}
  $$
- **In-Run Bias Stability**: Typical values of $2°/\text{hr}$ for the gyroscope and $3.6~\mu g$ for the accelerometer.
- **Cross-Axis Alignment Error**: $\pm 0.1°$, significantly reducing installation alignment effort during multi-sensor fusion.

### Key Parameters

| Parameter | Value | Notes/Source |
|-----------|-------|--------------|
| Sensor Type | 6-axis IMU (3-axis gyroscope + 3-axis accelerometer) | ADI datasheet |
| Package | 44-ball BGA, approx. 11 mm × 15 mm × 11 mm | ADI datasheet |
| Gyroscope Range | ±125 °/s, ±500 °/s, ±2000 °/s (selectable) | ADI datasheet |
| Accelerometer Range | ±8 g | ADI datasheet |
| In-Run Gyroscope Bias Stability | 2 °/hr (typical) | ADI datasheet |
| Angular Random Walk | 0.15 °/√hr | ADI datasheet |
| In-Run Accelerometer Bias Stability | 3.6 μg | ADI datasheet |
| Cross-Axis Alignment Error | ±0.1° | ADI datasheet |
| Output Data | Angular velocity, acceleration, temperature, delta angle, delta velocity | ADI datasheet |
| Interface | SPI | ADI datasheet |
| Supply Voltage | 3.0 V – 3.6 V | ADI datasheet |
| Operating Current | Approx. 44 mA (typical) | Distributor |
| Operating Temperature | −40 °C ~ +105 °C | ADI datasheet |
| Calibration Temperature Range | −40 °C ~ +85 °C | ADI datasheet |
| Shock Resistance | 2000 g | ADI datasheet |
| Price | Not publicly available | - |

### Application Scenarios

- **Humanoid Robot Attitude Estimation**: Provides high-frequency inertial reference for the torso, feet, or head, fused with vision and joint encoders for stable attitude estimation.
- **Drone Flight Control**: Used for attitude stabilization, heading hold, and navigation calculations.
- **Autonomous Driving and Robot Navigation**: Fused with GNSS/LiDAR/vision for high-dynamic pose estimation.
- **Industrial Stabilization Platforms**: Active vibration damping and stabilization control for cameras, antennas, and robotic arm end-effectors.
- **Precision Instruments and Surveying**: Inertial measurement, vibration analysis, and motion capture.

### Supply Chain Relationships

- **Upstream**: MEMS wafers, ASIC chips, BGA package substrates, precision resistors and capacitors, temperature compensation algorithm IP.
- **Manufacturer**: Analog Devices, recorded in the knowledge graph via the relationship `ent_company_analog_devices -- manufactures --> ent_component_analog_devices_adis16475`.
- **Downstream**: Robot OEMs, drones, autonomous driving platforms, industrial automation, aerospace, medical devices. Main competitors include Bosch Sensortec, STMicroelectronics, TDK InvenSense, Honeywell, etc.

### Sources and Verification

Key parameters are sourced from the official Analog Devices ADIS16475 datasheet (Rev. C) and the DigiKey authorized distributor page. Critical specifications such as gyroscope range, bias stability, ARW, cross-axis alignment error, supply voltage, and temperature range are clearly stated in the official datasheet. The price is not publicly available.

## 개요
관성 측정 장치는 휴머노이드 로봇 분야의 중요한 부품입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
## Analog Devices ADIS16475 초소형 MEMS 관성 측정 장치 / Analog Devices ADIS16475 Miniature MEMS IMU

### 개요

ADIS16475는 Analog Devices에서 출시한 정밀 초소형 MEMS 관성 측정 장치(IMU)로, 3축 자이로스코프와 3축 가속도계를 통합하고 온도 센서, 신호 조정, 보정 및 디지털 필터링 기능을 내장하고 있습니다. 이 장치는 출하 전에 각 센서의 감도, 바이어스, 축 정렬, 선형 가속도(자이로 바이어스) 및 충격 중심(가속도계 위치)을 보정하여 넓은 온도 범위에서 고정밀 6자유도 관성 측정을 제공하며, 로봇, 드론, 자율 주행, 산업용 안정화 플랫폼 및 항법 시스템 등에 적용됩니다.

### 작동 원리 및 기술 아키텍처

ADIS16475는 ADI iSensor 기술 플랫폼을 기반으로 하며, 핵심 아키텍처는 다음과 같습니다:

1. **MEMS 관성 감지 소자**: 3축 자이로스코프와 3축 가속도계가 동일한 패키지에 통합되어 정밀 미세 기계 구조를 통해 각속도와 비력을 감지합니다.
2. **신호 조정 및 동적 보상**: 각 센서 채널에는 저잡음 증폭, 필터링 및 A/D 변환이 통합되어 있으며, 공장 보정 데이터는 온도, 비선형성, 축 간 결합 및 $g$ 민감도 보상에 사용됩니다.
3. **내부 프로세서 및 레지스터**: SPI 인터페이스를 통해 각속도, 가속도, 온도, 델타 각도 및 델타 속도 등의 데이터를 출력합니다.
4. **자체 테스트 및 동기화**: 온디맨드 자체 테스트, 플래시 자체 테스트, 데이터 준비 표시 및 외부 동기화 모드(direct/pulse/scaled/output)를 지원합니다.

주요 정밀도 지표:

- **각 랜덤 워크(ARW)**: $0.15°/\sqrt{\text{hr}}$로, 자이로 각도 적분 잡음을 나타냅니다:
  $$
  \sigma_\theta(t) = \text{ARW} \cdot \sqrt{t}
  $$
- **동작 중 바이어스 안정성**: 자이로스코프 일반값 $2°/\text{hr}$, 가속도계 $3.6~\mu g$.
- **축 간 정렬 오차**: $\pm 0.1°$로, 다중 센서 융합 시 설치 정렬 작업량을 크게 줄입니다.

### 주요 파라미터

| 파라미터 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 센서 유형 | 6축 IMU(3축 자이로스코프 + 3축 가속도계) | ADI 데이터시트 |
| 패키지 | 44볼 BGA, 약 11 mm × 15 mm × 11 mm | ADI 데이터시트 |
| 자이로스코프 범위 | ±125 °/s, ±500 °/s, ±2000 °/s(선택 가능) | ADI 데이터시트 |
| 가속도계 범위 | ±8 g | ADI 데이터시트 |
| 동작 중 자이로 바이어스 안정성 | 2 °/hr(일반) | ADI 데이터시트 |
| 각 랜덤 워크 | 0.15 °/√hr | ADI 데이터시트 |
| 가속도계 동작 바이어스 안정성 | 3.6 μg | ADI 데이터시트 |
| 축 간 정렬 오차 | ±0.1° | ADI 데이터시트 |
| 출력 데이터 | 각속도, 가속도, 온도, 델타 각도, 델타 속도 | ADI 데이터시트 |
| 인터페이스 | SPI | ADI 데이터시트 |
| 공급 전압 | 3.0 V – 3.6 V | ADI 데이터시트 |
| 동작 전류 | 약 44 mA(일반) | 유통업체 |
| 동작 온도 | −40 °C ~ +105 °C | ADI 데이터시트 |
| 보정 온도 범위 | −40 °C ~ +85 °C | ADI 데이터시트 |
| 내충격성 | 2000 g | ADI 데이터시트 |
| 가격 | 비공개 | - |

### 적용 시나리오

- **휴머노이드 로봇 자세 추정**: 몸통, 발 또는 머리에 고주파 관성 기준을 제공하여 비전, 관절 엔코더와 융합하여 안정적인 자세 추정 구현.
- **드론 비행 제어**: 자세 안정화, 방향 유지 및 항법 계산에 사용.
- **자율 주행 및 로봇 항법**: GNSS/LiDAR/비전과 융합하여 고동적 환경에서의 위치 추정 제공.
- **산업용 안정화 플랫폼**: 카메라, 안테나, 로봇 팔 끝단의 능동 진동 감쇠 및 안정화 제어.
- **정밀 기기 및 측량**: 관성 측정, 진동 분석 및 모션 캡처.

### 공급망 관계

- **상류**: MEMS 웨이퍼, ASIC 칩, BGA 패키지 기판, 정밀 저항 및 커패시터, 온도 보상 알고리즘 IP.
- **제조사**: Analog Devices는 관계 `ent_company_analog_devices -- manufactures --> ent_component_analog_devices_adis16475`를 통해 지식 그래프에 기록됨.
- **하류**: 로봇 OEM, 드론, 자율 주행 플랫폼, 산업 자동화, 항공 우주, 의료 기기. 주요 경쟁사로는 Bosch Sensortec, STMicroelectronics, TDK InvenSense, Honeywell 등이 있음.

### 출처 및 검증

주요 파라미터는 Analog Devices 공식 ADIS16475 데이터시트(Rev. C) 및 DigiKey 공인 유통업체 페이지에서 가져왔습니다. 자이로스코프 범위, 바이어스 안정성, ARW, 축 간 정렬 오차, 공급 전압 및 온도 범위 등 주요 지표는 공식 데이터시트에 명확히 명시되어 있습니다. 가격은 비공개입니다.
