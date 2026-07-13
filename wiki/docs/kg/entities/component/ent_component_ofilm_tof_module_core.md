---
id: ent_component_ofilm_tof_module_core
type: component
'title:': OFILM 3D ToF Depth Camera Module Core Component
domain: 02_components
theoretical_depth: system
aliases:
- 欧菲光 3D ToF 深度相机模组 核心零部件
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-09 00:00:00+00:00
sources:
- id: ent_component_ofilm_tof_module_core_official
  type: website
  url: http://www.ofilm.com/en/products_inner1_39.html
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-09 00:00:00+00:00
  review_notes: Specifications from official datasheets and public reports; missing
    values marked as 未公开.
---





# ofilm_tof_module_core

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [欧菲光 / OFILM](../../../appendices/appendix-d/companies/company_ofilm.md) |
| **产品类别** | 飞行时间 3D 深度相机模组 |
| **发布时间** | 持续在售/迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [欧菲光 3D ToF 深度相机模组产品/资料页](http://www.ofilm.com/en/products_inner1_39.html) |

## 产品概述

欧菲光 3D ToF 深度相机模组基于飞行时间（Time-of-Flight）原理，通过 940 nm VCSEL 发射调制红外光并接收反射光，实时输出深度图与点云。模组可集成 RGB 摄像头实现 RGB-D 对齐，广泛用于扫地机器人避障、服务机器人导航、AR/VR 手势交互与人脸识别。

## 产品图片

> 欧菲光 3D ToF 深度相机模组：请访问 [官方资料](http://www.ofilm.com/en/products_inner1_39.html) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 飞行时间 3D 深度相机模组 | 欧菲光官网 |
| 深度分辨率 | VGA / QVGA（因型号而异） | 欧菲光官网 |
| RGB 分辨率 | 可选配 2MP / 5MP | 欧菲光官网 |
| 光源 | 940 nm VCSEL | 欧菲光官网 |
| 视场角 | 60°×45° / 70°×54°（典型） | 欧菲光官网 |
| 测距范围 | 0.3 – 5 m | 欧菲光官网 |
| 精度 | 约 1% @ 1 m | 欧菲光官网 |
| 帧率 | 最高 30 fps | 欧菲光官网 |
| 接口 | MIPI / USB2.0 | 欧菲光官网 |
| 供电 | 3.3 V / 5 V DC | 欧菲光官网 |
| 工作温度 | -20℃ – +70℃ | 欧菲光官网 |
| 重量 | 未公开 | - |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[欧菲光 / OFILM](../../../appendices/appendix-d/companies/company_ofilm.md)
- **核心零部件/技术来源**：VCSEL、ToF 图像传感器、DOE/光学镜头、ISP、PCB/FPC、结构件
- **下游应用/客户**：智能手机、智能机器人、AR/VR、智能家居、汽车电子

## 知识图谱节点与关系

- 产品实体：`ent_product_ofilm_tof_3d_module`
- 零部件实体：`ent_component_ofilm_tof_module_core`
- 制造商实体：`ent_company_ofilm`
- 关键关系：
  - `rel_ent_company_ofilm_manufactures_ent_product_ofilm_tof_3d_module`（`ent_company_ofilm` → `manufactures` → `ent_product_ofilm_tof_3d_module`）
  - `rel_ent_company_ofilm_manufactures_ent_component_ofilm_tof_module_core`（`ent_company_ofilm` → `manufactures` → `ent_component_ofilm_tof_module_core`）
  - `ent_product_ofilm_tof_3d_module` -- `uses` --> `ent_component_ofilm_tof_module_core`

## 应用场景

- **扫地机器人避障、服务机器人导航、AR/VR 手势、人脸/生物识别、工业 3D 检测**

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

- [制造商：欧菲光 / OFILM](../../../appendices/appendix-d/companies/company_ofilm.md)
- [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)

## 参考资料

1. [欧菲光官网](http://www.ofilm.com)
2. [欧菲光 3D ToF 深度相机模组产品/资料页](http://www.ofilm.com/en/products_inner1_39.html)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)