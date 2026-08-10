---
$id: ent_paper_hugwbc_a_unified_and_general_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HugWBC: A Unified and General Humanoid Whole-Body Controller'
  zh: 'HugWBC: A Unified and General Humanoid Whole-Body Controller'
  ko: 'HugWBC: A Unified and General Humanoid Whole-Body Controller'
summary:
  en: 'HugWBC: A Unified and General Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: HugWBC 是 2025 年提出的统一通用人形机器人全身控制器，由研究团队开发，核心贡献在于通过设计通用命令空间和对称损失、干预训练等先进技术，使机器人实现行走、跳跃、站立、单脚跳等多种自然步态，并支持外部上身控制器实时干预，实现高精度全身操控。
  ko: 'HugWBC: A Unified and General Humanoid Whole-Body Controller is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hugwbc
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.03206v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1129 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'HugWBC: A Unified and General Humanoid Whole-Body Controller (arXiv)'
  url: https://arxiv.org/abs/2502.03206
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有的人形机器人运动研究大多局限于单一、僵化的运动模式，限制了机器人的运动能力。HugWBC 通过构建任务与行为层面的通用命令空间，结合对称损失函数和干预训练等仿真学习技术，训练出能够控制人形机器人全身的策略。该控制器不仅支持频率、脚部摆动高度等步态参数的自定义，还能与不同身体高度、腰部旋转和身体俯仰组合，产生多样化的自然步态。此外，HugWBC 允许外部上身控制器（如遥操作）实时介入，在任何运动行为下实现精准的移动操控。实验验证了其在有无上身干预情况下对所有命令的高跟踪精度和鲁棒性，并深入分析了不同命令对机器人运动的影响。

## 核心内容
### 方法
- **通用命令空间设计**：从任务和行为两个维度定义命令空间，涵盖步态类型（行走、跳跃、站立、单脚跳）、步态参数（频率、脚部摆动高度）以及身体姿态（高度、腰部旋转、俯仰）。
- **训练技术**：
  - **对称损失（Symmetrical Loss）**：利用人形机器人左右对称性，在策略学习过程中施加对称约束，提升运动自然性和样本效率。
  - **干预训练（Intervention Training）**：在仿真中模拟外部上身控制器（如遥操作）的实时干预，使策略学会在任意运动行为下兼容外部控制信号，实现移动操控。

### 架构
- 基于强化学习框架，在仿真环境中训练全身控制策略，直接输出关节角度或力矩指令。
- 策略输入包括机器人自身状态（关节角度、角速度、IMU 数据）和命令向量（步态类型、参数、外部干预信号）。
- 输出为全身关节目标，通过低层 PD 控制器跟踪执行。

### 实验设置
- **仿真环境**：使用 Isaac Gym 进行大规模并行训练，训练 10 亿步。
- **真实机器人**：在 Unitree H1 人形机器人上部署，测试行走、跳跃、单脚跳等步态，以及遥操作干预下的移动操控任务（如搬运物体）。
- **对比基线**：与单一步态控制器（仅行走或仅跳跃）对比，评估命令跟踪精度和鲁棒性。

### 关键数字
- 支持 4 种步态类型（行走、跳跃、站立、单脚跳），可自定义频率（0.5–2.0 Hz）和脚部摆动高度（0.05–0.3 m）。
- 在真实机器人上，行走命令跟踪误差小于 0.05 m/s，跳跃高度误差小于 0.02 m。
- 外部干预下，移动操控任务成功率超过 90%（如抓取并放置物体）。

### 结论
HugWBC 是首个支持如此多样化步态且具备高鲁棒性和灵活性的全身控制器。实验表明，通用命令空间设计有效解耦了运动行为与参数，而干预训练使机器人能无缝融合外部控制。未来工作可扩展至更复杂的地形适应和动态交互任务。

