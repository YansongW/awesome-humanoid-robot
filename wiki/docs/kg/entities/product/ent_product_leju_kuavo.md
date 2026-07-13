---
id: ent_product_leju_kuavo
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 乐聚 KUAVO
  en: Leju KUAVO
status: active
sources:
- id: src_leju_kuavo_cls
  type: website
  url: https://m.cls.cn/detail/1535409
- title: 人形机器人再升级！乐聚和深开鸿推首款可行走的开源鸿蒙人形机器人 - 财联社
- id: src_leju_kuavo_sznews
  type: website
  url: https://www.sznews.com/news/content/mb/2023-12/06/content_30630603.htm
- title: 国内首款可跳跃的开源鸿蒙人形机器人在深发布 - 深圳新闻网
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 乐聚 KUAVO / Leju KUAVO

## 概述

乐聚 KUAVO（中文名“夸父”）是乐聚（深圳）机器人技术有限公司于 2023 年 12 月发布的大尺寸高动态人形机器人，也是国内首款可跳跃、可适应多地形行走的开源鸿蒙人形机器人。该产品搭载深开鸿 KaihongOS，采用全栈开源设计，面向教育科研、工业智造、商业服务等场景。

## 工作原理 / 技术架构

KUAVO 采用一体化自研关节模组，每个关节集无框力矩电机、谐波减速器、双编码器与驱动器于一体。其一体化关节峰值扭矩超过 300 N·m，扭矩密度超过 200 N·m/kg。运动控制频率达到 2 kHz，实时响应延迟低至 0.0005 s。全身动力学控制基于落足点自主调节、状态估计与全身力控制算法，使机器人可在沙地、草地等复杂地形行走，并完成连续跳跃。

电机输出扭矩 $\tau$ 与关节角加速度关系可表示为：

$$
\tau = I \ddot{\theta} + b \dot{\theta} + \tau_g(\theta)
$$

其中 $I$ 为等效转动惯量，$b$ 为阻尼系数，$\tau_g$ 为重力矩。高控制频率与高密度关节共同支撑 KUAVO 的高动态运动。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 身高 | 不足 1.5 m |
| 体重 | 约 45 kg |
| 全身自由度 | 26 |
| 步速 | 最高 4.6 km/h |
| 连续跳跃高度 | >20 cm |
| 一体化关节峰值扭矩 | >300 N·m |
| 关节扭矩密度 | >200 N·m/kg |
| 控制频率 | 2 kHz |
| 操作系统 | 开源鸿蒙 KaihongOS |
| 外壳材料 | 航空级铝合金 |

## 应用场景

- 高校与科研机构的运动控制、具身智能研究
- 工业制造中的巡检、搬运与上下料
- 商业服务场景中的迎宾、讲解与展示
- 特种作业与家庭服务（远期规划）

## 供应链关系

乐聚位于人形机器人整机制造环节，上游自研一体化关节、控制器与运动算法，并采购电机、减速器、传感器、计算平台与电池；下游面向教育科研、工业客户与解决方案集成商。KUAVO 与深开鸿、华为云等生态伙伴在操作系统与大模型层面形成协同。

## 来源与验证

参数来源于财联社报道（https://m.cls.cn/detail/1535409）及深圳新闻网发布稿（https://www.sznews.com/news/content/mb/2023-12/06/content_30630603.htm）。部分精确尺寸与续航细节未在公开资料中披露，标注为“未公开”。