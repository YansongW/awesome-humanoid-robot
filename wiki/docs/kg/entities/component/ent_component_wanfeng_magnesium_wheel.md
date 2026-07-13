---
id: ent_component_wanfeng_magnesium_wheel
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 万丰奥威镁合金轮毂
  en: Wanfeng Magnesium Alloy Wheel
sources:
- id: src_wanfeng_official
  type: website
- title: 万丰奥威官网
  url: https://www.wanfeng.com.cn
- id: src_wanfeng_investor
  type: report
- title: 万丰奥威投资者关系活动记录
  url: https://www.jiemian.com/article/10821995.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from Wanfeng Auto Wheels company profile and investor
    relations materials; missing values marked as 未公开.
---


# 万丰奥威镁合金轮毂 / Wanfeng Magnesium Alloy Wheel

## 概述

万丰奥威镁合金轮毂是万丰奥威（Wanfeng Auto Wheels）汽车金属轻量化业务的重要产品，采用 AZ91D、AM60B 等镁合金材料，通过低压铸造或锻造工艺制成。相比传统铝合金轮毂，镁合金轮毂可实现 30% – 40% 的重量降低，同时具备优良的减振、散热与抗电磁干扰性能，广泛应用于高端乘用车、新能源汽车、赛车及特种车辆。万丰奥威旗下镁瑞丁（Meridian）是全球最大的镁合金压铸企业之一，为人形机器人镁合金结构件拓展提供了材料与工艺基础。

## 工作原理与技术架构

镁合金轮毂的核心优势源于镁合金材料特性：

1. **低密度**：镁合金密度约 1.8 g/cm³，仅为铝合金的 2/3、钢的 1/4，是实现轮毂轻量化的关键。
2. **高比强度 / 比刚度**：在相同重量下，镁合金可提供较高的刚度与强度，有助于降低簧下质量，提升操控响应与续航里程。
3. **优良减振性**：镁合金阻尼系数高于铝合金，可有效吸收路面振动，提高乘坐舒适性。
4. **良好散热性**：镁合金热导率较高，有助于制动系统散热。
5. **成形工艺**：采用低压铸造或锻造工艺，结合热处理、机加工与表面处理（涂装/钝化/微弧氧化）获得所需尺寸精度与耐腐蚀性能。

轮毂轻量化对车辆性能的影响可通过簧下质量加速度响应近似说明：

$$
a = \frac{F}{m}
$$

其中 $F$ 为路面激励力，$m$ 为簧下质量。降低 $m$ 可减小轮胎与路面接触力的波动，改善抓地力与舒适性。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 直径 | 14 inch – 22 inch（系列范围）| 万丰奥威产品手册 |
| 宽度 | 5.5 inch – 10.5 inch（系列范围）| 万丰奥威产品手册 |
| 材质 | AZ91D / AM60B | 万丰奥威产品手册 |
| 制造工艺 | 低压铸造 / 锻造 | 万丰奥威产品手册 |
| 重量优势 | 较铝合金轮毂轻 30% – 40% | 万丰奥威产品手册 |
| 表面处理 | 涂装 / 钝化 | 万丰奥威产品手册 |
| 载荷 | 依车型定制 | 万丰奥威产品手册 |
| 认证 | IATF 16949（汽车质量体系）| 万丰奥威年报 |
| 主要客户 | 特斯拉、奔驰、宝马、福特、比亚迪、蔚来等 | 万丰奥威年报 |
| 价格 | 未公开 | - |

## 应用场景

- **高端乘用车**：轻量化、高性能车型的轮毂配套。
- **新能源汽车**：降低簧下质量，提升续航与操控。
- **赛车与高性能车**：高比强度、良好散热满足极限工况。
- **特种车辆**：越野车、军用车辆等对减重与可靠性要求高的场景。
- **人形机器人结构件延伸**：万丰奥威依托镁瑞丁的大型镁合金压铸能力，向机器人关节壳体、足部支架等轻量化结构件拓展。

## 供应链关系

- **上游**：镁合金锭、铝合金锭、模具钢、压铸机、热处理设备、涂装材料。
- **制造商**：万丰奥威通过关系 `ent_company_wanfeng -- manufactures --> ent_component_wanfeng_magnesium_wheel` 记录于知识图谱。公司同时制造 `ent_component_wanfeng_magnesium_structure` 镁合金压铸结构件。
- **下游**：全球汽车主机厂（特斯拉、奔驰、宝马、福特、比亚迪、蔚来等）及机器人整机厂。主要竞争对手包括宝武镁业、云海金属、广东鸿图、文灶股份等。

## 来源与验证

轮毂直径、宽度、材质、工艺、重量优势及表面处理参数来自万丰奥威企业 Wiki 与投资者关系资料。主要客户与认证信息来自公司年报及机构调研记录。具体产品价格未公开。