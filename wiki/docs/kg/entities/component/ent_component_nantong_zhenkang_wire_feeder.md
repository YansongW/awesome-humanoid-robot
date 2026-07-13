---
id: ent_component_nantong_zhenkang_wire_feeder
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 南通振康焊接送丝机
  en: Nantong Zhenkang Wire Feeder
status: active
sources:
- id: src_zhenkang_official
  type: website
  url: https://www.zhenkang.com
- id: src_weldhome_sb10b1
  type: website
  url: https://www.weldhome.com.cn/index.php?a=show&c=index&catid=997&id=402&m=yp&top=1011
- id: src_welding21_sb10
  type: website
  url: http://www.3w21.com/company/show_product.asp?id=33400
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 南通振康焊接送丝机 / Nantong Zhenkang Wire Feeder

## 概述

南通振康焊接送丝机是面向 MIG/MAG/TIG 自动焊与机器人焊接的辅机，由直流电机驱动送丝轮，将焊丝以稳定速度推送至焊枪。产品具有数字/模拟控制、过流与堵转保护功能，可与焊接电源、机器人控制器联动，广泛应用于船舶、钢结构及工程机械焊接产线。

## 工作原理 / 技术架构

送丝机由控制板、直流电机、减速机构、主动轮/从动轮及压紧装置组成。控制板接收机器人或焊机给出的送丝指令后，驱动电机带动送丝轮旋转；通过调节压杆压力控制焊丝与滚轮间的摩擦力，从而保证送丝稳定。系统支持滞后送丝、提前抽丝、连续/断续送丝模式，并具备过流与堵转保护。

送丝速度 \(v\)（m/min）与送丝轮转速 \(n\)（rpm）及轮径 \(d\)（mm）的关系为
\[
v=\frac{\pi d n}{1000}.
\]
实际速度由控制器通过电机转速闭环调节。

## 关键参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 机器人/自动焊用送丝机 | 产品手册 |
| 送丝速度 | 1.5–20 m/min（依型号） | 振康 SB-10B1 等 |
| 适用焊丝直径 | Φ0.8–Φ1.6 mm（部分型号 Φ2.0–Φ2.4） | 产品手册 |
| 供电电压 | DC 24–42 V | 产品手册 |
| 额定电流 | 3.5–5 A | 产品手册 |
| 适用焊丝盘 | Φ300 × Φ50 × 103 mm，最大 20 kg | 产品手册 |
| 外形尺寸 | 约 460 × 200 × 280 mm（SB-10B1） | 焊接之家 |
| 整机重量 | 7–11 kg（型号相关） | 焊接之家 |
| 控制方式 | 数字 / 模拟 | 产品手册 |
| 保护功能 | 过流、堵转保护 | 产品手册 |

## 应用场景

- 焊接机器人配套送丝
- 船舶与海洋工程焊接
- 钢结构自动焊
- 工程机械制造

## 供应链关系

南通振康焊接机电有限公司（`ent_company_nantong_zhenkang`）制造该送丝机。上游包括直流电机、减速齿轮、控制板、送丝导管及焊丝盘；下游为焊接机器人系统集成商与造船/重工企业。在知识图谱中，`ent_company_nantong_zhenkang` 通过 `manufactures` 关系指向 `ent_component_nantong_zhenkang_wire_feeder`。

## 来源与验证

- [南通振康官网](https://www.zhenkang.com)
- [振康 SB-10B1 多功能送丝机参数](https://www.weldhome.com.cn/index.php?a=show&c=index&catid=997&id=402&m=yp&top=1011)
- [焊接21世纪 南通振康 SB-10-B 送丝机参数](http://www.3w21.com/company/show_product.asp?id=33400)