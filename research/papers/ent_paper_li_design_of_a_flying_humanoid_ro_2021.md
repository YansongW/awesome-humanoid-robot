---
$id: ent_paper_li_design_of_a_flying_humanoid_ro_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Design of a Flying Humanoid Robot Based on Thrust Vector Control
  zh: 基于推力矢量控制的飞行人形机器人设计
  ko: 추력 벡터 제어에 기반한 비행 휴머노이드 로봇 설계
summary:
  en: This paper presents Jet-HR2, a life-sized flying humanoid robot propelled by
    four ducted fans and ten brushless-motor joints, and experimentally demonstrates
    stable-attitude takeoff at a thrust-to-weight ratio of 1.17 using thrust-vector
    control of foot-mounted fans.
  zh: 本文提出Jet-HR2——一款配备四个涵道风扇和十个无刷电机关节的全尺寸飞行人形机器人，并通过脚部风扇的推力矢量控制，在1.17的推重比下实验实现了稳定姿态起飞。
  ko: 본 논문은 4개의 덕티드 팬과 10개의 브러시리스 모터 관절을 갖춘 실물 크기 비행 휴머노이드 로봇 Jet-HR2를 제안하며, 발에 장착된
    팬의 추력 벡터 제어를 통해 추중비 1.17에서 안정적인 자세 이륙을 실험적으로 입증한다.
domains:
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- system
tags:
- jet_hr2
- flying_humanoid_robot
- thrust_vector_control
- ducted_fan
- aerial_takeoff
- low_thrust_to_weight
- attitude_stabilization
- brushless_motor
- harmonic_drive
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the supplied metadata/abstract; full-text review is needed
    to confirm section-level citations, exact component specifications, and experimental
    details.
sources:
- id: src_001
  type: paper
  title: Design of a Flying Humanoid Robot Based on Thrust Vector Control
  url: https://arxiv.org/abs/2108.11557
  date: '2021'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
- system
---

## Overview

This study proposes Jet-HR2, a life-sized flying humanoid robot intended to improve the mobility of humanoid robots in complex environments such as disaster sites with large obstacles or elevated targets. The robot has ten joints driven by brushless motors and harmonic drives for locomotion. Its propulsion system consists of four ducted fans: two fixed on the waist and two mounted on the feet. Because the overall thrust-to-weight ratio is only 1.17 (17 kg thrust / 20 kg weight), conventional multi-rotor-like high thrust margins are infeasible, so the authors stabilize attitude by actively adjusting foot attitude to vector thrust and generate pitch/yaw moments.

To address attitude instability caused by mass errors and joint-position errors during takeoff, the authors propose a simplified sagittal-plane model together with PD-based control strategies. Experiments showed that the robot's spin and dive behaviors during takeoff were effectively suppressed by controlling the thrust vector of the foot-mounted ducted fan. The robot achieved stable-attitude takeoff at a thrust-to-weight ratio of 1.17 and reached a takeoff height of over 1000 mm.

## Key Contributions

- Designed and built Jet-HR2, a life-sized flying humanoid robot with a ducted-fan propulsion system.
- Proposed thrust-vector control on the feet to stabilize attitude during low-thrust-to-weight takeoff.
- Developed a simplified force model and PD-based control strategy to suppress dive and spin behaviors.
- Experimentally demonstrated stable takeoff at a thrust-to-weight ratio of 1.17, reaching over 1000 mm height.

## Relevance to Humanoid Robotics

Jet-HR2 extends humanoid robot mobility beyond walking and jumping to short-distance aerial takeoff, which is directly relevant to deploying humanoids in search-and-rescue and other complex environments where ground-only locomotion is insufficient. The work also provides a concrete example of integrating propulsion components—ducted fans, brushless motors, harmonic drives, and LiPo batteries—into a humanoid platform, linking component design to system-level aerial capability.
