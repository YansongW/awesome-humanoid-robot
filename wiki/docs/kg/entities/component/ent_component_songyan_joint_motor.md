---
id: ent_component_songyan_joint_motor
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 松延动力高性能关节电机
  en: Songyan Dynamics High-Performance Joint Motor
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-13 00:00:00+00:00
sources:
- id: src_songyan_n2_page
  type: website
- title: 松延动力 N2 产品页
  url: https://noetixrobotics.com/n2
- id: src_songyan_baidu_baike
  type: website
- title: 百度百科 - 松延动力 N2
  url: https://baike.baidu.com/item/%E6%9D%BE%E5%BB%B6%E5%8A%A8%E5%8A%9BN2/67393633
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自松延动力官方产品页与公开资料；核心机电参数未公开，已标注。
---


# 松延动力高性能关节电机 / Songyan Dynamics High-Performance Joint Motor

## 概述

松延动力高性能关节电机是北京松延动力科技集团股份有限公司（Noetix Robotics）为其 N2 人形机器人自研的关节执行器。该电机部署于 N2 整机 18 个自由度中，膝关节峰值扭矩达 150 N·m，配合双编码器与轻量化结构，支撑机器人完成奔跑、跳跃、连续空翻等高动态运动。

## 工作原理 / 技术架构

人形机器人关节电机通常由无刷直流电机、减速器（行星或谐波）、双编码器与伺服驱动器组成。输出扭矩 $\tau_{\mathrm{out}}$ 与电机扭矩 $\tau_{\mathrm{motor}}$、减速比 $i$ 及传动效率 $\eta$ 的关系为

$$
\tau_{\mathrm{out}} = \tau_{\mathrm{motor}} \cdot i \cdot \eta
$$

整机质量约 30 kg，单腿 5 自由度、单臂 4 自由度，关键关节需输出足够峰值扭矩以克服惯性力与重力矩，实现空翻落地缓冲与动态平衡。松延 N2 采用 MPC（模型预测控制）与强化学习融合的运动控制算法，关节电机需提供毫秒级力矩响应。

## 关键参数表

| 参数 | 典型值 | 备注 |
|------|--------|------|
| 峰值扭矩 | ≥ 150 N·m（膝关节） | 松延官网 |
| 整机自由度 | 18 DOF | 单腿 5，单臂 4 |
| 整机重量 | 约 30 kg | 松延官网 |
| 膝关节运动范围 | 0°–126° | 产品页 |
| 髋关节运动范围 | P -90°~+45°，R -37°~+57°，Y -37°~+57° | 产品页 |
| 编码器 | 双编码器 | 产品页 |
| 关节输出轴承 | 交叉滚子 + 深沟球组合 | 产品页 |
| 供电 | 锂电池 48 V / 7 Ah | 产品页 |
| 通信 | Wi-Fi 6 / 蓝牙 5.2 / OTA | 产品页 |
| 电机型号 | 未公开 | - |
| 额定功率 / 额定转速 / 减速比 | 未公开 | - |

## 应用场景

- 人形机器人 N2 的髋、膝、踝、肩、肘等关节驱动
- 科研教育与机器人竞赛
- 商业展示与娱乐表演
- 幼儿陪伴与家庭服务机器人

## 供应链关系

制造商为北京松延动力科技集团股份有限公司（`ent_company_songyan_dynamics`）。该关节电机被其产品实体 `ent_product_songyan_dynamics_n2` 使用。上游关键原材料包括磁材、硅钢片、铜线、轴承、编码器芯片与减速器；下游为人形机器人整机厂与终端用户。知识图谱中的关键关系为：`ent_company_songyan_dynamics` -- `manufactures` --> `ent_component_songyan_joint_motor`。

## 来源与验证

本卡片参数引自松延动力 N2 官方产品页与百度百科公开资料。电机型号、额定功率、减速比、重量等核心机电参数未公开。