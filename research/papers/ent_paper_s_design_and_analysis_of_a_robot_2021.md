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
  zh: Rajashekhar 等人提出了一种基于五杆机构集成的仿生机器人蜥蜴，通过矢量环法推导了其位置运动学，并利用伺服电机驱动的原型验证了行走步态。核心贡献在于将两个五杆机构以特定顺序连接，形成四足运动结构，实现了粗糙地形的仿生移动。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2107.12614v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该研究针对足式机器人在崎岖地形中的移动需求，设计了一种新型仿生蜥蜴机器人。其核心机构由两个五杆机构通过特定顺序连接而成，形成额外的两个子机构，腿部直接附着于五杆机构的连杆上。当机构被驱动时，连杆运动带动腿部实现前进。作者采用矢量环法完成了机构的位置运动学分析，并搭建了伺服电机驱动的物理原型，成功演示了行走步态。

## 核心内容
### 机构设计
- 机器人采用两个五杆机构作为基础，通过特定顺序连接连杆，衍生出另外两个子机构，共同构成四足运动框架。
- 腿部直接固定在五杆机构的连杆上，当伺服电机驱动机构时，连杆的周期性运动转化为腿部的摆动与支撑，推动机器人前进。

### 运动学分析
- 使用矢量环法（vector-loop method）对五杆机构进行位置运动学推导，建立了各连杆角度与末端执行器（腿部）位置之间的数学关系。
- 该分析为后续的步态规划与控制提供了理论依据，确保机构在运动过程中满足闭环约束。

### 原型验证
- 搭建了物理原型，采用伺服电机作为驱动源，控制五杆机构的关节角度。
- 实验成功演示了机器人蜥蜴的行走步态，验证了机构设计的可行性与运动学模型的正确性。

## Overview
Legged robots are being used to explore rough terrains as they are capable of traversing gaps and obstacles. In this paper, a new mechanism is designed to replicate a robotic lizard using integrated five-bar mechanisms. There are two five bar mechanisms from which two more are formed by connecting the links in a particular order. The legs are attached to the links of the five bar mechanism such that, when the mechanism is actuated, they move the robot forward. Position analysis using vector loop approach has been done for the mechanism. A prototype has been built and controlled using servo motors to verify the robotic lizard mechanism.

## Overview
Legged robots are being used to explore rough terrains as they are capable of traversing gaps and obstacles. In this paper, a new mechanism is designed to replicate a robotic lizard using integrated five-bar mechanisms. There are two five-bar mechanisms from which two more are formed by connecting the links in a particular order. The legs are attached to the links of the five-bar mechanism such that, when the mechanism is actuated, they move the robot forward. Position analysis using the vector loop approach has been done for the mechanism. A prototype has been built and controlled using servo motors to verify the robotic lizard mechanism.

## Content
Legged robots are being used to explore rough terrains as they are capable of traversing gaps and obstacles. In this paper, a new mechanism is designed to replicate a robotic lizard using integrated five-bar mechanisms. There are two five-bar mechanisms from which two more are formed by connecting the links in a particular order. The legs are attached to the links of the five-bar mechanism such that, when the mechanism is actuated, they move the robot forward. Position analysis using the vector loop approach has been done for the mechanism. A prototype has been built and controlled using servo motors to verify the robotic lizard mechanism.

## 개요
다리형 로봇은 틈새와 장애물을 통과할 수 있어 거친 지형 탐사에 사용되고 있습니다. 본 논문에서는 통합된 5절 링크 메커니즘을 활용하여 도마뱀 로봇을 재현하는 새로운 메커니즘을 설계했습니다. 두 개의 5절 링크 메커니즘이 있으며, 특정 순서로 링크를 연결하여 추가로 두 개의 메커니즘이 형성됩니다. 다리는 5절 링크 메커니즘의 링크에 부착되어, 메커니즘이 작동될 때 로봇을 앞으로 움직이게 합니다. 벡터 루프 방식을 이용한 위치 해석이 메커니즘에 대해 수행되었습니다. 프로토타입이 제작되었으며, 서보 모터를 사용하여 제어함으로써 도마뱀 로봇 메커니즘을 검증했습니다.

## 핵심 내용
다리형 로봇은 틈새와 장애물을 통과할 수 있어 거친 지형 탐사에 사용되고 있습니다. 본 논문에서는 통합된 5절 링크 메커니즘을 활용하여 도마뱀 로봇을 재현하는 새로운 메커니즘을 설계했습니다. 두 개의 5절 링크 메커니즘이 있으며, 특정 순서로 링크를 연결하여 추가로 두 개의 메커니즘이 형성됩니다. 다리는 5절 링크 메커니즘의 링크에 부착되어, 메커니즘이 작동될 때 로봇을 앞으로 움직이게 합니다. 벡터 루프 방식을 이용한 위치 해석이 메커니즘에 대해 수행되었습니다. 프로토타입이 제작되었으며, 서보 모터를 사용하여 제어함으로써 도마뱀 로봇 메커니즘을 검증했습니다.

## 参考
- http://arxiv.org/abs/2107.12614v1
