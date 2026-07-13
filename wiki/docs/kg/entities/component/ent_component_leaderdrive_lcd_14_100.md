---
id: ent_component_leaderdrive_lcd_14_100
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
status: active
names:
  zh: 绿的谐波 LCD-14-100 超薄谐波减速器
  en: Leaderdrive LCD-14-100 Ultra-thin Harmonic Reducer
sources:
- id: src_leaderdrive_official
  type: website
- title: Leaderdrive Official Website
  url: https://www.leaderdrive.com
- id: src_sipgears_lcd
  type: product_page
- title: 谐波减速器 LCD 系列 - 苏州盖尔斯威
  url: http://www.sipgears.com/Products-10602467.html
- id: src_dfcfw_harmonic_report
  type: report
- title: 绿的谐波公司公告 / 东方财富研报
  url: https://pdf.dfcfw.com/pdf/H3_AP202403191627111620_1.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---


# 绿的谐波 LCD-14-100 超薄谐波减速器 / Leaderdrive LCD-14-100 Ultra-thin Harmonic Reducer

## 概述

绿的谐波 LCD-14-100 是 LCD 系列超薄杯状谐波减速器，减速比 100:1，额定扭矩（输入转速 2000 rpm 时）5.1 N·m。LCD 系列柔轮为薄壁杯状结构，整机采用超扁平设计，内置高刚性十字交叉滚子轴承直接承载外部负载，具有体积小、重量轻、轴向尺寸短的特点，是国产谐波减速器中面向机器人末端、人形机器人腕部/手指关节的代表型号。

## 工作原理 / 技术架构

谐波减速器由波发生器（Wave Generator）、柔轮（Flexspline）和刚轮（Circular Spline）组成：

1. **波发生器**：椭圆凸轮与柔性轴承组成，安装于柔轮内部，使柔轮产生可控椭圆变形。
2. **柔轮**：薄壁外齿圈，变形后长轴两端齿与刚轮内齿啮合，短轴方向脱啮。
3. **刚轮**：刚性内齿圈，齿数比柔轮多 2（双波传动）。

波发生器旋转时，柔轮与刚轮的啮合区域随之转动；由于齿数差，柔轮相对刚轮低速反向旋转。减速比：
$$i = \frac{Z_{cs}}{Z_{cs} - Z_{fs}}$$
对于 LCD-14-100，$i = 100:1$。

输出扭矩：
$$T_{out} = \eta \cdot i \cdot T_{in}$$
谐波减速器典型效率 75%–90%。

## 关键参数表

| 参数 | 数值 | 备注/来源 |
|------|------|-----------|
| 型号 | LCD-14-100 | 绿的谐波产品手册 |
| 规格 | 14（柔轮节圆直径约 35 mm） | 绿的谐波 |
| 减速比 | 100:1 | 绿的谐波产品手册 |
| 额定扭矩（2000 rpm） | 5.1 N·m | 绿的谐波产品手册 |
| 启动停止容许扭矩 | 18 N·m | 绿的谐波产品手册 |
| 瞬时最大扭矩 | 33 N·m | 绿的谐波产品手册 |
| 最高输入转速 | 6000 rpm | 绿的谐波产品手册 |
| 平均输入转速 | 3500 rpm | 绿的谐波产品手册 |
| 背隙 | ≤ 20 arcsec | 绿的谐波产品手册 |
| 重量 | 0.68 kg（100 比） | 绿的谐波产品手册 |
| 结构 | 超薄杯状柔轮、内置交叉滚子轴承 | 绿的谐波 |
| 设计寿命 | > 10000 h | 行业公开资料 |

## 应用场景

- **协作机器人末端**：腕部、手指关节，需要超薄、轻量、高精度的减速传动。
- **人形机器人腕部/手指**：利用小体积、低重量实现高自由度末端。
- **医疗机器人**：手术机器人末端精密旋转与夹持。
- **3C 自动化**：小负载、高节拍装配与检测。

## 供应链关系

- **制造商**：绿的谐波 Leaderdrive（ent_company_leaderdrive），苏州科创板上市公司。
- **上游关键物料**：合金钢（柔轮/刚轮）、柔性轴承、润滑脂、铝材。
- **下游整机集成**：埃斯顿、优必选、埃夫特等机器人 OEM；协作机器人与人形机器人末端关节。
- **竞争/对标**：Harmonic Drive Systems（日本哈默纳科）、来福谐波、同川精密、大族谐波。

## 来源与验证

- 绿的谐波官网：https://www.leaderdrive.com
- 苏州盖尔斯威 LCD 系列产品页：http://www.sipgears.com/Products-10602467.html
- 东方财富 RV/谐波减速器研报（引用绿的谐波公告）：https://pdf.dfcfw.com/pdf/H3_AP202403191627111620_1.pdf