---
$id: ent_paper_chasing_stability_humanoid_run_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL'
  zh: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL'
  ko: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL'
summary:
  en: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL is a 2025 work on locomotion for humanoid
    robots.'
  zh: CLF-RL 是一种将控制李雅普诺夫函数（CLF）与优化动态参考轨迹嵌入强化学习训练过程的方法，用于实现人形机器人的奔跑运动。该方法由研究团队于2025年提出，核心贡献在于无需手工设计启发式奖励项，通过可证明的稳定性引导学习，使机器人能够在跑步机和户外环境中可靠运行，并实现基于机载传感器的全局参考轨迹跟踪。
  ko: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL is a 2025 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- chasing_stability
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19573v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (814 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL (arXiv)'
  url: https://arxiv.org/abs/2509.19573
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人的高速动态行为（如奔跑）需要兼具鲁棒性和精确性的控制器，但传统控制方法在应对非线性和混合动力学时面临实时合成难题。CLF-RL 将非线性控制理论中的控制李雅普诺夫函数与优化动态参考轨迹相结合，通过塑造奖励函数来引导强化学习过程。这种方法不仅消除了手工调参的繁琐，还通过提供有意义的中间奖励和可证明的稳定性保障，显著扩展了机器人的动态能力。实验表明，该策略能在跑步机和户外环境中稳定运行，并对躯干和足部受到的扰动表现出鲁棒性，同时仅依赖机载传感器即可实现精确的全局轨迹跟踪。

## 核心内容
### 方法架构
- **核心思想**：将控制李雅普诺夫函数（CLF）与优化动态参考轨迹嵌入强化学习（RL）训练过程，通过奖励塑造引导策略学习。
- **CLF 作用**：提供可证明的稳定性保障，同时作为中间奖励信号，避免手工设计启发式奖励项。
- **动态参考轨迹**：基于优化生成的动态可行轨迹，使机器人能够实现包含飞行相和单支撑相的奔跑动作。

### 实验设置
- **硬件平台**：人形机器人（具体型号未在摘要中提及）。
- **测试环境**：跑步机（受控环境）与户外（非结构化环境）。
- **传感器配置**：仅使用机载传感器（如IMU、关节编码器等）进行状态估计与轨迹跟踪。

### 关键结果
- **鲁棒性**：策略对躯干和足部施加的外部扰动表现出强鲁棒性，在跑步机和户外均能稳定运行。
- **跟踪精度**：实现基于机载传感器的全局参考轨迹精确跟踪，无需外部定位系统。
- **动态能力**：成功实现包含飞行相（双脚离地）和单支撑相的奔跑动作，扩展了人形机器人的动态运动范围。

### 结论
CLF-RL 通过将经典控制理论与强化学习结合，为人形机器人高速动态控制提供了一种无需手工调参、可证明稳定的解决方案。该方法在真实环境中的可靠表现，标志着向将动态运动集成到完整自主系统迈出了关键一步。

## Overview
Achieving highly dynamic behaviors on humanoid robots, such as running, requires controllers that are both robust and precise, and hence difficult to design. Classical control methods offer valuable insight into how such systems can stabilize themselves, but synthesizing real-time controllers for nonlinear and hybrid dynamics remains challenging. Recently, reinforcement learning (RL) has gained popularity for locomotion control due to its ability to handle these complex dynamics. In this work, we embed ideas from nonlinear control theory, specifically control Lyapunov functions (CLFs), along with optimized dynamic reference trajectories into the reinforcement learning training process to shape the reward. This approach, CLF-RL, eliminates the need to handcraft and tune heuristic reward terms, while simultaneously encouraging certifiable stability and providing meaningful intermediate rewards to guide learning. By grounding policy learning in dynamically feasible trajectories, we expand the robot's dynamic capabilities and enable running that includes both flight and single support phases. The resulting policy operates reliably on a treadmill and in outdoor environments, demonstrating robustness to disturbances applied to the torso and feet. Moreover, it achieves accurate global reference tracking utilizing only on-board sensors, making a critical step toward integrating these dynamic motions into a full autonomy stack.

## 参考
- http://arxiv.org/abs/2509.19573v1

## 개요
휴머노이드 로봇의 고속 동적 행동(예: 달리기)은 견고성과 정밀성을 모두 갖춘 제어기를 필요로 하지만, 전통적인 제어 방법은 비선형 및 혼합 동역학을 다룰 때 실시간 합성 문제에 직면합니다. CLF-RL은 비선형 제어 이론의 제어 리아푸노프 함수(CLF)를 최적화된 동적 참조 궤적과 결합하여 보상 함수를 형성함으로써 강화 학습 과정을 유도합니다. 이 방법은 수동 파라미터 튜닝의 번거로움을 제거할 뿐만 아니라 의미 있는 중간 보상과 증명 가능한 안정성 보장을 제공하여 로봇의 동적 능력을 크게 확장합니다. 실험 결과, 이 전략은 러닝머신과 야외 환경에서 안정적으로 작동하며, 몸통과 발에 가해지는 외란에 대해 견고성을 보여주고, 온보드 센서만으로 정밀한 전역 궤적 추적을 달성합니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 제어 리아푸노프 함수(CLF)와 최적화된 동적 참조 궤적을 강화 학습(RL) 훈련 과정에 통합하여 보상 형성을 통해 정책 학습을 유도합니다.
- **CLF 역할**: 증명 가능한 안정성 보장을 제공하는 동시에 중간 보상 신호로 작용하여 수동 설계된 휴리스틱 보상 항을 피합니다.
- **동적 참조 궤적**: 최적화를 통해 생성된 동적으로 실현 가능한 궤적을 기반으로, 로봇이 비행 단계와 단일 지지 단계를 포함한 달리기 동작을 구현할 수 있게 합니다.

### 실험 설정
- **하드웨어 플랫폼**: 휴머노이드 로봇(구체적인 모델은 초록에 언급되지 않음).
- **테스트 환경**: 러닝머신(통제된 환경) 및 야외(비구조화된 환경).
- **센서 구성**: 상태 추정 및 궤적 추적을 위해 온보드 센서(예: IMU, 관절 엔코더 등)만 사용.

### 주요 결과
- **견고성**: 정책은 몸통과 발에 가해지는 외부 외란에 대해 강한 견고성을 보여주며, 러닝머신과 야외 모두에서 안정적으로 작동합니다.
- **추적 정밀도**: 외부 위치 추적 시스템 없이 온보드 센서 기반의 전역 참조 궤적 정밀 추적을 달성합니다.
- **동적 능력**: 비행 단계(양발 이탈)와 단일 지지 단계를 포함한 달리기 동작을 성공적으로 구현하여 휴머노이드 로봇의 동적 운동 범위를 확장합니다.

### 결론
CLF-RL은 고전 제어 이론과 강화 학습을 결합하여, 수동 파라미터 튜닝이 필요 없고 증명 가능한 안정성을 갖춘 휴머노이드 로봇의 고속 동적 제어 솔루션을 제공합니다. 이 방법은 실제 환경에서의 신뢰할 수 있는 성능을 통해, 동적 운동을 완전한 자율 시스템에 통합하는 방향으로의 핵심적인 진전을 나타냅니다.