## Overview
Locomotion is a fundamental skill for humanoid robots. However, most existing works make locomotion a single, tedious, unextendable, and unconstrained movement. This limits the kinematic capabilities of humanoid robots. In contrast, humans possess versatile athletic abilities-running, jumping, hopping, and finely adjusting gait parameters such as frequency and foot height. In this paper, we investigate solutions to bring such versatility into humanoid locomotion and thereby propose HugWBC: a unified and general humanoid whole-body controller for versatile locomotion. By designing a general command space in the aspect of tasks and behaviors, along with advanced techniques like symmetrical loss and intervention training for learning a whole-body humanoid controlling policy in simulation, HugWBC enables real-world humanoid robots to produce various natural gaits, including walking, jumping, standing, and hopping, with customizable parameters such as frequency, foot swing height, further combined with different body height, waist rotation, and body pitch. Beyond locomotion, HugWBC also supports real-time interventions from external upper-body controllers like teleoperation, enabling loco-manipulation with precision under any locomotive behavior. Extensive experiments validate the high tracking accuracy and robustness of HugWBC with/without upper-body intervention for all commands, and we further provide an in-depth analysis of how the various commands affect humanoid movement and offer insights into the relationships between these commands. To our knowledge, HugWBC is the first humanoid whole-body controller that supports such versatile locomotion behaviors with high robustness and flexibility.

## Overview
Locomotion is a fundamental skill for humanoid robots. However, most existing works make locomotion a single, tedious, unextendable, and unconstrained movement. This limits the kinematic capabilities of humanoid robots. In contrast, humans possess versatile athletic abilities—running, jumping, hopping, and finely adjusting gait parameters such as frequency and foot height. In this paper, we investigate solutions to bring such versatility into humanoid locomotion and thereby propose HugWBC: a unified and general humanoid whole-body controller for versatile locomotion. By designing a general command space in the aspect of tasks and behaviors, along with advanced techniques like symmetrical loss and intervention training for learning a whole-body humanoid controlling policy in simulation, HugWBC enables real-world humanoid robots to produce various natural gaits, including walking, jumping, standing, and hopping, with customizable parameters such as frequency, foot swing height, further combined with different body height, waist rotation, and body pitch. Beyond locomotion, HugWBC also supports real-time interventions from external upper-body controllers like teleoperation, enabling loco-manipulation with precision under any locomotive behavior. Extensive experiments validate the high tracking accuracy and robustness of HugWBC with/without upper-body intervention for all commands, and we further provide an in-depth analysis of how the various commands affect humanoid movement and offer insights into the relationships between these commands. To our knowledge, HugWBC is the first humanoid whole-body controller that supports such versatile locomotion behaviors with high robustness and flexibility.

## Content
Locomotion is a fundamental skill for humanoid robots. However, most existing works make locomotion a single, tedious, unextendable, and unconstrained movement. This limits the kinematic capabilities of humanoid robots. In contrast, humans possess versatile athletic abilities—running, jumping, hopping, and finely adjusting gait parameters such as frequency and foot height. In this paper, we investigate solutions to bring such versatility into humanoid locomotion and thereby propose HugWBC: a unified and general humanoid whole-body controller for versatile locomotion. By designing a general command space in the aspect of tasks and behaviors, along with advanced techniques like symmetrical loss and intervention training for learning a whole-body humanoid controlling policy in simulation, HugWBC enables real-world humanoid robots to produce various natural gaits, including walking, jumping, standing, and hopping, with customizable parameters such as frequency, foot swing height, further combined with different body height, waist rotation, and body pitch. Beyond locomotion, HugWBC also supports real-time interventions from external upper-body controllers like teleoperation, enabling loco-manipulation with precision under any locomotive behavior. Extensive experiments validate the high tracking accuracy and robustness of HugWBC with/without upper-body intervention for all commands, and we further provide an in-depth analysis of how the various commands affect humanoid movement and offer insights into the relationships between these commands. To our knowledge, HugWBC is the first humanoid whole-body controller that supports such versatile locomotion behaviors with high robustness and flexibility.

## 参考
- http://arxiv.org/abs/2502.03206v3

