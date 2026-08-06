---
$id: ent_paper_luo_ceer_compliant_end_effector_an_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation'
  zh: CEER：作为分层人形机器人移动操作统一接口的柔顺末端执行器与根控制
  ko: 'CEER: 계층형 휴머노이드 로코-매니퓰레이션을 위한 통합 인터페이스로서의 순응적 최종 효과기 및 루트 제어'
summary:
  en: CEER proposes a compliant end-effector and root (EE-root) control abstraction for humanoid loco-manipulation, training
    a low-level policy via teacher-student distillation from a whole-body motion tracker so that heterogeneous high-level
    planners can command the robot without retraining.
  zh: CEER 提出了一种用于人形机器人全身移动操作的分层控制抽象，通过端-根（EE-root）指令实现柔顺控制。该方法采用教师-学生蒸馏框架，将全身运动跟踪策略转化为仅依赖端-根命令的低层策略，支持异构高层规划器即插即用，无需重新训练。实验表明，该方法在仿真和硬件上实现了
    3.3 cm 的末端执行器跟踪精度，并显著降低了加加速度。
  ko: CEER는 휴머노이드 로코-매니퓰레이션을 위한 순응적 최종 효과기-루트(EE-root) 제어 추상화를 제안하며, 전신 동작 추적기로부터 교사-학생 증류를 통해 저수준 정책을 학습시켜 재학습 없이 이종 고수준
    플래너가 로봇을 명령할 수 있게 한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- whole_body_control
- end_effector_control
- loco_manipulation
- hierarchical_planning
- teacher_student_distillation
- compliant_control
- humanoid_robotics
- motion_tracking
- sim_to_real
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.19981v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP1 dedup merge 2026-08-06: merged
    ent_paper_luo_ceer_compliant_end_effector_an_2026 into this card (rules: same_title_same_year). Backup+manifest: .staging/cleanup_wp12/.'
sources:
- id: src_001
  type: paper
  title: 'CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2605.19981
  date: '2026'
  accessed_at: '2026-06-26'
- id: src_002
  type: website
  title: CEER project page
  url: https://robotproject8.github.io/ceer_page/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
人形机器人在移动操作中面临接触丰富和长时域任务的挑战，传统关节空间跟踪方法难以兼顾柔顺性与模块化。CEER 提出了一种基于末端执行器和根部（EE-root）指令的柔顺控制抽象，将全身控制映射到可解释的任务空间。通过教师-学生蒸馏，一个通用运动跟踪控制器被压缩为仅响应端-根命令的低层策略，从而允许不同高层规划器（如运动规划器或强化学习策略）直接接入。在仿真和硬件实验中，该方法在遥操作接触任务中表现出稳定性能，并在房间尺度场景下的单物体移动操作任务中实现了高达 70% 的成功率。

## 核心内容
### 方法架构
- **EE-root 控制抽象**：将人形机器人的全身控制分解为根部运动命令（如线速度、角速度）和末端执行器位姿目标（位置与姿态），形成可解释的任务空间。
- **教师-学生蒸馏框架**：
  - **教师策略**：基于全身运动跟踪控制器，使用关节空间指令实现精确运动跟踪。
  - **学生策略**：仅接收 EE-root 命令作为输入，通过蒸馏学习模仿教师策略的输出，从而消除对关节级信息的依赖。
- **分层规划系统**：高层规划器（如运动规划器、强化学习策略或遥操作接口）通过 EE-root 接口与低层策略交互，无需针对不同任务重新训练低层控制器。

### 实验设置与关键数字
- **仿真环境**：使用 Isaac Gym 进行训练，并在房间尺度场景中测试单物体移动操作任务。
- **硬件平台**：基于 Unitree H1 人形机器人，配备力/扭矩传感器和关节编码器。
- **跟踪精度**：末端执行器位置跟踪误差为 3.3 cm，相比基线方法（如纯位置控制）显著降低了加加速度（jerk）。
- **任务成功率**：在仿真中，单物体移动操作任务（如抓取并放置物体）的成功率达到 70%。
- **遥操作验证**：在硬件上通过遥操作实现接触丰富的操作任务（如推门、搬运物体），展示了稳定的柔顺交互能力。

