---
id: ent_component_nanjing_craft_linear_guide
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 南京工艺滚动直线导轨副
  en: Nanjing Craft Linear Guide
status: active
sources:
- id: src_nanjing_craft_linear_guide_pdf
  type: datasheet
- title: 南京工艺滚动直线导轨副产品手册
  url: https://download.s21i.co99.net/32350855/0/0/ABUIABA9GAAg3dHnwwYogLCCigQ.pdf?f=%E5%8D%97%E4%BA%AC%E5%B7%A5%E8%89%BA%E7%9B%B4%E7%BA%BF%E5%AF%BC%E8%BD%A8.pdf&v=1752819934
- id: src_nanjing_craft_official
  type: website
- title: 南京工艺装备制造股份有限公司官网
  url: https://www.njgy.com.cn
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自南京工艺公开产品手册；缺失值标注为“未公开”。
---


# 南京工艺滚动直线导轨副 / Nanjing Craft Linear Guide

## 概述

南京工艺滚动直线导轨副是南京工艺装备制造股份有限公司生产的滚动功能部件产品，涵盖 GGB（滚珠型）、GGC（微型）、GGD（滚柱重载型）等系列。公司前身为南京机床附件厂，是国内历史最悠久的滚动功能部件专业制造商之一，产品广泛应用于高端机床、半导体设备、自动化平台与人形机器人线性关节。

## 工作原理 / 技术架构

滚动直线导轨副通过滑块内滚珠或滚柱在导轨滚道上的滚动实现低摩擦直线导向。GGB 系列滚珠直线导轨采用四方向等载荷设计，滚道接触角约 45°，可同时承受径向、反向及横向载荷。

额定寿命 $L$ 与基本额定动载荷 $C$、当量动载荷 $P$ 的关系满足 ISO 14728-1/2：

$$
L = \left( \frac{C}{P} \right)^3 \times 100 \ \mathrm{km}
$$

该公式适用于滚珠型直线导轨。对于滚柱型导轨，寿命指数取 $10/3$。

## 关键参数表

| 参数 | 典型值 / 范围 | 备注 |
|------|--------------|------|
| 系列 | GGB（滚珠）/ GGC（微型）/ GGD（滚柱重载） | 产品手册 |
| 导轨宽度 | 15–100 mm（GGB 系列） | 产品手册 |
| 精度等级 | 2 / 3 / 4 / 5 级（GGB 系列） | 产品手册 |
| 预紧 | P / P1 等 | 产品手册 |
| 单根最大长度 | 4000–6000 mm（依系列） | 产品手册 |
| 额定动载荷 $C$ | 4.7–143 kN（GGB 系列，依规格） | 产品手册 |
| 额定静载荷 $C_0$ | 7.6–4255 kN（依规格） | 产品手册 |
| 材质 | 轴承钢 / 合金钢 | 产品手册 |
| 噪音 | 高速滚动直线导轨副 60 m/min 运行时 ≤ 68 dB | 公开报道 |
| 价格 | 未公开 | - |

## 应用场景

- 数控机床进给轴与定位平台
- 人形机器人线性关节与直线模组
- 半导体设备与电子制造
- 自动化产线与物流分拣
- 精密测量与光学平台

## 供应链关系

制造商为南京工艺装备制造有限公司（`ent_company_nanjing_craft`），隶属于南京新工投资集团。上游关键原材料包括轴承钢、合金钢、润滑脂、砂轮与热处理服务；下游客户包括机床厂商、机器人 OEM、自动化集成商与半导体设备商。知识图谱中的关键关系为：`ent_company_nanjing_craft` -- `manufactures` --> `ent_component_nanjing_craft_linear_guide`。

## 来源与验证

本卡片参数引自南京工艺滚动直线导轨副公开产品手册与官网。具体型号价格未公开。