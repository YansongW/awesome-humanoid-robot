---
id: ent_company_deep_robotics
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 云深处科技
  en: DEEPRobotics
status: active
sources:
- id: src_deep_robotics_official
  type: website
  url: https://www.deeprobotics.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 云深处科技 / DEEPRobotics

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 云深处科技 |
| **英文名** | DEEPRobotics |
| **总部** | 中国杭州 |
| **成立时间** | 2017 年 |
| **官网** | [https://www.deeprobotics.cn](https://www.deeprobotics.cn) |
| **供应链环节** | 整机 OEM / 四足机器人 + 人形机器人、关节模组 |
| **企业属性** | 电力巡检龙头、特种环境足式机器人 |
| **母公司/所属集团** | 无 |
| **数据来源** | 云深处官网、公开报道、近 30 家具身公司业务梳理 |

## 公司简介

云深处科技是中国四足机器人商业化的先行者，“绝影”系列已广泛应用于电力巡检、应急救援、管廊隧道等场景。

2024 年起公司进军人形机器人领域，提出“极端环境足式与人形机器人一体化解决方案”，并推出 J 系列关节模组与山猫 M20 轮足机器人。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 行业级四足 | 防爆、全地形巡检 | 绝影 X20 / X30 | 电力、消防、管廊 |
| 教育科研四足 | 轻量化、可二次开发 | 绝影 Lite3 | 教育、科研 |
| 轮足/人形 | 多形态移动操作 | 山猫 M20 / DR01 / DR02 | 工业、救援 |

## 代表产品

### 绝影 X30

> 云深处 绝影 X30：请访问 [官方资料](https://www.deeprobotics.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 100 × 69.5 × 47 cm | 电池行业公开资料 |
| 重量 | 约 56 kg | 电池行业公开资料 |
| 自由度 | 未公开 | - |
| 负载/扭矩 | 负载约 15 kg | 行业分析报告 |
| 速度/转速 | 可攀爬 45° 斜坡 / 楼梯 | 云深处官网 / 行业报道 |
| 续航 | 2.5–4 h（行业资料）；另有 8 h 报道 | 不同场景配置差异 |
| 接口/通信 | 未公开 | - |
| 价格 | 未公开 | 需询价 |

**技术亮点**：IP67/IP68 防护、-20 °C 至 55 °C 工作温度、双光云台、多传感器融合导航。

**应用场景**：变电站巡检、消防救援、地下管廊、金属冶炼。

### 绝影 Lite3

> 云深处 绝影 Lite3：请访问 [官方资料](https://www.deeprobotics.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 未公开 | - |
| 重量 | 未公开 | - |
| 自由度 | 未公开 | - |
| 负载/扭矩 | 未公开 | - |
| 速度/转速 | 未公开 | - |
| 续航 | 约 4 h | 行业分析报告 |
| 接口/通信 | 支持二次开发 | 云深处官网 |
| 价格 | 未公开 | 需询价 |

**技术亮点**：轻量化设计、关节扭矩提升 50%、算力提升 3 倍、模块化拓展。

**应用场景**：教育科研、巡检算法验证、开发者社区。

## 供应链位置

- **上游关键零部件/材料**：自研 J60/J80/J100 关节模组，外购电机、减速器、电池、激光雷达、云台。
- **下游客户/应用场景**：国家电网、南方电网、新加坡电网、应急救援单位。
- **主要竞争对手/对标**：宇树 B2、波士顿动力 Spot、ANYbotics ANYmal。

## 知识图谱节点与关系

- 公司实体：`ent_company_deep_robotics`
- 产品实体：`ent_product_deep_robotics_x30`、`ent_product_deep_robotics_lite3`
- 关键关系：
  - `ent_company_deep_robotics` -- `manufactures` --> `ent_product_deep_robotics_x30`
  - `ent_company_deep_robotics` -- `manufactures` --> `ent_product_deep_robotics_lite3`
  - `ent_product_deep_robotics_x30` -- `uses` --> `ent_component_deep_robotics_j_series_joint`

## 参考资料

1. [云深处科技官网](https://www.deeprobotics.cn)
2. [云深处行业应用页](https://www.deeprobotics.cn/robot/index/industry.html)
3. [格瑞普电池 – 主流机器人动力电池解析](https://www.grepow.cn/hyxw/ysyscxmwlzljqrdc.html)
4. [Reportify – 近 30 家具身公司业务一览](https://reportify.cn/social-media/690201058833550)
5. [附录 D.4 重点产品 Wiki](../../../appendices/appendix-d/index-products.md)