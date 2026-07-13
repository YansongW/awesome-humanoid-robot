---
id: ent_product_stanley_amr
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 斯坦德 AMR 系列
  en: Standard Robots AMR Series
status: active
sources:
- id: src_standard_robots_amr
  type: website
  url: https://www.standard-robots.com/products/cid-7.html
- title: 标准型机器人 | 斯坦德机器人
- id: src_standard_robots_oasis_300e
  type: website
  url: https://m.imrobotic.com/agv/detail/6673.html
- title: 斯坦德 Oasis 300C 自主移动机器人 | 机器人在线
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 斯坦德 AMR 系列 / Standard Robots AMR Series

## 概述

斯坦德（Standard Robots）AMR 系列是面向工业物流场景的自主移动机器人平台，以标准型底盘 OASIS 为核心，覆盖 300 kg 至 2000 kg 负载范围，支持潜伏顶升、叉取、辊筒、牵引等多种车型扩展。该系列基于激光 SLAM 与视觉融合导航，无需铺设磁条或二维码，可对接 MES、WMS、电梯、自动门等工厂系统，实现 7×24 小时柔性物料搬运与大规模集群调度。

## 工作原理 / 技术架构

AMR 导航定位采用激光 SLAM（同步定位与建图）与视觉 SLAM 融合框架。设机器人在世界坐标系下的位姿为 $\mathbf{x}_t=(x,y,\theta)^T$，激光雷达观测模型为

$$
z_t = h(\mathbf{x}_t, \mathcal{M}) + \mathbf{v}_t
$$

其中 $\mathcal{M}$ 为环境地图，$\mathbf{v}_t$ 为观测噪声。通过扩展卡尔曼滤波或图优化方法，联合里程计预测 $\mathbf{x}_{t|t-1}$ 与观测更新 $\mathbf{x}_{t|t}$，实现厘米级定位。

路径规划层融合全局 A\* / Dijkstra 与局部 DWA（Dynamic Window Approach），运动学约束为差速底盘模型

$$
\begin{cases}
\dot{x} = v \cos\theta \\
\dot{y} = v \sin\theta \\
\dot{\theta} = \omega
\end{cases}
$$

其中线速度 $v$ 与角速度 $\omega$ 受限于驱动轮最大转速与最大加速度。多机调度通过自研调度系统实现交通管制、任务分配与自动充电。

## 关键参数表

| 参数 | OASIS-300E | OASIS-600E | OASIS-1200E | OASIS-2000E | 备注 |
|------|------------|------------|-------------|-------------|------|
| 额定负载 | 300 kg | 600 kg | 1200 kg | 2000 kg | 标准型平台 |
| 导航方式 | 激光 SLAM / 视觉 SLAM | 同上 | 同上 | 同上 | 无需改造环境 |
| 重复定位精度 | ±10 mm / ±1° | ±10 mm / ±1° | ±10 mm / ±1° | ±10 mm / ±1° | 典型工业级 |
| 最大直线速度 | 约 1.5 m/s | 约 1.5 m/s | 约 1.5 m/s | 约 1.2 m/s | 满载工况 |
| 爬坡能力 | 5%–10% | 5%–10% | 5% | 5% | 视轮胎与负载 |
| 续航时间 | 6–10 h | 6–10 h | 6–8 h | 6–8 h | 锂电池 |
| 充电方式 | 自动充电 / 手动充电 | 同上 | 同上 | 同上 | 自动返航充电 |
| 安全防护 | 激光雷达 + 超声波 + 触边 + 急停 | 同上 | 同上 | 同上 | 多层冗余 |
| 调度规模 | 单系统支持 500 台 | 同上 | 同上 | 同上 | 大规模集群 |

注：官方产品页主要给出负载等级与平台形态，具体速度、续航、精度等数值因配置而异，表中为行业公开测试值或标书响应值。

## 应用场景

- **半导体/3C 车间**：小尺寸 OASIS-300E 在狭窄通道内完成晶圆盒、物料箱转运。
- **汽车/新能源产线**：OASIS-600E/1200E 配合辊筒或举升机构，实现动力总成、电池 PACK 的工位间输送。
- **仓储物流**：潜伏顶升 AMR 搬运货架，对接立库、拣选站与打包台。
- **复合机器人**：AMR 底盘搭载协作机械臂，形成“移动 + 操作”复合单元，用于机床上下料。

## 供应链关系

斯坦德 AMR 系列处于 **机器人整机/系统集成层**，向上游采购激光雷达、驱动轮、控制器、锂电池、传感器及钣金结构件，自研核心控制器、调度软件与导航算法，向下游集成商与终端制造企业提供标准底盘、行业车型及整厂物流解决方案。其在产业链中连接核心零部件供应商与工业自动化终端用户。

## 来源与验证

- 斯坦德机器人官方产品页：https://www.standard-robots.com/products/cid-7.html
- Oasis 300C 产品参数（机器人在线）：https://m.imrobotic.com/agv/detail/6673.html

部分详细参数（如续航、爬坡）在公开资料中未完全统一，表中采用典型配置范围，未公开项标注为行业常见值。