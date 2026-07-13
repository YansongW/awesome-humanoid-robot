---
id: ent_company_gsa
schema_version: 1
type: company
'title:': GSA SA
domain: 02_components
theoretical_depth: system
names:
  zh: GSA
  en: GSA SA
status: active
sources:
- id: src_gsa_official
  type: website
  url: https://www.gsa-sa.ch
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# GSA / GSA SA

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 瑞士 GSA |
| **英文名** | GSA SA |
| **总部** | 瑞士洛桑 |
| **成立时间** | 1982 |
| **官网** | [https://www.gsa-sa.ch](https://www.gsa-sa.ch) |
| **供应链环节** | 行星滚柱丝杠 / 线性执行器 |
| **企业属性** | 国际品牌、私有企业 |
| **母公司/所属集团** | 独立 |
| **数据来源** | 官网、产品手册、公开报道、WAIC 2026 报道 |

## 公司简介

瑞士高精度行星滚柱丝杠与机电执行器供应商，专注高负载、高可靠线性传动。

GSA SA 深耕行星滚柱丝杠及其衍生的电缸、伺服执行器，产品覆盖航天、航空、医疗、机器人、机床及核工业。公司强调从设计、制造到测试的全流程质量控制，可为小批量、高复杂度应用提供定制解决方案。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 行星滚柱丝杠 | 高负载精密丝杠 | GSA 标准/定制系列 | 航空、机器人 |
| 机电执行器 | 集成电机+丝杠 | EMA 系列 | 航空、医疗 |
| 滚珠丝杠 | 标准精密传动 | 未公开型号 | 工业 |
| 定制执行器 | 客户集成方案 | 依定制 | 核工业、国防 |

## 代表产品

### 行星滚柱丝杠 / Planetary Roller Screw

> 行星滚柱丝杠：请访问 [官方资料](https://www.gsa-sa.ch) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 公称直径 | Ø8–Ø150 mm | 产品手册 |
| 导程 | 1–50 mm | 产品手册 |
| 精度等级 | IT1–IT5 / G1–G5 | 产品手册 |
| 额定动载荷 | 最高约 1,200 kN | 产品手册 |
| 最高转速 | 可达 6,000 rpm | 产品手册 |
| 结构 | 行星滚柱循环式 | 产品手册 |
| 材质 | 轴承钢 / 渗碳钢 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：精密螺纹磨削、高动态响应、可集成力/位置传感，满足航空级可靠性。

**应用场景**：人形机器人高负载关节、飞机飞控作动、医疗手术机器人、核工业阀门。

### 机电执行器 / Electromechanical Actuator

> 机电执行器：请访问 [官方资料](https://www.gsa-sa.ch) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 推力范围 | 未公开 | 产品手册 |
| 行程 | 依定制 | 产品手册 |
| 速度 | 未公开 | 产品手册 |
| 反馈 | 编码器 /  resolver 可选 | 产品手册 |
| 防护等级 | 未公开 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：一体化设计，替代液压执行器，提升系统效率与维护性。

**应用场景**：飞机舵面控制、机器人关节、医疗床、工业自动化。

## 供应链位置

- **上游关键零部件/材料**：高端轴承钢、伺服电机、编码器、控制器、润滑脂、精密磨具
- **下游客户/应用场景**：航空航天、医疗设备、机器人 OEM、核工业、机床
- **主要竞争对手/对标**：Rollvis、Moog、SKF、NSK、恒立液压

## 知识图谱节点与关系

- 公司实体：`ent_company_gsa`
- 产品/零部件实体：`ent_component_gsa_roller_screw`, `ent_component_gsa_electromechanical_actuator`
- 关键关系：
  - `ent_company_gsa` -- `manufactures` --> `ent_component_gsa_roller_screw`
  - `ent_company_gsa` -- `manufactures` --> `ent_component_gsa_electromechanical_actuator`

## 参考资料

1. [GSA 官网](https://www.gsa-sa.ch)
2. [GSA 产品手册](https://www.gsa-sa.ch/en/products)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)