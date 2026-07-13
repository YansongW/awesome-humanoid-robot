---
id: ent_component_wuzhou_xinchun_harmonic_reducer_bearing
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 五洲新春谐波减速器轴承
  en: Wuzhou Xinchun Harmonic Reducer Bearing
status: active
sources:
- id: src_wuzhou_xinchun_company_wiki
  type: document
- title: 附录 D 企业 Wiki - 五洲新春
  url: docs/appendices/appendix-d/companies/company_wuzhou_xinchun.md
- id: src_wuzhou_xinchun_eastmoney
  type: website
- title: 五洲新春投资者关系互动 - 东方财富
  url: https://guba.eastmoney.com/news,603667,1670142753.html
- id: src_wuzhou_xinchun_stockstar
  type: website
- title: 五洲新春减速器轴承配套情况 - 证券之星
  url: http://stock.stockstar.com/RB2022101700005152.shtml
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications extracted from company Wiki and investor relations
    disclosures; model-specific dynamic load ratings and price are not public.
---


# 五洲新春谐波减速器轴承 / Wuzhou Xinchun Harmonic Reducer Bearing

## 概述

五洲新春谐波减速器轴承是浙江五洲新春集团股份有限公司面向机器人关节减速器开发的精密轴承产品。该类轴承主要包括用于波发生器的柔性薄壁轴承（flexible bearing）和用于输出端的高刚性交叉滚子轴承（crossed roller bearing），是谐波减速器实现低背隙、高扭转刚性与长寿命的关键支撑件。五洲新春具备锻造车削、热处理、磨削全产业链能力，产品已配套国内多家减速器企业。

## 工作原理 / 技术架构

谐波减速器轴承需在柔轮周期性弹性变形的工况下保持高精度运转：

- **柔性薄壁轴承**：安装在椭圆波发生器凸轮与柔轮内壁之间，外圈随柔轮一起发生可控弹性变形。其设计需在薄壁化与疲劳寿命之间取得平衡，常用椭圆度补偿与特殊保持架结构降低边缘应力。
- **交叉滚子轴承（刚性轴承）**：安装在减速器输出端，承受径向、轴向与倾覆力矩联合载荷。滚子以 90° 交错排列，可在一个轴承内实现多向承载与高刚性。

轴承额定寿命 \(L_{10}\) 可按 ISO 281 基本额定寿命公式估算：

\[
L_{10} = \left( \frac{C}{P} \right)^p \times 10^6 \quad \text{rev}
\]

其中 \(C\) 为基本额定动载荷（N），\(P\) 为当量动载荷（N），\(p = 3\) 为球轴承寿命指数。柔性轴承由于工作过程中存在周期性椭圆变形，其疲劳分析还需考虑柔性变形引起的附加应力。

## 关键参数

| 参数项 | 数值/范围 | 备注/来源 |
|--------|-----------|-----------|
| 轴承类型 | 柔性薄壁轴承 / 交叉滚子轴承 | 公司 Wiki |
| 内径范围 | 20–150 mm | 产品手册 |
| 外径范围 | 40–200 mm | 产品手册 |
| 精度等级 | P5 / P4 | 产品手册 |
| 材质 | 轴承钢 GCr15 / 渗碳钢 | 产品手册 |
| 热处理 | 淬火 + 低温回火 | 产品手册 |
| 润滑 | 油脂润滑 | 产品手册 |
| 额定动载荷 | 依型号 | 产品手册 |
| 基本额定静载荷 | 依型号 | 产品手册 |
| 接触角（角接触系列） | 15° / 25° / 40°（参考同公司角接触轴承） | 产品手册 |
| 主要客户 | 南高齿、来福谐波等减速器企业 | 投资者关系披露 |
| 价格 | 未公开 | — |

## 应用场景

- **协作机器人关节**：为谐波减速器提供波发生器柔性轴承与输出端交叉滚子轴承。
- **人形机器人旋转关节**：适配肩部、肘部、腕部、髋部等需要高刚性、低背隙的旋转执行器。
- **精密转台与医疗机器人**：高刚性交叉滚子轴承用于半导体转台、手术机器人等精密旋转支撑。

## 供应链关系

谐波减速器轴承由 **五洲新春集团股份有限公司（实体 `ent_company_wuzhou_xinchun`）** 制造。上游依赖轴承钢、渗碳钢、锻造设备、数控车床、磨床与热处理炉；下游客户包括 SKF、Schaeffler、NSK、汽车 OEM、风电主机厂及机器人减速器厂。在知识图谱中，该实体通过 `manufactures` 关系与公司节点 `ent_company_wuzhou_xinchun` 相连，是机器人减速器轴承国产替代的重要供应节点。

## 来源与验证

- 附录 D 企业 Wiki《五洲新春》（docs/appendices/appendix-d/companies/company_wuzhou_xinchun.md）
- 五洲新春投资者关系互动（https://guba.eastmoney.com/news,603667,1670142753.html）
- 证券之星投资者关系报道（http://stock.stockstar.com/RB2022101700005152.shtml）

具体型号的额定动载荷、静载荷与单价在公开渠道未完整披露，已标注为“未公开”。