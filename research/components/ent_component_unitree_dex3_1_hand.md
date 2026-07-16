---
$id: ent_component_unitree_dex3_1_hand
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Unitree Dex3-1 Dexterous Hand
  zh: Unitree Dex3-1 灵巧手
  ko: Unitree Dex3-1 민첩한 손
summary:
  en: A force-controlled, three-fingered dexterous end effector option for the Unitree G1-EDU humanoid robot, adding 7+2 degrees
    of freedom per hand for object manipulation.
  zh: Unitree Dex3-1 灵巧手是人形机器人领域的重要component。以下内容整理自项目 Wiki，供深入查阅。
  ko: Unitree G1-EDU 휴머노이드 로봇을 위한 힘 제어식 3지 민첩한 엔드 이펙터 옵션으로, 물체 조작을 위해 손당 7+2자유도를 추가함.
domains:
- 02_components
- 06_design_engineering
- 11_applications_markets
layers:
- upstream
- midstream
functional_roles:
- component
- knowledge
tags:
- unitree
- dex3_1
- dexterous_hand
- end_effector
- force_control
- three_finger
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_unitree.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Unitree G1 Developer Specifications
  url: https://support.unitree.com/home/en/G1_developer
  date: '2026'
  accessed_at: '2026-06-22'
- id: src_002
  type: paper
  title: Identification of a Physics-Based Electrical Power Consumption Model for the Unitree G1 Humanoid Arm
  url: https://arxiv.org/abs/2606.15915
  date: '2026'
  accessed_at: '2026-06-22'
theoretical_depth:
- system
---


## 概述
Unitree Dex3-1 灵巧手是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 宇树科技 / Unitree Robotics

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 宇树科技 |
| **英文名** | Unitree Robotics |
| **总部** | 中国杭州 |
| **成立时间** | 2016 年 |
| **官网** | [https://www.unitree.com](https://www.unitree.com) |
| **供应链环节** | 整机 OEM / 四足+人形机器人、自研关节电机 |
| **企业属性** | 独角兽、四足机器人全球销量领先 |
| **母公司/所属集团** | 无 |
| **数据来源** | Unitree 官网、IT之家、Robozaps、第三方产品数据库 |

### 公司简介

宇树科技以高性价比四足机器人（机器犬）切入市场，2023 年发布首款全尺寸人形机器人 H1，2024 年推出紧凑型人形 G1。

公司坚持核心零部件垂直整合，自研 M107 永磁同步电机、驱动器与整机运控算法，并通过 ROS2 兼容生态与激进定价策略，成为科研机构和开发者社区中最具出货量的人形平台之一。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 全尺寸人形 | 高动态运动、科研原型 | H1 / H1-2 | 科研教育、AI 具身智能研究 |
| 紧凑人形 | 低成本开发平台 | G1 / G1-Comp | 教育、开发者、轻工业 |
| 四足机器人 | 巡检、运输、科研 | Go2 / B2 / B2-W | 电力巡检、应急救援、科研 |

### 代表产品

#### Unitree H1

> Unitree H1：请访问 [官方资料](https://www.unitree.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 180 cm | Unitree 公开资料 / Robozaps |
| 重量 | 47 kg | 公开规格 |
| 自由度 | 26 DOF（基础版） | Robozaps 汇总 |
| 负载/扭矩 | 膝关节峰值扭矩 360 N·m | 公开规格 |
| 速度/转速 | 行走约 1.5 m/s；跑步 3.3 m/s | Unitree 宣称世界纪录 |
| 续航 | 约 1.5–2 h（864 Wh 电池） | 公开规格 |
| 接口/通信 | Wi-Fi、蓝牙、ROS2 / Unitree SDK | 公开规格 |
| 价格 | 约 9 万美元 / 国内约 65 万元 | 经销商与媒体报道 |

**技术亮点**：M107 高扭矩密度电机（189 N·m/kg）、强化学习-based 步态、可热插拔电池、OTA 持续升级。

**应用场景**：双足运动研究、具身智能算法验证、高校实验室。

#### Unitree G1

> Unitree G1：请访问 [官方资料](https://www.unitree.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 127 cm | 公开规格 |
| 重量 | 约 35 kg | 公开规格 |
| 自由度 | 23–43 DOF（含灵巧手配置） | Unitree 配置差异 |
| 负载/扭矩 | 负载约 2 kg | Humanoid.Guide |
| 速度/转速 | 约 2 m/s | 公开规格 |
| 续航 | 约 2 h | 公开规格 |
| 接口/通信 | Wi-Fi、蓝牙、ROS2 | 公开规格 |
| 价格 | 约 1.6 万美元 / 国内 9.9 万元起 | 媒体报道 |

**技术亮点**：三指力控灵巧手、Intel RealSense / LIVOX 传感器、低成本高可及性。

**应用场景**：教育演示、AI 研究、轻量物流与商用展示。

### 供应链位置

- **上游关键零部件/材料**：自研 M107 电机与驱动器，外购减速器、轴承、电池、视觉传感器（参见 [第 4 章 执行器](../../../chapters/chapter-04.md)）。
- **下游客户/应用场景**：高校、科研院所、开发者、物流与安防客户。
- **主要竞争对手/对标**：优必选 Walker、傅利叶 GR-1、特斯拉 Optimus。

### 知识图谱节点与关系

- 公司实体：`ent_company_unitree`
- 产品实体：`ent_product_unitree_h1`、`ent_product_unitree_g1`
- 关键关系：
  - `ent_company_unitree` -- `manufactures` --> `ent_product_unitree_h1`
  - `ent_company_unitree` -- `manufactures` --> `ent_product_unitree_g1`
  - `ent_product_unitree_h1` -- `uses` --> `ent_component_unitree_m107_motor`

### 参考资料

1. [Unitree 官网](https://www.unitree.com)
2. [Robozaps – Unitree H1 Review](https://blog.robozaps.com/b/unitree-h1-review)
3. [Humanoid.Guide – Unitree G1](https://humanoid.guide/product/g1/)
4. [IT之家 – Unitree 人形机器人报道](https://www.ithome.com)
5. [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考
- [Unitree G1 Developer Specifications](https://support.unitree.com/home/en/G1_developer)
- [Identification of a Physics-Based Electrical Power Consumption Model for the Unitree G1 Humanoid Arm](https://arxiv.org/abs/2606.15915)
- 项目 Wiki：appendix-d/companies/company_unitree.md



