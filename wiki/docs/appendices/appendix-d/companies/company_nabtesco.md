---
id: ent_company_nabtesco
schema_version: 1
type: company
title: Nabtesco
domain: 02_components
theoretical_depth: system
names:
  zh: Nabtesco（纳博特斯克）
  en: Nabtesco
status: active
sources:
  - id: src_nabtesco_official
    type: website
    title: Nabtesco Official Website
    url: https://www.nabtesco-motion.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Nabtesco（纳博特斯克） / Nabtesco

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Nabtesco（纳博特斯克） |
| **英文名** | Nabtesco |
| **总部** | 日本东京 |
| **成立时间** | 2003 |
| **官网** | [https://www.nabtesco-motion.cn](https://www.nabtesco-motion.cn) |
| **供应链环节** | RV 减速器 / 精密减速器 / 执行器 |
| **企业属性** | 外资品牌、Nabtesco Corporation 子公司 |
| **母公司/所属集团** | Nabtesco Corporation |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

## 公司简介

全球 RV 减速器龙头，累计出货超过 700 万台，主导工业机器人重载关节市场。

Nabtesco 的 RV-E、RV-C、RV-N 系列 RV 减速器以高刚性、高扭矩、低背隙和长寿命著称，广泛用于工业机器人基座、大臂、肩部等重载关节。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| RV-E 系列 | 标准 RV 减速器 | RV-20E / RV-40E / RV-80E | 工业机器人重载关节 |
| RV-N 系列 | 紧凑型高扭矩 RV 减速器 | RV-25N / RV-42N | 协作/人形机器人 |

## 代表产品

### RV-40E-105 RV 减速器 / RV-40E-105 Precision Reducer

> RV-40E-105 RV 减速器：请访问 [官方资料](https://www.nabtesco-motion.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 外径 | 约 105 mm | Nabtesco RV-E 手册 |
| 重量 | 9.3 kg | 行业研报 / Nabtesco 参数表 |
| 减速比 | 105:1 | Nabtesco 产品页 |
| 额定扭矩 | 412 N·m | Nabtesco 产品页 |
| 启动停止容许扭矩 | 1029 N·m | Nabtesco 产品页 |
| 瞬时最大扭矩 | 2058 N·m | Nabtesco 产品页 |
| 容许输出转速 | 70 rpm（100% 占空比） | Nabtesco 产品页 |
| 背隙 | < 1 arc-min | Nabtesco 产品页 |
| 额定寿命 | 6000 h | Nabtesco 产品页 |

**技术亮点**：主轴承内置、高刚性、抗冲击，是工业机器人肩/腰关节的标准选择。

**应用场景**：六轴工业机器人 J1–J3 关节、人形机器人腰/髋部、重载变位机。

### RV-20E-81 RV 减速器 / RV-20E-81 Precision Reducer

> RV-20E-81 RV 减速器：请访问 [官方资料](https://www.nabtesco-motion.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 外径 | 约 65 mm | Nabtesco RV-E 手册 |
| 重量 | 约 4.7 kg | Nabtesco 参数表 |
| 减速比 | 81:1 | Nabtesco 产品页 |
| 额定扭矩 | 167 N·m | Nabtesco 产品页 |
| 启动停止容许扭矩 | 412 N·m | Nabtesco 产品页 |
| 瞬时最大扭矩 | 833 N·m | Nabtesco 产品页 |
| 容许输出转速 | 75 rpm（100% 占空比） | Nabtesco 产品页 |
| 背隙 | < 1 arc-min | Nabtesco 产品页 |
| 额定寿命 | 6000 h | Nabtesco 产品页 |

**技术亮点**：中小型 RV 减速器，适合中等负载机器人关节和精密转台。

**应用场景**：SCARA、小型六轴机器人、人形机器人腿部关节、CNC 转台。

## 供应链位置

- **上游关键零部件/材料**：合金钢、摆线轮、针齿壳、轴承、润滑脂
- **下游客户/应用场景**：工业机器人四大家族、国产机器人、人形机器人 OEM
- **主要竞争对手/对标**：双环传动、中大力德、住友重机械

## 知识图谱节点与关系

- 公司实体：`ent_company_nabtesco`
- 产品实体：`ent_component_nabtesco_rv_40e_105`、`ent_component_nabtesco_rv_20e_81`
- 关键关系：
  - `ent_company_nabtesco` -- `manufactures` --> `ent_component_nabtesco_rv_40e_105`
  - `ent_company_nabtesco` -- `manufactures` --> `ent_component_nabtesco_rv_20e_81`

## 参考资料

1. [官网](https://www.nabtesco-motion.cn)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）