# 思岚科技 / SLAMTEC

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 思岚科技 |
| **英文名** | SLAMTEC |
| **总部** | 中国上海 |
| **成立时间** | 2013（团队始于 2009） |
| **官网** | [https://www.slamtec.com](https://www.slamtec.com) |
| **供应链环节** | 激光雷达、SLAM 定位导航、机器人移动底盘 |
| **企业属性** | 民营企业、高新技术企业 |
| **母公司/所属集团** | 独立运营 |
| **数据来源** | 思岚科技官网、产品 datasheet、公开报道 |

## 公司简介

思岚科技（SLAMTEC）是国内最具代表性的机器人自主定位导航技术提供商，团队自 2009 年起致力于机器人自主定位导航核心传感器与算法的研发。

公司核心产品包括 RPLIDAR 系列 2D 激光雷达、SLAMTEC Mapper 激光建图雷达、Zeus 系列机器人底盘及相关导航算法。其产品以低成本、高性能和易集成著称，已基本实现服务机器人激光雷达的进口替代，并将价格下探至百至千元级别，广泛应用于服务机器人、清洁机器人、配送机器人、无人车与人形机器人导航。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 2D 激光雷达 | 机器人环境感知 | RPLIDAR A1 / A2 / A3 / S1 | 服务机器人、无人车、人形机器人 |
| 激光建图雷达 | 实时建图与定位 | SLAMTEC Mapper | 测绘、巡检、机器人导航 |
| 机器人底盘 | 完整移动平台 | Zeus / Apollo 系列 | 服务机器人、配送机器人 |
| SLAM 算法/SDK | 定位导航软件 | RoboStudio / SDK | 机器人开发 |

## 代表产品

### 思岚科技 RPLIDAR A3 激光测距传感器

> SLAMTEC RPLIDAR A3：请访问 [官方资料](https://www.slamtec.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 360° 2D 激光测距雷达 | 官方 datasheet |
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

**技术亮点**：光磁融合（OPTMAG）无线供电+光通信技术，彻底解决滑环磨损问题；室内外双模式；超薄 4 cm 设计适合服务机器人集成。

**应用场景**：服务机器人导航避障、无人车环境感知、大屏互动、人形机器人定位建图。

### 思岚科技 SLAMTEC Mapper 激光建图雷达

> SLAMTEC Mapper：请访问 [官方资料](https://www.slamtec.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 集成实时建图与定位的激光雷达 | 官方公开资料 |
| 特点 | 上电即用、无需外部依赖 | 官方公开资料 |
| 输出 | 高品质地图数据与定位坐标 | 官方公开资料 |
| 抗干扰 | 晃动、慢跑不影响建图 | 公开评测 |
| 测距/采样 | 未公开 | - |
| 重量 | 未公开 | - |
| 价格 | 未公开 | - |

**技术亮点**：集激光雷达与 SLAM 算法于一体，可直接对外输出地图与定位信息，降低机器人开发门槛。

**应用场景**：机器人巡检、室内测绘、AGV/AMR 定位、科研教育。

## 供应链位置

- **上游关键零部件/材料**：激光发射器、光电探测器、无刷电机、光学透镜、FPGA/SoC、结构件、无线供电模块
- **下游客户/应用场景**：服务机器人、清洁机器人、配送机器人、无人车、人形机器人、大屏互动、测绘巡检
- **主要竞争对手/对标**：禾赛科技、速腾聚创、北醒光子、镭神智能、欧思丹

## 知识图谱节点与关系

- 公司实体：`ent_company_slamtec`
- 产品实体：`ent_component_slamtec_rplidar_a3`
- 产品实体：`ent_product_slamtec_mapper`
- 关键关系：
  - `ent_company_slamtec` -- `manufactures` --> `ent_component_slamtec_rplidar_a3`
  - `ent_company_slamtec` -- `manufactures` --> `ent_product_slamtec_mapper`
  - `ent_component_slamtec_rplidar_a3` -- `used_in` --> `ent_product_service_robot`

## 参考资料

1. [思岚科技官网](https://www.slamtec.com)
2. [思岚科技 RPLIDAR A3 产品页](https://www.slamtec.com/cn/Lidar/A3)
3. [RPLIDAR A3M1 datasheet](https://files.seeedstudio.com/wiki/robotics/Sensor/Lidar/slamtec/LD310_SLAMTEC_rplidar_datasheet_A3M1_v1.9_cn.pdf)
4. [附录 D 产品目录](../index-products.md)