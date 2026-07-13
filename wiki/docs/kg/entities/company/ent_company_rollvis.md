---
id: ent_company_rollvis
schema_version: 1
type: company
'title:': Rollvis SA
domain: 02_components
theoretical_depth: system
names:
  zh: Rollvis
  en: Rollvis SA
status: active
sources:
- id: src_rollvis_official
  type: website
  url: https://www.rollvis.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# Rollvis / Rollvis SA

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 瑞士 Rollvis |
| **英文名** | Rollvis SA |
| **总部** | 瑞士日内瓦 |
| **成立时间** | 1975 |
| **官网** | [https://www.rollvis.com](https://www.rollvis.com) |
| **供应链环节** | 行星滚柱丝杠 / 精密线性传动 |
| **企业属性** | 国际品牌、私有企业 |
| **母公司/所属集团** | 独立（2022 年被 Nidec 集团旗下 Nidec-Shimpo 收购） |
| **数据来源** | 官网、产品手册、公开报道、WAIC 2026 报道 |

## 公司简介

全球领先的行星滚柱丝杠专业制造商，以高承载、高精度和长寿命著称。

Rollvis SA 长期专注于行星滚柱丝杠（Planetary Roller Screw）研发与制造，产品广泛应用于航空航天、机床、医疗、注塑、机器人与国防装备。其 R 系列行星滚柱丝杠以高转速、高加速度和紧凑结构闻名，是人形机器人高负载线性关节的核心进口件来源之一。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 行星滚柱丝杠 | 标准/定制高负载丝杠 | R 系列 | 航空、机床、机器人 |
| 卫星滚柱丝杠 | 高速精密传动 | SAT 系列 | 医疗、半导体 |
| 循环滚柱丝杠 | 高刚性、长导程 | RV 系列 | 注塑、压铸 |
| 定制丝杠 | 客户特殊设计 | 依定制 | 国防、航天 |

## 代表产品

### 行星滚柱丝杠 / Planetary Roller Screw

> 行星滚柱丝杠：请访问 [官方资料](https://www.rollvis.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 公称直径 | Ø8–Ø240 mm | 产品手册 |
| 导程 | 1–60 mm | 产品手册 |
| 精度等级 | G1–G9（Rollvis 内部等级） | 产品手册 |
| 额定动载荷 | 最高约 1,500 kN | 产品手册 |
| 最高转速 | 可达 5,000 rpm | 产品手册 |
| 结构 | 行星滚柱循环式 | 产品手册 |
| 材质 | 轴承钢 / 表面硬化钢 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：高承载密度、长寿命、可承受高加速度，适合极限工况。

**应用场景**：人形机器人下肢线性关节、飞机伺服作动、机床进给轴、注塑机。

### 卫星滚柱丝杠 / Satellite Roller Screw

> 卫星滚柱丝杠：请访问 [官方资料](https://www.rollvis.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 公称直径 | 未公开 | 产品手册 |
| 导程 | 未公开 | 产品手册 |
| 精度等级 | 未公开 | 产品手册 |
| 结构 | 卫星滚柱非循环式 | 产品手册 |
| 特点 | 高转速、低振动 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：适用于高速往复运动， medical 与半导体设备常见选型。

**应用场景**：手术机器人、半导体设备、精密定位平台。

## 供应链位置

- **上游关键零部件/材料**：高品质轴承钢、表面硬化钢材、润滑脂、磨削砂轮、热处理服务
- **下游客户/应用场景**：航空航天、机床、医疗、机器人 OEM、国防
- **主要竞争对手/对标**：GSA、SKF、NSK、THK、秦川机床、恒立液压

## 知识图谱节点与关系

- 公司实体：`ent_company_rollvis`
- 产品/零部件实体：`ent_component_rollvis_roller_screw`, `ent_component_rollvis_satellite_roller_screw`
- 关键关系：
  - `ent_company_rollvis` -- `manufactures` --> `ent_component_rollvis_roller_screw`
  - `ent_company_rollvis` -- `manufactures` --> `ent_component_rollvis_satellite_roller_screw`

## 参考资料

1. [Rollvis 官网](https://www.rollvis.com)
2. [Nidec-Shimpo 收购公告](https://www.nidec.com)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)