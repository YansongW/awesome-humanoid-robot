---
$id: ent_paper_tahir_mobile_robot_control_and_auton_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Mobile Robot Control and Autonomy Through Collaborative Simulation Twin
  zh: 通过协同仿真孪生实现移动机器人控制与自主性
  ko: 협업 시뮬레이션 트윈을 통한 이동 로봇 제어 및 자율성
summary:
  en: Proposes a collaborative Simulation Twin (ST) framework that offloads SLAM-based path planning to a remote simulated
    agent and synchronizes velocity commands with predicted force feedback from a physical robot, evaluated in constrained
    indoor environments.
  zh: 本文提出一种协作仿真孪生（Simulation Twin, ST）框架，将基于SLAM的路径规划卸载至远程仿真智能体，并通过预测力反馈同步物理机器人的速度指令。该框架在受限室内环境中验证了计算与网络性能的提升，但障碍场景下成功率为64%，且状态映射延迟导致目标精度低于直接远程卸载。
  ko: SLAM 기반 경로 계획을 원격 시뮬레이션 에이전트에 오프로드하고 물리 로봇의 속도 추적 및 예측 힘 피드백을 통해 양방향 동기화하는 협업 시뮬레이션 트윈(ST) 프레임워크를 제안하며, 제한된 실내 환경에서
    실험적으로 평가하였다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- simulation_twin
- digital_twin
- remote_offloading
- autonomous_navigation
- slam
- path_planning
- velocity_tracking
- predictive_force_feedback
- resource_constrained_robot
- human_in_the_loop
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from the arXiv abstract; hardware and algorithm details taken from supplied metadata and require human
    verification against the full paper. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Mobile Robot Control and Autonomy Through Collaborative Simulation Twin
  url: https://arxiv.org/abs/2303.06172
  date: '2023'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---
## 概述
该框架将移动机器人系统分为通过网络连接的虚拟空间与物理空间：物理机器人留在操作现场，远程仿真智能体执行高层自主导航。与纯镜像的数字孪生不同，ST强调协作控制，并支持可选的人在回路遥操作——通过速度多路复用器按优先级规则切换自主规划器与操作员指令，实现安全避障。实验在3m×3m和6m×6m的小型室内场地使用低成本移动机器人进行，对比了远程计算卸载、手动遥操作和数字孪生基线，结果表明该方案对资源受限机器人具有实用性，但障碍场景下性能受限。

## 核心内容
### 方法
- **协作仿真孪生（ST）架构**：将移动机器人系统拆分为虚拟空间（仿真智能体）与物理空间（真实机器人），两者通过通信信道连接。仿真智能体运行基于SLAM的路径规划器，生成速度指令发送给物理机器人；物理机器人跟踪速度并返回与环境交互的力反馈。
- **控制模式**：支持可选的人在回路遥操作，通过速度多路复用器按优先级规则切换自主规划器与操作员指令，确保安全避障。反馈机制应用于远程仿真智能体而非操纵杆。

### 实验设置
- **场地**：3m×3m和6m×6m的小型室内竞技场。
- **机器人**：低成本移动机器人。
- **基线对比**：传统远程计算卸载、手动遥操作、数字孪生。

### 关键结果
- **性能优势**：ST框架在计算与网络性能上优于基线方法，适用于资源受限机器人。
- **局限性**：障碍场景下成功率为64%；由于状态映射延迟，目标精度低于直接远程卸载。
- **结论**：该方案在受限环境中具有实用性，但延迟与精度问题需进一步优化。

## Overview

This paper introduces a collaborative Simulation Twin (ST) strategy that splits a mobile robot system into a cyber (simulated) space and a physical (real) space connected over a communication channel. The physical robot remains at the operational site while a simulated autonomous agent at a remote location performs high-level autonomy. The simulated twin runs autonomous navigation using a SLAM-based path planner and sends velocity commands to the physical robot, which tracks those velocities and returns feedback from its interactions with the environment.

The framework is positioned as an extension of the digital-twin concept, but with an emphasis on collaborative control rather than pure mirroring. It also supports optional human-in-the-loop teleoperation, where the simulated twin’s autonomous planner and the human operator’s commands are multiplexed according to priority rules for safe obstacle avoidance. Experiments compare the ST approach against conventional remote computing/offloading, manual teleoperation, and digital-twin baselines, reporting gains in computational and network performance.

Evaluation was carried out in small indoor arenas (3 m × 3 m and 6 m × 6 m) using a low-cost mobile robot. The results demonstrate that the simulation-physical twinning approach is practical for resource-constrained robots, although obstructed scenarios showed a success rate of 64 % and goal accuracy was lower than direct remote offloading due to state-mapping delay.

## Key Contributions

