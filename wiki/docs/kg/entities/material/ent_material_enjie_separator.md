---
id: ent_material_enjie_separator
schema_version: 1
type: material
domain: 01_raw_materials
theoretical_depth: system
names:
  zh: 恩捷股份湿法锂离子电池隔膜
  en: SEM Wet Lithium-Ion Battery Separator
status: active
aliases:
- 恩捷隔膜
- SEM Wet Separator
sources:
- id: src_enjie_annual_esg
  type: document
  url: https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=002812&id=10057614
- title: 恩捷股份 2023 环境、社会及管治报告
- id: src_enjie_cibf2025
  type: article
  url: https://libattery.ofweek.com/2025-05/ART-36002-8120-30663593.html
- title: 恩捷股份 CIBF2025 专访
- id: src_enjie_firstshanghai_report
  type: document
  url: https://pdf.dfcfw.com/pdf/H3_AP202305181586743033_1.pdf
- title: 湿法隔膜龙头标的研报
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 恩捷股份湿法锂离子电池隔膜 / SEM Wet Lithium-Ion Battery Separator

## 概述

恩捷股份湿法锂离子电池隔膜是由云南恩捷新材料股份有限公司（SEM）生产的聚烯烃微孔隔膜，广泛应用于新能源汽车动力电池、3C 消费电子电池及储能电池。产品包括湿法基膜与功能性涂布膜，厚度覆盖 5–20 μm，具有微孔尺寸均匀、横向力学性能好、穿刺强度高等特点。恩捷股份已与宁德时代、比亚迪、LGES、松下、三星等全球主流电池厂商建立合作关系，是全球湿法隔膜龙头供应商之一。

## 物理化学基础

湿法隔膜以聚乙烯（PE）为主要原料，通过热致相分离法制备：将 PE 与增塑剂混合挤出成膜，经双向拉伸后用萃取剂去除增塑剂，形成连通微孔结构。隔膜的核心功能是允许锂离子在电解液中迁移，同时阻隔电子导通以防止短路。

关键性能可用以下关系描述：

1. **离子传输**：有效离子电导率

$$
   \sigma_{\text{eff}}=\frac{\varepsilon}{\tau}\sigma_{\text{elyte}},
   $$

其中 $\varepsilon$ 为孔隙率，$\tau$ 为迂曲度，$\sigma_{\text{elyte}}$ 为电解液本征电导率。

2. **机械强度**：穿刺强度与拉伸强度决定隔膜在卷绕与装配过程中的完整性。
3. **热安全性**：隔膜在约 130 °C 附近闭孔以阻断离子通路；恩捷高安全基膜 x 系列通过分子链改性将破膜温度提升至 230 °C。
4. **厚度与能量密度**：更薄的隔膜有助于提升电池体积能量密度，但需兼顾机械强度与热稳定性。

## 关键参数表

| 参数 | 数值 / 说明 |
|---|---|
| 材料体系 | 聚乙烯（PE）湿法微孔隔膜 |
| 产品形态 | 基膜 / 涂布膜（陶瓷、PVDF、勃姆石等） |
| 厚度范围 | 5–20 μm |
| 生产工艺 | 湿法双向拉伸 + 萃取成孔 |
| 高安全基膜破膜温度 | 230 °C（x 系列） |
| 在线涂布 | 一体化生产，提升一致性 |
| 主要应用 | 动力电池、3C、储能 |
| 下游客户 | 宁德时代、比亚迪、中创新航、亿纬锂能、LGES、松下、三星等 |
| 孔隙率 / 透气度（公开值） | 未公开 |
| 拉伸强度（公开值） | 未公开 |

## 在机器人系统中的作用

湿法隔膜是锂离子电池的核心安全材料之一。在人形机器人、无人叉车、移动机器人等电动化平台中，隔膜直接影响电池的能量密度、循环寿命与热安全：

- **高能量密度**：薄型化隔膜允许更多活性物质装载，提升续航。
- **高安全性**：闭孔与破膜温度设计可在热失控早期阻断或延缓反应。
- **长循环寿命**：均匀的孔径分布与低迂曲度有助于降低锂离子传输极化。

## 供应链关系

- **上游**：PE 树脂、成孔剂/增塑剂、萃取剂、涂覆材料（陶瓷、PVDF）、生产设备供应商。
- **同层**：恩捷股份作为隔膜制造商，同时布局干法隔膜、铝塑膜等产品，形成“湿法+干法+涂覆”的综合供应能力。
- **下游**：动力电池与储能电池 cell 厂商（CATL、BYD、LGES 等），再向下游供应给电动汽车、机器人、3C 终端制造商。

## 来源与验证

- 恩捷股份 ESG 报告（含业务介绍）：https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid=002812&id=10057614
- OFweek CIBF2025 专访：https://libattery.ofweek.com/2025-05/ART-36002-8120-30663593.html
- 第一上海研报：https://pdf.dfcfw.com/pdf/H3_AP202305181586743033_1.pdf

具体隔膜孔隙率、透气度、拉伸强度等未在公开资料中披露，本卡片以“未公开”标注。