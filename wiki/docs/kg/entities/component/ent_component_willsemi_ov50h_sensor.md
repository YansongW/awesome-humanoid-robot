---
id: ent_component_willsemi_ov50h_sensor
type: component
'title:': Will Semiconductor OmniVision OV50H Image Sensor Core Component
domain: 02_components
theoretical_depth: system
aliases:
- 韦尔股份 OmniVision OV50H 图像传感器 核心零部件
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-09 00:00:00+00:00
sources:
- id: ent_component_willsemi_ov50h_sensor_official
  type: website
  url: https://www.ovt.com/products/ov50h/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-09 00:00:00+00:00
  review_notes: Specifications from official datasheets and public reports; missing
    values marked as 未公开.
---





# willsemi_ov50h_sensor

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [韦尔股份 / Will Semiconductor](../../../appendices/appendix-d/companies/company_willsemi.md) |
| **产品类别** | 50MP 高端移动设备 CMOS 图像传感器 |
| **发布时间** | 2023 年发布/量产 |
| **状态** | 量产/商用 |
| **官网/来源** | [韦尔股份 OmniVision OV50H 图像传感器产品/资料页](https://www.ovt.com/products/ov50h/) |

## 产品概述

OmniVision OV50H 是面向高端智能手机后置主摄的 5000 万像素图像传感器，采用 PureCel®Plus-S 堆栈技术与 1.2 µm 像素，支持双转换增益（DCG™）HDR、水平/垂直四向相位检测（H/V QPD）自动对焦，具备旗舰级低光与对焦性能。

## 产品图片

> 韦尔股份 OmniVision OV50H 图像传感器：请访问 [官方资料](https://www.ovt.com/products/ov50h/) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 50MP CMOS 图像传感器 | OmniVision 官网 |
| 有效像素 | 50 MP（8192 × 6144） | OmniVision 官网 |
| 像素尺寸 | 1.197 µm | OmniVision 官网 |
| 光学尺寸 | 1/1.3" | OmniVision 官网 |
| 技术 | PureCel®Plus-S、DCG™ HDR、H/V QPD | OmniVision 官网 |
| 帧率 | 50MP@30fps / 12.5MP@120fps | OmniVision 官网 |
| HDR | DCG / Staggered HDR | OmniVision 官网 |
| 对焦 | H/V QPD PDAF，100% 覆盖率 | OmniVision 官网 |
| 输出格式 | 10/12/14-bit RGB RAW | OmniVision 官网 |
| 接口 | 4-lane MIPI / C-PHY | OmniVision 官网 |
| 功耗 | 活动模式约 1395 mW（50MP@30fps） | OmniVision 官网 |
| 工作温度 | -30℃ – +85℃ | OmniVision 官网 |
| 封装 | COB / RW | OmniVision 官网 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[韦尔股份 / Will Semiconductor](../../../appendices/appendix-d/companies/company_willsemi.md)
- **核心零部件/技术来源**：晶圆代工、封装测试、光学镜头、滤光片、ISP 算法
- **下游应用/客户**：智能手机 OEM、笔记本厂商、车载 Tier1、机器人、医疗设备

## 知识图谱节点与关系

- 产品实体：`ent_product_willsemi_ov50h`
- 零部件实体：`ent_component_willsemi_ov50h_sensor`
- 制造商实体：`ent_company_willsemi`
- 关键关系：
  - `rel_ent_company_willsemi_manufactures_ent_product_willsemi_ov50h`（`ent_company_willsemi` → `manufactures` → `ent_product_willsemi_ov50h`）
  - `rel_ent_company_willsemi_manufactures_ent_component_willsemi_ov50h_sensor`（`ent_company_willsemi` → `manufactures` → `ent_component_willsemi_ov50h_sensor`）
  - `ent_product_willsemi_ov50h` -- `uses` --> `ent_component_willsemi_ov50h_sensor`

## 应用场景

- **高端智能手机主摄/广角、笔记本摄像头、视频会议、机器人视觉、车载感知**

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

- [制造商：韦尔股份 / Will Semiconductor](../../../appendices/appendix-d/companies/company_willsemi.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [韦尔股份官网](https://www.willsemi.com)
2. [韦尔股份 OmniVision OV50H 图像传感器产品/资料页](https://www.ovt.com/products/ov50h/)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)