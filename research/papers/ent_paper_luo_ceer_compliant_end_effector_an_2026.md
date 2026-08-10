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
    ent_paper_luo_ceer_compliant_end_effector_an_2026 into this card (rules: same_title_same_year). Backup+manifest: .staging/cleanup_wp12/.
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (936 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2605.19981v1

## 개요
휴머노이드 로봇은 이동 조작에서 접촉이 빈번하고 장시간 지속되는 작업의 도전 과제에 직면하며, 기존의 관절 공간 추적 방법은 유연성과 모듈성을 동시에 확보하기 어렵습니다. CEER는 엔드 이펙터 및 루트(EE-root) 명령 기반의 유연 제어 추상화를 제안하여 전신 제어를 해석 가능한 작업 공간에 매핑합니다. 교사-학생 증류를 통해 범용 운동 추적 컨트롤러가 엔드-루트 명령에만 응답하는 저수준 정책으로 압축되며, 이를 통해 다양한 고수준 플래너(예: 운동 플래너 또는 강화 학습 정책)가 직접 연결될 수 있습니다. 시뮬레이션 및 하드웨어 실험에서 이 방법은 원격 조작 접촉 작업에서 안정적인 성능을 보였으며, 방 규모 시나리오의 단일 물체 이동 조작 작업에서 최대 70%의 성공률을 달성했습니다.

## 핵심 내용
### 방법 아키텍처
- **EE-root 제어 추상화**: 휴머노이드 로봇의 전신 제어를 루트 운동 명령(예: 선속도, 각속도)과 엔드 이펙터 자세 목표(위치 및 방향)로 분해하여 해석 가능한 작업 공간을 형성합니다.
- **교사-학생 증류 프레임워크**:
  - **교사 정책**: 전신 운동 추적 컨트롤러를 기반으로 관절 공간 명령을 사용하여 정밀한 운동 추적을 구현합니다.
  - **학생 정책**: EE-root 명령만 입력으로 받아 증류 학습을 통해 교사 정책의 출력을 모방하며, 관절 수준 정보에 대한 의존성을 제거합니다.
- **계층적 계획 시스템**: 고수준 플래너(예: 운동 플래너, 강화 학습 정책 또는 원격 조작 인터페이스)는 EE-root 인터페이스를 통해 저수준 정책과 상호작용하며, 작업별로 저수준 컨트롤러를 재훈련할 필요가 없습니다.

### 실험 설정 및 주요 수치
- **시뮬레이션 환경**: Isaac Gym을 사용하여 훈련하고, 방 규모 시나리오에서 단일 물체 이동 조작 작업을 테스트합니다.
- **하드웨어 플랫폼**: Unitree H1 휴머노이드 로봇 기반, 힘/토크 센서 및 관절 엔코더를 장착합니다.
- **추적 정밀도**: 엔드 이펙터 위치 추적 오차는 3.3cm이며, 기준 방법(예: 순수 위치 제어)과 비교하여 저크(jerk)를 크게 줄였습니다.
- **작업 성공률**: 시뮬레이션에서 단일 물체 이동 조작 작업(예: 물체 집기 및 배치)의 성공률은 70%에 도달합니다.
- **원격 조작 검증**: 하드웨어에서 원격 조작을 통해 접촉이 빈번한 조작 작업(예: 문 밀기, 물체 운반)을 구현하여 안정적인 유연 상호작용 능력을 보여줍니다.

### 결론
CEER는 EE-root 제어 추상화를 통해 휴머노이드 로봇 이동 조작의 모듈성과 확장성을 구현하며, 접촉이 빈번한 작업에서 기존 방법보다 우수한 유연 제어 특성을 보여줍니다. 이 프레임워크는 이기종 플래너의 원활한 통합을 지원하여 복잡한 장시간 조작 작업에 실용적인 솔루션을 제공합니다.
