---
$id: ent_paper_coordinated_humanoid_robot_loc_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy
  zh: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy
  ko: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy
summary:
  en: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy is a 2025 work on locomotion
    for humanoid robots.
  zh: SE-Policy 是一种针对人形机器人运动控制的深度强化学习框架，由研究团队于 2025 年提出。其核心贡献在于将严格对称等变性嵌入策略网络、对称不变性嵌入价值网络，无需额外超参数即可提升运动协调性。在 Unitree G1 人形机器人上的仿真与实物实验中，该方法将速度跟踪精度最高提升
    40%。
  ko: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy is a 2025 work on locomotion
    for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- coordinated_humanoid_robot_loc
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.01247v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (814 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy (arXiv)
  url: https://arxiv.org/abs/2508.01247
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有深度强化学习方法忽略了人形机器人的形态对称性，导致运动不协调。SE-Policy 受人类神经系统双侧对称性启发，在策略网络中强制对称观测产生一致行为，在价值网络中保持对称不变性。该方法在速度跟踪任务中显著优于现有基线，不仅提升了跟踪精度，还实现了更优的时空协调性，并在 Unitree G1 机器人上完成了实物验证。

## 核心内容
### 方法架构
- **对称等变策略**：SE-Policy 在策略网络（actor）中嵌入严格对称等变性，确保机器人左右对称的观测输入产生对称的动作输出，从而生成协调的运动模式。
- **对称不变价值网络**：价值网络（critic）保持对称不变性，即对称状态具有相同价值估计，避免不对称的优化信号。
- **无需额外超参数**：该框架通过网络结构设计直接实现对称性约束，不引入额外的损失项或超参数。

### 实验设置
- **平台**：Unitree G1 人形机器人，包含仿真环境（Isaac Gym）和实物部署。
- **任务**：速度跟踪任务，要求机器人按指令速度前进、后退、侧移及转向。
- **基线**：与当前最优的深度强化学习方法（如 PPO、Symmetric PPO 等）对比。

### 关键结果
- **跟踪精度**：SE-Policy 将速度跟踪误差降低最多 40%，在多个速度指令下均优于所有基线。
- **时空协调性**：通过对称性约束，机器人左右腿步态对称性提升，关节轨迹更平滑，减少了非对称抖动。
- **实物验证**：在 Unitree G1 实物机器人上，SE-Policy 成功实现稳定、协调的行走与转向，验证了仿真到实物的迁移能力。

### 结论
SE-Policy 通过显式建模机器人形态对称性，显著提升了人形机器人运动控制的协调性与任务性能。该方法具有通用性，可应用于不同型号的人形机器人，为未来高动态运动控制提供了新范式。

## Overview
The human nervous system exhibits bilateral symmetry, enabling coordinated and balanced movements. However, existing Deep Reinforcement Learning (DRL) methods for humanoid robots neglect morphological symmetry of the robot, leading to uncoordinated and suboptimal behaviors. Inspired by human motor control, we propose Symmetry Equivariant Policy (SE-Policy), a new DRL framework that embeds strict symmetry equivariance in the actor and symmetry invariance in the critic without additional hyperparameters. SE-Policy enforces consistent behaviors across symmetric observations, producing temporally and spatially coordinated motions with higher task performance. Extensive experiments on velocity tracking tasks, conducted in both simulation and real-world deployment with the Unitree G1 humanoid robot, demonstrate that SE-Policy improves tracking accuracy by up to 40% compared to state-of-the-art baselines, while achieving superior spatial-temporal coordination. These results demonstrate the effectiveness of SE-Policy and its broad applicability to humanoid robots.

## 参考
- http://arxiv.org/abs/2508.01247v2

## 개요
기존 심층 강화 학습 방법은 휴머노이드 로봇의 형태 대칭성을 무시하여 움직임이 부자연스럽다. SE-Policy는 인간 신경계의 양측 대칭성에서 영감을 받아, 정책 네트워크에서 대칭 관측이 일관된 행동을 생성하도록 강제하고, 가치 네트워크에서는 대칭 불변성을 유지한다. 이 방법은 속도 추적 작업에서 기존 기준선보다 현저히 우수하며, 추적 정밀도 향상뿐만 아니라 더 나은 시공간 조정을 달성하고, Unitree G1 로봇에서 실물 검증을 완료했다.

## 핵심 내용
### 방법 아키텍처
- **대칭 등변 정책**: SE-Policy는 정책 네트워크(actor)에 엄격한 대칭 등변성을 내장하여, 로봇의 좌우 대칭 관측 입력이 대칭 동작 출력을 생성하도록 보장하여 조화로운 움직임 패턴을 생성한다.
- **대칭 불변 가치 네트워크**: 가치 네트워크(critic)는 대칭 불변성을 유지하며, 즉 대칭 상태는 동일한 가치 추정을 가지므로 비대칭 최적화 신호를 방지한다.
- **추가 하이퍼파라미터 불필요**: 이 프레임워크는 네트워크 구조 설계를 통해 대칭 제약을 직접 구현하며, 추가 손실 항목이나 하이퍼파라미터를 도입하지 않는다.

### 실험 설정
- **플랫폼**: Unitree G1 휴머노이드 로봇, 시뮬레이션 환경(Isaac Gym) 및 실물 배포 포함.
- **작업**: 속도 추적 작업으로, 로봇이 지시된 속도로 전진, 후진, 측면 이동 및 회전을 수행해야 한다.
- **기준선**: 현재 최적의 심층 강화 학습 방법(예: PPO, Symmetric PPO 등)과 비교.

### 주요 결과
- **추적 정밀도**: SE-Policy는 속도 추적 오류를 최대 40%까지 줄였으며, 여러 속도 명령에서 모든 기준선보다 우수했다.
- **시공간 조정**: 대칭 제약을 통해 로봇의 좌우 다리 보행 대칭성이 향상되고, 관절 궤적이 더 매끄러워지며 비대칭 떨림이 감소했다.
- **실물 검증**: Unitree G1 실물 로봇에서 SE-Policy는 안정적이고 조화로운 보행 및 회전을 성공적으로 구현하여 시뮬레이션에서 실물로의 전이 능력을 검증했다.

### 결론
SE-Policy는 로봇 형태 대칭성을 명시적으로 모델링하여 휴머노이드 로봇 운동 제어의 조정성과 작업 성능을 현저히 향상시켰다. 이 방법은 일반성을 가지며 다양한 모델의 휴머노이드 로봇에 적용할 수 있어, 미래의 고동적 운동 제어를 위한 새로운 패러다임을 제공한다.
