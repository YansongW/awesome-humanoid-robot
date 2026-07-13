---
id: ent_component_moons_stepper_drive
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 鸣志步进电机驱动器（SR/STF 系列）
  en: MOONS' Stepper Drive (SR / STF Series)
status: active
sources:
- id: src_moons_stepper_official
  type: website
- title: MOONS' Stepper Drives Official Page
  url: https://www.moons.com.cn/c/stepper-drives-cn0501
- id: src_moons_sr_datasheet
  type: pdf
- title: MOONS' SR Series Two Phase Stepper Drive Datasheet
  url: https://www.motiontech.com.au/wp-content/uploads/2023/07/MT-MOONS-SR-Series-Two-Phase-100723.pdf
- id: src_moons_drivers_pdf
  type: pdf
- title: MOONS' Stepper Drive Catalog
  url: http://www.soulutions.co.il/wp-content/uploads/2015/12/Drivers-Moons.pdf
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets and website; missing values
    marked as 未公开.
---


# 鸣志步进电机驱动器（SR/STF 系列） / MOONS' Stepper Drive (SR / STF Series)

## 概述

鸣志电器（MOONS' Electric）步进电机驱动器是面向两相/三相步进电机的数字式驱动单元，典型系列包括 SR（脉冲型直流输入）与 STF（总线控制型）。产品采用 DSP 数字控制与先进电流斩波技术，具备微步细分、反共振、转矩纹波抑制与多种工业总线接口，广泛用于 3C 自动化、半导体设备、医疗仪器及小型机器人关节。

## 工作原理 / 技术架构

步进电机驱动器通过双 H 桥功率放大器对电机两相绕组施加按顺序换向的电流。采用 PWM 电流斩波（典型 16 kHz）维持绕组电流恒定，并通过微步细分将整步角进一步划分，提高运动平稳性。

对于两相混合式步进电机，整步角通常为 $1.8°$（200 步/转）。微步细分后单步角为

$$
\theta_s = \frac{1.8°}{N}
$$

其中 $N$ 为细分数。官方资料指出微步分辨率可在 200 至 51200 步/转之间以 2 步/转为增量软件选择，对应最大细分数 256。

电磁转矩近似与相电流成正比：

$$
T \approx K_t \cdot I
$$

其中 $K_t$ 为转矩常数，$I$ 为绕组电流。驱动器通过空闲电流自动降低、转矩纹波补偿与反共振算法，改善中低速振动与噪音。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 放大器类型 | 双 H 桥，四象限 | MOONS' 驱动器手册 |
| 电流控制 | 4 态 PWM，16 kHz | MOONS' 驱动器手册 |
| 输入电压（DC 系列） | 12–80 VDC | SR/STF 系列产品页 |
| 输入电压（AC 系列） | 80–265 VAC | SRAC 系列产品页 |
| 输出电流 | 0.1–10 A（依系列） | MOONS' 驱动器手册 |
| 微步分辨率 | 200–51200 步/转 | MOONS' 驱动器手册 |
| 最大细分数 | 256 | SR 系列手册 |
| 控制方式 | 脉冲/方向、CW/CCW、CANopen、Modbus/RTU、EtherNet/IP、EtherCAT | MOONS' 官网 |
| 反共振 | 自动计算系统固有频率并施加阻尼 | MOONS' 驱动器手册 |
| 保护功能 | 过压、欠压、过流、过热、电机开路/短路 | MOONS' 驱动器手册 |
| 工作温度 | 0–40 °C（需合适散热） | MOONS' 驱动器手册 |
| 重量 | 0.12–0.8 kg（依型号） | MOONS' 驱动器手册 |
| 具体型号尺寸 | 未公开（系列内各异） | - |

## 应用场景

- **3C 与半导体设备**：精密定位、贴片、点胶、检测平台。
- **医疗仪器**：样品处理、精密移液、影像设备定位。
- **小型机器人关节**：低成本、中低动态机器人关节与执行器。
- **自动化产线**：输送、分拣、装配等开环/半闭环定位任务。

## 供应链关系

- **上游**：稀土永磁体、硅钢片、铜线、轴承、功率 MOSFET、驱动 IC、控制 DSP。
- **制造商**：`ent_company_moons` -- `manufactures` --> `ent_component_moons_stepper_drive`。
- **下游客户**：工业机器人、人形机器人、医疗设备、半导体设备、3C 自动化厂商。
- **竞争对手/对标**：Maxon、Faulhaber、汇川技术、步科股份、禾川科技。

## 来源与验证

1. 鸣志电器官网步进驱动器页：https://www.moons.com.cn/c/stepper-drives-cn0501
2. MOONS' SR Series Two Phase Stepper Drive Datasheet（MotionTech）
3. MOONS' Stepper Drive Catalog（Drivers-Moons.pdf）
4. 鸣志电器年报与 WAIC 2026 参展报道