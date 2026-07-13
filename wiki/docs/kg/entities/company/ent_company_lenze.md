---
id: ent_company_lenze
schema_version: 1
type: company
'title:': Lenze
domain: 02_components
theoretical_depth: system
names:
  zh: 伦茨
  en: Lenze
status: active
sources:
- id: src_lenze_official
  type: website
  url: https://www.lenze.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 伦茨 / Lenze

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 伦茨 |
| **英文名** | Lenze |
| **总部** | 德国阿伦森（Aerzen） |
| **成立时间** | 1947 |
| **官网** | [https://www.lenze.com](https://www.lenze.com) |
| **供应链环节** | 运动控制 / 减速机 / 伺服驱动 |
| **企业属性** | 家族企业、国际运动控制品牌 |
| **母公司/所属集团** | 独立（Lenze SE） |
| **数据来源** | 官网、产品样本、WAIC 2026 报道 |

## 公司简介

Lenze 是德国运动控制与自动化技术供应商，提供 g500 系列模块化减速机、m850 伺服电机、i950/i700 变频器以及基于 FAST 应用软件的自动化平台。其 g500 系列以标准化接口、低背隙和终身润滑为特点。

公司产品覆盖从机械减速、电机驱动到数字化产线的完整运动控制链路，特别适用于包装、物流、机器人和机床应用。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 模块化减速机 | 同轴/直角/轴装式 | g500-H / g500-B / g500-S | 自动化、机器人 |
| 伺服电机与驱动 | 高动态/可扩展 | m850 / i950 / i700 | 包装、机床 |
| 自动化平台 | 运动控制软件 | FAST / Lenze Smart Motor | 产线、物流 |

## 代表产品

### g500-H 斜齿减速机

> g500-H 斜齿减速机：请访问 [官方资料](https://www.lenze.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 减速比 | 最高约 i=370（2/3 级） | 产品手册 |
| 额定输出扭矩 | 45 – 20,000 N·m（系列范围） | 产品手册 |
| 级数 | 2 级 / 3 级（部分 4 级） | 产品手册 |
| 背隙 | 低背隙设计 | 产品手册 |
| 防护等级 | 最高 IP65 | 产品手册 |
| 润滑 | 终身润滑（合成润滑脂） | 产品手册 |
| 安装方式 | 底脚 / 法兰 / 实心轴 / 空心轴 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：模块化设计、与 Lenze 电机/变频器即插即用、标准化轴与法兰尺寸、终身润滑免维护。

**应用场景**：包装机械、输送系统、机器人关节、机床进给、仓储物流。

### 其他代表产品

g500-B 伞齿减速机：扭矩 45–20,000 N·m，减速比最高 360，适用于直角布局；m850 同步伺服电机支持高动态应用。

## 供应链位置

- **上游关键零部件/材料**：钢材、铸件、轴承、密封件、电机、磁性材料、功率电子
- **下游客户/应用场景**：包装 OEM、机器人整机厂、物流集成商、机床制造商
- **主要竞争对手/对标**：SEW-Eurodrive、Siemens、Bosch Rexroth、STOBER

## 知识图谱节点与关系

- 公司实体：`ent_company_lenze`
- 零部件实体：`ent_component_lenze_g500_h`
- 关键关系：
  - `ent_company_lenze` -- `manufactures` --> `ent_component_lenze_g500_h`

## 参考资料

1. [伦茨 官网](https://www.lenze.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [Lenze g500 产品手册](https://www.lenze.com/en/products/gearmotors/gearmotors/)