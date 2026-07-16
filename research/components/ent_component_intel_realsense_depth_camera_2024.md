---
$id: ent_component_intel_realsense_depth_camera_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Intel RealSense Depth Camera
  zh: Intel RealSense 深度相机
  ko: Intel RealSense 깊이 칩차
summary:
  en: RGB-D stereo camera widely used for head, wrist, and torso perception in humanoids.
  zh: Intel RealSense 深度相机是人形机器人领域的重要component。以下内容整理自项目 Wiki，供深入查阅。
  ko: 휨로봇의 머리, 손목, 몸통 인식에 널리 사용되는 RGB-D 스테레오 칩차.
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
- camera
- component
- depth
- realsense
- sensor
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_intel.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Intel RealSense Depth Camera
  url: https://www.intelrealsense.com/
  date: '2024'
  accessed_at: '2026-07-02'
---


## 概述
Intel RealSense 深度相机是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 英特尔 / Intel

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 英特尔 |
| **英文名** | Intel |
| **总部** | 美国加利福尼亚州圣克拉拉 |
| **成立时间** | 1968 |
| **官网** | [https://www.intel.com](https://www.intel.com) |
| **供应链环节** | 深度视觉传感器、计算平台、AI 推理硬件 |
| **企业属性** | 上市公司（NASDAQ: INTC）、跨国半导体与计算企业 |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 官网、产品 datasheet、第三方评测 |

### 公司简介

Intel 是全球最大的半导体与计算平台公司之一，其 RealSense 系列深度相机在机器人视觉与学术研究中拥有广泛生态。

Intel RealSense 产品线覆盖立体视觉、结构光、LiDAR 等多种深度感知技术，提供集成 RGB-D、IMU 与视觉处理器的模块化方案。产品被广泛应用于服务机器人、AMR、工业检测、3D 扫描与虚拟现实等领域，并依托开源 librealsense SDK 与 ROS/ROS 2 社区形成完整开发者生态。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| RealSense D400 系列 | 立体深度相机 | D455 / D435i / D405 | 机器人导航、避障、SLAM、3D 扫描 |
| RealSense D500 / 新平台 | 新一代深度感知 | D515 / D555 等 | 增强现实、数字孪生、智能设备 |

### 代表产品

#### Intel RealSense D455

> Intel RealSense D455：请访问 [官方资料](https://www.intel.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 124 mm × 26 mm × 29 mm | 官方 datasheet |
| 重量 | 约 120 g | 第三方评测 |
| 深度技术 | 主动 IR 立体视觉 | 官方 datasheet |
| 深度 FOV | 87° × 58° | 官方 datasheet |
| 深度分辨率/帧率 | 最高 1280×720 @ 90 fps | 官方 datasheet |
| RGB 分辨率 | 最高 1280×800 @ 30 fps | 官方 datasheet |
| 理想量程 | 0.6 m – 6 m | 官方 datasheet |
| 深度精度 | <2% @ 4 m | 官方 datasheet |
| IMU | 集成 6 轴 IMU | 官方 datasheet |
| 接口 | USB-C 3.1 Gen 1 | 官方 datasheet |
| 价格 | 约 USD 299 | 公开市场参考 |

**技术亮点**：95 mm 基线、全局快门、集成 IMU、宽视场角，适合室内外机器人导航与动态场景感知。

**应用场景**：人形机器人头部/躯干视觉、AMR 避障、3D 扫描、工业检测、学术研究。

#### Intel RealSense D435i

> Intel RealSense D435i：请访问 [官方资料](https://www.intel.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 90 mm × 25 mm × 25 mm | 官方 datasheet |
| 重量 | 约 72 g | 第三方评测 |
| 深度技术 | 主动 IR 立体视觉 | 官方 datasheet |
| 深度 FOV | 87° × 58° | 官方 datasheet |
| 深度分辨率/帧率 | 最高 1280×720 @ 90 fps | 官方 datasheet |
| RGB 分辨率 | 最高 1920×1080 @ 30 fps | 官方 datasheet |
| 理想量程 | 0.1 m – 10 m | 官方 datasheet |
| 深度精度 | <2% @ 2 m | 官方 datasheet |
| IMU | 集成 Bosch BMI055 | 官方 datasheet |
| 接口 | USB-C 3.1 | 官方 datasheet |
| 价格 | 约 USD 199 | 公开市场参考 |

**技术亮点**：体积更小、成本更低，集成 IMU，适合对尺寸和预算敏感的机器人平台。

**应用场景**：无人机、小型 AMR、协作机器人视觉、教育与研究。

### 供应链位置

- **上游关键零部件/材料**：CMOS 图像传感器、红外激光器、视觉处理器 ASIC、光学镜片
- **下游客户/应用场景**：服务机器人、AMR/AGV、人形机器人、工业检测、3D 扫描设备、科研教育机构
- **主要竞争对手/对标**：奥比中光、Stereolabs、Azure Kinect、海康机器人、图漾科技

### 知识图谱节点与关系

- 公司实体：`ent_company_intel`
- 产品实体：`ent_component_intel_realsense_d455`
- 产品实体：`ent_component_intel_realsense_d435i`
- 关键关系：
  - `ent_company_intel` -- `manufactures` --> `ent_component_intel_realsense_d455`
  - `ent_company_intel` -- `manufactures` --> `ent_component_intel_realsense_d435i`

### 参考资料

1. [官网](https://www.intel.com)
2. [产品资料与公开报道](https://www.intel.com)
3. [附录 D 产品目录](../index-products.md)

## 参考
- [Intel RealSense Depth Camera](https://www.intelrealsense.com/)
- 项目 Wiki：appendix-d/companies/company_intel.md