### 结论
CEER 通过 EE-root 控制抽象实现了人形机器人移动操作的模块化与可扩展性，其柔顺控制特性在接触丰富的任务中优于传统方法。该框架支持异构规划器的无缝集成，为复杂长时域操作任务提供了实用解决方案。

## Overview
Humanoid robots have achieved impressive locomotion performance, yet contact-rich and long-horizon manipulation remains a major bottleneck. Manipulation is inherently contact-rich and demands compliant whole-body control for stable interaction, while its diversity and long-horizon nature favor modular, planner-compatible interfaces over joint-space tracking.   We propose CEER, a compliant end-effector-root (EE-root) control abstraction for modular humanoid loco-manipulation within a hierarchical planning framework. CEER enables compliance-aware whole-body control in an interpretable task space defined by root motion commands and end-effector pose targets, and supports plug-and-play integration with heterogeneous high-level planners. A teacher-student framework is adopted to distill a general motion-tracking controller into a low-level policy that consumes only EE-root commands.   We further construct a hierarchical system that integrates heterogeneous planners and task modules through the EE-root interface, enabling diverse manipulation tasks without retraining the underlying whole-body policy. Experiments in simulation and on hardware demonstrate 3.3 cm end-effector tracking accuracy with substantially reduced jerk compared to baselines, stable contact-rich manipulation under teleoperation, and up to 70% success in simulated single-object loco-manipulation tasks within a room-scale environment. These results indicate that compliant EE-root control provides a practical abstraction for humanoid loco-manipulation, enabling modular and scalable integration of diverse skills.

## Overview
Humanoid robots have achieved impressive locomotion performance, yet contact-rich and long-horizon manipulation remains a major bottleneck. Manipulation is inherently contact-rich and demands compliant whole-body control for stable interaction, while its diversity and long-horizon nature favor modular, planner-compatible interfaces over joint-space tracking. We propose CEER, a compliant end-effector-root (EE-root) control abstraction for modular humanoid loco-manipulation within a hierarchical planning framework. CEER enables compliance-aware whole-body control in an interpretable task space defined by root motion commands and end-effector pose targets, and supports plug-and-play integration with heterogeneous high-level planners. A teacher-student framework is adopted to distill a general motion-tracking controller into a low-level policy that consumes only EE-root commands. We further construct a hierarchical system that integrates heterogeneous planners and task modules through the EE-root interface, enabling diverse manipulation tasks without retraining the underlying whole-body policy. Experiments in simulation and on hardware demonstrate 3.3 cm end-effector tracking accuracy with substantially reduced jerk compared to baselines, stable contact-rich manipulation under teleoperation, and up to 70% success in simulated single-object loco-manipulation tasks within a room-scale environment. These results indicate that compliant EE-root control provides a practical abstraction for humanoid loco-manipulation, enabling modular and scalable integration of diverse skills.

## Content
Humanoid robots have achieved impressive locomotion performance, yet contact-rich and long-horizon manipulation remains a major bottleneck. Manipulation is inherently contact-rich and demands compliant whole-body control for stable interaction, while its diversity and long-horizon nature favor modular, planner-compatible interfaces over joint-space tracking. We propose CEER, a compliant end-effector-root (EE-root) control abstraction for modular humanoid loco-manipulation within a hierarchical planning framework. CEER enables compliance-aware whole-body control in an interpretable task space defined by root motion commands and end-effector pose targets, and supports plug-and-play integration with heterogeneous high-level planners. A teacher-student framework is adopted to distill a general motion-tracking controller into a low-level policy that consumes only EE-root commands. We further construct a hierarchical system that integrates heterogeneous planners and task modules through the EE-root interface, enabling diverse manipulation tasks without retraining the underlying whole-body policy. Experiments in simulation and on hardware demonstrate 3.3 cm end-effector tracking accuracy with substantially reduced jerk compared to baselines, stable contact-rich manipulation under teleoperation, and up to 70% success in simulated single-object loco-manipulation tasks within a room-scale environment. These results indicate that compliant EE-root control provides a practical abstraction for humanoid loco-manipulation, enabling modular and scalable integration of diverse skills.

