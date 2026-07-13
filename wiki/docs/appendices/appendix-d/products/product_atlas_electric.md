# Boston Dynamics Atlas（电动版）

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Boston Dynamics](../companies/company_boston_dynamics.md) |
| **产品类别** | 工业级人形机器人 |
| **发布时间** | 2024 年 4 月发布电动版；2026 年进入早期量产 |
| **状态** | 早期量产/企业内测 |
| **官网/来源** | [Boston Dynamics Atlas](https://bostondynamics.com/products/atlas/) |

## 产品概述

Boston Dynamics 于 2024 年 4 月宣布退役液压驱动的经典 Atlas，并推出全电动版 Atlas。新 Atlas 采用定制高功率电驱执行器，髋关节、腰部与颈部支持 360° 连续旋转，整机具备 56 个自由度，承载能力与运动范围均处于行业前列。

电动版 Atlas 定位于重载工业任务，包括物料搬运、设备操作与汽车制造流程。其电池支持自主热插拔，结合 Boston Dynamics Orbit  fleet 管理平台，可实现接近连续作业。首批部署预计集中于现代汽车集团（Hyundai）制造基地与 Google DeepMind 研究场景。

## 产品图片

> Boston Dynamics Atlas Electric：请访问 [官方资料](https://bostondynamics.com/products/atlas/) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 190 cm（高） | 官方规格页 |
| 重量 | 约 90 kg | 官方规格页 |
| 自由度（整机） | 56 DOF | 官方规格页 |
| 关键性能指标 | 瞬时负载 50 kg；持续负载 30 kg；最大臂展 2.3 m | 官方规格页 |
| 行走速度 | 约 9 km/h | 第三方评测 |
| 续航 | 约 4 小时（典型任务） | 官方规格页 |
| 防护等级 | IP67 | 官方规格页 |
| 工作温度 | -20°C 至 40°C | 官方规格页 |
| 价格 | 未公开（行业估计约 150,000 USD） | 第三方估计 |

## 供应链位置

- **制造商**：[Boston Dynamics](../companies/company_boston_dynamics.md)
- **核心零部件/技术来源**：定制电驱执行器、多摄像头 360° 视觉、自研实时控制栈与 Orbit 软件平台；Hyundai 集团提供制造与供应链支持。
- **下游应用/客户**：Hyundai 汽车制造、Google DeepMind 研究、重载工业场景。

## 知识图谱节点与关系

- 产品实体：`ent_product_boston_dynamics_atlas_electric`
- 制造商实体：`ent_company_boston_dynamics`
- 关键关系：
  - `rel_ent_company_boston_dynamics_manufactures_ent_product_boston_dynamics_atlas_electric`（`ent_company_boston_dynamics` → `manufactures` → `ent_product_boston_dynamics_atlas_electric`）

## 应用场景

- **汽车制造**：现代汽车集团工厂中的 heavy material handling、部件搬运与复杂装配。
- **重载工业**：替代人工完成超过 30 kg 的重复搬运、设备维护与高危区域作业。
- **研究与开发**：Google DeepMind 等机构用于机器人学习与动态运动控制算法验证。

## 竞争对比

| 对比项 | Boston Dynamics Atlas（电动版） | Tesla Optimus Gen 3 | Agility Digit |
|--------|----------------------------------|---------------------|---------------|
| 定位 | 重载工业人形 | 通用/工业人形 | 物流仓储人形 |
| 整机 DOF | 56 | 28+ 躯干 + 22×2 手 | 16–28 |
| 负载 | 50 kg 瞬时 / 30 kg 持续 | 约 20 kg | 16 kg |
| 核心优势 | 运动能力、负载、360° 关节 | 成本目标、AI 数据闭环 | 商业部署成熟度 |

## 选购与部署建议

- 当前 Atlas 电动版主要面向企业试点与现代汽车集团生态客户，建议通过 Boston Dynamics 商务渠道咨询。
- 部署前需评估场地承重、人机协作安全方案以及与 MES/WMS 的集成需求。

## 参考资料

1. [Boston Dynamics Atlas 官方产品页](https://bostondynamics.com/products/atlas/)
2. [Boston Dynamics Blog – Electric Atlas Reveal](https://bostondynamics.com/)
3. [Robozaps – Boston Dynamics Atlas Review](https://blog.robozaps.com/b/boston-dynamics-atlas-review)
4. [Humanoid.Guide – Atlas](https://humanoid.guide/product/atlas/)