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
  zh: 人形机器人髋关节、肩关节往往需要几十到上百 N·m 的输出扭矩。若采用普通伺服电机加高减速比，虽可放大扭矩，但会牺牲透明度和带宽。一种方案是使用 无框力矩电机（frameless torque motor）：它把定子和转子直接嵌入关节结构，取消外壳、端盖和轴承，直径大、极数多，可在低转速下直接输出大扭矩。
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
无框力矩电机是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

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

## Overview
Frameless torque motors are an important component in the field of humanoid robots. The following content is compiled from the project Wiki for in-depth reference.

## Content
The hip and shoulder joints of humanoid robots often require output torques ranging from tens to hundreds of N·m. While using a standard servo motor with a high reduction ratio can amplify torque, it compromises transparency and bandwidth. One solution is to use a **frameless torque motor**: it embeds the stator and rotor directly into the joint structure, eliminating the housing, end caps, and bearings. With a large diameter and high pole count, it can directly output high torque at low speeds.

The torque density of a frameless torque motor can be expressed as

$$
\tau = 2 \pi r^2 l B_{\text{gap}} J_s
$$

where \(r\) is the air gap radius, \(l\) is the axial length, \(B_{\text{gap}}\) is the air gap flux density, and \(J_s\) is the electric loading (total winding current per circumference). Increasing \(r\) enhances torque quadratically, so large-diameter frameless motors can achieve higher torque for the same mass.

!!! note "Terminology: Frameless torque motor, electric loading, air gap, direct drive, torque motor"
    - **Frameless torque motor**: A motor without a housing, shaft, or end caps, where the user integrates the stator and rotor directly into the mechanical structure to maximize torque density.
    - **Electric loading**: The total ampere-conductors per unit circumference, reflecting the winding's current-carrying capacity.
    - **Air gap**: The small air gap between the stator and rotor, across which magnetic flux must pass. A smaller air gap reduces magnetic reluctance but imposes stricter requirements on manufacturing and thermal deformation.
    - **Direct drive**: The motor drives the load directly without a reducer, offering zero backlash and high transparency, but requiring a high-torque motor.
    - **Torque motor**: A motor designed for low-speed, high-torque applications, typically with a large diameter and high pole count.

Tesla Optimus's rotary joints reportedly adopt an integrated solution using a frameless torque motor with a harmonic reducer[14].

## 개요
프레임리스 토크 모터는 휴머노이드 로봇 분야의 중요한 부품입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
휴머노이드 로봇의 고관절과 어깨 관절은 종종 수십에서 수백 N·m의 출력 토크를 필요로 합니다. 일반 서보 모터에 높은 감속비를 적용하면 토크를 증폭할 수 있지만, 투명성과 대역폭이 희생됩니다. 한 가지 해결책은 **프레임리스 토크 모터**(frameless torque motor)를 사용하는 것입니다. 이 모터는 고정자와 회전자를 관절 구조에 직접 내장하고, 하우징, 엔드 캡, 베어링을 제거하며, 직경이 크고 극 수가 많아 저속에서도 직접 큰 토크를 출력할 수 있습니다.

프레임리스 토크 모터의 토크 밀도는 다음과 같이 표현됩니다.

$$
\tau = 2 \pi r^2 l B_{\text{gap}} J_s
$$

여기서 \(r\)은 공극 반경, \(l\)은 축 방향 길이, \(B_{\text{gap}}\)은 공극 자속 밀도, \(J_s\)는 전기 부하(권선 총 전류 per 둘레)입니다. \(r\)을 증가시키면 토크 향상이 제곱 관계로 나타나므로, 대직경 프레임리스 모터는 동일한 질량에서 더 높은 토크를 얻을 수 있습니다.

!!! note "용어 설명: 프레임리스 토크 모터, 전기 부하, 공극, 직접 구동, 토크 모터"
    - **프레임리스 토크 모터(frameless torque motor)**: 하우징, 회전축, 엔드 캡이 없는 모터로, 사용자가 고정자와 회전자를 기계 구조에 직접 통합하여 토크 밀도를 극대화합니다.
    - **전기 부하(electric loading)**: 단위 둘레 길이당 총 암페어 도체 수로, 권선의 "전류 운반 능력"을 반영합니다.
    - **공극(air gap)**: 고정자와 회전자 사이의 미세한 공기 간극으로, 자속이 이를 통과해야 합니다. 공극이 작을수록 자기 저항이 낮아지지만, 제조 및 열 변형 요구 사항이 더 높아집니다.
    - **직접 구동(direct drive)**: 모터가 감속기 없이 직접 부하를 구동하며, 백래시가 없고 투명성이 높지만, 큰 토크의 모터가 필요합니다.
    - **토크 모터(torque motor)**: 저속에서 큰 토크를 내도록 설계된 모터로, 일반적으로 직경이 크고 극 수가 많습니다.

Tesla Optimus의 회전 관절은 프레임리스 토크 모터와 하모닉 감속기를 결합한 일체형 솔루션을 채택한 것으로 알려져 있습니다[14].
