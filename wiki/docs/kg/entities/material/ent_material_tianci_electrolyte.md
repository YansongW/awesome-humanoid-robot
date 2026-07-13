---
id: ent_material_tianci_electrolyte
schema_version: 1
type: material
domain: 01_raw_materials
theoretical_depth: system
names:
  zh: 天赐材料 锂离子电池电解液
  en: Tinci Lithium-ion Battery Electrolyte
status: active
sources:
- id: src_tianci_tinchem
  type: website
  url: https://www.tinchem.com
- title: 广州天赐高新材料股份有限公司官网
- id: src_tianci_investor_qa
  type: website
  url: https://new.qq.com/rain/a/20230522A07L1E00
- title: 天赐材料：公司主要产品为锂离子电池电解液 - 腾讯新闻
- id: src_tianci_research_report
  type: website
  url: https://pdf.dfcfw.com/pdf/H3_AP202512231806514343_1.pdf
- title: 天赐材料（002709）公司深度研究 - 东方财富
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 天赐材料 锂离子电池电解液 / Tinci Lithium-ion Battery Electrolyte

## 概述

锂离子电池电解液是锂离子电池的“血液”，在充放电过程中承担锂离子在正负极之间传输的介质功能。广州天赐高新材料股份有限公司（股票代码：002709）是全球主要的锂离子电池电解液供应商之一，2023 年全球市场占有率约 36.4%。公司产品覆盖磷酸铁锂、三元、高电压、快充及硅基负极等多种电池体系，并在 LiFSI 新型锂盐与固态/半固态电解质领域持续布局。

## 物理化学基础 / 本构关系

电解液通常由溶剂、锂盐与添加剂组成。溶剂多为碳酸酯类（如 EC、DMC、EMC、DEC）与醚类；锂盐主要包括六氟磷酸锂（LiPF6）与双氟磺酰亚胺锂（LiFSI）；添加剂包括碳酸亚乙烯酯（VC）、氟代碳酸乙烯酯（FEC）等，用于形成稳定的固体电解质界面膜（SEI）。

电解液的离子电导率可表示为

\[
\kappa = \sum_i n_i q_i \mu_i
\]

其中 \(n_i\) 为载流子浓度，\(q_i\) 为电荷量，\(\mu_i\) 为离子迁移率。LiFSI 因阴离子更大、解离能力更强，其电解液室温离子电导率可达约 \(9.8\,\text{mS/cm}\)，高于传统 LiPF6 电解液的约 \(6.8\,\text{mS/cm}\)。锂离子迁移数

\[
t_{\text{Li}^+} = \frac{\mu_{\text{Li}^+}}{\mu_{\text{Li}^+} + \mu_{\text{anion}}}
\]

是衡量电解液中锂离子传输选择性的重要指标。

电池的能量密度可近似为

\[
E = \int_{Q_0}^{Q_1} V(Q)\,\text{d}Q
\]

电解液通过稳定高电压正极、抑制副反应与优化 SEI，直接影响电池的可用容量、循环寿命与安全性。

## 关键参数表

| 参数 | 数值/范围 |
|------|-----------|
| 主要锂盐 | LiPF6、LiFSI（双氟磺酰亚胺锂） |
| LiPF6 电解液电导率 | 约 \(6.8\,\text{mS/cm}\) |
| LiFSI 电解液电导率 | 约 \(9.8\,\text{mS/cm}\) |
| LiFSI 分解温度 | \(>200^\circ\text{C}\) |
| 工作电压 | 支持 4.5 V 以上高电压体系 |
| 低温性能 | \(-20^\circ\text{C}\) 仍保持较高离子电导率 |
| 核心锂盐自供率 | 六氟磷酸锂自供比例 >97% |
| 2023 年全球电解液市占率 | 约 36.4% |
| 聚合物凝胶电解质室温离子电导率 | \(>5\,\text{mS/cm}\) |
| 硫化物固态电解质离子电导率 | \(>8\,\text{mS/cm}\)（实验室阶段） |

## 在机器人系统中的作用

锂离子电池电解液是服务机器人、人形机器人、AGV/AMR、无人机及外骨骼等移动装备电池包的核心材料。高电导率、宽温域与长循环寿命的电解液可提升电池能量密度与快充能力，从而延长机器人续航、缩短充电时间并提高任务连续性。LiFSI 等新型锂盐与固态电解质技术路线，是下一代高安全、高能量密度机器人电池的重要发展方向。

## 供应链关系

天赐材料电解液处于锂电池材料产业链中游。上游为碳酸酯溶剂、锂盐（六氟磷酸锂、LiFSI）、功能性添加剂与氟化锂等原料，其中天赐自产六氟磷酸锂比例超过 97%；中游为天赐材料的电解液配方开发、混合与纯化能力；下游面向动力电池与储能电池企业（如宁德时代、比亚迪等），最终应用于新能源汽车、电动工具、消费电子及各类机器人产品。

## 来源与验证

参数与业务描述来自天赐材料官网、投资者互动平台及东方财富研究报告。具体商业配方、添加剂种类与比例属于企业商业秘密，未在公开资料中披露，标注为“未公开”。