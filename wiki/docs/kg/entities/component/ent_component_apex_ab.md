---
id: ent_component_apex_ab
schema_version: 1
type: component
'title:': Apex Dynamics AB 系列高精度行星减速器
domain: 02_components
theoretical_depth: system
names:
  zh: Apex Dynamics AB 系列高精度行星减速器
  en: Apex Dynamics AB Series Planetary Gearbox
status: active
sources:
- id: src_apex_dynamics_apex_ab_official
  type: website
  url: https://www.apexdynamicsusa.com/ab-series-high-precision-planetary-gearboxes.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# Apex Dynamics AB 系列高精度行星减速器 / Apex Dynamics AB Series Planetary Gearbox

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [精锐科技（Apex Dynamics） / Apex Dynamics](../../../appendices/appendix-d/companies/company_apex_dynamics.md) |
| **产品类别** | 高精度行星减速器 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [精锐科技（Apex Dynamics） 官网](https://www.apexdynamics.com) |

## 产品概述

Apex Dynamics AB 系列采用 100% 优化螺旋齿轮和跨装高精度轴承，提供 1 级 3–10 和 2 级 12–100 的减速比。框号从 AB042 到 AB220，额定输出扭矩 14–2,000 N·m，背隙可选 P0 ≤1 arcmin、P1 ≤3 arcmin、P2 ≤5 arcmin（1 级）。

AB 系列防护等级 IP65，工作温度 -10 °C 至 +90 °C，输出法兰符合 ISO 9409-1，可直接安装转盘或机械臂末端，广泛应用于 CNC、机器人、半导体和医疗领域。

## 产品图片

> Apex Dynamics AB 系列高精度行星减速器 / Apex Dynamics AB Series Planetary Gearbox：请访问 [官方资料](https://www.apexdynamicsusa.com/ab-series-high-precision-planetary-gearboxes.html) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 减速比 | 1 级 3–10；2 级 12–100 | 产品手册 |
| 框号尺寸 | AB042 / 060 / 090 / 115 / 142 / 180 / 220 | 产品手册 |
| 额定输出扭矩 | 14 – 2,000 N·m | 产品手册 |
| 背隙 | P0 ≤1 / P1 ≤3 / P2 ≤5 arcmin（1 级） | 产品手册 |
| 效率 | 1 级 ≥97%；2 级 ≥94% | 产品手册 |
| 防护等级 | IP65 | 产品手册 |
| 工作温度 | -10 °C – +90 °C | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[精锐科技（Apex Dynamics） / Apex Dynamics](../../../appendices/appendix-d/companies/company_apex_dynamics.md)
- **核心零部件/技术来源**：螺旋齿轮、高精度轴承、密封件、润滑脂、ISO 9409-1 法兰、铝/不锈钢箱体
- **下游应用/客户**：CNC 机床、工业机器人、人形机器人、半导体、医疗设备

## 知识图谱节点与关系

- 零部件实体：`ent_component_apex_ab`
- 制造商实体：`ent_company_apex_dynamics`
- 关键关系：
  - `rel_ent_company_apex_dynamics_manufactures_ent_component_apex_ab`（`ent_company_apex_dynamics` --> `manufactures` --> `ent_component_apex_ab`）

## 应用场景

- **工业机器人**：机器人肩部、腕部、转台
- **人形机器人**：手臂、腿部旋转关节
- **数控机床**：CNC 进给轴、刀库、第四/五轴转台
- **其他自动化**：半导体搬运、医疗定位、包装机械

## 竞争对比

| 对比项 | AB 系列行星减速器 | Neugart PLN | Wittenstein SP+ |
|--------|------------------------|---------------|---------------|
| 核心优势 | 高性价比 helical、台湾制造 | 高精度直齿 | 德国高端螺旋齿 |
| 背隙/精度 | ≤1–5 arcmin | <1–3 arcmin | ≤1–3 arcmin |
| 价格水平 | 中高端 | 高端 | 高端 |
| 交付周期 | 较短 | 中等 | 中等 |

## 选购与部署建议

根据精度等级（P0/P1/P2）与扭矩选择框号；机器人关节建议 P1 及以上，并校核倾覆力矩。

## 参考资料

1. [精锐科技（Apex Dynamics） 官网](https://www.apexdynamics.com)
2. [Apex Dynamics AB Series High Precision Planetary Gearboxes](https://www.apexdynamicsusa.com/ab-series-high-precision-planetary-gearboxes.html)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)