---
id: ent_component_slamtec_rplidar_a3
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 思岚科技 RPLIDAR A3 激光测距雷达
  en: SLAMTEC RPLIDAR A3 2D Laser Range Scanner
status: active
sources:
- id: src_ent_component_slamtec_rplidar_a3_1
  type: website
  url: https://cdn.robotshop.com/media/r/rpk/rb-rpk-07/pdf/ld310_slamtec_rplidar_datasheet_a3m1_v1.9_en.pdf
- id: src_ent_component_slamtec_rplidar_a3_2
  type: website
  url: https://www.slamtec.com/cn/Lidar/A3
- id: src_ent_component_slamtec_rplidar_a3_3
  type: website
  url: https://files.seeedstudio.com/wiki/robotics/Sensor/Lidar/slamtec/LM310_SLAMTEC_rplidarkit_usermanual_A3M1_v1.4_cn.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 思岚科技 RPLIDAR A3 激光测距雷达 / SLAMTEC RPLIDAR A3 2D Laser Range Scanner

## 概述

思岚科技 RPLIDAR A3（型号 A3M1）是一款低成本、高性能的 360° 二维激光测距雷达，采用激光三角测距原理与自研 RPVision 3.0 高速视觉测距引擎。该雷达支持增强模式与室外模式，在增强模式下可实现 25 m 测距半径与 16 kHz 采样频率；室外模式则提升抗日光干扰能力。RPLIDAR A3 采用光磁融合（OPTMAG）无线供电与光通信技术，取消传统滑环，官方标称寿命长达 5 年，广泛应用于服务机器人、无人车、大屏互动及人形机器人导航等场景。

## 工作原理 / 技术架构

RPLIDAR A3 通过旋转扫描核心发射激光束，激光经目标反射后在内部成像面上形成光斑，利用三角几何关系解算目标距离。扫描核心由无刷电机驱动，典型转速为 600 rpm（10 Hz），扫描频率可在 5–15 Hz 范围内配置。在 10 Hz 模式下，采样率为 16,000 次/秒，对应的角分辨率为

$$
\theta = \frac{360°}{16000 / 10} = 0.225°
$$

OPTMAG 技术通过无线供电与光信号传输替代机械滑环，消除了滑环磨损导致的寿命瓶颈。每个采样点输出距离（mm）、方位角（°）及起始标志位，主机通过 TTL UART 以 256,000 bps 接收数据。

## 关键参数表

| 参数项 | 典型值/范围 | 备注/来源 |
|--------|-------------|-----------|
| 传感器类型 | 360° 二维激光测距雷达 | 官方 datasheet |
| 测距原理 | 激光三角测距 | 官方 datasheet |
| 测距引擎 | RPVision 3.0 | 官方 datasheet |
| 扫描角度 | 360° | 官方 datasheet |
| 测距半径 | 25 m（增强模式白色物体）/ 20 m（室外模式白色物体） | 官方 datasheet |
| 最小测距 | 0.2 m | 官方 datasheet |
| 采样频率 | 16,000 次/秒（增强模式）/ 10,000 次/秒（室外模式） | 官方 datasheet |
| 扫描频率 | 5 – 15 Hz（典型 10 Hz） | 官方 datasheet |
| 角度分辨率 | 0.225°（10 Hz 增强模式） | 官方 datasheet |
| 测距分辨率 | ≤ 1%（≤ 12 m）；≤ 2%（12 m – 25 m） | 官方 datasheet |
| 测距精度 | 1%（≤ 3 m）；2%（3 – 5 m）；2.5%（5 – 25 m） | 官方 datasheet |
| 通信接口 | 3.3 V TTL UART | 官方 datasheet |
| 通信波特率 | 256,000 bps | 官方 datasheet |
| 供电电压 | 5 V DC（4.9–5.2 V） | 官方 datasheet |
| 工作电流 | 450 – 600 mA（稳定工作） | 官方 datasheet |
| 启动冲击电流 | 最大 2500 mA | 官方 datasheet |
| 功耗 | 2.25 – 3 W | 官方 datasheet |
| 尺寸 | 直径 76 mm × 高 41 mm | 官方 datasheet |
| 重量 | 190 g | 官方 datasheet |
| 工作温度 | 0 – 40 °C | 官方 datasheet |
| 激光安全等级 | Class 1（人眼安全，< 3 mW） | 官方 datasheet |
| 寿命 | OPTMAG 技术，长达 5 年 | 官方 datasheet |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **服务机器人导航与避障**：室内 SLAM 建图、路径规划、动态障碍物检测。
- **人形机器人环境感知**：低成本二维定位与建图，辅助下肢导航。
- **无人车/AGV**：低速场景下边界识别与障碍物检测。
- **大屏互动与测绘**：多点触控、互动投影、室内测绘巡检。

## 供应链关系

- **制造商**：思岚科技 / SLAMTEC（`ent_company_slamtec`）。
- **上游关键零部件/材料**：激光发射器、光电探测器、无刷电机、光学透镜、FPGA/SoC、结构件、无线供电模块。
- **下游客户/应用场景**：服务机器人厂商、清洁机器人厂商、配送机器人厂商、无人车开发商、人形机器人整机厂。
- **竞争/对标**：禾赛科技、速腾聚创、北醒光子、镭神智能、欧思丹、Velodyne。
- **知识图谱关系**：`ent_company_slamtec` — `manufactures` → `ent_component_slamtec_rplidar_a3`；该产品常用于 `ent_product_service_robot` 等移动机器人平台。

## 来源与验证

1. [SLAMTEC RPLIDAR A3M1 Datasheet（PDF）](https://cdn.robotshop.com/media/r/rpk/rb-rpk-07/pdf/ld310_slamtec_rplidar_datasheet_a3m1_v1.9_en.pdf)
2. [思岚科技 RPLIDAR A3 产品页](https://www.slamtec.com/cn/Lidar/A3)
3. [RPLIDAR A3 开发套件用户手册（PDF）](https://files.seeedstudio.com/wiki/robotics/Sensor/Lidar/slamtec/LM310_SLAMTEC_rplidarkit_usermanual_A3M1_v1.4_cn.pdf)
4. [附录 D 企业 Wiki：思岚科技](../../../appendices/appendix-d/companies/company_slamtec.md)