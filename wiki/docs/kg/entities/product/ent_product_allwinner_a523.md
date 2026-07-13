---
id: ent_product_allwinner_a523
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 全志 A523
  en: Allwinner A523
status: active
sources:
- id: src_allwinner_a523_linux_sunxi
  type: website
  url: https://linux-sunxi.org/A523
- title: Allwinner A523 — linux-sunxi.org
- id: src_allwinner_a523_cnx
  type: website
  url: https://www.cnx-software.com/2023/07/06/allwinner-a523-octa-core-cortex-a55-processor-to-show-up-in-tablets-sbcs/
- title: Allwinner A523 octa-core Cortex-A55 processor to show up in tablets, SBCs
- id: src_allwinner_a523_notebookcheck
  type: website
  url: https://www.notebookcheck.net/Helio-G80-vs-A523-vs-Helio-G88_12221_17339_14007.247596.0.html
- title: Processor Comparison - Allwinner A523 Specifications
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 全志 A523 / Allwinner A523

## 概述

全志 A523 是全志科技（Allwinner Technology）于 2023 年推出的面向平板电脑、交互式显示及边缘 AI 应用的八核 ARM SoC。该芯片采用 22 nm HPC 工艺，集成两个四核 ARM Cortex-A55 集群、玄铁 E906 RISC-V 实时管理核心、Mali-G57 GPU 以及约 2 TOPS 的 AI 加速器，主打高性价比的多媒体处理与轻量级 AI 推理。

## 工作原理 / 技术架构

### CPU 与微架构
A523 采用 big.LITTLE（DynamIQ）式八核 Cortex-A55 配置：

- **性能集群**：4× Cortex-A55 @ 最高 1.8 GHz，每核 128 KB L2 缓存；
- **能效集群**：4× Cortex-A55 @ 最高 1.42 GHz，每核 64 KB L2 缓存；
- **共享 L3 缓存**：1 MB；
- **实时协控**：XuanTie E906 RISC-V @ 200 MHz，用于功耗管理与实时任务。

Cortex-A55 为顺序执行、双发射 ARMv8.2-A 微架构，支持 NEON SIMD、VFP4、AES 加密扩展与 FP16 运算，适合轻量级控制与媒体处理。

### GPU 与 NPU
- **GPU**：ARM Mali-G57 MC1-2EE，支持 OpenGL ES 3.2、Vulkan 1.0、OpenCL 2.0；
- **AI 加速器**：集成约 2 TOPS INT8 算力的 NPU，用于语音唤醒、图像分类、目标检测等边缘 AI 任务。

### 多媒体与接口
- 视频解码：4K@60fps H.265 / HEVC；
- 视频编码：4K@25fps H.264；
- 内存：32-bit DDR3 / DDR4 / LPDDR2 / LPDDR3 / LPDDR4 / LPDDR4X，最高 4 GB；
- 显示：双 4-lane MIPI-DSI、Dual-LVDS、RGB、eDP 1.3（最高 2560×1600@60Hz）、HDMI 2.0；
- 摄像头：8M ISP + 双 4-lane MIPI-CSI；
- 高速接口：1× USB 3.0（与 PCIe 2.1×1 复用）、2× USB 2.0、GMAC 千兆以太网；
- 封装：FCCSP 522-ball，15 mm × 15 mm，0.5 mm 球距。

算力密度可用下式近似：

$$
\eta_{\text{AI}} = \frac{2\ \text{TOPS}}{T_{\text{dp}}} \approx 0.29\ \text{TOPS/W}
$$

其中典型热设计功耗 TDP 约为 7 W（来源为第三方对比数据库）。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 工艺制程 | 22 nm HPC |
| CPU | 8× ARM Cortex-A55（4×1.8 GHz + 4×1.42 GHz） |
| 实时核心 | XuanTie E906 RISC-V @ 200 MHz |
| L2 缓存 | 128 KB / 64 KB 每核 |
| L3 缓存 | 1 MB |
| GPU | ARM Mali-G57 MC1-2EE |
| AI 算力 | 约 2 TOPS INT8 |
| 内存支持 | DDR3/DDR4/LPDDR2/3/4/4X，最高 4 GB |
| 视频解码 | 4K@60fps H.265 |
| 视频编码 | 4K@25fps H.264 |
| 显示输出 | MIPI-DSI / LVDS / RGB / eDP / HDMI 2.0 |
| 摄像头 | 8M ISP，双 MIPI-CSI |
| 高速接口 | USB 3.0（与 PCIe 2.1×1 复用）、GMAC |
| 典型 TDP | 约 7 W |
| 封装 | FCCSP 522-ball，15 mm × 15 mm |

## 应用场景

- **教育平板与交互屏**：多路显示与触控驱动；
- **智能家居网关**：多传感器接入与本地语音控制；
- **轻量级机器人控制板**：用于轮式服务机器人、清洁机器人、低复杂度人形机器人的主控或协处理；
- **边缘 AI 盒子**：2 TOPS NPU 可运行轻量化视觉模型。

## 供应链关系

Allwinner A523 处于机器人供应链的上游“计算与控制芯片”层：

- **芯片设计**：全志科技（Allwinner Technology）；
- **晶圆代工**：22 nm 工艺由外部代工厂（未公开）制造；
- **下游整机**：被平板、教育终端、智能家居及中低端机器人厂商采用；
- **生态**：Linux/Android SDK、linux-sunxi 开源社区支持。

## 来源与验证

- linux-sunxi 社区 A523 页面（https://linux-sunxi.org/A523）
- CNX Software 技术报道（2023-07-06）
- Notebookcheck 处理器对比数据库

> 注：全志官方未公开完整 datasheet，部分参数（如 NPU 精确算力、TDP）来自社区拆机与第三方评测，标注为“约”。