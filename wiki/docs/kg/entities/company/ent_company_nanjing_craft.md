---
id: ent_company_nanjing_craft
schema_version: 1
type: company
'title:': Nanjing Craft Equipment Manufacturing
domain: 02_components
theoretical_depth: system
names:
  zh: 南京工艺装备制造
  en: Nanjing Craft Equipment Manufacturing
status: active
sources:
- id: src_nanjing_craft_official
  type: website
  url: https://www.njgy.com.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 南京工艺装备制造 / Nanjing Craft Equipment Manufacturing

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 南京工艺装备制造有限公司 |
| **英文名** | Nanjing Craft Equipment Manufacturing |
| **总部** | 中国江苏南京 |
| **成立时间** | 1952 |
| **官网** | [https://www.njgy.com.cn](https://www.njgy.com.cn) |
| **供应链环节** | 滚动功能部件 / 滚珠丝杠 / 直线导轨 / 行星滚柱丝杠 |
| **企业属性** | 国有改制企业、国内品牌 |
| **母公司/所属集团** | 南京新工投资集团 |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

## 公司简介

国内历史最悠久的滚动功能部件专业制造商之一，产品覆盖高端机床、机器人与自动化装备。

南京工艺装备制造有限公司前身为南京机床附件厂，长期专注滚珠丝杠副、滚动直线导轨副、行星滚柱丝杠副等滚动功能部件的研发与生产。公司拥有从原材料热处理、精密磨削到装配检测的完整工艺链，是国内高端丝杠导轨进口替代的重要供应商。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 滚珠丝杠副 | 标准/定制精密丝杠 | FFZD/DG 系列 | 机床、机器人 |
| 滚动直线导轨副 | 高刚性线性导轨 | GGB/GGC 系列 | 自动化、半导体 |
| 行星滚柱丝杠副 | 高负载线性传动 | 未公开型号 | 人形机器人 |
| 微型丝杠 | 小规格精密传动 | 未公开型号 | 医疗、电子 |

## 代表产品

### 滚珠丝杠副 / Ball Screw

> 滚珠丝杠副：请访问 [官方资料](https://www.njgy.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 丝杠直径 | Ø4–Ø200 mm | 产品手册 |
| 导程 | 1–50 mm | 产品手册 |
| 精度等级 | P1–P7 / C3–C10 | 产品手册 |
| 额定动载荷 | 未公开 | 产品手册 |
| 最大行程 | 依定制 | 产品手册 |
| 预紧方式 | 双螺母垫片预紧 / 单螺母变位 | 产品手册 |
| 材质 | 轴承钢 / 合金钢 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：全规格覆盖、磨制/轧制工艺兼备，可满足高精度机床与机器人批量需求。

**应用场景**：数控机床、人形机器人关节、半导体设备、自动化产线。

### 滚动直线导轨副 / Linear Guide

> 滚动直线导轨副：请访问 [官方资料](https://www.njgy.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 导轨宽度 | 15–65 mm | 产品手册 |
| 精度等级 | H / P / SP / UP | 产品手册 |
| 额定动载荷 | 未公开 | 产品手册 |
| 滑块型式 | 法兰型 / 四方型 | 产品手册 |
| 材质 | 轴承钢 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：高刚性、低摩擦、长寿命，可替代进口导轨应用于高端装备。

**应用场景**：自动化设备、机床、机器人直线模组、电子制造。

## 供应链位置

- **上游关键零部件/材料**：轴承钢、合金钢、润滑脂、砂轮、热处理服务、数控系统
- **下游客户/应用场景**：机床厂商、机器人 OEM、自动化集成商、半导体设备
- **主要竞争对手/对标**：THK、HIWIN、秦川机床、贝斯特、上银科技

## 知识图谱节点与关系

- 公司实体：`ent_company_nanjing_craft`
- 产品/零部件实体：`ent_component_nanjing_craft_ball_screw`, `ent_component_nanjing_craft_linear_guide`
- 关键关系：
  - `ent_company_nanjing_craft` -- `manufactures` --> `ent_component_nanjing_craft_ball_screw`
  - `ent_company_nanjing_craft` -- `manufactures` --> `ent_component_nanjing_craft_linear_guide`

## 参考资料

1. [南京工艺官网](https://www.njgy.com.cn)
2. [南京新工投资集团](http://www.njxg.com)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)