---
id: ent_component_rollvis_roller_screw
schema_version: 1
type: component
'title:': Rollvis 行星滚柱丝杠
domain: 02_components
theoretical_depth: system
names:
  zh: Rollvis 行星滚柱丝杠
  en: Rollvis Planetary Roller Screw
status: active
sources:
- id: src_rollvis_roller_screw_official
  type: website
  url: https://www.rollvis.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# Rollvis 行星滚柱丝杠 / Rollvis Planetary Roller Screw

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [Rollvis SA](../../../appendices/appendix-d/companies/company_rollvis.md) |
| **产品类别** | 精密传动 / 行星滚柱丝杠 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [Rollvis 官网](https://www.rollvis.com) |

## 产品概述

Rollvis 行星滚柱丝杠是全球高负载线性传动领域的标杆产品，广泛应用于航空航天、机床、医疗、注塑及人形机器人。R 系列采用行星滚柱循环结构，在同等体积下提供远高于滚珠丝杠的承载能力与使用寿命，是人形机器人高负载关节的重要进口选项。

Rollvis 于 2022 年被 Nidec-Shimpo 收购，进一步强化了其在精密传动领域的供应链能力。

## 产品图片

> Rollvis 行星滚柱丝杠：请访问 [官方资料](https://www.rollvis.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 公称直径 | Ø8–Ø240 mm | 产品手册 |
| 导程 | 1–60 mm | 产品手册 |
| 精度等级 | G1–G9（Rollvis 内部等级） | 产品手册 |
| 额定动载荷 | 最高约 1,500 kN | 产品手册 |
| 最高转速 | 可达 5,000 rpm | 产品手册 |
| 结构 | 行星滚柱循环式 | 产品手册 |
| 材质 | 轴承钢 / 表面硬化钢 | 产品手册 |
| 润滑 | 润滑脂 / 油润滑 | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[Rollvis SA](../../../appendices/appendix-d/companies/company_rollvis.md)
- **核心零部件/技术来源**：高品质轴承钢、精密螺纹磨削、表面硬化处理、润滑技术。
- **下游应用/客户**：航空航天、机床、医疗设备、机器人 OEM、国防。

## 知识图谱节点与关系

- 零部件实体：`ent_component_rollvis_roller_screw`
- 制造商实体：`ent_company_rollvis`
- 关键关系：
  - `rel_ent_company_rollvis_manufactures_ent_component_rollvis_roller_screw`（`ent_company_rollvis` --> `manufactures` --> `ent_component_rollvis_roller_screw`）

## 应用场景

- **人形机器人**：髋、膝、踝等高负载线性关节。
- **航空航天**：飞机舵面、起落架、舱门电作动器。
- **机床**：重切削进给轴、大型龙门进给。
- **注塑与压铸**：合模机构、顶出机构。

## 竞争对比

| 对比项 | Rollvis 行星滚柱丝杠 | GSA | 秦川机床 |
|--------|----------------------|-----|----------|
| 核心优势 | 承载能力、品牌、航空级经验 | 定制化、机电执行器集成 | 国产替代、性价比 |
| 交付周期 | 较长 | 较长 | 较短 |
| 服务响应 | 中等 | 中等 | 快速 |
| 价格水平 | 高端 | 高端 | 中端 |

## 选购与部署建议

- 高负载应用需明确动态载荷、转速、加速度和寿命要求，建议联系厂商进行定制化设计。
- 安装时需保证丝杠与负载的同轴度，润滑方式与维护周期直接影响寿命。

## 参考资料

1. [Rollvis 官网](https://www.rollvis.com)
2. [Nidec-Shimpo 收购公告](https://www.nidec.com)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)