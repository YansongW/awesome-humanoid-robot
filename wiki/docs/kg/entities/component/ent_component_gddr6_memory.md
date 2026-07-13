---
id: ent_component_gddr6_memory
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: GDDR6 显存
  en: GDDR6 Memory
status: active
sources:
- id: src_jedec_gddr6
  type: website
  url: https://www.jedec.org/standards-documents/docs/jesd250
- id: src_micron_gddr6
  type: website
  url: https://www.anandtech.com/show/11543/micron-discusses-gddr5x-gddr6-and-gddr5
- id: src_samsung_gddr6
  type: website
  url: https://www.notebookcheck.net/The-NVIDIA-Quadro-RTX-GPUs-feature-Samsung-s-16-Gigabit-GDDR6-memory.323050.0.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# GDDR6 显存 / GDDR6 Memory

## 概述

GDDR6（Graphics Double Data Rate 6）是 JEDEC 制定的高带宽图形显存标准（JESD250），采用双 16-bit 独立通道、16n prefetch 架构，工作电压 1.35 V。其单 pin 数据率通常在 12–16 Gbps，高端产品可达 20–24 Gbps，广泛应用于 GPU、AI 加速器、游戏主机及高性能计算领域。

## 工作原理 / 技术架构

GDDR6 在每个时钟周期的上升沿与下降沿均传输数据，因此等效数据率为时钟频率的两倍。每颗芯片内部包含两个独立的 16-bit 通道，可同时处理不同请求，提升通道利用率。有效带宽由总线位宽与数据率共同决定：
\[
B=\frac{f_{\text{data}} \times W}{8},
\]
其中 \(f_{\text{data}}\) 为等效数据率（GT/s），\(W\) 为总线位宽（bit）。以 16 GT/s、256-bit 总线为例：
\[
B=\frac{16\times10^{9}\times256}{8}=512\ \text{GB/s}.
\]
PCIe 设备通常还需考虑 128b/130b 编码开销，但 GDDR6 芯片级带宽多用上述峰值表示。

## 关键参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 标准 | JEDEC JESD250 | JEDEC |
| 工作电压 | 1.35 V | Micron / Samsung |
| 单 pin 数据率 | 12–16 Gbps（量产），高端 20–24 Gbps | Micron / Samsung |
| 通道架构 | 每颗芯片 2×16-bit 独立通道 | AnandTech |
| Prefetch | 16n | AnandTech |
| 单颗容量 | 8 Gb / 16 Gb / 32 Gb | Micron |
| 64-bit 通道带宽（16 GT/s） | 128 GB/s | 计算 |
| 典型总线位宽 | 256-bit / 384-bit / 512-bit | GPU 应用 |
| 封装 | FBGA180 / FBGA190 | 行业资料 |

## 应用场景

- GPU 显存与图形渲染
- AI 训练/推理加速器
- 游戏主机内存
- 高性能计算（HPC）与数字孪生

## 供应链关系

GDDR6 由三星、美光、SK 海力士等存储原厂制造，供应给 GPU/AI 芯片厂商。在知识图谱中，`ent_component_gddr6_memory` 被 `ent_product_moore_threads_s4000`、`ent_product_moore_threads_s80` 等产品通过 `uses` 关系引用，是国产算力 GPU 的核心上游物料之一。

## 来源与验证

- [JEDEC GDDR6 Standard (JESD250)](https://www.jedec.org/standards-documents/docs/jesd250)
- [Micron Discusses GDDR5X and GDDR6](https://www.anandtech.com/show/11543/micron-discusses-gddr5x-gddr6-and-gddr5)
- [Samsung 16Gb GDDR6 Memory Announcement](https://www.notebookcheck.net/The-NVIDIA-Quadro-RTX-GPUs-feature-Samsung-s-16-Gigabit-GDDR6-memory.323050.0.html)