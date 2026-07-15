---
$id: ent_component_imu_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Inertial Measurement Unit
  zh: 惯性测量单元
  ko: 관성 측정 장치
summary:
  en: Sensor package combining accelerometers and gyroscopes to estimate orientation, angular velocity, and linear acceleration
    of a robot.
  zh: '核心内容 ## Analog Devices ADIS16475 微型 MEMS 惯性测量单元 / Analog Devices ADIS16475 Miniature MEMS IMU'
  ko: 가속도계와 자이로스코프를 결합하여 로봇의 자세, 각속도, 선가속도를 추정하는 센서 패키지.
domains:
- 02_components
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component
- sensor
- imu
- inertial
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
  accessed_at: '2026-07-13'
---

## 概述
惯性测量单元是人形机器人领域的重要component。以下内容整理自项目 Wiki，供深入查阅。

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


