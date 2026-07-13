---
id: ent_product_moore_threads_s4000
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 摩尔线程 MTT S4000
  en: Moore Threads MTT S4000
status: active
sources:
- id: src_moorethreads_official
  type: website
  url: https://www.moorethreads.com
- id: src_tweaktown_s4000
  type: website
  url: https://www.tweaktown.com/news/95058/moore-threads-mtt-s4000-48gb-ai-gpu-with-mtlink-and-zero-cost-nvidia-cuda-framework/index.html
- id: src_techpowerup_s4000
  type: website
  url: https://www.techpowerup.com/316881/moore-threads-launches-mtt-s4000-48-gb-gpu-for-ai-training-inference-and-presents-1000-gpu-cluster
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 摩尔线程 MTT S4000 / Moore Threads MTT S4000

## 概述

摩尔线程 MTT S4000 是基于第三代 MUSA（Moore Threads Unified System Architecture，春晓核心）的数据中心级全功能 GPU，定位于 AI 训练/推理、图形渲染、视频编解码与云游戏。其单卡配备 48 GB GDDR6 显存与 768 GB/s 显存带宽，支持 PCIe 5.0 x16 接口与 MTLink 1.0 多卡互联，是国产算力集群的重要组成单元。

## 工作原理 / 技术架构

MTT S4000 集成 8192 个计算核心、128 个 Tensor Core、512 个 TMU 与 512 个 ROP，支持 FP32/TF32/FP16/BF16/INT8/INT4 多种精度。显存控制器提供 384-bit 位宽，峰值带宽为
\[
B=\frac{16\times10^{9}\times384}{8}=768\ \text{GB/s},
\]
对应 16 Gbps 的 GDDR6 数据率。多卡之间通过 MTLink 1.0 实现高速互连，可扩展至千卡级 KUAE 智算集群，并借助 MUSIFY 工具将 CUDA 代码迁移至 MUSA 平台。

## 关键参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | MUSA Gen3（春晓） | 摩尔线程 / TechPowerUp |
| 制程 | 12 nm | TechPowerUp |
| 计算核心 | 8192 | TechPowerUp |
| Tensor Core | 128 | TechPowerUp |
| 显存 | 48 GB GDDR6 | 摩尔线程 |
| 显存位宽 | 384-bit | TechPowerUp |
| 显存带宽 | 768 GB/s | 摩尔线程 |
| 接口 | PCIe 5.0 x16 | 摩尔线程 |
| FP32 算力 | 25 TFLOPS | 摩尔线程 |
| TF32 算力 | 50 TFLOPS | 摩尔线程 |
| FP16/BF16 算力 | 100 TFLOPS | TweakTown |
| INT8 算力 | 200 TOPS | 摩尔线程 |
| TDP | 450 W | TechPowerUp |
| 多卡互联 | MTLink 1.0 | 摩尔线程 |
| 视频能力 | 96 路 1080p 解码，8K 显示 | 摩尔线程 |

## 应用场景

- 智算中心 AI 训练与推理
- 大语言模型微调与部署
- 云游戏与数字孪生渲染
- 机器人云端大脑与仿真训练

## 供应链关系

摩尔线程（`ent_company_moore_threads`）设计 MTT S4000。上游依赖晶圆代工、GDDR6 显存（`ent_component_gddr6_memory`）、PCIe 5.0 接口（`ent_component_pcie_interface`）及服务器 OEM；下游客户包括智算中心、云服务商与 AI 企业。在知识图谱中，`ent_company_moore_threads` 通过 `manufactures` 指向 `ent_product_moore_threads_s4000`，后者通过 `uses` 关系引用 GDDR6 与 PCIe 接口。

## 来源与验证

- [摩尔线程官网](https://www.moorethreads.com)
- [Moore Threads MTT S4000 48GB AI GPU](https://www.tweaktown.com/news/95058/moore-threads-mtt-s4000-48gb-ai-gpu-with-mtlink-and-zero-cost-nvidia-cuda-framework/index.html)
- [Moore Threads Launches MTT S4000 48 GB GPU](https://www.techpowerup.com/316881/moore-threads-launches-mtt-s4000-48-gb-gpu-for-ai-training-inference-and-presents-1000-gpu-cluster)