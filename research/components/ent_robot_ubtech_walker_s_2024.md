---
$id: ent_robot_ubtech_walker_s_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: UBTECH Walker S
  zh: 优必选 Walker S
  ko: UBTECH Walker S
summary:
  en: Industrial humanoid robot for factory operations, featuring all-electric modular joints.
  zh: 面向工厂作业的工业人形机器人，采用全电驱模块化关节。
  ko: 공장 작업용 산업용 휨로봇, 전기식 모듈형 관절 특징.
domains:
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- industrial
- modular_joint
- robot_system
- ubtech
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_walker_s2.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: UBTECH Walker S
  url: https://www.ubtrobot.com/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
优必选 Walker S是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 优必选 Walker S2 / UBTECH Walker S2

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [优必选 / UBTECH](../companies/company_ubtech.md) |
| **产品类别** | 工业级人形机器人 |
| **发布时间** | 2024–2025 年 |
| **状态** | 量产/企业交付 |
| **官网/来源** | [UBTECH 商用官网](https://www.commercial.ubtrobot.com/) |

### 产品概述

优必选 Walker S2 是 Walker 工业人形机器人系列的第二代产品，专为汽车制造、3C 电子与物流仓储场景设计。整机拥有 52 个自由度，双臂最大负载 15 kg，并配备第四代五指灵巧手与 ±162° 腰部旋转，能够完成拆箱、上料、质检、喷涂等复杂工业动作。

Walker S2 的核心亮点是自主电池热插拔系统，可在 3 分钟内完成电池更换，实现接近 24 小时连续作业。其感知系统包括双目立体视觉、深度 LiDAR、六轴力传感器与 IMU，搭载 ROSA 2.0 操作系统与多模态大模型，支持多机协同与 MES 系统对接。Walker S2 已在蔚来、比亚迪、空客等客户的产线或试点项目中部署验证。

### 产品图片

> UBTECH Walker S2：请访问 [官方资料](https://www.commercial.ubtrobot.com/) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 176 cm（高） | 公开规格 |
| 重量 | 约 70–75 kg | 不同配置来源 |
| 自由度（整机） | 52 DOF | 公开规格 |
| 关键性能指标 | 双臂最大负载 15 kg；腰部旋转 ±162° | 公开规格 |
| 行走速度 | 约 2 m/s（7.2 km/h） | 公开规格 |
| 续航 | 约 2 小时；支持热插拔电池 | 公开规格 |
| 计算平台 | X86 + NVIDIA Jetson Orin | RBTX 产品页 |
| 价格 | 未公开（行业估计 68,000–120,000 USD） | 第三方估计 |

### 供应链位置

- **制造商**：[优必选 / UBTECH](../companies/company_ubtech.md)
- **核心零部件/技术来源**：自研一体化关节、NVIDIA Jetson Orin 计算平台、双目立体视觉、深度 LiDAR、灵巧手；部分减速器、电机外购。
- **下游应用/客户**：蔚来汽车、比亚迪、空客、沙特/新加坡/日本试点项目。

### 知识图谱节点与关系

- 产品实体：`ent_product_ubtech_walker_s2`
- 制造商实体：`ent_company_ubtech`
- 关键关系：
  - `rel_ent_company_ubtech_manufactures_ent_product_ubtech_walker_s2`（`ent_company_ubtech` → `manufactures` → `ent_product_ubtech_walker_s2`）

### 应用场景

- **汽车制造**：蔚来、比亚迪等工厂执行外观质检、内饰装配、安全带检测与物料搬运。
- **3C 电子**：精密装配、螺丝拧紧、元器件插装与 AOI 复检辅助。
- **商用展示**：展厅讲解、商超导览与品牌活动互动展示。

### 竞争对比

| 对比项 | 优必选 Walker S2 | Tesla Optimus Gen 3 | Figure 02 |
|--------|------------------|---------------------|-----------|
| 定位 | 工业人形 | 通用/工业人形 | 工业制造人形 |
| 整机 DOF | 52 | 28+ 躯干 + 22×2 手 | 28 |
| 双臂负载 | 15 kg | 约 20 kg | 25 kg |
| 核心优势 | 工厂部署案例、热插拔电池、灵巧手 | 成本目标、AI 数据 | Helix VLA、宝马部署 |

### 选购与部署建议

- 汽车/3C 制造企业应重点评估 Walker S2 与现有 MES/AGV 系统的对接能力。
- 建议规划电池热插拔站点与多机协同调度方案，以发挥 24 小时连续作业优势。

### 参考资料

1. [UBTECH 商用官网](https://www.commercial.ubtrobot.com/)
2. [Robozaps – UBTECH Walker S Review](https://blog.robozaps.com/b/ubtech-walker-s-review)
3. [Humanoid.Guide – Walker S2](https://humanoid.guide/product/walker-s2/)
4. [RBTX – UBTECH Walker S2 产品页](https://rbtx.com/en-US/components/humanoid/ubtech-humanoid-walker-s2)

## 参考
- [UBTECH Walker S](https://www.ubtrobot.com/)
- 项目 Wiki：appendix-d/products/product_walker_s2.md

