---
id: ent_component_taide_ac_compressor_bearing
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 泰德股份汽车空调压缩机轴承
  en: Taide Automotive A/C Compressor Bearing
status: active
sources:
- id: src_taide_company_wiki
  type: document
- title: 附录 D 企业 Wiki - 泰德股份
  url: docs/appendices/appendix-d/companies/company_taide.md
- id: src_taide_made_in_china
  type: website
- title: Qingdao Taide Automobile Bearing Co., Ltd - Company Profile
  url: https://www.made-in-china.com/showroom/taidebearing/
- id: src_nsk_mcb
  type: document
- title: NSK Magnetic Clutch Bearings for A/C Compressor
  url: https://www.nsk.com/content/dam/nsk/am/en_us/documents/automotive-americas/MCB_products_heet.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications extracted from company Wiki and public product literature;
    exact model-level dynamic ratings and price are not public.
---


# 泰德股份汽车空调压缩机轴承 / Taide Automotive A/C Compressor Bearing

## 概述

汽车空调压缩机轴承是青岛泰德汽车轴承股份有限公司的核心产品之一，主要用于汽车空调压缩机电磁离合器皮带轮与压缩机主轴之间的旋转支撑。该类产品通常为双列角接触球轴承或带密封深沟球轴承，需在高转速、制冷剂侵蚀、高低温交变与振动环境下长期可靠运行。泰德股份在该细分领域处于国内领先地位，产品配套国内外主流汽车空调系统供应商，并逐步向新能源汽车热管理与机器人微型轴承拓展。

## 工作原理 / 技术架构

空调压缩机离合器轴承一般为双列角接触球轴承（double-row angular contact ball bearing）或薄截面磁离合器轴承（magnetic clutch bearing, MCB）。其结构特点包括：

- **双列角接触设计**：可同时承受径向载荷与双向轴向载荷，适合皮带张力与电磁吸合力共同作用的工况。
- **高密封性**：采用接触式橡胶密封（2RS）或金属防尘盖，防止制冷剂、水分与灰尘侵入。
- **长寿命润滑脂**：填充耐制冷剂、耐高温的专用润滑脂，减少高速运转下的泄漏与老化。

轴承接触角 \(\alpha\) 决定其承受轴向载荷的能力。轴向承载系数 \(Y\) 与接触角相关，对于角接触球轴承：

\[
F_a / F_r > e \quad \Rightarrow \quad P = X F_r + Y F_a
\]

其中 \(P\) 为当量动载荷，\(F_r\) 为径向载荷，\(F_a\) 为轴向载荷，\(X\)、\(Y\) 为载荷系数，\(e\) 为判断系数。

基本额定寿命按 ISO 281：

\[
L_{10} = \left( \frac{C}{P} \right)^p \times 10^6 \quad \text{rev}
\]

对于球轴承，\(p = 3\)。

## 关键参数

| 参数项 | 数值/范围 | 备注/来源 |
|--------|-----------|-----------|
| 轴承类型 | 双列角接触球轴承 / 汽车空调磁离合器轴承 | 产品手册 |
| 内径范围 | 15–45 mm | 产品手册 |
| 外径范围 | 32–80 mm | 产品手册 |
| 宽度范围 | 3–27 mm（参考同公司深沟球轴承系列） | 产品手册 |
| 最高转速 | 10,000 rpm | 产品手册 |
| 工作温度 | −30 °C – +120 °C | 产品手册 |
| 精度等级 | P6 / P5 / P4（参考同公司标准） | 产品手册 |
| 材质 | 轴承钢 GCr15 | 产品手册 |
| 密封方式 | 接触式橡胶密封（2RS） | 产品手册 |
| 润滑 | 长寿命专用润滑脂 | 产品手册 |
| 额定动载荷 | 依型号 | 产品手册 |
| 主要客户 | Sanden、VALEO、OGURA CLUTCH、三菱、一汽丰田、上海通用五菱等 | 公开资料 |
| 年产能 | 约 1000 万套（全系列轴承） | 公开资料 |
| 价格 | 未公开 | — |

## 应用场景

- **传统燃油车空调压缩机**：支撑电磁离合器皮带轮，传递发动机皮带驱动扭矩。
- **新能源汽车电动压缩机**：适配电动涡旋式/斜盘式压缩机的高转速主轴支撑。
- **热管理系统泵阀**：为新能源汽车热泵、电子水泵等旋转部件提供轴承。
- **机器人微型轴承拓展**：泰德股份正布局人形机器人小关节微型球轴承。

## 供应链关系

汽车空调压缩机轴承由 **青岛泰德汽车轴承股份有限公司（实体 `ent_company_taide`）** 制造。上游依赖轴承钢、润滑脂、密封圈、保持架与磨削设备；下游客户包括汽车空调压缩机厂、新能源汽车热管理系统厂及机器人关节模组厂。在知识图谱中，该实体通过 `manufactures` 关系与公司节点 `ent_company_taide` 相连，是泰德股份从汽车轴承向机器人轴承延伸的基础产品。

## 来源与验证

- 附录 D 企业 Wiki《泰德股份》（docs/appendices/appendix-d/companies/company_taide.md）
- 泰德股份 Made-in-China 企业简介（https://www.made-in-china.com/showroom/taidebearing/）
- NSK Magnetic Clutch Bearings 技术资料（https://www.nsk.com/content/dam/nsk/am/en_us/documents/automotive-americas/MCB_products_heet.pdf）

具体型号的额定动载荷、静载荷与单价在公开渠道未完整披露，已标注为“未公开”。