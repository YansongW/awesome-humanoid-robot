---
id: ent_company_kollmorgen
schema_version: 1
type: company
title: Kollmorgen
domain: 02_components
theoretical_depth: system
names:
  zh: Kollmorgen
  en: Kollmorgen
status: active
sources:
  - id: src_kollmorgen_official
    type: website
    title: Kollmorgen Official Website
    url: https://www.kollmorgen.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Kollmorgen / Kollmorgen

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Kollmorgen |
| **英文名** | Kollmorgen |
| **总部** | 美国 Radford, Virginia |
| **成立时间** | 1916 |
| **官网** | [https://www.kollmorgen.com](https://www.kollmorgen.com) |
| **供应链环节** | 伺服电机 / 无框力矩电机 / 运动控制 |
| **企业属性** | 外资品牌、Regal Rexnord 旗下 |
| **母公司/所属集团** | Regal Rexnord |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

## 公司简介

全球运动控制领域领导品牌，TBM/KBM 无框力矩电机广泛用于机器人关节和精密转台。

Kollmorgen 提供无框力矩电机、伺服电机、驱动器和运动控制器。TBM2G 系列专为协作机器人和人形机器人关节设计，具有低齿槽、高扭矩密度和 48 V 以下低压运行能力。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| TBM2G 无框电机 | 下一代机器人关节电机 | TBM2G-050 / TBM2G-115 | 协作/人形机器人关节 |
| AKM 伺服电机 | 高性能伺服电机 | AKM24 / AKM32 | 工业自动化、CNC |

## 代表产品

### TBM2G-050 无框电机 / TBM2G-050 Frameless Motor

> TBM2G-050 无框电机：请访问 [官方资料](https://www.kollmorgen.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 外径 | 50 mm | Kollmorgen / INMOCO |
| 重量 | 未公开 | - |
| 连续扭矩 | 0.27 N·m | INMOCO 2022 |
| 额定转速 | 8000 rpm | INMOCO 2022 |
| 输出功率 | 0.205 kW | INMOCO 2022 |
| 电压 | ≤ 48 VDC | Kollmorgen |
| 反馈 | 可选集成 Hall 传感器 | Kollmorgen |
| 电机常数 | 0.061 N·m/√W | INMOCO 2022 |

**技术亮点**：专为 3–15 kg 协作机器人设计，低齿槽、高响应，适配谐波减速器尺寸。

**应用场景**：协作机器人关节、人形机器人小臂/腕部、精密转台。

### TBM2G-115 无框电机 / TBM2G-115 Frameless Motor

> TBM2G-115 无框电机：请访问 [官方资料](https://www.kollmorgen.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 外径 | 115 mm | Kollmorgen / INMOCO |
| 重量 | 未公开 | - |
| 连续扭矩 | 6.03 N·m | INMOCO 2022 |
| 额定转速 | 3100 rpm | INMOCO 2022 |
| 输出功率 | 1.43 kW | INMOCO 2022 |
| 电压 | ≤ 48 VDC | Kollmorgen |
| 反馈 | 可选集成 Hall 传感器 | Kollmorgen |
| 电机常数 | 0.802 N·m/√W | INMOCO 2022 |

**技术亮点**：大扭矩无框电机，可直接嵌入机器人肩部/髋部关节，支持高负载动态运动。

**应用场景**：工业机器人大关节、人形机器人腰/髋部、重载协作机器人。

## 供应链位置

- **上游关键零部件/材料**：稀土磁体、硅钢片、铜线、绝缘材料、轴承
- **下游客户/应用场景**：协作机器人、人形机器人、航空航天、医疗设备 OEM
- **主要竞争对手/对标**：Maxon、汇川技术、禾川科技、Parker

## 知识图谱节点与关系

- 公司实体：`ent_company_kollmorgen`
- 产品实体：`ent_component_kollmorgen_tbm2g_050`、`ent_component_kollmorgen_tbm2g_115`
- 关键关系：
  - `ent_company_kollmorgen` -- `manufactures` --> `ent_component_kollmorgen_tbm2g_050`
  - `ent_company_kollmorgen` -- `manufactures` --> `ent_component_kollmorgen_tbm2g_115`

## 参考资料

1. [官网](https://www.kollmorgen.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）