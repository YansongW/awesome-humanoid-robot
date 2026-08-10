---
$id: ent_paper_closing_the_reality_gap_zero_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation'
  zh: 'Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation'
  ko: 'Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation'
summary:
  en: 'arXiv:2607.04940v1 Announce Type: new Abstract: Human-like dexterous hands with multiple fingers offer human-level
    manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich
    physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback
    combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer,
    we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units
    and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii)
    a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current
    to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects
    and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation
    and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1)
    command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly
    executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing
    and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge,
    this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation
    and transferred zero-shot on real hardware.'
  zh: 本文提出一种基于强化学习的仿真到现实零样本迁移方法，用于多指灵巧手的力控抓取与操作。该方法通过密集触觉反馈与关节力矩感知相结合，并引入快速触觉仿真、电流-力矩标定及执行器动力学随机化建模，在五指手上实现了可控抓取力跟踪与物体重定向两项关键技能，无需真实机器人微调即可直接部署。
  ko: 'arXiv:2607.04940v1 Announce Type: new Abstract: Human-like dexterous hands with multiple fingers offer human-level
    manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich
    physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback
    combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer,
    we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units
    and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii)
    a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current
    to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects
    and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation
    and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1)
    command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly
    executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing
    and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge,
    this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation
    and transferred zero-shot on real hardware.'
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
- robotics
- closing_the_reality_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04940v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (740 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.04940
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
针对多指灵巧手因接触丰富物理与不完美驱动导致的策略训练难题，作者提出一套完整的仿真到现实迁移方案。核心创新包括：利用并行正向运动学快速计算虚拟触觉单元与物体距离的高效触觉仿真；通过电机电流映射关节力矩的标定方法，省去力矩传感器；以及考虑非理想力矩-速度效应的执行器动力学随机化建模。基于非对称actor-critic PPO框架，策略完全在仿真中训练后直接迁移至真实五指手，成功实现可控抓取力跟踪与物体重定向，且无需任何微调。

## 核心内容
### 方法架构
- **触觉仿真**：采用并行正向运动学计算密集虚拟触觉单元与物体间的距离，为强化学习提供高频率、高分辨率的触觉信号，计算效率高。
- **电流-力矩标定**：通过映射电机电流至关节力矩，消除灵巧手对专用力矩传感器的依赖，降低硬件成本与复杂度。
- **执行器动力学建模**：对非理想力矩-速度效应进行建模并引入随机化，弥合仿真与真实执行器之间的差距。
- **训练框架**：使用非对称actor-critic PPO算法，策略完全在仿真环境中训练，观测空间融合触觉与力矩信息。

### 实验设置与关键结果
- **硬件平台**：五指灵巧手，直接部署仿真训练策略，无需真实机器人微调。
- **演示技能**：
  - 基于指令的可控抓取力跟踪：策略能根据外部命令精确调节抓取力。
  - 手内物体重定向：策略可稳健地改变物体在手中的姿态。
- **关键数字**：据作者所知，这是首次在仿真中完全训练的多指灵巧手实现可控抓取，并零样本迁移至真实硬件。

### 结论
通过将触觉与力矩观测结合可扩展的传感与执行器建模，该系统为可靠灵巧操作提供了实用解决方案，验证了仿真到现实迁移在接触丰富任务中的有效性。

## Overview
Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1) command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.

## 参考
- http://arxiv.org/abs/2607.04940v1

## 개요
다지성 로봇 핸드가 접촉이 풍부한 물리적 환경과 불완전한 구동으로 인해 정책 훈련이 어려운 문제를 해결하기 위해, 저자는 완전한 시뮬레이션-현실 전이 솔루션을 제안한다. 핵심 혁신은 다음과 같다: 병렬 순운동학을 활용해 가상 촉각 유닛과 물체 간 거리를 빠르게 계산하는 고효율 촉각 시뮬레이션; 모터 전류를 관절 토크로 매핑하는 캘리브레이션 방법으로 토크 센서를 생략; 비이상적 토크-속도 효과를 고려한 액추에이터 동역학 무작위화 모델링. 비대칭 actor-critic PPO 프레임워크를 기반으로, 정책은 완전히 시뮬레이션에서 훈련된 후 미세 조정 없이 실제 5지 핸드로 직접 전이되어 제어 가능한 파지력 추적과 물체 재방향 전환을 성공적으로 구현한다.

## 핵심 내용
### 방법 아키텍처
- **촉각 시뮬레이션**: 병렬 순운동학을 사용해 밀집된 가상 촉각 유닛과 물체 간 거리를 계산하여, 강화 학습에 고주파수·고해상도 촉각 신호를 제공하며 계산 효율이 높다.
- **전류-토크 캘리브레이션**: 모터 전류를 관절 토크로 매핑하여 로봇 핸드의 전용 토크 센서 의존성을 제거하고, 하드웨어 비용과 복잡성을 낮춘다.
- **액추에이터 동역학 모델링**: 비이상적 토크-속도 효과를 모델링하고 무작위화를 도입하여 시뮬레이션과 실제 액추에이터 간의 격차를 줄인다.
- **훈련 프레임워크**: 비대칭 actor-critic PPO 알고리즘을 사용하며, 정책은 완전히 시뮬레이션 환경에서 훈련되고, 관측 공간은 촉각 및 토크 정보를 통합한다.

### 실험 설정 및 주요 결과
- **하드웨어 플랫폼**: 5지 로봇 핸드로, 실제 로봇 미세 조정 없이 시뮬레이션 훈련 정책을 직접 배포한다.
- **시연 기술**:
  - 명령 기반 제어 가능한 파지력 추적: 정책이 외부 명령에 따라 파지력을 정밀하게 조절할 수 있다.
  - 손 안 물체 재방향 전환: 정책이 손 안 물체의 자세를 견고하게 변경할 수 있다.
- **주요 수치**: 저자가 아는 한, 이는 시뮬레이션에서 완전히 훈련된 다지성 로봇 핸드가 제어 가능한 파지를 구현하고 제로샷으로 실제 하드웨어에 전이한 최초의 사례이다.

### 결론
촉각 및 토크 관측을 확장 가능한 센싱 및 액추에이터 모델링과 결합함으로써, 이 시스템은 신뢰할 수 있는 정밀 조작을 위한 실용적 솔루션을 제공하며, 접촉이 풍부한 작업에서 시뮬레이션-현실 전이의 효과를 검증한다.
