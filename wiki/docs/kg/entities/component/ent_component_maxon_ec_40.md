---
id: ent_component_maxon_ec_40
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: Maxon EC 40 无刷直流电机
  en: Maxon EC 40 Brushless DC Motor
status: active
sources:
- id: src_maxon_ec40_traceparts
  type: website
- title: Maxon EC 40 Ø40 mm, brushless, 120 Watt, with Hall sensors - TraceParts
  url: https://www.traceparts.com/en/product/maxon-motor-ag-ec-40-o40-mm-brushless-120-watt-with-hall-sensors
- id: src_maxon_ec40_product_page
  type: website
- title: Maxon EC-i 40 Ø40 mm, brushless, 100 Watt, with Hall sensors
  url: https://www.maxongroup.com/maxon/view/product/488607
- id: src_maxon_ec40_news
  type: website
- title: maxon's EC 40, a 40 mm brushless motor with a formula for high power density
  url: https://www.automate.org/robotics/news/maxons-ec-40-a-40mm-brushless-motor-with-a-formula-for-high-power-density
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications compiled from Maxon product page, TraceParts CAD data
    and industry news; EC 40 has multiple winding variants and values should be verified
    against specific part number.
---


# Maxon EC 40 无刷直流电机 / Maxon EC 40 Brushless DC Motor

## 概述

Maxon EC 40 是瑞士 Maxon Motor 推出的 Ø40 mm 无刷直流电机系列，以高转速、高效率与长寿命著称。该系列包括不同绕组与功率等级（如 100 W、120 W），标配霍尔传感器用于电子换向，并可搭配编码器、齿轮箱与制动器组成完整驱动系统。EC 40 广泛应用于医疗手持工具、光学平台、小型无人机与机器人末端执行器。

## 工作原理 / 技术架构

EC 40 采用电子换向无刷直流电机结构：定子为多槽绕组，转子为表面贴装式稀土永磁体；霍尔传感器检测转子位置，外部伺服放大器按 120° 或 60° 换向逻辑驱动三相绕组。由于取消了机械电刷，电机具有低磨损、低电磁噪声与高转速能力。

电机端电压与反电动势、电流的关系可表示为：

\[
U = R \cdot I + k_e \cdot \omega
\]

其中 \(U\) 为端电压（V），\(R\) 为相电阻（Ω），\(I\) 为电流（A），\(k_e\) 为反电动势常数（V/(rad/s)），\(\omega\) 为机械角速度（rad/s）。输出转矩与电流的关系为：

\[
T = k_t \cdot I
\]

其中 \(k_t\) 为转矩常数（N·m/A）。对于 EC 40（件号 118896），\(k_t = 38.2\ \text{mN·m/A}\)。

机械时间常数 \(\tau_m\) 反映电机从静止加速到 63% 空载转速所需时间：

\[
\tau_m = \frac{J \cdot R}{k_t \cdot k_e}
\]

其中 \(J\) 为转子惯量。EC 40 118896 的 \(\tau_m = 7.3\ \text{ms}\)。

## 关键参数

| 参数项 | 数值（EC 40, P/N 118896） | 备注/来源 |
|--------|---------------------------|-----------|
| 标称电压 | 42 V | TraceParts |
| 额定功率 | 120 W | TraceParts |
| 空载转速 | 10,400 rpm | TraceParts |
| 空载电流 | 258 mA | TraceParts |
| 额定转速 | 9,280 rpm | TraceParts |
| 额定转矩（最大连续转矩） | 124 mN·m | TraceParts |
| 额定电流 | 3.44 A | TraceParts |
| 堵转转矩 | 1,280 mN·m | TraceParts |
| 堵转电流 | 33.5 A | TraceParts |
| 最大效率 | 84% | TraceParts |
| 端子电阻（相间） | 1.25 Ω | TraceParts |
| 端子电感（相间） | 0.319 mH | TraceParts |
| 转矩常数 | 38.2 mN·m/A | TraceParts |
| 速度常数 | 250 rpm/V | TraceParts |
| 转速/转矩梯度 | 8.2 rpm/mN·m | TraceParts |
| 机械时间常数 | 7.3 ms | TraceParts |
| 转子惯量 | 85 g·cm² | TraceParts |
| 最大转速 | 18,000 rpm | TraceParts |
| 工作温度 | −20 °C – +125 °C | TraceParts |
| 重量 | 390 g | TraceParts |
| 极对数 | 1 | TraceParts |
| 轴承类型 | 滚珠轴承 | TraceParts |

## 应用场景

- **机器人末端执行器**：高转速、小体积特性适合夹爪、螺丝刀等末端工具。
- **医疗手持设备**：无刷、低噪音、长寿命特性适用于手术工具、牙科设备。
- **光学平台与小型无人机**：高速响应与轻量化结构适合精密定位与旋翼驱动。

## 供应链关系

EC 40 由 **Maxon Motor / maxon Group（实体 `ent_company_maxon`）** 设计制造。上游依赖稀土永磁体（钕铁硼）、铜线、硅钢片、轴承与铝外壳；下游客户包括医疗器械、航空航天、协作机器人与人形机器人 OEM。在知识图谱中，该实体通过 `manufactures` 关系与公司节点 `ent_company_maxon` 相连，可与 Maxon 编码器、行星齿轮箱及 ESCON/EPOS 控制器组成模块化驱动系统。

## 来源与验证

- Maxon EC 40 TraceParts CAD/参数页（https://www.traceparts.com/en/product/maxon-motor-ag-ec-40-o40-mm-brushless-120-watt-with-hall-sensors）
- Maxon EC-i 40 官方产品页（https://www.maxongroup.com/maxon/view/product/488607）
- A3 Automate 新闻报道（https://www.automate.org/robotics/news/maxons-ec-40-a-40mm-brushless-motor-with-a-formula-for-high-power-density）

EC 40 系列存在多种绕组变体，上表以件号 118896 为代表；实际选型应以具体件号 datasheet 为准。