---
id: ent_component_hao_zhi_harmonic_drive
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 昊志机电谐波减速器
  en: Hao Zhi Harmonic Drive
sources:
- id: src_hao_zhi_official
  type: website
- title: 昊志机电官网
  url: http://www.haozhi.cn
- id: src_hao_zhi_reducer_series
  type: website
- title: 昊志机电谐波减速器产品系列
  url: https://www.haozhihs.com/show.php?id=392
- id: src_hao_zhi_hat_type
  type: website
- title: 昊志机电礼帽型谐波减速器产品页
  url: https://www.haozhihs.com/show_list.php?id=73
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from Hao Zhi official product pages and company Wiki;
    exact model-level values depend on specific size and ratio configuration.
---


# 昊志机电谐波减速器 / Hao Zhi Harmonic Drive

## 概述

昊志机电谐波减速器（Hao Zhi Harmonic Drive）是广州市昊志机电股份有限公司开发的精密谐波传动部件，产品覆盖 G 系列、H 系列等多个型号，规格涵盖外径 32–100 mm，减速比 50–160:1。该产品基于自主齿形设计，具有高扭转刚度、低背隙、结构紧凑等特点，主要应用于协作机器人、人形机器人手臂/腿部、半导体转台与医疗机器人。

## 工作原理 / 技术架构

昊志谐波减速器遵循谐波齿轮传动的基本物理机制：

1. **波发生器**：由椭圆凸轮与柔性轴承组成，驱动柔轮产生周期性弹性变形。
2. **柔轮**：薄壁杯形或礼帽形齿轮，外齿与刚轮内齿啮合；随波发生器旋转，柔轮齿依次啮入/啮出刚轮齿，实现减速。
3. **刚轮**：刚性内齿圈，固定于壳体或作为另一输出端。
4. **交叉滚子轴承**：集成输出轴承支撑外部径向、轴向与倾覆载荷。

减速比 $i$ 与刚轮齿数 $z_c$、柔轮齿数 $z_f$ 的关系为

$$
i = \frac{z_c}{z_c - z_f}
$$

对于常见双波传动，齿数差为 2。输出扭矩 $\tau_{out}$ 与输入扭矩 $\tau_{in}$、传动效率 $\eta$ 的关系为

$$
\tau_{out} = \eta \, i \, \tau_{in}
$$

昊志通过优化齿形与材料热处理工艺，使减速器在保持低背隙（≤ 1 arc-min）的同时提高扭转刚度与承载能力。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | 昊志机电 / Hao Zhi Electromechanical | 公司官网 |
| 产品系列 | G 系列、H 系列 | 产品手册 |
| 外径范围 | 32–100 mm | 产品手册 |
| 重量范围 | 0.1–1.5 kg | 产品手册 |
| 减速比 | 50–160:1 | 产品手册 |
| 额定扭矩 | 3.9–112 N·m（系列范围） | 产品手册 |
| 背隙 | ≤ 1 arc-min | 产品手册 |
| 最高输入转速 | 6,500 rpm | 产品手册 |
| 安装方式 | 杯型 / 帽型 | 产品手册 |
| 结构特点 | 自主齿形设计、高扭转刚度 | 产品手册 |
| 适用润滑 | 专用谐波润滑脂 | 行业惯例 |
| 价格 | 未公开 | 需询价 |

注：昊志官网公开的是系列参数范围，未提供单一型号（如 G-32-100）的完整参数表。具体型号的额定扭矩、重量、背隙需以官方选型手册或样册为准。

## 应用场景

- **人形机器人手臂与腿部关节**：为肩、肘、腕、髋、膝、踝等关节提供高减速比、低背隙的扭矩输出。
- **协作机器人**：满足协作机器人对安全性、精度与紧凑性的综合要求。
- **半导体转台**：用于晶圆传输、检测设备的精密旋转定位。
- **医疗机器人**：为手术机械臂与康复机器人提供平稳、精确的关节运动。
- **数控机床与自动化设备**：作为精密传动部件，替代传统行星减速器。

## 供应链关系

昊志机电（`ent_company_hao_zhi`）是国内高端电主轴龙头，逐步拓展至直线电机、力矩电机、谐波减速器与机器人关节模组。谐波减速器（`ent_component_hao_zhi_harmonic_drive`）与力矩电机（`ent_component_hao_zhi_torque_motor`）共同构成公司面向人形机器人的核心传动产品线。上游原材料包括稀土永磁体（力矩电机）、轴承、合金钢（柔轮/刚轮）、铜线、绝缘材料；下游客户包括数控机床厂商、机器人整机厂、半导体设备与人形机器人 OEM。昊志与 Harmonic Drive、绿的谐波、来福谐波、大族传动、新宝等形成竞争。

## 来源与验证

- 昊志机电官网确认其为 A 股上市公司（SZ.300503），主营电主轴、力矩电机、谐波减速器等产品。
- 昊志谐波减速器产品系列页公开了外径、减速比、额定扭矩范围、背隙与最高输入转速等参数。
- 礼帽型谐波减速器产品页补充了规格 14/17/20/25/32、减速比 50/80/100/120 等配置信息。