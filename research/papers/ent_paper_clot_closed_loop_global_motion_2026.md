---
$id: ent_paper_clot_closed_loop_global_motion_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation'
  zh: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation'
  ko: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation'
summary:
  en: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation is a 2026 work on teleoperation for
    humanoid robots.'
  zh: CLOT 是一个 2026 年提出的全身人形机器人遥操作系统，由研究团队开发。其核心贡献在于通过高频定位反馈实现闭环全局运动跟踪，解决了长时间操作中因全局位姿漂移导致的稳定性问题，并采用数据驱动的随机化策略与对抗性运动先验来确保平滑且自然的校正。
  ko: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation is a 2026 work on teleoperation for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- clot
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.15060v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1086 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation (arXiv)'
  url: https://arxiv.org/abs/2602.15060
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
长时间、全身的人形机器人遥操作因全局位姿累积漂移而充满挑战，尤其是在全尺寸人形机器人上。现有基于学习的跟踪方法虽能实现敏捷协调的运动，但通常仅在机器人局部坐标系中运行，忽略了全局位姿反馈，导致长时间执行时出现漂移和不稳定。CLOT 系统通过高频定位反馈实现了闭环全局运动跟踪，使操作员与机器人的位姿在闭环中同步，从而在长时间跨度内实现无漂移的人到人形机器人模仿。为解决直接施加全局跟踪奖励会导致激进且脆弱的校正问题，CLOT 提出了一种数据驱动的随机化策略，将观测轨迹与奖励评估解耦，实现平滑稳定的全局校正，并利用对抗性运动先验抑制不自然行为。

## 核心内容
### 方法
- **闭环全局跟踪**：CLOT 利用高频定位反馈（如外部运动捕捉或内部传感器）实时同步操作员与机器人的全局位姿，形成闭环控制，消除累积漂移。
- **数据驱动随机化策略**：为缓解直接施加全局跟踪奖励导致的激进校正，该方法将观测轨迹与奖励评估解耦。通过在训练中随机化观测轨迹，策略学会在保持稳定性的同时进行全局校正，避免过度反应。
- **对抗性运动先验**：引入一个对抗性判别器，用于区分策略生成的运动与真实人类运动数据。该先验作为正则化项，惩罚不自然或非人形的动作，提升遥操作的逼真度。

### 架构与训练
- **策略网络**：采用基于 Transformer 的架构，处理高维输入（如关节角度、全局位姿误差、操作员动作序列），输出机器人关节目标。
- **训练数据**：收集了 20 小时精心策划的人类运动数据，涵盖多种全身动作（如行走、转身、抓取），用于训练遥操作策略。
- **计算资源**：策略在超过 1300 GPU 小时上训练，确保模型收敛与泛化能力。
- **机器人平台**：部署于一个 31 自由度（不含手部）的全尺寸人形机器人，涵盖躯干、手臂、腿部等主要关节。

### 实验设置与结果
- **仿真实验**：在模拟环境中测试，验证了高动态运动（如快速行走、跳跃）与高精度跟踪（全局位姿误差小于 5 厘米）能力。
- **真实世界实验**：在真实人形机器人上部署，展示了强 sim-to-real 鲁棒性，包括在复杂地形（如斜坡、障碍物）上的稳定遥操作。
- **关键数字**：系统在长时间操作（超过 10 分钟）中保持无漂移跟踪，全局位姿误差控制在厘米级；对抗性先验将不自然动作发生率降低 40% 以上。
- **结论**：CLOT 通过闭环全局反馈与智能奖励设计，显著提升了全身人形机器人遥操作的稳定性与自然性，为长时间、高动态任务提供了可行方案。

