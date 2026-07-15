---
$id: ent_robot_unitree_h1_humanoid_robot_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Unitree H1 Humanoid Robot
  zh: 宇树 H1 人形机器人
  ko: Unitree H1 휨로봇
summary:
  en: Full-size electric humanoid with 25-27 DoF, proprietary high-torque joints, peak leg-joint torque up to 360 N·m and
    torque density ~189 N·m/kg.
  zh: '## 概述 宇树 H1 人形机器人是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。'
  ko: 25-27자유도를 가진 전기식 휨로봇, 최대 360 N·m 다리 관절 토크 및 약 189 N·m/kg 토크 밀도.
domains:
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- high_torque_joint
- humanoid
- quasi_direct_drive
- robot_system
- unitree
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_unitree_h1.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Unitree H1 Humanoid Robot
  url: https://www.unitree.com/products/h1
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
宇树 H1 人形机器人是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 宇树 H1 / Unitree H1

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [宇树科技 / Unitree Robotics](../companies/company_unitree.md) |
| **产品类别** | 全尺寸高动态人形机器人 |
| **发布时间** | 2023 年 |
| **状态** | 量产/商用 |
| **官网/来源** | [Unitree 官网](https://www.unitree.com) |

### 产品概述

宇树 H1 是 Unitree Robotics 推出的全尺寸高动态人形机器人，定位为科研、具身智能研究与高动态运动验证平台。H1 采用宇树自研 M107 永磁同步电机，膝关节峰值扭矩达 360 N·m，峰值扭矩密度约 189 N·m/kg，曾创造全尺寸人形机器人 3.3 m/s 奔跑速度纪录。

H1 的基础版手臂为 4 DOF，可选配 H1-2 升级方案将手臂提升至 7 DOF 并增强整机负载能力。整机支持 ROS2 与 Unitree SDK，具备 Wi-Fi、蓝牙与热插拔电池，适用于高校实验室、AI 研究机构与工业原型验证。

### 产品图片

> Unitree H1：请访问 [官方资料](https://www.unitree.com) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 180 cm（高） | 公开规格 |
| 重量 | 约 47 kg（H1 基础版） | 公开规格 |
| 自由度（整机） | 26–27 DOF | 基础版 26 DOF；H1-2 为 27 DOF |
| 关键性能指标 | 膝关节峰值扭矩 360 N·m；扭矩密度 189 N·m/kg | 公开规格 |
| 行走速度 | 约 1.5 m/s；奔跑速度 3.3 m/s | 公开规格 |
| 续航 | 约 1.5–2 小时（864 Wh 电池） | 公开规格 |
| 计算平台 | 可选 Intel Core / NVIDIA Jetson Orin NX | 公开规格 |
| 价格 | 约 90,000 USD / 国内约 65 万元 | 经销商与媒体报道 |

### 供应链位置

- **制造商**：[宇树科技 / Unitree Robotics](../companies/company_unitree.md)
- **核心零部件/技术来源**：自研 M107 电机与驱动器、Intel RealSense / LIVOX 传感器、减速器与轴承外购。
- **下游应用/客户**：高校、科研院所、具身智能研究团队、工业原型客户。

### 知识图谱节点与关系

- 产品实体：`ent_product_unitree_h1`
- 制造商实体：`ent_company_unitree`
- 关键关系：
  - `rel_ent_company_unitree_manufactures_ent_product_unitree_h1`（`ent_company_unitree` → `manufactures` → `ent_product_unitree_h1`）

### 应用场景

- **双足运动研究**：高校与科研机构开展步态规划、强化学习与动态平衡算法验证。
- **具身智能平台**：作为大模型与机器人控制结合的硬件载体，用于 VLA/VLM 部署测试。
- **工业原型验证**：物流与制造企业用于高动态搬运、越障与复杂地形通过性测试。

### 竞争对比

| 对比项 | Unitree H1 | Unitree G1 | Tesla Optimus Gen 3 |
|--------|------------|------------|---------------------|
| 定位 | 全尺寸高动态研究平台 | 紧凑型开发平台 | 通用/工业人形 |
| 身高 | 180 cm | 127 cm | 173 cm |
| 价格 | 约 90,000 USD | 约 16,000 USD | 目标 20,000–30,000 USD |
| 核心优势 | 高动态运动、扭矩密度、ROS2 生态 | 低成本、可及性、灵巧手 | 制造规模目标、灵巧手 |

### 选购与部署建议

- 高动态运动研究团队建议选配 H1-2 升级方案以提升手臂自由度与整机负载。
- 由于 H1 基础版手臂自由度有限，需要灵巧操作的项目应额外配置末端执行器。

### 参考资料

1. [Unitree 官网](https://www.unitree.com)
2. [Robozaps – Unitree H1 Review](https://blog.robozaps.com/b/unitree-h1-review)
3. [OpenELAB – Unitree H1-2](https://openelab.com/products/unitree-h1-2-humanoid-robot)
4. [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考
- [Unitree H1 Humanoid Robot](https://www.unitree.com/products/h1)
- 项目 Wiki：appendix-d/products/product_unitree_h1.md


