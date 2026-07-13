---
id: ent_product_smartsens_sc580xs
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 思特威 SC580XS CMOS 图像传感器
  en: SmartSens SC580XS CMOS Image Sensor
status: active
sources:
- id: src_ent_product_smartsens_sc580xs_official
  type: website
  url: https://www.smartsenstech.com/en/m
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# 思特威 SC580XS CMOS 图像传感器 / SmartSens SC580XS CMOS Image Sensor

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [思特威 / SmartSens](../../../appendices/appendix-d/companies/company_smartsens.md) |
| **产品类别** | 50MP 旗舰手机/机器视觉 CMOS 图像传感器 |
| **发布时间** | 2024 年发布/量产 |
| **状态** | 量产/商用 |
| **官网/来源** | [思特威 SC580XS CMOS 图像传感器产品/资料页](https://www.smartsenstech.com/en/m) |

## 产品概述

思特威 SC580XS 是面向旗舰级智能手机主摄的 5000 万像素 1/1.28 英寸 CMOS 图像传感器，采用 22 nm HKMG Stack 工艺与 SFCPixel®-2 技术，集成 PixGain HDR®、AllPix ADAF® 与 Sparse PDAF，兼顾高动态范围、低噪声与全像素对焦能力。

## 产品图片

> 思特威 SC580XS CMOS 图像传感器：请访问 [官方资料](https://www.smartsenstech.com/en/m) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 50MP CMOS 图像传感器 | 思特威官网 |
| 有效像素 | 50 MP | 思特威官网 |
| 像素尺寸 | 1.22 µm | 思特威官网 |
| 光学尺寸 | 1/1.28" | 思特威官网 |
| 工艺 | 22 nm HKMG Stack | 思特威官网 |
| HDR | PixGain HDR® / 三重曝光 HDR | 思特威官网 |
| 动态范围 | 最高 120 dB | 思特威官网 |
| 读取噪声 | 低至 0.7 e⁻ | 思特威官网 |
| 对焦 | AllPix ADAF® / Sparse PDAF | 思特威官网 |
| 视频 | 4K 120 fps（四合一模式） | 思特威官网 |
| 接口 | MIPI C-PHY / D-PHY | 思特威官网 |
| 功耗 | 50MP@25fps 约 500 mW | 思特威官网 |
| 工作温度 | -20℃ – +70℃ | 思特威官网 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[思特威 / SmartSens](../../../appendices/appendix-d/companies/company_smartsens.md)
- **核心零部件/技术来源**：晶圆代工、封测、光学镜头、滤光片、ISP 算法
- **下游应用/客户**：智能手机 OEM、安防厂商、车载 Tier1、机器人、工业相机

## 知识图谱节点与关系

- 产品实体：`ent_product_smartsens_sc580xs`
- 零部件实体：`ent_component_smartsens_sc580xs_sensor`
- 制造商实体：`ent_company_smartsens`
- 关键关系：
  - `rel_ent_company_smartsens_manufactures_ent_product_smartsens_sc580xs`（`ent_company_smartsens` → `manufactures` → `ent_product_smartsens_sc580xs`）
  - `rel_ent_company_smartsens_manufactures_ent_component_smartsens_sc580xs_sensor`（`ent_company_smartsens` → `manufactures` → `ent_component_smartsens_sc580xs_sensor`）
  - `ent_product_smartsens_sc580xs` -- `uses` --> `ent_component_smartsens_sc580xs_sensor`

## 应用场景

- **旗舰智能手机主摄、超广角、机器人视觉、工业检测、无人机航拍**

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

- [制造商：思特威 / SmartSens](../../../appendices/appendix-d/companies/company_smartsens.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [思特威官网](https://www.smartsenstech.com)
2. [思特威 SC580XS CMOS 图像传感器产品/资料页](https://www.smartsenstech.com/en/m)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)