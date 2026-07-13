---
id: ent_component_realman_rjm
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 睿尔曼 RJM 一体化关节模组
  en: RealMan RJM Integrated Joint Module
sources:
- id: src_realman_official
  type: website
- title: 睿尔曼智能官网
  url: https://www.realman-robotics.com
- id: src_realman_ites
  type: website
- title: RealMan Intelligent Technology company profile
  url: https://global.iteschina.com/en/exhibitor-list/details/11808
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from RealMan official materials and public reports;
    detailed actuator-level parameters are not fully disclosed and marked as 未公开.
---


# 睿尔曼 RJM 一体化关节模组 / RealMan RJM Integrated Joint Module

## 概述

睿尔曼 RJM 一体化关节模组是睿尔曼智能（RealMan）推出的高集成度机器人关节执行单元，采用无框力矩电机、谐波减速器与双编码器一体化设计。该模组将电机、减速器、编码器、驱动器与控制器高度集成，可直接用于构建超轻量仿人机械臂与人形机器人关节，显著缩短整机开发周期。

## 工作原理与技术架构

RJM 关节模组的典型机电架构为：

1. **无框力矩电机**：采用永磁同步无框力矩电机作为动力源，定子与转子可直接嵌入关节结构，提高扭矩密度并降低关节惯量。
2. **谐波减速器**：电机高速低扭矩输出经谐波减速器转换为低速高扭矩关节输出。谐波减速器减速比 $i$ 通常介于 50:1 至 160:1，输出扭矩 $T_{\text{out}}$ 与电机扭矩 $T_m$ 的关系为：
   $$
   T_{\text{out}} = \eta \cdot i \cdot T_m
   $$
   其中 $\eta$ 为传动效率。
3. **双编码器反馈**：电机端编码器用于 FOC 电流环控制，关节输出端编码器用于高精度位置闭环，消除减速器回程误差。
4. **驱控一体化**：集成伺服驱动器与通信接口，支持位置、速度、力矩控制模式。

关节输出转速 $n_{\text{out}}$ 与电机转速 $n_m$ 的关系：

$$
n_{\text{out}} = \frac{n_m}{i}
$$

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 无框力矩电机 + 谐波减速器 + 双编码器 | 睿尔曼官网 |
| 控制模式 | 位置 / 速度 / 力矩 | 睿尔曼产品手册 |
| 通信接口 | CAN / EtherCAT（视配置）| 睿尔曼产品手册 |
| 电机类型 | 永磁同步无框力矩电机 | 睿尔曼公开报道 |
| 减速器类型 | 谐波减速器 | 睿尔曼公开报道 |
| 编码器 | 双编码器（电机端 + 输出端）| 睿尔曼公开报道 |
| 扭矩范围 | 未公开 | - |
| 减速比 | 未公开 | - |
| 额定转速 | 未公开 | - |
| 重复定位精度 | 未公开 | - |
| 防护等级 | 未公开 | - |
| 价格 | 未公开 | - |

注：睿尔曼未公开 RJM 系列具体型号的扭矩、减速比、转速及精度等参数，上表为其公开披露的一体化关节架构信息。

## 应用场景

- **超轻量仿人机械臂**：作为 RLM-63 / RLM-85 / RLM-100 机械臂的关节核心。
- **人形机器人上半身**：双臂、躯干等旋转关节的一体化驱动单元。
- **协作机器人**：紧凑、高集成度的关节模组，降低机械臂自重。
- **科研教育**：支持 ROS/ROS2 与二次开发，用于机器人运动控制研究。
- **商业服务机器人**：展厅讲解、无人零售、遥操作等场景。

## 供应链关系

- **上游**：谐波减速器、无框力矩电机、编码器、驱动器、铝镁合金结构件、控制芯片。
- **制造商**：睿尔曼智能（RealMan）通过关系 `ent_company_realman -- manufactures --> ent_component_realman_rjm` 记录于知识图谱。
- **下游**：整机产品 `ent_product_realman_rlm63` 使用 RJM 关节模组。下游客户包括高校、科研院所、具身智能创业公司、服务机器人整机厂。主要竞争对手包括越疆、遨博、节卡、大族机器人、优傲 UR 等。

## 来源与验证

RJM 关节模组的架构与控制接口信息来自睿尔曼官网及 ITES 展会企业资料。扭矩、减速比、额定转速、重复定位精度等具体性能参数未在公开资料中披露，已标注为未公开。