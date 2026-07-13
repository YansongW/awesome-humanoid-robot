---
id: ent_product_t_head_xuantie_c920
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 平头哥玄铁 C920
  en: T-Head Xuantie C920
aliases:
- 玄铁 C920
- Xuantie C920
status: active
sources:
- id: src_thead_c920_baike
  type: website
  url: https://baike.baidu.com/item/%E7%8E%84%E9%93%81C920/63747745
- title: 玄铁 C920 | 百度百科
- id: src_thead_c920_ithome
  type: website
  url: https://www.ithome.com/0/734/341.htm
- title: 平头哥玄铁 RISC-V 处理器 C920、C907、R910 发布 | IT之家
- id: src_thead_c920_doc
  type: document
  url: https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1680257166949/%E7%8E%84%E9%93%81RISC-V%E5%A4%84%E7%90%86%E5%99%A8%E5%85%A5%E9%97%A8%E4%B8%8E%E5%AE%9E%E6%88%98.pdf
- title: 玄铁 RISC-V 处理器入门与实战 | 平头哥
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 平头哥玄铁 C920 / T-Head Xuantie C920

## 概述

玄铁 C920 是阿里巴巴旗下平头哥半导体（T-Head）于 2023 年 11 月发布的 64 位高性能 RISC-V 处理器 IP，面向人工智能、自动驾驶、网络通信、企业级 SSD、边缘计算与 AI PC 等高算力场景。C920 采用 12 级多发乱序流水线，兼容 RISC-V Vector 1.0 与 RVA23 规范，支持多核多 Cluster 扩展，并已应用于嘉楠科技 K230 芯片、AI PC 概念机等产品中。

## 工作原理 / 技术架构

C920 基于 RV64GCV 指令集架构，核内子系统包括指令提取单元（IFU）、译码单元（IDU）、整型执行单元（IU）、浮点单元（FPU）、矢量执行单元（VU）、存储载入单元（LSU）、指令退休单元（RTU）、MMU 与 PMP。多核子系统包含数据一致性接口单元（CIU）、二级高速缓存、主设备接口单元、AXI4.0 设备一致性接口（DCP）、平台级中断控制器（PLIC）与调试框架。

处理器性能常用 DMIPS/MHz 与 CoreMark/MHz 衡量。C920 标称 Dhrystone 性能为

$$
5.8\ \text{DMIPS/MHz}
$$

CoreMark 性能为

$$
7.03\ \text{CoreMark/MHz}
$$

峰值算力可通过时钟频率 $f$ 与每周期指令数 IPC 估算：

$$
P = f \times \text{IPC} \times \text{cores}
$$

标称工作频率大于 2.5 GHz，最高可达 3 GHz，并支持最多 64 核心多 Cluster 扩展。

矢量单元支持 128 位矢量寄存器，数据类型覆盖 FP16/BF16/FP32/INT8/INT16/INT32/INT64。基于软硬件协同优化，C920 较上一代 AI 性能提升最高 3.8 倍，可运行 Transformer 类模型。

## 关键参数表

| 参数 | 数值/说明 | 备注 |
|------|-----------|------|
| 架构 | RV64GCV | 官方资料 |
| 流水线 | 12 级多发乱序 | 官方资料 |
| 典型工作频率 | >2.5 GHz | 官方资料 |
| 最高工作频率 | 3 GHz | 媒体报道 |
| 指令集扩展 | RISC-V Vector 1.0、RVA22/RVA23 | 官方资料 |
| 浮点单元 | 标配单精度 FPU | IEEE 754-2008 |
| 矢量单元 | 可选乱序矢量单元（VU）| 官方资料 |
| 矢量寄存器宽度 | 128 bit | 官方资料 |
| 每 Cluster 核心数 | 最多 4 核 | 官方资料 |
| 最大支持核心数 | 64 核 | 媒体报道 |
| 指令 Cache | 最大 64 KB | 可选奇偶校验 |
| 数据 Cache | 最大 64 KB | 可选 ECC |
| L2 Cache | 最大 8 MB | 可选 ECC |
| MMU | SV39 / SV48 | 官方资料 |
| PMP | 最多 16 个区域 | 官方资料 |
| 总线接口 | AMBA4.0 AXI/ACE-128 | 官方资料 |
| Dhrystone | 5.8 DMIPS/MHz（O2）| 百度百科 |
| CoreMark | 7.03 CoreMark/MHz（O3）| 百度百科 |
| 典型应用 | AI、自动驾驶、网络通信、企业 SSD、AI PC | 官方资料 |

## 应用场景

- **AI PC 与边缘推理**：基于 C920 的 AI PC 概念机已跑通 Llama、Qwen、DeepSeek 等开源模型，实现全链路开源架构。
- **自动驾驶**：作为域控制器主控或协同芯片，处理多传感器融合与感知决策任务。
- **网络通信与 5G/6G**：S5000C-M 等衍生平台用于基站、核心网与边缘计算设备。
- **机器人主控**：为高端服务机器人、人形机器人提供 RISC-V 架构的高性能计算与 AI 推理能力。
- **企业级 SSD**：配合实时处理器 R910 用于 SSD 主控芯片镇岳 510 等存储产品。

## 供应链关系

玄铁 C920 属于 **半导体 IP/处理器芯片层**，上游依赖 EDA 工具、晶圆代工（如台积电、中芯国际）与封测；中游由平头哥提供 RISC-V IP 授权、参考设计与工具链；下游包括芯片设计公司（如嘉楠科技）、整机厂商与操作系统/软件生态伙伴。C920 已与 Android、Debian、Fedora、Ubuntu、龙蜥、统信、openKylin 等操作系统完成适配，处于 RISC-V 高性能计算生态的核心位置。

## 来源与验证

- 百度百科（引用平头哥官方资料）：https://baike.baidu.com/item/%E7%8E%84%E9%93%81C920/63747745
- IT之家发布报道：https://www.ithome.com/0/734/341.htm
- 平头哥官方文档《玄铁 RISC-V 处理器入门与实战》：https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1680257166949/%E7%8E%84%E9%93%81RISC-V%E5%A4%84%E7%90%86%E5%99%A8%E5%85%A5%E9%97%A8%E4%B8%8E%E5%AE%9E%E6%88%98.pdf

最高频率 3 GHz、最大 64 核心等参数主要来自媒体报道与百科汇总，平头哥官方公开文档中未完整披露所有 SKU 频率上限。