---
id: ent_company_byd
type: company
'title:': BYD / 比亚迪
domain: 02_components
theoretical_depth: system
aliases:
- 比亚迪
- BYD Company
status: active
created_at: 2026-07-01 00:00:00+00:00
updated_at: 2026-07-09 00:00:00+00:00
sources:
- id: byd_official
  type: website
  url: https://www.byd.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-09 00:00:00+00:00
---





# byd

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 比亚迪股份有限公司 |
| **英文名** | BYD Company Limited |
| **总部** | 中国广东省深圳市 |
| **成立时间** | 1995 年 |
| **官网** | [https://www.byd.com](https://www.byd.com) |
| **供应链环节** | 动力电池、储能电池、新能源汽车、电子代工 |
| **企业属性** | 上市公司（深交所：002594 / 港交所：1211） |
| **母公司/所属集团** | 无（独立上市） |
| **数据来源** | 公司官网、Fraunhofer IKTS 拆解研究、公开技术资料 |

## 公司简介

比亚迪是全球领先的新能源整体解决方案提供商，业务横跨汽车、轨道交通、新能源和电子四大产业。

其子公司弗迪电池（FinDreams Battery）生产的刀片电池（Blade Battery）采用磷酸铁锂（LFP）化学体系，通过“Cell-to-Pack”无模组结构提升空间利用率与安全性能。刀片电池已广泛应用于比亚迪自有车型，并开始外供丰田等合作伙伴。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 动力电池 | 高安全 LFP 电池包 | 刀片电池（Blade Battery） | 乘用车、商用车、机器人平台 |
| 储能电池 | 电网级储能系统 | BYD B-Box / Cube | 工商业与户用储能 |
| 汽车电子 | 电机、电控、BMS | 八合一电动力总成 | 新能源汽车 |

## 代表产品

### 刀片电池（BYD Blade Battery）

![刀片电池](https://www.byd.com/en/news-list/20200329-the-blade-battery)


| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 电芯尺寸 | 960 mm × 90 mm × 12 mm（示例） | BatteryDesign 拆解资料 |
| 电芯重量 | 约 2.63 kg（138 Ah 版本） | BatteryDesign 拆解资料 |
| 化学体系 | 磷酸铁锂（LFP） | BYD 官网 |
| 标称电压 | 3.2 V | BYD 官网 |
| 电芯容量 | 138 Ah / 202 Ah 等 | 公开拆解资料 |
| 能量密度 | 约 160–169.6 Wh/kg（电芯级） | Fraunhofer IKTS / Evlithium |
| 循环寿命 | ≥3000 次 | BYD 官网 |
| 价格 | 未公开 | 未公开 |

**技术亮点**：长条形叠片 LFP 电芯直接成组，无模组化设计提升体积利用率；通过针刺测试不起火，强调本征安全。

**应用场景**：新能源汽车底盘、储能集装箱、对安全敏感的人形机器人电池方案。

## 与人形机器人的关联

- 电池、功率半导体与先进材料是人形机器人实现长续航、高动态与轻量化的共性基础。
- 工业机器人与自动化产线为人形机器人整机装配、测试与量产提供可复用的制造能力。

## 供应链位置

- **上游关键零部件/材料**：磷酸铁锂正极、石墨负极、隔膜、电解液、结构件。
- **下游客户/应用场景**：比亚迪汽车、丰田（bZ3 等合作项目）、储能集成商。
- **主要竞争对手/对标**：CATL、国轩高科、亿纬锂能、LG Energy Solution。

## 知识图谱节点与关系

- 公司实体：`ent_company_byd`
- 产品实体：`ent_component_byd_blade_battery`
- 关键关系：
  - `ent_company_byd` -- `manufactures` --> `ent_component_byd_blade_battery`
  - `ent_company_byd` -- `supplies` --> `ent_company_toyota`

## 参考资料

1. [BYD 官网](https://www.byd.com)
2. [BYD Blade Battery 官方介绍](https://www.byd.com/en/news-list/20200329-the-blade-battery)
3. [BatteryDesign BYD Blade 拆解](https://www.batterydesign.net/byd-blade/)