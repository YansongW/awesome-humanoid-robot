---
id: ent_component_intel_realsense_d455
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: Intel RealSense D455 深度相机
  en: Intel RealSense D455 Depth Camera
sources:
- id: src_intel_d455_datasheet
  type: datasheet
- title: Intel RealSense D400 Series Product Family Datasheet
  url: https://cdrdv2-public.intel.com/841984/Intel-RealSense-D400-Series-Datasheet.pdf
- id: src_intel_d455_framos
  type: website
- title: RealSense Depth Camera D455 (camera only) - Framos
  url: https://framos.com/products/3d/3d-cameras/depth-camera-d455-bulk-24722/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from Intel D400 series datasheet and verified distributor
    listings; missing values marked as 未公开.
---


# Intel RealSense D455 深度相机 / Intel RealSense D455 Depth Camera

## 概述

Intel RealSense D455 是 Intel RealSense D400 系列中的长距离立体深度相机，面向机器人、无人机、工业检测、3D 扫描及增强现实等应用。该相机基于主动红外（Active IR）立体视觉原理，集成 RGB 传感器、全局快门深度传感器以及 6 轴 IMU，通过 USB-C 接口输出同步的深度、RGB 与惯性数据。

## 工作原理与技术架构

D455 采用双目立体视觉深度重建架构：

1. **主动红外立体成像**：左右红外相机形成基线 $B=95~\text{mm}$，红外投射器投射结构化纹理，提升低纹理场景的匹配成功率。
2. **深度计算**：Intel RealSense Vision Processor D4 在相机端完成立体匹配，输出深度图。深度分辨率最高 $1280 \times 720$，帧率最高 90 fps。
3. **全局快门 RGB 与深度同步**：RGB 传感器采用全局快门，与深度传感器视场匹配，便于 RGB-D 对齐与三维重建。
4. **IMU 融合**：集成 Bosch BMI055/BMI085 6 轴 IMU，加速度计量程 ±4 g，陀螺仪量程 ±1000 °/s，时间戳精度约 50 μs，支持视觉-惯性融合 SLAM。
5. **SDK 与生态**：通过 Intel RealSense SDK 2.0（开源）及 ROS/ROS 2 节点，实现标定、对齐、点云生成与算法部署。

深度精度在 4 m 处优于 2%，可表达为：

$$
\Delta Z \approx \frac{Z^2}{B \cdot f} \cdot \Delta d
$$

其中 $Z$ 为物距，$B$ 为基线，$f$ 为焦距，$\Delta d$ 为视差误差。更长的 95 mm 基线相较 D435i 的 50 mm 基线显著改善了远距离深度精度。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 124 mm × 26 mm × 29 mm | Intel datasheet / Framos |
| 重量 | 约 120 g | 第三方评测 |
| 深度技术 | 主动 IR 立体视觉 | Intel datasheet |
| 深度基线 | 95 mm | Intel datasheet |
| 深度 FOV（H × V） | 87° × 58°（±3°）| Intel datasheet |
| 深度分辨率/帧率 | 最高 1280 × 720 @ 90 fps | Intel datasheet |
| RGB 分辨率/帧率 | 最高 1280 × 800 @ 30 fps；最高 90 fps（较低分辨率）| Intel datasheet |
| RGB FOV（H × V） | 90° × 65°（近似）| Intel datasheet |
| 理想量程 | 0.6 m – 6 m | Intel datasheet |
| 最小深度距离 | 约 0.4 m – 0.52 m |  distributor specs |
| 深度精度 | <2% @ 4 m | Intel datasheet |
| IMU | 6 轴（BMI055 / BMI085）| Intel datasheet |
| 快门类型 | 全局快门（深度 + RGB）| Intel datasheet |
| 接口 | USB-C 3.1 Gen 1 | Intel datasheet |
| 安装接口 | 2×M3 × 0.5 + 1×1/4-20 UNC | Intel datasheet |
| 使用环境 | 室内/室外 | Intel datasheet |
| 价格 | 约 USD 299 – 399 | 公开市场参考 |

## 应用场景

- **人形机器人视觉**：部署于头部或躯干，用于导航、避障与目标识别。
- **AMR/AGV**：长距离深度感知支持动态路径规划与障碍物检测。
- **无人机**：全局快门与 IMU 融合提升高速运动下的 SLAM 稳定性。
- **工业检测与 3D 扫描**：高精度点云重建用于尺寸测量与缺陷检测。
- **学术研究**：依托开源 SDK 与 ROS 生态，广泛应用于计算机视觉与机器人算法验证。

## 供应链关系

- **上游**：CMOS 红外图像传感器、RGB 传感器、红外激光投射器、Vision Processor D4 ASIC、光学镜头、IMU 芯片、USB-C 连接器。
- **制造商**：Intel 通过关系 `ent_company_intel -- manufactures --> ent_component_intel_realsense_d455` 记录于知识图谱。
- **下游**：服务机器人、AMR/AGV、人形机器人、工业检测系统、3D 扫描设备、科研教育机构。主要对标奥比中光、Stereolabs、Azure Kinect 等方案。

## 来源与验证

核心参数源自 Intel D400 系列官方 datasheet（修订版 013/014）及 Framos、Mouser、Generation Robots 等授权分销商页面。D455 与 D435i 的基线、FOV、IMU 配置差异已在官方 SKU 属性表（Table 3-49）中明确。价格数据来自公开市场参考，未公开项已标注。