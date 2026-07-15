---
$id: ent_component_frameless_torque_motor_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Frameless Torque Motor
  zh: 无框力矩电机
  ko: Frameless Torque Motor
summary:
  en: Direct-drive motor without housing or bearings, integrated into robot joints for high torque density.
  zh: 核心内容 人形机器人髋关节、肩关节往往需要几十到上百 N·m 的输出扭矩。若采用普通伺服电机加高减速比，虽可放大扭矩，但会牺牲透明度和带宽。一种方案是使用 **无框力矩电机**（frameless torque motor）：它把定子和转子直接嵌入关节结构，取消外壳、端盖和轴承，直径大、极数多，可在低转速下直接输出大扭矩。
  ko: 하우징이나 베어링이 없는 직접 구동 모터, 로봇 관절에 통합되어 높은 토크 밀도 제공.
domains:
- 02_components
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component
- direct_drive
- frameless_torque_motor
- joint
- motor
- torque_density
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from chapter-04.md#4.2.5 无框力矩电机与关节集成 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Frameless Torque Motor
  url: https://en.wikipedia.org/wiki/Torque_motor
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
无框力矩电机是人形机器人领域的重要component。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
人形机器人髋关节、肩关节往往需要几十到上百 N·m 的输出扭矩。若采用普通伺服电机加高减速比，虽可放大扭矩，但会牺牲透明度和带宽。一种方案是使用 **无框力矩电机**（frameless torque motor）：它把定子和转子直接嵌入关节结构，取消外壳、端盖和轴承，直径大、极数多，可在低转速下直接输出大扭矩。

无框力矩电机的扭矩密度可表示为

$$
\tau = 2 \pi r^2 l B_{\text{gap}} J_s
$$

其中 \(r\) 为气隙半径，\(l\) 为轴向长度，\(B_{\text{gap}}\) 为气隙磁密，\(J_s\) 为电负荷（绕组总电流 per 周长）。增大 \(r\) 对扭矩的提升是二次方关系，因此大直径无框电机在相同质量下可获得更高扭矩。

!!! note "术语解释：无框力矩电机、电负荷、气隙、直接驱动、力矩电机"
    - **无框力矩电机（frameless torque motor）**：没有外壳、转轴和端盖的电机，由用户把定子、转子直接集成到机械结构中，以最大化扭矩密度。
    - **电负荷（electric loading）**：单位圆周长度上的总安培导体数，反映绕组"载流能力"。
    - **气隙（air gap）**：定子与转子之间的微小空气间隙，磁通必须跨越它。气隙越小，磁阻越低，但制造与热变形要求更高。
    - **直接驱动（direct drive）**：电机不经减速器直接驱动负载，无背隙、高透明度，但需要大扭矩电机。
    - **力矩电机（torque motor）**：专为低速大扭矩设计的电机，通常直径大、极数多。

Tesla Optimus 的旋转关节 reportedly 采用无框力矩电机加谐波减速器的一体化方案[14]。

## 参考
- [Frameless Torque Motor](https://en.wikipedia.org/wiki/Torque_motor)
- 项目 Wiki：chapter-04.md#4.2.5 无框力矩电机与关节集成


