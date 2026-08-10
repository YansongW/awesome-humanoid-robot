---
$id: ent_paper_ulc_a_unified_and_fine_grained_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation'
  zh: ULC｜用于人形移动操作的统一细粒度控制器
  ko: 'ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation'
summary:
  en: Loco-Manipulation for humanoid robots aims to enable robots to integrate mobility with upper-body tracking capabilities.
    Most existing approaches adopt hierarchical architectures that decompose control into isolated upper-body (manipulation)
    and lower-body (locomotion) policies. While this decomposition reduces training complexity, it inherently limits coordination
    between subsystems and contradicts the unified whole-body control exhibited by humans. We demonstrate that a single unified
    policy can achieve a combination of tracking accuracy, large workspace, and robustness for humanoid loco-manipulation.
    We propose the Unified Loco-Manipulation Controller (ULC), a single-policy framework that simultaneously tracks root velocity,
    root height, torso rotation, and dual-arm joint positions in a
  zh: ULC（统一移动操作控制器）是一个单策略框架，用于人形机器人的全身协调控制。由研究团队提出，核心贡献在于通过单一策略同时跟踪根部速度、根部高度、躯干旋转和双臂关节位置，实现了高精度、大工作空间和鲁棒性，验证了统一控制在不牺牲性能下的可行性。
  ko: ULC 把本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、全身控制器/WBC/MPC、分层技能/专家策略训练或组合全身策略，最终输出关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
