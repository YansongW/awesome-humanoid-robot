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
  en: This paper presents Jet-HR2, a life-sized flying humanoid robot propelled by four ducted fans and ten brushless-motor
    joints, and experimentally demonstrates stable-attitude takeoff at a thrust-to-weight ratio of 1.17 using thrust-vector
    control of foot-mounted fans.
  zh: 本文提出Jet-HR2，一款由四个涵道风扇和十个无刷电机关节驱动的真人大小飞行人形机器人。通过足部风扇的推力矢量控制，该机器人在推重比1.17的条件下实现了稳定姿态起飞，核心贡献在于解决了小推重比下的姿态稳定性难题。
  ko: 본 논문은 4개의 덕티드 팬과 10개의 브러시리스 모터 관절을 갖춘 실물 크기 비행 휴머노이드 로봇 Jet-HR2를 제안하며, 발에 장착된 팬의 추력 벡터 제어를 통해 추중비 1.17에서 안정적인 자세 이륙을
    실험적으로 입증한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2108.11557v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
## 概述
Jet-HR2机器人配备十个由无刷电机和谐波减速器驱动的关节，用于地面运动。其推进系统包含四个涵道风扇：两个固定在腰部，两个安装在足部，通过调整飞行中足部姿态实现推力矢量控制。针对起飞时质量误差和关节位置误差导致的姿态失稳问题，研究提出了简化模型与控制策略。实验表明，足部涵道风扇的推力矢量控制有效抑制了起飞过程中的旋转和俯冲行为。

## 核心内容
### 研究动机
短距离飞行能力有助于人形机器人在复杂环境中（如跨越大型障碍或到达高处）执行快速应急任务时提升效率。

### 机器人设计
- **关节系统**：10个关节由无刷电机与谐波减速器驱动，支持地面运动。
- **推进系统**：四个涵道风扇，两个固定于腰部，两个安装于足部，实现推力矢量控制。
- **推力矢量控制**：通过调整飞行中足部姿态改变推力方向。

### 控制策略
- **问题**：起飞时质量误差与关节位置误差导致姿态不稳定。
- **方法**：提出简化模型与控制策略，利用足部涵道风扇的推力矢量抑制旋转和俯冲行为。

### 实验设置与结果
- **推重比**：1.17（推力17 kg / 重量20 kg）。
- **起飞高度**：超过1000 mm。
- **关键发现**：足部风扇的推力矢量控制有效抑制了起飞过程中的姿态失稳，机器人成功实现稳定姿态起飞。

## Overview
Achieving short-distance flight helps improve the efficiency of humanoid robots moving in complex environments (e.g., crossing large obstacles or reaching high places) for rapid emergency missions. This study proposes a design of a flying humanoid robot named Jet-HR2. The robot has 10 joints driven by brushless motors and harmonic drives for locomotion. To overcome the challenge of the stable-attitude takeoff in small thrust-to-weight conditions, the robot was designed based on the concept of thrust vectoring. The propulsion system consists of four ducted fans, that is, two fixed on the waist of the robot and the other two mounted on the feet, for thrust vector control. The thrust vector is controlled by adjusting the attitude of the foot during the flight. A simplified model and control strategies are proposed to solve the problem of attitude instability caused by mass errors and joint position errors during takeoff. The experimental results show that the robot's spin and dive behaviors during takeoff were effectively suppressed by controlling the thrust vector of the ducted fan on the foot. The robot successfully achieved takeoff at a thrust-to-weight ratio of 1.17 (17 kg / 20 kg) and maintained a stable attitude, reaching a takeoff height of over 1000 mm.

## 개요
단거리 비행을 실현하면 복잡한 환경(예: 큰 장애물을 넘거나 높은 곳에 도달)에서 이동하는 휴머노이드 로봇의 효율성을 향상시켜 신속한 응급 임무 수행이 가능해집니다. 본 연구에서는 Jet-HR2라는 비행 휴머노이드 로봇의 설계를 제안합니다. 이 로봇은 브러시리스 모터와 하모닉 드라이브로 구동되는 10개의 관절을 갖추고 있습니다. 작은 추력-중량비 조건에서 안정적인 자세 이륙이라는 과제를 해결하기 위해, 로봇은 추력 벡터링 개념을 기반으로 설계되었습니다. 추진 시스템은 4개의 덕티드 팬으로 구성되며, 그중 2개는 로봇의 허리에 고정되고 나머지 2개는 발에 장착되어 추력 벡터 제어를 수행합니다. 추력 벡터는 비행 중 발의 자세를 조정하여 제어됩니다. 이륙 중 질량 오차와 관절 위치 오차로 인한 자세 불안정 문제를 해결하기 위해 단순화된 모델과 제어 전략이 제안되었습니다. 실험 결과, 발에 장착된 덕티드 팬의 추력 벡터를 제어함으로써 이륙 중 로봇의 회전 및 급강하 동작이 효과적으로 억제되었습니다. 로봇은 1.17(17kg/20kg)의 추력-중량비에서 성공적으로 이륙하여 안정적인 자세를 유지했으며, 1000mm 이상의 이륙 높이에 도달했습니다.

## 핵심 내용
단거리 비행을 실현하면 복잡한 환경(예: 큰 장애물을 넘거나 높은 곳에 도달)에서 이동하는 휴머노이드 로봇의 효율성을 향상시켜 신속한 응급 임무 수행이 가능해집니다. 본 연구에서는 Jet-HR2라는 비행 휴머노이드 로봇의 설계를 제안합니다. 이 로봇은 브러시리스 모터와 하모닉 드라이브로 구동되는 10개의 관절을 갖추고 있습니다. 작은 추력-중량비 조건에서 안정적인 자세 이륙이라는 과제를 해결하기 위해, 로봇은 추력 벡터링 개념을 기반으로 설계되었습니다. 추진 시스템은 4개의 덕티드 팬으로 구성되며, 그중 2개는 로봇의 허리에 고정되고 나머지 2개는 발에 장착되어 추력 벡터 제어를 수행합니다. 추력 벡터는 비행 중 발의 자세를 조정하여 제어됩니다. 이륙 중 질량 오차와 관절 위치 오차로 인한 자세 불안정 문제를 해결하기 위해 단순화된 모델과 제어 전략이 제안되었습니다. 실험 결과, 발에 장착된 덕티드 팬의 추력 벡터를 제어함으로써 이륙 중 로봇의 회전 및 급강하 동작이 효과적으로 억제되었습니다. 로봇은 1.17(17kg/20kg)의 추력-중량비에서 성공적으로 이륙하여 안정적인 자세를 유지했으며, 1000mm 이상의 이륙 높이에 도달했습니다.

## 参考
- http://arxiv.org/abs/2108.11557v1
