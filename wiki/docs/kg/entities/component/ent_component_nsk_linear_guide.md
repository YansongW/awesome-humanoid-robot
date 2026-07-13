---
id: ent_component_nsk_linear_guide
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: NSK 直线导轨
  en: NSK Linear Guide
status: active
sources:
- id: src_nsk_linear_guide_catalog
  type: datasheet
- title: NSK Linear Guides NH/NS Series Catalog
  url: https://www.nsk.com/content/dam/nsk/common/catalogs/ctrgPdf/precision/e3332c.pdf
- id: src_nsk_smooth_motion_spec
  type: datasheet
- title: NSK Smooth Motion Specification for NH/NS Models
  url: https://www.nsk.com/content/dam/nsk/common/catalogs/ctrgPdf/precision/ESP-230125.pdf
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自 NSK 公开产品目录；缺失值标注为“未公开”。
---


# NSK 直线导轨 / NSK Linear Guide

## 概述

NSK 直线导轨是日本精工株式会社（NSK Ltd.）生产的滚动直线导轨产品，广泛应用于数控机床、半导体设备、液晶面板制造设备、自动化平台以及人形机器人线性关节。NH/NS 系列在经典 LH/LS 系列基础上优化了滚珠沟槽几何形状，额定载荷提高约 1.3 倍，额定寿命提升约 2 倍，同时保持与 LH/LS 系列相同的安装尺寸，便于替换升级。

## 工作原理 / 技术架构

滚动直线导轨通过滑块内部的滚珠在导轨与滑块滚道之间滚动，将传统的滑动摩擦转化为滚动摩擦，从而实现高精度、低摩擦的直线运动。NSK NH/NS 系列采用 50° 接触角设计，以提高垂直方向的承载能力。

滚动导轨的额定疲劳寿命 $L$（以 100 km 为基本额定行程）可依据 ISO 14728-1/2 估算：

$$
L = \left( \frac{C}{P} \right)^3 \times 100 \ \mathrm{km}
$$

其中 $C$ 为基本额定动载荷，$P$ 为当量动载荷。当考虑振动、冲击等使用条件时，需引入载荷系数 $f_w$ 对 $P$ 进行修正。

## 关键参数表

| 参数 | 典型值 / 范围 | 备注 |
|------|--------------|------|
| 系列 | NH / NS | 高负载型 / 紧凑型 |
| 导轨宽度 | 15–100 mm | 产品手册 |
| 精度等级 | P3 / P4 / P5 / P6 / PN（预紧装配）；PH / PC（互换型） | 产品手册 |
| 预紧 | 轻预紧 Z1、中等预紧 Z2、普通间隙 T / fine clearance Z3 | 依型号 |
| 基本额定动载荷 $C_{50}$ | 6.55–44.0 kN（NS 系列，高/中负载型，尺寸 15–30） | Smooth Motion 规格书 |
| 基本额定静载荷 $C_0$ | 7.6–66.5 kN | 产品手册 |
| 最大导轨长度 | 1700–4000 mm（依尺寸与材质） | 可对接延长 |
| 材质 | 高碳钢 / 不锈钢 | 可选表面处理 |
| 最大运行速度 | 100 m/min（Smooth Motion 规格） | 产品手册 |
| 价格 | 未公开 | - |

## 应用场景

- 数控机床进给轴与定位平台
- 半导体晶圆传输与检测设备
- 液晶面板与 OLED 制造设备
- 协作/人形机器人线性关节与直线模组
- 医疗仪器、光学平台与测量设备

## 供应链关系

制造商为日本精工株式会社（`ent_company_nsk`）。上游关键原材料包括轴承钢、特种钢材、润滑脂、密封件与陶瓷球；下游客户包括机床厂商、半导体设备商、液晶面板设备商、机器人 OEM 与医疗设备制造商。在知识图谱中，`ent_company_nsk` -- `manufactures` --> `ent_component_nsk_linear_guide`。

## 来源与验证

本卡片参数引自 NSK Linear Guides NH/NS Series Catalog 与 NSK Smooth Motion Specification for NH/NS Models。具体型号价格未公开。