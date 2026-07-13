---
id: ent_component_step_servo_motor
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 步科（Kinco）伺服电机
  en: Kinco Step Servo Motor
sources:
- id: src_step_servo_motor_catalog
  type: datasheet
- title: Kinco 产品综合型录选型手册
  url: https://www.worldrobotconference.com/profile/robot/download/2025/07/04/Kinco%20%E4%BA%A7%E5%93%81%E7%BB%BC%E5%90%88%E5%9E%8B%E5%BD%95%E9%80%89%E5%9E%8B%E6%89%8B%E5%86%8C_%E4%B8%AD%E6%96%87202503_compressed_20250704093858A741.pdf
- id: src_kinco_official
  type: website
- title: Kinco 步科官网
  url: https://www.kinco.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from Kinco product catalog and official website; missing
    values marked as 未公开.
---


# 步科（Kinco）伺服电机 / Kinco Step Servo Motor

## 概述

步科（Kinco）伺服电机是步科股份（Step Automation）推出的旋转伺服电机系列，覆盖 40 mm 至 380 mm 法兰规格，额定功率从 50 W 到 7.5 kW。该系列电机采用低齿槽转矩设计，可适配增量式、磁电式、通信式及多圈绝对值编码器，与步科伺服驱动器、低压伺服系统、模块化伺服系统及无框力矩电机共同构成完整的运动控制解决方案。

## 工作原理与技术架构

步科伺服电机为永磁同步伺服电机（PMSM），其基本电磁转矩方程为：

$$
T = \frac{3}{2} p \left[ \psi_f i_q + (L_d - L_q) i_d i_q \right]
$$

其中 $p$ 为极对数，$\psi_f$ 为永磁体磁链，$i_d$、$i_q$ 为旋转坐标系下的电流分量，$L_d$、$L_q$ 为直轴与交轴电感。在 $i_d=0$ 控制策略下，电磁转矩与 $i_q$ 近似成正比。

电机通过编码器反馈实现闭环控制：

- **编码器选项**：增量式编码器、磁电编码器、通信式编码器、多圈绝对值编码器（最高 24 位）。
- **控制模式**：位置、速度、力矩控制，支持脉冲、模拟量、Modbus、CANopen、EtherCAT 等控制方式。
- **集成应用**：可与步科 FD/OD/MD/iSMK 等驱动器及一体化伺服轮模组配套使用。

额定转速通常为 3000 rpm，峰值转速及过载能力视具体型号而定。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 法兰规格 | 40 / 60 / 80 / 110 / 130 / 150 / 380 mm | Kinco catalog |
| 额定功率 | 50 W – 7.5 kW | Kinco catalog |
| 额定扭矩 | 0.16 N·m – 48 N·m（系列范围）| Kinco catalog |
| 额定转速 | 3000 rpm | Kinco catalog |
| 最高转速 | 未公开（视型号）| - |
| 供电电压 | 24 VDC / 48 VDC / 220 VAC / 380 VAC | Kinco catalog |
| 编码器 | 增量式、磁电式、通信式、多圈绝对值（最高 24 位）| Kinco catalog |
| 防护等级 | IP65（部分型号）| Kinco catalog |
| 绝缘等级 | 未公开 | - |
| 电机系列 | SMH / SMC / SMK 等 | Kinco catalog |
| 价格 | 未公开 | - |

注：上表为系列级典型参数，具体型号的额定功率、扭矩、转速、电压及编码器配置以对应产品手册为准。

## 应用场景

- **工业机器人**：SCARA、Delta、六关节机器人关节驱动。
- **移动机器人**：AGV/AMR 轮毂驱动、顶升机构、输送机构。
- **协作机器人与人形机器人**：关节模组一体化集成，配合谐波减速器构成旋转关节。
- **数控机床与包装机械**：进给轴、主轴辅助驱动及定位控制。
- **医疗设备**：康复机器人、小型自动化系统。

## 供应链关系

- **上游**：稀土永磁材料、硅钢片、漆包线、轴承、编码器芯片、传感器、接插件。
- **制造商**：步科股份（Step Automation / Kinco）通过关系 `ent_company_step -- manufactures --> ent_component_step_servo_motor` 记录于知识图谱。
- **下游**：机器人 OEM、自动化设备厂商、机床制造商、医疗装备厂商。常与步科伺服驱动器、低压伺服系统形成配套销售，竞争对手包括汇川技术、禾川科技、雷赛智能、鸣志电器等。

## 来源与验证

主要参数来自步科股份公开的产品综合型录（2025 版）及官网。型录中给出了不同法兰尺寸下的功率与扭矩范围、供电电压及编码器选项。最高转速、绝缘等级及具体型号价格未在公开资料中披露，已标注为未公开。