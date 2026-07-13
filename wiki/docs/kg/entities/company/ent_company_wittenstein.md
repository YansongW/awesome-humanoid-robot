---
id: ent_company_wittenstein
schema_version: 1
type: company
'title:': WITTENSTEIN alpha
domain: 02_components
theoretical_depth: system
names:
  zh: 威腾斯坦
  en: WITTENSTEIN alpha
status: active
sources:
- id: src_wittenstein_official
  type: website
  url: https://www.wittenstein.de
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 威腾斯坦 / WITTENSTEIN alpha

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 威腾斯坦 |
| **英文名** | WITTENSTEIN alpha |
| **总部** | 德国伊格斯海姆（Igersheim） |
| **成立时间** | 1949 |
| **官网** | [https://www.wittenstein.de](https://www.wittenstein.de) |
| **供应链环节** | 精密减速器 / 伺服执行器 / 机电驱动系统 |
| **企业属性** | 家族企业、国际品牌 |
| **母公司/所属集团** | WITTENSTEIN SE（独立家族企业） |
| **数据来源** | 官网、产品手册、WAIC 2026 报道 |

## 公司简介

WITTENSTEIN alpha 是德国 WITTENSTEIN SE 旗下专注于精密伺服减速器与机电执行器的高端品牌。凭借低背隙行星减速器、高刚性轴承与模块化电机接口，alpha 产品广泛应用于高动态、高精度的运动控制场合。

公司提供 SP+、TP+、XP+、NPL、CPS 等系列行星减速器，以及 Servo Actuator 机电执行器和 rack/pinion 线性系统。其工程工具 cymex® 支持驱动系统选型与寿命计算。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 行星减速器 | 低背隙/高刚性 | SP+ / TP+ / XP+ | 机床、机器人 |
| 机电执行器 | 一体化直线/旋转驱动 | Servo Actuator | 医疗、自动化 |
| 线性传动系统 | 齿条/小齿轮/齿轮箱 | alpha Rack & Pinion | 龙门、机器人 |

## 代表产品

### SP+ 低背隙行星减速器

> SP+ 低背隙行星减速器：请访问 [官方资料](https://www.wittenstein.de) 查看。

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

**技术亮点**：螺旋齿、恒定低背隙、高扭矩密度、圆锥滚子轴承承受轴向/径向载荷、多种输出形式。

**应用场景**：工业机器人关节、人形机器人关节、机床进给轴、包装机械、医疗设备。

### 其他代表产品

TP+ HIGH TORQUE 系列：减速比 22–302.5，最大扭矩 315–22,000 N·m，适用于高刚性定位；alpha Servo Actuator 一体化执行器用于直线/旋转运动。

## 供应链位置

- **上游关键零部件/材料**：高强度合金钢、精密轴承、特种润滑脂、电机、传感器
- **下游客户/应用场景**：机床 OEM、工业机器人、人形机器人整机厂、医疗与包装设备商
- **主要竞争对手/对标**：Neugart、STOBER、Apex Dynamics、Harmonic Drive、Nabtesco

## 知识图谱节点与关系

- 公司实体：`ent_company_wittenstein`
- 零部件实体：`ent_component_wittenstein_sp_plus`
- 关键关系：
  - `ent_company_wittenstein` -- `manufactures` --> `ent_component_wittenstein_sp_plus`

## 参考资料

1. [威腾斯坦 官网](https://www.wittenstein.de)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [WITTENSTEIN alpha SP+ 技术数据](https://alpha.wittenstein.de/en-en/products/sp-planetary-gearbox/)