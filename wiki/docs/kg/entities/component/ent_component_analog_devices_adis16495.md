---
id: ent_component_analog_devices_adis16495
type: component
schema_version: 1
domain: 02_components
status: active
names:
  zh: Analog Devices ADIS16495 战术级六轴惯性测量单元
  en: Analog Devices ADIS16495 Tactical-Grade Six-Axis IMU
sources:
- id: src_analog_devices_adis16495_datasheet
  type: website
- title: ADIS16495 Datasheet
  url: https://www.analog.com/en/products/adis16495.html
- id: src_analog_devices_adis16477_family
  type: website
- title: ADIS16477 Precision Miniature MEMS IMU Datasheet
  url: https://static.chipdip.ru/lib/717/DOC011717749.pdf
- id: src_analog_devices_official
  type: website
- title: Analog Devices 官网
  url: https://www.analog.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official Analog Devices datasheets and product
    pages; ADIS16495 exact variant suffix determines gyroscope range.
---


# Analog Devices ADIS16495 战术级六轴惯性测量单元 / Analog Devices ADIS16495 Tactical-Grade Six-Axis IMU

## 概述

ADIS16495 是 Analog Devices（ADI）推出的战术级六轴惯性测量单元（IMU），集成三轴 MEMS 陀螺仪与三轴 MEMS 加速度计，并内置温度传感器。该模块采用 24 引脚封装，提供 SPI 数字输出，具备低漂移、低噪声、高抗冲击与宽温工作特性，适用于人形机器人姿态估计、导航、运动控制、无人机飞控、自动驾驶与工业稳定平台。

## 工作原理 / 技术架构

ADIS16495 基于 ADI iSensor MEMS 技术，通过以下方式实现高精度惯性测量：

1. **三轴陀螺仪**：测量载体绕 X、Y、Z 三轴的角速度，采用 MEMS 谐振结构，通过科里奥利力将角速度转换为电容变化。
2. **三轴加速度计**：测量三轴线性加速度，基于 MEMS 质量块-弹簧-阻尼系统，通过检测质量块位移获得加速度信号。
3. **信号调理与校准**：每个传感器均经过工厂校准，补偿灵敏度、偏置、轴向对准、线性加速度（陀螺仪偏置）与冲击响应（加速度计位置），并通过动态补偿公式在宽温度范围内保持精度。
4. **温度传感器与自诊断**：内置温度传感器用于热补偿，支持自测试与flash 存储器校验。

IMU 的姿态估计误差主要由陀螺仪偏置不稳定性 $B$ 与角随机游走 $N$ 决定。在纯惯性导航模式下，航向角误差随时间 $t$ 增长可近似表示为

$$
\sigma_{\theta}(t) \approx B \cdot t + N \cdot \sqrt{t}
$$

ADIS16495 的典型运行偏置稳定性为 0.8°/hr，角随机游走为 0.09°/√hr，属于战术级 IMU 性能区间。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | Analog Devices（ADI） | 官网 |
| 传感器类型 | 6 轴 IMU（3 轴陀螺仪 + 3 轴加速度计） | 官方 datasheet |
| 封装 | 24 引脚模块（带连接器接口） | 官方 datasheet |
| 加速度计量程 | ±8 g | 官方 datasheet |
| 陀螺仪量程 | ±125°/s / ±450°/s / ±2000°/s（可选型号） | 官方 datasheet |
| 运行偏置稳定性 | 0.8°/hr（典型值） | 官方 datasheet |
| 角随机游走 | 0.09°/√hr | 官方 datasheet |
| 轴间对准误差 | ±0.1° | 官方 datasheet |
| 输出接口 | SPI | 官方 datasheet |
| 供电电压 | 3.0 V – 3.6 V | 官方 datasheet |
| 工作电流 | 89 mA | 官方 datasheet |
| 工作温度 | -40 °C – +105 °C | 官方 datasheet |
| 抗冲击 | 2,000 g | 官方 datasheet |
| 分辨率 | 32 bit | 官方资料 |
| 灵敏度 | 10,485,760 LSB/(°/s)，262,144,000 LSB/g | 官方资料 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **人形机器人姿态估计与平衡控制**：安装于躯干或足部，实时估计机器人姿态、角速度与加速度，支撑全身平衡与步态规划。
- **无人机飞控与导航**：为飞控系统提供高动态姿态参考，支持 GPS 拒止环境下的短期惯性导航。
- **自动驾驶与机器人底盘**：与轮速计、GNSS、激光雷达融合，提升定位与建图精度。
- **工业稳定平台与精密仪器**：用于光电吊舱、天线稳定平台、测绘仪器的振动抑制与姿态保持。
- **医疗与外骨骼**：为康复机器人、外骨骼提供运动意图识别与步态相位检测。

## 供应链关系

Analog Devices（`ent_company_analog_devices`）是全球领先的模拟、混合信号与数字信号处理半导体公司，其 iSensor MEMS IMU 产品线覆盖工业、战术与导航级应用。ADIS16495（`ent_component_analog_devices_adis16495`）属于战术级 6 轴 IMU，与 ADIS16475、ADIS16465 等形成产品矩阵。ADI 的上游包括 MEMS 晶圆、ASIC 代工、封装材料与精密电阻电容；下游客户覆盖机器人 OEM、无人机、自动驾驶、航空航天与工业自动化厂商。ADI 与 Bosch Sensortec、STMicroelectronics、TDK InvenSense、Honeywell、NovAtel 等形成竞争。

## 来源与验证

- Analog Devices 官网与 ADIS16495 产品页确认了其封装、量程、接口与工作环境。
- ADI 官方 datasheet 提供了运行偏置稳定性、角随机游走、工作电流、抗冲击等关键指标。
- ADIS16477  datasheet 展示了同系列 IMU 的校准补偿机制与典型性能框架，可作为 ADIS16495 技术路线的参考。