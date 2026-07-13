---
id: ent_component_orbbec_gemini335
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 奥比中光 Gemini 335
  en: Orbbec Gemini 335
status: active
sources:
- id: src_ent_component_orbbec_gemini335
  type: website
  url: ''
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 奥比中光 Gemini 335 / Orbbec Gemini 335

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [奥比中光 / Orbbec](../../../appendices/appendix-d/companies/company_orbbec.md) |
| **产品类别** | 双目深度相机 |
| **发布时间** | 2024 年 4 月 |
| **状态** | 量产/商用 |
| **官网/来源** | [Orbbec Gemini 335 产品页](https://www.orbbec.com/products/stereo-vision-camera/gemini-335/) |

## 产品概述

奥比中光 Gemini 335 是 Gemini 330 系列双目 3D 相机的标准版，面向室内与半室外机器人场景设计。Gemini 335 搭载奥比中光自研 MX6800 深度引擎 ASIC，采用主动 + 被动融合立体视觉技术，可在强光直射、暗光、白墙等弱纹理环境下稳定输出高质量深度数据。

Gemini 335 机身小巧（90×25×30 mm，97 g），支持 USB 3.0 Type-C 接口与 UVC 驱动，便于快速集成到 AMR、人形机器人、机械臂、无人机等设备。其深度对角 FOV 超过 100°，最大测量范围超过 10 m，并集成 IMU 与多机同步功能，是机器人 3D 视觉的主流选择之一。

## 产品图片

> Orbbec Gemini 335：请访问 [官方资料](https://www.orbbec.com/products/stereo-vision-camera/gemini-335/) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 90 mm × 25 mm × 30 mm | Orbbec Store |
| 重量 | 97 g | Orbbec Store |
| 深度技术 | 主动 + 被动立体视觉 | Orbbec 官网 |
| 深度分辨率 | 最高 1280×800 @ 30 fps | Orbbec Store |
| RGB 分辨率 | 最高 1920×1080 @ 30 fps | Orbbec Store |
| 深度 FOV | 90° × 65°（对角 >100°） | Orbbec Store |
| 深度量程 | 0.1 m – 20 m+（理想 0.26–3.0 m） | Orbbec Store |
| 空间精度 | ≤1.5% @ 2 m | Orbbec Store |
| 接口 | USB 3.0 Type-C | Orbbec Store |
| 功耗 | <3 W | Orbbec Store |
| 防护等级 | IP5X | Orbbec Store |
| 价格 | 约 CNY 1,950 | 经销商参考 |

## 供应链位置

- **制造商**：[奥比中光 / Orbbec](../../../appendices/appendix-d/companies/company_orbbec.md)
- **核心零部件/技术来源**：自研 MX6800 深度引擎 ASIC、光学模组、深度算法；图像传感器、激光投射器外购。
- **下游应用/客户**：AMR、人形机器人、协作机械臂、无人机、3D 扫描与人体重建。

## 知识图谱节点与关系

- 零部件实体：`ent_component_orbbec_gemini_335`
- 制造商实体：`ent_company_orbbec`
- 关键关系：
  - `rel_ent_company_orbbec_manufactures_ent_component_orbbec_gemini_335`（`ent_company_orbbec` → `manufactures` → `ent_component_orbbec_gemini_335`）

## 应用场景

- **AMR/AGV 导航避障**：室内外大 FOV 深度感知与动态障碍物检测。
- **人形机器人视觉**：头部或躯干视觉模块，支持 VSLAM、手势与物体识别。
- **协作机械臂**：箱拣选、零件定位、尺寸测量与抓取引导。
- **无人机与户外设备**：强光下可用的深度数据辅助低空避障与地形测绘。

## 竞争对比

| 对比项 | 奥比中光 Gemini 335 | Intel RealSense D435i | Stereolabs ZED 2i |
|--------|---------------------|-----------------------|-------------------|
| 深度技术 | 主动+被动双目 | 主动红外立体视觉 | 被动双目 |
| 量程 | 0.1–20 m+ | 0.3–10 m | 0.3–20 m |
| 功耗 | <3 W | 约 3 W | 约 4 W |
| 核心优势 | 户外强光、MX6800 ASIC、低延迟 | 生态成熟、ROS 支持好 | 高精度与 3D 重建 |

## 参考资料

1. [Orbbec Gemini 335 产品页](https://www.orbbec.com/products/stereo-vision-camera/gemini-335/)
2. [Orbbec Store – Gemini 335](https://store.orbbec.com/products/gemini-335)
3. [奥比中光中文官网 – Gemini 330 系列发布](https://www.orbbec.com.cn/index/News/info.html?cate=31&id=273)
4. [CSDN – ROS2 + Gemini 335L 使用](https://blog.csdn.net/imwaters/article/details/156425172)