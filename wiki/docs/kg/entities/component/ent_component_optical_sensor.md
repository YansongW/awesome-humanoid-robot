---
id: ent_component_optical_sensor
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 光学传感器
  en: Optical Sensor
status: active
sources:
- id: src_ams_mira220_datasheet
  type: website
  url: https://ams-osram.com/products/sensors/image-sensors/ams-mira220-2-2mp-nir-enhanced-image-sensor
- id: src_ams_mira220_prod
  type: website
  url: https://ams-osram.com/products/sensors/image-sensors/ams-mira220-2-2mp-nir-enhanced-image-sensor
- id: src_ams_mira220_ai_sensors
  type: website
  url: https://ams-osram.com/products/sensors/image-sensors
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 光学传感器 / Optical Sensor

## 概述

光学传感器是将光信号转换为电信号的器件，按工作原理可分为光电二极管、CCD/CMOS 图像传感器、ToF 传感器、环境光传感器等。作为通用技术类别节点，以下以 ams OSRAM Mira220 作为全球快门 CMOS 图像传感器的代表型号，说明机器人视觉与感知系统中光学传感器的关键参数。

## 工作原理 / 技术架构

CMOS 图像传感器通过光电二极管阵列将入射光子转换为电子-空穴对，收集的信号电荷经微透镜、滤色片后由像素级读出电路转换为电压信号，再由 ADC 量化输出数字图像。

光子到电子的转换效率用量子效率（Quantum Efficiency, QE）描述：

$$
QE(\lambda) = \frac{N_e}{N_p}
$$

其中 $N_e$ 为收集到的电子数，$N_p$ 为入射光子数。Mira220 在 550 nm 可见光下 QE 约为 94 %，在 850 nm 近红外下约为 54 %，在 940 nm 下约为 36 %。

图像传感器的空间分辨率由像素尺寸与像素数决定：

$$
R_{\text{spatial}} = \frac{1}{p}
$$

$Mira220 像素尺寸 $p = 2.79\ \mu\text{m}$，分辨率为 1600 × 1400。

帧率 $f$ 与行读出时间、数据带宽的关系可近似表示为：

$$
f = \frac{B_{\text{data}}}{H \cdot W \cdot b}
$$

其中 $B_{\text{data}}$ 为数据接口带宽，$H \times W$ 为分辨率，$b$ 为每像素位数。Mira220 在 10-bit 输出、全分辨率下最高可达 90 fps。

## 关键参数表

| 参数 | ams OSRAM Mira220（代表值） |
|------|---------------------------|
| 传感器类型 | CMOS 全局快门图像传感器 |
| 有效像素 | 1600 × 1400（2.2 MP） |
| 光学尺寸 | 1/2.7" |
| 像素尺寸 | 2.79 µm × 2.79 µm |
| 输出接口 | MIPI CSI-2（4 通道） |
| 位深 | 8 / 10 / 12 bit |
| 最大帧率 | 90 fps（全分辨率，10-bit） |
| QE @ 550 nm | 94 % |
| QE @ 850 nm | 54 % |
| QE @ 940 nm | 36 % |
| 封装尺寸 | 5.4 mm × 5.4 mm × 0.74 mm（CSP） |
| 工作温度 | -30 °C ~ 85 °C |
| 近红外增强 | 是，适用于低光与 3D 感知 |
| 典型应用 | 人脸识别、手势识别、机器人视觉、AR/VR |

## 应用场景

- 机器人视觉导航与目标识别；
- 人脸识别与生物特征认证；
- 自动驾驶与 ADAS 摄像头；
- 工业检测与机器视觉；
- AR/VR 头显与手势追踪；
- 医疗内窥镜与显微镜成像。

## 供应链关系

`ent_component_optical_sensor` 是传感器类别节点，向上依赖晶圆代工、光学镜头、滤光片、封装基板与驱动 IC 等；向下为机器人、汽车、消费电子、安防等整机提供视觉输入。ams OSRAM 是 `ent_company_ams_osram` 节点，其具体产品 `ent_component_ams_osram_mira220_sensor` / `ent_product_ams_osram_mira220` 是该类别的实例节点，广泛应用于 `ent_product_unitree_h1` 等机器人产品的环境感知子系统。

## 来源与验证

- ams OSRAM Mira220 官方 datasheet 提供了像素数、像素尺寸、帧率、QE、接口、封装与工作温度等参数。
- ams OSRAM 官网图像传感器产品页确认 Mira220 为 2.2 MP NIR 增强全局快门传感器。
- 本条目以 Mira220 为代表值说明通用光学传感器参数；不同厂商/型号参数以各自 datasheet 为准。