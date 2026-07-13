---
id: ent_component_livox_hap
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 览沃 HAP 激光雷达
  en: Livox HAP LiDAR
sources:
- id: src_livox_official
  type: website
- title: '"Livox HAP 官网"'
  url: https://www.livoxtech.com/hap
- id: src_livox_manual
  type: website
- title: '"LIVOX HAP High Performance LiDAR Sensor User Guide"'
  url: https://device.report/manual/3730533
- id: src_livox_deviestore
  type: website
- title: '"Livox HAP (TX) 产品规格"'
  url: https://deviestore.com/product/livox-hap-lidar/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# 览沃 HAP 激光雷达 / Livox HAP LiDAR

## 概述

览沃 HAP 是大疆内部孵化企业览沃科技推出的车规级混合固态激光雷达，采用 905 nm 激光与旋镜式扫描，具有 120° 水平视场、最远 150 m@10% 反射率探测距离与 452,000 点/秒点频。HAP 通过超过 70 项汽车级可靠性测试，已用于乘用车 ADAS、Robotaxi 与高端移动机器人。

## 工作原理 / 技术架构

HAP 通过电机带动扫描镜旋转，实现非重复式扫描图案，激光束经发射与接收通道测得目标距离。测距基于 ToF（Time of Flight）原理：

$$d = \frac{c \cdot \Delta t}{2}$$

其中 $c$ 为光速，$\Delta t$ 为发射与回波时间差。水平角分辨率 0.18°、垂直 0.23°，单回波点频 452,000 pts/s，等效线数约 144 线。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 激光波长 | 905 nm | 官方 datasheet |
| 激光安全等级 | Class 1（IEC60825-1:2014） | 官方 datasheet |
| 视场角 FOV | 120°(H) × 25°(V) | 官方 datasheet |
| 探测距离 | 150 m @ 10% 反射率；200 m @ 50% 反射率 | 官方 datasheet |
| 点频 | 452,000 pts/s（单回波）；904,000 pts/s（双回波） | 官方 datasheet |
| 角分辨率 | 0.18°(H) × 0.23°(V) | 官方 datasheet |
| 测距精度 | < 2 cm（1σ @ 20 m） | 官方 datasheet |
| 角度精度 | < 0.1° | 官方 datasheet |
| 帧率 | 10 / 20 Hz | 官方 datasheet |
| 典型功耗 | 12 W | 官方 datasheet |
| 供电电压 | 9–18 V DC | 官方 datasheet |
| 工作温度 | -40°C ~ +85°C | 官方 datasheet |
| 防护等级 | IP67 / IP6K9K | 官方 datasheet |
| 尺寸 | 约 105×131.6×65 mm（HAP TX） | 官方 datasheet |
| 重量 | 约 1120 g | 官方 datasheet |
| 数据接口 | 100BASE-TX Ethernet | 官方 datasheet |
| 时间同步 | gPTP / IEEE 1588 PTP | 官方 datasheet |

## 应用场景

乘用车 ADAS、Robotaxi、AMR/AGV 导航、四足机器人、工业 portal 扫描、高精地图测绘。

## 供应链关系

览沃科技（`ent_company_livox`）由 DJI 内部孵化并独立运营；上游包括 905 nm 激光器、SPAD/APD、扫描电机、光学镜片与主控 SoC；下游客户包括小鹏汽车、一汽解放、云深处绝影 X30 等机器人/车企，与禾赛科技、速腾聚创、Ouster、RoboSense 竞争。

## 来源与验证

- Livox HAP 官网：https://www.livoxtech.com/hap
- Livox HAP 用户手册：https://device.report/manual/3730533
- Livox HAP (TX) 规格页：https://deviestore.com/product/livox-hap-lidar/