# 思岚科技 RPLIDAR A3 激光测距传感器 / SLAMTEC RPLIDAR A3 Laser Range Scanner

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [思岚科技 / SLAMTEC](../companies/company_slamtec.md) |
| **产品类别** | 360° 二维激光测距雷达 |
| **发布时间** | 2018 年起持续在售 |
| **状态** | 量产/商用 |
| **官网/来源** | [思岚科技官网](https://www.slamtec.com) |

## 产品概述

思岚科技 RPLIDAR A3 是一款低成本、高性能的 360° 二维激光测距雷达，采用激光三角测距原理与自研 RPVision 3.0 高速视觉测距引擎，采样频率高达 16,000 次/秒，测距半径可达 25 米。

A3 支持增强模式与室外模式，在增强模式下测距半径与采样频率达到最大值，在室外模式下具备更强的抗日光干扰能力。产品采用独创的光磁融合（OPTMAG）无线供电与光通信技术，彻底解决传统滑环磨损问题，寿命长达 5 年。其 4 cm 超薄机身与 190 g 重量，使其非常适合服务机器人、无人车、大屏互动及人形机器人导航等场景。

## 产品图片

> SLAMTEC RPLIDAR A3：请访问 [官方资料](https://www.slamtec.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 360° 二维激光测距雷达 | 官方 datasheet |
| 测距原理 | 激光三角测距 | 官方 datasheet |
| 测距引擎 | RPVision 3.0 | 官方 datasheet |
| 扫描角度 | 360° | 官方 datasheet |
| 测距半径 | 25 m（增强模式白色物体）/ 20 m（室外模式白色物体） | 官方 datasheet |
| 最小测距 | 0.2 m | 官方 datasheet |
| 采样频率 | 16,000 次/秒（增强模式）/ 10,000 次/秒（室外模式） | 官方 datasheet |
| 扫描频率 | 5 – 15 Hz（典型 10 Hz） | 官方 datasheet |
| 角度分辨率 | 0.225° | 官方 datasheet |
| 测距分辨率 | ≤1%（≤12 m）；≤2%（12 m – 25 m） | 官方 datasheet |
| 测距精度 | 1%（≤3 m）；2%（3 – 5 m）；2.5%（5 – 25 m） | 官方 datasheet |
| 通信接口 | TTL UART | 官方 datasheet |
| 通信波特率 | 256,000 bps | 官方 datasheet |
| 供电电压 | 5 V | 官方 datasheet |
| 工作电流 | 450 – 600 mA | 官方 datasheet |
| 功耗 | 2.25 – 3 W | 官方 datasheet |
| 尺寸 | 直径 76 mm × 高 41 mm | 官方 datasheet |
| 重量 | 190 g | 官方 datasheet |
| 工作温度 | 0℃ – 40℃ | 官方 datasheet |
| 激光安全等级 | Class 1（人眼安全） | 官方 datasheet |
| 寿命 | 光磁融合技术，长达 5 年 | 官方 datasheet |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[思岚科技 / SLAMTEC](../companies/company_slamtec.md)
- **核心零部件/技术来源**：自研 RPVision 测距引擎、光磁融合供电与通信技术；激光发射器、光电探测器、无刷电机、光学透镜、FPGA 外购。
- **下游应用/客户**：服务机器人、清洁机器人、配送机器人、无人车、人形机器人、大屏互动、测绘巡检。

## 知识图谱节点与关系

- 零部件实体：`ent_component_slamtec_rplidar_a3`
- 制造商实体：`ent_company_slamtec`
- 关键关系：
  - `rel_ent_company_slamtec_manufactures_ent_component_slamtec_rplidar_a3`（`ent_company_slamtec` → `manufactures` --> `ent_component_slamtec_rplidar_a3`）

## 应用场景

- **服务机器人**：室内导航、避障、SLAM 建图与路径规划。
- **人形机器人**：环境感知、定位建图与自主行走。
- **无人车/AGV**：低速场景下障碍物检测与边界识别。
- **大屏互动**：多点触控、互动投影与空间定位。

## 竞争对比

| 对比项 | 思岚 RPLIDAR A3 | 禾赛 ET25 | 速腾聚创 M1 Plus |
|--------|-----------------|-----------|------------------|
| 类型 | 2D 三角测距雷达 | 半固态/舱内激光雷达 | 半固态激光雷达 |
| 测距半径 | 25 m | 250 m | 180 m |
| 采样频率 | 16,000 次/秒 | >300 万点/秒 | 未公开 |
| 视场角 | 360°（水平单线） | 120°×25° | 未公开 |
| 价格 | 百至千元级 | 车规级 | 车规级 |
| 核心优势 | 低成本、超薄、长寿命 | 远距车规、舱内安装 | 车规量产 |

## 选购与部署建议

- 三角测距雷达在室外强光或深色物体场景下性能会下降，应根据环境选择增强模式或室外模式。
- 安装时需避免雷达窗口被遮挡或沾染灰尘，并确保 5 V 供电稳定以满足启动电流要求。

## 参考资料

1. [思岚科技官网](https://www.slamtec.com)
2. [思岚科技 RPLIDAR A3 产品页](https://www.slamtec.com/cn/Lidar/A3)
3. [RPLIDAR A3M1 datasheet](https://files.seeedstudio.com/wiki/robotics/Sensor/Lidar/slamtec/LD310_SLAMTEC_rplidar_datasheet_A3M1_v1.9_cn.pdf)
4. [附录 D 企业目录](../index-companies.md)