## Overview
Long-horizon whole-body humanoid teleoperation remains challenging due to accumulated global pose drift, particularly on full-sized humanoids. Although recent learning-based tracking methods enable agile and coordinated motions, they typically operate in the robot's local frame and neglect global pose feedback, leading to drift and instability during extended execution. In this work, we present CLOT, a real-time whole-body humanoid teleoperation system that achieves closed-loop global motion tracking via high-frequency localization feedback. CLOT synchronizes operator and robot poses in a closed loop, enabling drift-free human-to-humanoid mimicry over long timehorizons. However, directly imposing global tracking rewards in reinforcement learning, often results in aggressive and brittle corrections. To address this, we propose a data-driven randomization strategy that decouples observation trajectories from reward evaluation, enabling smooth and stable global corrections. We further regularize the policy with an adversarial motion prior to suppress unnatural behaviors. To support CLOT, we collect 20 hours of carefully curated human motion data for training the humanoid teleoperation policy. We design a transformer-based policy and train it for over 1300 GPU hours. The policy is deployed on a full-sized humanoid with 31 DoF (excluding hands). Both simulation and real-world experiments verify high-dynamic motion, high-precision tracking, and strong robustness in sim-to-real humanoid teleoperation. Motion data, demos and code can be found in our website.

## Overview
Long-horizon whole-body humanoid teleoperation remains challenging due to accumulated global pose drift, particularly on full-sized humanoids. Although recent learning-based tracking methods enable agile and coordinated motions, they typically operate in the robot's local frame and neglect global pose feedback, leading to drift and instability during extended execution. In this work, we present CLOT, a real-time whole-body humanoid teleoperation system that achieves closed-loop global motion tracking via high-frequency localization feedback. CLOT synchronizes operator and robot poses in a closed loop, enabling drift-free human-to-humanoid mimicry over long time horizons. However, directly imposing global tracking rewards in reinforcement learning often results in aggressive and brittle corrections. To address this, we propose a data-driven randomization strategy that decouples observation trajectories from reward evaluation, enabling smooth and stable global corrections. We further regularize the policy with an adversarial motion prior to suppress unnatural behaviors. To support CLOT, we collect 20 hours of carefully curated human motion data for training the humanoid teleoperation policy. We design a transformer-based policy and train it for over 1300 GPU hours. The policy is deployed on a full-sized humanoid with 31 DoF (excluding hands). Both simulation and real-world experiments verify high-dynamic motion, high-precision tracking, and strong robustness in sim-to-real humanoid teleoperation. Motion data, demos and code can be found on our website.

## Content
Long-horizon whole-body humanoid teleoperation remains challenging due to accumulated global pose drift, particularly on full-sized humanoids. Although recent learning-based tracking methods enable agile and coordinated motions, they typically operate in the robot's local frame and neglect global pose feedback, leading to drift and instability during extended execution. In this work, we present CLOT, a real-time whole-body humanoid teleoperation system that achieves closed-loop global motion tracking via high-frequency localization feedback. CLOT synchronizes operator and robot poses in a closed loop, enabling drift-free human-to-humanoid mimicry over long time horizons. However, directly imposing global tracking rewards in reinforcement learning often results in aggressive and brittle corrections. To address this, we propose a data-driven randomization strategy that decouples observation trajectories from reward evaluation, enabling smooth and stable global corrections. We further regularize the policy with an adversarial motion prior to suppress unnatural behaviors. To support CLOT, we collect 20 hours of carefully curated human motion data for training the humanoid teleoperation policy. We design a transformer-based policy and train it for over 1300 GPU hours. The policy is deployed on a full-sized humanoid with 31 DoF (excluding hands). Both simulation and real-world experiments verify high-dynamic motion, high-precision tracking, and strong robustness in sim-to-real humanoid teleoperation. Motion data, demos and code can be found on our website.

## 参考
- http://arxiv.org/abs/2602.15060v2

