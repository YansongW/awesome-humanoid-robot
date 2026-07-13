---
id: ent_product_samsung_electro_mechanics_200mp_camera_module
schema_version: 1
type: product
domain: 02_components
theoretical_depth: system
names:
  zh: 三星电机 200MP ISOCELL 摄像头模组
  en: Samsung Electro-Mechanics 200MP ISOCELL Camera Module
status: active
sources:
- id: src_ent_product_samsung_electro_mechanics_200mp_camera_module_official
  type: website
  url: https://www.samsungsem.com/product/camera-module
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# 三星电机 200MP ISOCELL 摄像头模组 / Samsung Electro-Mechanics 200MP ISOCELL Camera Module

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [三星电机（Samsung Electro-Mechanics） / Samsung Electro-Mechanics](../../../appendices/appendix-d/companies/company_samsung_electro_mechanics.md) |
| **产品类别** | 高像素摄像头模组 |
| **发布时间** | 随旗舰机型迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [三星电机 200MP ISOCELL 摄像头模组 产品/资料页](https://www.samsungsem.com/product/camera-module) |

## 产品概述

该模组是三星电机基于三星 ISOCELL 200MP 图像传感器开发的高像素摄像头模组，集成高精度光学镜头、VCM 自动对焦与 OIS 光学防抖机构。除智能手机主摄外，其高解析力与小型化设计也适用于机器人视觉、无人机航拍与车载环视等场景。

## 产品图片

> 三星电机 200MP ISOCELL 摄像头模组：请访问 [官方资料](https://www.samsungsem.com/product/camera-module) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 高像素摄像头模组 | 官网/新闻稿 |
| 有效像素 | 200 MP | 官网/新闻稿 |
| 光学尺寸 | 约 1/1.3"–1/1.4" | 官网/新闻稿 |
| 像素尺寸 | 约 0.56 µm | 官网/新闻稿 |
| 镜头 | 多片式塑料/玻璃混合镜头 | 官网/新闻稿 |
| 对焦 | VCM 自动对焦 | 官网/新闻稿 |
| 防抖 | 可选 OIS | 官网/新闻稿 |
| 视场角 | 未公开 | - |
| 接口 | MIPI D-PHY / C-PHY | 官网/新闻稿 |
| 模组尺寸 | 未公开 | - |
| 功耗 | 未公开 | - |
| 工作温度 | 未公开 | - |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[三星电机（Samsung Electro-Mechanics） / Samsung Electro-Mechanics](../../../appendices/appendix-d/companies/company_samsung_electro_mechanics.md)
- **核心零部件/技术来源**：ISOCELL 200MP CMOS 图像传感器、混合光学镜头、VCM 马达、OIS 机构、FPC/连接器、封装结构件。
- **下游应用/客户**：智能手机 OEM、机器人整机厂、无人机厂商、汽车 Tier 1、模组集成商。

## 知识图谱节点与关系

- 产品实体：`ent_product_samsung_electro_mechanics_200mp_camera_module`
- 零部件实体：`ent_component_samsung_electro_mechanics_200mp_camera_module`
- 制造商实体：`ent_company_samsung_electro_mechanics`
- 关键关系：
  - `rel_ent_company_samsung_electro_mechanics_manufactures_ent_product_samsung_electro_mechanics_200mp_camera_module`（`ent_company_samsung_electro_mechanics` → `manufactures` → `ent_product_samsung_electro_mechanics_200mp_camera_module`）
  - `rel_ent_company_samsung_electro_mechanics_manufactures_ent_component_samsung_electro_mechanics_200mp_camera_module`（`ent_company_samsung_electro_mechanics` → `manufactures` → `ent_component_samsung_electro_mechanics_200mp_camera_module`）
  - `rel_ent_product_samsung_electro_mechanics_200mp_camera_module_uses_ent_component_samsung_electro_mechanics_200mp_camera_module`（`ent_product_samsung_electro_mechanics_200mp_camera_module` → `uses` → `ent_component_samsung_electro_mechanics_200mp_camera_module`）

## 应用场景

- **智能手机主摄**：超高解析力摄影与多倍无损变焦。
- **机器人视觉**：为移动机器人/人形机器人提供高分辨率视觉输入。
- **车载环视**：高像素环视与行车记录仪。
- **工业检测**：高精度表面缺陷检测与尺寸测量。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 200MP 摄像头模组 | 舜宇光学车载模组 | 丘钛科技机器视觉模组 |
| 传感器 | Samsung ISOCELL 200MP | 多款 CIS | 多款 CIS |
| 像素尺寸 | 约 0.56 µm | 因型号而异 | 因型号而异 |
| 核心优势 | 三星自有传感器+模组垂直整合 | 车载可靠性 | 成本与快速交付 |

## 选购与部署建议

- 根据目标应用的分辨率、量程、精度或算力需求选择具体型号。
- 部署前确认接口、供电、散热、机械安装与环境温度范围匹配。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：三星电机（Samsung Electro-Mechanics） / Samsung Electro-Mechanics](../../../appendices/appendix-d/companies/company_samsung_electro_mechanics.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [Samsung Electro-Mechanics 官网](https://www.samsungsem.com)
2. [三星电机 200MP ISOCELL 摄像头模组 产品/资料页](https://www.samsungsem.com/product/camera-module)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)