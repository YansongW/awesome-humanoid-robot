---
id: ent_component_weiguang_ec_fan
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 微光股份 EC 外转子风机
  en: Weiguang EC External Rotor Fan
status: active
sources:
- id: src_ent_component_weiguang_ec_fan_1
  type: website
  url: https://eurocool.co.za/wp-content/uploads/2020/07/20171026-%E5%A4%96%E8%BD%AC%E5%AD%90%E8%BD%B4%E6%B5%81%E9%A3%8E%E6%9C%BAAxial-Fans-1.pdf
- id: src_ent_component_weiguang_ec_fan_2
  type: website
  url: https://static.insales-cdn.com/files/1/2915/36399971/original/EC092-25E3G01-B280-50S1-01.pdf
- id: src_ent_component_weiguang_ec_fan_3
  type: website
  url: https://www.weiguang.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 微光股份 EC 外转子风机

## 概述

微光股份（Hangzhou Weiguang Electronic）EC 外转子风机是将电子换向（Electronically Commutated, EC）无刷直流电机与外转子叶轮集成的离心/轴流通风设备。相比传统交流异步风机，EC 风机具有调速范围宽、效率高、噪音低、可智能控制等优势，广泛用于冷链物流、数据中心、新能源储能及机器人整机热管理。

## 工作原理 / 技术架构

EC 风机采用永磁转子与定子绕组，通过内置控制器实现电子换向。其气动性能由风量 $Q$、静压 $\Delta p$ 与输入功率 $P_{in}$ 描述。风机有效气动功率为

$$
P_{air} = \frac{Q \cdot \Delta p}{\eta_{fan}}
$$

其中 $\eta_{fan}$ 为风机效率。风机的相似定律表明：当转速 $N$ 变化时，风量与转速成正比，静压与转速平方成正比，轴功率与转速立方成正比：

$$
\frac{Q_1}{Q_2} = \frac{N_1}{N_2},\quad
\frac{\Delta p_1}{\Delta p_2} = \left(\frac{N_1}{N_2}\right)^2,\quad
\frac{P_1}{P_2} = \left(\frac{N_1}{N_2}\right)^3
$$

EC 控制器支持 0–10 V 模拟量或 PWM 调速，可根据温度反馈实时调整转速，从而在保证散热的前提下降低能耗与噪声。热阻视角下，风机提供的对流换热能力可表示为

$$
R_{th,conv} = \frac{1}{h A}
$$

其中 $h$ 为对流换热系数，$A$ 为散热面积；提高风量可增强 $h$，降低热阻。

## 关键参数表

| 参数项 | 典型值 | 备注/来源 |
|--------|--------|-----------|
| 叶轮直径 | 154–400 mm（系列范围） | 微光股份产品手册 |
| 风量 | 200–4,500 m³/h | 产品手册 |
| 静压 | 30–1,200 Pa | 产品手册 |
| 额定功率 | 20–600 W | 产品手册 |
| 供电电压 | 24–380 VAC/VDC | 产品手册 |
| 噪音水平 | ≤68 dB(A) | 产品手册 |
| 调速接口 | 0–10 V / PWM | 产品手册 |
| 绝缘等级 | F 级（示例 EC092） | EC092 规格书 |
| 寿命 | 20,000 h（L10，示例 EC092） | EC092 规格书 |
| 防护等级 | IP44–IP54 | 产品手册（部分型号） |
| 价格 | 未公开 | 按型号询价 |

## 应用场景

- **机器人整机热管理**：用于控制器、电池包、电机驱动器的风冷散热，维持关节与计算单元在安全工作温度内。
- **数据中心与通信基站**：为服务器机柜、5G 基站提供高效、可调速的强制风冷。
- **新能源储能系统**：电池簇热管理与空调辅助风机。
- **冷链物流设备**：冷柜、展示柜、冷库通风。

## 供应链关系

微光股份 EC 外转子风机由 `ent_company_weiguang` 制造。上游包括硅钢片（磁钢）、铜线、铝材、永磁体、电子元器件（MOSFET、控制芯片）与塑料粒子；下游客户覆盖冷链设备商、数据中心运营商、新能源车企及机器人整机厂。在人形机器人供应链中，EC 风机属于热管理子系统的关键零部件，与电池、控制器、关节驱动器共同构成整机热管理网络。

## 来源与验证

- 系列范围参数（叶轮直径、风量、静压、功率、电压、噪音、调速接口）来自微光股份外转子轴流风机产品手册。
- EC092 具体型号的绝缘等级、寿命、功率等数据来自其规格书 PDF。
- 微光股份官网作为品牌与产品来源引用。