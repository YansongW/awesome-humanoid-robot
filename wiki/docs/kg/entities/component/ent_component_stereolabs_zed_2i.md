---
id: ent_component_stereolabs_zed_2i
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: Stereolabs ZED 2i 立体视觉深度相机
  en: Stereolabs ZED 2i Stereo Depth Camera
sources:
- id: src_stereolabs_zed2i_store
  type: website
- title: Stereolabs ZED 2i Product Page
  url: https://www.stereolabs.com/en-hk/store/products/zed-2i
- id: src_stereolabs_official
  type: website
- title: Stereolabs Official Website
  url: https://www.stereolabs.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-13'
  review_notes: Specifications based on official store and datasheets.
---


# Stereolabs ZED 2i 立体视觉深度相机 / Stereolabs ZED 2i Stereo Depth Camera

## 概述

Stereolabs ZED 2i 是一款面向机器人、无人机与空间分析的工业级立体视觉深度相机，采用双 4 MP RGB 传感器、神经网络深度引擎与多传感器融合（IMU、气压计、磁力计、温度），通过 USB 3.1 Type-C 与主机连接。相机提供 0.3 m 至 20 m 的深度量程（2.1 mm 镜头），可选偏振滤镜与 IP66 防护外壳，适合室内外动态环境下的 SLAM、避障与 3D 测量。

## 工作原理 / 技术架构

ZED 2i 基于被动双目立体视觉原理，结合主动神经网络深度增强：

- **双目成像**：左右 RGB 传感器同步采集场景图像，基线长度约 120 mm；通过立体匹配计算视差图。
- **Neural Depth Engine**：利用深度学习模型对视差进行优化，提高弱纹理、反光及低光照场景的深度质量。
- **多传感器融合**：内置 BMI088/BMM150 等 IMU、气压计、磁力计与温度传感器，支持 6-DoF 视觉惯性 SLAM。
- **ZED SDK**：在主机端（x86/ARM/NVIDIA Jetson）运行，提供深度、点云、位姿、物体检测与骨架追踪算法。

深度估计基本关系：
$$Z = \frac{f \cdot B}{d}$$
其中 $f$ 为焦距（像素），$B$ 为基线（mm），$d$ 为视差（像素）。2.1 mm 镜头对应约 110°(H) × 70°(V) 视场角。

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 传感器 | 双 1/3" 4 MP CMOS，2 µm 像素 | 经销商 / Stereolabs |
| 分辨率模式 | 2K（2208×1242）、1080p、720p、VGA | 经销商 |
| 帧率 | 15 fps @ 2K / 30 fps @ 1080p / 60 fps @ 720p / 100 fps @ VGA | 经销商 |
| 镜头选项 | 2.1 mm / 4 mm | Stereolabs |
| FOV（2.1 mm，H/V/D） | 110° / 70° / 120° | Stereolabs |
| 深度量程（2.1 mm） | 0.3 m – 20 m | Stereolabs |
| 理想量程（2.1 mm） | 0.3 m – 12 m | Stereolabs |
| 深度技术 | Neural Stereo Depth Sensing | Stereolabs |
| 深度 FPS | 最高 100 Hz | Stereolabs |
| IMU | 加速度计 + 陀螺仪，400 Hz | Stereolabs |
| 其他传感器 | 气压计、磁力计、温度 | Stereolabs |
| 位姿更新率 | 最高 100 Hz | Stereolabs |
| 定位漂移（平移/旋转） | 0.35% / 0.005°/m | Stereolabs |
| 接口 | USB 3.1 Type-C | Stereolabs |
| 防护等级 | IP66（可选外壳） | Stereolabs |
| 尺寸 | 175.25 × 30.25 × 43.10 mm | 官方 datasheet |
| 重量 | 230 g | 官方 datasheet |
| 工作温度 | 0 °C – 45 °C | 官方 |
| 价格 | 约 USD 499 起 | Stereolabs 商店 |

## 应用场景

- **AMR/人形机器人视觉导航**：户外/室内 SLAM、路径规划与避障。
- **无人机空间感知**：长距离深度与前向障碍物检测。
- **工业检测与测量**：3D 尺寸测量、体积估算与缺陷检测。
- **混合现实与数字孪生**：大空间实时 3D 重建。

## 供应链关系

- **制造商**：Stereolabs（ent_company_stereolabs），2026 年已被 Ouster 收购。
- **上游关键物料**：CMOS 图像传感器、AI 加速芯片、光学镜头、USB 控制器、IMU。
- **下游整机集成**：AMR、无人机、人形机器人、自动驾驶原型、AR/VR 平台。
- **竞争/对标**：Intel RealSense D455、奥比中光、图漾科技、海康机器人、Ouster。

## 来源与验证

- Stereolabs ZED 2i 产品页：https://www.stereolabs.com/en-hk/store/products/zed-2i
- Stereolabs 官网：https://www.stereolabs.com