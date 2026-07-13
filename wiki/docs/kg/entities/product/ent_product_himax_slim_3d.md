---
id: ent_product_himax_slim_3d
schema_version: 1
type: product
domain: 02_components
theoretical_depth: system
names:
  zh: Himax SLiM 3D 传感模组
  en: Himax SLiM 3D Sensing Module
status: active
sources:
- id: src_ent_product_himax_slim_3d_official
  type: website
  url: https://www.himax.com.tw/products/structured-light-sensing/
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01 00:00:00+00:00
---





# Himax SLiM 3D 传感模组 / Himax SLiM 3D Sensing Module

> 返回：[附录 D.4 重点产品 Wiki 目录](../../../appendices/appendix-d/index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [奇景光电（Himax Technologies） / Himax Technologies](../../../appendices/appendix-d/companies/company_himax.md) |
| **产品类别** | 结构光 3D 传感模组 |
| **发布时间** | 2018 年起商用 |
| **状态** | 量产/商用 |
| **官网/来源** | [Himax SLiM 3D 传感模组 产品/资料页](https://www.himax.com.tw/products/structured-light-sensing/) |

## 产品概述

SLiM（Structured Light Module）是奇景光电推出的结构光 3D 传感整体解决方案，集成红外投射器、WLO 光学元件与接收传感器，可实现高精度、低功耗的 3D 深度感知。其小型化设计使其不仅适用于手机人脸解锁，也适合机器人近距离避障、手势识别与物体抓取导引。

## 产品图片

> Himax SLiM 3D 传感模组：请访问 [官方资料](https://www.himax.com.tw/products/structured-light-sensing/) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 结构光 3D 传感模组 | 官网/新闻稿 |
| 深度技术 | 结构光 / 主动红外投射 | 官网/新闻稿 |
| 深度分辨率 | VGA 级（640 × 480）@ 30 fps | 官网/新闻稿 |
| 视场角 | 水平约 67°（典型） | 官网/新闻稿 |
| 工作距离 | 约 0.3 m – 1.0 m | 官网/新闻稿 |
| 深度精度 | 未公开 | - |
| 尺寸 | 小型化模组（具体未公开） | 官网/新闻稿 |
| 功耗 | 未公开 | - |
| 接口 | MIPI / USB2.0（因方案而异） | 官网/新闻稿 |
| 发射器 | VCSEL / EEL + WLO DOE | 官网/新闻稿 |
| 接收器 | NIR 增强 CMOS / ToF | 官网/新闻稿 |
| 工作温度 | 未公开 | - |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[奇景光电（Himax Technologies） / Himax Technologies](../../../appendices/appendix-d/companies/company_himax.md)
- **核心零部件/技术来源**：自研 WLO 衍射光学元件、红外投射器、NIR CMOS 接收器、深度算法 ASIC、模组封装。
- **下游应用/客户**：智能手机 OEM、机器人整机厂、AR/VR 设备商、智能门锁/门禁厂商、支付终端厂商。

## 知识图谱节点与关系

- 产品实体：`ent_product_himax_slim_3d`
- 零部件实体：`ent_component_himax_slim_3d_module`
- 制造商实体：`ent_company_himax`
- 关键关系：
  - `rel_ent_company_himax_manufactures_ent_product_himax_slim_3d`（`ent_company_himax` → `manufactures` → `ent_product_himax_slim_3d`）
  - `rel_ent_company_himax_manufactures_ent_component_himax_slim_3d_module`（`ent_company_himax` → `manufactures` → `ent_component_himax_slim_3d_module`）
  - `rel_ent_product_himax_slim_3d_uses_ent_component_himax_slim_3d_module`（`ent_product_himax_slim_3d` → `uses` → `ent_component_himax_slim_3d_module`）

## 应用场景

- **机器人避障与抓取**：近距离高精度深度图辅助机械臂路径规划。
- **人脸识别与支付**：结构光活体检测提升安全等级。
- **AR/VR 手势**：低延迟手部追踪与交互。
- **3D 扫描**：小型化模组用于手持或固定式三维重建。

## 竞争对比

| 对比项 | 本产品 | 主要竞品 A | 主要竞品 B |
|--------|--------|------------|------------|
| 类型 | 结构光 3D 模组 | 奥比中光 Gemini 335 | Intel RealSense D435i |
| 深度技术 | 结构光 | 主动+被动双目 | 主动红外立体 |
| 最佳距离 | 0.3–1.0 m | 0.1–20 m+ | 0.3–10 m |
| 核心优势 | WLO 小型化、支付级安全 | 户外强光、MX6800 ASIC | 生态成熟、ROS 支持 |

## 选购与部署建议

- 根据目标应用的分辨率、量程、精度或算力需求选择具体型号。
- 部署前确认接口、供电、散热、机械安装与环境温度范围匹配。
- 建议通过官方渠道或授权代理商获取最新固件、SDK 与技术支持。

## 相关词条

- [制造商：奇景光电（Himax Technologies） / Himax Technologies](../../../appendices/appendix-d/companies/company_himax.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [Himax Technologies 官网](https://www.himax.com.tw)
2. [Himax SLiM 3D 传感模组 产品/资料页](https://www.himax.com.tw/products/structured-light-sensing/)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)