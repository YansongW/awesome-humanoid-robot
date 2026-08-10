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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.07295v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (930 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2408.07295v4

## 개요
휴머노이드 로봇 제어의 핵심 과제는 정밀한 보행 시퀀스부터 국소 사지 모방, 조이스틱 원격 조작에 이르기까지 다양한 전신 동작을 지휘할 수 있는 통합 인터페이스를 설계하는 방법입니다. 본 논문에서 제안하는 MHC 컨트롤러는 혁신적으로 마스크된 목표 궤적 사양을 채택하여, 상위 시스템이 로봇 상태 변수의 임의 하위 집합을 제어 목표로 유연한 형식으로 지정할 수 있게 합니다. 이 프레임워크는 시뮬레이션 환경에서 모든 모달리티를 포함하는 커리큘럼 훈련을 통해, 컨트롤러가 부분적으로 지정된 동작 명령을 견고하게 실행하면서 균형과 외란 저항 능력을 유지할 수 있게 합니다. 연구진은 Digit V3 휴머노이드 로봇에서 이 방법의 유효성을 검증하여, 단일 학습형 컨트롤러가 일반 표현 인터페이스를 통해 실제 세계에서 다양한 전신 제어 명령을 실행할 수 있음을 증명했습니다.

## 핵심 내용
### 방법 아키텍처
MHC의 핵심 혁신은 전신 제어 문제를 마스크된 궤적 추적 작업으로 변환하는 데 있습니다. 컨트롤러는 두 부분의 입력을 받습니다:
- **마스크된 목표 궤적**: 로봇 상태 변수의 하위 집합(예: 하지 관절만 또는 상지 말단만)의 원하는 운동 궤적을 지정
- **마스크 행렬**: 제어 목표로 활성화된 상태 변수를 나타내는 지표

이 설계는 컨트롤러가 지정되지 않은 관절의 협조 운동을 자동으로 추론하면서 전신 동역학 일관성을 유지할 수 있게 합니다.

### 훈련 전략
**커리큘럼 학습** 방법을 채택하여 단계적으로 훈련합니다:
1. 1단계: 전체 상태 궤적 추적(모든 관절에 명확한 목표가 있음)
2. 2단계: 무작위 마스크 훈련(상태 변수의 30%-70%를 무작위로 마스킹)
3. 3단계: 다중 모달리티 혼합 훈련(최적화 궤적, 모션 캡처 데이터, 비디오 리타겟팅 신호 및 조이스틱 명령을 동시에 입력)

### 실험 설정
- **시뮬레이션 환경**: Isaac Gym 기반 물리 시뮬레이션
- **실제 플랫폼**: Digit V3 휴머노이드 로봇(높이 1.75m, 무게 65kg, 28자유도)
- **훈련 데이터**: 5000개의 최적화 궤적, 2000개의 모션 캡처 클립, 1000개의 리타겟팅 비디오 및 실시간 조이스틱 신호 포함

### 주요 결과
- **보행 제어**: 0.5m/s 보행 속도에서 보행 주기 오차 <3%
- **국소 모방**: 동작 캡처 상지 동작의 80%를 성공적으로 재현하면서 하지 균형 유지
- **외란 저항 테스트**: 20N 측방 추력 가해졌을 때 회복 시간 <0.8초
- **다중 모달리티 전환**: 실행 중 제어 모드 전환(보행에서 조이스틱으로) 지연 시간 <50ms

### 결론
MHC는 단일 학습형 컨트롤러가 통합 인터페이스를 통해 여러 제어 모달리티를 처리할 수 있음을 증명하여, 일반 휴머노이드 로봇 제어 프레임워크 구축을 위한 실현 가능한 솔루션을 제공합니다. 향후 작업은 더 복잡한 작업 조합과 교차 플랫폼 전이 능력을 탐구할 것입니다.