## 개요
휴머노이드 로봇은 인상적인 보행 성능을 달성했지만, 접촉이 많고 장기적인 조작은 여전히 주요 병목 현상으로 남아 있습니다. 조작은 본질적으로 접촉이 많으며 안정적인 상호작용을 위해 순응적인 전신 제어가 필요하고, 그 다양성과 장기적 특성은 관절 공간 추적보다 모듈식이고 계획기와 호환되는 인터페이스를 선호합니다.  
본 논문에서는 계층적 계획 프레임워크 내에서 모듈식 휴머노이드 보행-조작을 위한 순응적 말단-뿌리(EE-root) 제어 추상화인 CEER를 제안합니다. CEER는 루트 모션 명령과 말단 효과기 자세 목표로 정의된 해석 가능한 작업 공간에서 순응 인식 전신 제어를 가능하게 하며, 이기종 고수준 계획기와의 플러그 앤 플레이 통합을 지원합니다. 교사-학생 프레임워크를 채택하여 일반 모션 추적 컨트롤러를 EE-root 명령만 소비하는 저수준 정책으로 증류합니다.  
또한 EE-root 인터페이스를 통해 이기종 계획기와 작업 모듈을 통합하는 계층적 시스템을 구축하여, 기본 전신 정책을 재훈련하지 않고도 다양한 조작 작업을 가능하게 합니다. 시뮬레이션 및 하드웨어 실험에서 기준선 대비 크게 감소된 저크와 함께 3.3cm의 말단 효과기 추적 정확도, 원격 조작 하에서의 안정적인 접촉이 많은 조작, 그리고 방 크기 환경 내 시뮬레이션된 단일 물체 보행-조작 작업에서 최대 70%의 성공률을 입증했습니다. 이러한 결과는 순응적 EE-root 제어가 휴머노이드 보행-조작을 위한 실용적인 추상화를 제공하여 다양한 기술의 모듈식 및 확장 가능한 통합을 가능하게 함을 나타냅니다.

## 핵심 내용
휴머노이드 로봇은 인상적인 보행 성능을 달성했지만, 접촉이 많고 장기적인 조작은 여전히 주요 병목 현상으로 남아 있습니다. 조작은 본질적으로 접촉이 많으며 안정적인 상호작용을 위해 순응적인 전신 제어가 필요하고, 그 다양성과 장기적 특성은 관절 공간 추적보다 모듈식이고 계획기와 호환되는 인터페이스를 선호합니다.  
본 논문에서는 계층적 계획 프레임워크 내에서 모듈식 휴머노이드 보행-조작을 위한 순응적 말단-뿌리(EE-root) 제어 추상화인 CEER를 제안합니다. CEER는 루트 모션 명령과 말단 효과기 자세 목표로 정의된 해석 가능한 작업 공간에서 순응 인식 전신 제어를 가능하게 하며, 이기종 고수준 계획기와의 플러그 앤 플레이 통합을 지원합니다. 교사-학생 프레임워크를 채택하여 일반 모션 추적 컨트롤러를 EE-root 명령만 소비하는 저수준 정책으로 증류합니다.  
또한 EE-root 인터페이스를 통해 이기종 계획기와 작업 모듈을 통합하는 계층적 시스템을 구축하여, 기본 전신 정책을 재훈련하지 않고도 다양한 조작 작업을 가능하게 합니다. 시뮬레이션 및 하드웨어 실험에서 기준선 대비 크게 감소된 저크와 함께 3.3cm의 말단 효과기 추적 정확도, 원격 조작 하에서의 안정적인 접촉이 많은 조작, 그리고 방 크기 환경 내 시뮬레이션된 단일 물체 보행-조작 작업에서 최대 70%의 성공률을 입증했습니다. 이러한 결과는 순응적 EE-root 제어가 휴머노이드 보행-조작을 위한 실용적인 추상화를 제공하여 다양한 기술의 모듈식 및 확장 가능한 통합을 가능하게 함을 나타냅니다.

## 参考
- http://arxiv.org/abs/2605.19981v1
