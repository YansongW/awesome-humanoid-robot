---
id: ent_product_mediatek_genio_700
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: MediaTek Genio 700 边缘 AI IoT 平台
  en: MediaTek Genio 700 Edge AI IoT Platform
status: active
sources:
- id: src_mediatek_genio700_factsheet
  type: document
  url: https://www.mediatek.com/hubfs/Factsheet-Genio-700.pdf
- title: MediaTek Genio 700 Factsheet
- id: src_mediatek_genio700_page
  type: website
  url: https://genio.mediatek.com/genio-700
- title: MediaTek Genio 700 Product Page
- id: src_ubergizmo_genio700
  type: article
  url: https://www.ubergizmo.com/2023/01/mediatek-genio-700-iot-soc/
- title: MediaTek Genio 700 IoT SoC
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# MediaTek Genio 700 / MediaTek Genio 700

## 概述

MediaTek Genio 700（MT8390）是联发科面向高端物联网与边缘 AI 应用推出的系统级芯片（SoC），采用 6 nm 制程，集成八核 CPU、Mali-G57 GPU、第五代 AI 处理器（NPU）以及双 ISP、双显示输出和丰富的外设接口。Genio 700 定位于智能零售、工业物联网、智能家居、机器人边缘网关等场景，产品生命周期可持续至 2034 年。

## 工作原理 / 技术架构

Genio 700 采用异构集成架构，将通用计算、图形渲染、AI 推理、多媒体编解码与实时控制整合在单芯片中：

1. **CPU**：2× Arm Cortex-A78 @ 2.2 GHz + 6× Arm Cortex-A55 @ 2.0 GHz，负责操作系统与复杂应用。
2. **GPU**：Arm Mali-G57 MC3 @ 950 MHz，支持 OpenGL ES 3.2、Vulkan 1.1、OpenCL 2.2。
3. **NPU**：MediaTek 第五代 NPU（1× MDLA3.0 + 1× Tensilica VP6），INT8 峰值算力

$$
   \text{TOPS}_{\text{NPU}}=4.0.
   $$

4. **多媒体**：双 ISP 支持 32 MP 单摄或 16 MP+16 MP 双摄；视频解码 4K75，编码 4K30；双 4K 显示输出。
5. **连接与外设**：USB 3.2 Gen1、PCIe 2.0 x1、GbE（TSN）、UART/SPI/I2C/I3C、Wi-Fi/BT 外接组合模块。

NPU 推理能效可近似表示为

$$
E_{\text{infer}}=\frac{O}{P}=\frac{4\ \text{TOPS}}{P_{\text{SoC}}},
$$

其中 $O$ 为峰值算力，$P_{\text{SoC}}$ 为整机功耗，具体数值依赖于负载与散热条件。

## 关键参数表

| 参数 | 数值 / 说明 |
|---|---|
| 制程 | 6 nm |
| CPU | 2× Cortex-A78 @ 2.2 GHz + 6× Cortex-A55 @ 2.0 GHz |
| GPU | Arm Mali-G57 MC3 @ 950 MHz |
| NPU | MediaTek 5th-Gen，4.0 TOPS |
| 内存 | LPDDR4X-3733，最高 8 GB |
| 存储 | eMMC 5.1 / SD 3.0 / SPI-NOR |
| 显示 | 双 4K（4K60 + 4K30） |
| 摄像头 | 双 ISP，32 MP 单摄 / 16 MP+16 MP 双摄 @ 30 fps |
| 视频编解码 | 解码 4K75；编码 4K30 |
| 高速接口 | USB 3.2 Gen1、PCIe 2.0 x1、GbE TSN |
| 封装 | VFBGA 15×15×0.9 mm，0.4 mm ball pitch |
| 产品寿命 | 可供应至 2034 年 |

## 应用场景

- **智能零售**：数字标牌、自助结算、客流分析。
- **工业物联网**：预测性维护、机器视觉质检、边缘网关。
- **智能家居**：智能音箱、中控面板、安防摄像头。
- **机器人**：机器人边缘控制器、视觉导航、多模态交互。
- **智慧城市**：能源管理、交通监控。

## 供应链关系

- **上游**：台积电 6 nm 晶圆代工、LPDDR 存储、PMIC、Wi-Fi/BT 组合模块、PCB 与被动元件供应商。
- **同层**：联发科提供 SoC、参考设计、MediaTek IoT Yocto SDK；SECO、Grinn、Boundary Devices 等模块/单板厂商基于 Genio 700 开发 SOM/SBC。
- **下游**：智能终端 OEM、机器人厂商、工业设备制造商。

## 来源与验证

- MediaTek Genio 700 Factsheet：https://www.mediatek.com/hubfs/Factsheet-Genio-700.pdf
- MediaTek Genio 700 产品页：https://genio.mediatek.com/genio-700
- Ubergizmo 报道：https://www.ubergizmo.com/2023/01/mediatek-genio-700-iot-soc/