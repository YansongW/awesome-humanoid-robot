---
id: ent_company_orbbec
type: company
'title:': 奥比中光 / Orbbec
domain: 02_components
theoretical_depth: system
aliases:
- 奥比中光
- Orbbec
status: active
created_at: 2024-01-15 00:00:00+00:00
updated_at: 2026-07-01 00:00:00+00:00
sources:
- id: ent_company_orbbec_official
  type: website
  url: https://www.orbbec.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-01 00:00:00+00:00
  review_notes: Data sourced from official website and public reports; missing specs
    marked as 未公开.
---





# orbbec

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 奥比中光 |
| **英文名** | Orbbec |
| **总部** | 中国深圳 |
| **成立时间** | 2013 |
| **官网** | [https://www.orbbec.com](https://www.orbbec.com) |
| **供应链环节** | 3D 视觉传感器、深度相机、机器人视觉模组 |
| **企业属性** | 上市公司（688322.SH）、中国 3D 视觉第一股 |
| **母公司/所属集团** | 独立上市 |
| **数据来源** | 官网、财报、公开报道 |

## 公司简介

奥比中光是中国 3D 视觉感知龙头，提供结构光、双目、iToF/dToF、LiDAR 等全技术路线 3D 视觉传感器。

奥比中光拥有从深度引擎 ASIC、光学系统到算法与量产的全栈能力，产品覆盖消费级与工业级 3D 相机。其 Gemini 系列双目深度相机在机器人、AMR、人形机器人视觉领域应用广泛，并与优必选、英伟达 Jetson 生态等建立合作。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Gemini 330 系列 | 双目立体深度相机 | Gemini 335 / 335L / 336 | 服务机器人、AMR、人形机器人 |
| Astra 系列 | 结构光深度相机 | Astra / Astra Pro | 人脸识别、体感交互、智能电视 |
| Femto / Dabai 系列 | iToF / dToF | Femto Bolt / Dabai | 3D 扫描、医疗、工业测量 |

## 代表产品

### 奥比中光 Gemini 335

> 奥比中光 Gemini 335：请访问 [官方资料](https://www.orbbec.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 90 mm × 25 mm × 30 mm | 官方 datasheet |
| 重量 | 97 g | 官方 datasheet |
| 深度技术 | 主动 + 被动立体视觉 | 官方 datasheet |
| 深度 FOV | 90° × 65° | 官方 datasheet |
| 深度分辨率/帧率 | 最高 1280×800 @ 30 fps / 640×400 @ 60 fps | 官方 datasheet |
| RGB 分辨率 | 最高 1920×1080 @ 30 fps | 官方 datasheet |
| 深度量程 | 0.1 m – 20 m+（理想 0.26 m – 3.0 m） | 官方 datasheet |
| 空间精度 | ≤1.5% @ 2 m | 官方 datasheet |
| IMU | 支持 | 官方 datasheet |
| 接口 | USB 3.0 Type-C | 官方 datasheet |
| 价格 | 约 CNY 1,950 | 公开市场参考 |

**技术亮点**：全场景室内外可用、MX6800 深度引擎 ASIC、硬件 D2C、IP5X 防尘、支持多机同步。

**应用场景**：人形机器人视觉、AMR 导航避障、协作机器人抓取、无人机、3D 扫描。

### 奥比中光 Gemini 335Lg

> 奥比中光 Gemini 335Lg：请访问 [官方资料](https://www.orbbec.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 124 mm × 29 mm × 36 mm | Seeed Studio Wiki |
| 重量 | 164 g ± 3 g | Seeed Studio Wiki |
| 深度技术 | 主动 + 被动立体视觉 | 官方 datasheet |
| 深度 FOV | 90° × 65° | 官方 datasheet |
| 深度分辨率/帧率 | 1280×800 @ 30 fps / 848×480 @ 60 fps | 官方 datasheet |
| RGB 分辨率 | 1280×800 @ 60 fps | 官方 datasheet |
| 空间精度 | ≤0.8% @ 2 m；≤1.6% @ 4 m | 官方 datasheet |
| 接口 | GMSL2 FAKRA + USB 3 | 官方 datasheet |
| 防护等级 | IP65 | 官方 datasheet |
| 价格 | 未公开 | 未公开 |

**技术亮点**：GMSL2 长距离传输、全局快门 RGB、IP65 防护，适合车规与户外机器人。

**应用场景**：人形机器人、自动驾驶、AMR、工业检测、户外测绘。

## 供应链位置

- **上游关键零部件/材料**：CMOS 图像传感器、VCSEL/激光器、深度引擎 ASIC、光学镜片、ISP 算法
- **下游客户/应用场景**：服务机器人、AMR/AGV、人形机器人（如优必选 Walker 系列）、智能电视、支付终端、3D 扫描
- **主要竞争对手/对标**：Intel RealSense、Stereolabs、图漾科技、海康机器人、微软 Azure Kinect

## 知识图谱节点与关系

- 公司实体：`ent_company_orbbec`
- 产品实体：`ent_component_orbbec_gemini_335`
- 产品实体：`ent_component_orbbec_gemini_335lg`
- 关键关系：
  - `ent_company_orbbec` -- `manufactures` --> `ent_component_orbbec_gemini_335`
  - `ent_company_orbbec` -- `manufactures` --> `ent_component_orbbec_gemini_335lg`
  - `ent_company_orbbec` -- `supplies` --> `ent_company_ubtech` (优必选 Walker S/X 搭载奥比中光 3D 视觉传感器)

## 参考资料

1. [官网](https://www.orbbec.com)
2. [产品资料与公开报道](https://www.orbbec.com)
3. [附录 D 产品目录](../../../appendices/appendix-d/index-products.md)