- {'en': 'A simulated-physical robot collaboration framework that allows optional human-in-the-loop control.', 'zh': '允许可选人在回路控制的虚实机器人协同框架。', 'ko': '선택적 인간 개입 제어를 가능하게 하는 실제-가상 로봇 협업 프레임워크.'}
- {'en': 'Prioritized switching-based control using a velocity multiplexer for safe obstacle avoidance.', 'zh': '使用速度多路复用器进行优先级切换控制，实现安全避障。', 'ko': '속도 멀티플렉서를 활용한 우선순위 기반 전환 제어를 통한 안전한 장애물 회피.'}
- {'en': 'A feedback mechanism applied to the remote simulated autonomous agent rather than to a joystick.', 'zh': '将反馈机制应用于远程仿真自主智能体而非操纵杆。', 'ko': '조이스틱이 아닌 원격 시뮬레이션 자율 에이전트에 피드백 메커니즘 적용.'}
- {'en': 'Experimental comparison of task, network, and computing performance against remote offloading, manual teleoperation, and digital-twin baselines.', 'zh': '与远程卸载、手动遥操作及数字孪生基线进行任务、网络和计算性能对比。', 'ko': '원격 오프로딩, 수동 텔레오퍼레이션, 디지털 트윈 기준과의 작업·네트워크·계산 성능 비교.'}

## Relevance to Humanoid Robotics

{'en': 'The ST framework is directly relevant to humanoid robotics because it offloads compute-intensive autonomy algorithms to a remote simulated twin, reducing the onboard processing and networking burden on the physical robot. This can lower hardware costs and enable scalable deployment of humanoids with limited payload or battery capacity. However, the paper’s experiments use a small wheeled robot; whether the same latency, balance, and safety guarantees transfer to bipedal locomotion remains to be validated.', 'zh': 'ST框架对人形机器人具有直接相关性，因为它将计算密集型的自主算法卸载到远程仿真孪生体，从而减轻物理机器人的机载处理与网络负担。这有助于降低硬件成本，并支持载荷或电池容量有限的人形机器人规模化部署。但论文实验仅使用小型轮式机器人，该方法能否迁移到双足行走并保证相同的延迟、平衡与安全性仍需验证。', 'ko': 'ST 프레임워크는 연산 집약적인 자율 알고리즘을 원격 시뮬레이션 트윈에 오프로드하여 물리 로봇의 온보드 처리 및 네트워크 부담을 줄이므로 인간형 로봇과 직접적으로 관련이 있다. 이는 하드웨어 비용을 낮추고 탑재 하중이나 배터리 용량이 제한된 인간형 로봇의 확장 가능한 배포를 가능하게 한다. 그러나 논문의 실험은 소형 휠 로봇을 사용하였으므로, 동일한 지연 시간, 균형 및 안전성 보장이 이족 보행에도 적용되는지는 추가 검증이 필요하다.'}

## References

- [Mobile Robot Control and Autonomy Through Collaborative Simulation Twin](https://arxiv.org/abs/2303.06172) (accessed 2026-07-01)

## 개요
이 프레임워크는 이동 로봇 시스템을 네트워크로 연결된 가상 공간과 물리적 공간으로 분할합니다. 물리적 로봇은 작업 현장에 남아 있고, 원격 시뮬레이션 에이전트는 고수준 자율 주행을 수행합니다. 순수 미러링 기반의 디지털 트윈과 달리, ST는 협력 제어를 강조하며, 선택적으로 사람이 개입하는 원격 조작을 지원합니다. 속도 멀티플렉서를 통해 우선순위 규칙에 따라 자율 계획기와 운영자 명령을 전환하여 안전한 장애물 회피를 구현합니다. 실험은 3m×3m 및 6m×6m의 소형 실내 공간에서 저비용 이동 로봇을 사용하여 진행되었으며, 원격 연산 오프로딩, 수동 원격 조작 및 디지털 트윈 기준선과 비교한 결과, 해당 방식이 자원이 제한된 로봇에 실용적이지만 장애물 시나리오에서는 성능이 제한됨을 보여주었습니다.

## 핵심 내용
### 방법
- **협력 시뮬레이션 트윈(ST) 아키텍처**: 이동 로봇 시스템을 가상 공간(시뮬레이션 에이전트)과 물리적 공간(실제 로봇)으로 분할하며, 두 공간은 통신 채널로 연결됩니다. 시뮬레이션 에이전트는 SLAM 기반 경로 계획기를 실행하여 속도 명령을 생성하고 물리적 로봇에 전송하며, 물리적 로봇은 속도를 추종하고 환경과의 상호작용에 따른 힘 피드백을 반환합니다.
- **제어 모드**: 선택적으로 사람이 개입하는 원격 조작을 지원하며, 속도 멀티플렉서를 통해 우선순위 규칙에 따라 자율 계획기와 운영자 명령을 전환하여 안전한 장애물 회피를 보장합니다. 피드백 메커니즘은 조이스틱이 아닌 원격 시뮬레이션 에이전트에 적용됩니다.

### 실험 설정
- **공간**: 3m×3m 및 6m×6m의 소형 실내 경기장.
- **로봇**: 저비용 이동 로봇.
- **기준선 비교**: 기존 원격 연산 오프로딩, 수동 원격 조작, 디지털 트윈.

### 주요 결과
- **성능 우위**: ST 프레임워크는 연산 및 네트워크 성능에서 기준선 방법보다 우수하며, 자원이 제한된 로봇에 적합합니다.
- **한계**: 장애물 시나리오에서 성공률은 64%입니다. 상태 매핑 지연으로 인해 목표 정밀도가 직접 원격 오프로딩보다 낮습니다.
- **결론**: 해당 방식은 제한된 환경에서 실용적이지만, 지연 및 정밀도 문제는 추가 최적화가 필요합니다.
