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
  zh: 本文介绍了 Kid Cosmo，一款身高 1.45 米、重 25 千克、具有 28 自由度的力控儿童尺寸人形机器人，面向娱乐表演，结合了本体感知驱动、柔顺的角色外壳以及基于模型的全身控制运动栈。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.11884v1.
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
Humanoid robots represent the cutting edge of robotics research, yet their potential in entertainment remains largely unexplored. Entertainment as a field prioritizes visuals and form, a principle that contrasts with the purely functional designs of most contemporary humanoid robots. Designing entertainment humanoid robots capable of fluid movement presents a number of unique challenges. In this paper, we present Kid Cosmo, a research platform designed for robust locomotion and life-like motion generation while imitating the look and mannerisms of its namesake character from Netflix's movie The Electric State. Kid Cosmo is a child-sized humanoid robot, standing 1.45 m tall and weighing 25 kg. It contains 28 degrees of freedom and primarily uses proprioceptive actuators, enabling torque-control walking and lifelike motion generation. Following worldwide showcases as part of the movie's press tour, we present the system architecture, challenges of a functional entertainment robot and unique solutions, and our initial findings on stability during simultaneous upper and lower body movement. We demonstrate the viability of performance-oriented humanoid robots that prioritize both character embodiment and technical functionality.

## 核心内容
Humanoid robots represent the cutting edge of robotics research, yet their potential in entertainment remains largely unexplored. Entertainment as a field prioritizes visuals and form, a principle that contrasts with the purely functional designs of most contemporary humanoid robots. Designing entertainment humanoid robots capable of fluid movement presents a number of unique challenges. In this paper, we present Kid Cosmo, a research platform designed for robust locomotion and life-like motion generation while imitating the look and mannerisms of its namesake character from Netflix's movie The Electric State. Kid Cosmo is a child-sized humanoid robot, standing 1.45 m tall and weighing 25 kg. It contains 28 degrees of freedom and primarily uses proprioceptive actuators, enabling torque-control walking and lifelike motion generation. Following worldwide showcases as part of the movie's press tour, we present the system architecture, challenges of a functional entertainment robot and unique solutions, and our initial findings on stability during simultaneous upper and lower body movement. We demonstrate the viability of performance-oriented humanoid robots that prioritize both character embodiment and technical functionality.

## 参考
- http://arxiv.org/abs/2508.11884v1

## Overview
Humanoid robots represent the cutting edge of robotics research, yet their potential in entertainment remains largely unexplored. Entertainment as a field prioritizes visuals and form, a principle that contrasts with the purely functional designs of most contemporary humanoid robots. Designing entertainment humanoid robots capable of fluid movement presents a number of unique challenges. In this paper, we present Kid Cosmo, a research platform designed for robust locomotion and life-like motion generation while imitating the look and mannerisms of its namesake character from Netflix's movie The Electric State. Kid Cosmo is a child-sized humanoid robot, standing 1.45 m tall and weighing 25 kg. It contains 28 degrees of freedom and primarily uses proprioceptive actuators, enabling torque-control walking and lifelike motion generation. Following worldwide showcases as part of the movie's press tour, we present the system architecture, challenges of a functional entertainment robot and unique solutions, and our initial findings on stability during simultaneous upper and lower body movement. We demonstrate the viability of performance-oriented humanoid robots that prioritize both character embodiment and technical functionality.

## Content
Humanoid robots represent the cutting edge of robotics research, yet their potential in entertainment remains largely unexplored. Entertainment as a field prioritizes visuals and form, a principle that contrasts with the purely functional designs of most contemporary humanoid robots. Designing entertainment humanoid robots capable of fluid movement presents a number of unique challenges. In this paper, we present Kid Cosmo, a research platform designed for robust locomotion and life-like motion generation while imitating the look and mannerisms of its namesake character from Netflix's movie The Electric State. Kid Cosmo is a child-sized humanoid robot, standing 1.45 m tall and weighing 25 kg. It contains 28 degrees of freedom and primarily uses proprioceptive actuators, enabling torque-control walking and lifelike motion generation. Following worldwide showcases as part of the movie's press tour, we present the system architecture, challenges of a functional entertainment robot and unique solutions, and our initial findings on stability during simultaneous upper and lower body movement. We demonstrate the viability of performance-oriented humanoid robots that prioritize both character embodiment and technical functionality.

## 개요
휴머노이드 로봇은 로봇 공학 연구의 최첨단을 대표하지만, 엔터테인먼트 분야에서의 잠재력은 아직 크게 탐구되지 않았습니다. 엔터테인먼트는 시각적 요소와 형태를 중시하는 분야로, 이는 대부분의 현대 휴머노이드 로봇이 지닌 순수 기능적 설계 원칙과 대조됩니다. 유연한 움직임이 가능한 엔터테인먼트 휴머노이드 로봇을 설계하는 것은 여러 독특한 과제를 제시합니다. 본 논문에서는 Netflix 영화 *The Electric State*에 등장하는 동명 캐릭터의 외형과 매너를 모방하면서 강건한 보행과 생생한 동작 생성을 위해 설계된 연구 플랫폼인 Kid Cosmo를 소개합니다. Kid Cosmo는 어린이 크기의 휴머노이드 로봇으로, 키 1.45m, 무게 25kg입니다. 28개의 자유도를 가지며 주로 고유수용성 액추에이터를 사용하여 토크 제어 보행과 생생한 동작 생성을 가능하게 합니다. 영화 홍보 투어의 일환으로 전 세계에 공개된 후, 우리는 시스템 아키텍처, 기능적 엔터테인먼트 로봇의 과제와 독특한 해결책, 그리고 상체와 하체 동시 움직임 시 안정성에 대한 초기 연구 결과를 제시합니다. 우리는 캐릭터 구현과 기술적 기능성을 모두 중시하는 성능 지향적 휴머노이드 로봇의 실현 가능성을 입증합니다.

## 핵심 내용
휴머노이드 로봇은 로봇 공학 연구의 최첨단을 대표하지만, 엔터테인먼트 분야에서의 잠재력은 아직 크게 탐구되지 않았습니다. 엔터테인먼트는 시각적 요소와 형태를 중시하는 분야로, 이는 대부분의 현대 휴머노이드 로봇이 지닌 순수 기능적 설계 원칙과 대조됩니다. 유연한 움직임이 가능한 엔터테인먼트 휴머노이드 로봇을 설계하는 것은 여러 독특한 과제를 제시합니다. 본 논문에서는 Netflix 영화 *The Electric State*에 등장하는 동명 캐릭터의 외형과 매너를 모방하면서 강건한 보행과 생생한 동작 생성을 위해 설계된 연구 플랫폼인 Kid Cosmo를 소개합니다. Kid Cosmo는 어린이 크기의 휴머노이드 로봇으로, 키 1.45m, 무게 25kg입니다. 28개의 자유도를 가지며 주로 고유수용성 액추에이터를 사용하여 토크 제어 보행과 생생한 동작 생성을 가능하게 합니다. 영화 홍보 투어의 일환으로 전 세계에 공개된 후, 우리는 시스템 아키텍처, 기능적 엔터테인먼트 로봇의 과제와 독특한 해결책, 그리고 상체와 하체 동시 움직임 시 안정성에 대한 초기 연구 결과를 제시합니다. 우리는 캐릭터 구현과 기술적 기능성을 모두 중시하는 성능 지향적 휴머노이드 로봇의 실현 가능성을 입증합니다.
