---
id: ent_component_delta_ecma
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 台达 ECMA 伺服电机
  en: Delta ECMA Servo Motor
status: active
sources:
- id: src_delta_asda_b3_catalog
  type: website
  url: https://www.deltaww.com/en-US/products/servo-systems-ac-servo-motors-and-drives/
- id: src_delta_acdrives_ecma
  type: website
  url: https://www.deltaacdrives.com/delta-ecma-servo-motors/
- id: src_delta_ecma_c10604rs
  type: website
  url: https://www.deltaacdrives.com/ecma-ca0604rs-04kw-delta-servo-motor/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 台达 ECMA 伺服电机 / Delta ECMA Servo Motor

## 概述

ECMA 系列是台达电子（Delta Electronics）推出的交流永磁同步伺服电机产品线，功率覆盖 0.1 kW 至 7.5 kW，惯量分为低、中、高三种类型，可与台达 ASDA-B2、B3、A2、A3 等伺服驱动器配套使用。ECMA 电机广泛应用于机床、电子制造、包装、半导体设备、机器人关节与自动化产线，具有高响应、高过载能力与多种编码器配置。

## 工作原理 / 技术架构

ECMA 电机为三相 PMSM，转子采用稀土永磁体，定子分布绕组由 ASDA 系列伺服驱动器通过 SVPWM 逆变供电。驱动器接收来自电机后部编码器的位置反馈，实现电流环、速度环、位置环三闭环控制。

电机电磁转矩与电流的关系可近似表示为：

$$
\tau = k_t \, I_q
$$

其中 $k_t$ 为转矩常数（N·m/A），$I_q$ 为交轴电流。额定转速 $n_r$ 下的机械功率为：

$$
P = \tau \, \omega = \tau \cdot \frac{2\pi n_r}{60}
$$

台达 ASDA-B3 驱动器支持 350 % 瞬时过载能力，可在短时高加速场合提供额外转矩裕量。

## 关键参数表

| 参数 | ECMA-CA0604RS（代表值） | ECMA-CA0807SS（代表值） | ECMA-E11315RS（代表值） |
|------|------------------------|------------------------|------------------------|
| 额定功率 | 0.4 kW | 0.75 kW | 1.5 kW |
| 额定扭矩 | 1.27 N·m | 2.39 N·m | 7.16 N·m |
| 最大扭矩 | 3.82 N·m | 7.17 N·m | 21.48 N·m |
| 额定转速 | 3000 rpm | 3000 rpm | 2000 rpm |
| 最高转速 | 5000 rpm | 5000 rpm | 3000 rpm |
| 转矩常数 | 0.53 N·m/A | 0.55 N·m/A | 1.09 N·m/A |
| 转子惯量 | 0.37 kg·cm² | 1.36 kg·cm² | 15.4 kg·cm² |
| 编码器 | 20-bit incremental / 17-bit absolute | 20-bit incremental / 17-bit absolute | 20-bit incremental / 17-bit absolute |
| 防护等级 | IP65（不含轴端/连接器） | IP65 | IP65 |
| 绝缘等级 | Class B / F | Class B / F | Class B / F |
| 配套驱动器 | ASDA-B3 / B2 / A2 | ASDA-B3 / B2 / A2 | ASDA-B3 / B2 / A2 |

## 应用场景

- CNC 机床进给轴与主轴驱动；
- 工业机器人、SCARA、Delta 机器人关节驱动；
- 电子组装、半导体封装与检测设备；
- 包装、印刷、纺织等连续运动控制；
- 协作机器人与 AGV/AMR 轮边驱动。

## 供应链关系

`ent_component_delta_ecma` 由 `ent_company_delta_electronics` 设计与制造，属于伺服系统核心部件。该电机通常与 `ent_component_delta_asda_b3` 伺服驱动器及配套线缆、制动器、减速器组成完整伺服轴；向下供应给机床、工业机器人、电子制造设备等整机平台，亦可在机器人关节模组 `ent_product_humanoid_robot_joint` 中作为执行电机使用。

## 来源与验证

- 台达官方伺服系统产品页与 ASDA-B3 产品型录提供了 ECMA 系列功率范围、编码器规格、过载能力、防护等级等数据。
- Delta AC Drives 的产品页列出了 ECMA-CA0604RS、ECMA-CA0807SS 等型号的额定扭矩、转速、转矩常数、惯量等具体参数。
- 本表为代表性型号参数，不同后缀（如 RS/SS）与配置以台达官方最新 datasheet 为准；未公开项未作推断。