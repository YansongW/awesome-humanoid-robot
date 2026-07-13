---
id: ent_product_pacsini_dexh13
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 帕西尼 DexH13 多维触觉灵巧手
  en: Pacsini DexH13 Tactile Dexterous Hand
status: active
sources:
- id: src_pacsini_official
  type: website
  url: https://paxini.com
- id: src_pacsini_dexh13
  type: website
  url: https://paxini.com/cn/dex/gen2
- id: src_stdaily_pacsini
  type: website
  url: https://www.stdaily.com/web/gdxw/2025-04/28/content_332431.html
- id: src_36kr_pacsini
  type: website
  url: https://m.36kr.com/p/3006232413757953
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 帕西尼 DexH13 多维触觉灵巧手

## 概述

DexH13 是帕西尼感知科技（Pacsini Technology）推出的全球首款融合“多维触觉 + AI 视觉”双模态的四指仿生灵巧手。单手集成 **1140 个 ITPU 多维触觉传感单元**、**800 万像素 RGB AI 手眼相机**与 **16 个自由度（13 主动 + 3 被动）**，可同步捕捉三维力、三维力矩、接触位置、材质、温度、硬度等 15 种触觉信息，力控分辨率达 **0.01 N**，采样频率 **1000 Hz**，额定负载 **5 kg**，工业寿命超过 **100 万次**。

## 工作原理 / 技术架构

DexH13 基于帕西尼自研的 6D 霍尔阵列式 ITPU（Intelligent Tactile Processing Unit）触觉传感技术。每个 ITPU 单元通过霍尔效应检测弹性体在受力时的磁场变化，从而解耦出法向力、剪切力、力矩及材质、温度、滑动等多维信息。

触觉信号总数由单元数量与每单元通道数决定：

$$
N_{\text{channels}} = N_{\text{ITPU}} \times n_{\text{ch/ITPU}}
$$

公开资料称 DexH13 单手触觉信号路数为 **3420 路**，对应每个 ITPU 平均输出约 3 路独立信号。指尖力 $F_{\text{tip}}$ 最大 **15 N**，额定负载 $m = 5 \ \text{kg}$，对应可承受的重力载荷为：

$$
F_g = m \cdot g = 5 \times 9.8 \approx 49 \ \text{N}
$$

该负载为整手抓取能力指标，非单指指标。灵巧手由空心杯电机驱动，支持 EtherCAT / Modbus 通信，最小开合时间 **1.5 s**。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 制造商 | 帕西尼感知科技 / Pacsini Technology |
| 手指数量 | 4 |
| 自由度 | 16（13 主动 + 3 被动） |
| 触觉传感单元 | 1140 个 ITPU 多维触觉传感单元 |
| 触觉信号路数 | 3420 路 |
| 视觉能力 | 800 万像素高清 RGB AI 手眼相机 |
| 触觉感知维度 | 15 种（三维力/力矩、温度、材质、硬度、回弹等） |
| 力控分辨率 | 0.01 N |
| 采样频率 | 1000 Hz |
| 指尖力 | 15 N |
| 额定负载 | 5 kg |
| 最大抓握直径 | 15 cm |
| 最小开合时间 | 1.5 s |
| 驱动方式 | 空心杯电机驱动 |
| 通信协议 | EtherCAT / Modbus |
| 使用寿命 | 100 万次 |
| 重量 / 价格 | 未公开 |

## 应用场景

- **人形机器人灵巧操作**：抓取、拧转、按压、工具使用等复杂人手动作。
- **精密装配**：汽车产线插件、螺丝拧紧、柔性物件装配。
- **物流仓储**：异形、易碎、柔软物品的柔性分拣与包装。
- **医疗康养**：辅助抓取、康复训练、假肢控制与微创手术训练。

## 供应链关系

在公司—产品—零部件网络中，DexH13 处于**机器人末端执行器产品层**：

- **上游**：霍尔传感器阵列、柔性基材、纳米敏感材料、空心杯电机、AI 视觉模组、信号处理 ASIC。
- **自身位置**：`ent_company_pacsini -- manufactures --> ent_product_pacsini_dexh13`；`ent_product_pacsini_dexh13 -- uses --> ent_component_pacsini_px6ax`。
- **下游**：人形机器人 OEM、工业机器人、物流仓储、医疗康养、汽车主机厂及精密制造。

## 来源与验证

- 帕西尼感知科技官网：https://paxini.com
- 帕西尼 DexH13 产品页：https://paxini.com/cn/dex/gen2
- 科技日报报道：https://www.stdaily.com/web/gdxw/2025-04/28/content_332431.html
- 36Kr 深度报道：https://m.36kr.com/p/3006232413757953

手指数量、自由度、触觉单元数、相机像素、力控分辨率与使用寿命均来自帕西尼官方公开资料；重量与价格未公开。