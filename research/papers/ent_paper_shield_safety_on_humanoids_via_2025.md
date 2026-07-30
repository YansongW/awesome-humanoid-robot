---
$id: ent_paper_shield_safety_on_humanoids_via_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics'
  zh: 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics'
  ko: 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics'
summary:
  en: 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics is a 2025 work on locomotion for humanoid robots.'
  zh: SHIELD 是 2025 年提出的一种分层安全框架，旨在为人形机器人的动态运动提供安全保障。该工作由研究团队基于 Unitree G1 人形机器人实现，核心贡献在于通过训练生成式随机动力学残差模型，并结合随机离散时间控制障碍函数（CBF），在概率意义上为基于学习的控制器提供形式化的安全约束。
  ko: 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- shield
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.11494v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics (arXiv)'
  url: https://arxiv.org/abs/2505.11494
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对强化学习控制器难以在运行时保证动态安全且修改约束需重新训练的问题，SHIELD 提出了一种分层安全框架。该框架首先利用标称控制器在硬件上运行的真实数据，训练一个生成式随机动力学残差模型，以捕捉系统行为与不确定性。随后，在该标称控制器之上添加一个安全层，通过随机离散时间 CBF 公式，在概率意义上强制执行安全约束。最终，SHIELD 以最小侵入的方式集成到现有自主系统中，在风险与性能之间取得平衡，为安全提供概率性保证。

## 核心内容
### 方法
SHIELD 采用分层架构，在现有标称（学习型）运动控制器之上叠加一个安全层。该安全层不修改底层控制器，而是通过干预其输出以维持安全约束。

### 核心组件
1.  **动力学残差模型**：利用标称控制器在硬件部署中收集的真实世界数据，训练一个生成式随机动力学残差模型。该模型旨在捕捉系统实际行为与标称模型之间的偏差及其不确定性。
2.  **随机离散时间 CBF**：基于上述随机模型，采用一种随机离散时间控制障碍函数（CBF）公式。该公式将安全约束表达为概率条件，即系统状态以不低于指定概率保持在安全集内。

### 实验设置
-   **硬件平台**：Unitree G1 人形机器人。
-   **标称控制器**：一个未知的强化学习（RL）运动控制器。
-   **感知**：机器人搭载机载感知系统。
-   **任务**：在多种室内外环境中执行安全导航（避障）。

### 关键结果
-   SHIELD 成功地在硬件实验中实现了安全导航，使 Unitree G1 能够有效避开障碍物。
-   该框架以最小侵入的方式工作，无需重新训练或修改底层的 RL 控制器。
-   通过概率性 CBF 公式，SHIELD 在保证安全（以概率形式）的同时，尽可能减少对标称控制器性能的影响，从而平衡了风险与任务表现。

## Overview
Robot learning has produced remarkably effective ``black-box'' controllers for complex tasks such as dynamic locomotion on humanoids. Yet ensuring dynamic safety, i.e., constraint satisfaction, remains challenging for such policies. Reinforcement learning (RL) embeds constraints heuristically through reward engineering, and adding or modifying constraints requires retraining. Model-based approaches, like control barrier functions (CBFs), enable runtime constraint specification with formal guarantees but require accurate dynamics models. This paper presents SHIELD, a layered safety framework that bridges this gap by: (1) training a generative, stochastic dynamics residual model using real-world data from hardware rollouts of the nominal controller, capturing system behavior and uncertainties; and (2) adding a safety layer on top of the nominal (learned locomotion) controller that leverages this model via a stochastic discrete-time CBF formulation enforcing safety constraints in probability. The result is a minimally-invasive safety layer that can be added to the existing autonomy stack to give probabilistic guarantees of safety that balance risk and performance. In hardware experiments on an Unitree G1 humanoid, SHIELD enables safe navigation (obstacle avoidance) through varied indoor and outdoor environments using a nominal (unknown) RL controller and onboard perception.

## Overview
Robot learning has produced remarkably effective "black-box" controllers for complex tasks such as dynamic locomotion on humanoids. Yet ensuring dynamic safety, i.e., constraint satisfaction, remains challenging for such policies. Reinforcement learning (RL) embeds constraints heuristically through reward engineering, and adding or modifying constraints requires retraining. Model-based approaches, like control barrier functions (CBFs), enable runtime constraint specification with formal guarantees but require accurate dynamics models. This paper presents SHIELD, a layered safety framework that bridges this gap by: (1) training a generative, stochastic dynamics residual model using real-world data from hardware rollouts of the nominal controller, capturing system behavior and uncertainties; and (2) adding a safety layer on top of the nominal (learned locomotion) controller that leverages this model via a stochastic discrete-time CBF formulation enforcing safety constraints in probability. The result is a minimally-invasive safety layer that can be added to the existing autonomy stack to give probabilistic guarantees of safety that balance risk and performance. In hardware experiments on an Unitree G1 humanoid, SHIELD enables safe navigation (obstacle avoidance) through varied indoor and outdoor environments using a nominal (unknown) RL controller and onboard perception.

