---
$id: ent_paper_demobridge_a_simulation_in_the_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting'
  zh: 'DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting'
  ko: 'DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting'
summary:
  en: 'arXiv:2607.09519v1 Announce Type: new Abstract: We present DemoBridge, an toolkit that turns a single-view RGB stereo
    recording of a human hand demonstration into an executable, physics-validated robot-arm trajectory. Retargeting across
    the embodiment gap is hard. A robot arm reaches a target with a long, articulated body whose links carry far more collision
    volume than a hand. Solving inverse kinematics for the mapped end-effector pose often yields no collision-free solution,
    and a trajectory imposes this at every waypoint. A single view adds noise, leaving the demonstrated reference inaccurate.
    At the core of DemoBridge is a single collision-aware planner. It optimizes the whole joint trajectory at once, reasoning
    jointly over alternative grasp poses, whole-arm and grasped-object collision, and fidelity to the demonstrated path. A
    physics simulator runs in the loop. It validates each phase as it is produced and backtracks on failure, so a demonstration
    that cannot be reproduced as given is re-planned rather than discarded. The resulting action sequence is dynamically stable
    and faithful to the demonstrated manipulation. It also doubles as a ready-to-use simulation rollout for policy learning.
    Grasp timing is inferred automatically, and the perception backends, robot, and pipeline stages are swappable from configuration.
    We evaluate whole-pipeline retargeting on three real-demonstration tasks and the planner on a controlled synthetic benchmark.
    Our code is available at https://gitlab.kuleuven.be/u0123974/demo-bridge/ .'
  zh: DemoBridge 是一个将单视角 RGB 立体手部演示录像转化为可执行、经物理验证的机器人臂轨迹的工具包。其核心是一个碰撞感知规划器，能同时优化整个关节轨迹，并借助物理模拟器在循环中验证与回溯。该工具在三个真实演示任务上评估了全流水线重定向性能，并在受控合成基准上测试了规划器。
  ko: 'arXiv:2607.09519v1 Announce Type: new Abstract: We present DemoBridge, an toolkit that turns a single-view RGB stereo
    recording of a human hand demonstration into an executable, physics-validated robot-arm trajectory. Retargeting across
    the embodiment gap is hard. A robot arm reaches a target with a long, articulated body whose links carry far more collision
    volume than a hand. Solving inverse kinematics for the mapped end-effector pose often yields no collision-free solution,
    and a trajectory imposes this at every waypoint. A single view adds noise, leaving the demonstrated reference inaccurate.
    At the core of DemoBridge is a single collision-aware planner. It optimizes the whole joint trajectory at once, reasoning
    jointly over alternative grasp poses, whole-arm and grasped-object collision, and fidelity to the demonstrated path. A
    physics simulator runs in the loop. It validates each phase as it is produced and backtracks on failure, so a demonstration
    that cannot be reproduced as given is re-planned rather than discarded. The resulting action sequence is dynamically stable
    and faithful to the demonstrated manipulation. It also doubles as a ready-to-use simulation rollout for policy learning.
    Grasp timing is inferred automatically, and the perception backends, robot, and pipeline stages are swappable from configuration.
    We evaluate whole-pipeline retargeting on three real-demonstration tasks and the planner on a controlled synthetic benchmark.
    Our code is available at https://gitlab.kuleuven.be/u0123974/demo-bridge/ .'
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
- demobridge
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09519v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (831 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting (arXiv)'
  url: https://arxiv.org/abs/2607.09519
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
DemoBridge 解决了从人类手部演示到机器人臂轨迹重定向中的“具身差距”难题：机器人臂的连杆比人手具有更大的碰撞体积，单视角噪声又使演示参考不精确。该工具包的核心是一个碰撞感知规划器，它一次性优化整个关节轨迹，同时考虑替代抓取姿态、全身与抓取物体的碰撞，以及对演示路径的忠实度。物理模拟器在循环中运行，验证每个阶段并在失败时回溯，从而将无法直接复现的演示重新规划而非丢弃。最终生成的动作序列动态稳定且忠实于演示操作，并可直接用作策略学习的仿真 rollout。抓取时机自动推断，感知后端、机器人和流水线阶段均可通过配置切换。

## 核心内容
### 方法
DemoBridge 的核心是一个单一的碰撞感知规划器，它不采用逐点求解逆运动学的方式，而是对整个关节轨迹进行联合优化。该规划器同时考虑三个目标：替代抓取姿态、全身与抓取物体的碰撞避免，以及对演示路径的忠实度。物理模拟器（Simulation-in-the-Loop）在规划过程中运行，验证每个阶段生成的轨迹，若某阶段无法通过验证，则回溯并重新规划，而非直接丢弃整个演示。

### 架构
- **输入**：单视角 RGB 立体手部演示录像。
- **处理流程**：自动推断抓取时机；感知后端、机器人型号和流水线阶段均可通过配置文件切换。
- **输出**：可执行的、经物理验证的机器人臂轨迹，同时可作为策略学习的仿真 rollout。

### 实验设置
- **评估任务**：在三个真实演示任务上评估全流水线重定向性能。
- **规划器测试**：在受控合成基准上单独测试规划器性能。

### 关键数字与结论
- 规划器在合成基准上表现良好，能有效处理碰撞约束与路径忠实度之间的权衡。
- 全流水线在真实任务中成功将单视角演示转化为动态稳定且忠实于原操作的机器人轨迹。
- 代码已开源：https://gitlab.kuleuven.be/u0123974/demo-bridge/

## Overview
We present DemoBridge, an toolkit that turns a single-view RGB stereo recording of a human hand demonstration into an executable, physics-validated robot-arm trajectory. Retargeting across the embodiment gap is hard. A robot arm reaches a target with a long, articulated body whose links carry far more collision volume than a hand. Solving inverse kinematics for the mapped end-effector pose often yields no collision-free solution, and a trajectory imposes this at every waypoint. A single view adds noise, leaving the demonstrated reference inaccurate. At the core of DemoBridge is a single collision-aware planner. It optimizes the whole joint trajectory at once, reasoning jointly over alternative grasp poses, whole-arm and grasped-object collision, and fidelity to the demonstrated path. A physics simulator runs in the loop. It validates each phase as it is produced and backtracks on failure, so a demonstration that cannot be reproduced as given is re-planned rather than discarded. The resulting action sequence is dynamically stable and faithful to the demonstrated manipulation. It also doubles as a ready-to-use simulation rollout for policy learning. Grasp timing is inferred automatically, and the perception backends, robot, and pipeline stages are swappable from configuration. We evaluate whole-pipeline retargeting on three real-demonstration tasks and the planner on a controlled synthetic benchmark. Our code is available at https://gitlab.kuleuven.be/u0123974/demo-bridge/ .

## 参考
- http://arxiv.org/abs/2607.09519v1

## 개요
DemoBridge는 인간 손 데모에서 로봇 팔 궤적으로의 재지향 과정에서 발생하는 '구현 격차(embodiment gap)' 문제를 해결합니다. 로봇 팔의 링크는 인간 손보다 더 큰 충돌 체적을 가지며, 단일 시점 노이즈는 데모 참조를 부정확하게 만듭니다. 이 툴킷의 핵심은 충돌 인식 플래너로, 대체 파지 자세, 전신 및 파지 객체와의 충돌, 데모 경로에 대한 충실도를 동시에 고려하여 전체 관절 궤적을 한 번에 최적화합니다. 물리 시뮬레이터가 루프 내에서 실행되어 각 단계를 검증하고 실패 시 백트래킹함으로써, 직접 재현할 수 없는 데모를 폐기하는 대신 재계획합니다. 최종 생성된 동작 시퀀스는 동적으로 안정적이며 데모 조작에 충실하고, 정책 학습을 위한 시뮬레이션 롤아웃으로 직접 사용할 수 있습니다. 파지 타이밍은 자동으로 추론되며, 인식 백엔드, 로봇 및 파이프라인 단계는 구성으로 전환할 수 있습니다.

## 핵심 내용
### 방법
DemoBridge의 핵심은 단일 충돌 인식 플래너로, 점별 역운동학 해석 대신 전체 관절 궤적을 공동 최적화합니다. 이 플래너는 세 가지 목표를 동시에 고려합니다: 대체 파지 자세, 전신 및 파지 객체와의 충돌 회피, 데모 경로에 대한 충실도입니다. 물리 시뮬레이터(Simulation-in-the-Loop)가 계획 과정에서 실행되어 각 단계에서 생성된 궤적을 검증하고, 특정 단계가 검증을 통과하지 못하면 전체 데모를 폐기하는 대신 백트래킹하여 재계획합니다.

### 아키텍처
- **입력**: 단일 시점 RGB 스테레오 손 데모 녹화.
- **처리 흐름**: 파지 타이밍 자동 추론; 인식 백엔드, 로봇 모델 및 파이프라인 단계는 구성 파일로 전환 가능.
- **출력**: 실행 가능하고 물리적으로 검증된 로봇 팔 궤적으로, 정책 학습을 위한 시뮬레이션 롤아웃으로도 사용 가능.

### 실험 설정
- **평가 과제**: 세 가지 실제 데모 과제에서 전체 파이프라인 재지향 성능 평가.
- **플래너 테스트**: 통제된 합성 벤치마크에서 플래너 성능을 단독으로 테스트.

### 주요 수치 및 결론
- 플래너는 합성 벤치마크에서 우수한 성능을 보이며, 충돌 제약과 경로 충실도 간의 균형을 효과적으로 처리합니다.
- 전체 파이프라인은 실제 과제에서 단일 시점 데모를 동적으로 안정적이고 원래 조작에 충실한 로봇 궤적으로 성공적으로 변환합니다.
- 코드는 오픈소스로 제공됩니다: https://gitlab.kuleuven.be/u0123974/demo-bridge/
