---
id: ent_component_csb_self_lubricating_bearing
schema_version: 1
type: component
'title:': 自润滑轴承
domain: 02_components
theoretical_depth: system
names:
  zh: 自润滑轴承
  en: CSB Self-Lubricating Bearing
status: active
sources:
- id: src_csb_self_lubricating_bearing_official
  type: website
  url: https://www.csb.com.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 自润滑轴承 / CSB Self-Lubricating Bearing

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [长盛轴承 / CSB](../../../appendices/appendix-d/companies/company_csb.md) |
| **产品类别** | 轴承 / 自润滑轴承 / 滑动轴承 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [长盛轴承官网](https://www.csb.com.cn) |

## 产品概述

长盛轴承自润滑轴承采用金属-聚合物复合材料，通过烧结工艺在钢背表面复合青铜粉与 PTFE 润滑层，实现免维护、低摩擦、耐磨损的滑动支撑。该产品系列覆盖轴套、衬套、止推垫片及关节轴承等多种形式，可替代传统油脂润滑轴承，特别适用于难以频繁维护或污染环境的场合。

在人形机器人应用中，自润滑轴承可用于关节摆动部位、连杆铰接点及线性执行器导向套，能够降低维护需求并提升整机可靠性。

## 产品图片

> 长盛轴承自润滑轴承：请访问 [官方资料](https://www.csb.com.cn) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 内径范围 | 2–300 mm | 产品手册 |
| 外径范围 | 4–340 mm | 产品手册 |
| 宽度范围 | 3–100 mm | 产品手册 |
| 壁厚 | 0.5–2.5 mm | 产品手册 |
| 最大载荷 | 140 MPa（静载） | 产品手册 |
| 最大 PV 值 | 2.5 MPa·m/s | 产品手册 |
| 摩擦系数 | 0.03–0.25 | 产品手册 |
| 工作温度 | -200 °C – +280 °C | 产品手册 |
| 材质 | 钢背 + 青铜粉 + PTFE | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[长盛轴承 / CSB](../../../appendices/appendix-d/companies/company_csb.md)
- **核心零部件/技术来源**：冷轧钢板、铜粉、PTFE、烧结炉、精密冲压与拉拔模具。
- **下游应用/客户**：汽车 OEM、工程机械、液压件厂商、人形机器人整机厂、自动化设备。

## 知识图谱节点与关系

- 零部件实体：`ent_component_csb_self_lubricating_bearing`
- 制造商实体：`ent_company_csb`
- 关键关系：
  - `rel_ent_company_csb_manufactures_ent_component_csb_self_lubricating_bearing`（`ent_company_csb` --> `manufactures` --> `ent_component_csb_self_lubricating_bearing`）

## 应用场景

- **人形机器人**：关节摆动轴、连杆铰接点、线性执行器导向套、足部铰链。
- **工程机械**：挖掘机、装载机、起重机的铰接与油缸支撑部位。
- **汽车工业**：转向系统、悬挂系统、车门铰链、座椅调节机构。
- **液压与气动**：油缸导向套、气缸支撑套、阀门执行机构。

## 竞争对比

| 对比项 | 本产品 | GGB | Oiles |
|--------|--------|-----|-------|
| 核心优势 | 本土化供应、性价比高、定制化 | 国际精度与可靠性领先 | 材料体系丰富 |
| 交付周期 | 较短 | 较长 | 较长 |
| 服务响应 | 快速 | 中等 | 中等 |
| 价格水平 | 中低端至中高端 | 高端 | 高端 |

## 选购与部署建议

- 选型时应核算实际载荷、速度、温度及环境介质，确保 PV 值在允许范围内。
- 压装时建议使用芯轴或专用工装，避免轴承内孔变形影响配合。
- 在有化学腐蚀或水下工况时，应选用纤维缠绕或不锈钢背衬型号。

## 参考资料

1. [长盛轴承官网](https://www.csb.com.cn)
2. [长盛轴承产品手册](https://www.csb.com.cn/products/)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)