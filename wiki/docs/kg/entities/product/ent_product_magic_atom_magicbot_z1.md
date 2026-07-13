---
id: ent_product_magic_atom_magicbot_z1
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 魔法原子 MagicBot Z1
  en: MagicLab MagicBot Z1 Humanoid Robot
status: active
sources:
- id: src_magicbot_z1_robot_china
  type: website
  url: https://www.robot-china.com/news/202507/09/93390.html
- title: 魔法原子推出高动态双足人形机器人 MagicBot Z1 - 中国机器人网
- id: src_magicbot_z1_qbitai
  type: website
  url: https://www.qbitai.com/2025/07/306985.html
- title: 魔法原子推出高动态双足人形机器人 MagicBot Z1 - 量子位
- id: src_magiclab_official
  type: website
  url: https://www.magiclab.top
- title: MagicLab 魔法原子官网
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 魔法原子 MagicBot Z1 / MagicLab MagicBot Z1 Humanoid Robot

## 概述

MagicBot Z1 是由具身智能公司魔法原子（MagicLab）于 2025 年 7 月发布的高动态双足人形机器人，定位“高性能可靠本体 + 开放 AI 生态系统 + 丰富场景落地”三位一体。该机器人面向科研教育、商业服务、工业操作与家庭陪伴等场景，提供标准版与开发版两个系列，开发版可选装灵巧手、高性能算力包及额外手臂自由度。

## 工作原理 / 技术架构

MagicBot Z1 采用自研高性能关节模组，整机具备 24 个基础自由度，通过加装灵巧手与额外关节可扩展至 49–50 个自由度。单关节最大扭矩超过 \(130\,\text{N}\cdot\text{m}\)，关节运动范围最大可达 \(320^\circ\)，结合鲁棒运动控制算法可实现“大扰动冲击恢复”“连续倒地起身”等高爆发动作。

运动控制层面，关节动力学满足

\[
\boldsymbol{\tau} = \mathbf{M}(\mathbf{q})\ddot{\mathbf{q}} + \mathbf{C}(\mathbf{q},\dot{\mathbf{q}})\dot{\mathbf{q}} + \mathbf{g}(\mathbf{q}) + \boldsymbol{\tau}_{\text{ext}}
\]

其中 \(\mathbf{q}\) 为关节角度，\(\mathbf{M}\)、\(\mathbf{C}\)、\(\mathbf{g}\) 分别为质量矩阵、科氏力/离心力项与重力项，\(\boldsymbol{\tau}_{\text{ext}}\) 为外部扰动力矩。控制器通过模仿学习与强化学习在一天内掌握拟人化全身动作，并能在跌倒后自行站起。

感知系统配备 3D 激光雷达、深度相机与双目相机，搭载魔法原子定位导航系统，可在复杂场景中实现自主移动与避障。开发版可选配 11 自由度灵巧手，支持精细抓取与多模态交互。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 身高 | 约 140 cm |
| 体重 | 约 40 kg |
| 基础自由度 | 24 |
| 最大自由度 | 49–50 |
| 单关节最大扭矩 | \(>130\,\text{N}\cdot\text{m}\) |
| 关节运动范围 | 最大 \(320^\circ\) |
| 电池容量 | 10000 mAh |
| 传感器 | 3D 激光雷达、深度相机、双目相机 |
| 灵巧手（开发版选装） | 11 自由度 |
| 学习新动作时间 | 约 20 分钟（基于多源数据库） |

## 应用场景

- 科研教育与算法验证
- 商业讲解、展览展示与文旅演艺
- 工业场景中的移动操作与物料搬运
- 家庭陪伴与特种应用开发

## 供应链关系

MagicBot Z1 由魔法原子（MagicLab，由追觅科技孵化）研发与销售。上游包括高性能关节电机、减速器、IMU、激光雷达、深度相机、计算平台与电池；中游为魔法原子自研关节模组、标准控制器与多源动作数据库；下游面向开发者、科研机构及行业集成商。魔法原子还提供端到端“原子万象大模型”与开发工具链，支持二次开发。

## 来源与验证

关键参数来自中国机器人网、IT之家等公开报道及 MagicLab 官网。关节最大转速、计算平台算力、续航时间、整机功率与价格等未在公开资料中披露，标注为“未公开”。