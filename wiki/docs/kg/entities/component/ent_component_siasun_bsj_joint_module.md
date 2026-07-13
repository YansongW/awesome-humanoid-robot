---
id: ent_component_siasun_bsj_joint_module
type: component
schema_version: 1
domain: 02_components
status: active
names:
  zh: 新松 BSJ 仿生人形一体化关节模组
  en: SIASUN BSJ Humanoid Integrated Joint Module
sources:
- id: src_siasun_bsj_joint_module_official
  type: website
- title: 新松多可仿生人形机器人新品发布
  url: https://www.siasun.com/news-detail167.html
- id: src_siasun_mr73a_report
  type: website
- title: 腾讯新闻 – 新松睿可系列报道
  url: https://view.inews.qq.com/a/20250710A0496M00
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from official public materials and industry reports;
    missing values marked as 未公开.
---


# 新松 BSJ 仿生人形一体化关节模组 / SIASUN BSJ Humanoid Integrated Joint Module

## 概述

新松 BSJ 仿生人形一体化关节模组（SIASUN BSJ Humanoid Integrated Joint Module）是由新松机器人（SIASUN）为其轮式人形机器人“睿可（rico）”系列开发的自研核心驱动单元。该模组将无框力矩电机、谐波减速器、双编码器与驱动控制器集成于关节内部，构成高度紧凑的旋转关节执行器，是新松在具身智能本体硬件层面的关键零部件。BSJ 系列关节模组主要服务于 MR73A/B 等人形机器人，实现双臂柔顺操作、全身阻抗控制与动态平衡。

## 工作原理 / 技术架构

一体化关节模组基于“电机 + 减速器 + 传感器 + 驱动”的四合一架构：

1. **无框力矩电机**：采用外转子无框直驱电机，定子与转子直接嵌入关节壳体，省去传统电机轴、轴承与联轴器，提高扭矩密度并降低轴向尺寸。
2. **谐波减速器**：通过柔轮、刚轮与波发生器的弹性变形传动，实现高减速比（通常 50:1–120:1）与接近零背隙的输出，使关节在低速下输出大扭矩。
3. **双编码器系统**：电机端高速编码器用于电流环与速度环闭环控制，输出端低速绝对值编码器用于位置环与力矩估算，实现全闭环力控。
4. **驱动控制器**：集成 FOC（磁场定向控制）算法，支持 CAN/EtherCAT 总线通信，实时完成扭矩、速度、位置三环控制。

关节输出扭矩与电机电磁扭矩的关系可表示为

$$
\tau_{\text{joint}} = \eta \, i \, \tau_{\text{motor}}
$$

其中 $\tau_{\text{joint}}$ 为关节输出扭矩，$\tau_{\text{motor}}$ 为电机峰值扭矩，$i$ 为谐波减速比，$\eta$ 为传动效率（谐波减速器典型值 0.70–0.90）。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | 新松机器人 / SIASUN Robot & Automation | 官方新闻稿 |
| 产品系列 | BSJ 仿生人形一体化关节模组 | 新松官网 |
| 关节类型 | 旋转关节（四合一集成） | 公开报道 |
| 适用机型 | 睿可 MR73A / MR73B、松羿 / 松行 | 新松官网 / 行业研报 |
| 最大扭矩 | 未公开 | 新松未披露单关节额定/峰值扭矩 |
| 减速比 | 未公开 | 依关节位置配置 |
| 编码器分辨率 | 未公开 | 双编码器全闭环 |
| 通信接口 | CAN / EtherCAT（推测） | 行业常见配置 |
| 控制方式 | FOC + 阻抗控制 / 力位混合控制 | 公开报道 |
| 工作温度 | 未公开 | - |
| 防护等级 | 未公开 | - |
| 重量 | 未公开 | - |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **人形机器人双臂操作**：BSJ 关节模组部署于 MR73A 双臂，支持全身阻抗控制，完成柔性抓取、装配、搬运等任务。
- **轮式人形机器人移动操作**：在 MR73B 升降底盘与上肢中提供关节驱动，适配仓储物流中不同高度货架的存取作业。
- **商业服务与导览**：为松羿/松行系列提供低噪音、高响应的关节运动，支持人机交互场景中的自然姿态。

## 供应链关系

在公司–产品网络中，新松机器人（`ent_company_siasun`）作为整机 OEM 与核心零部件制造商，自研并生产 BSJ 一体化关节模组（`ent_component_siasun_bsj_joint_module`）。该零部件通过 `uses` 关系装配于人形机器人产品睿可 MR73A（`ent_product_siasun_mr73a`）与 MR73B（`ent_product_siasun_mr73b`）中。新松通过自研关节模组降低对外部减速器、电机供应商的依赖，但在芯片、传感器、电池等环节仍部分依赖外购。其上游潜在包括高性能磁钢、谐波柔轮钢材、伺服驱动芯片；下游直接对接新松自家人形机器人整机，未来可能外供国内其他人形机器人 OEM。

## 来源与验证

- 新松官网新闻稿披露了睿可 MR73A/B 的产品定位、自由度与双臂柔顺控制方案，并明确其采用自研 BSJ 系列一体化关节模组。
- 腾讯新闻等行业报道补充了 MR73A 约 21–27 DOF、MR73B 移动速度约 1 m/s 等整机参数，但未公开 BSJ 单关节的扭矩、减速比、重量等核心指标。
- 本卡片严格以公开来源为准，未公开参数均标注为“未公开”，未进行数值外推。