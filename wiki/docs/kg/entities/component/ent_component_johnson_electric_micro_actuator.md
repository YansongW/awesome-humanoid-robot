---
id: ent_component_johnson_electric_micro_actuator
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 德昌电机微型执行器
  en: Johnson Electric Micro Actuator
status: active
sources:
- id: src_johnsonelectric_hvac
  type: website
  url: https://www.johnsonelectric.com/products/actuators-automotive/hvac-actuators
- id: src_johnsonelectric_headlamp
  type: website
  url: https://www.johnsonelectric.com/zh/products/actuators-automotive/headlamp-actuators
- id: src_johnsonelectric_saia_catalog
  type: website
  url: https://www.johnsonelectric.com/pub/media/wysiwyg/je/je_pdf/saia_motor_catalog.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 德昌电机微型执行器

## 概述

德昌电机（Johnson Electric）是全球领先的微型电机与运动子系统供应商，其微型执行器产品线涵盖步进电机式线性执行器、直流电机式执行器以及面向汽车 HVAC、车灯调节、阀门控制等场景的定制执行模组。德昌电机通过收购 Saia-Burgess 等品牌，将步进电机、同步电机与精密传动机构整合为模块化执行器，可提供高分辨率定位、快速动态响应与长寿命运行。其 HVAC 执行器平台（如 EFB、EVD 系列）与车灯执行器平台（如 Static/Dynamic）代表了微型执行器在汽车与工业自动化中的典型应用。

## 工作原理 / 技术架构

德昌电机微型执行器通常由微型电机（步进或直流）、减速齿轮组、螺杆/蜗杆传动机构、位置反馈元件（电位器或霍尔传感器）及电子驱动板组成。以步进电机线性执行器为例，电机每接收一个脉冲旋转一个步距角 $\theta_{\text{step}}$，经减速比 $i$ 与丝杠导程 $p$ 转换为直线位移 $\Delta x$：

$$
\Delta x = \frac{\theta_{\text{step}}}{360^\circ} \cdot \frac{p}{i}.
$$

在微步进模式下，步距角可进一步细分，从而提高定位分辨率。对于汽车 HVAC 执行器，减速齿轮将电机高速低扭矩输出转换为风门所需的低速高扭矩输出，并通过位置传感器闭环控制风门开度。

## 关键参数表

| 参数 | HVAC 执行器（EFB 平台） | 车灯执行器（Static 平台） | Saia 线性步进执行器（代表性） |
|---|---|---|---|
| 电机类型 | 步进或直流电机 | 步进电机 | 步进电机 + 丝杠 |
| 额定电压 | $12\text{–}24\,\text{VDC}$ | $9\text{–}16\,\text{VDC}$ | $10\text{–}48\,\text{VDC}$（依型号） |
| 名义扭矩 | $60\,\text{cNm}$ | — | — |
| 失速扭矩范围 | $40\text{–}100\,\text{cNm}$ | — | — |
| 名义转速 | $14\,\text{rpm}$ | — | — |
| 轴向力 | — | — | $26\text{–}49\,\text{N}$（依绕组与占空比） |
| 直线速度 | — | — | $4.16\text{–}8.33\,\text{mm/s}$ |
| 行程 | — | — | $10\text{–}150\,\text{mm}$（依型号） |
| 工作温度 | $-40^\circ\text{C}$ – $+85^\circ\text{C}$ | $-40^\circ\text{C}$ – $+155^\circ\text{C}$（卤素灯型） | $-15^\circ\text{C}$ – $+60^\circ\text{C}$ |
| 典型寿命 | $10^5$ 周期 | — | $10^6$ 周期以上 |

## 应用场景

德昌电机微型执行器在机器人及相关领域中主要用于非主驱动的高精度微运动控制：

- **汽车电子执行**：车灯水平/随动调节、空调风门控制、进气格栅开闭、阀门驱动等。
- **医疗设备**：呼吸机阀门、注射泵、手术器械中的精密直线定位。
- **小型机器人关节与末端**：用于夹爪开合、摄像头云台俯仰、传感器伸缩等低扭矩微动场景。
- **工业自动化**：小型挡板、分选机构、流量控制阀的电动替代。

## 供应链关系

德昌电机作为运动子系统一级供应商，向上游采购电机绕组、永磁体、齿轮、丝杠、传感器及驱动 IC，向下游汽车 OEM、Tier 1 供应商、医疗设备制造商及工业自动化客户提供定制执行器模组。在机器人产业链中，其微型执行器通常不直接驱动大型机器人关节，而是作为末端执行器、传感器云台、维护舱门等辅助机构的驱动单元，与伺服电机、减速器共同构成完整运动系统。

## 来源与验证

- Johnson Electric HVAC Actuators 页面列出 EFB、EVD、Gen III、Altas、APACHE 等平台的扭矩、电流、转速、噪声与工作温度范围。
- Johnson Electric Headlamp Actuators 页面说明步进电机式执行器用于大灯调平与随动，工作温度可达 $-40^\circ\text{C}$ 至 $+155^\circ\text{C}$。
- Johnson Electric Saia Motors Catalog 提供同步电机、步进电机、线性执行器的技术数据，包括轴向力、速度、行程与电气参数。