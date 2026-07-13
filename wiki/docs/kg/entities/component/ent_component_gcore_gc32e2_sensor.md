---
id: ent_component_gcore_gc32e2_sensor
type: component
'title:': GalaxyCore GC32E2 CMOS Image Sensor Core Component
domain: 02_components
theoretical_depth: system
aliases:
- 格科微 GC32E2 CMOS 图像传感器 核心零部件
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-09 00:00:00+00:00
sources:
- id: ent_component_gcore_gc32e2_sensor_official
  type: website
  url: https://en.gcoreinc.com/news/detail-67
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-09 00:00:00+00:00
  review_notes: Specifications from official datasheets and public reports; missing
    values marked as 未公开.
---





# gcore_gc32e2_sensor

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [格科微 / GalaxyCore](../../../appendices/appendix-d/companies/company_gcore.md) |
| **产品类别** | 32MP CMOS 图像传感器 |
| **发布时间** | 2024 年量产 |
| **状态** | 量产/商用 |
| **官网/来源** | [格科微 GC32E2 CMOS 图像传感器产品/资料页](https://en.gcoreinc.com/news/detail-67) |

## 产品概述

格科微 GC32E2 是第二代高性能单芯片 32MP CMOS 图像传感器，采用背照式（BSI）工艺与单帧 DAG HDR 技术，可在预览、拍照与录像中保留高亮与暗部细节。传感器支持 PDAF 相位检测对焦与 AON 低功耗模式，适用于智能手机前摄及机器人视觉等场景。

## 产品图片

> 格科微 GC32E2 CMOS 图像传感器：请访问 [官方资料](https://en.gcoreinc.com/news/detail-67) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 32MP CMOS 图像传感器 | 格科微官网 |
| 有效像素 | 32 MP | 格科微官网 |
| 像素尺寸 | 0.7 µm | 格科微官网 |
| 光学尺寸 | 1/3.1" | 格科微官网 |
| 工艺 | 背照式（BSI） | 格科微官网 |
| 快门 | 卷帘快门 | 格科微官网 |
| HDR | 单帧 DAG HDR | 格科微官网 |
| 对焦 | PDAF 相位检测对焦 | 格科微官网 |
| 输出格式 | RAW 10 / 12 | 格科微官网 |
| 接口 | MIPI D-PHY | 格科微官网 |
| 封装 | COB / COM | 格科微官网 |
| 帧率 | 最高 15 fps（全分辨率） | 格科微官网 |
| 工作温度 | -20℃ – +70℃ | 格科微官网 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[格科微 / GalaxyCore](../../../appendices/appendix-d/companies/company_gcore.md)
- **核心零部件/技术来源**：晶圆代工、封装测试、彩色滤光片、微透镜、载板
- **下游应用/客户**：智能手机 OEM、ODM、平板、机器人、IoT 摄像头厂商

## 知识图谱节点与关系

- 产品实体：`ent_product_gcore_gc32e2`
- 零部件实体：`ent_component_gcore_gc32e2_sensor`
- 制造商实体：`ent_company_gcore`
- 关键关系：
  - `rel_ent_company_gcore_manufactures_ent_product_gcore_gc32e2`（`ent_company_gcore` → `manufactures` → `ent_product_gcore_gc32e2`）
  - `rel_ent_company_gcore_manufactures_ent_component_gcore_gc32e2_sensor`（`ent_company_gcore` → `manufactures` → `ent_component_gcore_gc32e2_sensor`）
  - `ent_product_gcore_gc32e2` -- `uses` --> `ent_component_gcore_gc32e2_sensor`

## 应用场景

- **智能手机前摄、平板电脑、机器人视觉、可穿戴设备、视频通话**

## 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 见规格参数表 | 同类产品 | 同类产品 |
| 核心优势 | 官方公开性能指标 | 竞品公开指标 | 竞品公开指标 |
| 生态/服务 | 制造商官方支持 | 竞品生态 | 竞品生态 |

## 选购与部署建议

- 根据目标应用的分辨率、量程、精度或算力需求选择具体型号。
- 部署前确认接口、供电、散热、机械安装与环境温度范围匹配。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：格科微 / GalaxyCore](../../../appendices/appendix-d/companies/company_gcore.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [格科微官网](https://www.gcoreinc.com)
2. [格科微 GC32E2 CMOS 图像传感器产品/资料页](https://en.gcoreinc.com/news/detail-67)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)