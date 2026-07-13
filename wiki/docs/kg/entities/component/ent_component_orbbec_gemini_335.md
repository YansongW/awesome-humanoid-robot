---
id: ent_component_orbbec_gemini_335
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 奥比中光 Gemini 335 深度相机
  en: Orbbec Gemini 335 Depth Camera
sources:
- id: src_orbbec_official
  type: website
- title: '"奥比中光官网"'
  url: https://www.orbbec.com
- id: src_orbbec_datasheet
  type: website
- title: '"Orbbec Gemini 330 Series Datasheet"'
  url: https://d1cd332k3pgc17.cloudfront.net/wp-content/uploads/2024/06/Orbbec-Gemini-330-Series-Datasheet-v1.1-2.pdf
- id: src_sodavision_gemini335
  type: website
- title: '"Orbbec Gemini 335 产品页"'
  url: https://www.sodavision.com/product/orbbec-gemini-335/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# 奥比中光 Gemini 335 深度相机 / Orbbec Gemini 335 Depth Camera

## 概述

Gemini 335 是奥比中光 Gemini 330 系列双目立体深度相机，融合主动与被动立体视觉技术，可在室内、室外及低光照环境下工作。相机内置 Orbbec MX6800 深度引擎 ASIC，实现硬件 D2C（深度到彩色对齐）、多机同步与 IMU 数据输出，广泛应用于机器人导航避障、人形机器人视觉、AMR 与 3D 扫描。

## 工作原理 / 技术架构

Gemini 335 采用左右红外/彩色相机组成双目系统，基线 50 mm，通过结构光投射器增强纹理，结合被动立体匹配计算视差图，再经三角测量得到深度：

$$Z = \frac{f \cdot B}{d}$$

其中 $Z$ 为深度，$f$ 为焦距（像素），$B$ 为基线，$d$ 为视差。相机输出 1280×800 深度图与 1920×1080 RGB 图，深度视场角 90°(H) × 65°(V)，空间精度 ≤1.5% @ 2 m。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 尺寸 | 90 mm × 25 mm × 30 mm | 官方 datasheet |
| 重量 | 97 g | 官方 datasheet |
| 深度技术 | 主动 + 被动立体视觉 | 官方 datasheet |
| 基线 | 50 mm | 官方 datasheet |
| 深度 FOV | 90°(H) × 65°(V) | 官方 datasheet |
| 深度分辨率/帧率 | 最高 1280×800 @ 30 fps | 官方 datasheet |
| RGB 分辨率/帧率 | 最高 1920×1080 @ 30 fps | 官方 datasheet |
| 深度量程 | 0.1 m – 10 m（理想 0.26 m – 3 m） | 官方 datasheet |
| 空间精度 | ≤ 1.5% @ 2 m | 官方 datasheet |
| 平均功耗 | < 3.0 W | 官方 datasheet |
| 数据/供电 | USB 3.0 Type-C | 官方 datasheet |
| IMU | 支持 | 官方 datasheet |
| 防护等级 | IP5X | 官方 datasheet |

## 应用场景

人形机器人视觉、AMR/AGV 导航避障、协作机器人抓取、无人机、3D 扫描、智能支付终端。

## 供应链关系

奥比中光（`ent_company_orbbec`）自研 MX6800 ASIC、光学系统与算法；传感器上游包括 CMOS、VCSEL、光学镜片；下游供应优必选 Walker 系列、服务机器人与 AMR 厂商，与 Intel RealSense、Stereolabs、图漾科技等竞争。

## 来源与验证

- 奥比中光官网：https://www.orbbec.com
- Gemini 330 系列 datasheet：https://d1cd332k3pgc17.cloudfront.net/wp-content/uploads/2024/06/Orbbec-Gemini-330-Series-Datasheet-v1.1-2.pdf
- Gemini 335 产品页：https://www.sodavision.com/product/orbbec-gemini-335/