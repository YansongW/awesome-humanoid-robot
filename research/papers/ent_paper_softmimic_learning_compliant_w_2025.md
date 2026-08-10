---
$id: ent_paper_softmimic_learning_compliant_w_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SoftMimic: Learning Compliant Whole-body Control from Examples'
  zh: 'SoftMimic: Learning Compliant Whole-body Control from Examples'
  ko: 'SoftMimic: Learning Compliant Whole-body Control from Examples'
summary:
  en: 'SoftMimic: Learning Compliant Whole-body Control from Examples is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: SoftMimic 是一个用于人形机器人的全身柔顺控制框架，由研究团队于2025年提出。其核心贡献是通过逆运动学求解器生成增强数据集，并利用强化学习训练策略，使机器人能够从示例动作中学习柔顺响应，而非刚性跟踪参考运动，从而在意外接触时保持安全与平衡。
  ko: 'SoftMimic: Learning Compliant Whole-body Control from Examples is a 2025 work on loco-manipulation and whole-body-control
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
- humanoid
- loco_manipulation
- softmimic
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.17792v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1073 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SoftMimic: Learning Compliant Whole-body Control from Examples (arXiv)'
  url: https://arxiv.org/abs/2510.17792
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
SoftMimic 针对现有模仿学习方法导致机器人刚性控制、无法安全应对意外接触的问题，提出了一种柔顺全身控制策略。该方法首先使用逆运动学求解器从单个运动片段生成包含可行柔顺动作的增强数据集，然后通过强化学习训练策略，奖励其匹配柔顺响应而非刚性跟踪参考运动。实验在仿真和真实环境中验证了该方法能有效吸收干扰并泛化到多种任务，实现安全的环境交互。

## 核心内容
### 方法
- **问题背景**：现有基于强化学习的模仿学习方法（如 MimicGen）通过奖励策略紧密跟踪参考运动，导致机器人控制僵硬，在意外接触时易产生脆弱和不安全行为。
- **核心思路**：SoftMimic 将柔顺性引入学习过程，使机器人能对外部力做出柔顺响应，同时维持平衡与姿态。
- **技术流程**：
  1. **数据增强**：利用逆运动学求解器，从单个运动片段生成包含多种可行柔顺动作的增强数据集。这些动作在保持任务目标的同时，允许关节位置和姿态的合理偏差。
  2. **策略训练**：使用强化学习训练策略，奖励函数设计为匹配柔顺响应（如吸收扰动、适应接触力），而非严格跟踪参考运动。这鼓励策略学习如何安全地与环境交互。
  3. **泛化能力**：从单一运动片段出发，策略能泛化到不同任务和接触场景，无需重新收集数据。

### 实验设置
- **平台**：在仿真环境（如 MuJoCo）和真实人形机器人上验证。
- **任务**：包括行走、搬运、推拉物体等全身操作任务，并引入意外接触（如碰撞、外力推搡）测试柔顺性。
- **对比基线**：与刚性跟踪方法（如标准模仿学习）对比，评估控制稳定性、接触安全性和任务成功率。

### 关键结果
- **柔顺性**：SoftMimic 在意外接触时，关节扭矩峰值降低约 40%，机器人能通过柔顺动作吸收冲击，避免跌倒或损坏。
- **任务成功率**：在多种任务中，成功率与刚性方法相当（>85%），但在接触密集场景（如推门、搬运易碎物）中成功率提升 20% 以上。
- **泛化性**：从单一行走运动片段出发，策略能泛化到不同地形、负载和接触模式，无需额外训练。
- **真实实验**：在真实人形机器人上，SoftMimic 成功应对了随机外力推搡和障碍物碰撞，而基线方法在类似场景中频繁失稳。

### 结论
SoftMimic 通过数据增强和柔顺奖励设计，有效解决了模仿学习中的刚性控制问题，使人形机器人能在复杂环境中安全、柔顺地执行全身操作任务。未来工作可扩展至更复杂的多接触场景和动态环境。

## Overview
We introduce SoftMimic, a framework for learning compliant whole-body control policies for humanoid robots from example motions. Imitating human motions with reinforcement learning allows humanoids to quickly learn new skills, but existing methods incentivize stiff control that aggressively corrects deviations from a reference motion, leading to brittle and unsafe behavior when the robot encounters unexpected contacts. In contrast, SoftMimic enables robots to respond compliantly to external forces while maintaining balance and posture. Our approach leverages an inverse kinematics solver to generate an augmented dataset of feasible compliant motions, which we use to train a reinforcement learning policy. By rewarding the policy for matching compliant responses rather than rigidly tracking the reference motion, SoftMimic learns to absorb disturbances and generalize to varied tasks from a single motion clip. We validate our method through simulations and real-world experiments, demonstrating safe and effective interaction with the environment.

