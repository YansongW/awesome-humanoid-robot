---
$id: ent_paper_s_design_and_analysis_of_a_robot_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Design and Analysis of a Robotic Lizard using Five-Bar Mechanisms
  zh: 采用五杆机构的机器蜥蜴设计与分析
  ko: 5절 링크 메커니즘을 이용한 로봇 도마뱀의 설계 및 분석
summary:
  en: Rajashekhar et al. present a robotic lizard built from integrated five-bar mechanisms, derive its position kinematics
    via the vector-loop method, and demonstrate a walking gait with a servo-driven prototype.
  zh: Legged robots are being used to explore rough terrains as they are capable of traversing gaps and obstacles. In this
    paper, a new mechanism is designed to replicate a robotic lizard using integrated five-bar mechanisms. There are two five
    bar mechanisms from which two more are formed by connecting the links in a particular order. The legs are attached to
    the links of the five bar mechanism such that, when the mechanism is actuated, they move the robot forward. Position analysis
    using vector loop approach has been done for the mechanism. A prototype has been built and controlled using servo mot
  ko: Rajashekhar 등은 통합된 5절 링크 메커니즘으로 구성된 로봇 도마뱀을 제안하고, 벡터 루프법으로 위치 운동학을 분석하며, 서보 모터로 구동되는 프로토타입으로 보행 동작을 입증한다.
domains:
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- five_bar_mechanism
- bio_inspired_robotics
- quadruped_locomotion
- linkage_kinematics
- servo_actuation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2107.12614v1.
sources:
- id: src_001
  type: paper
  title: Design and Analysis of a Robotic Lizard using Five-Bar Mechanisms
  url: https://arxiv.org/abs/2107.12614
  date: '2021'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## 概述
Legged robots are being used to explore rough terrains as they are capable of traversing gaps and obstacles. In this paper, a new mechanism is designed to replicate a robotic lizard using integrated five-bar mechanisms. There are two five bar mechanisms from which two more are formed by connecting the links in a particular order. The legs are attached to the links of the five bar mechanism such that, when the mechanism is actuated, they move the robot forward. Position analysis using vector loop approach has been done for the mechanism. A prototype has been built and controlled using servo motors to verify the robotic lizard mechanism.

## 核心内容
Legged robots are being used to explore rough terrains as they are capable of traversing gaps and obstacles. In this paper, a new mechanism is designed to replicate a robotic lizard using integrated five-bar mechanisms. There are two five bar mechanisms from which two more are formed by connecting the links in a particular order. The legs are attached to the links of the five bar mechanism such that, when the mechanism is actuated, they move the robot forward. Position analysis using vector loop approach has been done for the mechanism. A prototype has been built and controlled using servo motors to verify the robotic lizard mechanism.

## 参考
- http://arxiv.org/abs/2107.12614v1


