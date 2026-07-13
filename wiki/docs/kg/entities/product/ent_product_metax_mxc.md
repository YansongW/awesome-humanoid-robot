---
id: ent_product_metax_mxc
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 沐曦 MXC 系列通用 GPU
  en: MetaX MXC Series General-Purpose GPU
status: active
sources:
- id: src_metax_c500
  type: website
  url: https://www.metax-tech.com/en/goods/prod.html?cid=107&id=21
- id: src_metax_c550
  type: website
  url: https://www.metax-tech.com/en/goods/prod.html?cid=107&id=35
- id: src_flopper_c500
  type: website
  url: https://flopper.io/gpu/metax-c500/spec-sheet
- id: src_exportsemi_mxc
  type: website
  url: https://www.exportsemi.com/company-product/104/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 沐曦 MXC 系列通用 GPU / MetaX MXC Series General-Purpose GPU

## 概述

MXC 系列是沐曦（MetaX）推出的通用 GPU（GPGPU）产品线，基于公司自研 XCORE GPU IP，面向人工智能训练/推理、高性能计算、数据中心通用计算与科学计算。该系列代表型号包括 C500（PCIe 全高全长双槽卡）与 C550（OAM 模块），采用 7 nm 工艺，配备大容量 HBM2E 高带宽显存，并通过 MetaXLink 实现多卡高速互联。

## 工作原理 / 技术架构

MXC 系列 GPU 的核心架构包括：

- **自研 XCORE GPGPU IP**：支持 FP32、TF32、FP16/BF16、INT8 等多精度混合计算。
- **HBM2E 高带宽显存**：C500 单卡配备 64 GB HBM2E，提供高容量与超高内存带宽，满足大模型训练与推理需求。
- **MetaXLink 多卡互联**：C550 OAM 模块支持 8 GPU 全互联，全互联带宽达 896 GB/s，便于构建大规模 GPU 集群。
- **MXMACA 软件栈**：兼容主流 GPU 生态，提供编译器、运行时库与迁移优化工具，降低模型迁移成本。

峰值算力可表示为
\[
R = N_{\text{core}} \times f \times n_{\text{op}}
\]
其中 \(N_{\text{core}}\) 为计算单元数，\(f\) 为工作频率，\(n_{\text{op}}\) 为每周期每核心可执行操作数。以 C500 为例，公开标称 FP32 峰值算力为 18.0 TFLOPS，FP16/BF16 峰值算力为 280 TFLOPS，INT8 峰值算力为 560 TOPS。

## 关键参数表

| 参数项 | MetaX C500 | MetaX C550 |
|---|---|---|
| 架构 | XCORE GPGPU | XCORE GPGPU |
| 制程 | 7 nm | 7 nm |
| 形态 | PCIe 全高全长双槽卡 | OAM 1.5/2.0 模块 |
| FP32 峰值算力 | 18.0 TFLOPS | 未公开 |
| FP16/BF16 峰值算力 | 280 TFLOPS | 未公开 |
| INT8 峰值算力 | 560 TOPS | 未公开 |
| 显存容量 | 64 GB HBM2E | 64 GB HBM2E |
| GPU-to-GPU 互联 | MetaXLink | MetaXLink，8 GPU 全互联带宽 896 GB/s |
| 最大板级功耗 | 350 W | 未公开 |
| 软件栈 | MXMACA | MXMACA |

## 应用场景

- **大模型训练与推理**：为 LLM、CV、推荐系统提供国产 GPU 算力。
- **科学计算与仿真**：气候模拟、流体计算、分子动力学等 HPC 应用。
- **智算中心与云计算**：作为数据中心 AI 加速卡部署。
- **机器人与自动驾驶**：用于机器人感知模型、端到端策略模型与仿真训练。

## 供应链关系

- **上游**：晶圆代工（台积电 7 nm）、HBM2E 显存（三星/SK 海力士/美光）、封装测试（OSAT）、PCB、散热模组、电源管理芯片。
- **开发商**：沐曦（MetaX），中国上海，2020 年成立。
- **下游**：服务器厂商、云服务商、AI 企业、科研院所、智算中心运营商。
- **竞争对标**：NVIDIA A100/H100、AMD MI 系列、壁仞科技、摩尔线程、海光信息。
- **图谱位置**：`ent_company_metax` → `manufactures` → `ent_product_metax_mxc`；并通过 `uses` 关系连接 `ent_component_hbm_memory`。

## 来源与验证

- C500/C550 产品介绍与关键规格来自沐曦官网。
- C500 具体算力、显存与功耗数据参考 Flopper.io 公开的规格表。
- MXC 系列定位与软件栈信息来自 ExportSemi 产品页及附录 D 沐曦企业 Wiki。