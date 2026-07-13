---
id: ent_product_megvii_megengine
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 旷视天元 MegEngine 深度学习框架
  en: Megvii MegEngine Deep Learning Framework
status: active
sources:
- id: src_ent_product_megvii_megengine_1
  type: website
  url: https://en.megvii.com/news_detail/id/124
- id: src_ent_product_megvii_megengine_2
  type: website
  url: https://github.com/MegEngine
- id: src_ent_product_megvii_megengine_3
  type: website
  url: https://pandaily.com/chinese-ai-startup-megvii-open-sources-its-proprietary-deep-learning-framework-megengine
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 旷视天元 MegEngine 深度学习框架 / Megvii MegEngine Deep Learning Framework

## 概述

天元 MegEngine 是旷视科技自主研发的工业级深度学习框架，也是旷视 Brain++ AI 生产力平台的核心组件之一（另两个组件为 MegData 数据管理平台与 MegCompute 算力调度系统）。MegEngine 于 2014 年启动内部研发，2020 年 3 月正式以 Apache 2.0 协议开源。该框架强调“训练推理一体”，支持动态图与静态图混合编程，并针对计算机视觉任务进行了深度优化，已广泛应用于旷视的人脸识别、物体检测、图像分割、物流机器人及工业检测等业务。

## 工作原理 / 技术架构

MegEngine 采用五层架构：计算接口层、图表示层、优化与编译层、运行时管理层以及计算内核层。其核心特性包括：

- **训练推理一体化**：避免传统方案中训练框架与推理框架转换导致的性能或精度损失，可直接部署训练后的模型。
- **动静合一**：支持动态图调试与静态图优化的一键切换，兼顾开发效率与执行性能。
- **自动亚线性内存优化**：通过梯度重计算等技术降低大模型训练显存占用。
- **低比特量化**：支持 FP32、FP16、INT8 及 CUDA INT4 量化推理，其中 INT4 可将模型体积压缩至 FP32 的 1/4，并在 ResNet-50 等模型上相比 INT8 获得约 1.3 倍加速。
- **多硬件兼容**：计算内核兼容 CPU、GPU 及主流 AI 芯片，支持多机多卡分布式训练。

在量化场景中，模型体积压缩倍数可表示为

$$
\frac{V_{\text{FP32}}}{V_{\text{INT8}}} = 4, \quad \frac{V_{\text{FP32}}}{V_{\text{INT4}}} = 8
$$

实际加速比受硬件 Tensor Core/INT 单元支持及算子融合策略影响。

## 关键参数表

| 参数项 | 典型值/范围 | 备注/来源 |
|--------|-------------|-----------|
| 产品类型 | 深度学习训练与推理框架 | 旷视官方 |
| 中文名 | 天元 | 旷视官方 |
| 开源协议 | Apache 2.0 | GitHub / 官方新闻 |
| 内部研发起始 | 2014 年 | 旷视官方 |
| 开源时间 | 2020 年 3 月 | 旷视官方 |
| 支持语言 | Python / C++ | 官方文档 |
| 编程范式 | 动态图 / 静态图 / 混合编程 | 官方文档 |
| 主要优化方向 | 计算机视觉、大模型训练、端侧推理 | 官方文档 |
| 量化支持 | FP32 / FP16 / INT8 / INT4（CUDA INT4 开源实现） | 公开报道 |
| 分布式训练 | 支持多机多卡 | 官方文档 |
| 模型兼容 | 可导入 PyTorch Module | 官方文档 |
| 典型生态项目 | BaseDet（目标检测代码库）、Objects365 数据集 | GitHub |
| 价格 | 免费开源 | Apache 2.0 |

## 应用场景

- **机器人视觉算法**：目标检测、语义分割、实例分割、姿态估计，用于 AMR、物流机器人与人形机器人感知。
- **工业检测**：缺陷检测、尺寸测量、OCR、产品分类。
- **自动驾驶**：感知模型训练与部署、BEV 算法开发。
- **智能终端**：手机端人脸识别、计算摄影、AI 相机等端侧推理。
- **人脸识别与安防**：旷视早期商业化产品均基于 MegEngine 训练与部署。

## 供应链关系

- **开发商**：旷视科技 / Megvii（`ent_company_megvii`）。
- **所属平台**：Brain++ AI 生产力平台（MegEngine + MegData + MegCompute）。
- **上游关键零部件/材料**：GPU/AI 芯片、服务器、开源社区贡献、训练数据集。
- **下游客户/应用场景**：旷视物流机器人、工业检测方案、开发者社区、企业客户。
- **竞争/对标**：PyTorch、TensorFlow、百度 PaddlePaddle、华为 MindSpore、OneFlow。
- **知识图谱关系**：`ent_company_megvii` — `manufactures` → `ent_product_megvii_megengine`；`ent_product_megvii_logistics_robot` — `uses` → `ent_product_megvii_megengine`。

## 来源与验证

1. [旷视官方新闻：MegEngine 开源](https://en.megvii.com/news_detail/id/124)
2. [MegEngine GitHub 组织](https://github.com/MegEngine)
3. [Pandaily：Megvii Open Sources MegEngine](https://pandaily.com/chinese-ai-startup-megvii-open-sources-its-proprietary-deep-learning-framework-megengine)
4. [附录 D 企业 Wiki：旷视科技](../../../appendices/appendix-d/companies/company_megvii.md)