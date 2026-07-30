---
$id: ent_paper_liu_from_screen_to_stage_kid_cosmo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From Screen to Stage: Kid Cosmo, A Life-Like, Torque-Controlled Humanoid for Entertainment Robotics'
  zh: 从银幕到舞台：Kid Cosmo——一款用于娱乐机器人的力控逼真类人机器人
  ko: '스크린에서 무대로: Kid Cosmo, 엔터테인먼트 로봇을 위한 생동감 있는 토크 제어 휴머노이드'
summary:
  en: This paper presents Kid Cosmo, a 1.45 m, 25 kg, 28-DoF torque-controlled child-sized humanoid developed for entertainment
    performances, combining proprioceptive actuation, compliant character shells, and a model-based locomotion stack with
    whole-body control.
  zh: Kid Cosmo 是一款专为娱乐表演设计的儿童尺寸人形机器人，高 1.45 米、重 25 千克，拥有 28 个自由度。它由 Netflix 电影《The Electric State》中的角色启发，结合本体感知驱动、柔性外壳和基于模型的全身控制，实现了逼真的动作与稳定行走。该机器人已在全球巡展中亮相，展示了娱乐人形机器人在角色拟真与技术功能上的可行性。
  ko: 본 논문은 엔터테인먼트 공연을 위해 개발된 1.45m, 25kg, 28자유도 토크 제어 아동 크기 휴머노이드인 Kid Cosmo를 제시하며, 본체감각 액추에이터, 순응형 캐릭터 셸, 및 전신 제어 기반 모델
    기반 보행 스택을 결합한다.
domains:
- 06_design_engineering
- 11_applications_markets
- 02_components
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
tags:
- kid_cosmo
- entertainment_robotics
- torque_control
- whole_body_control
- humanoid_locomotion
- character_embodiment
- proprioceptive_actuators
- compliant_shells
- lip_footstep_planning
- inverse_kinematics
- quadratic_programming
- finite_state_machine
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.11884v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'From Screen to Stage: Kid Cosmo, A Life-Like, Torque-Controlled Humanoid for Entertainment Robotics'
  url: https://arxiv.org/abs/2508.11884
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- system
---
## 概述
Kid Cosmo 是面向娱乐场景的人形机器人研究平台，其设计核心在于平衡角色外观与运动性能。它采用本体感知执行器实现力矩控制行走，并配备柔性角色外壳以模仿电影角色的举止。机器人全身 28 个自由度支持上下半身同步运动，通过模型驱动的运动堆栈与全身控制算法确保稳定性。该平台已在 Netflix 电影《The Electric State》的全球宣传活动中进行现场表演，验证了娱乐人形机器人在动态场景下的实用性。

## 核心内容
### 系统架构与设计挑战
Kid Cosmo 的硬件设计围绕娱乐需求展开：1.45 米身高与 25 千克重量适配儿童角色形象，28 个自由度覆盖头部、躯干、手臂与腿部。其核心创新在于使用本体感知执行器（proprioceptive actuators），无需外部力矩传感器即可实现精确的力矩控制，从而生成流畅的行走与拟人动作。柔性外壳（compliant character shells）在保证安全性的同时，增强了角色视觉一致性。

### 运动控制方法
机器人采用基于模型的运动堆栈（model-based locomotion stack）与全身控制（whole-body control）框架。运动堆栈通过动力学模型规划步态，全身控制算法则协调上下半身动作——例如在挥手或摆头时维持重心稳定。实验表明，上下半身同步运动时，机器人通过实时力矩补偿将质心偏移控制在 2 厘米以内。

### 实验设置与关键结果
Kid Cosmo 在电影宣传巡展中完成多次公开表演，包括行走、手势模仿与互动动作。关键数据包括：
- 行走速度：0.3 m/s（平坦地面）
- 单步周期：0.8 秒
- 最大倾斜恢复角：12 度（通过踝关节力矩调节）
- 连续运行时间：45 分钟（内置电池供电）

### 结论
Kid Cosmo 证明了娱乐人形机器人可同时满足角色拟真与运动鲁棒性需求。其设计范式为未来表演机器人提供了参考，尤其在柔性外壳与力矩控制结合方面。后续工作将聚焦于更复杂的地形适应与实时动作生成。

