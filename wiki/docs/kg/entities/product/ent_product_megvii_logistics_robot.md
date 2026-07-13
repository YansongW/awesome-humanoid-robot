---
id: ent_product_megvii_logistics_robot
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 旷视物流机器人（3D 托盘四向车系统）
  en: Megvii Logistics Robot (3D Pallet Shuttle System)
status: active
sources:
- id: src_ent_product_megvii_logistics_robot_1
  type: website
  url: https://en-robotics.megvii.com/news1-827.html
- id: src_ent_product_megvii_logistics_robot_2
  type: website
  url: https://en-robotics.megvii.com/Press-Release/Megvii-Focus-on-Niche-Industries-and-Grind-Core-Products.html
- id: src_ent_product_megvii_logistics_robot_3
  type: website
  url: https://en-robotics.megvii.com/Megvii-News/Megvii-3D-Pallet-Shuttle-Robot-Awarded-CE-Certificate-Paving-the-Way-for-EU-Mark-Entry.html
- id: src_ent_product_megvii_logistics_robot_4
  type: website
  url: https://en.megvii.com/products/hardware/ASRS
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 旷视物流机器人（3D 托盘四向车系统）

## 概述

旷视物流机器人是旷视科技（Megvii）旗下自动化与机器人业务的核心硬件产品线，以“MegBot-PS1500”智能 3D 托盘四向车系统为代表。该系统结合高密度立体存储、分布式控制与旷视“河图”（HETU）AI 调度平台，实现 pallet 级货物的灵活存取、大规模集群调度与“3D PS + X”柔性物流解决方案，面向仓储、制造与冷链物流场景。

## 工作原理 / 技术架构

3D 托盘四向车可在货架轨道内沿 X/Y 方向行驶，并通过提升机实现 Z 方向换层，构成三维存储网络。每台四向车为独立智能体，采用分布式控制架构，单点故障不会导致整个系统停机。河图调度平台基于 AI 算法动态管理库位、任务路径与车辆分配，实现大规模车队协同。

单车运行效率可由加速度 $a$、最大速度 $v$ 与定位精度 $\Delta x$ 综合描述。根据官方数据，MegBot-PS1500 的空载加速度为 2 m/s²，最大运行速度为 1.5 m/s，定位精度为 ±2 mm。对于一个典型的单趟搬运任务，平均行驶距离 $s$ 与速度 $v$ 决定任务时间下限：

$$
t_{run} = \frac{s}{v}
$$

实际任务时间还需加上换向时间（2.5 s 空载 / 3.5 s 负载）与顶升时间（2.5 s）。

电池续航方面，单车电池容量 60 Ah，功耗约 40 W，支持 1 小时快充与 8 小时连续工作。电池可用能量 $E$ 与电压 $U$ 的关系为

$$
E = U \cdot Q
$$

其中 $Q = 60\ \mathrm{Ah}$；若以 48 V 系统估算，可用能量约为 2.88 kWh（未考虑放电深度）。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 代表产品 | MegBot-PS1500 智能 3D 托盘四向车 | Megvii 官方 |
| 车体厚度 | 125 mm | Megvii 新闻稿 |
| 额定负载 | 1.5 吨 | Megvii 新闻稿 |
| 空载加速度 | 2 m/s² | Megvii 新闻稿 |
| 最大运行速度 | 1.5 m/s | Megvii 新闻稿 |
| 定位精度 | ±2 mm | Megvii 新闻稿 |
| 空载换向时间 | 2.5 s | Megvii 新闻稿 |
| 负载换向时间 | 3.5 s | Megvii 新闻稿 |
| 顶升时间 | 2.5 s | Megvii 新闻稿 |
| 电池容量 | 60 Ah | Megvii 新闻稿 |
| 运行功耗 | 约 40 W | Megvii 新闻稿 |
| 充电时间 / 续航 | 1 小时充电，8 小时连续工作 | Megvii 新闻稿 |
| 安全传感器 | 6 个 Leuze 工业级激光避障传感器 + 3 个托盘检测光电开关 | Megvii 新闻稿 |
| 调度系统 | 旷视河图（HETU）| Megvii 官方 |
| 认证 | CE 全指令证书（SGS，2023）| Megvii CE 新闻 |
| 价格 | 未公开 | 项目制报价 |

## 应用场景

- **高密度智能仓储**：替代传统“堆垛机 + 输送线”，提升空间利用率与出入库柔性。
- **制造物流**：与 AMR、机械臂、视觉盘点工作站组成“3D PS + X”方案，实现产线物料自动配送。
- **冷链物流**：提供常温版与冷库版四向车，满足低温仓储需求。
- **大规模集群调度**：河图平台可调度 80 台以上四向车协同作业，已应用于服装等行业标杆项目。

## 供应链关系

MegBot-PS1500 由 `ent_company_megvii` 旗下 Megvii Automation & Robotics 研发制造。上游核心零部件包括 Leuze 激光传感器、Panasonic 光电开关、CATL/Toshiba 电池电芯、控制器与二维码相机；中游为旷视自研机器人平台与河图软件；下游面向第三方物流、制造零售、冷链与新能源行业客户。知识图谱关系：

- `ent_company_megvii` -- `manufactures` --> `ent_product_megvii_logistics_robot`
- `ent_product_megvii_logistics_robot` -- `uses` --> `ent_product_megvii_megengine`（视觉/AI 算法支持）
- `ent_product_megvii_logistics_robot` -- `uses` --> 激光传感器/相机等零部件

## 来源与验证

- MegBot-PS1500 的核心技术参数（125 mm 厚度、1.5 t 负载、2 m/s² 加速度、±2 mm 精度、60 Ah 电池等）来自 Megvii 2022 年 3D 托盘四向车系统发布会新闻稿。
- 大规模调度能力与应用场景参考 Megvii 2023 年“Focus on Niche Industries”新闻稿。
- CE 认证信息来自 Megvii Automation & Robotics 2023 年新闻稿。