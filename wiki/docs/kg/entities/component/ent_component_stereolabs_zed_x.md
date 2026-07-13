---
id: ent_component_stereolabs_zed_x
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: Stereolabs ZED X GMSL2 工业立体相机
  en: Stereolabs ZED X GMSL2 Industrial Stereo Camera
sources:
- id: src_stereolabs_zedx_web
  type: website
- title: Stereolabs ZED X Product Page
  url: https://www.stereolabs.com/en-be/products/zed-x
- id: src_stereolabs_zedx_mouser
  type: datasheet
- title: StereoLabs ZED X Stereo Cameras - Mouser
  url: https://www.mouser.vn/new/stereolabs/stereolabs-zed-x-stereo-camera/
- id: src_generationrobots_zedx
  type: product_page
- title: ZED X Mini Depth Camera - Generation Robots
  url: https://www.generationrobots.com/en/404308-zed-x-mini-depth-camera.html
verification:
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-13'
---


# Stereolabs ZED X GMSL2 工业立体相机 / Stereolabs ZED X GMSL2 Industrial Stereo Camera

## 概述

Stereolabs ZED X 是面向机器人、自动驾驶与工业自动化的 GMSL2 工业立体相机，采用双 2.3 MP 全局快门彩色传感器、Neural Depth Engine 2 与抗振工业 IMU，通过 FAKRA-Z GMSL2 接口与 NVIDIA Jetson Orin/Xavier 平台连接。ZED X 具备 IP67 防护、硬件多相机同步、15 m 同轴电缆供电与数据传输能力，适合农业机器人、AMR、人形机器人等恶劣环境下的 3D 感知。

## 工作原理 / 技术架构

ZED X 在双目立体视觉基础上引入全局快门与 GMSL2 高速串行接口：

- **全局快门传感器**：双 2.3 MP 彩色全局快门 CMOS，消除运动模糊，适合高动态场景。
- **Neural Depth Engine 2**：基于深度学习的视差优化，提升弱纹理与低光照下的深度鲁棒性。
- **GMSL2 接口**：通过单根同轴电缆同时传输视频、控制与电源（PoC），支持 15 m 长距离、低延迟与强 EMI 抗扰。
- **多相机同步**：硬件帧级同步精度约 ±100 µs，支持多 ZED X 相机同时曝光。
- **ZED SDK / Terra AI**：提供 SLAM、物体检测、骨架追踪与数字孪生算法。

深度估计关系：
$$Z = \frac{f \cdot B}{d}$$
2.2 mm 镜头对应约 110°(H) 视场角与 0.3–20 m 深度量程。

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 传感器 | 双 2.3 MP 彩色全局快门 CMOS，3 µm 像素 | Stereolabs |
| 分辨率 | 2×1920×1200 @ 60 fps；2×960×600 @ 120 fps | Stereolabs |
| 镜头选项 | 2.2 mm / 4 mm | Stereolabs |
| FOV（2.2 mm，H/V/D） | 110° / 80° / 120° | Stereolabs / 经销商 |
| 深度量程（2.2 mm） | 0.3 m – 20 m | Stereolabs |
| 深度量程（4 mm） | 1.0 m – 35 m | Stereolabs |
| 深度技术 | Neural Stereo Depth Sensing Gen2 | Stereolabs |
| IMU | 16-bit 三轴加速度计 + 陀螺仪，400 Hz | Stereolabs |
| 接口 | GMSL2 FAKRA-Z，PoC | Stereolabs |
| 防护等级 | IP67 | Stereolabs |
| 工作温度 | -20 °C – +55 °C | Stereolabs |
| 尺寸（ZED X） | 约 163.4 × 31.8 × 36.7 mm | 经销商 |
| 重量（ZED X） | 约 239 g | 经销商 |
| 多机同步 | 硬件帧级同步（±100 µs） | Stereolabs |
| 兼容平台 | NVIDIA Jetson Orin / Xavier（需 GMSL2 采集卡） | Stereolabs |

## 应用场景

- **自动驾驶/AMR 感知**：长距离深度、障碍物检测与路径规划。
- **人形机器人**：头部/躯干多相机环视与 VIO 定位。
- **农业机器人**：户外强光、振动环境下的作物与路径识别。
- **工业自动化**：高精度抓取、体积测量与数字孪生。

## 供应链关系

- **制造商**：Stereolabs（ent_company_stereolabs），2026 年已被 Ouster 收购。
- **上游关键物料**：全局快门 CMOS、GMSL2 串行器、FAKRA 连接器、光学镜头、IMU、铝外壳。
- **下游整机集成**：AMR、自动驾驶原型、人形机器人、农业机器人、工业 3D 检测系统。
- **竞争/对标**：Intel RealSense D455、奥比中光、图漾科技、海康机器人、Ouster LiDAR。

## 来源与验证

- Stereolabs ZED X 产品页：https://www.stereolabs.com/en-be/products/zed-x
- Mouser ZED X 规格页：https://www.mouser.vn/new/stereolabs/stereolabs-zed-x-stereo-camera/
- Generation Robots ZED X Mini 产品页：https://www.generationrobots.com/en/404308-zed-x-mini-depth-camera.html