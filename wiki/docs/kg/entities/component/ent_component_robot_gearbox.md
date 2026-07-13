---
id: ent_component_robot_gearbox
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 机器人减速器
  en: Robot Gearbox
status: active
sources:
- id: src_picea_harmonic_vs_planetary
  type: website
  url: https://www.piceamotiondrive.com/harmonic-drive-vs-planetary-gearbox-which-is-better-for-precision-motion.html
- id: src_sdtgear_harmonic_stiffness
  type: website
  url: https://sdtgear.com/harmonic-drive-gearbox-torsional-stiffness-compared-to-planetary-gearbox/
- id: src_risc_drive_reducers
  type: website
  url: http://www.risc-drive.com/news_details/236.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 机器人减速器 / Robot Gearbox

## 概述

机器人减速器是连接伺服电机与机器人关节的机械传动部件，用于降低转速、放大扭矩并提高负载端的运动精度。根据传动原理，机器人精密减速器主要分为谐波减速器（strain wave gear）、RV 减速器（rotate vector / cycloidal-pinwheel）、行星减速器（planetary gearbox）与摆线减速器（cycloidal drive）。不同拓扑在减速比、回程间隙、扭矩密度、效率与刚性方面各有侧重，共同构成机器人关节模组的核心。

## 工作原理 / 技术架构

减速器的基本功能可通过以下关系描述：

- **减速比**：
  \[
  i = \frac{\omega_{\text{in}}}{\omega_{\text{out}}} = \frac{n_{\text{in}}}{n_{\text{out}}}
  \]
- **输出扭矩**：
  \[
  \tau_{\text{out}} = \tau_{\text{in}} \cdot i \cdot \eta
  \]
  其中 \(\eta\) 为传动效率。
- **功率守恒（理想）**：
  \[
  P = \tau_{\text{in}} \omega_{\text{in}} = \tau_{\text{out}} \omega_{\text{out}} \cdot \eta
  \]

各类减速器的技术特点：

- **谐波减速器**：由波发生器、柔轮与刚轮组成，依靠弹性变形传动，单级减速比可达 50:1–320:1，回程间隙接近零，适合机器人小臂、腕部与协作机器人关节。
- **RV 减速器**：两级结构（行星 + 摆线），减速比 30:1–192:1，刚性高、抗冲击，常用于工业机器人底座、肩部、腰部与人形机器人髋/膝关节。
- **行星减速器**：太阳轮、行星轮与内齿圈多级啮合，单级减速比通常不超过 10:1，效率高、刚性强、成本低，广泛应用于伺服辅助轴与移动机器人轮边驱动。
- **摆线减速器**：摆线轮与针齿啮合，减速比 10:1–100:1，效率高、寿命长，常用于重载转台与 AGV 驱动。

## 关键参数表

| 参数项 | 谐波减速器 | RV 减速器 | 行星减速器 | 摆线减速器 |
|---|---|---|---|---|
| 单级减速比范围 | 50:1–320:1 | 30:1–192:1 | 3:1–10:1 | 10:1–100:1 |
| 传动效率 | 80%–90% | 85%–95% | >90% | 90%–95% |
| 回程间隙 | 接近零 / 很小 | <1 arcmin | 低至中等 | <1 arcmin |
| 扭矩密度 | 高 | 高 | 中等 | 高 |
| 扭转刚性 | 中等 | 高 | 高 | 高 |
| 抗冲击能力 | 中等 | 强 | 强 | 强 |
| 主要应用 | 小臂、腕部、协作机器人 | 重载关节、人形机器人躯干 | 伺服轴、轮边驱动 | 转台、AGV、重载驱动 |

## 应用场景

- **工业机器人**：RV 减速器用于 J1–J4 重载轴，谐波减速器用于 J5–J6 精密轴。
- **协作机器人**：谐波减速器提供零背隙与紧凑体积。
- **人形机器人**：髋/膝/踝采用 RV 或行星减速器，手臂与手指采用谐波或微型行星减速器。
- **移动机器人**：行星与摆线减速器用于轮边驱动与转向机构。

## 供应链关系

- **上游**：特种轴承钢、齿轮毛坯、精密轴承、密封件、润滑脂、加工设备与热处理服务。
- **中游**：专业减速器制造商，包括日本 Nabtesco（RV）、Harmonic Drive（谐波）、德国 Wittenstein、SPINEA，以及中国南通振康、绿的谐波、来福谐波、双环传动等。
- **下游**：伺服电机与关节模组厂商、机器人整机厂、自动化设备集成商。
- **图谱位置**：`ent_component_robot_gearbox` 作为通用类别，通过 `used_in` 关系连接各类机器人关节实体；具体型号如 `ent_component_nantong_zhenkang_rv_e_reducer` 为其子类实例。

## 来源与验证

- 谐波与行星减速器对比参数参考 Picea Motion Drive 与 SDT Gear 技术文章。
- RV、谐波、行星与摆线减速器综合对比参考 RISC Drive 技术博客。
- 实际选型应以减速器厂商官方 catalog 与机器人关节负载计算为准。