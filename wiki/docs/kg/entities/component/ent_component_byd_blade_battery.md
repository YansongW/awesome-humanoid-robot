---
id: ent_component_byd_blade_battery
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 比亚迪刀片电池
  en: BYD Blade Battery
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-13 00:00:00+00:00
sources:
- id: src_byd_blade_release
  type: press_release
- title: BYD Blade Battery Official Release
  url: https://www.byd.com/en/news-list/20200329-the-blade-battery
- id: src_byd_blade_batterydesign
  type: website
- title: BatteryDesign BYD Blade Battery Teardown
  url: https://www.batterydesign.net/byd-blade/
- id: src_byd_global
  type: website
- title: BYD Global Blade Battery Technology
  url: https://www.bydglobal.com/cn/news/2020-03-29/1514436215678
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自 BYD 官方发布资料与公开拆解研究；缺失值标注为“未公开”。
---


# 比亚迪刀片电池 / BYD Blade Battery

## 概述

比亚迪刀片电池（BYD Blade Battery）是弗迪电池生产的磷酸铁锂（LFP）动力电池，采用 Cell-to-Pack（CTP）无模组结构，电芯呈长条形“刀片”状直接成组。该设计显著提升了电池包体积利用率与安全性能，已广泛应用于比亚迪新能源汽车，并开始外供丰田等合作伙伴。

## 工作原理 / 技术架构

刀片电池基于磷酸铁锂正极与石墨负极的锂离子嵌入/脱嵌反应。单电芯储能 $E$ 与容量 $Q$、标称电压 $V$ 的关系为

$$
E = Q \cdot V
$$

以 202 Ah 电芯为例，标称电压 3.2 V，则单电芯储能为

$$
E = 202 \ \mathrm{Ah} \times 3.2 \ \mathrm{V} = 646.4 \ \mathrm{Wh}
$$

质量能量密度 $\rho_m$ 与体积能量密度 $\rho_v$ 分别为

$$
\rho_m = \frac{E}{m} \approx \frac{646.4 \ \mathrm{Wh}}{3.92 \ \mathrm{kg}} \approx 165 \ \mathrm{Wh/kg}
$$

$$
\rho_v = \frac{E}{V} \approx \frac{646.4 \ \mathrm{Wh}}{1.44 \ \mathrm{L}} \approx 448 \ \mathrm{Wh/L}
$$

刀片电池通过无模组化设计将体积利用率提升约 50%，并在针刺试验中实现无明火、无烟、表面温度 30–60 ℃，展现了优异的本征安全性。

## 关键参数表

| 参数 | 典型值 | 备注 |
|------|--------|------|
| 化学体系 | 磷酸铁锂（LFP） | BYD 官方 |
| 电芯尺寸 | 905 mm × 118 mm × 13.5 mm（202 Ah 型） | 拆解资料 |
| 电芯重量 | 约 3.92 kg（202 Ah 型） | 估算 |
| 标称电压 | 3.2 V | BYD 官方 |
| 电芯容量 | 138 Ah / 202 Ah 等 | 公开资料 |
| 单电芯能量 | 646.4 Wh（202 Ah 型） | 计算 |
| 质量能量密度 | 约 160–169.6 Wh/kg（电芯级） | Fraunhofer IKTS / Evlithium |
| 体积能量密度 | 约 448 Wh/L（电芯级） | 拆解资料 |
| 循环寿命 | ≥ 3000 次（部分报道 ≥ 5000 次） | BYD 官方/报道 |
| 针刺测试 | 无明火、无烟、表面温度 30–60 ℃ | 官方测试 |
| 最大承受力 | 445 kN（约 45 吨卡车碾压） | BYD 官方 |
| 充电 | 10%–80% SOC 约 33 分钟（一代） | BYD 官方 |
| 价格 | 未公开 | - |

## 应用场景

- 新能源汽车底盘动力电池包
- 电动商用车与储能集装箱
- 对安全敏感的人形机器人电池方案
- 电网级工商业与户用储能

## 供应链关系

制造商为比亚迪股份有限公司（`ent_company_byd`），由子公司弗迪电池生产。上游关键原材料包括磷酸铁锂正极、石墨负极、隔膜、电解液与结构件；下游客户包括比亚迪自有车型、丰田等合作伙伴、储能集成商与机器人平台。知识图谱中的关键关系为：`ent_company_byd` -- `manufactures` --> `ent_component_byd_blade_battery`。

## 来源与验证

本卡片参数引自 BYD 官方刀片电池发布资料、BatteryDesign 拆解报告及 Fraunhofer IKTS 研究。批量价格、部分二代刀片电池细节未公开。