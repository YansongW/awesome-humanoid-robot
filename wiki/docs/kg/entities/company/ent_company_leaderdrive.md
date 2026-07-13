---
id: ent_company_leaderdrive
schema_version: 1
type: company
'title:': Leaderdrive
domain: 02_components
theoretical_depth: system
names:
  zh: 绿的谐波
  en: Leaderdrive
status: active
sources:
- id: src_leaderdrive_official
  type: website
  url: https://www.leaderdrive.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 绿的谐波 / Leaderdrive

# 绿的谐波 / Leaderdrive

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 绿的谐波 |
| **英文名** | Leaderdrive |
| **总部** | 中国江苏苏州 |
| **成立时间** | 2011 |
| **官网** | [https://www.leaderdrive.com](https://www.leaderdrive.com) |
| **供应链环节** | 谐波减速器 / 机电一体化 / 精密传动 |
| **企业属性** | 国产品牌、科创板上市公司（688017.SH） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

## 公司简介

国产谐波减速器龙头，打破日本哈默纳科长期垄断，产品覆盖工业机器人与人形机器人关节。

绿的谐波提供 LHS/LCS/LCD 系列谐波减速器及 KGM 一体化关节模组，具备自主知识产权的 P 型齿形，客户包括埃斯顿、优必选、埃夫特等国内主流机器人企业。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| LHS/LCS 谐波减速器 | 标准/中空谐波减速器 | LHS-32 / LCS-25 | 机器人关节、转台 |
| LCD 超薄系列 | 扁平谐波减速器 | LCD-14 / LCD-17 | 机器人末端、人形手腕 |

## 代表产品

### LHS-32-100 谐波减速器 / LHS-32-100 Harmonic Reducer

> LHS-32-100 谐波减速器：请访问 [官方资料](https://www.leaderdrive.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 规格 | 32（节圆直径） | 绿的谐波产品手册 |
| 减速比 | 50/80/100/120:1 | 绿的谐波产品手册 |
| 额定扭矩（2000rpm） | 50/79/91/91 N·m | 绿的谐波产品手册 |
| 启动停止容许扭矩 | 143/202/221/235 N·m | 绿的谐波产品手册 |
| 瞬时最大扭矩 | 255/350/399/423 N·m | 绿的谐波产品手册 |
| 最高输入转速 | 4500 rpm | 绿的谐波产品手册 |
| 平均输入转速 | 3500 rpm | 绿的谐波产品手册 |
| 背隙 | ≤ 20 arcsec | 绿的谐波产品手册 |
| 重量 | 2.5 kg | 绿的谐波产品手册 |

**技术亮点**：高刚性中空结构，承载能力高，寿命长，适配机器人肩/肘/腕关节。

**应用场景**：工业机器人、人形机器人关节、协作机器人、CNC 转台。

### LCD-14-100 超薄谐波减速器 / LCD-14-100 Ultra-thin Harmonic Reducer

> LCD-14-100 超薄谐波减速器：请访问 [官方资料](https://www.leaderdrive.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 规格 | 14 | 绿的谐波产品手册 |
| 减速比 | 50/80/100:1 | 绿的谐波产品手册 |
| 额定扭矩（2000rpm） | 3.5/5.1/5.1 N·m | 绿的谐波产品手册 |
| 启动停止容许扭矩 | 11.4/15/18 N·m | 绿的谐波产品手册 |
| 瞬时最大扭矩 | 23/29/33 N·m | 绿的谐波产品手册 |
| 最高输入转速 | 8000/7000/6000 rpm | 绿的谐波产品手册 |
| 背隙 | ≤ 20 arcsec | 绿的谐波产品手册 |
| 重量 | 0.56/0.48/0.68 kg | 绿的谐波产品手册 |

**技术亮点**：超薄杯状柔轮设计，轴向尺寸小、重量轻，适合机器人末端和手指关节。

**应用场景**：协作机器人末端、人形机器人腕部/手指、医疗机器人。

## 供应链位置

- **上游关键零部件/材料**：合金钢（柔轮/刚轮）、柔性轴承、润滑脂、铝材
- **下游客户/应用场景**：埃斯顿、优必选、埃夫特、新时达等机器人 OEM
- **主要竞争对手/对标**：Harmonic Drive Systems、来福谐波、同川精密

## 知识图谱节点与关系

- 公司实体：`ent_company_leaderdrive`
- 产品实体：`ent_component_leaderdrive_lhs_32_100`、`ent_component_leaderdrive_lcd_14_100`
- 关键关系：
  - `ent_company_leaderdrive` -- `manufactures` --> `ent_component_leaderdrive_lhs_32_100`
  - `ent_company_leaderdrive` -- `manufactures` --> `ent_component_leaderdrive_lcd_14_100`
  - `ent_company_leaderdrive` -- `supplies` --> `ent_company_estun`
  - `ent_company_leaderdrive` -- `supplies` --> `ent_company_ubtech`

## 参考资料

1. [官网](https://www.leaderdrive.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）