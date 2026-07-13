---
id: ent_product_metax_mxn
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 沐曦 MXN 系列推理 GPU
  en: MetaX MXN Series Inference GPU
status: active
sources:
- id: src_ent_product_metax_mxn_official
  type: website
  url: https://www.metax-tech.com/ndetail/12469.html
- id: src_ent_product_metax_mxn_ithome
  type: website
  url: https://www.ithome.com/0/698/445.htm
- id: src_ent_product_metax_mxn_tencent
  type: website
  url: https://cloud.tencent.com/developer/article/2309978
- id: src_ent_product_metax_mxn_wiki
  type: website
  url: docs/appendices/appendix-d/companies/company_metax.md
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 沐曦 MXN 系列推理 GPU / MetaX MXN Series Inference GPU

## 概述

沐曦 MXN 系列推理 GPU（MetaX MXN Series Inference GPU）是沐曦集成电路（MetaX）面向云端数据中心推出的 AI 推理加速产品，核心型号包括曦思 N100（内置 MXN100 GPGPU 处理器）。该系列采用 7 nm 工艺与 HBM2E 高带宽显存，配合沐曦自研 MXMACA 软件栈，支持计算机视觉、视频转码、自然语言处理及大模型推理等任务，已广泛应用于智慧城市、智慧安防、智慧交通、云计算与智能视频处理等领域。

## 工作原理与技术架构

MXN 系列基于沐曦自研的异构 GPGPU 架构，集成大量通用计算单元与专用 AI 加速器，支持 INT8/FP16/FP32 等多精度混合计算。显存采用 HBM2E（High Bandwidth Memory 2E）堆叠封装，通过宽总线提供高吞吐、低延迟的数据供给。其 INT8 峰值算力可表示为：

$$
R_{\text{INT8}} = 160\ \text{TOPS}
$$

FP16 峰值算力为：

$$
R_{\text{FP16}} = 80\ \text{TFLOPS}
$$

视频处理单元支持多路高清视频并行编解码；以曦思 N100 为例，公开规格为 128 路编码与 96 路解码高清视频流，并兼容 HEVC（H.265）、H.264、AV1、AVS2 等主流格式，最高支持 8K 分辨率。MXMACA 软件栈提供底层驱动、编译器、运行时库及 ModelZoo，支持主流深度学习框架模型的快速迁移。

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 产品定位 | 云端 AI 推理 GPU 加速卡 | 曦思 N100 为代表 |
| 核心处理器 | MXN100 异构 GPGPU | 沐曦自研 |
| 制程工艺 | 7 nm | 公开报道 |
| 显存类型 | HBM2E | 高带宽 |
| 显存容量 | 未公开 | 依型号 |
| 显存带宽 | 未公开 | 公开资料未披露 |
| INT8 峰值算力 | 160 TOPS | 曦思 N100 |
| FP16 峰值算力 | 80 TFLOPS | 曦思 N100 |
| 视频编码 | 128 路高清 | 同时编码 |
| 视频解码 | 96 路高清 | 同时解码 |
| 支持视频格式 | HEVC、H.264、AV1、AVS2 | 最高 8K |
| 接口 | PCIe Gen4 | 加速卡形态 |
| 软件栈 | MXMACA | 沐曦自研 |
| 量产状态 | 已规模量产 | 2023 年起 |
| 功耗 | 未公开 | 官方未披露 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **智慧城市与安防**：人脸识别、车辆检测、车牌识别、视频结构化分析。
- **智慧交通**：道路监控、车流统计、违章识别。
- **云计算与智算中心**：大模型推理、推荐系统、图像/视频分析。
- **人形机器人云端大脑**：将视觉、语音、决策模型部署在边缘/云端推理节点，为机器人提供 AI 算力支持。

## 供应链关系

- **制造商/设计商**：`ent_company_metax`（沐曦集成电路有限公司）。
- **上游关键物料**：7 nm 晶圆代工、HBM2E 显存、先进封装（2.5D/CoWoS）、PCB、电源管理、散热器。
- **下游客户**：云计算厂商、安防集成商、互联网大厂、AI 算法公司及人形机器人/具身智能平台的云端/边缘算力方案商。
- **知识图谱关系**：
  - `ent_company_metax` — `manufactures` → `ent_product_metax_mxn`
  - `ent_product_metax_mxn` — `uses` → `ent_component_pcie_interface`

## 来源与验证

- 沐曦官方新闻《沐曦首款人工智能推理GPU曦思N100亮相北京安博会》明确列出：内置 MXN100 异构 GPGPU + HBM2E、INT8 160 TOPS、FP16 80 TFLOPS、128 路编码/96 路解码、兼容 HEVC/H.264/AV1/AVS2、最高 8K、MXMACA 软件栈、已规模量产。
- IT之家与腾讯云开发者社区报道重复确认了上述算力与视频处理能力。
- 显存容量、显存带宽及功耗等参数未在公开资料中完整披露，表中标注为“未公开”。