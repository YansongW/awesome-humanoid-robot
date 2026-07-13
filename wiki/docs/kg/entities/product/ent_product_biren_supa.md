---
id: ent_product_biren_supa
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 壁仞 BIRENSUPA 软件平台
  en: Biren SUPA Software Platform
status: active
sources:
- id: src_ent_product_biren_supa_1
  type: website
  url: https://pandaily.com/biren-technology-releases-first-general-purpose-gpu-chip-br100
- id: src_ent_product_biren_supa_2
  type: website
  url: https://www.aiwire.net/2022/08/23/chinese-startup-biren-details-br100-gpu/
- id: src_ent_product_biren_supa_3
  type: website
  url: https://www.servethehome.com/biren-br100-gpu-for-datacenter-compute-and-ai-workloads/
- id: src_ent_product_biren_supa_4
  type: website
  url: https://www.futunn.com/en/stock/06082-HK/company
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 壁仞 BIRENSUPA 软件平台

## 概述

BIRENSUPA 是壁仞科技（Biren Technology）为其 BR100 系列通用 GPU 推出的自研软件平台与编程模型，名称对应壁仞的“SUPA”计算架构。该平台覆盖驱动层、编程平台（编译器、加速库、工具链）、框架适配层（PyTorch、TensorFlow、PaddlePaddle 等）及应用解决方案，目标是为大模型训练、推理、高性能计算（HPC）及科学计算提供国产自主可控的算力软件栈。

## 工作原理 / 技术架构

BIRENSUPA 采用类 CUDA 的编程模型，使熟悉 NVIDIA CUDA 的开发者能够较快迁移到壁仞 GPU。其软件栈自下而上包括：

- **驱动层**：管理 BR100/Brien 硬件资源、内存分配与多 GPU 互联（BLink）。
- **编程平台**：提供 SUPA 编程模型、编译器、加速库与工具链；BR100 双芯芯片在软件层呈现为单一 GPU。
- **框架层**：支持 PyTorch、TensorFlow、PaddlePaddle 等主流深度学习框架，并提供模型迁移与性能调优工具。
- **应用层**：覆盖大模型、计算机视觉、自然语言处理、医疗影像、分子动力学等场景。

壁仞 BR100 基于 7 nm 工艺与 2.5D CoWoS 封装，晶体管数约 770 亿，配备 64 GB HBM2e 显存。其峰值算力为

$$
\mathrm{FP32}: 256\ \mathrm{TFLOPS},\quad \mathrm{BF16}: 1024\ \mathrm{TFLOPS},\quad \mathrm{INT8}: 2048\ \mathrm{TOPS}
$$

内存带宽约为 1.6 TB/s。BIRENSUPA 通过显存管理与跨芯片互联调度，使双芯 BR100 对上层应用透明，提升编程便利性。

## 关键参数表

| 参数项 | 数值/描述 | 备注/来源 |
|--------|-----------|-----------|
| 所属公司 | 壁仞科技 / Biren Technology | 公开资料 |
| 对应硬件 | BR100 / BR104 / BR106 / BR166 / BR110 等 GPGPU | Futubull / Pandaily |
| 编程模型 | SUPA（类 CUDA） | AI Wire |
| 支持框架 | PyTorch、TensorFlow、PaddlePaddle | AI Wire / Pandaily |
| 编译器/工具链 | 自研编译器、OpenCL 编译器、迁移工具 | ServeTheHome |
| BR100 峰值算力 | FP32 256 TFLOPS / BF16 1024 TFLOPS / INT8 2048 TOPS | Flopper / Pandaily |
| BR100 显存 | 64 GB HBM2e，带宽约 1.6 TB/s | ServeTheHome / TweakTown |
| BR100 TDP | 约 550 W | 公开报道 |
| 软件栈层级 | 驱动 / 编程平台 / 框架 / 应用解决方案 | Pandaily |
| 许可与定价 | 随硬件提供，具体未公开 | 未公开 |

## 应用场景

- **大语言模型训练与推理**：为国产智算中心提供替代方案，支持 Transformer 类大模型。
- **科学计算与仿真**：分子动力学、电磁仿真、气象模拟、计算流体力学。
- **医疗影像与 AIGC**：CT/MRI 图像重建、生成式 AI 内容创作。
- **机器人云端大脑**：为具身智能模型训练、数字孪生仿真与大规模数据回流提供算力。

## 供应链关系

BIRENSUPA 由 `ent_company_biren` 开发，是壁仞“芯片 + 软件”端到端智能计算解决方案的软件部分。上游依赖 BR100 系列 GPU 硬件、HBM 显存、7 nm 晶圆代工与封装测试；下游客户包括互联网大厂、智算中心、科研院所、云计算厂商及 AI 初创企业。在知识图谱中：

- `ent_company_biren` -- `manufactures` --> `ent_product_biren_supa`
- `ent_product_biren_supa` -- `runs_on` --> `ent_product_biren_br100`
- `ent_product_biren_br100` -- `uses` --> `ent_component_hbm_memory`

## 来源与验证

- BIRENSUPA 的层级结构、支持框架与类 CUDA 编程模型参考 Pandaily 与 AI Wire 报道。
- BR100 硬件算力、显存与功耗数据参考 ServeTheHome、TweakTown 与 Flopper 汇总。
- 壁仞公司产品线（BR100/104/106/166/110）与端到端解决方案描述来自 Futubull 公司资料。