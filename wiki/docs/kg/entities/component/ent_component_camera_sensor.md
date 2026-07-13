---
id: ent_component_camera_sensor
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 机器人视觉相机传感器
  en: Camera Sensor for Robotics
status: active
sources:
- id: src_ent_component_camera_sensor_1
  type: website
  url: https://www.orbbec.com/blog/how-lidar-and-rgbd-cameras-compare-and-work-together/
- id: src_ent_component_camera_sensor_2
  type: website
  url: https://rosindustrial.org/3d-camera-survey
- id: src_ent_component_camera_sensor_3
  type: website
  url: https://www.baslerweb.com/en/cameras/basler-tof-camera/rgb-d-solution/
- id: src_ent_component_camera_sensor_4
  type: website
  url: https://www.e-consystems.com/blog/camera/technology/what-are-rgbd-cameras-why-rgbd-cameras-are-preferred-in-some-embedded-vision-applications/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 机器人视觉相机传感器

## 概述

机器人视觉相机传感器是将光信号转换为电信号，并输出二维图像或三维点云的感知器件。按成像维度可分为 2D 相机（单目/双目/多目）与 3D 深度相机（结构光、ToF、双目立体视觉）。在人形机器人中，相机传感器通常部署于头部、胸部或腕部，用于环境感知、目标识别、SLAM 建图、导航避障及灵巧操作中的位姿估计。

## 工作原理 / 技术架构

2D 相机基于 CMOS 图像传感器的光电二极管阵列，通过卷帘或全局快门将入射光子转换为电荷包，再经 ADC 得到数字图像。空间分辨率由像素数 $N_x \times N_y$ 与像元尺寸 $p$ 决定；对远处目标的角分辨率约为

$$
\Delta\theta \approx \frac{p}{f}
$$

其中 $f$ 为镜头焦距。

3D 深度相机通过双目立体视觉、结构光或飞行时间（ToF）获取像素级距离。双目立体视觉的深度 $Z$ 与视差 $d$、基线 $b$ 及焦距 $f$ 的关系为

$$
Z = \frac{b \cdot f}{d}
$$

视差越小，可测距离越远；基线越大，远距离精度越高，但最近可测距离增大。

飞行时间相机通过测量调制光往返相位差计算距离：

$$
Z = \frac{c \cdot \Delta\phi}{4\pi f_m}
$$

其中 $c$ 为光速，$f_m$ 为调制频率，$\Delta\phi$ 为发射与接收光波的相位差。结构光则通过投射已知图案并解码变形来恢复深度。

## 关键参数表

| 参数项 | 典型值 | 备注/来源 |
|--------|--------|-----------|
| 传感器类型 | CMOS 单目 / 双目 / 结构光 / ToF | 机器人常用 RGB-D |
| RGB 分辨率 | 1,280×800 – 1,920×1,080 | 视型号而定 |
| 深度分辨率 | 640×480 @ 30 fps（常见） | Basler blaze / ROS Industrial |
| 视场角（FOV） | H 67°–120°，V 51°–95° | 因型号而异 |
| 工作距离 | 0.1–5 m（室内 RGB-D）；最远可达 20 m（双目） | Orbbec / ROS Industrial |
| 精度 | ±1% @ 0.5–5 m；近距离 ±1.5–2.5 cm | e-con Systems / DFRobot |
| 数据接口 | USB 3.0 / USB 2.0 / Gigabit Ethernet | 视型号 |
| 供电 | 5 V / 0.6 A 或 PoE | 典型低功耗 RGB-D |
| 延迟 | 约 66–110 ms（含传输与处理） | ROS Industrial 调查 |
| 价格 | 未公开 | 视传感器类型与批量差异大 |

## 应用场景

- **人形机器人头部感知**：RGB-D 相机用于大场景语义分割、人体检测与人机交互。
- **导航与避障**：结合 LiDAR 与 IMU，实现实时 SLAM、路径规划与动态障碍物躲避。
- **灵巧操作**：腕部或胸部深度相机提供近距离点云，辅助抓取位姿估计与碰撞检测。
- **工业质检与物流**：2D 高分辨率相机用于条码识别、缺陷检测与视觉引导。

## 供应链关系

相机传感器上游为图像传感器晶圆厂（如 Sony、OmniVision、ams OSRAM、Intel RealSense 模组供应链）、光学镜头与滤光片厂商；中游为相机模组/整机厂商（如 Basler、Orbbec、Intel RealSense、RoboSense 等）；下游集成于人形机器人头部、移动机器人或机械臂末端，为 `ent_product_casbot_01`、`ent_product_limx_oli`、`ent_product_pacsini_tora_one` 等整机提供视觉感知输入。

## 来源与验证

- RGB-D 与 LiDAR 的选型参数参考 Orbbec 技术博客。
- 典型 3D 相机（ZED、RealSense、Ensenso、SICK Visionary-T、Basler blaze）的规格来自 ROS Industrial 3D Camera Survey 与 Basler 官方资料。
- RGB-D 相机的分辨率、精度与接口参数参考 e-con Systems 与 DFRobot 产品说明。