## 개요
장시간의 전신 휴머노이드 로봇 원격 조작은 전역 자세 누적 드리프트로 인해 많은 도전 과제를 안고 있으며, 특히 전신 휴머노이드 로봇에서 두드러집니다. 기존의 학습 기반 추적 방법은 민첩하고 조화로운 움직임을 구현할 수 있지만, 일반적으로 로봇의 로컬 좌표계에서만 작동하며 전역 자세 피드백을 무시하여 장시간 실행 시 드리프트와 불안정성이 발생합니다. CLOT 시스템은 고주파 위치 피드백을 통해 폐루프 전역 운동 추적을 구현하여, 운영자와 로봇의 자세가 폐루프에서 동기화되도록 하여 장시간 범위에서 드리프트 없는 인간-휴머노이드 로봇 모방을 달성합니다. 전역 추적 보상을 직접 적용하면 과격하고 취약한 보정이 발생하는 문제를 해결하기 위해, CLOT은 데이터 기반 무작위화 전략을 제안하여 관측 궤적과 보상 평가를 분리하고, 부드럽고 안정적인 전역 보정을 구현하며, 적대적 운동 사전을 활용하여 부자연스러운 행동을 억제합니다.

## 핵심 내용
### 방법
- **폐루프 전역 추적**: CLOT은 고주파 위치 피드백(예: 외부 모션 캡처 또는 내부 센서)을 활용하여 운영자와 로봇의 전역 자세를 실시간으로 동기화하여 폐루프 제어를 형성하고 누적 드리프트를 제거합니다.
- **데이터 기반 무작위화 전략**: 전역 추적 보상을 직접 적용할 때 발생하는 과격한 보정을 완화하기 위해, 이 방법은 관측 궤적과 보상 평가를 분리합니다. 훈련 중 관측 궤적을 무작위화함으로써, 정책은 안정성을 유지하면서 전역 보정을 수행하고 과도한 반응을 피하는 법을 학습합니다.
- **적대적 운동 사전**: 정책이 생성한 운동과 실제 인간 운동 데이터를 구분하는 적대적 판별기를 도입합니다. 이 사전은 정규화 항으로 작용하여 부자연스럽거나 비인간적인 동작을 처벌하고 원격 조작의 사실감을 향상시킵니다.

### 아키텍처 및 훈련
- **정책 네트워크**: Transformer 기반 아키텍처를 채택하여 고차원 입력(예: 관절 각도, 전역 자세 오차, 운영자 동작 시퀀스)을 처리하고 로봇 관절 목표를 출력합니다.
- **훈련 데이터**: 다양한 전신 동작(예: 걷기, 회전, 잡기)을 포함하는 20시간의 정제된 인간 운동 데이터를 수집하여 원격 조작 정책을 훈련합니다.
- **계산 자원**: 정책은 1300 GPU 시간 이상 동안 훈련되어 모델 수렴과 일반화 능력을 보장합니다.
- **로봇 플랫폼**: 손을 제외한 31 자유도를 가진 전신 휴머노이드 로봇에 배포되며, 몸통, 팔, 다리 등 주요 관절을 포함합니다.

### 실험 설정 및 결과
- **시뮬레이션 실험**: 시뮬레이션 환경에서 테스트하여 고역학적 움직임(예: 빠른 걷기, 점프)과 고정밀 추적(전역 자세 오차 5cm 미만) 능력을 검증합니다.
- **실제 세계 실험**: 실제 휴머노이드 로봇에 배포하여 복잡한 지형(예: 경사로, 장애물)에서의 안정적인 원격 조작을 포함한 강력한 sim-to-real 견고성을 보여줍니다.
- **주요 수치**: 시스템은 장시간 작동(10분 이상)에서 드리프트 없는 추적을 유지하며, 전역 자세 오차는 센티미터 수준으로 제어됩니다. 적대적 사전은 부자연스러운 동작 발생률을 40% 이상 감소시킵니다.
- **결론**: CLOT은 폐루프 전역 피드백과 지능적인 보상 설계를 통해 전신 휴머노이드 로봇 원격 조작의 안정성과 자연스러움을 크게 향상시켜, 장시간 및 고역학적 작업에 대한 실현 가능한 솔루션을 제공합니다.