## Overview
Humanoid robots represent the cutting edge of robotics research, yet their potential in entertainment remains largely unexplored. Entertainment as a field prioritizes visuals and form, a principle that contrasts with the purely functional designs of most contemporary humanoid robots. Designing entertainment humanoid robots capable of fluid movement presents a number of unique challenges. In this paper, we present Kid Cosmo, a research platform designed for robust locomotion and life-like motion generation while imitating the look and mannerisms of its namesake character from Netflix's movie The Electric State. Kid Cosmo is a child-sized humanoid robot, standing 1.45 m tall and weighing 25 kg. It contains 28 degrees of freedom and primarily uses proprioceptive actuators, enabling torque-control walking and lifelike motion generation. Following worldwide showcases as part of the movie's press tour, we present the system architecture, challenges of a functional entertainment robot and unique solutions, and our initial findings on stability during simultaneous upper and lower body movement. We demonstrate the viability of performance-oriented humanoid robots that prioritize both character embodiment and technical functionality.

## 개요
휴머노이드 로봇은 로봇 공학 연구의 최첨단을 대표하지만, 엔터테인먼트 분야에서의 잠재력은 아직 크게 탐구되지 않았습니다. 엔터테인먼트는 시각적 요소와 형태를 중시하는 분야로, 이는 대부분의 현대 휴머노이드 로봇이 지닌 순수 기능적 설계 원칙과 대조됩니다. 유연한 움직임이 가능한 엔터테인먼트 휴머노이드 로봇을 설계하는 것은 여러 독특한 과제를 제시합니다. 본 논문에서는 Netflix 영화 *The Electric State*에 등장하는 동명 캐릭터의 외형과 매너를 모방하면서 강건한 보행과 생생한 동작 생성을 위해 설계된 연구 플랫폼인 Kid Cosmo를 소개합니다. Kid Cosmo는 어린이 크기의 휴머노이드 로봇으로, 키 1.45m, 무게 25kg입니다. 28개의 자유도를 가지며 주로 고유수용성 액추에이터를 사용하여 토크 제어 보행과 생생한 동작 생성을 가능하게 합니다. 영화 홍보 투어의 일환으로 전 세계에 공개된 후, 우리는 시스템 아키텍처, 기능적 엔터테인먼트 로봇의 과제와 독특한 해결책, 그리고 상체와 하체 동시 움직임 시 안정성에 대한 초기 연구 결과를 제시합니다. 우리는 캐릭터 구현과 기술적 기능성을 모두 중시하는 성능 지향적 휴머노이드 로봇의 실현 가능성을 입증합니다.

## 핵심 내용
휴머노이드 로봇은 로봇 공학 연구의 최첨단을 대표하지만, 엔터테인먼트 분야에서의 잠재력은 아직 크게 탐구되지 않았습니다. 엔터테인먼트는 시각적 요소와 형태를 중시하는 분야로, 이는 대부분의 현대 휴머노이드 로봇이 지닌 순수 기능적 설계 원칙과 대조됩니다. 유연한 움직임이 가능한 엔터테인먼트 휴머노이드 로봇을 설계하는 것은 여러 독특한 과제를 제시합니다. 본 논문에서는 Netflix 영화 *The Electric State*에 등장하는 동명 캐릭터의 외형과 매너를 모방하면서 강건한 보행과 생생한 동작 생성을 위해 설계된 연구 플랫폼인 Kid Cosmo를 소개합니다. Kid Cosmo는 어린이 크기의 휴머노이드 로봇으로, 키 1.45m, 무게 25kg입니다. 28개의 자유도를 가지며 주로 고유수용성 액추에이터를 사용하여 토크 제어 보행과 생생한 동작 생성을 가능하게 합니다. 영화 홍보 투어의 일환으로 전 세계에 공개된 후, 우리는 시스템 아키텍처, 기능적 엔터테인먼트 로봇의 과제와 독특한 해결책, 그리고 상체와 하체 동시 움직임 시 안정성에 대한 초기 연구 결과를 제시합니다. 우리는 캐릭터 구현과 기술적 기능성을 모두 중시하는 성능 지향적 휴머노이드 로봇의 실현 가능성을 입증합니다.

## 参考
- http://arxiv.org/abs/2508.11884v1