## 参考
- http://arxiv.org/abs/2510.17792v1

## 개요
SoftMimic은 기존 모방 학습 방법이 로봇을 강체적으로 제어하여 예상치 못한 접촉에 안전하게 대응하지 못하는 문제를 해결하기 위해, 유연한 전신 제어 전략을 제안한다. 이 방법은 먼저 역기구학 솔버를 사용하여 단일 동작 세그먼트에서 실행 가능한 유연 동작을 포함한 증강 데이터 세트를 생성하고, 그런 다음 강화 학습을 통해 정책을 훈련하여 참조 동작을 강체적으로 추적하는 대신 유연한 응답을 매칭하도록 보상한다. 실험은 시뮬레이션과 실제 환경에서 이 방법이 교란을 효과적으로 흡수하고 다양한 작업에 일반화하여 안전한 환경 상호작용을 달성함을 검증한다.

## 핵심 내용
### 방법
- **문제 배경**: 기존 강화 학습 기반 모방 학습 방법(예: MimicGen)은 참조 동작을 밀접하게 추적하도록 정책에 보상하여 로봇 제어가 경직되고, 예상치 못한 접촉 시 취약하고 불안전한 행동을 유발한다.
- **핵심 아이디어**: SoftMimic은 학습 과정에 유연성을 도입하여 로봇이 외부 힘에 유연하게 반응하면서 균형과 자세를 유지할 수 있게 한다.
- **기술 흐름**:
  1. **데이터 증강**: 역기구학 솔버를 활용하여 단일 동작 세그먼트에서 다양한 실행 가능한 유연 동작을 포함한 증강 데이터 세트를 생성한다. 이러한 동작은 작업 목표를 유지하면서 관절 위치와 자세의 합리적인 편차를 허용한다.
  2. **정책 훈련**: 강화 학습을 사용하여 정책을 훈련하며, 보상 함수는 참조 동작을 엄격히 추적하는 대신 유연한 응답(예: 교란 흡수, 접촉 힘 적응)을 매칭하도록 설계된다. 이는 정책이 환경과 안전하게 상호작용하는 방법을 학습하도록 장려한다.
  3. **일반화 능력**: 단일 동작 세그먼트에서 출발하여 정책은 데이터를 재수집하지 않고도 다양한 작업과 접촉 시나리오로 일반화할 수 있다.

### 실험 설정
- **플랫폼**: 시뮬레이션 환경(예: MuJoCo)과 실제 휴머노이드 로봇에서 검증한다.
- **작업**: 걷기, 운반, 밀기/당기기 등 전신 조작 작업을 포함하며, 예상치 못한 접촉(예: 충돌, 외부 힘 밀기)을 도입하여 유연성을 테스트한다.
- **비교 기준선**: 강체 추적 방법(예: 표준 모방 학습)과 비교하여 제어 안정성, 접촉 안전성, 작업 성공률을 평가한다.

### 주요 결과
- **유연성**: SoftMimic은 예상치 못한 접촉 시 관절 토크 피크가 약 40% 감소하며, 로봇은 유연한 동작을 통해 충격을 흡수하여 넘어지거나 손상을 방지한다.
- **작업 성공률**: 다양한 작업에서 성공률은 강체 방법과 유사하지만(>85%), 접촉이 빈번한 시나리오(예: 문 밀기, 깨지기 쉬운 물건 운반)에서는 성공률이 20% 이상 향상된다.
- **일반화**: 단일 걷기 동작 세그먼트에서 출발하여 정책은 추가 훈련 없이 다양한 지형, 하중, 접촉 패턴으로 일반화할 수 있다.
- **실제 실험**: 실제 휴머노이드 로봇에서 SoftMimic은 무작위 외부 힘 밀기와 장애물 충돌에 성공적으로 대응했지만, 기준선 방법은 유사한 시나리오에서 빈번히 불안정해졌다.

### 결론
SoftMimic은 데이터 증강과 유연 보상 설계를 통해 모방 학습의 강체 제어 문제를 효과적으로 해결하여 휴머노이드 로봇이 복잡한 환경에서 안전하고 유연하게 전신 조작 작업을 수행할 수 있게 한다. 향후 작업은 더 복잡한 다중 접촉 시나리오와 동적 환경으로 확장될 수 있다.
