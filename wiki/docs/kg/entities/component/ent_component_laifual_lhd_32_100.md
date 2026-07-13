---
id: ent_component_laifual_lhd_32_100
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 来福 LHD-32-100-U-I 超薄谐波减速器
  en: Laifual LHD-32-100-U-I Ultra-thin Harmonic Reducer
status: active
sources:
- id: src_laifual_official
  type: website
- title: Laifual Official Website
  url: https://www.laifual.com
- id: src_laifual_catalog
  type: pdf
- title: Laifual Harmonic Reducer Catalog
  url: https://www.laifual.com/upload/Laifual%20Harmonic%20reducer%20catalog.pdf
- id: src_laifual_lhd_marketplace
  type: website
- title: Laifual LHD Series Product Introduction
  url: https://china.makepolo.com/product-detail/101096111853.html
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official public materials; missing values marked
    as 未公开.
---


# 来福 LHD-32-100-U-I 超薄谐波减速器 / Laifual LHD-32-100-U-I Ultra-thin Harmonic Reducer

## 概述

LHD-32-100-U-I 是来福谐波（Laifual）推出的 LHD 系列超薄型谐波减速器，规格代号为 32（节圆直径约 32×1/10 英寸），减速比 100:1。该型号采用超薄中空翻边柔轮结构，并集成高刚性交叉滚子轴承，轴向长度较标准杯型谐波减速器缩短约 50%，适用于对安装空间、轴向尺寸和重量敏感的机器人关节。

## 工作原理 / 技术架构

谐波减速器由波发生器（Wave Generator）、柔轮（Flexspline）和刚轮（Circular Spline）组成。波发生器装入柔轮内腔后，使柔轮产生可控椭圆弹性变形；柔轮长轴两端齿与刚轮齿啮合，短轴两端脱开。波发生器旋转一周，柔轮相对刚轮转动一个齿差角度，实现大减速比输出。

减速比由刚轮齿数 $z_c$ 与柔轮齿数 $z_f$ 决定：

$$
i = \frac{z_c}{z_c - z_f}
$$

对于 LHD-32-100-U-I，标称减速比 $i=100$。输出扭矩与输入扭矩的关系为

$$
T_{\text{out}} = i \cdot T_{\text{in}} \cdot \eta
$$

其中 $\eta$ 为传动效率，典型谐波减速器效率约为 80%–90%。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 系列 | LHD 超薄系列 | 来福官方产品资料 |
| 规格 | 32 | 来福产品页 |
| 减速比 | 50 / 80 / 100 :1（100 为当前型号） | 来福 LHD 产品参数 |
| 背隙 | ≤ 20 arcsec | 来福产品页 |
| 结构 | 超薄中空翻边 + 高刚性交叉滚子轴承 | 来福产品页 |
| 轴向长度 | 较标准型缩短约 50% | 来福产品页 |
| 额定扭矩（@2000 rpm） | 未公开 | - |
| 启动停止容许扭矩 | 未公开 | - |
| 瞬时最大扭矩 | 未公开 | - |
| 最高输入转速 | 未公开 | - |
| 重量 | 未公开 | - |

## 应用场景

- **协作机器人腕部/末端关节**：超薄结构可降低末端惯量，提升灵活性。
- **人形机器人手臂/腕部**：中空结构便于线缆穿过，简化走线。
- **医疗机械臂**：紧凑尺寸与高定位精度适用于手术/康复机器人。
- **精密转台与自动化设备**：利用低背隙特性实现高精度定位。

## 供应链关系

- **上游**：合金钢柔轮/刚轮、柔性轴承、润滑脂、铝合金壳体。
- **制造商**：`ent_company_laifual` -- `manufactures` --> `ent_component_laifual_lhd_32_100`。
- **下游客户**：工业机器人、协作机器人、人形机器人、医疗设备 OEM。
- **竞争对手/对标**：绿的谐波 LCD/LHS 系列、Harmonic Drive Systems CSF/SHD 系列、同川精密。

## 来源与验证

1. 来福谐波官网：https://www.laifual.com
2. Laifual Harmonic Reducer Catalog（PDF）
3. 马可波罗网 LHD-32-100-U-I 产品介绍：https://china.makepolo.com/product-detail/101096111853.html

> 注：LHD-32-100-U-I 的额定扭矩、极限扭矩、最高转速与重量等具体型号参数未在官方公开资料中完整披露，已标注为“未公开”。