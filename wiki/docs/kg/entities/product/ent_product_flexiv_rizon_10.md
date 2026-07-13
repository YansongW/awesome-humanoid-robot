---
id: ent_product_flexiv_rizon_10
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 非夕 Rizon 10
  en: Flexiv Rizon 10
status: active
sources:
- id: src_flexiv_rizon
  type: website
  url: https://www.flexiv.cn/product/rizon
- title: 自适应机器人 | 拂晓 Rizon | 非夕科技
- id: src_flexiv_rizon10_reddot
  type: website
  url: https://www.flexiv.cn/news/rizon10_got_reddot_award_bestofthebest
- title: 自适应机器人 Rizon 10 斩获红点奖最高奖项 | 非夕科技
- id: src_flexiv_rizon_automate
  type: website
  url: https://www.automate.org/products/flexiv-robotics/rizon-10
- title: Rizon 10 | 7-axis Adaptive Robot | Flexiv
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 非夕 Rizon 10 / Flexiv Rizon 10

## 概述

Flexiv Rizon 10（中文名“非夕 Rizon 10”或“拂晓 10”）是非夕科技推出的高负载七轴自适应机器人，深度融合工业级力控、机器视觉与 AI 技术。区别于传统位置控制机械臂，Rizon 10 采用全身力控架构，可在位置误差、外部扰动与工件公差范围内自适应调整接触力，适用于精密装配、抛光、插拔与协作搬运等任务。该产品曾获 2022 年红点奖产品设计组别最高奖项“Best of the Best”。

## 工作原理 / 技术架构

Rizon 10 为 7 自由度冗余机械臂，每个关节集成力矩传感器，形成全臂力感知闭环。其阻抗控制（impedance control）将末端力-位关系建模为二阶系统：

$$
M_d \ddot{x} + D_d \dot{x} + K_d (x - x_d) = F_{\text{ext}}
$$

其中 $M_d$、$D_d$、$K_d$ 分别为期望惯性、阻尼与刚度矩阵，$x$ 为实际位置，$x_d$ 为期望位置，$F_{\text{ext}}$ 为外部环境作用力。通过调节 $K_d$ 与 $D_d$，机器人可在高刚度定位与柔顺接触之间切换。

末端力控精度达 0.2 N，力控跟踪精度 0.5 N，最大可控力范围 350 N。重复定位精度 ±0.05 mm（ISO 9283）。七轴冗余构型使其能够规避奇异点，在狭小空间内以灵活姿态完成作业。

Rizon 10 配备 Hesper 控制器，支持 Flexiv RDK SDK 与图形化示教器，并可选配腕部六维力/力矩传感器（Rizon 10 + F/T Sensor），将力感知精度提升至 0.1 N。

## 关键参数表

| 参数 | Rizon 10 | Rizon 10 + F/T Sensor | 备注 |
|------|----------|----------------------|------|
| 自由度 | 7 | 7 | 冗余构型 |
| 额定负载 | 10 kg | 10 kg | 末端负载 |
| 自重 | 38 kg | 39 kg | 官方产品页 |
| 臂展 | 941 mm | 984 mm | 关节 1 到腕部中心 |
| 重复定位精度 | ±0.05 mm | ±0.05 mm | ISO 9283 |
| 力感知精度 | 0.2 N | 0.1 N | 全身 / 腕部 |
| 力控跟踪精度 | 0.5 N | 未公开 | 官方资料 |
| 最大可控力范围 | 350 N | 350 N | 官方资料 |
| 标准末端线速度 | 1.0 m/s | 1.0 m/s | 官方产品页 |
| 防护等级 | IP65 | IP65 | 防尘防水 |
| 安装位置 | 任意 | 任意 | 落地/倒置/侧挂 |
| 运行温度 | 0–45 ℃ | 0–45 ℃ | 官方产品页 |
| 湿度 | 20%–80% 非凝结 | 20%–80% 非凝结 | 官方产品页 |
| 噪声 | <70 dB | <70 dB | 官方产品页 |
| 工具输出法兰 | ISO 9409-1-50-4-M6 | ISO 9409-1-50-4-M6 | 官方产品页 |
| 安全认证 | CE / ETL / ISO 13849-1 PL d Cat.3 | 同上 | 官方资料 |

## 应用场景

- **精密装配**：连接器插拔、PCB 装配、汽车零部件压装，通过力控避免过盈配合损伤。
- **表面加工**：打磨、抛光、去毛刺，利用恒力控制保证加工一致性。
- **柔性搬运**：装配线上的零件取放，允许工件位置存在毫米级偏差。
- **医疗/食品**：IP65 防护与力控安全特性适用于对卫生与安全要求较高的环境。
- **科研平台**：作为全身力控自适应机械臂，用于力控算法与人机协作研究。

## 供应链关系

Flexiv Rizon 10 属于 **协作机器人/自适应机器人整机层**，核心零部件包括谐波减速器/行星减速器、力矩电机、关节力矩传感器、视觉相机、控制器与结构件。非夕科技自研力控算法、AI 视觉与机器人操作系统，向下游 3C、汽车、医疗、新零售等行业提供机器人本体与自适应解决方案。其在产业链中位于核心零部件与终端应用之间，强调“力控 + AI”的技术差异化。

## 来源与验证

- 非夕科技官方 Rizon 产品页：https://www.flexiv.cn/product/rizon
- 非夕科技红点奖新闻稿：https://www.flexiv.cn/news/rizon10_got_reddot_award_bestofthebest
- Automate.org 产品页：https://www.automate.org/products/flexiv-robotics/rizon-10

Rizon 10 与 Rizon 10 + F/T Sensor 的部分参数（如臂展、力感知精度）存在配置差异，表中已分别列出；未公开项以官方产品页为准。