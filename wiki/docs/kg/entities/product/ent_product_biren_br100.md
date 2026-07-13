---
id: ent_product_biren_br100
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 壁仞 BR100 通用 GPU
  en: Biren BR100 General-purpose GPU
status: active
sources:
- id: src_biren_official
  type: website
  url: https://www.birentech.com/
- id: src_mydrivers_br100
  type: website
  url: https://news.mydrivers.com/1/851/851378.htm
- id: src_gamersky_br100
  type: website
  url: https://www.gamersky.com/hardware/202208/1507359.shtml
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 壁仞 BR100 通用 GPU

## 概述

BR100 是壁仞科技（Biren Technology）发布的首款通用 GPU，采用 7 nm 制程、Chiplet 与 2.5D CoWoS 封装技术，集成约 **770 亿个晶体管**，配备 **64 GB HBM2E** 高带宽显存。该芯片面向人工智能训练/推理、高性能计算（HPC）、AIGC 与科学计算，强调高算力、高带宽显存与片间高速互联。

## 工作原理 / 技术架构

BR100 基于壁仞自研的“壁立仞”通用 GPU 架构，采用以数据流为中心的并行计算设计，包含 TF32+ 数据流精度、TDA 数据流存取加速、C-Warp 数据流并行、NME/NUMA 数据搬移优化与 SVI 数据流隔离等技术。

片上存储带宽与算力的关系可通过存储墙效率描述。BR100 配置 300 MB 片上缓存与 2.3 TB/s 的 HBM2E 显存带宽。对于计算密集型算子，有效算力利用率取决于数据复用度：

$$
\text{有效算力} = \text{理论峰值算力} \times \eta_{\text{compute}} \times \eta_{\text{memory}}
$$

公开披露的峰值性能包括：

$$
\text{INT8} = 2048 \ \text{TOPS}, \quad \text{BF16} = 1024 \ \text{TFLOPS}, \quad \text{FP32} = 256 \ \text{TFLOPS}
$$

BR100 支持 PCIe 5.0 与 CXL 互联协议，并可通过 BLink 片间互联扩展多卡集群。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 制造商 | 壁仞科技 / Biren Technology |
| 产品形态 | 通用 GPU / OAM 加速卡 |
| 制程 | 7 nm |
| 晶体管数 | 约 770 亿 |
| 架构 | 壁立仞（Biren）自研通用 GPU 架构 |
| 封装 | 2.5D CoWoS + Chiplet |
| 片上缓存 | 300 MB |
| 显存 | 64 GB HBM2E |
| 显存带宽 | 2.3 TB/s |
| 互联 | PCIe 5.0、CXL、BLink 片间互联 |
| INT8 峰值算力 | 2048 TOPS |
| BF16 峰值算力 | 1024 TFLOPS |
| TF32+ 峰值算力 | 512 TFLOPS |
| FP32 峰值算力 | 256 TFLOPS |
| 典型功耗（BR100 OAM） | 约 550 W |
| 价格 | 未公开 |

## 应用场景

- **大模型训练与推理**：GPT/LLaMA 类大语言模型、多模态大模型的分布式训练与推理。
- **AIGC**：文生图、文生视频、3D 生成等生成式 AI 工作负载。
- **科学计算与 HPC**：分子模拟、气象预测、计算流体力学。
- **自动驾驶云训练**：感知、预测模型的云端大规模训练。

## 供应链关系

在公司—产品—零部件网络中，BR100 处于**AI 算力芯片产品层**：

- **上游**：晶圆代工（台积电 7 nm）、HBM2E 存储、封测服务、EDA 工具、IP 核。
- **自身位置**：`ent_company_biren -- manufactures --> ent_product_biren_br100`；`ent_product_biren_br100 -- uses --> ent_component_hbm_memory`。
- **下游**：互联网大厂、智算中心、云计算厂商、科研院所、AI 初创企业及自动驾驶研发平台。

## 来源与验证

- 壁仞科技官网：https://www.birentech.com/
- 快科技 BR100 报道：https://news.mydrivers.com/1/851/851378.htm
- 游民星空 BR100 性能参数：https://www.gamersky.com/hardware/202208/1507359.shtml

7 nm 制程、770 亿晶体管、64 GB HBM2E、2.3 TB/s 带宽及各精度峰值算力均来自壁仞科技发布会及公开报道；具体产品价格需联系壁仞官方或授权渠道。