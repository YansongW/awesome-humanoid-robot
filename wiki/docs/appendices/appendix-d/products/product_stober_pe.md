# STOBER PE 系列经济型行星减速器 / STOBER PE Series Planetary Gearbox

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [STOBER（斯多博） / STOBER](../companies/company_stober.md) |
| **产品类别** | 经济型行星减速器 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [STOBER（斯多博） 官网](https://www.stober.com) |

## 产品概述

STOBER PE 系列是面向成本敏感型伺服应用的经济型行星减速器，采用 helical 行星齿轮和集成电机适配器（MAI），提供 3:1–100:1 减速比和最高 160 N·m 额定扭矩。该系列提供 PE21、PE31、PE41、PE51 四种尺寸，背隙 <8 arcmin，效率单级 97%、双级 95%。

PE 系列防护等级 IP64，采用终身润滑，输入转速最高 8,000 rpm，适用于中小型机器人关节、自动化装置、包装和医疗设备。

## 产品图片

> STOBER PE 系列经济型行星减速器 / STOBER PE Series Planetary Gearbox：请访问 [官方资料](https://www.stober.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 减速比 | 3:1 – 100:1 | 产品手册 |
| 框号尺寸 | PE21 / PE31 / PE41 / PE51 | 产品手册 |
| 额定输出扭矩 | 最高 160 N·m | 产品手册 |
| 加速扭矩 | 最高 310 N·m | 产品手册 |
| 背隙 | <8 arcmin | 产品手册 |
| 效率 | 1 级 97% / 2 级 95% | 产品手册 |
| 最大输入转速 | 最高 8,000 rpm | 产品手册 |
| 防护等级 | IP64 | - |

## 供应链位置

- **制造商**：[STOBER（斯多博） / STOBER](../companies/company_stober.md)
- **核心零部件/技术来源**：螺旋行星齿轮、轴承、密封件、润滑脂、电机适配法兰、铝制箱体
- **下游应用/客户**：中小型机器人、自动化设备、包装、医疗、半导体

## 知识图谱节点与关系

- 零部件实体：`ent_component_stober_pe`
- 制造商实体：`ent_company_stober`
- 关键关系：
  - `rel_ent_company_stober_manufactures_ent_component_stober_pe`（`ent_company_stober` --> `manufactures` --> `ent_component_stober_pe`）

## 应用场景

- **工业机器人**：小型工业机器人关节、转台
- **人形机器人**：手指/腕部等小扭矩关节或执行器
- **数控机床**：小型 CNC、检测平台
- **其他自动化**：包装、医疗、半导体搬运

## 竞争对比

| 对比项 | PE 系列行星减速器 | Neugart PLE | Apex Dynamics PA II |
|--------|------------------------|---------------|---------------|
| 核心优势 | 经济型 helical、快速交付 | 经济型直齿、品牌口碑 | 经济型 helical、性价比 |
| 背隙/精度 | <8 arcmin | 经济型 <8 arcmin | 6–12 arcmin |
| 价格水平 | 中端 | 中端 | 中端 |
| 交付周期 | 较短 | 中等 | 较短 |

## 选购与部署建议

适用于对背隙要求不高的中低扭矩伺服轴；高速应用需校核临界转速与轴承寿命。

## 参考资料

1. [STOBER（斯多博） 官网](https://www.stober.com)
2. [STOBER PE Series Inline Planetary Gearbox](https://www.stober.com)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)