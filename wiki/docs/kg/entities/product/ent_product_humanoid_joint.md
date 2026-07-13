---
id: ent_product_humanoid_joint
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 人形机器人关节模组
  en: Humanoid Robot Joint Actuator Module
status: active
sources:
- id: src_ent_product_humanoid_joint_1
  type: website
  url: https://www.makongear.com/integrated-joint-actuator-for-humanoid-robots/
- id: src_ent_product_humanoid_joint_2
  type: website
  url: https://robotics.zhinno.com/blog/humanoid-robot-actuator-torque-density.html
- id: src_ent_product_humanoid_joint_3
  type: website
  url: https://www.makongear.com/product/humanoid-joint-actuator/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 人形机器人关节模组 / Humanoid Robot Joint Actuator Module

## 概述

人形机器人关节模组是集成无框力矩电机、减速器（谐波或行星）、双编码器、力矩传感器、制动器与伺服驱动器的一体化旋转执行器，为人形机器人提供运动、力控与承载能力。一个典型的人形机器人需要 25–30 个关节模组，分布于髋、膝、踝、肩、肘、腕等关键部位。关节模组的性能直接决定人形机器人的负载能力、动态响应、能耗与整机成本，因此扭矩密度（Nm/kg）、背隙、控制带宽与可靠性是其核心评价指标。

## 工作原理 / 技术架构

关节模组本质上是一个机电一体化系统，其输出扭矩由电机电磁转矩经减速器放大后得到：

$$
T_{\text{out}} = \eta \, i \, T_{\text{motor}}
$$

其中 $i$ 为减速比，$\eta$ 为传动效率。衡量其轻量化水平的核心指标为扭矩密度：

$$
\rho_T = \frac{T_{\text{peak}}}{m_{\text{total}}}
$$

$T_{\text{peak}}$ 为峰值输出扭矩，$m_{\text{total}}$ 为包含电机、减速器、编码器、驱动器与结构件的总质量。当前行业对人形机器人髋/膝关节的峰值扭矩密度通常要求高于 30 Nm/kg，肩/肘关节高于 25 Nm/kg，腕/踝关节高于 20 Nm/kg；部分高端谐波关节产品峰值扭矩密度可达 100 Nm/kg 以上。

电机输出功率 $P$ 与转速 $\omega$、扭矩 $T$ 的关系为 $P = T \omega$。高扭矩密度要求电机具备高极对数、高槽满率及高效散热设计，同时减速器需在紧凑体积内提供大减速比。

## 关键参数表

| 参数项 | 典型值/范围（以市场主流一体化关节为例） | 备注/来源 |
|--------|----------------------------------------|-----------|
| 结构形式 | 电机 + 减速器 + 双编码器 + 驱动器 + 制动器 | 行业通用 |
| 外径 | 30 – 110 mm | Makon 产品目录 |
| 重量 | 0.23 – 6.87 kg | Makon 产品目录 |
| 减速比 | 51:1 – 161:1 | Makon 产品目录 |
| 额定扭矩 | 1.8 – 363 Nm | Makon 产品目录 |
| 峰值扭矩 | 3.3 – 800 Nm | Makon 产品目录 |
| 峰值扭矩密度 | 30 – 116 Nm/kg（视型号） | 行业 benchmark / Makon |
| 中空孔径 | 6 – 40 mm | Makon 产品目录 |
| 通信总线 | EtherCAT / CAN | Makon 产品目录 |
| 编码器 | 双绝对值编码器（输入/输出端） | 行业通用 |
| 峰值扭矩密度行业要求 | 髋/膝 > 30 Nm/kg；肩/肘 > 25 Nm/kg；腕/踝 > 20 Nm/kg | 行业 benchmark |
| 价格 | 未公开 | 因型号与批量差异大 |

## 应用场景

- **人形机器人**：髋、膝、踝、肩、肘、腕等全身关节，实现行走、奔跑、跳跃、抓取等复杂动作。
- **协作机器人**：轻量化、高力控精度的关节模组，支持安全人机协作。
- **外骨骼与康复机器人**：为穿戴式设备提供助力与运动辅助。
- **工业机械臂**：高扭矩密度关节可提升负载比与作业节拍。

## 供应链关系

- **核心子部件/上游**：无框力矩电机、谐波减速器（如 `ent_component_shimpo_flexwave_harmonic`）、行星减速器、光电/磁编码器（如 `ent_component_aurora_jft`）、六维力/力矩传感器（如 `ent_component_keli_sbe` 相关产品线）、伺服驱动器（如 `ent_component_googoltech_gshd`）、轴承、结构件。
- **下游客户/应用场景**：人形机器人整机厂、协作机器人厂商、外骨骼与康复设备商、高端数控机床制造商。
- **竞争/对标**：Makon、Harmonic Drive Systems、Nidec-Shimpo、绿的谐波、中大力德、汇川技术、禾川科技。
- **知识图谱关系**：`ent_product_humanoid_joint` 由多家零部件组合而成，典型关系包括 `uses` → `ent_component_shimpo_flexwave_harmonic`、`uses` → `ent_component_googoltech_gshd`、`uses` → `ent_component_aurora_jft`。

## 来源与验证

1. [Makon：Integrated Joint Actuator for Humanoid Robots](https://www.makongear.com/integrated-joint-actuator-for-humanoid-robots/)
2. [Zhinno：Humanoid Robot Actuator Torque Density Benchmarks](https://robotics.zhinno.com/blog/humanoid-robot-actuator-torque-density.html)
3. [Makon Humanoid Joint Actuator Product Catalog](https://www.makongear.com/product/humanoid-joint-actuator/)

注：本实体为人形机器人关节模组的通用产品类别，表中参数为市场代表性产品范围，具体型号参数应以制造商 datasheet 为准。