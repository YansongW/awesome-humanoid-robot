---
id: ent_component_qinchuan_ball_screw
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 秦川机床汉江滚珠丝杠
  en: Qinchuan Hanjiang Ball Screw
status: active
sources:
- id: src_qinchuan_company_wiki
  type: document
- title: 附录 D 企业 Wiki - 秦川机床
  url: docs/appendices/appendix-d/companies/company_qinchuan.md
- id: src_qinchuan_sh_gov
  type: website
- title: 秦川集团汉江机床SH系列高性能滚珠丝杠副定型成功 - 陕西省国资委
  url: https://sxgz.shaanxi.gov.cn/sy/gqzc/qydt/202504/t20250428_3508671.html
- id: src_qinchuan_investor
  type: website
- title: 秦川机床投资者关系 - 人形机器人丝杠布局
  url: https://stock.stockstar.com/RB2024121300027818.shtml
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications extracted from company Wiki, Shaanxi SASAC release
    and investor relations disclosures; model-specific dynamic load ratings and price
    are not public.
---


# 秦川机床汉江滚珠丝杠 / Qinchuan Hanjiang Ball Screw

## 概述

汉江滚珠丝杠是秦川机床工具集团旗下汉江机床有限公司生产的精密滚动功能部件，广泛应用于数控机床、工业机器人、人形机器人线性关节、航空航天作动器与半导体设备。产品覆盖磨制滚珠丝杠、直线导轨及行星滚柱丝杠，依托秦川机床在螺纹磨床与“04 专项”技术积累，可实现 P2 级及以上精度，部分产品达到 P1/P0 级。

## 工作原理 / 技术架构

滚珠丝杠通过滚珠在丝杠螺纹滚道与螺母滚道之间的滚动，将旋转运动转换为直线运动。相比滑动丝杠，其摩擦系数显著降低，传动效率可达 90% 以上。

导程 \(P_h\)、转速 \(n\) 与直线速度 \(v\) 的关系为：

\[
v = \frac{P_h \cdot n}{60}
\]

其中 \(v\) 单位为 mm/s，\(P_h\) 单位为 mm，\(n\) 单位为 rpm。定位精度由丝杠导程误差、反向间隙与预紧方式共同决定；高精度磨制丝杠通过双螺母预紧或单螺母变位预紧消除轴向间隙。

额定动载荷 \(C_a\) 与额定寿命 \(L_{10}\) 的关系可表示为：

\[
L_{10} = \left( \frac{C_a}{F_m} \right)^3 \times 10^6 \quad \text{rev}
\]

其中 \(F_m\) 为当量轴向载荷。汉江机床滚珠丝杠通过自主螺纹磨削工艺与高精度螺母配对，保证批次一致性与精度保持性。

## 关键参数

| 参数项 | 数值/范围 | 备注/来源 |
|--------|-----------|-----------|
| 丝杠直径 | Ø6 – Ø100 mm | 产品手册 |
| 导程 | 1 – 50 mm | 产品手册 |
| 精度等级 | C3 – C10（标准系列）；SH 系列 P2 级及以上，P1 级占比 > 60% | 产品手册 / 陕西省国资委 |
| 最大行程 | 依定制，SH 系列覆盖 GQ63 以下、长度 4 m 以内 | 产品手册 |
| 预紧方式 | 双螺母预紧 / 单螺母变位预紧 | 产品手册 |
| 材质 | 轴承钢 / 渗碳淬火钢 | 产品手册 |
| 额定动载荷 | 依型号 | 产品手册 |
| 额定静载荷 | 依型号 | 产品手册 |
| 噪音水平 | SH 系列较常规产品降低 15% | 陕西省国资委 |
| 精度保持性 | SH 系列较常规产品提高 31% | 陕西省国资委 |
| 直线度（长丝杠） | 10 m 长丝杠直线度误差 ≤ 0.02 mm（公开报道） | 市场公开报道 |
| 价格 | 未公开 | — |

## 应用场景

- **数控机床进给轴**：为加工中心、精密磨床提供高精度直线传动。
- **人形机器人线性关节**：行星滚柱丝杠与滚珠丝杠用于下肢线性执行器、手指推杆等。
- **航空航天与半导体设备**：高刚性、高精度、长寿命特性适配电动作动器与晶圆传输机构。

## 供应链关系

汉江滚珠丝杠由 **秦川机床工具集团（实体 `ent_company_qinchuan`）** 旗下汉江机床有限公司制造。上游依赖轴承钢、合金结构钢、砂轮、数控系统、伺服电机与热处理服务；下游客户包括机床厂商、人形机器人 OEM、航空航天与汽车制造企业。在知识图谱中，该实体通过 `manufactures` 关系与公司节点 `ent_company_qinchuan` 相连，是秦川机床滚动功能部件产品线的核心零部件。

## 来源与验证

- 附录 D 企业 Wiki《秦川机床》（docs/appendices/appendix-d/companies/company_qinchuan.md）
- 陕西省国资委发布《秦川集团汉江机床SH系列高性能滚珠丝杠副定型成功》（https://sxgz.shaanxi.gov.cn/sy/gqzc/qydt/202504/t20250428_3508671.html）
- 秦川机床投资者关系互动（https://stock.stockstar.com/RB2024121300027818.shtml）

具体型号的额定动/静载荷、单价与部分长丝杠精度参数在公开渠道未完整披露，已标注为“未公开”。