---
id: ent_component_nabtesco_rv_20e_81
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: Nabtesco RV-20E-81 精密摆线减速器
  en: Nabtesco RV-20E-81 Precision Cycloidal Reducer
sources:
- id: src_nabtesco_rv_catalog
  type: datasheet
- title: Nabtesco RV Series Full Catalog
  url: https://s3.amazonaws.com/www.motionusa.com/nabtesco/RV_Series_Full_Catalog.pdf
- id: src_nabtesco_de_catalog
  type: datasheet
- title: Precision Reduction Gear RV Catalog
  url: https://www.nabtesco.de/fileadmin/04_Service/05_Downloads/01_Produktkataloge/RV_Katalog_EN.pdf
- id: src_nabtesco_official
  type: website
- title: Nabtesco Motion Control Official Website
  url: https://www.nabtesco-motion.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---


# Nabtesco RV-20E-81 精密摆线减速器 / Nabtesco RV-20E-81 Precision Cycloidal Reducer

## 概述

Nabtesco RV-20E-81 是日本纳博特斯克 RV-E 系列中小型精密摆线减速器，外径约 65 mm，减速比 81:1，额定扭矩 167 N·m。作为工业机器人关节的标准减速器之一，RV-20E-81 以高刚性、低背隙（< 1 arc-min）、强抗冲击和长寿命著称，广泛用于 SCARA、小型六轴机器人、人形机器人腿部关节及 CNC 转台。

## 工作原理 / 技术架构

RV-20E-81 采用 Nabtesco 专利的两级 planocentric 减速结构：

1. **第一级**：输入齿轮与 3 个行星齿轮啮合，驱动与行星齿轮固连的曲柄轴。
2. **第二级**：曲柄轴带动两片相位差 180° 的 RV 齿轮（摆线轮）做偏心运动；RV 齿轮齿廓与针齿壳内圆柱针齿多齿同时啮合。
3. **输出**：由于 RV 齿轮齿数比针齿少 1，曲柄轴旋转一周时 RV 齿轮相对针齿壳反向转过一个齿距，经曲柄轴将运动传递给输出盘。

传动比：
$$i = \frac{Z_p}{Z_p - Z_c} \cdot i_{first-stage}$$
RV-20E-81 的名义减速比为 81:1。

输出扭矩与效率关系：
$$T_{out} = \eta \cdot i \cdot T_{in}$$
典型效率 $\eta$ > 85%。

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 型号 | RV-20E-81 | Nabtesco |
| 外径 | 约 65 mm | Nabtesco RV-E 手册 |
| 重量 | 约 4.7 kg | Nabtesco 参数表 |
| 减速比 | 81:1 | Nabtesco 产品页 |
| 额定扭矩 | 167 N·m | Nabtesco 产品页 |
| 启动停止容许扭矩 | 412 N·m | Nabtesco 产品页 |
| 瞬时最大扭矩 | 833 N·m | Nabtesco 产品页 |
| 容许输出转速 | 75 rpm（100% 占空比） | Nabtesco 产品页 |
| 背隙 | < 1 arc-min | Nabtesco 产品页 |
| 额定寿命 | 6000 h（额定工况） | Nabtesco 产品页 |
| 传动效率 | > 85% | 行业公开资料 |
| 结构 | 主轴承内置、两级摆线行星 | Nabtesco 目录 |

## 应用场景

- **SCARA 机器人**：末端 J4 关节或轻载 J1–J2 关节。
- **小型六轴工业机器人**：腕部、小臂等中低负载关节。
- **人形机器人腿部关节**：膝、踝等部位，配合无框力矩电机使用。
- **CNC 转台与精密分度**：利用低背隙与高刚性保证重复定位精度。

## 供应链关系

- **制造商**：Nabtesco（ent_company_nabtesco），日本精密减速器龙头。
- **上游关键物料**：合金钢、摆线轮、针齿壳、轴承、润滑脂。
- **下游整机集成**：全球工业机器人四大家族、国产机器人、人形机器人 OEM。
- **竞争/对标**：双环传动 SHPR 系列、中大力德 RVE/RVC、住友重机械、南通振康。

## 来源与验证

- Nabtesco RV Series Full Catalog：https://s3.amazonaws.com/www.motionusa.com/nabtesco/RV_Series_Full_Catalog.pdf
- Nabtesco Precision Reduction Gear RV Catalog：https://www.nabtesco.de/fileadmin/04_Service/05_Downloads/01_Produktkataloge/RV_Katalog_EN.pdf
- Nabtesco 中国官网：https://www.nabtesco-motion.cn