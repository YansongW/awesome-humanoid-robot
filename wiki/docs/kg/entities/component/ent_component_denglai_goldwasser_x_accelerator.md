---
id: ent_component_denglai_goldwasser_x_accelerator
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 登临 Goldwasser-X 加速器
  en: Denglai Goldwasser-X Accelerator
sources:
- id: src_denglai_official
  type: website
- title: 登临科技官网
  url: https://www.denglai.com.cn/product/
- id: src_denglai_qbitai
  type: website
- title: 登临科技联合创始人王平：GPU+赋能AI落地生根
  url: https://www.qbitai.com/2022/07/36338.html
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from Denglai public product information and industry
    reports; some detailed specs are not fully disclosed and marked as 未公开.
---


# 登临 Goldwasser-X 加速器 / Denglai Goldwasser-X Accelerator

## 概述

登临 Goldwasser-X 加速器是登临科技基于自主 GPU+ 架构推出的全高全长 PCIe 数据中心 AI 加速卡。GPU+ 架构在兼容 CUDA/OpenCL 编程模型与主流 AI 框架的基础上，通过片内异构计算提升 AI 推理与训练效率，主要面向云端大模型推理、AIGC、推荐系统、视频分析、智算中心及机器人端侧/边缘推理等场景。

## 工作原理与技术架构

Goldwasser-X 加速器的技术架构包括：

1. **GPU+ 片内异构架构**：将 GPGPU 通用计算单元与专用 AI 加速单元在同一芯片内融合，通过软件定义调度实现通用性与效率的平衡。
2. **CUDA/OpenCL 兼容**：硬件层兼容 CUDA/OpenCL，降低算法迁移成本，支持 PyTorch、TensorFlow、PaddlePaddle 等主流框架。
3. **多精度计算**：支持 INT8、FP16 等精度，针对不同神经网络进行硬件级优化。
4. **高带宽存储与多卡互联**：部分型号配置 32 GB HBM2e 显存，支持多卡互联扩展算力。
5. **翰铭（Hamming）软件栈**：提供编译器、运行时、驱动及推理服务工具，支持 x86 与 ARM 平台。

算力利用率可近似用有效算力 $A_{\text{eff}}$ 表示：

$$
A_{\text{eff}} = A_{\text{peak}} \cdot \eta_{\text{util}}
$$

其中 $A_{\text{peak}}$ 为峰值算力，$\eta_{\text{util}}$ 为实际利用率。登临公开测试数据显示，在 40 W TDP 下可输出 128 TOPS INT8 算力，能效比显著优于传统 GPU。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | GPU+（GPGPU + AI 加速）| 登临公开资料 |
| 制程 | 7 nm（公开报道）| 公开报道 |
| 形态 | 全高全长 PCIe 加速卡 | 登临公开资料 |
| 接口 | PCIe Gen3 / Gen4 | 公开报道 |
| INT8 峰值算力 | 512 TOPS（Goldwasser-XL 级）| 登临公开资料 |
| FP16 算力 | 数百 TOPS 级 | 登临公开资料 |
| 显存 | 最高 32 GB HBM2e（部分型号）| 公开报道 |
| 功耗 | 约 150 – 300 W（视型号）| 公开报道 |
| 能效参考 | 40 W TDP 输出 128 TOPS | 百度飞桨 / 量子位报道 |
| 互联 | 支持多卡互联 | 登临公开资料 |
| 软件栈 | 登临翰铭（Hamming）SDK | 登临公开资料 |
| 支持框架 | PyTorch、TensorFlow、PaddlePaddle 等 | 登临公开资料 |
| 价格 | 未公开 | - |

注：登临未公开 Goldwasser-X 各型号的完整规格表，上表参数来自公开报道与公司宣传资料。

## 应用场景

- **大模型推理**：GPT/LLM 类生成式 AI 的云端推理加速。
- **AIGC**：文本生成、图像生成、视频生成等生成式 AI 应用。
- **推荐系统与搜索**：互联网大厂在线推理与排序加速。
- **视频分析与智慧城市**：高路数视频编解码与 AI 解析。
- **智算中心**：国产算力替代与数据中心 AI 训练/推理。
- **机器人端侧/边缘推理**：与边缘服务器配合，支持具身智能感知与决策。

## 供应链关系

- **上游**：晶圆代工（7 nm）、HBM2e 存储、封测、EDA/IP、PCB、散热、电源管理。
- **制造商**：登临科技（Denglai Technology）通过关系 `ent_company_denglai -- manufactures --> ent_component_denglai_goldwasser_x_accelerator` 记录于知识图谱。整机产品 `ent_product_denglai_goldwasser_x` 使用该加速器作为核心算力部件。
- **下游**：互联网大厂、云计算厂商、智算中心、AI 企业、机器人公司、科研院所。主要竞争对手包括 NVIDIA T4/L4、寒武纪、燧原科技、天数智芯、沐曦等。

## 来源与验证

GPU+ 架构、Goldwasser 系列产品定位及算力/功耗数据来自登临科技官网、量子位、36 氪、百度飞桨等公开报道。具体型号的完整 datasheet、显存带宽、PCIe 版本及价格未在公开渠道完整披露，已标注为未公开。