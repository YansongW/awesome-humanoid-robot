---
id: ent_component_robosense_m1_plus
type: component
schema_version: 1
domain: 02_components
status: active
names:
  zh: 速腾聚创 M1 Plus 固态激光雷达
  en: RoboSense M1 Plus Solid-State LiDAR
sources:
- id: src_robosense_m1_plus_brochure
  type: website
- title: RoboSense RS-LiDAR-M1 Plus Brochure
  url: https://cdn.robotshop.com/media/U/UTR/RB-Utr-08/pdf/robosense-rs-lidar-m1-plus-advanced-2d-mems-smart-chip-lidar-200m-range-brochure.pdf
- id: src_robosense_m1_plus_openelab
  type: website
- title: RoboSense M1 Plus Solid-State LiDAR Review – OpenELAB
  url: https://openelab.io/blogs/learn/robosense-m1-plus-solid-state-lidar-review-mems-based-150m-range-for-autonomous-vehicles
- id: src_robosense_official
  type: website
- title: 速腾聚创官网
  url: https://www.robosense.ai
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official RoboSense datasheets and verified product
    documentation; power values are typical at 10 Hz frame rate.
---


# 速腾聚创 M1 Plus 固态激光雷达 / RoboSense M1 Plus Solid-State LiDAR

## 概述

速腾聚创 M1 Plus（RoboSense M1 Plus）是全球首款智能可变焦汽车级固态激光雷达，采用 2D MEMS 半固态扫描技术，面向乘用车 ADAS 与高阶自动驾驶设计。该产品具备 200 m 最大探测距离（10% NIST 反射率目标下 180 m）、120°×25° 视场角、0.2°×0.2° 角分辨率（ROI 区域 0.1° 垂直分辨率）以及最高 1,575,000 点/秒的点频，已在多款车型量产前装应用，并适用于 Robotaxi、干线物流与人形机器人环境感知。

## 工作原理 / 技术架构

M1 Plus 基于 2D MEMS 微镜扫描与飞行时间（Time-of-Flight, ToF）测距原理：

1. **905 nm 激光发射**：采用 905 nm 波长激光器，符合 Class 1 人眼安全等级。
2. **2D MEMS 微镜扫描**：通过微机电系统微镜在水平与垂直两个方向偏转激光束，实现固态/半固态扫描，无需传统机械旋转部件。
3. **飞行时间测距**：发射激光脉冲并接收目标反射回波，通过测量光脉冲往返时间 $t$ 计算目标距离：

$$
d = \frac{c \cdot t}{2}
$$

其中 $c$ 为光速，$d$ 为测距距离。

4. **智能可变焦与 ROI**：可根据场景动态调整感兴趣区域（ROI）的扫描密度，在远距离目标区域获得更高垂直分辨率。
5. **集成 AI 感知 SoC**：M1 Plus Smart 版本内置 SPAD-SoC 与 AI 感知算法，可直接输出障碍物检测、分类与跟踪结果。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | 速腾聚创 / RoboSense | 官网 |
| 深度技术 | 2D MEMS 半固态激光雷达 | 官方 datasheet |
| 激光波长 | 905 nm | 官方 datasheet |
| 激光安全等级 | Class 1（IEC 60825-1，SGS/goebel 认证） | 官方 datasheet |
| 最大探测距离 | 200 m（180 m @ 10% NIST 反射率） | 官方 datasheet |
| 盲区 | ≤ 0.5 m | 官方 datasheet |
| 水平 FOV | 120°（-60° ~ +60°） | 官方 datasheet |
| 垂直 FOV | 25°（-12.5° ~ +12.5°） | 官方 datasheet |
| 水平角分辨率 | 平均 0.2° | 官方 datasheet |
| 垂直角分辨率 | 平均 0.2°（ROI 区域平均 0.1°） | 官方 datasheet |
| 帧率 | 10 Hz / 20 Hz | 官方 datasheet |
| 点频（单回波） | 787,500 点/秒 | 官方 datasheet |
| 点频（双回波） | 1,575,000 点/秒 | 官方 datasheet |
| 测距精度 | ±5 cm（典型，50% NIST 目标） | 官方 datasheet |
| 数据接口 | 1000Base-T1 Ethernet | 官方 datasheet |
| 输出协议 | UDP 数据包（坐标、强度、时间戳等） | 官方 datasheet |
| 时间同步 | gPTP（IEEE 802.1AS）/ PTP | 官方 datasheet |
| 工作电压 | 9 – 16 V DC（部分资料 9 – 36 V DC） | 官方/经销商资料 |
| 功耗 | 15 W（典型，10 Hz，≤100 m 范围） | 官方 datasheet |
| 工作温度 | -40 °C ~ +85 °C | 官方 datasheet |
| 存储温度 | -40 °C ~ +105 °C | 官方 datasheet |
| 防护等级 | IP67 / IP6K9K | 官方 datasheet |
| 尺寸（D×W×H） | 111 × 110 × 45 mm | 官方 datasheet |
| 重量（不含线缆） | 690 g ± 20 g | 官方 datasheet |
| 功能安全 | ISO 26262 ASIL-B | 官方 datasheet |
| 芯片可靠性 | AEC-Q100 | 官方 datasheet |
| 故障检测时间 | < 100 ms | 官方 datasheet |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **乘用车 ADAS 前向主激光雷达**：为高速公路与城市道路提供远距离、高密度环境感知。
- **Robotaxi 与干线物流**：支撑 L3/L4 级自动驾驶系统的 360° 感知方案中的前向或角向补盲。
- **人形机器人与 AMR**：作为前向/环视深度传感器，提供 3D 点云用于避障、导航与场景理解。
- **工业巡检与无人配送**：在复杂环境中实现可靠的障碍物检测与路径规划。

## 供应链关系

速腾聚创（`ent_company_robosense`）是全球激光雷达市占率领先企业，香港交易所上市（HKEX: 2498）。M1 Plus（`ent_component_robosense_m1_plus`）属于 M 系列车规级 MEMS 激光雷达产品线，与 E1R 等全固态数字激光雷达共同构成其感知硬件矩阵。上游包括 VCSEL 激光器、SPAD-SoC 芯片、驱动 IC、光学镜片、MEMS 微镜与精密结构件；下游客户包括乘用车 OEM（比亚迪、小鹏、吉利等）、人形机器人、AMR、无人配送与割草机器人厂商。速腾聚创与禾赛科技、览沃 Livox、华为、Ouster、Luminar、Innovusion 等形成竞争。

## 来源与验证

- RoboSense 官方 M1 Plus 产品手册提供了完整的探测距离、FOV、角分辨率、点频、功耗、尺寸与功能安全认证参数。
- OpenELAB 等渠道的产品评测对官方参数进行了交叉验证，并补充了 ROS/ROS2 驱动支持信息。
- 速腾聚创官网与招股说明书确认其为港股上市公司及激光雷达市场地位。