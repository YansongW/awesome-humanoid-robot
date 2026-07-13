---
id: ent_component_benmo_m1502d
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 本末 M1502D 直驱关节
  en: Benmo M1502D Direct-Drive Joint
status: active
sources:
- id: src_benmo_m1502d_diablo
  type: website
- title: 本末科技刑天产品页
  url: https://directdrive.com/product_diablo
- id: src_benmo_company_profile
  type: pdf
- title: 本末科技公司介绍 PDF
  url: https://www.worldrobotconference.com/profile/robot/download/2025/07/10/250110%20%E6%9C%AC%E6%9C%AB%E7%A7%91%E6%8A%80%E4%BB%8B%E7%BB%8D_20250710110734A073.pdf
- id: src_benmo_official
  type: website
- title: 本末科技官网
  url: https://directdrive.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official public materials; missing values marked
    as 未公开.
---


# 本末 M1502D 直驱关节 / Benmo M1502D Direct-Drive Joint

## 概述

本末 M1502D 直驱关节是东莞本末科技（Benmo Technology / Direct Drive Technology）开发的一体化机器人关节模组，采用外转子永磁同步电机（PMSM）直接驱动方案，取消传统减速器，以“感驱控一体”结构实现低噪声、高动态响应的旋转运动输出。该关节主要搭载于本末科技轮足机器人“刑天（Diablo）”，构成其下肢与躯干动力单元。

## 工作原理 / 技术架构

M1502D 基于无减速器直驱架构：外转子永磁同步电机产生电磁转矩，转子与输出轴刚性连接，电机输出转矩直接传递至负载。控制器采用磁场定向控制（FOC），配合内置高精度编码器实现电流、速度与位置闭环。

电磁转矩方程为

$$
T_e = \frac{3}{2} p \left[ \psi_f i_q + (L_d - L_q) i_d i_q \right]
$$

其中 $p$ 为极对数，$\psi_f$ 为永磁体磁链，$i_d$、$i_q$ 为同步旋转坐标系下的直轴与交轴电流，$L_d$、$L_q$ 为直轴与交轴电感。由于无减速器，关节输出转矩等于电机电磁转矩（扣除轴承摩擦与风阻损耗），输出转速等于电机转速，机械传动关系为

$$
T_{\text{joint}} = T_e - T_{\text{loss}}, \qquad \omega_{\text{joint}} = \omega_e
$$

编码器分辨率决定位置反馈精度；官方资料披露 M1502D 采用 16 位编码器，单圈分辨率为 $2^{16}=65536$ 计数。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 一体化直驱旋转关节 | 本末科技公司介绍 PDF |
| 单个关节峰值扭矩 | 17 N·m | 本末科技刑天产品页 |
| 编码器分辨率 | 16 bit | 本末科技刑天产品页 |
| 传动方式 | 无减速器直驱 | 本末科技公司介绍 PDF |
| 电机类型 | 外转子永磁同步电机 | 本末科技公司介绍 PDF |
| 控制方式 | FOC 矢量控制 + 内置驱动器 | 本末科技公司介绍 PDF |
| 噪声水平 | 接近环境噪声（≈0 dB 额外噪音） | 本末科技刑天产品页 |
| 额定扭矩 | 未公开 | - |
| 额定转速 | 未公开 | - |
| 关节重量 | 未公开 | - |
| 工作电压 | 未公开 | - |
| 防护等级 | 未公开 | - |

## 应用场景

- **轮足机器人关节**：作为本末“刑天”轮足机器人的 6 个直驱关节，实现站立、匍匐、跳跃、越障与自平衡。
- **服务/商用机器人动力模组**：适用于对噪声敏感、空间受限的轮式机器人驱动轮与关节。
- **健身与工业直驱模组**：同系列直驱技术亦延伸至智能动力模组与 AGV/AMR 驱动轮。

## 供应链关系

在本末科技的产品网络中，M1502D 处于核心零部件层：

- **上游**：稀土永磁体、硅钢片、轴承、驱动 IC、编码器、控制器由本末自研或外购。
- **同公司关系**：`ent_company_benmo` -- `manufactures` --> `ent_component_benmo_m1502d`。
- **下游整机**：`ent_product_benmo_tita` 与“刑天”轮足机器人均使用 M1502D 系列直驱关节，构成 `ent_product_benmo_tita` -- `uses` --> `ent_component_benmo_m1502d`。
- **客户**：扫地/服务机器人厂商、AGV/AMR 集成商、健身设备商、科研教育机构。

## 来源与验证

1. 本末科技官网：https://directdrive.com
2. 本末科技刑天产品页：https://directdrive.com/product_diablo
3. 本末科技公司介绍 PDF（世界机器人大会资料）

> 注：额定扭矩、额定转速、重量与电压等型号级参数在官方公开资料中未披露，已标注为“未公开”。