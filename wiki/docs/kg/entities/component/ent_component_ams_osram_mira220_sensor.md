---
id: ent_component_ams_osram_mira220_sensor
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: ams OSRAM Mira220 近红外 CMOS 图像传感器 核心传感单元
  en: ams OSRAM Mira220 NIR CMOS Image Sensor Core Sensing Unit
status: active
sources:
- id: src_ent_component_ams_osram_mira220_sensor_official
  type: website
  url: https://ams-osram.com/products/sensors/area-imaging-sensors/ams-mira220
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# ams OSRAM Mira220 近红外 CMOS 图像传感器 核心传感单元 / ams OSRAM Mira220 NIR CMOS Image Sensor Core Sensing Unit

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [艾迈斯欧司朗（ams OSRAM） / ams OSRAM](../../../appendices/appendix-d/companies/company_ams_osram.md) |
| **产品类别** | 近红外增强全局快门 CMOS 图像传感器 |
| **发布时间** | 2022 年起商用 |
| **状态** | 量产/商用 |
| **官网/来源** | [ams OSRAM Mira220 近红外 CMOS 图像传感器 产品/资料页](https://ams-osram.com/products/sensors/area-imaging-sensors/ams-mira220) |

## 产品概述

Mira220 是 ams OSRAM 面向 3D 传感与近红外成像的 2.2 MP 全局快门 CMOS 图像传感器。它在 850 nm 与 940 nm 近红外波段具有高光量子效率，支持低功耗、高帧率运行，是机器人 3D 视觉、结构光/ToF 相机与舱内监控的理想感光元件。

## 产品图片

> ams OSRAM Mira220 近红外 CMOS 图像传感器：请访问 [官方资料](https://ams-osram.com/products/sensors/area-imaging-sensors/ams-mira220) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 近红外增强全局快门 CMOS | 官网/datasheet |
| 有效像素 | 2.2 MP | 官网/datasheet |
| 分辨率 | 约 1920 × 1080 | 官网/datasheet |
| 光学尺寸 | 1/2.7 型 | 官网/datasheet |
| 像素尺寸 | 2.79 µm | 官网/datasheet |
| 快门 | 全局快门 | 官网/datasheet |
| NIR QE | 850/940 nm 波段高光量子效率 | 官网/datasheet |
| 最大帧率 | 最高 90 fps | 官网/datasheet |
| 接口 | MIPI CSI-2 | 官网/datasheet |
| 功耗 | 未公开 | - |
| 供电 | 未公开 | - |
| 工作温度 | 未公开 | - |
| 封装 | CSP | 官网/datasheet |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[艾迈斯欧司朗（ams OSRAM） / ams OSRAM](../../../appendices/appendix-d/companies/company_ams_osram.md)
- **核心零部件/技术来源**：自研 NIR 增强像素、全局快门读出电路、MIPI 接口、晶圆级光学（WLO）适配。
- **下游应用/客户**：3D 相机模组厂、机器人 OEM、AR/VR 设备商、安防监控、汽车 Tier 1。

## 知识图谱节点与关系

- 产品实体：`ent_product_ams_osram_mira220`
- 零部件实体：`ent_component_ams_osram_mira220_sensor`
- 制造商实体：`ent_company_ams_osram`
- 关键关系：
  - `rel_ent_company_ams_osram_manufactures_ent_product_ams_osram_mira220`（`ent_company_ams_osram` → `manufactures` → `ent_product_ams_osram_mira220`）
  - `rel_ent_company_ams_osram_manufactures_ent_component_ams_osram_mira220_sensor`（`ent_company_ams_osram` → `manufactures` → `ent_component_ams_osram_mira220_sensor`）
  - `rel_ent_product_ams_osram_mira220_uses_ent_component_ams_osram_mira220_sensor`（`ent_product_ams_osram_mira220` → `uses` → `ent_component_ams_osram_mira220_sensor`）

## 应用场景

- **机器人 3D 视觉**：配合结构光/ToF 投射器获取高质量深度图。
- **人脸识别与手势**：高 NIR QE 提升暗光与强光下的识别率。
- **舱内监控**：低功耗持续监控驾驶员/乘客状态。
- **AR/VR 追踪**：高速全局快门减少运动伪影。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | NIR 全局快门 CMOS | Sony IMX426 | Himax 3D 传感 |
| NIR 优化 | 850/940 nm 高光 QE | 部分型号支持 | 模组级方案 |
| 快门 | 全局快门 | 全局快门 | 结构光/ToF |
| 核心优势 | 发射+接收光学整合 | 高分辨率 | WLO 小型化 |

## 选购与部署建议

- 根据目标应用的分辨率、量程、精度或算力需求选择具体型号。
- 部署前确认接口、供电、散热、机械安装与环境温度范围匹配。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：艾迈斯欧司朗（ams OSRAM） / ams OSRAM](../../../appendices/appendix-d/companies/company_ams_osram.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [ams OSRAM 官网](https://ams-osram.com)
2. [ams OSRAM Mira220 近红外 CMOS 图像传感器 产品/资料页](https://ams-osram.com/products/sensors/area-imaging-sensors/ams-mira220)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)