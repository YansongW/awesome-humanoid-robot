---
id: ent_component_rockchip_rk3576_soc
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 瑞芯微 RK3576 系统级芯片
  en: Rockchip RK3576 SoC
status: active
sources:
- id: src_rockchip_rk3576_datasheet
  type: document
- title: Rockchip RK3576 Brief Datasheet
  url: https://cdn.flipper.net/rk3576_brief_datasheet_v1_2_20240311.pdf
- id: src_rockchip_rk3576_debix
  type: website
- title: DEBIX Rockchip RK3576 AI SBC Specifications
  url: https://debix.io/product/debix-r3576-01/
- id: src_rockchip_rk3576_boardcon
  type: website
- title: Boardcon Idea3576 SBC Features Rockchip RK3576
  url: https://www.electronics-lab.com/boardcon-idea3576-sbc-features-rockchip-rk3576-soc-with-6-tops-npu-dual-ethernet-and-4k-multimedia-support/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications compiled from Rockchip brief datasheet, development
    board vendors and public reports; missing values marked as 未公开.
---


# 瑞芯微 RK3576 系统级芯片 / Rockchip RK3576 SoC

## 概述

RK3576 是瑞芯微（Rockchip）面向中高端 AIoT、工业网关、教育机器人与边缘 AI 设备推出的系统级芯片（SoC）。它采用 big.LITTLE 八核 CPU 架构，集成 Mali-G52 GPU、6 TOPS NPU、4K/8K 多媒体编解码引擎与丰富的工业接口，在功耗、算力与成本之间取得平衡，是机器人主控、智能相机与边缘 AI 盒子的常见选择。

## 工作原理 / 技术架构

RK3576 基于异构多核架构设计：

- **CPU**：4× Arm Cortex-A72 @ 最高 2.2 GHz（性能核）+ 4× Arm Cortex-A53 @ 最高 2.0 GHz（能效核），部分资料也记载为 1.8 GHz，并集成一颗 Cortex-M0 MCU 用于低功耗实时任务。
- **NPU**：自研神经网络处理单元，INT8 峰值算力约 6 TOPS，支持 INT4/INT8/INT16/FP16/BF16/TF32 混合精度。
- **GPU**：Arm Mali-G52 MC3 @ 约 0.9 GHz，支持 OpenGL ES 3.2、OpenCL 2.0、Vulkan 1.1。
- **多媒体**：4K@120 fps 解码（H.265/HEVC、VP9、AV1、AVS2），4K@60 fps 编码（H.265/H.264），部分公开资料提到支持 8K@30 fps 解码；内置 16 MP ISP，支持 HDR、3DNR 与多路相机输入。
- **内存与接口**：支持 LPDDR4/LPDDR4X/LPDDR5 与 DDR4，最高可选 8 GB；提供 PCIe、USB 3.0/3.2、GbE、MIPI CSI/DSI、HDMI 2.1/eDP、CAN-FD 等接口。

AI 推理吞吐能力可近似表示为：

\[
\text{OPS} = \text{MAC}_{\text{peak}} \times 2 \times \text{utilization}
\]

其中 6 TOPS 为标称 INT8 峰值，实际有效吞吐受模型结构、内存带宽与量化策略影响。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 未公开（公开报道推测为先进 FinFET/8 nm 级） | 行业分析 |
| CPU | 4× Cortex-A72 @ 2.2 GHz + 4× Cortex-A53 @ 2.0 GHz + Cortex-M0 | Flipper / DEBIX |
| GPU | Arm Mali-G52 MC3 @ ~0.9 GHz | DEBIX / Boardcon |
| NPU | 6 TOPS @ INT8 | Rockchip 公开资料 |
| 精度支持 | INT4/INT8/INT16/FP16/BF16/TF32 | DEBIX |
| 内存支持 | LPDDR4/LPDDR4X/LPDDR5/DDR4，最高 8 GB | 公开资料 |
| 视频解码 | 4K@120 fps（H.265/VP9/AV1/AVS2），部分资料称 8K@30 fps | DEBIX / Boardcon |
| 视频编码 | 4K@60 fps（H.265/H.264） | DEBIX |
| ISP | 16 MP，支持 HDR、3A、3DNR、LDC | DEBIX |
| 显示输出 | HDMI 2.1（4K@120 fps）、eDP 1.3（4K@60 fps）、MIPI DSI（2K@60 fps） | DEBIX |
| 相机接口 | 2× MIPI CSI D-PHY，支持 D/CPHY | DEBIX |
| 高速接口 | PCIe 3.0/2.1、USB 3.2 Gen1 Type-C/OTG、双 GbE、SATA 3.1 | DEBIX / Boardcon |
| 其他接口 | CAN-FD ×2、I2C、SPI、UART、ADC、GPIO | DEBIX |
| 典型功耗 | 约 3–8 W（整板），重载约 10 W | 公开报道 |
| 封装 | 未公开 | — |
| 价格 | 未公开 | — |

## 应用场景

- **机器人主控**：多路相机输入、SLAM、路径规划与机械臂控制，常见于教育机器人、服务机器人与轻量工业机器人。
- **工业网关与边缘 AI 盒子**：双千兆网、多路串口与 CAN-FD 适合工厂数据采集与本地 AI 推理。
- **智能商显与自助终端**：4K 多媒体输出与触控交互支持数字标牌、Kiosk 等设备。

## 供应链关系

RK3576 由 **瑞芯微电子股份有限公司（Rockchip，实体 `ent_company_rockchip`）** 设计。上游依赖台积电/中芯国际等晶圆代工、ARM CPU/GPU IP、自研 NPU、LPDDR 存储与封测；下游客户包括机器人整机厂、工业平板/网关厂商、NVR/安防客户、商显与教育设备商。在知识图谱中，该 SoC 实体通过 `manufactures` 关系与公司节点 `ent_company_rockchip` 相连，并可通过 `uses` 关系嵌入到机器人主控产品节点中。

## 来源与验证

- Rockchip RK3576 Brief Datasheet（https://cdn.flipper.net/rk3576_brief_datasheet_v1_2_20240311.pdf）
- DEBIX RK3576 SBC 规格页（https://debix.io/product/debix-r3576-01/）
- Boardcon Idea3576 报道（https://www.electronics-lab.com/boardcon-idea3576-sbc-features-rockchip-rk3576-soc-with-6-tops-npu-dual-ethernet-and-4k-multimedia-support/）

制程、封装与单价等参数在公开渠道未完整披露，已标注为“未公开”。