---
id: ent_component_minebea_micro_bldc
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Minebea 微型无刷直流电机
  en: MinebeaMitsumi Micro BLDC Motor
status: active
sources:
- id: src_minebea_bldc_eu
  type: website
  url: https://www.minebeamitsumi.eu/en/brushless-dc-motor
- id: src_nmbtc_dnq10m
  type: website
  url: https://cdn.nmbtc.com/uploads/2020/12/dnq10m_home_appliances-datasheet.pdf
- id: src_nmbtc_bldc_table
  type: website
  url: https://nmbtc.com/product-category/high-performance-bldc/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# Minebea 微型无刷直流电机

## 概述

MinebeaMitsumi（美蓓亚三美，前身为 NMB）是全球知名的微型电机与精密零部件制造商，其无刷直流电机（Brushless DC Motor, BLDC）产品线覆盖外转子型、内转子型及风扇/泵类定制方案，广泛应用于机器人关节、电动工具、汽车、医疗及工业自动化设备。Minebea 微型 BLDC 电机以电子换向取代机械电刷，具有高效率、低噪声、长寿命与紧凑结构的特点。代表性型号包括外转子型 DNQ10M、DNQ12MF 以及内转子型 BLDC 20/24/36/40/65 系列。

## 工作原理 / 技术架构

无刷直流电机由永磁转子、三相定子绕组、转子位置传感器（霍尔或编码器）及电子换向驱动器组成。三相绕组按 $120^\circ$ 电角度分布，驱动器根据转子位置依次导通各相，形成旋转磁场。电机的电磁转矩 $T$ 与电枢电流 $I$、转矩常数 $k_t$ 满足

$$
T = k_t \cdot I.
$$

反电动势 $E$ 与角速度 $\omega$ 及反电动势常数 $k_e$ 的关系为

$$
E = k_e \cdot \omega.
$$

在稳态运行时，端电压 $V$、电枢电阻 $R$ 与电流 $I$ 的关系可近似写为

$$
V = E + I R = k_e \omega + I R.
$$

Minebea 微型 BLDC 电机常采用外转子结构以获得较高转矩惯量比，并内置驱动电路实现 PWM 调速、正反转与过流/堵转保护。部分型号支持无传感器（sensorless）运行，通过反电动势过零检测完成换向。

## 关键参数表

| 参数 | DNQ10M（外转子） | DNQ12MF（外转子） | BLDC 20-OR（内转子） | BLDC 65（内转子） |
|---|---|---|---|---|
| 电机类型 | 三相外转子 BLDC | 三相外转子 BLDC | 三相内转子 BLDC | 三相内转子 BLDC |
| 额定电压 | $24\,\text{VDC}$ | $24\,\text{VDC}$ | $9\,\text{VDC}$ | $48\,\text{VDC}$ |
| 转速范围 | $300\text{–}3000\,\text{rpm}$ | $600\text{–}3000\,\text{rpm}$ | $3200\,\text{rpm}$（额定） | $3550\,\text{rpm}$（额定） |
| 连续输出功率 | $30\,\text{W}$ | $50\,\text{W}$ | $2.38\,\text{W}$ | $184\,\text{W}$ |
| 转子惯量 | $564\,\text{g}\cdot\text{cm}^2$ | $556\,\text{g}\cdot\text{cm}^2$ | 未公开 | 未公开 |
| 工作温度 | $0\text{–}50^\circ\text{C}$ | $0\text{–}50^\circ\text{C}$ | 未公开 | 未公开 |
| 重量 | 约 $100\,\text{g}$ | 约 $290\,\text{g}$ | 未公开 | 未公开 |
| 驱动方式 | 内置驱动电路 | 内置驱动电路 | 需外部驱动 | 需外部驱动 |
| 控制接口 | VSP/PWM、CW/CCW、FG | VSP/PWM、CW/CCW、FG | — | — |

## 应用场景

Minebea 微型 BLDC 电机在机器人及相关领域的主要应用包括：

- **机器人关节驱动**：小型外转子 BLDC 可直接驱动轻载旋转关节，内转子 BLDC 配合减速器用于中高转速关节。
- **电动工具与灵巧手**：BLDC 39/40 系列因高转速、高功率密度常用于手持工具及机器人手指驱动。
- **泵与风机**：DNQ 系列外转子电机常用于小型水泵、散热风扇及气动系统。
- **汽车执行器**：Minebea BLDC 也应用于座椅调节、HVAC 风门、电动门把手等车载微执行机构。

## 供应链关系

MinebeaMitsumi 位于电机零部件供应链上游，向上游采购硅钢片、永磁体、轴承、绕组铜线及驱动 IC，向下游供应标准电机或定制化驱动模组。在机器人产业链中，其微型 BLDC 电机被电机模组集成商、减速器厂商与机器人本体制造商采购，用于构建关节执行器、灵巧手及各类辅助驱动单元。

## 来源与验证

- MinebeaMitsumi Europe 官网 Brushless DC Motor 页面列出 BLDC 24/36/39/40/65 系列产品定位，并给出 BLDC 65 的 $300\,\text{W}$ 功率、$8000\,\text{rpm}$ 空载转速与 $860\,\text{mNm}$ 扭矩等参数。
- NMBTC 官方 DNQ10M datasheet 确认外转子结构、$24\,\text{VDC}$ 额定电压、$30\,\text{W}$ 功率、$300\text{–}3000\,\text{rpm}$ 转速范围及转子惯量 $564\,\text{g}\cdot\text{cm}^2$。
- NMBTC High Performance BLDC 产品表提供 BLDC 20-OR、BLDC 24、BLDC 36、BLDC 40、BLDC 65 等型号的额定电压、空载转速、额定转速、连续功率与额定效率数据。