---
id: ent_component_wittenstein_sp_plus
schema_version: 1
type: component
'title:': WITTENSTEIN alpha SP+ 行星减速器
domain: 02_components
theoretical_depth: system
names:
  zh: WITTENSTEIN alpha SP+ 行星减速器
  en: WITTENSTEIN alpha SP+ Planetary Gearbox
status: active
sources:
- id: src_wittenstein_wittenstein_sp_plus_official
  type: website
  url: https://www.wittenstein.de/en-en/products/servo-gearboxes/low-backlash-planetary-gearboxes/sp-planetary-gearbox/
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# WITTENSTEIN alpha SP+ 行星减速器 / WITTENSTEIN alpha SP+ Planetary Gearbox

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [威腾斯坦 / WITTENSTEIN alpha](../../../appendices/appendix-d/companies/company_wittenstein.md) |
| **产品类别** | 行星减速器 / 伺服减速器 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [威腾斯坦 官网](https://www.wittenstein.de) |

## 产品概述

SP+ 是 WITTENSTEIN alpha 经典的低背隙行星减速器系列，专为高定位精度与循环动态应用设计。采用螺旋行星齿轮、预紧圆锥滚子轴承和模块化电机接口，可提供从 48 N·m 到 5,700 N·m 的加速扭矩范围。

该系列提供标准（MF）版本，减速比 3–100，7 种尺寸，可选降低背隙版本。SP+ HIGH SPEED 与 MC-L 低摩擦版本进一步覆盖连续运行与高速场景，是机床、机器人与自动化产线的核心传动部件。

## 产品图片

> WITTENSTEIN alpha SP+ 行星减速器 / WITTENSTEIN alpha SP+ Planetary Gearbox：请访问 [官方资料](https://www.wittenstein.de/en-en/products/servo-gearboxes/low-backlash-planetary-gearboxes/sp-planetary-gearbox/) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 减速比 | 3:1 – 100:1 | 产品手册 |
| 框号/尺寸 | 7 种尺寸（MF） | 产品手册 |
| 最大输出扭矩 | 48 – 5,700 N·m | 产品手册 |
| 最大输入转速 | 最高 8,500 rpm | 产品手册 |
| 背隙 | 标准 ≤3 arcmin / 降低 ≤1 arcmin | 产品手册 |
| 扭转刚度 | 550 N·m/arcmin | 产品手册 |
| 最大倾覆力矩 | 5,000 N·m | 产品手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[威腾斯坦 / WITTENSTEIN alpha](../../../appendices/appendix-d/companies/company_wittenstein.md)
- **核心零部件/技术来源**：高强度合金钢齿轮、精密轴承、密封件、润滑脂、电机适配法兰
- **下游应用/客户**：工业机器人、人形机器人关节、数控机床、包装与医疗设备制造商

## 知识图谱节点与关系

- 零部件实体：`ent_component_wittenstein_sp_plus`
- 制造商实体：`ent_company_wittenstein`
- 关键关系：
  - `rel_ent_company_wittenstein_manufactures_ent_component_wittenstein_sp_plus`（`ent_company_wittenstein` --> `manufactures` --> `ent_component_wittenstein_sp_plus`）

## 应用场景

- **工业机器人**：六轴机器人腕部、肩部关节的高精度减速
- **人形机器人**：手臂、腿部旋转关节传动
- **数控机床**：机床进给轴、刀库、转台定位
- **其他自动化**：包装机械、印刷设备、医疗定位平台

## 竞争对比

| 对比项 | SP+ 行星减速器 | Neugart PLN | STOBER P |
|--------|------------------------|---------------|---------------|
| 核心优势 | 德国高端螺旋齿、恒定低背隙 | 高精度直齿、PLN 标准 | 模块化 helical 行星 |
| 背隙/精度 | ≤1–3 arcmin | ≤1–3 arcmin | 1–4 arcmin |
| 价格水平 | 高端 | 高端 | 中高端 |
| 交付周期 | 中等 | 中等 | 中等 |

## 选购与部署建议

根据循环次数、峰值扭矩与安装空间选择尺寸；高动态机器人关节建议选用降低背隙版本，并配合 alpha 选型软件 cymex® 校核寿命。

## 参考资料

1. [威腾斯坦 官网](https://www.wittenstein.de)
2. [WITTENSTEIN alpha SP+ Planetary Gearbox](https://www.wittenstein.de/en-en/products/servo-gearboxes/low-backlash-planetary-gearboxes/sp-planetary-gearbox/)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)