---
id: ent_product_iluvatar_biv200
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 天数智芯 天垓 200
  en: Iluvatar BI-V200
aliases:
- 天垓 200
- BI-V200
status: active
sources:
- id: src_iluvatar_sdk_kb
  type: website
  url: https://ixkb.iluvatar.com.cn:9443/webdoc/view/Pub8a16948a9a4cb023019a94b4a8050c48.html
- title: 天数智芯 SDK 安装实操手册 V1.0
- id: src_iluvatar_moark
  type: website
  url: https://moark.com/docs/compute/clusters_gpu/iluvatar/iluvatar_BI-V150_gpu
- title: 天垓150 | 模力方舟
- id: src_iluvatar_ithome
  type: website
  url: https://www.ithome.com/0/629/412.htm
- title: GPU 芯片及算力提供商天数智芯完成超 10 亿元融资
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 天数智芯 天垓 200 / Iluvatar BI-V200

## 概述

天垓 200（BI-V200，内部简称 tg_v200）是上海天数智芯半导体股份有限公司开发的第二代云端训练通用 GPU/AI 加速卡，承接天垓 100（BI-V100）与智铠 100 系列，面向人工智能训练与推理任务。该产品基于天数智芯自研 ivcore11 通用 GPU 架构，采用 7 nm 工艺制程，兼容 CUDA 编程模型，旨在提供国产化训练算力解决方案。

## 工作原理 / 技术架构

### GPU 架构
天数智芯天垓系列采用自研 ivcore11 通用 GPU 架构，线程层级与 CUDA 类似：

$$
\text{Grid} \rightarrow \text{Thread Block} \rightarrow \text{Warp (64 threads)} \rightarrow \text{Thread}
$$

其 warp size 为 64（NVIDIA CUDA 为 32），开发者需注意线程同步与内存访问模式差异。硬件支持 FP32、FP16、BF16、INT8 等多种精度，并通过自研 SDK 提供算子库与通信优化。

### 计算与存储
- **工艺**：7 nm；
- **显存类型**：HBM2e 高带宽显存（参考天垓 150 为 64 GB HBM2e，天垓 200 具体容量未公开）；
- **接口**：PCIe 4.0 ×16；
- **互联**：支持多卡扩展，天数智芯提供 MLU-Link 类似的高速互联方案（天垓系列官方资料未明确命名）。

### 软件栈
- 天数智算软件栈；
- 兼容 CUDA/OpenCL 编程接口；
- 支持 PyTorch、TensorFlow、PaddlePaddle 等主流深度学习框架；
- 适配 DeepSpeed、Megatron-LM 等大模型训练框架。

算力可用通用峰值公式估算：

$$
P_{\text{peak}} = N_{\text{core}} \times f \times n_{\text{ops}}
$$

其中 $N_{\text{core}}$ 为计算核心数，$f$ 为主频，$n_{\text{ops}}$ 为每周期每核心操作数。具体核心数、主频与峰值算力未在公开资料中披露。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 产品名称 | 天垓 200 / Iluvatar BI-V200 |
| 内部型号简称 | tg_v200 |
| 架构 | ivcore11 通用 GPU |
| 工艺制程 | 7 nm |
| 显存 | 未公开（参考同代天垓 150：64 GB HBM2e） |
| 接口 | PCIe 4.0 ×16 |
| 支持精度 | FP32、FP16、BF16、INT8 |
| 编程接口 | CUDA/OpenCL 兼容 |
| 框架支持 | PyTorch、TensorFlow、PaddlePaddle、DeepSpeed、Megatron-LM |
| 典型功耗 | 未公开（参考天垓 150：350 W） |
| 互联 | 多卡互联扩展（具体带宽未公开） |

## 应用场景

- **大模型训练**：LLaMA、Qwen、Yi 等主流开源大模型的训练与微调；
- **推理服务**：数据中心 INT8/FP16 批量推理；
- **科学计算**：通用 GPU 计算任务；
- **机器人云端大脑**：为人形机器人、自动驾驶等具身智能系统提供远端训练与推理算力。

## 供应链关系

天垓 200 位于“AI 芯片设计—晶圆制造—服务器/智算中心”链条的芯片层：

- **芯片设计**：上海天数智芯半导体股份有限公司；
- **晶圆代工**：7 nm 工艺由外部代工厂制造（未公开）；
- **HBM 显存**：由海外存储原厂供应；
- **下游服务器厂商**：与浪潮、宁畅等国产服务器厂商合作适配；
- **软件生态**：天数智算软件栈、开源框架适配。

## 来源与验证

- 天数智芯知识库 SDK 手册（列明 tg_v200 型号简称）
- 模力方舟天垓 150 规格页（用于推断同代架构与工艺）
- IT之家融资报道（2022-07-13，提及天垓 200/300 开发计划）

> 注：天垓 200 尚未公开完整 datasheet，核心数、峰值算力、显存容量、TDP、互联带宽等关键参数标注为“未公开”。本条目基于同代产品天垓 150/100 及官方 SDK 中的型号命名信息进行合理推断。