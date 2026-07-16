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
  zh: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL is a 2025 work on locomotion for humanoid
    robots.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19573v1.
sources:
- id: src_001
  type: paper
  title: 'Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL (arXiv)'
  url: https://arxiv.org/abs/2509.19573
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Achieving highly dynamic behaviors on humanoid robots, such as running, requires controllers that are both robust and precise, and hence difficult to design. Classical control methods offer valuable insight into how such systems can stabilize themselves, but synthesizing real-time controllers for nonlinear and hybrid dynamics remains challenging. Recently, reinforcement learning (RL) has gained popularity for locomotion control due to its ability to handle these complex dynamics. In this work, we embed ideas from nonlinear control theory, specifically control Lyapunov functions (CLFs), along with optimized dynamic reference trajectories into the reinforcement learning training process to shape the reward. This approach, CLF-RL, eliminates the need to handcraft and tune heuristic reward terms, while simultaneously encouraging certifiable stability and providing meaningful intermediate rewards to guide learning. By grounding policy learning in dynamically feasible trajectories, we expand the robot's dynamic capabilities and enable running that includes both flight and single support phases. The resulting policy operates reliably on a treadmill and in outdoor environments, demonstrating robustness to disturbances applied to the torso and feet. Moreover, it achieves accurate global reference tracking utilizing only on-board sensors, making a critical step toward integrating these dynamic motions into a full autonomy stack.

## 核心内容
Achieving highly dynamic behaviors on humanoid robots, such as running, requires controllers that are both robust and precise, and hence difficult to design. Classical control methods offer valuable insight into how such systems can stabilize themselves, but synthesizing real-time controllers for nonlinear and hybrid dynamics remains challenging. Recently, reinforcement learning (RL) has gained popularity for locomotion control due to its ability to handle these complex dynamics. In this work, we embed ideas from nonlinear control theory, specifically control Lyapunov functions (CLFs), along with optimized dynamic reference trajectories into the reinforcement learning training process to shape the reward. This approach, CLF-RL, eliminates the need to handcraft and tune heuristic reward terms, while simultaneously encouraging certifiable stability and providing meaningful intermediate rewards to guide learning. By grounding policy learning in dynamically feasible trajectories, we expand the robot's dynamic capabilities and enable running that includes both flight and single support phases. The resulting policy operates reliably on a treadmill and in outdoor environments, demonstrating robustness to disturbances applied to the torso and feet. Moreover, it achieves accurate global reference tracking utilizing only on-board sensors, making a critical step toward integrating these dynamic motions into a full autonomy stack.

## 参考
- http://arxiv.org/abs/2509.19573v1

## Overview
Achieving highly dynamic behaviors on humanoid robots, such as running, requires controllers that are both robust and precise, and hence difficult to design. Classical control methods offer valuable insight into how such systems can stabilize themselves, but synthesizing real-time controllers for nonlinear and hybrid dynamics remains challenging. Recently, reinforcement learning (RL) has gained popularity for locomotion control due to its ability to handle these complex dynamics. In this work, we embed ideas from nonlinear control theory, specifically control Lyapunov functions (CLFs), along with optimized dynamic reference trajectories into the reinforcement learning training process to shape the reward. This approach, CLF-RL, eliminates the need to handcraft and tune heuristic reward terms, while simultaneously encouraging certifiable stability and providing meaningful intermediate rewards to guide learning. By grounding policy learning in dynamically feasible trajectories, we expand the robot's dynamic capabilities and enable running that includes both flight and single support phases. The resulting policy operates reliably on a treadmill and in outdoor environments, demonstrating robustness to disturbances applied to the torso and feet. Moreover, it achieves accurate global reference tracking utilizing only on-board sensors, making a critical step toward integrating these dynamic motions into a full autonomy stack.

