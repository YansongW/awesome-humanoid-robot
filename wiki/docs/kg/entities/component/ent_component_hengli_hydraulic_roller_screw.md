---
id: ent_component_hengli_hydraulic_roller_screw
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 恒立液压滚柱丝杠
  en: Hengli Hydraulic Roller Screw
status: active
sources:
- id: src_hengli_official
  type: website
- title: 恒立液压官网
  url: https://www.henglihydraulic.com
- id: src_hengli_ball_screw
  type: website
- title: Hengli Hydraulics Ball Screw Product Page
  url: https://www.henglihydraulics.com/en/col635/index
- id: src_iyanbao_screw_report
  type: pdf
- title: 人形机器人打开丝杠成长空间行业报告
  url: https://file.iyanbao.com/pdf/76044-854fe5e6-0c25-43a2-bfec-6056987c3dfe.pdf
- id: src_rollvis_catalog
  type: pdf
- title: Rollvis Planetary Roller Screw Catalogue
  url: https://rollvis.com/wp-content/uploads/2023/07/Catalogue-CN-2019-compressed.pdf
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Roller screw product-level specifications are not publicly disclosed;
    general roller screw principles cited from industry catalogs.
---


# 恒立液压滚柱丝杠 / Hengli Hydraulic Roller Screw

## 概述

恒立液压滚柱丝杠是江苏恒立液压股份有限公司基于其液压件精密加工、热处理与特种钢材制造能力布局的线性传动产品，主要面向高负载、高响应的人形机器人下肢关节与重载电缸。行星滚柱丝杠相较滚珠丝杠具有更多接触点、更高承载能力与更长寿命，适用于将电机旋转运动转换为直线推力输出的机器人执行器。

## 工作原理 / 技术架构

行星滚柱丝杠由丝杠轴、螺母及介于二者之间的行星滚柱组成。滚柱既绕丝杠轴公转又自转，通过螺纹啮合将旋转运动转换为螺母的直线运动。其导程 $P_h$ 与转速 $n$ 决定直线速度：

$$
v = P_h \cdot n
$$

在稳态负载 $F$ 下，所需驱动转矩为

$$
T = \frac{F \cdot P_h}{2000 \pi \eta}
$$

其中 $\eta$ 为传动效率（行星滚柱丝杠典型效率约 85%–90%）。

滚动接触疲劳寿命按基本额定动载荷 $C_a$ 与当量平均载荷 $F_m$ 计算：

$$
L_{10} = \left( \frac{C_a}{F_m} \right)^3 \times 10^6 \ \text{rev}
$$

恒立液压依托工程机械液压件积累的精密铸造、机加工与热处理能力，切入滚柱丝杠等高端传动件，但具体型号的几何与载荷参数尚未公开。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 结构形式 | 行星滚柱 / 循环滚柱 | 恒立液压公司 Wiki |
| 材质 | 轴承钢 | 恒立液压公司 Wiki |
| 应用领域 | 人形机器人下肢、重载电缸、工业自动化 | 恒立液压公司 Wiki |
| 公称直径 | 未公开 | - |
| 导程 | 未公开 | - |
| 精度等级 | 未公开 | - |
| 额定动载荷 $C_a$ | 未公开 | - |
| 额定静载荷 $C_0$ | 未公开 | - |
| 最高转速 | 未公开 | - |
| 重量 | 未公开 | - |
| 价格 | 未公开 | - |

## 应用场景

- **人形机器人线性关节**：用于膝关节、踝关节等需要大推力、高刚性直线驱动的部位。
- **重载电缸**：替代液压缸，实现清洁、可控的机电直线执行。
- **工业自动化**：高负载精密定位、压机、注塑机、机床进给轴。
- **工程机械**：依托恒立液压主机厂渠道，向高端液压-机电一体化延伸。

## 供应链关系

- **上游**：特种轴承钢、密封件、热处理服务、精密磨削设备、润滑脂。
- **制造商**：`ent_company_hengli_hydraulic` -- `manufactures` --> `ent_component_hengli_hydraulic_roller_screw`。
- **下游客户**：人形机器人 OEM、工程机械主机厂、工业自动化设备商。
- **竞争对手/对标**：Rollvis、GSA、Rexroth、SKF、南京工艺、济宁博特、新剑传动。

## 来源与验证

1. 恒立液压官网：https://www.henglihydraulic.com
2. 恒立液压滚珠丝杠产品页（用于验证公司传动件布局）：https://www.henglihydraulics.com/en/col635/index
3. 东方证券/国金证券等人形机器人丝杠行业研报
4. Rollvis 行星滚柱丝杠样本（传动原理与寿命公式参考）

> 注：恒立液压滚柱丝杠的具体型号、公称直径、导程、额定载荷与精度等级等参数未在官方公开资料中披露，已标注为“未公开”。