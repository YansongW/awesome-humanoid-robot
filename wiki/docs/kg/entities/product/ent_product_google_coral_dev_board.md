---
id: ent_product_google_coral_dev_board
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Coral Dev Board
  en: Coral Dev Board
status: active
sources:
- id: src_ent_product_google_coral_dev_board_official
  type: website
  url: https://coral.ai/products/dev-board/
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# Coral Dev Board / Coral Dev Board

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Google Coral / Google Coral](../../../appendices/appendix-d/companies/company_google_coral.md) |
| **产品类别** | 边缘 AI 开发板 / Edge TPU 评估平台 |
| **发布时间** | 2019 年 |
| **状态** | 量产/商用 |
| **官网/来源** | [Coral Dev Board Product Page](https://coral.ai/products/dev-board/) |

## 产品概述

Google Coral Dev Board 是一款集成 Edge TPU 的 AI 开发板，采用可拆卸 SoM 设计。其 Edge TPU 提供 4 TOPS INT8 算力，典型功耗仅约 2 W，可在本地高效运行 MobileNet、EfficientDet-Lite 等量化模型。开发板提供与 Raspberry Pi 兼容的 40-pin GPIO、MIPI CSI/DSI、HDMI、USB 3.0 和千兆以太网，适合机器人感知、智能相机和工业视觉原型的快速验证。

## 产品图片

> Google Coral Dev Board：请访问 [官方资料](https://coral.ai/products/dev-board/) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| SoC | NXP i.MX 8M（四核 Cortex-A53 + Cortex-M4F） | Coral 公开资料 |
| AI 加速器 | Google Edge TPU | Coral 公开资料 |
| AI 算力 | 最高 4 TOPS INT8 | Coral 公开资料 |
| 能效 | 约 2 TOPS/W | Coral 公开资料 |
| 内存 | 1 GB / 4 GB LPDDR4（依版本） | Coral 公开资料 |
| 存储 | 8 GB / 16 GB / 64 GB eMMC + MicroSD | Coral 公开资料 |
| 制程 | Edge TPU 未公开；i.MX 8M 14 nm | Coral 公开资料 |
| 接口 | USB 3.0、GbE、HDMI 2.0、MIPI CSI/DSI、40-pin GPIO、PCIe（SoM） | Coral 公开资料 |
| 功耗 | 约 5 W 典型（整板） | Coral 公开资料 |
| 尺寸 | 约 88 mm × 60 mm（含散热器） | Coral 公开资料 |
| 价格 | Dev Board 约 150 USD（参考价） | Coral 公开资料 |

## 供应链位置

- **制造商**：[Google Coral / Google Coral](../../../appendices/appendix-d/companies/company_google_coral.md)
- **核心零部件/技术来源**：Google 自研 Edge TPU、NXP i.MX 8M SoC、LPDDR4/eMMC、PMIC、载板/散热器
- **下游应用/客户**：机器人整机厂、AIoT 方案商、智能相机厂商、高校与开发者社区

## 知识图谱节点与关系

- 产品实体：`ent_product_google_coral_dev_board`
- 零部件实体：`ent_component_google_coral_edge_tpu`
- 制造商实体：`ent_company_google_coral`
- 关键关系：
  - `rel_ent_company_google_coral_manufactures_ent_product_google_coral_dev_board`（`ent_company_google_coral` → `manufactures` --> `ent_product_google_coral_dev_board`）
  - `rel_ent_company_google_coral_manufactures_ent_component_google_coral_edge_tpu`（`ent_company_google_coral` → `manufactures` --> `ent_component_google_coral_edge_tpu`）
  - `ent_product_google_coral_dev_board` -- `uses` --> `ent_component_google_coral_edge_tpu`

## 应用场景

- **机器人端侧感知**：实时目标检测、语义分割与导航辅助，降低云端依赖
- **智能相机原型**：本地事件检测与人脸识别，提升隐私与响应速度
- **工业视觉检测**：缺陷分类、条码/二维码识别与产线质检

## 竞争对比

| 对比项 | Coral Dev Board | NVIDIA Jetson Nano | Raspberry Pi 5 + AI HAT |
|---|---|---|---|
| 算力 | 4 TOPS | 0.5 TFLOPS | 13 TOPS |
| 功耗 | 约 5 W | 5–10 W | 约 7 W |
| 生态 | TensorFlow Lite | JetPack / CUDA | Raspberry Pi / Hailo |

## 选购与部署建议

优先使用 Edge TPU Compiler 将 TensorFlow Lite 模型量化并编译；确认主机接口与驱动版本；量产时建议采用 Coral SoM 定制载板以优化 BOM。

## 相关词条

- [制造商：Google Coral / Google Coral](../../../appendices/appendix-d/companies/company_google_coral.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [Coral Dev Board 产品页](https://coral.ai/products/dev-board/)
2. [Coral 官方文档](https://coral.ai/docs/)
3. [Coral Dev Board 数据手册](https://coral.ai/docs/dev-board/datasheet/)