---
id: ent_component_livox_mid_360
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 览沃 Mid-360
  en: Livox Mid-360
status: active
created_at: 2024-01-15 00:00:00+00:00
updated_at: 2026-07-13 00:00:00+00:00
sources:
- id: src_livox_mid360_datasheet
  type: datasheet
- title: Livox Mid-360 Datasheet
  url: https://5.imimg.com/data5/SELLER/Doc/2024/6/429559707/ST/QG/JI/14158318/livox-mid-360-lidar.pdf
- id: src_livox_official
  type: website
- title: Livox Technology Official Website
  url: https://www.livoxtech.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自 Livox Mid-360 官方 datasheet；缺失值标注为“未公开”。
---


# 览沃 Mid-360 / Livox Mid-360

## 概述

览沃 Mid-360（Livox Mid-360）是览沃科技推出的混合固态 360° 激光雷达，采用旋镜式扫描，具备小体积、轻量化、内置 IMU 与 IP67 防护等级。该激光雷达是移动机器人 SLAM、导航与避障的主流 3D 感知传感器，并已广泛应用于四足机器人、清洁机器人、AMR/AGV 与人形机器人平台。

## 工作原理 / 技术架构

Mid-360 基于飞行时间（Time-of-Flight, ToF）测距原理。发射激光脉冲经目标反射后被接收器捕获，目标距离 $d$ 由发射与接收的时间差 $\Delta t$ 计算：

$$
d = \frac{c \cdot \Delta t}{2}
$$

其中 $c \approx 3 \times 10^8 \ \mathrm{m/s}$ 为光速。Mid-360 采用 905 nm 激光器，水平视场角 360°，垂直视场角 -7°~+52°，点频 200,000 点/秒（首回波），帧率 10 Hz。内置 ICM40609 IMU 以 200 Hz 输出加速度与角速度，支持 PTPv2 与 GPS 时间同步。

## 关键参数表

| 参数 | 典型值 | 备注 |
|------|--------|------|
| 尺寸 | 65 mm × 65 mm × 60 mm | 官方 datasheet |
| 重量 | 265 g | 官方 datasheet |
| 激光波长 | 905 nm | 官方 datasheet |
| 激光安全等级 | Class 1（IEC 60825-1:2014） | 官方 datasheet |
| 探测距离 | 40 m @ 10% 反射率；70 m @ 80% 反射率 | 100 klx 环境 |
| 近距盲区 | 0.1 m | 官方 datasheet |
| 视场角 | 水平 360°；垂直 -7° ~ +52° | 官方 datasheet |
| 点频 | 200,000 点/秒（首回波） | 官方 datasheet |
| 帧率 | 10 Hz（典型） | 官方 datasheet |
| 测距精度（1σ） | ≤ 2 cm @ 10 m；≤ 3 cm @ 0.2 m | 官方 datasheet |
| 角度精度（1σ） | < 0.15° | 官方 datasheet |
| 虚警率 | < 0.01% @ 100 klx | 官方 datasheet |
| IMU | 内置 ICM40609 | 官方 datasheet |
| 数据接口 | 100 BASE-TX Ethernet | 官方 datasheet |
| 时间同步 | IEEE 1588-2008 (PTPv2)、GPS | 官方 datasheet |
| 供电 | 9–27 V DC | 官方 datasheet |
| 功耗 | 6.5 W（典型） | 官方 datasheet |
| 防护等级 | IP67 | 官方 datasheet |
| 工作温度 | -20 ℃ ~ +55 ℃ | 官方 datasheet |
| 价格 | 未公开 | - |

## 应用场景

- AMR/AGV 导航与避障
- 四足机器人 SLAM 与地形感知
- 清洁机器人、割草机器人环境感知
- 三维测绘与数字孪生
- 人形机器人头部/躯干环境感知

## 供应链关系

制造商为览沃科技（Livox Technology，`ent_company_livox`），DJI 大疆创新内部孵化企业。上游关键原材料包括 905 nm 激光器、SPAD/APD、扫描电机、光学镜片、主控 SoC 与 IMU；下游客户包括 AMR/AGV、四足机器人（如云深处绝影 X30）、清洁机器人与自动驾驶平台。知识图谱中的关键关系为：`ent_company_livox` -- `manufactures` --> `ent_component_livox_mid_360`。

## 来源与验证

本卡片参数引自 Livox Mid-360 官方 datasheet 与产品页。批量价格未公开。