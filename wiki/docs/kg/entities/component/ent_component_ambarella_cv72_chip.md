---
id: ent_component_ambarella_cv72_chip
type: component
'title:': Ambarella CV72 SoC
domain: 02_components
theoretical_depth: system
aliases:
- Ambarella CVflow AI Accelerator
- CV72 SoC
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-09 00:00:00+00:00
sources:
- id: ent_component_ambarella_cv72_chip_official
  type: website
  url: https://www.ambarella.com/products/aiot-industrial-robotics/cv72-ai-soc/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-09 00:00:00+00:00
  review_notes: Specifications from official datasheets and public reports; missing
    values marked as 未公开.
---





# ambarella_cv72_chip

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [安霸 / Ambarella](../../../appendices/appendix-d/companies/company_ambarella.md) |
| **产品类别** | 边缘 AI 视觉 SoC / 安防与机器人视觉处理器 |
| **发布时间** | 2023 年（CV72S） |
| **状态** | 量产/商用 |
| **官网/来源** | [Ambarella CV72 Product Page](https://www.ambarella.com/products/aiot-industrial-robotics/cv72-ai-soc/) |

## 产品概述

Ambarella CV72 系列是基于 5 nm 工艺的边缘 AI 视觉 SoC，搭载第三代 CVflow AI 加速器与集成 ISP。其 AI 算力约 12 TOPS，可在本地运行最新的 CNN 与 Transformer 网络，同时以低于 3 W 的功耗支持多路 4K/8K 视频编码。CV72 还支持雷达-视觉传感器融合与 AI-ISP 增强夜视，是安防相机、机器人视觉与工业检测的理想平台。

## 产品图片

> Ambarella CV72 视觉 AI SoC：请访问 [官方资料](https://www.ambarella.com/products/aiot-industrial-robotics/cv72-ai-soc/) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制程 | 5 nm（公开报道） | Ambarella 公开资料 |
| CPU | 双核 / 四核 Arm Cortex-A76（依版本最高 1.8 GHz） | Ambarella 公开资料 |
| AI 加速器 | 第三代 CVflow AI 加速器 | Ambarella 公开资料 |
| AI 算力 | 约 12 TOPS（CV72，公开报道） | Ambarella 公开资料 |
| ISP | 集成高性能 ISP，支持低照度 HDR、AI-ISP（AISP） | Ambarella 公开资料 |
| 视频 | 4Kp120 / 8Kp30 编码，多路视频并发 | Ambarella 公开资料 |
| 内存 | 支持 LPDDR4x / LPDDR5 / LPDDR5x | Ambarella 公开资料 |
| 接口 | PCIe、USB 3.2、GbE、MIPI CSI、雷达融合接口 | Ambarella 公开资料 |
| 功耗 | 典型 < 3 W（CV72S，公开报道） | Ambarella 公开资料 |
| 封装 | 未公开 | Ambarella 公开资料 |
| 价格 | 未公开 | Ambarella 公开资料 |

## 供应链位置

- **制造商**：[安霸 / Ambarella](../../../appendices/appendix-d/companies/company_ambarella.md)
- **核心零部件/技术来源**：三星 5 nm 代工、ARM CPU IP、自研 CVflow/ISP、LPDDR5x、封测、载板
- **下游应用/客户**：安防 OEM、智能相机方案商、机器人与无人机厂商、交通监控集成商

## 知识图谱节点与关系

- 产品实体：`ent_product_ambarella_cv72`
- 零部件实体：`ent_component_ambarella_cv72_chip`
- 制造商实体：`ent_company_ambarella`
- 关键关系：
  - `rel_ent_company_ambarella_manufactures_ent_product_ambarella_cv72`（`ent_company_ambarella` → `manufactures` --> `ent_product_ambarella_cv72`）
  - `rel_ent_company_ambarella_manufactures_ent_component_ambarella_cv72_chip`（`ent_company_ambarella` → `manufactures` --> `ent_component_ambarella_cv72_chip`）
  - `ent_product_ambarella_cv72` -- `uses` --> `ent_component_ambarella_cv72_chip`

## 应用场景

- **机器人视觉**：多路相机实时目标检测、语义分割与导航辅助
- **智能安防相机**：边缘端 4K AI 分析、低照度彩色夜视、人脸/车牌识别
- **工业视觉检测**：高速缺陷检测、尺寸测量、OCR 与条码识别

## 竞争对比

| 对比项 | Ambarella CV72 | Qualcomm QCS8550 | NVIDIA Jetson Orin NX |
|---|---|---|---|
| 制程 | 5 nm | 4 nm | 8 nm |
| AI 算力 | 约 12 TOPS | 约 15 TOPS | 最高 100 TOPS |
| 功耗 | < 3 W | 约 5–10 W | 10–25 W |

## 选购与部署建议

评估 Ambarella SDK 对目标 Transformer/CNN 模型的支持；利用 CVflow 工具链量化并优化模型；根据相机与雷达接口选择对应 CV72 版本及参考设计。

## 相关词条

- [制造商：安霸 / Ambarella](../../../appendices/appendix-d/companies/company_ambarella.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [Ambarella CV72 产品页](https://www.ambarella.com/products/aiot-industrial-robotics/cv72-ai-soc/)
2. [Ambarella CV72S 新闻稿](https://www.ambarella.com/news/ambarella-launches-4k-5nm-edge-ai-soc-mainstream-security/)
3. [Ambarella 官网](https://www.ambarella.com)