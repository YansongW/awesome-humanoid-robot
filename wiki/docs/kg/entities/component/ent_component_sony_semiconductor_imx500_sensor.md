---
id: ent_component_sony_semiconductor_imx500_sensor
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: Sony IMX500 智能视觉传感器 核心传感单元
  en: Sony IMX500 Intelligent Vision Sensor Core Sensing Unit
status: active
sources:
- id: src_ent_component_sony_semiconductor_imx500_sensor_official
  type: website
  url: https://www.sony-semicon.co.jp/products/common/IMX500.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# Sony IMX500 智能视觉传感器 核心传感单元 / Sony IMX500 Intelligent Vision Sensor Core Sensing Unit

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [索尼半导体解决方案（Sony Semiconductor Solutions） / Sony Semiconductor Solutions](../../../appendices/appendix-d/companies/company_sony_semiconductor.md) |
| **产品类别** | 堆栈式 CMOS 图像传感器（集成 AI 推理） |
| **发布时间** | 2020 年起商用 |
| **状态** | 量产/商用 |
| **官网/来源** | [Sony IMX500 智能视觉传感器 产品/资料页](https://www.sony-semicon.co.jp/products/common/IMX500.html) |

## 产品概述

IMX500 是世界首款在像素芯片与逻辑芯片堆栈结构中集成 AI 处理单元的图像传感器。它可在传感器端完成图像识别与推理，仅输出元数据，显著降低系统功耗与数据带宽，适用于机器人视觉、智能监控与具身智能边缘设备。

## 产品图片

> Sony IMX500 智能视觉传感器：请访问 [官方资料](https://www.sony-semicon.co.jp/products/common/IMX500.html) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 堆栈式 CMOS 图像传感器 + AI 推理 | 官网/datasheet |
| 有效像素 | 约 1230 万（4056 × 3040） | 官网/datasheet |
| 光学尺寸 | 1/2.3 型 | 官网/datasheet |
| 像素尺寸 | 未公开 | - |
| 快门 | 卷帘快门 | 官网/datasheet |
| 最大帧率 | 未公开 | - |
| AI 能力 | 传感器端 AI 模型推理 | 官网/datasheet |
| 输出格式 | 元数据 / 图像 + 元数据 | 官网/datasheet |
| 接口 | MIPI D-PHY / SLVS-EC | 官网/datasheet |
| 供电 | 未公开 | - |
| 功耗 | 未公开 | - |
| 工作温度 | 未公开 | - |
| 封装 | COB / CSP | 官网/datasheet |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[索尼半导体解决方案（Sony Semiconductor Solutions） / Sony Semiconductor Solutions](../../../appendices/appendix-d/companies/company_sony_semiconductor.md)
- **核心零部件/技术来源**：自研堆栈式像素芯片、AI 处理逻辑芯片、DRAM、ISP 算法、参考设计与模型工具链。
- **下游应用/客户**：机器人 OEM、智能相机厂商、安防监控、工业视觉集成商、汽车 Tier 1、消费电子品牌。

## 知识图谱节点与关系

- 产品实体：`ent_product_sony_semiconductor_imx500`
- 零部件实体：`ent_component_sony_semiconductor_imx500_sensor`
- 制造商实体：`ent_company_sony_semiconductor`
- 关键关系：
  - `rel_ent_company_sony_semiconductor_manufactures_ent_product_sony_semiconductor_imx500`（`ent_company_sony_semiconductor` → `manufactures` → `ent_product_sony_semiconductor_imx500`）
  - `rel_ent_company_sony_semiconductor_manufactures_ent_component_sony_semiconductor_imx500_sensor`（`ent_company_sony_semiconductor` → `manufactures` → `ent_component_sony_semiconductor_imx500_sensor`）
  - `rel_ent_product_sony_semiconductor_imx500_uses_ent_component_sony_semiconductor_imx500_sensor`（`ent_product_sony_semiconductor_imx500` → `uses` → `ent_component_sony_semiconductor_imx500_sensor`）

## 应用场景

- **机器人视觉感知**：低延迟物体识别与定位，减少主控算力占用。
- **智能监控**：仅输出事件元数据，保护隐私并降低存储成本。
- **工业质检**：边缘 AI 实时缺陷分类与装配验证。
- **具身智能**：端侧感知-决策闭环，降低系统响应延迟。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 智能视觉传感器 | 格科微 GC32E2 | OmniVision OX08D10 |
| AI 位置 | 传感器内推理 | ISP/SoC 侧 | ISP/SoC 侧 |
| 输出 | 元数据/图像+元数据 | RAW 图像 | RAW 图像 |
| 核心优势 | 低功耗、低带宽、隐私 | 高像素、低成本 | 车载高动态 |

## 选购与部署建议

- 根据目标应用的分辨率、量程、精度或算力需求选择具体型号。
- 部署前确认接口、供电、散热、机械安装与环境温度范围匹配。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：索尼半导体解决方案（Sony Semiconductor Solutions） / Sony Semiconductor Solutions](../../../appendices/appendix-d/companies/company_sony_semiconductor.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [Sony Semiconductor Solutions 官网](https://www.sony-semicon.co.jp)
2. [Sony IMX500 智能视觉传感器 产品/资料页](https://www.sony-semicon.co.jp/products/common/IMX500.html)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)