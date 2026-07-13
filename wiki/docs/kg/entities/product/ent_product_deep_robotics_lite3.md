---
id: ent_product_deep_robotics_lite3
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 云深处 绝影 Lite3
  en: DEEPRobotics Jueying Lite3
status: active
sources:
- id: src_deep_robotics_lite3_us
  type: website
  url: https://www.deeprobotics.us/news/how-the-deep-robotics-lite3-accelerates-innovation-in-education-research-real-world-robotics-applications/
- title: How the DEEP Robotics Lite3 Accelerates Innovation in Education, Research
    & Real-World Robotics Applications
- id: src_deep_robotics_lite3_leobotics
  type: website
  url: https://en.leobotics.com/comparateur-robot/robot-quadrupede-jueying-lite3-lidar-deep-robotics-securite-inspection
- title: Jueying Lite3 LiDAR Deep Quadruped Robot — Leobotics
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 云深处 绝影 Lite3 / DEEPRobotics Jueying Lite3

## 概述

绝影 Lite3 是杭州云深处科技（DEEPRobotics）推出的轻量化四足机器人平台，面向教育科研、算法验证与巡检探索等场景。整机采用 12 关节仿生腿足结构，机身自重约 11 kg（单腿约 1.12 kg），具备高扭矩密度关节、可扩展感知套件与完整 ROS/仿真开发工具链。

## 工作原理 / 技术架构

### 腿足运动学
绝影 Lite3 每条腿为串联三连杆 + 三关节构型（髋关节 2 DOF + 膝关节 1 DOF，或等效 3 DOF），整机腿部共 12 DOF。机体位姿由 6 个机身自由度（3 平移 + 3 旋转）与 12 个关节角共同描述。足端位置 $\mathbf{p}_i$ 可通过正向运动学由关节角 $\mathbf{q}_i$ 计算：

$$
\mathbf{p}_i = f_{\text{FK},i}(\mathbf{q}_i), \quad i=1,\dots,4
$$

控制上通常采用模型预测控制（MPC）或强化学习（RL）策略，结合足底接触力规划实现稳定爬行、越障与动态恢复。

### 关节与动力系统
- **关节扭矩**：公开资料称关节扭矩较前代提升 50%，具备高扭矩密度、响应带宽与反向传动效率；
- **电机技术**：采用无刷直流电机 + 行星/谐波减速器一体化关节模组；
- **电池**：24 V 锂离子电池，专用电池包可更换。

### 感知系统
基础版配置：

- 内置广角相机：水平视场角 130°，1920×1080@30fps；
- 前后自动停车超声波雷达；
- 自研 6 轴 IMU。

可选扩展套件：

- Intel RealSense D435i 深度相机；
- 16 线 LiDAR，探测距离 100 m@10% 反射率、150 m@70% 反射率；
- NVIDIA Jetson Xavier NX 计算平台（Ubuntu + ROS）。

### 开发接口
- 模块化 SDK、API、仿真模型；
- 支持 NVIDIA Isaac Sim、MuJoCo、Gazebo 等仿真平台；
- 提供 ROS/ROS2 接口、Python 开发示例。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 机体类型 | 四足仿生机器人 |
| 机身重量 | 约 11 kg |
| 单腿重量 | 约 1.12 kg |
| 腿部自由度 | 12（每条腿 3 DOF） |
| 整机自由度 | 约 31（含机身） |
| 关节扭矩 | 较前代提升 50% |
| 内置相机 | 130° 水平 FOV，1920×1080@30fps |
| 超声波雷达 | 前后自动停车雷达 |
| 可选深度相机 | Intel RealSense D435i |
| 可选 LiDAR | 16 线，100 m@10% / 150 m@70% |
| 可选计算平台 | NVIDIA Jetson Xavier NX |
| 供电接口 | 5 V / 12 V / 24 V 多路输出 |
| 通信接口 | Ethernet / WiFi / USB 3.0 / HDMI |
| 开发支持 | ROS、Python、仿真模型、SDK、API |

## 应用场景

- **高校与科研**：腿足运动控制、强化学习 sim-to-real、多足机器人算法验证；
- **工业巡检**：电力管廊、工厂车间、园区安防的轻量化巡检；
- **教育科普**：STEM 机器人课程、机器人竞赛；
- **户外探索**：地形适应、搜索与救援原型验证。

## 供应链关系

绝影 Lite3 位于“四足机器人整机—核心零部件—上游算力/传感”链条的整机与科研平台层：

- **整机厂商**：杭州云深处科技（DEEPRobotics）；
- **核心零部件**：自研高扭矩密度关节模组、自研 6 轴 IMU；
- **可选扩展**：Intel RealSense 深度相机、NVIDIA Jetson 计算平台、第三方 LiDAR；
- **下游用户**：高校、科研院所、巡检服务商与开发者社区。

## 来源与验证

- DEEPRobotics 美国官网新闻稿（2025-11-29）
- Leobotics 产品规格页（2026-03-30）
- GitHub DEEPRoboticsLab 开源模型仓库

> 注：电池容量、最大行走速度、续航时间、关节峰值扭矩等精确数值未在公开资料中完整披露，标注为“未公开”。