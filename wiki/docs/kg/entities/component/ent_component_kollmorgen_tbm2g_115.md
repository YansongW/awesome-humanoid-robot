---
id: ent_component_kollmorgen_tbm2g_115
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: Kollmorgen TBM2G-115 无框力矩电机
  en: Kollmorgen TBM2G-115 Frameless Torque Motor
sources:
- id: src_kollmorgen_tbm2g_sg
  type: datasheet
- title: TBM2G Frameless Motor Selection Guide
  url: https://www.kollmorgen.com/sites/default/files/TBM2G-KM_SG_00396_RevA_EN.pdf
- id: src_inmoco_tbm2g_2022
  type: article
- title: New frameless servo motors increase performance and reduce size for robot
    control
  url: https://inmoco.co.uk/new-frameless-servo-motors-increase-performance-and-reduce-size-for-robot-control/
- id: src_kollmorgen_official
  type: website
- title: Kollmorgen Official Website
  url: https://www.kollmorgen.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---


# Kollmorgen TBM2G-115 无框力矩电机 / Kollmorgen TBM2G-115 Frameless Torque Motor

## 概述

Kollmorgen TBM2G-115 是 TBM2G 系列中最大外径（115 mm）的无框永磁同步力矩电机，专为协作机器人与人形机器人关节集成设计。电机由分离的转子和定子构成，可直接嵌入谐波/行星减速器与关节壳体之间，形成高扭矩密度的模块化执行单元。其低压设计（≤48 VDC）满足协作机器人安全规范，适合 3–15 kg 级协作机器人肩部、髋部及腰关节等大扭矩负载位置。

## 工作原理 / 技术架构

TBM2G-115 采用外转子、内定子的无框结构：多极永磁体分布于转子环内壁，定子铁芯嵌入绕组并直接作为关节固定部分。三相正弦波驱动下，定子产生的旋转磁场牵引转子永磁体，实现电磁转矩输出。无框设计消除了传统伺服电机的轴承、端盖与外壳，电机与负载同轴集成，显著降低关节惯量与轴向尺寸。

电机关键性能可通过以下关系描述：

- 机械输出功率：
  $$P_m = T \cdot \omega = T \cdot \frac{2\pi n}{60}$$
  其中 $T$ 为额定扭矩（N·m），$n$ 为额定转速（rpm）。

- 电机常数（扭矩密度指标）：
  $$K_m = \frac{T_{stall}}{\sqrt{P_{loss}}}$$
  表征单位热损耗下的输出扭矩，TBM2G-115 26 叠片型号典型值约 0.802 N·m/√W。

- 峰值扭矩与电流近似成正比，受逆变器电流能力与永磁体去磁约束。

可选集成 Hall 传感器提供转子位置信号，便于无感/有感矢量控制；PT1000 或 PTC 热敏电阻用于绕组过温保护。

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 外径 | 115 mm | Kollmorgen 选型手册 |
| 叠片长度 | 8.2 / 12.7 / 26.3 mm（08/13/26） | Kollmorgen 选型手册 |
| 额定电压 | ≤48 VDC | Kollmorgen 公开资料 |
| 堵转连续扭矩（26 叠片） | 6.03 N·m | Kollmorgen 选型手册 |
| 额定转速（26 叠片 @ 48 VDC） | 3100 rpm | Kollmorgen 选型手册 |
| 额定功率（26 叠片） | 约 1.43–1.96 kW | INMOCO 2022 / 选型手册 |
| 电机常数 $K_m$（26 叠片） | 0.802 N·m/√W | Kollmorgen 选型手册 |
| 极对数 | 10（20 极） | 经销商产品页 |
| 反馈 | 可选集成 Hall 传感器 | Kollmorgen 公开资料 |
| 热保护 | PT1000 / 3×PTC | 经销商产品页 |
| 认证 | CE、UKCA、UR | 经销商产品页 |
| 重量（26 叠片） | 约 1.43 kg | 经销商产品页 |

## 应用场景

- **协作机器人**：肩部、髋部、腰部大扭矩关节，支持低电压安全运行。
- **人形机器人**：腰/髋关节直驱或配合谐波/行星减速器构成高动态执行单元。
- **精密转台与医疗设备**：利用无框结构实现紧凑、低齿槽转矩的旋转运动。

## 供应链关系

- **制造商**：Kollmorgen（ent_company_kollmorgen），Regal Rexnord 旗下运动控制品牌。
- **上游关键物料**：稀土永磁体、硅钢片、漆包线、绝缘材料、Hall/温度传感器。
- **下游整机集成**：协作机器人、人形机器人 OEM 及精密转台厂商；常与谐波减速器（如 Leaderdrive、Harmonic Drive）或 RV 减速器配对使用。
- **竞争/对标**：Maxon、汇川技术、禾川科技、Parker。

## 来源与验证

- Kollmorgen TBM2G 选型手册（Rev A）：https://www.kollmorgen.com/sites/default/files/TBM2G-KM_SG_00396_RevA_EN.pdf
- INMOCO 2022 产品报道：https://inmoco.co.uk/new-frameless-servo-motors-increase-performance-and-reduce-size-for-robot-control/
- Kollmorgen 官网：https://www.kollmorgen.com