---
id: ent_component_shuanghuan_shpr_40e_121
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: 双环传动 SHPR-40E-121 RV 减速器
  en: Shuanghuan Driveline SHPR-40E-121 RV Reducer
sources:
- id: src_shuanghuan_official
  type: website
- title: Shuanghuan Driveline Official Website
  url: http://www.shuanghuandrive.com
- id: src_sws_rv_reducer_report
  type: report
- title: 减速机：机器人零部件最大单品，“关节”定义仿生自由度
  url: https://wxweb.swsresearch.com/swsreport/2022_08/338728.pdf
- id: src_gys_shpr40e121
  type: product_page
- title: SHPR-40E-121 双环 RV 减速机产品页
  url: https://m.gys.cn/jiansuji/5145452402.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---


# 双环传动 SHPR-40E-121 RV 减速器 / Shuanghuan Driveline SHPR-40E-121 RV Reducer

## 概述

SHPR-40E-121 是双环传动（子公司环动科技）研制的 RV-E 系列主轴承内置型精密摆线减速器，减速比 121:1，额定扭矩 412 N·m。该产品采用两级减速结构（渐开线行星齿轮前级 + 摆线针轮后级），具有高刚性、强抗扭、背隙小等特点，是国产 RV 减速器的代表型号之一，已实现批量供货国内工业机器人与人形机器人企业。

## 工作原理 / 技术架构

SHPR-40E-121 为 planocentric（行星摆线）减速机构：

1. **第一级**：输入轴带动太阳轮，驱动 3 个行星轮同步公转，将运动传递给偏心曲柄轴。
2. **第二级**：曲柄轴驱动两片相位差 180° 的摆线轮做偏心运动，摆线轮齿廓与针齿壳内的圆柱针齿多齿啮合；由于摆线轮齿数比针齿少 1，曲柄轴每转一圈，摆线轮相对针齿壳反向转过一齿，实现大减速比。
3. **输出机构**：摆线轮的自转通过曲柄轴传递给输出盘（行星架），输出盘内置主轴承直接承受外部弯矩与轴向力。

总传动比：
$$i = i_1 \cdot i_2$$
其中 $i_1$ 为行星齿轮级减速比，$i_2 = \frac{Z_p}{Z_p - Z_c}$ 为摆线针轮级减速比，$Z_p$ 为针齿数，$Z_c$ 为摆线轮齿数。SHPR-40E-121 的名义传动比为 121:1。

输出扭矩与输入扭矩关系：
$$T_{out} = \eta \cdot i \cdot T_{in}$$
其中 $\eta$ 为传动效率（典型值 85%–95%）。

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 型号 | SHPR-40E-121 | 双环传动 / 环动科技 |
| 减速比 | 121:1 | 盖尔斯威 / 申万宏源研报 |
| 额定扭矩 | 412 N·m | 盖尔斯威 / 申万宏源研报 |
| 启动停止容许扭矩 | 1029 N·m | 同类产品参考 / 申万宏源研报 |
| 瞬时最大扭矩 | 约 2058 N·m | RV-40E 系列典型值 |
| 背隙 | ≤ 1 arcmin | 盖尔斯威产品页 |
| 传动精度 | ≤ 1 arcmin | 申万宏源研报 |
| 传动效率 | 85%–95% | 申万宏源研报 |
| 容许输出转速 | 约 70 rpm（100% 占空比） | 行业研报 |
| 扭转刚度 | 108 N·m/arcmin | 申万宏源研报 |
| 噪声 | < 75 dB(A) | 申万宏源研报 |
| 温升 | < 45 °C | 申万宏源研报 |
| 重量 | 未公开 | - |
| 额定寿命 | 6000 h（额定工况） | RV-E 系列典型值 |
| 结构特点 | 主轴承内置、同轴式、强抗扭刚度 | 盖尔斯威产品页 |

## 应用场景

- **六轴工业机器人 J1–J3 关节**：肩、腰、大臂等重载高刚性位置。
- **人形机器人腰/髋关节**：配合大扭矩无框电机实现高动态站立与行走。
- **重载变位机与转台**：利用高刚性输出与抗冲击能力。
- **焊接/切割机器人**：满足重载、高精度的轨迹控制需求。

## 供应链关系

- **制造商**：双环传动 Shuanghuan Driveline（ent_company_shuanghuan），子公司环动科技为实际生产主体。
- **上游关键物料**：合金钢（摆线轮、针齿壳）、轴承、润滑脂、齿轮毛坯。
- **下游整机集成**：宇树科技、埃斯顿、埃夫特、钱江机器人等；用于工业机器人与人形机器人重载关节。
- **竞争/对标**：Nabtesco RV-E 系列、中大力德 RVE/RVC、秦川机床、南通振康。

## 来源与验证

- 双环传动官网：http://www.shuanghuandrive.com
- 申万宏源《减速机：机器人零部件最大单品》：“关节”定义仿生自由度（2022-08）：https://wxweb.swsresearch.com/swsreport/2022_08/338728.pdf
- SHPR-40E-121 产品页：https://m.gys.cn/jiansuji/5145452402.html