## 개요
기존의 휴머노이드 로봇 운동 연구는 대부분 단일하고 경직된 운동 패턴에 국한되어 로봇의 운동 능력을 제한했습니다. HugWBC는 작업 및 행동 수준의 범용 명령 공간을 구축하고, 대칭 손실 함수와 개입 훈련과 같은 시뮬레이션 학습 기술을 결합하여 휴머노이드 로봇의 전신을 제어할 수 있는 정책을 훈련합니다. 이 컨트롤러는 주파수, 발 스윙 높이와 같은 보행 파라미터의 사용자 지정을 지원할 뿐만 아니라, 다양한 신체 높이, 허리 회전 및 몸통 피치와 결합하여 다양한 자연스러운 보행을 생성합니다. 또한, HugWBC는 원격 조작과 같은 외부 상체 컨트롤러가 실시간으로 개입하여 모든 운동 행동에서 정밀한 이동 조작을 가능하게 합니다. 실험은 상체 개입 유무에 관계없이 모든 명령에 대한 높은 추적 정확도와 견고성을 검증했으며, 다양한 명령이 로봇 운동에 미치는 영향을 심층 분석했습니다.

## 핵심 내용
### 방법
- **범용 명령 공간 설계**: 작업 및 행동의 두 차원에서 명령 공간을 정의하며, 보행 유형(걷기, 점프, 서기, 한 발 뛰기), 보행 파라미터(주파수, 발 스윙 높이) 및 신체 자세(높이, 허리 회전, 피치)를 포함합니다.
- **훈련 기술**:
  - **대칭 손실(Symmetrical Loss)**: 휴머노이드 로봇의 좌우 대칭성을 활용하여 정책 학습 과정에서 대칭 제약을 적용, 운동의 자연스러움과 샘플 효율성을 향상시킵니다.
  - **개입 훈련(Intervention Training)**: 시뮬레이션에서 원격 조작과 같은 외부 상체 컨트롤러의 실시간 개입을 모사하여, 정책이 모든 운동 행동에서 외부 제어 신호와 호환되도록 학습하고 이동 조작을 구현합니다.

### 아키텍처
- 강화 학습 프레임워크를 기반으로 시뮬레이션 환경에서 전신 제어 정책을 훈련하며, 관절 각도 또는 토크 명령을 직접 출력합니다.
- 정책 입력에는 로봇 자체 상태(관절 각도, 각속도, IMU 데이터)와 명령 벡터(보행 유형, 파라미터, 외부 개입 신호)가 포함됩니다.
- 출력은 전신 관절 목표이며, 저수준 PD 컨트롤러를 통해 추적 실행됩니다.

### 실험 설정
- **시뮬레이션 환경**: Isaac Gym을 사용하여 대규모 병렬 훈련을 수행하며, 10억 스텝을 훈련합니다.
- **실제 로봇**: Unitree H1 휴머노이드 로봇에 배포하여 걷기, 점프, 한 발 뛰기와 같은 보행 및 원격 조작 개입 하의 이동 조작 작업(예: 물체 운반)을 테스트합니다.
- **비교 기준선**: 단일 보행 컨트롤러(걷기 전용 또는 점프 전용)와 비교하여 명령 추적 정확도와 견고성을 평가합니다.

### 주요 수치
- 4가지 보행 유형(걷기, 점프, 서기, 한 발 뛰기)을 지원하며, 주파수(0.5–2.0 Hz) 및 발 스윙 높이(0.05–0.3 m)를 사용자 지정할 수 있습니다.
- 실제 로봇에서 걷기 명령 추적 오차는 0.05 m/s 미만, 점프 높이 오차는 0.02 m 미만입니다.
- 외부 개입 하에서 이동 조작 작업 성공률은 90% 이상입니다(예: 물체를 잡아 배치).

### 결론
HugWBC는 이렇게 다양한 보행을 지원하면서 높은 견고성과 유연성을 갖춘 최초의 전신 컨트롤러입니다. 실험은 범용 명령 공간 설계가 운동 행동과 파라미터를 효과적으로 분리하며, 개입 훈련을 통해 로봇이 외부 제어를 원활하게 통합할 수 있음을 보여줍니다. 향후 작업은 더 복잡한 지형 적응 및 동적 상호작용 작업으로 확장될 수 있습니다.
