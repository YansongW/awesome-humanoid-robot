# SRT SFG 柔性夹爪 / SRT SFG Soft Gripper

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [软体机器人科技 / SRT](../companies/company_srt.md) |
| **产品类别** | 气动柔性夹爪 / 软体机器人末端执行器 |
| **发布时间** | 2018 年起持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [SRT 官网](https://www.softrobottech.com) |

## 产品概述

SRT SFG 柔性夹爪是一款基于软体机器人技术的自适应气动末端执行器。与传统刚性夹爪不同，SFG 的手指由食品级硅胶制成，内部具有仿生气囊结构：通入正压时手指弯曲并自适应包覆目标物体；通入负压时手指张开释放物体。由于其柔软且可变形的特性，SFG 能够用同一套夹爪抓取不同尺寸、形状、硬度和表面特征的物体，特别适用于传统夹爪难以处理的柔性、异形和易损物品。

SFG 系列已发展出紧凑型（FTN）、对称可调型（FMA）、圆周型（FNC）等多种结构形式，并可根据客户需求定制手指模块与安装支架，兼容 UR、ABB、新松等主流机器人。

## 产品图片

> SRT SFG Gripper：请访问 [官方资料](https://www.softrobottech.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 驱动方式 | 气动（正压抓取 / 负压释放） | 产品手册 |
| 手指材料 | 食品级硅胶 | 产品手册 |
| 手指结构 | 仿生气囊/软体结构 | 产品手册 |
| 工作温度 | -40 ℃ – 150 ℃ | 产品手册 |
| 工作压力 | -100 – 100 kPa | 产品手册 |
| 使用寿命 | >300 万次循环 | 产品手册 |
| 重复定位精度 | 0.08 mm | 产品手册 |
| 工作频率 | ≤110 CPM | 产品手册 |
| 负载范围 | 100 g – 7 kg（因型号而异） | DirectIndustry |
| 夹爪重量 | 38 g – 1090 g（因型号而异） | DirectIndustry |
| 适用工件尺寸 | 随型号变化，可覆盖多种 SKU | 产品手册 |
| 驱动介质 | 洁净空气 | 产品手册 |
| 安装接口 | 兼容 ISO 9409-1:2004 / GB/T 14468.1 | 产品手册 |
| 配套控制器 | SCB 系列气动控制器 | 产品手册 |
| 认证 | CE、RoHS、FDA、LFGB、JFSL370 等 | 官网公开资料 |
| 通信接口 | 气动控制器 + 机器人 I/O | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[软体机器人科技 / SRT](../companies/company_srt.md)
- **核心零部件/技术来源**：自研硅胶材料配方、软体结构设计与成型工艺；气动元件、控制器、3D 视觉模组外购。
- **下游应用/客户**：食品生鲜、3C 电子、汽车零部件、医疗日化、物流仓储、协作机器人集成商。

## 知识图谱节点与关系

- 产品实体：`ent_product_srt_soft_gripper`
- 制造商实体：`ent_company_srt`
- 零部件实体：`ent_component_srt_flexible_finger`
- 关键关系：
  - `rel_ent_company_srt_manufactures_ent_product_srt_soft_gripper`（`ent_company_srt` → `manufactures` --> `ent_product_srt_soft_gripper`）
  - `rel_ent_company_srt_manufactures_ent_component_srt_flexible_finger`（`ent_company_srt` → `manufactures` --> `ent_component_srt_flexible_finger`）
  - `rel_ent_product_srt_soft_gripper_uses_ent_component_srt_flexible_finger`（`ent_product_srt_soft_gripper` → `uses` --> `ent_component_srt_flexible_finger`）

## 应用场景

- **食品生鲜**：肉类、果蔬、烘焙、海鲜、预制菜的分拣与包装。
- **3C 电子**：手机边框、电路板、异形电子元件的无损上下料。
- **汽车零部件**：橡胶件、线束、异形注塑件装配。
- **医疗日化**：安瓿瓶、注射器、医疗器械、化妆品包装。
- **物流仓储**：异形、柔软、易碎物品的混合 SKU 分拣。

## 竞争对比

| 对比项 | SRT SFG | OnRobot Soft Gripper | Soft Robotics Inc. mGrip |
|--------|---------|----------------------|--------------------------|
| 驱动方式 | 气动 | 电动/气动 | 气动 |
| 手指材料 | 食品级硅胶 | 柔性材料 | 柔性材料 |
| 工作温度 | -40 ℃ – 150 ℃ | 视型号而定 | 视型号而定 |
| 使用寿命 | >300 万次 | 视型号而定 | 视型号而定 |
| 核心优势 | 食品级认证、多系列、全球客户多 | 即插即用生态 | 模块化、易集成 |

## 选购与部署建议

- 根据工件重量、尺寸、形状选择 FTN/FMA/FNC 等对应系列与手指模块。
- 需配套洁净气源与 SRT 气动控制器，确保压力与节拍匹配。
- 对于食品直接接触场景，建议选用 SFG-N 食品级认证型号。

## 参考资料

1. [SRT 软体机器人官网](https://www.softrobottech.com)
2. [SRT Shopify 国际站](https://softrobotgripper.com)
3. [Asian Robotics Review – SRT 报道](https://asianroboticsreview.com/home620-html)
4. [DirectIndustry – SFG 系列产品参数](https://www.directindustry.com/prod/soft-robot-tech-co-ltd/product-244815-2538729.html)
5. [附录 D 企业目录](../index-companies.md)