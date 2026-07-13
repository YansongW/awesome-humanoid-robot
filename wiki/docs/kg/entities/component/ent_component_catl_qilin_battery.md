---
id: ent_component_catl_qilin_battery
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 宁德时代麒麟电池（CTP 3.0）
  en: CATL Qilin Battery (CTP 3.0)
status: active
sources:
- id: src_catl_qilin_news
  type: press_release
- title: CATL 麒麟电池发布会
  url: https://www.catl.com/en/news/958.html
- id: src_catl_tech
  type: website
- title: CATL Research Technology
  url: https://www.catl.com/en/research/technology/
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Pack-level dimensions/weight are vehicle-customized and not publicly
    disclosed; missing values marked as 未公开.
---


# 宁德时代麒麟电池（CTP 3.0） / CATL Qilin Battery (CTP 3.0)

## 概述

麒麟电池是宁德时代（CATL）推出的第三代 Cell-to-Pack（CTP 3.0）动力电池系统，通过取消传统模组结构，将电芯直接集成到电池包，提高体积利用率与能量密度。该系统支持 4C 快充，可在 10 分钟内将电量从 10% 充至 80%，主要面向高端长续航电动汽车，并为人形机器人底盘一体化电池包提供高能量密度、高安全性的技术参考。

## 工作原理 / 技术架构

麒麟电池 CTP 3.0 采用多功能弹性夹层、集成式水冷板与电芯倒置排列设计，将结构支撑、热管理与电气连接功能集成于一个紧凑空间。体积利用率 $\eta_{\text{vol}}$ 定义为电芯有效体积与电池包总体积之比：

$$
\eta_{\text{vol}} = \frac{V_{\text{cells}}}{V_{\text{pack}}}
$$

官方标称麒麟电池体积利用率最高可达 72%。电池包可用能量 $E_{\text{pack}}$ 可表示为

$$
E_{\text{pack}} = \eta_{\text{vol}} \cdot V_{\text{pack}} \cdot \rho_{E,\text{vol}}
$$

其中 $\rho_{E,\text{vol}}$ 为电芯体积能量密度。快充能力以 C 倍率表示，4C 意味着 15 min 左右可充入约 75% 电量（10%–80% SOC 约 10 min）。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 技术代际 | CTP 3.0（Cell-to-Pack） | CATL 官方新闻 |
| 体积利用率 | 最高 72% | CATL 官方新闻 |
| 质量能量密度（NCM） | 255 Wh/kg | CATL 官方新闻 |
| 质量能量密度（LFP） | 205 Wh/kg | CATL 官方新闻 |
| 快充能力 | 支持 4C 快充 | CATL 官方新闻 |
| 10%–80% SOC 充电时间 | 约 10 min | CATL 官方新闻 |
| 循环寿命（NCM） | ≥ 1000 次 | 行业公开资料 |
| 电芯类型 | 方形 / 圆柱（NCM / LFP） | CATL 官方新闻 |
| 热管理 | 集成式水冷板 + 多功能弹性夹层 | CATL 官方新闻 |
| 包级尺寸 | 未公开（依车型定制） | - |
| 包级重量 | 未公开（依车型定制） | - |
| 额定电压 / 容量 | 未公开 | - |
| 价格 | 未公开 | - |

## 应用场景

- **高端长续航电动汽车**：提升续航里程并缩短充电时间。
- **人形机器人底盘一体化电池包**：为人形机器人提供高能量密度、轻量化的底盘集成方案参考。
- **储能系统**：CATL EnerC/EnerOne 等储能产品线共享 CTP 技术积累。
- **商用车与特种车辆**：需要大容量、高安全性的动力电池平台。

## 供应链关系

- **上游**：锂、镍、钴等正极金属，隔膜、电解液、铜箔/铝箔、BMS 芯片、结构件。
- **制造商**：`ent_company_catl` -- `manufactures` --> `ent_component_catl_qilin_battery`。
- **下游客户**：Tesla、BMW、蔚来、大众、福特、现代等主流车企；储能系统集成商；机器人整机厂。
- **竞争对手/对标**：BYD 刀片电池、LG Energy Solution、三星 SDI、松下、亿纬锂能。

## 来源与验证

1. CATL 麒麟电池发布会：https://www.catl.com/en/news/958.html
2. CATL Research Technology：https://www.catl.com/en/research/technology/
3. 附录 D 企业 Wiki：company_catl.md
4. 行业拆解报告与公开研报

> 注：麒麟电池为定制化电池包，具体尺寸、重量、额定电压与容量因车型而异，官方未公开统一规格，已标注为“未公开”。