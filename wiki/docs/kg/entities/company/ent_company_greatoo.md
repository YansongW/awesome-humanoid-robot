---
id: ent_company_greatoo
schema_version: 1
type: company
'title:': Greatoo Intelligent Equipment
domain: 02_components
theoretical_depth: system
names:
  zh: 巨轮智能
  en: Greatoo Intelligent Equipment
status: active
sources:
- id: src_greatoo_official
  type: website
  url: http://www.greatoo.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 巨轮智能 / Greatoo Intelligent Equipment

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 巨轮智能 |
| **英文名** | Greatoo Intelligent Equipment |
| **总部** | 中国揭阳 |
| **成立时间** | 2001 |
| **官网** | [http://www.greatoo.com](http://www.greatoo.com) |
| **供应链环节** | RV 减速器 / 轮胎模具 / 工业机器人 / 精密机械 |
| **企业属性** | 上市公司（SZ.002031）、国内品牌 |
| **母公司/所属集团** | 巨轮智能装备股份有限公司 |
| **数据来源** | 官网、年报、产品手册、WAIC 2026 报道 |

## 公司简介

国内 RV 减速器重要供应商，由轮胎模具向机器人核心零部件延伸。

巨轮智能起家于轮胎模具与液压硫化机，后切入工业机器人与精密减速器领域。公司自主研发的 RV 减速器已实现批量应用，并逐步向人形机器人关节模组拓展，目标是实现减速器、电机与驱动的国产化替代。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| RV 减速器 | 重载机器人关节 | JR 系列 | 工业机器人、人形机器人 |
| 轮胎模具 | 子午线轮胎模具 | 活络模、两半模 | 轮胎制造 |
| 工业机器人 | 六轴/SCARA | GR 系列 | 搬运、打磨 |

## 代表产品

### RV 减速器 / Greatoo RV Reducer

> RV 减速器：请访问 [官方资料](http://www.greatoo.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 外径 110–400 mm（系列范围） | 产品手册 |
| 重量 | 2–60 kg | 产品手册 |
| 减速比 | 30–200:1 | 产品手册 |
| 额定扭矩 | 50–5,000 N·m | 产品手册 |
| 扭转刚度 | 未公开 | 产品手册 |
| 背隙 | ≤ 1 arc-min | 产品手册 |
| 传动精度 | ≤ 1 arc-min | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：自主齿形与轴承设计、高刚性、长寿命，适配重载工业机器人与人形机器人大扭矩关节。

**应用场景**：工业机器人基座/肩部/肘部、人形机器人髋/腰/膝关节、重型转台。

### 工业机器人 / Greatoo Industrial Robot

> 工业机器人：请访问 [官方资料](http://www.greatoo.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 负载 | 6–220 kg | 产品手册 |
| 臂展 | 700–3,200 mm | 产品手册 |
| 重复定位精度 | ±0.05 mm | 产品手册 |
| 自由度 | 6 | 产品手册 |
| 防护等级 | IP54 | 产品手册 |
| 应用领域 | 搬运、码垛、打磨 | 产品手册 |
| 通信接口 | EtherCAT / Modbus | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：六轴机器人本体与 RV 减速器协同开发，实现关键部件自主可控。

**应用场景**：汽车零部件、橡胶轮胎、金属加工、物流搬运。

## 供应链位置

- **上游关键零部件/材料**：合金钢、轴承、润滑油、铸件、电机、驱动器
- **下游客户/应用场景**：汽车轮胎厂、工业机器人集成商、人形机器人 OEM、金属加工
- **主要竞争对手/对标**：Nabtesco、住友、秦川机床、双环传动、中大力德

## 知识图谱节点与关系

- 公司实体：`ent_company_greatoo`
- 产品/零部件实体：`ent_component_greatoo_rv_reducer`, `ent_product_greatoo_industrial_robot`
- 关键关系：
  - `ent_company_greatoo` -- `manufactures` --> `ent_component_greatoo_rv_reducer`
  - `ent_company_greatoo` -- `manufactures` --> `ent_product_greatoo_industrial_robot`

## 参考资料

1. [官网](http://www.greatoo.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）