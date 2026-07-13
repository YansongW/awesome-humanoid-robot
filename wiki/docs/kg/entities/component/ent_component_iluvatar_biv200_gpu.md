---
id: ent_component_iluvatar_biv200_gpu
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: 天数智芯天垓 200 通用 GPU（BI-V200）
  en: Iluvatar CoreX Tiangai 200 General-Purpose GPU (BI-V200)
sources:
- id: src_iluvatar_official
  type: website
- title: Iluvatar CoreX Official Website
  url: https://www.iluvatar.com.cn
- id: src_iluvatar_product_page
  type: website
- title: Iluvatar Product Page
  url: https://www.iluvatar.com.cn/product/
- id: src_moark_biv150
  type: documentation
- title: 天垓150（BI-V150）技术文档
  url: https://moark.com/docs/compute/clusters_gpu/iluvatar/iluvatar_BI-V150_gpu
verification:
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-13'
  review_notes: Publicly disclosed specifications for BI-V200 itself are limited;
    values below combine company wiki data and BI-V150/BI-V100 public materials. Exact
    BI-V200 parameters should be verified against official datasheet.
---


# 天数智芯天垓 200 通用 GPU（BI-V200） / Iluvatar CoreX Tiangai 200 General-Purpose GPU (BI-V200)

## 概述

天垓 200（BI-V200）是天数智芯（Iluvatar CoreX）推出的第二代通用 GPU 训练/推理加速卡，基于自研通用 GPU 架构，采用 7 nm 制程，支持 FP32/FP16/BF16/INT8 等多精度混合计算，配套天数智算软件栈，并在 API 层面兼容主流 CUDA 生态。BI-V200 面向智算中心、互联网、金融及科研领域，提供国产云端 AI 训练与推理算力，也可用于机器人仿真、具身智能云端训练与大模型推理。

## 工作原理 / 技术架构

BI-V200 采用 SIMT（Single Instruction, Multiple Threads）通用 GPU 架构，计算引擎由大量可扩展计算核心阵列组成，支持 Grid → Thread Block → Warp（64 线程）→ Thread 四级线程层级。硬件内建 FP32/FP16/BF16/INT8 等多精度指令，支持混合精度训练；通过 2.5D CoWoS 封装集成 HBM2e 高带宽显存，并通过 PCIe Gen4 x16 与主机连接。

峰值算力（理论值）可表示为：
$$T_{peak} = N_{core} \cdot f_{clk} \cdot N_{op}/cycle$$
其中 $N_{core}$ 为计算核心数，$f_{clk}$ 为运行频率，$N_{op}/cycle$ 为每周期每核心操作数。实际有效算力受内存带宽、数据局部性与算法并行度影响。

天数智算软件栈提供编译器、运行时、算子库与推理引擎（IGIE/ixRT），支持 PyTorch、TensorFlow 等主流框架及 vLLM、LMDeploy 等推理框架。

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 架构 | 自研通用 GPU（ivcore 系列） | 天数智芯公开资料 |
| 制程 | 7 nm | 公开报道 / 公司 Wiki |
| 显存 | 32 GB / 64 GB HBM2e（依具体型号） | 公开报道 / BI-V150 参考 |
| 显存带宽 | 约 1.2 TB/s（单卡参考 BI-V150） | BI-V150 技术文档 |
| 接口 | PCIe Gen4 x16 | 公开报道 |
| FP32 峰值算力 | 数十 TFLOPS 级（具体值未公开） | 公司 Wiki |
| FP16/BF16 峰值算力 | 数百 TFLOPS 级（具体值未公开） | 公司 Wiki |
| INT8 峰值算力 | 数百 TOPS 级（具体值未公开） | 公司 Wiki |
| 功耗 | 约 300–350 W | 公开报道 |
| 形态 | 全高全长双槽 PCIe 加速卡 | 公开报道 |
| 互联 | 支持多卡互联（PCIe 4.0 / 未公开专用互联） | 公司 Wiki |
| 软件栈 | 天数智算软件栈、CUDA API 兼容 | 天数智芯公开资料 |
| 支持精度 | FP32、FP16、BF16、INT8、INT4 | BI-V150 参考 |

## 应用场景

- **大模型训练与微调**：LLM、多模态模型的云端分布式训练。
- **大模型推理**：LLM、CV、推荐系统的量化推理部署。
- **机器人仿真与具身智能**：Isaac Gym、Mujoco 等并行仿真与强化学习训练。
- **科学计算与 AIGC**：HPC、分子模拟、生成式 AI 内容生成。

## 供应链关系

- **制造商**：天数智芯 Iluvatar CoreX（ent_company_iluvatar），上海国产 GPU 企业。
- **上游关键物料**：台积电/中芯国际 7 nm 代工、HBM2e 显存、2.5D CoWoS 封测、EDA/IP、服务器主板。
- **下游整机集成**：智算中心、互联网大厂、云计算厂商、AI 企业、科研院所、机器人公司。
- **竞争/对标**：NVIDIA A100/H100/H200、AMD MI 系列、华为昇腾、壁仞科技、沐曦、摩尔线程。

## 来源与验证

- 天数智芯官网：https://www.iluvatar.com.cn
- 天数智芯产品页：https://www.iluvatar.com.cn/product/
- 模力方舟天垓150（BI-V150）技术文档：https://moark.com/docs/compute/clusters_gpu/iluvatar/iluvatar_BI-V150_gpu