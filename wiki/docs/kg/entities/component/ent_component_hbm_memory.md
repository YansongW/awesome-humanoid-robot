---
id: ent_component_hbm_memory
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 高带宽存储器（HBM）
  en: High Bandwidth Memory (HBM)
status: active
sources:
- id: src_jedec_hbm3_techspot
  type: website
  url: https://www.techspot.com/news/93182-hbm3-twice-fast-hbm2e-up-819-gbs-stack.html
- id: src_hbm_evolution_eefocus
  type: website
  url: https://www.eefocus.com/article/2045349.html
- id: src_hbm3_hothardware
  type: website
  url: https://hothardware.com/news/hbm3-specification-819gbs-bandwidth
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 高带宽存储器（HBM）/ High Bandwidth Memory (HBM)

## 概述

高带宽存储器（HBM）是一种基于 3D 堆叠 DRAM 与硅中介层（silicon interposer）封装的高性能存储技术，由 JEDEC 标准化。与传统 GDDR 相比，HBM 通过极宽的并行总线（每堆栈 1024 bit 或更高）实现更高的内存带宽，并通过 3D 堆叠提高存储密度，同时降低单位比特功耗。HBM 已成为人工智能训练/推理加速卡、高性能计算 GPU 以及先进机器人感知与策略计算平台的核心存储部件。

## 工作原理 / 技术架构

HBM 的核心架构包括：

- **3D TSV 堆叠**：多颗 DRAM 裸片通过硅通孔（Through-Silicon Via, TSV）与微凸点（micro-bump）垂直堆叠，再与底层逻辑/接口裸片连接。
- **宽总线接口**：每颗 HBM 堆栈通过 1024-bit（HBM2/HBM2E/HBM3）或 2048-bit（HBM4）数据总线与 GPU/加速器连接，分为多个独立通道（channel）与伪通道（pseudo-channel）。
- **硅中介层 2.5D 封装**：HBM 与计算芯片并排放置在硅中介层上，缩短互连长度，降低信号延迟与功耗。

单堆栈理论带宽可按下式估算：
\[
B = \frac{W \times R}{8}
\]
其中 \(B\) 为带宽（GB/s），\(W\) 为总线位宽（bit），\(R\) 为每引脚数据速率（Gbps）。例如 HBM3 在 1024-bit 总线、6.4 Gbps/pin 时：
\[
B = \frac{1024 \times 6.4}{8} = 819.2\,\text{GB/s}
\]

单堆栈容量为
\[
C = N_{\text{die}} \times C_{\text{die}}
\]
其中 \(N_{\text{die}}\) 为堆叠裸片数，\(C_{\text{die}}\) 为单裸片容量。

## 关键参数表

| 参数项 | HBM2 | HBM2E | HBM3 | HBM3E | HBM4（规划） |
|---|---|---|---|---|---|
| JEDEC 标准 | JESD235B | JESD235C | JESD238 | JESD238A | JESD270-4 |
| 总线位宽 | 1024 bit | 1024 bit | 1024 bit | 1024 bit | 2048 bit |
| 每引脚速率 | 2.4 Gbps | 3.6 Gbps | 6.4 Gbps | 9.2–12.4 Gbps | 6.4–12.8 Gbps |
| 单堆栈带宽 | 307 GB/s | 460 GB/s | 819 GB/s | 1.2–1.33 TB/s | 2.0–3.3 TB/s |
| 最大堆叠层数 | 8 | 8/12 | 8/12/16 | 8/12 | 4/8/12/16 |
| 单堆栈容量 | 8 GB | 16 GB | 16–64 GB | 24–36 GB | 64 GB |
| 通道数 | 8 | 8 | 16 | 16 | 32 |
| 工作电压 | 1.2 V | 1.2 V | 1.1 V | 1.1 V | 1.05 V |

注：HBM4 为 JEDEC 规划目标，实际产品规格以厂商发布为准。

## 应用场景

- **AI 训练与推理加速器**：NVIDIA H100、AMD MI300 及国产沐曦 MXC 系列等 GPU/AI 芯片的显存。
- **高性能计算（HPC）**：气候模拟、分子动力学、流体仿真等内存带宽受限型应用。
- **自动驾驶与机器人**：处理多路摄像头、激光雷达点云与端到端策略模型的大规模并行数据。

## 供应链关系

- **上游**：DRAM 裸片制造（三星、SK 海力士、美光）、TSV 与 2.5D 封装（台积电、Amkor 等）、硅中介层与基板。
- **中游**：HBM 堆栈供应商（三星、SK 海力士、美光）向 GPU/AI 芯片厂商供货。
- **下游**：AI 加速器、数据中心 GPU、机器人计算平台（如沐曦 C500 采用 HBM2E）。
- **图谱位置**：`ent_component_hbm_memory` 通过 `used_in` 关系连接 `ent_product_metax_mxc` 等高性能计算芯片。

## 来源与验证

- HBM 各代带宽、容量、电压与通道数来自 TechSpot、HotHardware 与与非网对 JEDEC 标准的公开解读。
- 具体厂商产品参数（如 HBM2E 容量）以三星、SK 海力士、美光官方 datasheet 为准；本表列出的为 JEDEC 标准上限或主流公开规格。