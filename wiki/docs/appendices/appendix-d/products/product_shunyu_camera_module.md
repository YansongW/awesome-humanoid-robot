# 舜宇光学车载/机器人摄像头模组 / Sunny Optical Automotive / Robot Camera Module

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [舜宇光学 / Sunny Optical](../companies/company_shunyu.md) |
| **产品类别** | 车规级摄像头模组 |
| **发布时间** | 持续在售/迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [舜宇光学车载/机器人摄像头模组产品/资料页](https://www.sunnyoptical.com/en/pro/009017006/index.html) |

## 产品概述

舜宇光学车载/机器人摄像头模组面向 ADAS、智能座舱及具身智能机器人视觉场景，集成自研玻塑混合镜头、CMOS 图像传感器与 ISP 调优，具备高可靠性、宽温域与 IP67/IP69K 防护等级。模组支持 GMSL2/FPD-Link III 等高速串行接口，可输出高清图像用于目标检测、车道线识别、SLAM 与手眼协调。

## 产品图片

> 舜宇光学车载/机器人摄像头模组：请访问 [官方资料](https://www.sunnyoptical.com/en/pro/009017006/index.html) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 车规级摄像头模组 | 官方产品资料 |
| 分辨率 | 2MP / 3MP / 8MP 多型号 | 官方产品资料 |
| 传感器 | 1/2.7" – 1/2.3" CMOS | 官方产品资料 |
| 视场角 | 30° – 120°（因型号而异） | 官方产品资料 |
| 镜头 | 玻塑混合高解析力镜头 | 官方产品资料 |
| 接口 | GMSL2 / FPD-Link III / 同轴 | 官方产品资料 |
| 帧率 | 最高 60 fps（因分辨率与接口而异） | 官方产品资料 |
| 防护等级 | IP67 / IP69K | 官方产品资料 |
| 工作温度 | -40℃ – +85℃ | 官方产品资料 |
| 供电 | 12 V DC（典型） | 官方产品资料 |
| 重量 | 约 50 – 150 g | 官方产品资料 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[舜宇光学 / Sunny Optical](../companies/company_shunyu.md)
- **核心零部件/技术来源**：CMOS 图像传感器、光学镜片、音圈马达、FPC/PCB、ISP 芯片、结构件
- **下游应用/客户**：智能手机 OEM、汽车 OEM/Tier1、机器人整机厂、AR/VR 厂商

## 知识图谱节点与关系

- 产品实体：`ent_product_shunyu_automotive_camera_module`
- 零部件实体：`ent_component_shunyu_camera_module_core`
- 制造商实体：`ent_company_shunyu`
- 关键关系：
  - `rel_ent_company_shunyu_manufactures_ent_product_shunyu_automotive_camera_module`（`ent_company_shunyu` → `manufactures` → `ent_product_shunyu_automotive_camera_module`）
  - `rel_ent_company_shunyu_manufactures_ent_component_shunyu_camera_module_core`（`ent_company_shunyu` → `manufactures` → `ent_component_shunyu_camera_module_core`）
  - `ent_product_shunyu_automotive_camera_module` -- `uses` --> `ent_component_shunyu_camera_module_core`

## 应用场景

- **人形机器人/服务机器人视觉导引、自动驾驶感知、智能座舱 DMS/OMS、工业检测**

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

- [制造商：舜宇光学 / Sunny Optical](../companies/company_shunyu.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [舜宇光学官网](https://www.sunnyoptical.com)
2. [舜宇光学车载/机器人摄像头模组产品/资料页](https://www.sunnyoptical.com/en/pro/009017006/index.html)
3. 产品 datasheet 与公开技术报道
4. [附录 D 企业目录](../index-companies.md)