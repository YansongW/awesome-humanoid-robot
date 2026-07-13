---
id: ent_product_flexiv_moonlight
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 非夕 Moonlight 玄晖力控型并联机器人
  en: Flexiv Moonlight Parallel Force-Control Robot
status: active
sources:
- id: src_flexiv_moonlight_page
  type: website
  url: https://www.flexiv.cn/product/enlight
- title: 非夕 Moonlight 玄晖产品页
- id: src_flexiv_launch_moonlight
  type: article
  url: https://www.flexiv.cn/news/launch_parallel_robot_moonlight
- title: 非夕科技发布力控型并联机器人 Moonlight 玄晖
- id: src_flexiv_exhibition_2024
  type: article
  url: https://www.sohu.com/a/811364322_120988576
- title: 非夕科技携多款解决方案亮相工博会
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 非夕 Moonlight / Flexiv Moonlight

## 概述

非夕 Moonlight（玄晖）是全球首款力控型并联机器人，由上海非夕机器人科技有限公司（Flexiv）推出。该产品将非夕自研的工业级力传感与力控技术与并联机构相结合，具备空间三自由度、高负载/自重比和 IP65 防护等级，适用于自由度要求相对较低但对力控精度要求较高的精密装配与表面处理任务。

## 工作原理 / 技术架构

Moonlight 采用并联机构（parallel manipulator），通过多根连杆将动平台与静平台连接，形成闭环运动链。相比串联机器人，并联结构具有更高的刚度、承载能力和定位精度。

1. **并联运动学**：设主动关节变量为 $\boldsymbol{\theta}\in\mathbb{R}^m$，动平台位姿为 $\mathbf{x}\in SE(3)$，正/逆运动学满足

$$
   \mathbf{x}=f(\boldsymbol{\theta}),\quad \boldsymbol{\theta}=f^{-1}(\mathbf{x}).
   $$

对于 Moonlight，$m=3$，实现空间三自由度平移/转动。
2. **力控技术**：集成关节与末端力/力矩感知，力控响应频率达 1 kHz，力跟踪精度 0.4–0.5 N。
3. **安全与通信**：达到 PLd 安全等级，采用 EtherCAT 总线实现多轴协同与故障保护。
4. **软件平台**：支持 Flexiv Elements 与 Flexiv RDK，提供点位示教、零重力拖拽示教与离线编程。

## 关键参数表

| 参数 | 数值 / 说明 |
|---|---|
| 构型 | 空间三自由度并联机器人 |
| 标准负载 | 7 kg |
| 慢速负载 | 12 kg |
| TCP 线速度 | ＞1.5 m/s |
| 工作范围直径 | 800 mm（最大工作直径 1200 mm） |
| 工作高度 | 400 mm |
| 重复定位精度 | ±0.03 mm |
| 力控响应频率 | 1 kHz |
| 力控跟踪精度 | 0.4–0.5 N |
| 防护等级 | IP65 |
| 自重 | 38 kg |
| 通信协议 | EtherCAT |
| 安全等级 | PLd |
| 安装方式 | 正装、倒装或任意角度 |

## 应用场景

- **精密装配**：力控搜孔、误差自适应插装。
- **表面处理**：打磨、去毛刺、曲面跟踪与贴合。
- **搬运分拣**：小件高速拾取与放置。
- **上下料**：与 CNC、注塑机等设备协同。
- **柔性产线**：快速换线、紧凑空间部署。

## 供应链关系

- **上游**：谐波/行星减速器、伺服电机、力/力矩传感器、控制器、铝合金结构件供应商。
- **同层**：非夕科技作为整机与算法供应商，提供 Moonlight 机器人、力控算法、Flexiv Elements/RDK 软件平台。
- **下游**：3C、汽车零部件、金属加工、家电等行业制造商与自动化集成商。

## 来源与验证

- 非夕 Moonlight 玄晖产品页：https://www.flexiv.cn/product/enlight
- 非夕科技发布新闻：https://www.flexiv.cn/news/launch_parallel_robot_moonlight
- 2024 工博会报道：https://www.sohu.com/a/811364322_120988576