## Content
Robot learning has produced remarkably effective "black-box" controllers for complex tasks such as dynamic locomotion on humanoids. Yet ensuring dynamic safety, i.e., constraint satisfaction, remains challenging for such policies. Reinforcement learning (RL) embeds constraints heuristically through reward engineering, and adding or modifying constraints requires retraining. Model-based approaches, like control barrier functions (CBFs), enable runtime constraint specification with formal guarantees but require accurate dynamics models. This paper presents SHIELD, a layered safety framework that bridges this gap by: (1) training a generative, stochastic dynamics residual model using real-world data from hardware rollouts of the nominal controller, capturing system behavior and uncertainties; and (2) adding a safety layer on top of the nominal (learned locomotion) controller that leverages this model via a stochastic discrete-time CBF formulation enforcing safety constraints in probability. The result is a minimally-invasive safety layer that can be added to the existing autonomy stack to give probabilistic guarantees of safety that balance risk and performance. In hardware experiments on an Unitree G1 humanoid, SHIELD enables safe navigation (obstacle avoidance) through varied indoor and outdoor environments using a nominal (unknown) RL controller and onboard perception.

## 개요
로봇 학습은 휴머노이드의 동적 보행과 같은 복잡한 작업에 대해 매우 효과적인 '블랙박스' 제어기를 생성해 왔습니다. 그러나 동적 안전, 즉 제약 조건 충족을 보장하는 것은 이러한 정책에 있어 여전히 어려운 과제입니다. 강화 학습(RL)은 보상 엔지니어링을 통해 경험적으로 제약 조건을 포함시키며, 제약 조건을 추가하거나 수정하려면 재학습이 필요합니다. 제어 장벽 함수(CBF)와 같은 모델 기반 접근 방식은 런타임 제약 조건 명세를 공식적인 보장과 함께 가능하게 하지만 정확한 동역학 모델을 필요로 합니다. 본 논문은 SHIELD를 제시합니다. 이는 계층적 안전 프레임워크로, 다음을 통해 이러한 격차를 해소합니다: (1) 공칭 제어기의 하드웨어 롤아웃에서 얻은 실제 데이터를 사용하여 생성적이고 확률적인 동역학 잔차 모델을 훈련하여 시스템 동작과 불확실성을 포착하고; (2) 공칭(학습된 보행) 제어기 위에 안전 계층을 추가하여 확률적 이산 시간 CBF 공식을 통해 이 모델을 활용, 확률적으로 안전 제약 조건을 강제합니다. 그 결과는 기존 자율 주행 스택에 추가되어 위험과 성능의 균형을 맞추는 확률적 안전 보장을 제공하는 최소 침습적 안전 계층입니다. Unitree G1 휴머노이드의 하드웨어 실험에서 SHIELD는 공칭(알려지지 않은) RL 제어기와 온보드 인식을 사용하여 다양한 실내 및 실외 환경에서 안전한 탐색(장애물 회피)을 가능하게 합니다.

## 핵심 내용
로봇 학습은 휴머노이드의 동적 보행과 같은 복잡한 작업에 대해 매우 효과적인 '블랙박스' 제어기를 생성해 왔습니다. 그러나 동적 안전, 즉 제약 조건 충족을 보장하는 것은 이러한 정책에 있어 여전히 어려운 과제입니다. 강화 학습(RL)은 보상 엔지니어링을 통해 경험적으로 제약 조건을 포함시키며, 제약 조건을 추가하거나 수정하려면 재학습이 필요합니다. 제어 장벽 함수(CBF)와 같은 모델 기반 접근 방식은 런타임 제약 조건 명세를 공식적인 보장과 함께 가능하게 하지만 정확한 동역학 모델을 필요로 합니다. 본 논문은 SHIELD를 제시합니다. 이는 계층적 안전 프레임워크로, 다음을 통해 이러한 격차를 해소합니다: (1) 공칭 제어기의 하드웨어 롤아웃에서 얻은 실제 데이터를 사용하여 생성적이고 확률적인 동역학 잔차 모델을 훈련하여 시스템 동작과 불확실성을 포착하고; (2) 공칭(학습된 보행) 제어기 위에 안전 계층을 추가하여 확률적 이산 시간 CBF 공식을 통해 이 모델을 활용, 확률적으로 안전 제약 조건을 강제합니다. 그 결과는 기존 자율 주행 스택에 추가되어 위험과 성능의 균형을 맞추는 확률적 안전 보장을 제공하는 최소 침습적 안전 계층입니다. Unitree G1 휴머노이드의 하드웨어 실험에서 SHIELD는 공칭(알려지지 않은) RL 제어기와 온보드 인식을 사용하여 다양한 실내 및 실외 환경에서 안전한 탐색(장애물 회피)을 가능하게 합니다.

## 参考
- http://arxiv.org/abs/2505.11494v3
