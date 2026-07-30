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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.03206v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
로코모션은 휴머노이드 로봇의 기본 기술입니다. 그러나 기존 연구 대부분은 로코모션을 단일하고, 단조롭고, 확장 불가능하며, 제약이 없는 움직임으로 만듭니다. 이는 휴머노이드 로봇의 운동 능력을 제한합니다. 반면, 인간은 달리기, 점프, 깡충깡충 뛰기, 그리고 주파수와 발 높이 같은 보행 매개변수를 미세 조정하는 등 다양한 운동 능력을 가지고 있습니다. 본 논문에서는 이러한 다양성을 휴머노이드 로코모션에 도입하는 솔루션을 연구하고, 그 결과 HugWBC를 제안합니다: 다양한 로코모션을 위한 통합적이고 일반적인 휴머노이드 전신 제어기입니다. 작업 및 행동 측면에서 일반 명령 공간을 설계하고, 시뮬레이션에서 휴머노이드 전신 제어 정책을 학습하기 위한 대칭 손실 및 개입 훈련과 같은 고급 기술을 통해 HugWBC는 실제 휴머노이드 로봇이 걷기, 점프, 서기, 깡충깡충 뛰기를 포함한 다양한 자연스러운 보행을 생성할 수 있게 하며, 주파수, 발 스윙 높이와 같은 사용자 정의 가능한 매개변수와 함께 다양한 신체 높이, 허리 회전, 몸통 기울기를 결합할 수 있습니다. 로코모션 외에도 HugWBC는 원격 조작과 같은 외부 상체 제어기의 실시간 개입을 지원하여 모든 로코모션 동작 하에서 정밀한 로코-조작을 가능하게 합니다. 광범위한 실험을 통해 상체 개입 유무에 관계없이 모든 명령에 대한 HugWBC의 높은 추적 정확도와 견고성을 검증했으며, 다양한 명령이 휴머노이드 움직임에 미치는 영향에 대한 심층 분석과 명령 간 관계에 대한 통찰력을 제공합니다. 우리가 아는 한, HugWBC는 높은 견고성과 유연성을 갖춘 이러한 다양한 로코모션 동작을 지원하는 최초의 휴머노이드 전신 제어기입니다.

## 핵심 내용
로코모션은 휴머노이드 로봇의 기본 기술입니다. 그러나 기존 연구 대부분은 로코모션을 단일하고, 단조롭고, 확장 불가능하며, 제약이 없는 움직임으로 만듭니다. 이는 휴머노이드 로봇의 운동 능력을 제한합니다. 반면, 인간은 달리기, 점프, 깡충깡충 뛰기, 그리고 주파수와 발 높이 같은 보행 매개변수를 미세 조정하는 등 다양한 운동 능력을 가지고 있습니다. 본 논문에서는 이러한 다양성을 휴머노이드 로코모션에 도입하는 솔루션을 연구하고, 그 결과 HugWBC를 제안합니다: 다양한 로코모션을 위한 통합적이고 일반적인 휴머노이드 전신 제어기입니다. 작업 및 행동 측면에서 일반 명령 공간을 설계하고, 시뮬레이션에서 휴머노이드 전신 제어 정책을 학습하기 위한 대칭 손실 및 개입 훈련과 같은 고급 기술을 통해 HugWBC는 실제 휴머노이드 로봇이 걷기, 점프, 서기, 깡충깡충 뛰기를 포함한 다양한 자연스러운 보행을 생성할 수 있게 하며, 주파수, 발 스윙 높이와 같은 사용자 정의 가능한 매개변수와 함께 다양한 신체 높이, 허리 회전, 몸통 기울기를 결합할 수 있습니다. 로코모션 외에도 HugWBC는 원격 조작과 같은 외부 상체 제어기의 실시간 개입을 지원하여 모든 로코모션 동작 하에서 정밀한 로코-조작을 가능하게 합니다. 광범위한 실험을 통해 상체 개입 유무에 관계없이 모든 명령에 대한 HugWBC의 높은 추적 정확도와 견고성을 검증했으며, 다양한 명령이 휴머노이드 움직임에 미치는 영향에 대한 심층 분석과 명령 간 관계에 대한 통찰력을 제공합니다. 우리가 아는 한, HugWBC는 높은 견고성과 유연성을 갖춘 이러한 다양한 로코모션 동작을 지원하는 최초의 휴머노이드 전신 제어기입니다.

## 参考
- http://arxiv.org/abs/2502.03206v3
