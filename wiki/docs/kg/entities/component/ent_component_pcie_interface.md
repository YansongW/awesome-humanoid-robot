---
id: ent_component_pcie_interface
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: PCI Express 接口
  en: PCI Express Interface
status: active
sources:
- id: src_pcisig_pcie5
  type: website
  url: https://www.pcisig.com/specifications
- id: src_pci_sig_news
  type: website
  url: https://www.design-reuse.com/news/6716-pci-sig-achieves-32gt-s-with-new-pci-express-5-0-specification/
- id: src_oemdrivers_pcie5
  type: website
  url: https://oemdrivers.com/pci-express-5-0
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# PCI Express 接口 / PCI Express Interface

## 概述

PCI Express（PCIe）是由 PCI-SIG 维护的高速串行点对点 I/O 总线标准，用于连接 GPU、AI 加速器、NVMe SSD、网卡及各类扩展卡。每一代 PCIe 在保持向后兼容的同时将单 lane 数据率翻倍，PCIe 5.0 单 lane 速率达到 32 GT/s，是 AI 服务器与高性能机器人计算平台的关键互联接口。

## 工作原理 / 技术架构

PCIe 采用差分信号对组成的 lane 进行全双工串行通信，每个方向独立传输。自 Gen3 起使用 128b/130b 线路编码，编码效率为 \(128/130\approx0.985\)。x16 配置下单向有效带宽可表示为
\[
B_{\text{eff}}=\frac{N_{\text{lane}} \times f_{\text{rate}} \times 128}{130 \times 8},
\]
其中 \(N_{\text{lane}}=16\)，\(f_{\text{rate}}\) 为每 lane 数据率（GT/s）。对于 PCIe 5.0：
\[
B_{\text{eff}}=\frac{16\times32\times128}{130\times8}\approx63\ \text{GB/s}.
\]
PCI-SIG 常引用原始带宽 \(16\times32/8=64\ \text{GB/s}\) 或双向合计 128 GB/s 作为标称值。

## 关键参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 标准组织 | PCI-SIG | PCI-SIG |
| 版本 | 1.0–6.0（主流 4.0/5.0） | PCI-SIG |
| 单 lane 速率 | 2.5 / 5 / 8 / 16 / 32 / 64 GT/s | PCI-SIG |
| x16 单向有效带宽（Gen5） | ≈63 GB/s | 计算 |
| x16 原始带宽（Gen5） | 128 GB/s（双向） | PCI-SIG |
| 线路编码 | 128b/130b（Gen3 及以上） | PCI-SIG |
| 通道配置 | x1 / x4 / x8 / x16 / x32 | PCI-SIG |
| 兼容性 | 向下兼容各代 | PCI-SIG |
| 典型应用 | GPU、AI 加速卡、NVMe SSD、高速网卡 | PCI-SIG |

## 应用场景

- 机器人边缘计算平台的 GPU/AI 卡扩展
- 数据中心 AI 训练/推理服务器
- 工业视觉采集卡与运动控制卡
- 高带宽存储与网络设备

## 供应链关系

PCI-SIG 负责协议规范，物理层与控制器 IP 由 Cadence、Synopsys 等 EDA/IP 公司提供，连接器与线缆由 Amphenol、Molex 等供应。在知识图谱中，`ent_component_pcie_interface` 被 `ent_product_moore_threads_s4000` 等产品通过 `uses` 关系引用，是 GPU/加速器与主机 CPU 之间的高速互联基础。

## 来源与验证

- [PCI-SIG PCI Express 5.0 Specification](https://www.pcisig.com/specifications)
- [PCI-SIG Achieves 32GT/s with PCIe 5.0](https://www.design-reuse.com/news/6716-pci-sig-achieves-32gt-s-with-new-pci-express-5-0-specification/)
- [PCI Express 5.0 Overview](https://oemdrivers.com/pci-express-5-0)