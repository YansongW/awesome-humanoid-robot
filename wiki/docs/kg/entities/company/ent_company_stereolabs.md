---
id: ent_company_stereolabs
type: company
'title:': Stereolabs / Stereolabs
domain: 02_components
theoretical_depth: system
aliases:
- Stereolabs
- Stereolabs
status: active
created_at: 2024-01-15 00:00:00+00:00
updated_at: 2026-07-01 00:00:00+00:00
sources:
- id: ent_company_stereolabs_official
  type: website
  url: https://www.stereolabs.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-01 00:00:00+00:00
  review_notes: Data sourced from official website and public reports; missing specs
    marked as 未公开.
---





# stereolabs

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Stereolabs |
| **英文名** | Stereolabs |
| **总部** | 法国巴黎 / 美国旧金山 |
| **成立时间** | 2010 |
| **官网** | [https://www.stereolabs.com](https://www.stereolabs.com) |
| **供应链环节** | 立体视觉深度相机、AI 感知软件、边缘计算 |
| **企业属性** | 私有公司、AI 视觉与深度感知技术公司 |
| **母公司/所属集团** | 2026 年被 Ouster 收购（ wholly owned subsidiary ） |
| **数据来源** | 官网、产品页、Ouster 收购公告 |

## 公司简介

Stereolabs 是全球领先的立体视觉与 AI 感知公司，ZED 系列深度相机在机器人、无人机与空间分析领域应用广泛。

Stereolabs 提供 ZED 系列立体深度相机及 ZED SDK、AI 感知算法和边缘计算平台。其神经网络深度引擎可在无主动光源条件下实现高精度深度估计，产品支持 NVIDIA Jetson 等边缘平台，广泛应用于自主导航、3D 测量、混合现实与机器人视觉。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| ZED 2i | 工业级立体相机 | ZED 2i | 机器人导航、户外感知、空间分析 |
| ZED X | GMSL2 车规/工业相机 | ZED X | 自动驾驶、AMR、工业视觉 |
| ZED Box | 边缘 AI 计算 | ZED Box Mini | 多相机融合、端侧感知 |

## 代表产品

### Stereolabs ZED 2i

> Stereolabs ZED 2i：请访问 [官方资料](https://www.stereolabs.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 175.25 mm × 30.25 mm × 43.10 mm | 官方 datasheet |
| 重量 | 230 g | 官方 datasheet |
| 深度技术 | 神经网络立体深度 | 官方 datasheet |
| FOV（2.1 mm 镜头） | 110°(H) × 70°(V) × 120°(D) | 官方 datasheet |
| 视频分辨率 | 2K @ 15 fps / 1080p @ 30 fps / 720p @ 60 fps | 官方 datasheet |
| 深度量程 | 0.3 m – 20 m（2.1 mm 镜头） | 官方 datasheet |
| 运动传感器 | 加速度计、陀螺仪、气压计、磁力计、温度 | 官方 datasheet |
| 防护等级 | IP66（选配） | 官方 datasheet |
| 接口 | USB 3.1 Type-C | 官方 datasheet |
| 价格 | 约 USD 499 起 | 官方商店 |

**技术亮点**：神经网络深度感知、宽视场角、IP66 防护、集成多传感器，适合室内外机器人与动态场景。

**应用场景**：人形机器人/AMR 视觉、户外测绘、空间分析、混合现实、工业检测。

### Stereolabs ZED X

> Stereolabs ZED X：请访问 [官方资料](https://www.stereolabs.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 164 mm × 32 mm × 37 mm | 官方 datasheet |
| 重量 | 240 g | 官方 datasheet |
| 深度技术 | Neural Depth Engine 2 + 全局快门 | 官方 datasheet |
| 分辨率 | 1920×1200 @ 60 fps / 960×600 @ 120 fps | 官方 datasheet |
| FOV | 110°(H) × 80°(V) × 120°(D)（2.2 mm） | 官方 datasheet |
| 接口 | GMSL2（可达 15 m） | 官方 datasheet |
| 防护等级 | IP67 | 官方 datasheet |
| IMU | 16-bit 三轴加速度计/陀螺仪 | 官方 datasheet |
| 工作温度 | -20°C ~ +55°C | 官方 datasheet |
| 价格 | 未公开 | 未公开 |

**技术亮点**：GMSL2 长距离传输、全局快门、IP67 防护、多相机硬件同步，面向车规与工业环境。

**应用场景**：自动驾驶、人形机器人、农业机器人、数字孪生、高精度 SLAM。

## 供应链位置

- **上游关键零部件/材料**：CMOS 图像传感器、AI 加速芯片、光学镜头、GMSL2 接口芯片
- **下游客户/应用场景**：AMR、无人机、人形机器人、自动驾驶、AR/VR、空间分析平台
- **主要竞争对手/对标**：Intel RealSense、奥比中光、图漾科技、海康机器人、Ouster

## 知识图谱节点与关系

- 公司实体：`ent_company_stereolabs`
- 产品实体：`ent_component_stereolabs_zed_2i`
- 产品实体：`ent_component_stereolabs_zed_x`
- 关键关系：
  - `ent_company_stereolabs` -- `manufactures` --> `ent_component_stereolabs_zed_2i`
  - `ent_company_stereolabs` -- `manufactures` --> `ent_component_stereolabs_zed_x`

## 参考资料

1. [官网](https://www.stereolabs.com)
2. [产品资料与公开报道](https://www.stereolabs.com)
3. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)