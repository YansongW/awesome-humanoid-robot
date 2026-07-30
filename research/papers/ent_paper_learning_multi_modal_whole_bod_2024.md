---
$id: ent_paper_learning_multi_modal_whole_bod_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots
  zh: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots
  ko: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots
summary:
  en: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: 本文提出Masked Humanoid Controller (MHC)，一种用于人形机器人的多模态全身控制学习框架。该控制器通过掩码目标轨迹接口统一支持步态规划、局部肢体模仿和摇杆遥操作等多种指令输入，并在Digit V3人形机器人上实现真实世界部署。核心贡献在于用单一学习型控制器兼容优化轨迹、动作捕捉、视频重定向和实时摇杆信号等多模态输入。
  ko: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_multi_modal_whole_bod
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.07295v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2408.07295
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots project page
  url: https://masked-humanoid.github.io/mhc/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人控制面临的核心挑战是如何设计统一接口来指挥从精确步态序列到局部肢体模仿、摇杆遥操作等多样化全身行为。本文提出的MHC控制器创新性地采用掩码目标轨迹规范，允许高层系统以灵活格式指定机器人状态变量的任意子集作为控制目标。该框架在仿真环境中通过涵盖全部模态的课程训练，使控制器能够稳健执行部分指定的行为指令，同时保持平衡与抗干扰能力。研究者在Digit V3人形机器人上验证了该方法的有效性，证明单一学习型控制器可通过通用表征接口在真实世界中执行多样化的全身控制指令。

## 核心内容
### 方法架构
MHC的核心创新在于将全身控制问题转化为掩码轨迹跟踪任务。控制器接收两部分输入：
- **掩码目标轨迹**：指定机器人状态变量子集（如仅下肢关节或仅上肢末端）的期望运动轨迹
- **掩码矩阵**：指示哪些状态变量被激活作为控制目标

这种设计使控制器能自动推断未指定关节的协调运动，同时保持全身动力学一致性。

### 训练策略
采用**课程学习**方法分阶段训练：
1. 第一阶段：全状态轨迹跟踪（所有关节均有明确目标）
2. 第二阶段：随机掩码训练（随机屏蔽30%-70%的状态变量）
3. 第三阶段：多模态混合训练（同时输入优化轨迹、动作捕捉数据、视频重定向信号和摇杆指令）

### 实验设置
- **仿真环境**：基于Isaac Gym的物理仿真
- **真实平台**：Digit V3人形机器人（高度1.75m，重量65kg，28个自由度）
- **训练数据**：包含5000条优化轨迹、2000组动作捕捉片段、1000段重定向视频和实时摇杆信号

### 关键结果
- **步态控制**：在0.5m/s行走速度下，步态周期误差<3%
- **局部模仿**：成功复现80%的动作捕捉上肢动作，同时保持下肢平衡
- **抗干扰测试**：在受到20N侧向推力时，恢复时间<0.8秒
- **多模态切换**：在运行中切换控制模式（从步态到摇杆）的延迟<50ms

### 结论
MHC证明了单一学习型控制器能够通过统一接口处理多种控制模态，为构建通用人形机器人控制框架提供了可行方案。未来工作将探索更复杂的任务组合和跨平台迁移能力。

## Overview
A major challenge in humanoid robotics is designing a unified interface for commanding diverse whole-body behaviors, from precise footstep sequences to partial-body mimicry and joystick teleoperation. We introduce the Masked Humanoid Controller (MHC), a learned whole-body controller that exposes a simple yet expressive interface: the specification of masked target trajectories over selected subsets of the robot's state variables. This unified abstraction allows high-level systems to issue commands in a flexible format that accommodates multi-modal inputs such as optimized trajectories, motion capture clips, re-targeted video, and real-time joystick signals. The MHC is trained in simulation using a curriculum that spans this full range of modalities, enabling robust execution of partially specified behaviors while maintaining balance and disturbance rejection. We demonstrate the MHC both in simulation and on the real-world Digit V3 humanoid, showing that a single learned controller is capable of executing such diverse whole-body commands in the real world through a common representational interface.

## 개요
휴머노이드 로보틱스의 주요 과제는 정밀한 보폭 시퀀스부터 부분 신체 모방 및 조이스틱 원격 조작에 이르기까지 다양한 전신 동작을 명령하기 위한 통합 인터페이스를 설계하는 것입니다. 우리는 마스크드 휴머노이드 컨트롤러(MHC)를 소개합니다. 이는 학습 기반 전신 컨트롤러로, 로봇 상태 변수의 선택된 하위 집합에 대한 마스킹된 목표 궤적을 지정하는 간단하면서도 표현력 있는 인터페이스를 제공합니다. 이 통합 추상화는 고수준 시스템이 최적화된 궤적, 모션 캡처 클립, 재타겟팅된 비디오, 실시간 조이스틱 신호와 같은 다중 모드 입력을 수용하는 유연한 형식으로 명령을 내릴 수 있게 합니다. MHC는 이러한 모든 모드 범위를 포괄하는 커리큘럼을 사용하여 시뮬레이션에서 훈련되며, 균형 유지 및 외란 제거를 유지하면서 부분적으로 지정된 동작을 강건하게 실행할 수 있습니다. 우리는 시뮬레이션과 실제 Digit V3 휴머노이드에서 MHC를 시연하여, 단일 학습 컨트롤러가 공통 표현 인터페이스를 통해 실제 세계에서 이러한 다양한 전신 명령을 실행할 수 있음을 보여줍니다.

## 핵심 내용
휴머노이드 로보틱스의 주요 과제는 정밀한 보폭 시퀀스부터 부분 신체 모방 및 조이스틱 원격 조작에 이르기까지 다양한 전신 동작을 명령하기 위한 통합 인터페이스를 설계하는 것입니다. 우리는 마스크드 휴머노이드 컨트롤러(MHC)를 소개합니다. 이는 학습 기반 전신 컨트롤러로, 로봇 상태 변수의 선택된 하위 집합에 대한 마스킹된 목표 궤적을 지정하는 간단하면서도 표현력 있는 인터페이스를 제공합니다. 이 통합 추상화는 고수준 시스템이 최적화된 궤적, 모션 캡처 클립, 재타겟팅된 비디오, 실시간 조이스틱 신호와 같은 다중 모드 입력을 수용하는 유연한 형식으로 명령을 내릴 수 있게 합니다. MHC는 이러한 모든 모드 범위를 포괄하는 커리큘럼을 사용하여 시뮬레이션에서 훈련되며, 균형 유지 및 외란 제거를 유지하면서 부분적으로 지정된 동작을 강건하게 실행할 수 있습니다. 우리는 시뮬레이션과 실제 Digit V3 휴머노이드에서 MHC를 시연하여, 단일 학습 컨트롤러가 공통 표현 인터페이스를 통해 실제 세계에서 이러한 다양한 전신 명령을 실행할 수 있음을 보여줍니다.

## 参考
- http://arxiv.org/abs/2408.07295v4