domains:
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- manipulation_interface
- mobile_manipulation
- ulc
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: ULC: A Unified and Fine-Grained
    Controller for Humanoid Loco-Manipulation. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (930 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: ULC project page
  url: https://hellod035.github.io/ULC/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
现有的人形机器人移动操作大多采用分层架构，将控制分解为孤立的上半身（操作）和下半身（移动）策略，这限制了子系统间的协调，与人类的统一全身控制相悖。ULC 提出了一种端到端的单策略框架，通过序列技能获取、残差动作建模、命令多项式插值、随机延迟释放、负载随机化和重心跟踪等关键技术，实现了对多个运动目标的同步跟踪。在 Unitree G1 人形机器人（3-DOF 腰部）上的实验表明，ULC 在跟踪精度和工作空间覆盖上优于解耦方法，并能在外负载下保持精确的双臂操作和协调的全身控制。

## 核心内容
### 方法概述
ULC 是一个单策略框架，旨在实现人形机器人移动操作的统一控制。其核心思想是摒弃传统的分层架构，通过一个端到端的策略同时跟踪多个运动目标，包括根部速度、根部高度、躯干旋转和双臂关节位置。

### 关键技术
- **序列技能获取**：通过渐进式学习复杂度，使策略逐步掌握从简单到复杂的技能组合。
- **残差动作建模**：对基础动作进行细粒度调整，提升控制精度。
- **命令多项式插值**：实现平滑的运动过渡，避免动作突变。
- **随机延迟释放**：模拟部署中的延迟变化，增强策略的鲁棒性。
- **负载随机化**：训练时随机施加外部负载，使策略能泛化到未知干扰。
- **重心跟踪**：提供显式策略梯度，帮助维持机器人稳定性。

### 实验设置
- **平台**：Unitree G1 人形机器人，配备 3-DOF 腰部。
- **基线**：与多种强基线方法（包括解耦方法）进行比较。
- **任务**：包括移动操作任务，如在外负载下进行双臂跟踪。

### 关键结果
- **跟踪性能**：ULC 在跟踪精度上显著优于解耦方法，特别是在多目标同步跟踪场景中。
- **工作空间覆盖**：ULC 展示了更大的工作空间覆盖范围，能够执行更复杂的移动操作任务。
- **鲁棒性**：在外负载干扰下，ULC 仍能保持精确的双臂操作和协调的全身控制，验证了其鲁棒性。

### 结论
ULC 证明了单策略框架在人形机器人移动操作中的可行性，通过统一控制实现了高精度、大工作空间和强鲁棒性，为未来人形机器人的全身协调控制提供了新思路。

## Overview
Loco-Manipulation for humanoid robots aims to enable robots to integrate mobility with upper-body tracking capabilities. Most existing approaches adopt hierarchical architectures that decompose control into isolated upper-body (manipulation) and lower-body (locomotion) policies. While this decomposition reduces training complexity, it inherently limits coordination between subsystems and contradicts the unified whole-body control exhibited by humans. We demonstrate that a single unified policy can achieve a combination of tracking accuracy, large workspace, and robustness for humanoid loco-manipulation. We propose the Unified Loco-Manipulation Controller (ULC), a single-policy framework that simultaneously tracks root velocity, root height, torso rotation, and dual-arm joint positions in an end-to-end manner, proving the feasibility of unified control without sacrificing performance. We achieve this unified control through key technologies: sequence skill acquisition for progressive learning complexity, residual action modeling for fine-grained control adjustments, command polynomial interpolation for smooth motion transitions, random delay release for robustness to deploy variations, load randomization for generalization to external disturbances, and center-of-gravity tracking for providing explicit policy gradients to maintain stability. We validate our method on the Unitree G1 humanoid robot with 3-DOF (degrees-of-freedom) waist. Compared with strong baselines, ULC shows better tracking performance to disentangled methods and demonstrating larger workspace coverage. The unified dual-arm tracking enables precise manipulation under external loads while maintaining coordinated whole-body control for complex loco-manipulation tasks.

## 参考
- Semantic Scholar search: ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation

## 개요
기존의 휴머노이드 로봇 이동 조작은 대부분 계층적 아키텍처를 채택하여 제어를 분리된 상반신(조작) 및 하반신(이동) 정책으로 분해하며, 이는 하위 시스템 간의 협조를 제한하고 인간의 통합된 전신 제어와 상충됩니다. ULC는 단일 정책 프레임워크를 제안하며, 순차적 스킬 획득, 잔차 동작 모델링, 명령 다항식 보간, 무작위 지연 릴리스, 부하 무작위화 및 무게 중심 추적과 같은 핵심 기술을 통해 여러 운동 목표의 동기 추적을 구현합니다. Unitree G1 휴머노이드 로봇(3-DOF 허리)에서의 실험은 ULC가 추적 정확도와 작업 공간 커버리지에서 분리 방법보다 우수하며, 외부 부하 하에서도 정밀한 양팔 조작과 협조된 전신 제어를 유지할 수 있음을 보여줍니다.

## 핵심 내용
### 방법 개요
ULC는 휴머노이드 로봇 이동 조작의 통합 제어를 목표로 하는 단일 정책 프레임워크입니다. 핵심 아이디어는 전통적인 계층적 아키텍처를 버리고, 루트 속도, 루트 높이, 몸통 회전 및 양팔 관절 위치를 포함한 여러 운동 목표를 동시에 추적하는 엔드투엔드 정책을 사용하는 것입니다.

### 핵심 기술
- **순차적 스킬 획득**: 점진적으로 복잡도를 학습하여 정책이 단순한 스킬 조합에서 복잡한 스킬 조합으로 점차 습득하게 합니다.
- **잔차 동작 모델링**: 기본 동작에 세밀한 조정을 수행하여 제어 정밀도를 향상시킵니다.
- **명령 다항식 보간**: 부드러운 운동 전환을 구현하여 동작 급변을 방지합니다.
- **무작위 지연 릴리스**: 배포 중 지연 변화를 시뮬레이션하여 정책의 견고성을 강화합니다.
- **부하 무작위화**: 훈련 중 무작위 외부 부하를 적용하여 정책이 알 수 없는 교란에 일반화될 수 있게 합니다.
- **무게 중심 추적**: 명시적 정책 기울기를 제공하여 로봇 안정성을 유지하는 데 도움을 줍니다.

### 실험 설정
- **플랫폼**: Unitree G1 휴머노이드 로봇, 3-DOF 허리 장착.
- **기준선**: 다양한 강력한 기준 방법(분리 방법 포함)과 비교.
- **작업**: 외부 부하 하에서 양팔 추적과 같은 이동 조작 작업 포함.

### 핵심 결과
- **추적 성능**: ULC는 특히 다중 목표 동기 추적 시나리오에서 추적 정확도에서 분리 방법보다 현저히 우수합니다.
- **작업 공간 커버리지**: ULC는 더 큰 작업 공간 커버리지를 보여주며, 더 복잡한 이동 조작 작업을 수행할 수 있습니다.
- **견고성**: 외부 부하 교란 하에서도 ULC는 정밀한 양팔 조작과 협조된 전신 제어를 유지하여 견고성을 검증합니다.

### 결론
ULC는 휴머노이드 로봇 이동 조작에서 단일 정책 프레임워크의 실행 가능성을 입증하며, 통합 제어를 통해 높은 정밀도, 넓은 작업 공간 및 강한 견고성을 구현하여 미래 휴머노이드 로봇의 전신 협조 제어에 새로운 방향을 제시합니다.
