---
id: ent_product_renesas_rz_v2n
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Renesas RZ/V2N 视觉 AI 微处理器
  en: Renesas RZ/V2N Vision AI MPU
status: active
sources:
- id: src_renesas_rzv2n_cn
  type: website
  url: https://www.renesas.cn/zh/products/rz-v2n
- title: Renesas RZ/V2N 产品页
- id: src_renesas_rzv2n_datasheet
  type: document
  url: https://www.renesas.com/en/document/dst/rzv2n-group-datasheet
- title: RZ/V2N Group Datasheet
- id: src_mouser_rzv2n
  type: article
  url: https://www.21ic.com/a/986969.html
- title: 贸泽开售 Renesas RZ/V2N 微处理器
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# Renesas RZ/V2N / Renesas RZ/V2N

## 概述

Renesas RZ/V2N 是瑞萨电子推出的视觉 AI 微处理器（MPU），面向需要低功耗、高性能嵌入式 AI 推理的摄像头、移动机器人、后装汽车电子等应用。该芯片集成瑞萨专有的 DRP-AI3 AI 加速器、四核 Arm Cortex-A55 应用处理器、Cortex-M33 实时处理器以及可选的 Mali-C55 ISP 与 Mali-G31 GPU，可在无额外散热器的条件下实现高算力视觉处理。

## 工作原理 / 技术架构

RZ/V2N 采用异构多核架构：

1. **应用处理**：四核 Arm Cortex-A55 @ 1.8 GHz，负责 Linux/Android 应用与中间件。
2. **实时控制**：Arm Cortex-M33 @ 200 MHz，用于低功耗管理与实时任务。
3. **AI 加速**：DRP-AI3（AI-MAC + DRP）支持稀疏/密集推理，峰值算力

$$
   \text{TOPS}_{\text{sparse}}=15,\quad \text{TOPS}_{\text{dense}}=4.
   $$

其能效约为 10 TOPS/W。
4. **视觉与多媒体**：可选 Mali-C55 ISP（最高 630 Mpixel/s）、Mali-G31 GPU、H.264/H.265 编解码器、MIPI CSI-2 / DSI。
5. **内存与接口**：支持 LPDDR4/LPDDR4X 32-bit（12.8 GB/s），双 GbE、USB 3.2 Gen2、PCIe Gen3 x2、CAN-FD、ADC 等。

芯片峰值算力与功耗的关系可写作

$$
P=\frac{\text{TOPS}}{\text{TOPS/W}}\approx\frac{15}{10}=1.5\ \text{W},
$$

表明其适用于电池供电或对热预算敏感的边缘设备。

## 关键参数表

| 参数 | 数值 / 说明 |
|---|---|
| 产品类型 | 视觉 AI MPU |
| CPU | 四核 Arm Cortex-A55 @ 1.8 GHz + Cortex-M33 @ 200 MHz |
| AI 加速器 | DRP-AI3 |
| AI 峰值性能 | 15 TOPS（稀疏）/ 4 TOPS（密集） |
| 能效 | 约 10 TOPS/W |
| 片上 SRAM | 1.5 MB（ECC） |
| 外部内存 | LPDDR4/LPDDR4X 32-bit，12.8 GB/s |
| ISP | 可选 Arm Mali-C55 |
| GPU | 可选 Arm Mali-G31 |
| 摄像头接口 | MIPI CSI-2 × 2（最多 4 lane） |
| 显示接口 | MIPI DSI × 1 |
| 高速接口 | PCIe Gen3 x2 lane、USB 3.2 Gen2、GbE ×2 |
| 封装 | 15×15 mm BGA，840 pin，0.5 mm 间距 |

## 应用场景

- **AI 摄像头**：人数统计、停车监控、安防识别。
- **移动机器人**：扫地机器人、割草机、服务/人形机器人视觉与导航。
- **后装汽车**：行车记录仪、驾驶员监控系统（DMS）。
- **工业视觉**：缺陷检测、质检、引导抓取。
- **人形机器人**：双目/多相机视觉前端与端侧大模型推理载体。

## 供应链关系

- **上游**：晶圆代工（TSMC 等）、封测、LPDDR 存储、PMIC、晶体振荡器供应商。
- **同层**：瑞萨电子作为芯片原厂提供 MPU、参考设计、评估板（RZ/V2N EVK）与软件栈。
- **下游**：摄像头模组厂商、机器人 OEM、汽车 Tier-1、工业视觉集成商。

## 来源与验证

- 瑞萨 RZ/V2N 中文产品页：https://www.renesas.cn/zh/products/rz-v2n
- RZ/V2N 数据手册：https://www.renesas.com/en/document/dst/rzv2n-group-datasheet
- 贸泽开售报道：https://www.21ic.com/a/986969.html