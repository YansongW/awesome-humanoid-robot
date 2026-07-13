---
id: ent_component_casbot_integrated_joint
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 灵宝 CASBOT 一体化关节
  en: CASBOT Integrated Joint
status: active
sources:
- id: src_ent_component_casbot_integrated_joint_1
  type: website
  url: https://www.originofbots.com/robot/casbot-01-by-casbot-details-specifications-rating
- id: src_ent_component_casbot_integrated_joint_2
  type: website
  url: https://humanoid.press/database/humanoid-press-database-casbot-1/
- id: src_ent_component_casbot_integrated_joint_3
  type: website
  url: https://www.robotseuropa.com/eu-lv/Casbot.htm
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 灵宝 CASBOT 一体化关节

## 概述

灵宝 CASBOT 一体化关节是北京中科慧灵机器人技术有限公司（CASBOT）为其全尺寸通用人形机器人 CASBOT 01 自研的高集成度驱动单元。该关节将无框力矩电机、减速器（行星/谐波/直线型）、制动器、双编码器及力控单元集成于一体，构成“电机—减速—传感—控制”同轴模块，用于实现机器人四肢与躯干的高动态运动与精细力控操作。

## 工作原理 / 技术架构

一体化关节的核心是“高扭矩密度电机 + 高精度减速器 + 闭环力控”。电机输出转速 $\omega_m$ 经减速器后降低为关节输出转速 $\omega_j$，减速比 $i$ 定义为

$$
i = \frac{\omega_m}{\omega_j} = \frac{\tau_j}{\tau_m \cdot \eta}
$$

其中 $\tau_j$ 为关节输出扭矩，$\tau_m$ 为电机扭矩，$\eta$ 为传动效率。对于谐波减速器，$\eta$ 通常为 0.70–0.90；行星减速器略高，可达 0.90–0.97。

CASBOT 官方宣称 CASBOT 01 的关节峰值扭矩密度达到

$$
\rho_t = \frac{\tau_{peak}}{m_{joint}} = 207\ \mathrm{N\cdot m/kg}
$$

该指标为系统级峰值数据，代表单位质量关节可输出的峰值扭矩。关节控制采用 2 kHz 实时力控环，结合惯量匹配与振动抑制算法，以支撑奔跑、跳跃与精细装配等任务。

关节输出机械功率 $P_j$ 与电机功率 $P_m$ 满足

$$
P_j = \tau_j \cdot \omega_j = \eta \cdot P_m
$$

在低速大扭矩场景（如蹲起、搬运），高减速比可将电机高速小扭矩转换为关节低速大扭矩；在高速摆动场景，则需权衡减速比与关节最大转速。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 峰值关节扭矩密度 | 207 N·m/kg | CASBOT 公开资料（系统级峰值） |
| 整机自由度 | 52 DOF | CASBOT 01 |
| 单只灵巧手自由度 | 13 DOF | 含五指主动/被动关节 |
| 实时力控频率 | 2 kHz | Robots Europa / CASBOT 报道 |
| 减速形式 | 行星 / 谐波 / 直线一体化 | CASBOT 官网 |
| 整机算力 | 550 TOPS | CASBOT 01 感知与运动计算平台 |
| 续航 | >4 h（双电池，支持 30 min 快充） | IT之家 / 雷峰网 |
| 单关节质量/减速比 | 未公开 | 厂商未披露逐项参数 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **人形机器人全身运动**：CASBOT 01 的髋、膝、踝、肩、肘、腕关节均采用一体化关节，实现行走、奔跑、跳跃与抗干扰平衡。
- **精细操作**：结合 13 DOF 五指灵巧手与 1 N 级指尖力控，完成拧螺丝、换灯泡、叠衣服等任务。
- **工业制造与应急救援**：在航天航海、井下作业、智能制造产线中提供高负载、高响应的关节驱动。

## 供应链关系

该零部件实体位于 CASBOT 产品供应链中游。上游包括磁钢（电工钢）、铜线绕组、稀土磁材、减速器柔轮/刚轮、轴承、编码器及功率半导体；下游直接集成于 `ent_product_casbot_01`，并由 `ent_company_casbot` 设计制造。关键关系为：

- `ent_company_casbot` -- `manufactures` --> `ent_product_casbot_01`
- `ent_product_casbot_01` -- `uses` --> `ent_component_casbot_integrated_joint`

## 来源与验证

- CASBOT 01 整机参数（52 DOF、550 TOPS、207 N·m/kg 关节扭矩密度、>4 h 续航）来自 Origin of Bots、Humanoid.Press 与 Robots Europa 对官方公开资料的汇总。
- 一体化关节的“行星/谐波/直线一体化”与 2 kHz 力控描述来自 CASBOT 官方公开报道。
- 单关节质量、减速比、峰值扭矩等分项参数厂商未公开，已标注为“未公开”。