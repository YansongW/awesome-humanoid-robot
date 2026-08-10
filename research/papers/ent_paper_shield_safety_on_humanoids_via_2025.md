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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.11494v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (794 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2505.11494v3

## 개요
강화 학습 컨트롤러가 실행 중에 동적 안전성을 보장하기 어렵고 제약 조건을 수정하려면 재학습이 필요한 문제를 해결하기 위해, SHIELD는 계층적 안전 프레임워크를 제안합니다. 이 프레임워크는 먼저 명목 컨트롤러가 하드웨어에서 실행될 때 수집된 실제 데이터를 활용하여 생성적 확률적 동역학 잔차 모델을 훈련하고, 시스템 동작과 불확실성을 포착합니다. 이후 명목 컨트롤러 위에 안전 계층을 추가하여 확률적 이산 시간 CBF 공식을 통해 안전 제약 조건을 확률적 의미에서 강제합니다. 마지막으로 SHIELD는 최소 침습적 방식으로 기존 자율 시스템에 통합되어 위험과 성능 사이의 균형을 유지하며 안전에 대한 확률적 보장을 제공합니다.

## 핵심 내용
### 방법
SHIELD는 계층적 아키텍처를 채택하여 기존 명목(학습 기반) 운동 컨트롤러 위에 안전 계층을 추가합니다. 이 안전 계층은 하위 컨트롤러를 수정하지 않고, 그 출력에 개입하여 안전 제약 조건을 유지합니다.

### 핵심 구성 요소
1.  **동역학 잔차 모델**: 명목 컨트롤러가 하드웨어 배포에서 수집한 실제 데이터를 활용하여 생성적 확률적 동역학 잔차 모델을 훈련합니다. 이 모델은 시스템의 실제 동작과 명목 모델 간의 편차 및 그 불확실성을 포착하는 것을 목표로 합니다.
2.  **확률적 이산 시간 CBF**: 위의 확률적 모델을 기반으로 확률적 이산 시간 제어 장벽 함수(CBF) 공식을 채택합니다. 이 공식은 안전 제약 조건을 확률적 조건으로 표현하며, 즉 시스템 상태가 지정된 확률 이상으로 안전 집합 내에 유지되도록 합니다.

### 실험 설정
-   **하드웨어 플랫폼**: Unitree G1 휴머노이드 로봇.
-   **명목 컨트롤러**: 알려지지 않은 강화 학습(RL) 운동 컨트롤러.
-   **인식**: 로봇은 온보드 인식 시스템을 탑재합니다.
-   **작업**: 다양한 실내외 환경에서 안전한 내비게이션(장애물 회피) 수행.

### 주요 결과
-   SHIELD는 하드웨어 실험에서 안전한 내비게이션을 성공적으로 구현하여 Unitree G1이 장애물을 효과적으로 회피할 수 있게 했습니다.
-   이 프레임워크는 최소 침습적 방식으로 작동하며, 하위 RL 컨트롤러를 재학습하거나 수정할 필요가 없습니다.
-   확률적 CBF 공식을 통해 SHIELD는 안전(확률적 형태)을 보장하면서도 명목 컨트롤러의 성능에 미치는 영향을 최소화하여 위험과 작업 성능 사이의 균형을 유지합니다.
