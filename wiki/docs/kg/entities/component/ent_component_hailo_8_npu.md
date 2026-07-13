---
id: ent_component_hailo_8_npu
type: component
'title:': Hailo-8 NPU
domain: 02_components
theoretical_depth: system
aliases:
- Hailo-8 AI Processor
- Hailo-8 Edge NPU
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-09 00:00:00+00:00
sources:
- id: ent_component_hailo_8_npu_official
  type: website
  url: https://hailo.ai/products/hailo-8/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-09 00:00:00+00:00
  review_notes: Specifications from official datasheets and public reports; missing
    values marked as 未公开.
---





# hailo_8_npu

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Hailo](../../../appendices/appendix-d/companies/company_hailo.md) |
| **产品类别** | 边缘 AI 加速器 / NPU |
| **发布时间** | 2019 年发布 Hailo-8 |
| **状态** | 量产/商用 |
| **官网/来源** | Hailo 官网、产品手册 |

## 产品概述

Hailo-8 是 Hailo 推出的边缘 AI 处理器，采用创新的数据流架构（Dataflow Architecture），在低功耗下实现高 AI 算力，广泛应用于机器人、汽车、安防与工业视觉。

Hailo-8 以 BGA 封装、M.2 模组或 PCIe 卡形式提供，可直接集成到现有嵌入式平台中。其数据流架构针对神经网络推理进行了深度优化，算力利用率与能效比优于传统 SIMD/GPU 方案，适合多路视频分析、实时目标检测与机器人端侧感知。

## 产品图片

> Hailo-8 AI 处理器：请访问 [官方资料](https://hailo.ai/products/hailo-8/) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| AI 处理器 | Hailo-8 | Hailo 官网 |
| 架构 | 数据流架构（Dataflow Architecture） | Hailo 公开资料 |
| 制程 | 16 nm | 公开报道 |
| AI 算力 | 最高 26 TOPS INT8 | Hailo 公开资料 |
| 能效 | 约 3 TOPS/W 典型 | Hailo 公开资料 |
| 精度支持 | INT8 / INT4 / FP16（部分） | Hailo 公开资料 |
| 封装尺寸 | 约 15 mm × 15 mm（BGA） | Hailo 公开资料 |
| 接口 | PCIe Gen3 / M.2 / BGA | Hailo 公开资料 |
| 功耗 | 约 2.5 W 典型 | Hailo 公开资料 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[Hailo](../../../appendices/appendix-d/companies/company_hailo.md)
- **核心零部件/技术来源**：自研数据流架构、晶圆代工、封测、模组/载板。
- **下游应用/客户**：汽车 Tier1/OEM、安防厂商、工业相机公司、机器人整机厂、AIoT 设备商。

## 知识图谱节点与关系

- 产品实体：`ent_product_hailo_8`
- 零部件实体：`ent_component_hailo_8_npu`
- 制造商实体：`ent_company_hailo`
- 关键关系：
  - `rel_ent_company_hailo_manufactures_ent_product_hailo_8`（`ent_company_hailo` → `manufactures` --> `ent_product_hailo_8`）
  - `rel_ent_company_hailo_manufactures_ent_component_hailo_8_npu`（`ent_company_hailo` → `manufactures` --> `ent_component_hailo_8_npu`）
  - `ent_product_hailo_8` -- `uses` --> `ent_component_hailo_8_npu`

## 应用场景

- **机器人端侧感知**：实时目标检测、语义分割、姿态估计与导航辅助。
- **智能安防摄像头**：边缘端视频分析与事件检测。
- **汽车 ADAS**：前视/环视感知、舱内监测与低延迟推理。

## 竞争对比

| 对比项 | Hailo-8 | Intel Movidius VPU | 地平线征程 3 |
|--------|------|------|------|
| 算力 | 26 TOPS | 约 4 TOPS | 约 5 TOPS |
| 功耗 | 约 2.5 W | 约 1 W | 约 2.5 W |
| 架构 | 数据流 | VPU / SHAVE | 自研 BPU |
| 生态 | Hailo SDK | OpenVINO | 地平线天工开物 |

## 选购与部署建议

- 优先使用 Hailo Dataflow Compiler 评估目标模型在 Hailo-8 上的性能与精度。
- 根据主机接口选择 M.2、PCIe 或 BGA 形态，确认驱动与 BSP 适配。
- 建议通过 Hailo 官方渠道获取最新 SDK、参考设计与技术支持。

## 相关词条

- [制造商：Hailo](../../../appendices/appendix-d/companies/company_hailo.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [Hailo 官网](https://hailo.ai)
2. [Hailo-8 产品页](https://hailo.ai/products/hailo-8/)
3. Hailo-8 数据手册与开发者文档