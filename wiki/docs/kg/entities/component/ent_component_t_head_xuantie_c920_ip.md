---
id: ent_component_t_head_xuantie_c920_ip
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 平头哥玄铁 C920 处理器 IP
  en: T-Head Xuantie C920 Processor IP
sources:
- id: src_t_head_product
  type: website
- title: '"T-Head 产品中心"'
  url: https://www.t-head.cn/product/
- id: src_t_head_c920_spec
  type: website
- title: '"玄铁 C920 处理器规格说明"'
  url: https://www.xrvm.cn/product/xuantie/4082464366237126656
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# 平头哥玄铁 C920 处理器 IP / T-Head Xuantie C920 Processor IP

## 概述

平头哥玄铁 C920 是阿里巴巴集团平头哥半导体推出的高性能 RISC-V 处理器 IP，面向边缘 AI、机器人主控、工业控制与 AIoT 应用。该 IP 基于 RV64GCV 指令集，支持 RISC-V Vector 1.0 向量扩展，可作为 SoC 的 CPU 集群核心，为机器人感知、规划与实时控制提供可授权的算力底座。

## 工作原理 / 技术架构

C920 采用 12 级乱序超标量流水线，每个 Cluster 最多支持 4 核 SMP；集成符合 IEEE 754-2008 的浮点单元与 128 位矢量寄存器，具备两条矢量执行单元与数据存储流水线，支持 FP16/BF16/FP32/INT8/INT16/INT32/INT64 等数据类型。内存子系统支持 SV39/SV48 MMU、PMP 最多 16 区域、可选奇偶校验/ECC 的 L1 Cache（最大 64 KB）与 L2 Cache（最大 8 MB），并通过 AMBA4.0 AXI/ACE-128 主接口与 AXI-128 从接口接入一致性总线。

性能方面，公开资料给出 Dhrystone 5.8 DMIPS/MHz（O2）与 CoreMark 7.03 CoreMark/MHz（O3）。主频随实现工艺变化，公开报道最高可达约 3 GHz；峰值算力未公开。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 架构 | RISC-V RV64GCV | 官方规格 |
| 流水线 | 12 级乱序超标量 | 官方规格 |
| 每 Cluster 最大核数 | 4 核 | 官方规格 |
| 矢量扩展 | RISC-V Vector 1.0 | 128 位矢量寄存器 |
| 最高主频 | 最高 3 GHz | 公开报道 |
| L1 I-Cache / D-Cache | 最大 64 KB + 64 KB | 可选奇偶校验/ECC |
| L2 Cache | 最大 8 MB | 可选 ECC |
| 总线接口 | AMBA4.0 AXI/ACE-128 + AXI-128 | 官方规格 |
| MMU | SV39/SV48 | 支持 Svpbmt、Svnapot |
| Dhrystone / CoreMark | 5.8 DMIPS/MHz；7.03 CoreMark/MHz | O2 / O3 |
| 峰值算力 | 未公开 | - |

## 应用场景

边缘 AI 推理主控、机器人运动规划与感知融合计算、工业网关、AIoT 终端以及国产 RISC-V 服务器 SoC。

## 供应链关系

平头哥半导体（`ent_company_t_head`）通过“无剑”SoC 平台将玄铁 C920 IP 授权给芯片设计公司；下游 SoC/模组厂商将其集成进机器人主控板、边缘服务器与工业控制器，与倚天 CPU、含光 NPU 形成端-边-云算力矩阵。

## 来源与验证

- T-Head 产品中心：https://www.t-head.cn/product/
- 玄铁 C920 规格页：https://www.xrvm.cn/product/xuantie/4082464366237126656