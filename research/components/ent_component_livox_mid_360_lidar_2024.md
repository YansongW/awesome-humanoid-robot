---
$id: ent_component_livox_mid_360_lidar_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Livox Mid-360 LiDAR
  zh: Livox Mid-360 激光雷达
  ko: Livox Mid-360 LiDAR
summary:
  en: Compact 360-degree LiDAR commonly mounted on the head or torso of humanoid robots.
  zh: Livox Mid-360 激光雷达是人形机器人领域的重要component。以下内容整理自项目 Wiki，供深入查阅。
  ko: 휨로봇 머리나 몸통에 장착되는 컴팩트한 360도 LiDAR.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- '360'
- component
- lidar
- livox
- sensor
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_livox.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Livox Mid-360 LiDAR
  url: https://www.livoxtech.com/
  date: '2024'
  accessed_at: '2026-07-02'
---


## 概述
Livox Mid-360 激光雷达是人形机器人领域的重要component。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 览沃 / Livox Technology

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 览沃 |
| **英文名** | Livox Technology |
| **总部** | 中国深圳 |
| **成立时间** | 2016 |
| **官网** | [https://www.livoxtech.com](https://www.livoxtech.com) |
| **供应链环节** | 激光雷达、混合固态 LiDAR、机器人 3D 感知 |
| **企业属性** | 私有公司、DJI 内部孵化独立公司 |
| **母公司/所属集团** | DJI 大疆创新内部孵化 / 独立运营 |
| **数据来源** | 官网、DJI/Livox 公开资料、产品 datasheet |

### 公司简介

览沃科技是 DJI 内部孵化的激光雷达公司，以高性价比混合固态激光雷达切入机器人与自动驾驶市场。

Livox 致力于提供高性能、低成本的激光雷达传感器，产品采用独特的旋镜式混合固态扫描技术。Mid-360 凭借 360° 环视、小体积与轻量化，成为机器人 SLAM 与导航的热门选择，并已应用于四足机器人、清洁机器人与 AMR。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Mid 系列 | 机器人 360° 激光雷达 | Mid-360 / Mid-360S / Mid-70 | AMR、四足机器人、清洁机器人、SLAM |
| HAP / Horizon | 车规级激光雷达 | HAP / Horizon / Tele-15 | 自动驾驶、乘用车 |
| Avia | 测绘级激光雷达 | Avia | 无人机测绘、三维建模 |

### 代表产品

#### 览沃 Mid-360

> 览沃 Mid-360：请访问 [官方资料](https://www.livoxtech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 65 mm × 65 mm × 60 mm | 官方 datasheet |
| 重量 | 265 g | 官方 datasheet |
| 激光波长 | 905 nm | 官方 datasheet |
| 激光安全等级 | Class 1（IEC60825-1:2014） | 官方 datasheet |
| FOV | 水平 360°；竖直 -7° ~ 52° | 官方 datasheet |
| 探测距离 | 40 m @ 10% 反射率；70 m @ 80% 反射率 | 官方 datasheet |
| 点频 | 200,000 点/秒（首回波） | 官方 datasheet |
| 帧率 | 10 Hz（典型） | 官方 datasheet |
| 测距精度 | ≤2 cm @ 10 m；≤3 cm @ 0.2 m | 官方 datasheet |
| IMU | 内置 ICM40609 | 官方 datasheet |
| 接口 | 100 BASE-TX Ethernet | 官方 datasheet |
| 功耗 | 6.5 W（典型） | 官方 datasheet |
| 价格 | 约 CNY 3,999 | 官方商城 |

**技术亮点**：360° 环视、超小体积、内置 IMU、IP67 防护，是机器人 SLAM 与导航的主流选择。

**应用场景**：AMR/AGV 导航、四足机器人、清洁机器人、割草机器人、三维测绘。

#### 览沃 HAP

> 览沃 HAP：请访问 [官方资料](https://www.livoxtech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| FOV | 120°(H) × 30°(V) | 官方 datasheet |
| 探测距离 | 150 m @ 10% 反射率 | 官方 datasheet |
| 点频 | 240,000 点/秒 | 官方 datasheet |
| 角分辨率 | 0.18°(H) × 0.23°(V) | 官方 datasheet |
| 扫描方式 | 混合固态（旋镜式） | 官方 datasheet |
| 防护等级 | IP67 | 官方 datasheet |
| 价格 | 未公开 | 未公开 |

**技术亮点**：车规级混合固态激光雷达，已在多款乘用车前装量产，兼顾远距探测与可靠性。

**应用场景**：乘用车 ADAS、Robotaxi、高端移动机器人。

### 供应链位置

- **上游关键零部件/材料**：905 nm 激光器、SPAD/APD、扫描电机、光学镜片、主控 SoC、IMU
- **下游客户/应用场景**：AMR/AGV、四足机器人（如云深处绝影 X30）、清洁机器人、割草机器人、自动驾驶
- **主要竞争对手/对标**：禾赛科技、速腾聚创、Ouster、Velodyne、RoboSense

### 知识图谱节点与关系

- 公司实体：`ent_company_livox`
- 产品实体：`ent_component_livox_mid_360`
- 产品实体：`ent_component_livox_hap`
- 关键关系：
  - `ent_company_livox` -- `manufactures` --> `ent_component_livox_mid_360`
  - `ent_company_livox` -- `manufactures` --> `ent_component_livox_hap`
  - `ent_company_livox` -- `supplies` --> `ent_company_deep_robotics` (云深处绝影 X30 四足机器人搭载 Livox Mid-360)

### 参考资料

1. [官网](https://www.livoxtech.com)
2. [产品资料与公开报道](https://www.livoxtech.com)
3. [附录 D 产品目录](../index-products.md)

## 参考
- [Livox Mid-360 LiDAR](https://www.livoxtech.com/)
- 项目 Wiki：appendix-d/companies/company_livox.md



