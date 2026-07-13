---
id: ent_product_horizon_journey6
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 地平线 Journey 6
  en: 地平线 Journey 6
status: active
sources:
- id: src_ent_product_horizon_journey6
  type: website
  url: ''
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 地平线 Journey 6

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [地平线 / Horizon Robotics](../../../appendices/appendix-d/companies/company_horizon.md) |
| **产品类别** | 智能驾驶/具身智能计算 SoC |
| **发布时间** | 2024 年发布 |
| **状态** | 量产导入中 |
| **官网/来源** | 见正文参考资料 |

## 产品概述

地平线 Journey 6 系列是面向下一代高阶智能驾驶与具身智能场景的高算力边缘 AI SoC。采用自研 BPU 纳什架构，Journey 6 强调算法与芯片协同设计，支持多路高分辨率摄像头、激光雷达与毫米波雷达融合，目标是为高阶智驾与人形机器人/AMR 提供感知与决策算力。

## 产品图片

> 地平线 Journey 6：请访问 [官方资料](https://www.horizon.ai) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| AI 算力 | Journey 6E 128 TOPS；Journey 6P 560 TOPS | 地平线公开资料 |
| BPU 架构 | BPU 纳什 | 地平线公开资料 |
| CPU | 多核 ARM Cortex-A78AE / 安全核 | 公开报道 |
| ISP | 支持多路高分辨率摄像头 | 地平线公开资料 |
| 功能安全 | ASIL-D / ASIL-B 支持 | 地平线公开资料 |
| 接口 | PCIe、Ethernet、MIPI CSI-2、CAN-FD | 产品手册 |
| 功耗 | 未公开 | - |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[地平线 / Horizon Robotics](../../../appendices/appendix-d/companies/company_horizon.md)
- **核心零部件/技术来源**：晶圆代工、ARM IP、存储器、ISP IP、车规认证、传感器合作伙伴。
- **下游应用/客户**：乘用车 OEM、Tier 1、机器人/AMR 方案商、自动驾驶公司。

## 知识图谱节点与关系

- 产品实体：`ent_product_horizon_journey6`
- 制造商实体：`ent_company_horizon`
- 关键关系：
  - `rel_ent_company_horizon_manufactures_ent_product_horizon_journey6`（`ent_company_horizon` → `manufactures` → `ent_product_horizon_journey6`）
  - `ent_product_horizon_journey6` -- `uses` --> `ent_component_bpu_nash`
  - `ent_product_horizon_journey6` -- `processes` --> `ent_component_camera_sensor`

## 应用场景

- **高阶智驾**：支持高速与城区 NOA、行泊一体。
- **具身智能感知**：为机器人提供视觉/多传感器融合感知。
- **多模态边缘 AI**：低延迟视觉语言理解与决策。

## 竞争对比

| 对比项 | Journey 6 | NVIDIA Orin | Qualcomm Snapdragon Ride |
|--------|------|------|------|
| 算力 | 128–560 TOPS | 254 TOPS | 数十至数百 TOPS |
| 架构 | BPU 纳什 | Ampere/Blackwell | Adreno/DSP |
| 优势 | 算法协同、成本优化 | 生态成熟 | 连接与舱驾一体 |

## 选购与部署建议

- 根据算力/精度/场景需求选择对应型号，优先考虑官方支持的工具链与生态兼容性。
- 部署前确认供电、散热、机械接口与通信协议是否满足整机要求。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：地平线 / Horizon Robotics](../../../appendices/appendix-d/companies/company_horizon.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [地平线 / Horizon Robotics 官方产品/公司页面](https://www.horizon.ai)
2. [地平线官网](https://www.horizon.ai)
3. 地平线 Journey 6 发布会资料