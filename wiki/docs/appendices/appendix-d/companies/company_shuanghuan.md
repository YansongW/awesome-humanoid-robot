---
id: ent_company_shuanghuan
schema_version: 1
type: company
title: Shuanghuan Driveline
domain: 02_components
theoretical_depth: system
names:
  zh: 双环传动
  en: Shuanghuan Driveline
status: active
sources:
  - id: src_shuanghuan_official
    type: website
    title: Shuanghuan Driveline Official Website
    url: http://www.shuanghuandrive.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# 双环传动 / Shuanghuan Driveline

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 双环传动 |
| **英文名** | Shuanghuan Driveline |
| **总部** | 中国浙江玉环 |
| **成立时间** | 1980 |
| **官网** | [http://www.shuanghuandrive.com](http://www.shuanghuandrive.com) |
| **供应链环节** | RV 减速器 / 谐波减速器 / 精密齿轮 |
| **企业属性** | 国产品牌、上市公司（002472.SZ） |
| **母公司/所属集团** | 无（独立上市），子公司环动科技 |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

## 公司简介

国产 RV 减速器龙头子公司环动科技，深耕精密齿轮与机器人减速器。

双环传动通过子公司环动科技布局 RV 减速器、谐波减速器和行星减速器，产品覆盖 3–1000 kg 负载机器人所需精密减速器，已实现批量供货宇树科技等头部机器人企业。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| SHPR-E RV 减速器 | 主轴承内置型 RV | SHPR-40E / SHPR-20E | 工业机器人重载关节 |
| 谐波/行星减速器 | 轻载及人形机器人关节 | 谐波系列 / 行星系列 | 人形机器人、协作机器人 |

## 代表产品

### SHPR-40E-121 RV 减速器 / SHPR-40E-121 RV Reducer

> SHPR-40E-121 RV 减速器：请访问 [官方资料](http://www.shuanghuandrive.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 型号 | SHPR-40E-121 | 盖尔斯威产品页 |
| 减速比 | 121:1 | 盖尔斯威产品页 |
| 额定扭矩 | 412 N·m | 盖尔斯威产品页 |
| 背隙 | ≤ 1 arcmin | 盖尔斯威产品页 |
| 特点 | 主轴承内置、强抗扭刚度、体积紧凑 | 盖尔斯威产品页 |
| 应用 | 工业机器人关节、焊接变位机、旋转台 | 盖尔斯威产品页 |
| 重量 | 未公开 | - |
| 最高输入转速 | 未公开 | - |

**技术亮点**：国产 RV 减速器代表型号，性能接近 Nabtesco 同类产品，性价比高。

**应用场景**：六轴工业机器人 J1–J3、人形机器人腰/髋部、重载变位机。

### SHPR-20E RV 减速器 / SHPR-20E RV Reducer

> SHPR-20E RV 减速器：请访问 [官方资料](http://www.shuanghuandrive.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 系列 | SHPR-E | 盖尔斯威产品页 |
| 减速比 | 57/81/105/121/141/161:1 | Nabtesco RV-E 兼容系列 |
| 额定扭矩 | 未公开 | - |
| 背隙 | ≤ 1 arcmin | 盖尔斯威产品页 |
| 结构 | 两级摆线行星 + 内置主轴承 | 盖尔斯威产品页 |
| 特点 | 高刚性、抗冲击、大减速比 | 盖尔斯威产品页 |

**技术亮点**：中小型 RV 减速器，适配中小负载机器人关节和精密转台。

**应用场景**：SCARA、协作机器人、人形机器人腿部关节。

## 供应链位置

- **上游关键零部件/材料**：合金钢、轴承、润滑脂、齿轮毛坯
- **下游客户/应用场景**：宇树科技、埃斯顿、埃夫特、钱江机器人等
- **主要竞争对手/对标**：Nabtesco、中大力德、秦川机床

## 知识图谱节点与关系

- 公司实体：`ent_company_shuanghuan`
- 产品实体：`ent_component_shuanghuan_shpr_40e_121`、`ent_component_shuanghuan_shpr_20e`
- 关键关系：
  - `ent_company_shuanghuan` -- `manufactures` --> `ent_component_shuanghuan_shpr_40e_121`
  - `ent_company_shuanghuan` -- `manufactures` --> `ent_component_shuanghuan_shpr_20e`
  - `ent_company_shuanghuan` -- `supplies` --> `ent_company_unitree`

## 参考资料

1. [官网](http://www.shuanghuandrive.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）