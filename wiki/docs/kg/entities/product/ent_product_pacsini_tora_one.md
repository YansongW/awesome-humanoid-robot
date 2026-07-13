---
id: ent_product_pacsini_tora_one
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 帕西尼 TORA-ONE 人形机器人
  en: Pacsini TORA-ONE Humanoid Robot
status: active
sources:
- id: src_ent_product_pacsini_tora_one_1
  type: website
  url: https://rbtx.se/sv-SE/components/humanoid/paxini-tora-one-humanoid-robot-21-dof
- id: src_ent_product_pacsini_tora_one_2
  type: website
  url: https://www.awesomerobots.xyz/robots/openloong-tora-one
- id: src_ent_product_pacsini_tora_one_3
  type: website
  url: https://www.aparobot.com/robots/tora-one
- id: src_ent_product_pacsini_tora_one_4
  type: website
  url: https://humanoid.guide/product/toraone/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 帕西尼 TORA-ONE 人形机器人

## 概述

TORA-ONE 是帕西尼感知科技（Pacsini Technology）推出的轮式人形机器人，以“多维触觉 + AI 视觉”双模态感知为核心卖点。该机器人采用可升降躯干设计，站立高度可在 1.46–1.86 m 之间调节，全身具备 47 个自由度，其中双手占 26 个自由度，集成近 2,000 个 ITPU 多维触觉传感单元，可感知三维力/力矩、压力、摩擦、柔软度与温度等信息，面向工业制造、医疗健康、物流仓储与公共服务等场景。

## 工作原理 / 技术架构

TORA-ONE 的感知系统由五颗单目相机、两颗深度相机、LiDAR 与激光 SLAM 构成 360° 环境感知，同时通过 ITPU（Intelligent Tactile Processing Unit）阵列实现接触级触觉感知。ITPU 阵列的触觉通道数为 7,824，触觉传感单元数为 1,956，平均每个单元对应 4 路信号通道。

触觉传感器的空间分辨率与力控分辨率共同决定精细操作能力。官方宣称 TORA-ONE 的触觉力识别精度达到 0.01 N，则单臂定位精度 ±0.05 mm 对应的位置分辨率为

$$
\Delta x = \pm 0.05\ \mathrm{mm}
$$

该指标使其能够完成插拔、分拣、按压等精密装配任务。

在自由度分配上，47 DOF 可分解为 21 个躯干/臂/颈自由度与 26 个手部自由度。双手采用四指仿生结构，每手 13 个主动自由度，配合空心杯电机驱动与 EtherCAT/Modbus 通信，实现类人手部的灵活抓握。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | 帕西尼感知科技 / Pacsini Technology | 官方 |
| 机器人形态 | 轮式人形机器人 | 多源报道 |
| 高度范围 | 1.46–1.86 m（可调） | RBTX / Awesome Robots |
| 总自由度 | 47 DOF（21 躯体 + 26 手部） | 多源报道 |
| 手部结构 | 四指仿生灵巧手 | 官方 |
| 触觉传感单元 | 1,956 个 ITPU | Awesome Robots / Aparobot |
| 触觉信号通道 | 7,824 路 | 多源报道 |
| 触觉力识别精度 | 0.01 N | 官方 |
| 单臂负载 | 5–6 kg（部分资料称最高 8 kg） | RBTX / Aparobot |
| 臂部重复定位精度 | ±0.05 mm | RBTX / Awesome Robots |
| 视觉系统 | 5 颗单目相机 + 2 颗深度相机 | Aparobot |
| 导航系统 | 激光 SLAM + LiDAR | 多源报道 |
| 移动速度 | 约 0.6–1.0 m/s | RBTX |
| 续航 | 最高约 8 小时 | Awesome Robots |
| 重量 | 未公开 | 未公开 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **工业精密装配**：利用高分辨率触觉反馈完成插件、拧螺丝、柔性物件装配与质量检测。
- **物流仓储分拣**：处理异形、易碎、柔软物品，实现安全可靠的柔性抓取。
- **医疗健康辅助**：在康养与康复场景中提供辅助抓取、物品递送与人机交互。
- **公共服务与商超**：迎宾、导购、安检与互动展示。

## 供应链关系

TORA-ONE 是 `ent_company_pacsini` 的旗舰整机产品。其关键零部件包括自研 `ent_component_pacsini_px6ax` 触觉传感单元、`ent_product_pacsini_dexh13` 多维触觉灵巧手，以及外购的空心杯电机、深度相机、LiDAR、计算平台与电池。下游客户面向人形机器人 OEM、汽车主机厂、物流仓储与医疗康养机构。知识图谱关键关系：

- `ent_company_pacsini` -- `manufactures` --> `ent_product_pacsini_tora_one`
- `ent_product_pacsini_tora_one` -- `uses` --> `ent_product_pacsini_dexh13`
- `ent_product_pacsini_dexh13` -- `uses` --> `ent_component_pacsini_px6ax`

## 来源与验证

- TORA-ONE 的高度、自由度、触觉传感器数量、负载与定位精度等核心参数来自 RBTX、Awesome Robots 与 Aparobot 产品页。
- 帕西尼官方技术背景（ITPU、0.01 N 力控、DexH13 灵巧手）与供应链关系参考附录 D 中 `company_pacsini` Wiki。
- 整机重量与具体电机/减速比参数厂商未公开，已标注为“未公开”。