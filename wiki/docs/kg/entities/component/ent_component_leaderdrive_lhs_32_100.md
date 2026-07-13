---
id: ent_component_leaderdrive_lhs_32_100
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 绿的谐波 LHS-32-100 谐波减速器
  en: Leaderdrive LHS-32-100 Harmonic Reducer
status: active
sources:
- id: src_leaderdrive_official
  type: website
- title: Leaderdrive Official Website
  url: https://www.leaderdrive.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from Leaderdrive product manual cited in company Wiki;
    missing values marked as 未公开.
---


# 绿的谐波 LHS-32-100 谐波减速器 / Leaderdrive LHS-32-100 Harmonic Reducer

## 概述

LHS-32-100 是苏州绿的谐波传动科技股份有限公司（Leaderdrive）推出的 LHS 系列标准中空型谐波减速器，规格 32、减速比 100:1。该产品采用自主 P 型齿形与高刚性中空结构，额定扭矩、承载能力与寿命接近国际主流水平，是国内工业机器人与人形机器人关节的主流减速器选项之一。

## 工作原理 / 技术架构

谐波减速器依靠波发生器迫使柔轮产生周期性弹性变形，实现柔轮与刚轮之间的少齿差啮合。减速比由齿数差决定：

$$
i = \frac{z_c}{z_c - z_f}
$$

对于 LHS-32-100，$i = 100$。输出扭矩与输入扭矩满足

$$
T_{\text{out}} = i \cdot T_{\text{in}} \cdot \eta
$$

其中 $\eta$ 为传动效率，典型值约 80%–90%。绿的谐波采用 P 型齿形优化啮合几何，降低齿面接触应力并提升扭转刚度。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 系列 | LHS 中空谐波减速器 | 绿的谐波产品手册 |
| 规格 | 32（节圆直径） | 绿的谐波产品手册 |
| 减速比 | 50 / 80 / 100 / 120 :1（100 为当前型号） | 绿的谐波产品手册 |
| 额定扭矩（@2000 rpm，100:1） | 91 N·m | 绿的谐波产品手册 |
| 启动停止容许扭矩（100:1） | 221 N·m | 绿的谐波产品手册 |
| 瞬时最大扭矩（100:1） | 399 N·m | 绿的谐波产品手册 |
| 最高输入转速 | 4500 rpm | 绿的谐波产品手册 |
| 平均输入转速 | 3500 rpm | 绿的谐波产品手册 |
| 背隙 | ≤ 20 arcsec | 绿的谐波产品手册 |
| 重量 | 2.5 kg | 绿的谐波产品手册 |
| 结构 | 高刚性中空结构，P 型齿形 | 绿的谐波产品手册 |
| 输出轴承 | 高刚性交叉滚子轴承 | 绿的谐波产品手册 |
| 扭转刚度（分段） | 未公开完整曲线 | - |

## 应用场景

- **工业机器人关节**：用于六轴机器人肩、肘、腕等关节。
- **人形机器人关节**：适用于肩、肘、腕、髋等中大扭矩关节。
- **协作机器人**：中空结构便于线缆与气管穿过。
- **CNC 转台与精密转台**：利用低背隙实现高精度分度。

## 供应链关系

- **上游**：合金钢（柔轮/刚轮）、柔性轴承、润滑脂、铝材。
- **制造商**：`ent_company_leaderdrive` -- `manufactures` --> `ent_component_leaderdrive_lhs_32_100`。
- **下游客户**：埃斯顿、优必选、埃夫特等国内机器人 OEM（见 company Leaderdrive Wiki）。
- **竞争对手/对标**：Harmonic Drive Systems、来福谐波、同川精密。

## 来源与验证

1. 绿的谐波官网：https://www.leaderdrive.com
2. 附录 D 企业 Wiki：company_leaderdrive.md
3. 绿的谐波产品手册（公司 Wiki 引用）