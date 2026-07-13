---
id: ent_component_intel_realsense_d435i
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: Intel RealSense D435i 深度相机
  en: Intel RealSense D435i Depth Camera
sources:
- id: src_intel_d435i_datasheet
  type: datasheet
- title: Intel RealSense D400 Series Product Family Datasheet
  url: https://cdrdv2-public.intel.com/841984/Intel-RealSense-D400-Series-Datasheet.pdf
- id: src_intel_d435i_openelab
  type: website
- title: Intel RealSense D435i Depth Camera Guide
  url: https://openelab.io/blogs/learn/intel-realsense-d435i-depth-camera-guide-complete-overview
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from Intel D400 series datasheet and verified distributor
    listings; missing values marked as 未公开.
---


# Intel RealSense D435i 深度相机 / Intel RealSense D435i Depth Camera

## 概述

Intel RealSense D435i 是 Intel RealSense D400 系列中集成惯性测量单元（IMU）的紧凑型立体深度相机。该产品在 D435 的基础上增加 6 轴 IMU，提供时间同步的深度与惯性数据流，适用于机器人 SLAM、无人机导航、3D 扫描及具身智能研究等场景。其较小的体积与重量使其成为空间受限平台的常见选择。

## 工作原理与技术架构

D435i 采用主动红外立体视觉架构：

1. **红外立体匹配**：左右红外相机基线 $B=50~\text{mm}$，配合红外投射器增强低纹理环境匹配；Vision Processor D4 在相机端完成实时立体匹配。
2. **全局快门深度传感器**：深度传感器采用全局快门，可在相机或目标快速运动时避免卷帘畸变。
3. **RGB 与深度对齐**：RGB 传感器为 2 MP 传感器，支持 1920 × 1080 @ 30 fps，视场与深度图可通过 SDK 进行外参对齐。
4. **IMU 数据融合**：集成 Bosch BMI055（早期批次）或 BMI085（后期批次）6 轴 IMU，加速度计量程 ±4 g，陀螺仪量程 ±1000 °/s；IMU 数据与深度数据通过时间戳对齐，便于 VIO/SLAM 算法使用。
5. **SDK 与生态**：Intel RealSense SDK 2.0 提供 Windows、Linux、Android、macOS 支持，并包含 ROS/ROS 2 封装。

深度误差模型与双目立体视觉一致：

$$
\Delta Z \approx \frac{Z^2}{B \cdot f} \cdot \Delta d
$$

其中基线 $B=50~\text{mm}$，因此 D435i 在同等焦距与视差精度下，远距离深度误差大于 D455，但近距离体积更小、成本更低。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 90 mm × 25 mm × 25 mm | Intel datasheet |
| 重量 | 约 72 g | 第三方评测 |
| 深度技术 | 主动 IR 立体视觉 | Intel datasheet |
| 深度基线 | 50 mm | Intel datasheet |
| 深度 FOV（H × V） | 87° × 58° | Intel datasheet |
| 深度分辨率/帧率 | 最高 1280 × 720 @ 90 fps | Intel datasheet |
| RGB 分辨率/帧率 | 最高 1920 × 1080 @ 30 fps | Intel datasheet |
| RGB FOV（H × V） | 69° × 42° | Intel datasheet |
| 理想量程 | 0.3 m – 3 m | Intel / distributor |
| 最小深度距离 | 约 0.28 m | distributor specs |
| 深度精度 | <2% @ 2 m | Intel datasheet |
| IMU | 6 轴（BMI055 / BMI085）| Intel datasheet |
| 深度快门 | 全局快门 | Intel datasheet |
| RGB 快门 | 卷帘快门 | Intel datasheet |
| 接口 | USB-C 3.1 Gen 1 | Intel datasheet |
| 安装接口 | 2×M3 + 1×1/4-20 UNC | Intel datasheet |
| 使用环境 | 室内/室外 | Intel datasheet |
| 价格 | 约 USD 199 – 489 | 公开市场参考 |

## 应用场景

- **小型移动机器人**：无人机、小型 AMR、家庭服务机器人等对尺寸与重量敏感的平台。
- **人形机器人视觉**：作为腕部或头部近距离精细操作相机。
- **SLAM 与 VIO 研究**：IMU 与深度数据同步，支持视觉-惯性 SLAM 算法开发。
- **3D 扫描与数字孪生**：紧凑体积便于手持扫描与快速部署。
- **教育科研**：依托开源 SDK 与 ROS 生态，广泛用于机器人课程与算法验证。

## 供应链关系

- **上游**：CMOS 红外图像传感器、RGB 传感器、红外激光投射器、Vision Processor D4 ASIC、光学镜头、IMU 芯片、USB-C 连接器。
- **制造商**：Intel 通过关系 `ent_company_intel -- manufactures --> ent_component_intel_realsense_d435i` 记录于知识图谱。
- **下游**：无人机、小型 AMR、协作机器人、人形机器人、3D 扫描设备、教育科研机构。与 D455 形成互补：D435i 侧重紧凑与近距离，D455 侧重长距离与全局快门 RGB。

## 来源与验证

核心参数源自 Intel D400 系列官方 datasheet（Table 3-49、IMU Specifications 等章节）及 OpenELAB、Kempit、DigiKey 等公开资料。BMI055 与 BMI085 两种 IMU 型号的批次差异在官方物料编码表中有明确记录。价格数据来自公开市场参考，未公开项已标注。