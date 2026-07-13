---
id: ent_component_nidec_coreless_motor
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 日本电产空心杯电机
  en: Nidec Coreless Motor
status: active
sources:
- id: src_nidec_coreless
  type: website
  url: https://www.nidec.com/en/nidec-precision/product/search/category/B101/M104/S100/
- id: src_nidec_company
  type: website
  url: https://www.nidec.com/en/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 日本电产空心杯电机 / Nidec Coreless Motor

## 概述

日本电产（Nidec）空心杯电机是一种转子无铁芯的永磁直流电机，分为有刷与无刷两类。其无铁芯结构消除了齿槽转矩，具有低转动惯量、高加速度、高效率与低噪声等特点，特别适合机器人手指、医疗手持器械、无人机云台等对体积和动态响应要求高的场景。

## 工作原理 / 技术架构

电机由永磁定子与空心杯形线圈转子组成。通电后线圈在磁场中受安培力作用旋转；无刷版本通过霍尔传感器或编码器实现电子换向。电机的基本电磁关系为
\[
T=K_t I,
\]
\[
E=K_e \omega,
\]
\[
P=T\omega,
\]
其中 \(T\) 为电磁转矩，\(K_t\) 为转矩常数，\(I\) 为电枢电流，\(E\) 为反电动势，\(K_e\) 为反电动势常数，\(\omega\) 为角速度，\(P\) 为机械输出功率。

## 关键参数表

| 规格项 | 数值（系列范围/示例） | 备注/来源 |
|--------|----------------------|-----------|
| 产品类型 | 空心杯有刷/无刷直流电机 | Nidec |
| 直径范围 | Φ8–Φ35 mm（系列） | 附录 D |
| 重量 | 2–80 g（依型号） | 附录 D |
| 额定电压 | 6–48 VDC | 附录 D |
| 额定转速 | 5,000–20,000 rpm | 附录 D |
| 额定扭矩 | 0.5–60 mNm | 附录 D |
| 效率 | ≥85% | 附录 D |
| 换向反馈 | Hall / 编码器可选 | 附录 D |
| 示例 LS12-003 | DC，Φ12 mm，长 25.9 mm，2–8.2 V，空载 28,300 rpm | Nidec 产品页 |
| 工作温度 | -20 °C ~ +65 °C（典型） | Nidec 产品页 |

## 应用场景

- 人形机器人灵巧手驱动
- 医疗手持器械与精密光学调焦
- 无人机云台与微型机械臂
- 微型泵阀与触觉执行器

## 供应链关系

日本电产株式会社（`ent_company_nidec`）制造空心杯电机。上游依赖稀土永磁体、铜线、轴承、驱动 IC 与结构件；下游为机器人、汽车、医疗与消费电子整机厂。在知识图谱中，`ent_company_nidec` 通过 `manufactures` 关系指向 `ent_component_nidec_coreless_motor`，该电机常用于机器人末端执行器的小型驱动关节。

## 来源与验证

- [NIDEC Coreless Motors Product Search](https://www.nidec.com/en/nidec-precision/product/search/category/B101/M104/S100/)
- [NIDEC Corporation Official](https://www.nidec.com/en/)
- [附录 D - Nidec Company Wiki](../../../appendices/appendix-d/companies/company_nidec.md)