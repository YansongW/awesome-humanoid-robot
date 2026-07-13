---
id: ent_component_orbbec_gemini_335lg
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 奥比中光 Gemini 335Lg 双目深度相机
  en: Orbbec Gemini 335Lg Stereo Depth Camera
status: active
sources:
- id: src_orbbec_gemini335lg
  type: website
- title: Orbbec Gemini 335Lg Product Page
  url: https://www.orbbec.com/gemini-335lg/
- id: src_hackster_gemini335lg
  type: website
- title: Hackster – Orbbec Gemini 335Lg Depth Camera
  url: https://www.hackster.io/news/orbbec-unveils-the-robust-fakra-connectable-gemini-335lg-depth-camera-for-autonomous-robots-and-more-e23d922b5158
- id: src_openelab_gemini335lg
  type: website
- title: OpenELAB – Orbbec Gemini 335Lg vs RealSense Guide
  url: https://openelab.io/blogs/learn/orbbec-gemini-335lg-vs-realsense-d455f-d456
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official product page and verified distributor/wiki
    pages; missing values marked as 未公开.
---


# 奥比中光 Gemini 335Lg 双目深度相机 / Orbbec Gemini 335Lg Stereo Depth Camera

## 概述

Gemini 335Lg 是奥比中光（Orbbec）Gemini 330 系列中的 GMSL2/FAKRA 版本双目立体深度相机，基于主动+被动立体视觉技术，搭载自研 MX6800 深度引擎 ASIC。该相机在 Gemini 335L 基础上新增 GMSL2 高速串行链路与 FAKRA 连接器，支持长达 15 m 的线缆传输，并具备 IP65 防护等级，适用于移动机器人、机械臂及户外/工业环境。

## 工作原理 / 技术架构

Gemini 335Lg 通过左右目相机获取同一场景的两幅图像，利用三角测量计算像素视差 $d$。对于焦距 $f$、基线 $B$ 的立体系统，空间点深度 $Z$ 为

$$
Z = \frac{f \cdot B}{d}
$$

其中视差 $d = x_L - x_R$ 为左右图像中对应像点的水平坐标差。深度引擎 ASIC（MX6800）在相机端完成深度图计算，并通过 GMSL2 或 USB 3 输出深度与 RGB 对齐后的数据流。

空间精度（相对误差）随距离增加而下降。官方标称在 1280×800 分辨率、2 m 距离、90%×90% ROI 条件下空间精度 ≤0.8%；4 m 距离、80%×80% ROI 条件下 ≤1.6%。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 深度技术 | 主动 + 被动立体视觉 | Orbbec 官方产品页 |
| 深度引擎 | MX6800 ASIC | Orbbec 官方产品页 |
| 深度分辨率/帧率 | 1280×800 @ 30 fps / 848×480 @ 60 fps | Orbbec 官方产品页 |
| RGB 分辨率/帧率 | 1280×800 @ 60 fps（YUYV） | Orbbec / OpenELAB |
| 深度 FOV | 90° × 65°（典型） | Orbbec 官方产品页 |
| RGB FOV | 94° × 68°（典型） | OpenELAB |
| 基线 | 95 mm | OpenELAB |
| 深度量程 | 0.17 m – 20 m+（理论最大 65 m） | Orbbec / OpenELAB |
| 空间精度 | ≤0.8% @ 2 m；≤1.6% @ 4 m | Orbbec / OpenELAB |
| 接口 | GMSL2 FAKRA + USB 3 Type-C | Orbbec 官方产品页 |
| GMSL2 传输距离 | 最长 15 m | Orbbec 官方产品页 |
| USB 传输距离 | 最长 3 m | Orbbec 官方产品页 |
| 防护等级 | IP65 | Orbbec 官方产品页 |
| 尺寸 | 124 × 29 × 36 mm | 公司 Wiki / Seeed |
| 重量 | 164 ± 3 g | 公司 Wiki / Seeed |
| 多机同步 | 支持最多 16 台同步 | Orbbec 官方产品页 |
| IMU / 温度传感器 | 支持 | Orbbec / OpenELAB |
| 典型功耗 | 未公开 | - |

## 应用场景

- **人形机器人视觉**：头部/躯干深度感知、障碍物检测、抓取定位。
- **AMR/AGV 导航避障**：长距离、高帧率深度图支持 SLAM 与路径规划。
- **协作机器人抓取**：目标识别、位姿估计与手眼协调。
- **户外巡检与测绘**：IP65 防护与 GMSL2 长距离传输适应恶劣环境。
- **工业检测**：三维测量、缺陷检测、体积估算。

## 供应链关系

- **上游**：CMOS 图像传感器、VCSEL/激光器、MX6800 深度引擎 ASIC、光学镜片、ISP 算法。
- **制造商**：`ent_company_orbbec` -- `manufactures` --> `ent_component_orbbec_gemini_335lg`。
- **下游客户**：服务机器人、AMR/AGV、人形机器人（如优必选 Walker 系列）、无人机、3D 扫描设备商。
- **生态支持**：官方 SDK 支持 ROS1/ROS2、NVIDIA Isaac ROS、NVIDIA Jetson AGX Orin/Orin NX/Xavier。
- **竞争对手/对标**：Intel RealSense D455F/D456、Stereolabs ZED、图漾科技、海康机器人。

## 来源与验证

1. Orbbec Gemini 335Lg 产品页：https://www.orbbec.com/gemini-335lg/
2. 附录 D 企业 Wiki：company_orbbec.md
3. Hackster 报道：https://www.hackster.io/news/orbbec-unveils-the-robust-fakra-connectable-gemini-335lg-depth-camera-for-autonomous-robots-and-more-e23d922b5158
4. OpenELAB 技术选型指南：https://openelab.io/blogs/learn/orbbec-gemini-335lg-vs-realsense-d455f-d456