## Content
Achieving highly dynamic behaviors on humanoid robots, such as running, requires controllers that are both robust and precise, and hence difficult to design. Classical control methods offer valuable insight into how such systems can stabilize themselves, but synthesizing real-time controllers for nonlinear and hybrid dynamics remains challenging. Recently, reinforcement learning (RL) has gained popularity for locomotion control due to its ability to handle these complex dynamics. In this work, we embed ideas from nonlinear control theory, specifically control Lyapunov functions (CLFs), along with optimized dynamic reference trajectories into the reinforcement learning training process to shape the reward. This approach, CLF-RL, eliminates the need to handcraft and tune heuristic reward terms, while simultaneously encouraging certifiable stability and providing meaningful intermediate rewards to guide learning. By grounding policy learning in dynamically feasible trajectories, we expand the robot's dynamic capabilities and enable running that includes both flight and single support phases. The resulting policy operates reliably on a treadmill and in outdoor environments, demonstrating robustness to disturbances applied to the torso and feet. Moreover, it achieves accurate global reference tracking utilizing only on-board sensors, making a critical step toward integrating these dynamic motions into a full autonomy stack.

## 개요
휴머노이드 로봇에서 달리기와 같은 고도로 동적인 행동을 구현하려면 강건하고 정밀한 제어기가 필요하므로 설계가 어렵습니다. 고전적인 제어 방법은 이러한 시스템이 스스로 안정화되는 방식에 대한 귀중한 통찰력을 제공하지만, 비선형 및 하이브리드 동역학을 위한 실시간 제어기를 합성하는 것은 여전히 어려운 과제입니다. 최근 강화 학습(RL)은 이러한 복잡한 동역학을 처리할 수 있는 능력 덕분에 보행 제어 분야에서 인기를 얻고 있습니다. 본 연구에서는 비선형 제어 이론의 아이디어, 특히 제어 리아푸노프 함수(CLF)와 최적화된 동적 기준 궤적을 강화 학습 훈련 과정에 내장하여 보상을 형성합니다. 이 접근법인 CLF-RL은 경험적 보상 항목을 수동으로 설계하고 조정할 필요를 없애는 동시에, 인증 가능한 안정성을 장려하고 학습을 안내하는 의미 있는 중간 보상을 제공합니다. 정책 학습을 동역학적으로 실현 가능한 궤적에 기반함으로써 로봇의 동적 능력을 확장하고, 비행 및 단일 지지 단계를 모두 포함하는 달리기를 가능하게 합니다. 결과 정책은 트레드밀과 실외 환경에서 안정적으로 작동하며, 몸통과 발에 가해지는 외란에 대한 강건성을 입증합니다. 또한, 온보드 센서만을 사용하여 정확한 전역 기준 추적을 달성함으로써, 이러한 동적 움직임을 완전한 자율 시스템에 통합하는 중요한 단계를 마련합니다.

## 핵심 내용
휴머노이드 로봇에서 달리기와 같은 고도로 동적인 행동을 구현하려면 강건하고 정밀한 제어기가 필요하므로 설계가 어렵습니다. 고전적인 제어 방법은 이러한 시스템이 스스로 안정화되는 방식에 대한 귀중한 통찰력을 제공하지만, 비선형 및 하이브리드 동역학을 위한 실시간 제어기를 합성하는 것은 여전히 어려운 과제입니다. 최근 강화 학습(RL)은 이러한 복잡한 동역학을 처리할 수 있는 능력 덕분에 보행 제어 분야에서 인기를 얻고 있습니다. 본 연구에서는 비선형 제어 이론의 아이디어, 특히 제어 리아푸노프 함수(CLF)와 최적화된 동적 기준 궤적을 강화 학습 훈련 과정에 내장하여 보상을 형성합니다. 이 접근법인 CLF-RL은 경험적 보상 항목을 수동으로 설계하고 조정할 필요를 없애는 동시에, 인증 가능한 안정성을 장려하고 학습을 안내하는 의미 있는 중간 보상을 제공합니다. 정책 학습을 동역학적으로 실현 가능한 궤적에 기반함으로써 로봇의 동적 능력을 확장하고, 비행 및 단일 지지 단계를 모두 포함하는 달리기를 가능하게 합니다. 결과 정책은 트레드밀과 실외 환경에서 안정적으로 작동하며, 몸통과 발에 가해지는 외란에 대한 강건성을 입증합니다. 또한, 온보드 센서만을 사용하여 정확한 전역 기준 추적을 달성함으로써, 이러한 동적 움직임을 완전한 자율 시스템에 통합하는 중요한 단계를 마련합니다.
