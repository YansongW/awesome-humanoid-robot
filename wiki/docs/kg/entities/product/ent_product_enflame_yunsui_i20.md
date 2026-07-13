---
id: ent_product_enflame_yunsui_i20
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 燧原科技 云燧 i20 推理加速卡
  en: Enflame Yunsui i20 Inference Accelerator
status: active
sources:
- id: src_ent_product_enflame_yunsui_i20_official
  type: website
  url: https://www.enflame-tech.com
- id: src_ent_product_enflame_yunsui_i20_qbitai
  type: website
  url: https://www.qbitai.com/2021/12/30826.html
- id: src_ent_product_enflame_yunsui_i20_china
  type: website
  url: https://m.tech.china.com/digi/digi/20211209/20211209947033.html
- id: src_ent_product_enflame_yunsui_i20_baike
  type: website
  url: https://baike.baidu.com/item/%E4%BA%91%E7%87%A7i20/59510967
- id: src_ent_product_enflame_yunsui_i20_wiki
  type: website
  url: docs/appendices/appendix-d/companies/company_enflame.md
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 燧原科技 云燧 i20 推理加速卡 / Enflame Yunsui i20 Inference Accelerator

## 概述

云燧 i20 是燧原科技（Enflame Technology）于 2021 年 12 月发布的第二代云端人工智能推理加速卡，基于自研“邃思 2.5”AI 推理芯片打造。该产品采用 12 nm 工艺与第二代 GCU-CARA 架构，通过架构升级提升单位面积晶体管效率，并搭载高带宽 HBM2E 显存，面向云端推理、大模型推理、推荐系统、计算机视觉、语音识别与自然语言处理等场景，已在互联网、智慧城市、智慧政务、金融、交通、能源等领域商用。

## 工作原理与技术架构

云燧 i20 的核心为“邃思 2.5”AI 推理芯片，采用第二代高性能计算核心与数据引擎，支持从 FP32、TF32、FP16、BF16 到 INT8 的多种数据精度。其峰值算力分别为：

- FP32：
  $$
  R_{\text{FP32}} = 32\ \text{TFLOPS}
  $$

- TF32：
  $$
  R_{\text{TF32}} = 128\ \text{TFLOPS}
  $$

- INT8：
  $$
  R_{\text{INT8}} = 256\ \text{TOPS}
  $$

显存采用 16 GB HBM2E，存储带宽达到：

$$
B_{\text{HBM2E}} = 819\ \text{GB/s}
$$

高带宽显存有效缓解大规模神经网络推理中的内存墙问题。软件栈“驭算 TopsRider”通过通用高层图优化、算子融合、低精度量化与混合精度支持，提升模型推理效率；同时支持单卡多实例，最多可同时运行 6 个相互隔离的业务。

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 产品定位 | 云端 AI 推理加速卡 | 第二代 |
| 核心芯片 | 邃思 2.5 | 自研 GCU-CARA 2.0 |
| 制程工艺 | 12 nm | — |
| 芯片尺寸 | 55 mm × 55 mm | — |
| 显存 | 16 GB HBM2E | — |
| 显存带宽 | 819 GB/s | — |
| FP32 峰值算力 | 32 TFLOPS | — |
| TF32 峰值算力 | 128 TFLOPS | — |
| INT8 峰值算力 | 256 TOPS | — |
| 支持精度 | FP32、TF32、FP16、BF16、INT8 | — |
| 接口 | PCIe 4.0 ×16 | — |
| 最大功耗 | 150 W | — |
| 软件栈 | 驭算 TopsRider | — |
| 支持模型 | 175+ 主流模型 | CV/NLP/语音 |
| 多实例隔离 | 最多 6 个业务 | 单卡多用户 |
| 兼容服务器 | 浪潮、H3C、Supermicro 等 | PCIe Gen4 AI 服务器 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **云端大模型推理**：自然语言处理、对话系统、推荐系统。
- **计算机视觉**：图像分类、目标检测、视频内容分析、人脸识别。
- **语音与 NLP**：语音识别、语义理解、文本情感分析。
- **智慧城市与政务**：城市大脑、智慧交通、金融风控。
- **人形机器人云端大脑**：将感知、认知与决策模型部署于云端或边缘推理节点，为机器人提供实时 AI 算力。

## 供应链关系

- **设计商/制造商**：`ent_company_enflame`（上海燧原科技有限公司）。
- **上游关键物料**：12 nm 晶圆代工、HBM2E 显存、先进封装、PCIe 4.0 PCB、电源管理、散热器。
- **下游客户**：互联网大厂、云计算厂商、智算中心、AI 企业、科研院所及机器人/具身智能平台。
- **知识图谱关系**：
  - `ent_company_enflame` — `manufactures` → `ent_product_enflame_yunsui_i20`
  - `ent_product_enflame_yunsui_i20` — `uses` → `ent_component_hbm_memory`
  - `ent_product_enflame_yunsui_i20` — `uses` → `ent_component_pcie_interface`

## 来源与验证

- 燧原科技官方及多家科技媒体报道确认了云燧 i20 基于邃思 2.5、12 nm 工艺、16 GB HBM2E、819 GB/s 显存带宽、FP32 32 TFLOPS、TF32 128 TFLOPS、INT8 256 TOPS、PCIe 4.0 ×16、150 W 功耗、驭算 TopsRider 软件栈及 175+ 模型支持。
- 百度百科词条亦对上述核心参数进行了汇总。
- 附录 D Wiki《燧原科技 / Enflame Technology》词条确认了云燧 i20 作为燧原第二代云端推理产品的定位。