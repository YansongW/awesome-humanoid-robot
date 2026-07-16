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
  zh: ULC 把本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、全身控制器/WBC/MPC、分层技能/专家策略训练或组合全身策略，最终输出关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
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
    Controller for Humanoid Loco-Manipulation.'
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
Loco-Manipulation for humanoid robots aims to enable robots to integrate mobility with upper-body tracking capabilities. Most existing approaches adopt hierarchical architectures that decompose control into isolated upper-body (manipulation) and lower-body (locomotion) policies. While this decomposition reduces training complexity, it inherently limits coordination between subsystems and contradicts the unified whole-body control exhibited by humans. We demonstrate that a single unified policy can achieve a combination of tracking accuracy, large workspace, and robustness for humanoid loco-manipulation. We propose the Unified Loco-Manipulation Controller (ULC), a single-policy framework that simultaneously tracks root velocity, root height, torso rotation, and dual-arm joint positions in an end-to-end manner, proving the feasibility of unified control without sacrificing performance. We achieve this unified control through key technologies: sequence skill acquisition for progressive learning complexity, residual action modeling for fine-grained control adjustments, command polynomial interpolation for smooth motion transitions, random delay release for robustness to deploy variations, load randomization for generalization to external disturbances, and center-of-gravity tracking for providing explicit policy gradients to maintain stability. We validate our method on the Unitree G1 humanoid robot with 3-DOF (degrees-of-freedom) waist. Compared with strong baselines, ULC shows better tracking performance to disentangled methods and demonstrating larger workspace coverage. The unified dual-arm tracking enables precise manipulation under external loads while maintaining coordinated whole-body control for complex loco-manipulation tasks.

## 核心内容
Loco-Manipulation for humanoid robots aims to enable robots to integrate mobility with upper-body tracking capabilities. Most existing approaches adopt hierarchical architectures that decompose control into isolated upper-body (manipulation) and lower-body (locomotion) policies. While this decomposition reduces training complexity, it inherently limits coordination between subsystems and contradicts the unified whole-body control exhibited by humans. We demonstrate that a single unified policy can achieve a combination of tracking accuracy, large workspace, and robustness for humanoid loco-manipulation. We propose the Unified Loco-Manipulation Controller (ULC), a single-policy framework that simultaneously tracks root velocity, root height, torso rotation, and dual-arm joint positions in an end-to-end manner, proving the feasibility of unified control without sacrificing performance. We achieve this unified control through key technologies: sequence skill acquisition for progressive learning complexity, residual action modeling for fine-grained control adjustments, command polynomial interpolation for smooth motion transitions, random delay release for robustness to deploy variations, load randomization for generalization to external disturbances, and center-of-gravity tracking for providing explicit policy gradients to maintain stability. We validate our method on the Unitree G1 humanoid robot with 3-DOF (degrees-of-freedom) waist. Compared with strong baselines, ULC shows better tracking performance to disentangled methods and demonstrating larger workspace coverage. The unified dual-arm tracking enables precise manipulation under external loads while maintaining coordinated whole-body control for complex loco-manipulation tasks.

## 参考
- Semantic Scholar search: ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation

## Overview
Loco-Manipulation for humanoid robots aims to enable robots to integrate mobility with upper-body tracking capabilities. Most existing approaches adopt hierarchical architectures that decompose control into isolated upper-body (manipulation) and lower-body (locomotion) policies. While this decomposition reduces training complexity, it inherently limits coordination between subsystems and contradicts the unified whole-body control exhibited by humans. We demonstrate that a single unified policy can achieve a combination of tracking accuracy, large workspace, and robustness for humanoid loco-manipulation. We propose the Unified Loco-Manipulation Controller (ULC), a single-policy framework that simultaneously tracks root velocity, root height, torso rotation, and dual-arm joint positions in an end-to-end manner, proving the feasibility of unified control without sacrificing performance. We achieve this unified control through key technologies: sequence skill acquisition for progressive learning complexity, residual action modeling for fine-grained control adjustments, command polynomial interpolation for smooth motion transitions, random delay release for robustness to deploy variations, load randomization for generalization to external disturbances, and center-of-gravity tracking for providing explicit policy gradients to maintain stability. We validate our method on the Unitree G1 humanoid robot with 3-DOF (degrees-of-freedom) waist. Compared with strong baselines, ULC shows better tracking performance to disentangled methods and demonstrating larger workspace coverage. The unified dual-arm tracking enables precise manipulation under external loads while maintaining coordinated whole-body control for complex loco-manipulation tasks.

## Content
Loco-Manipulation for humanoid robots aims to enable robots to integrate mobility with upper-body tracking capabilities. Most existing approaches adopt hierarchical architectures that decompose control into isolated upper-body (manipulation) and lower-body (locomotion) policies. While this decomposition reduces training complexity, it inherently limits coordination between subsystems and contradicts the unified whole-body control exhibited by humans. We demonstrate that a single unified policy can achieve a combination of tracking accuracy, large workspace, and robustness for humanoid loco-manipulation. We propose the Unified Loco-Manipulation Controller (ULC), a single-policy framework that simultaneously tracks root velocity, root height, torso rotation, and dual-arm joint positions in an end-to-end manner, proving the feasibility of unified control without sacrificing performance. We achieve this unified control through key technologies: sequence skill acquisition for progressive learning complexity, residual action modeling for fine-grained control adjustments, command polynomial interpolation for smooth motion transitions, random delay release for robustness to deploy variations, load randomization for generalization to external disturbances, and center-of-gravity tracking for providing explicit policy gradients to maintain stability. We validate our method on the Unitree G1 humanoid robot with 3-DOF (degrees-of-freedom) waist. Compared with strong baselines, ULC shows better tracking performance to disentangled methods and demonstrating larger workspace coverage. The unified dual-arm tracking enables precise manipulation under external loads while maintaining coordinated whole-body control for complex loco-manipulation tasks.

## 개요
휴머노이드 로봇을 위한 로코-조작(Loco-Manipulation)은 로봇이 이동성과 상체 추적 기능을 통합할 수 있도록 하는 것을 목표로 합니다. 대부분의 기존 접근 방식은 제어를 분리된 상체(조작) 및 하체(보행) 정책으로 분해하는 계층적 아키텍처를 채택합니다. 이러한 분해는 훈련 복잡성을 줄이지만, 본질적으로 하위 시스템 간의 조정을 제한하고 인간이 보이는 통합된 전신 제어와 모순됩니다. 우리는 단일 통합 정책이 휴머노이드 로코-조작을 위한 추적 정확도, 넓은 작업 공간 및 강건성의 조합을 달성할 수 있음을 보여줍니다. 우리는 통합 로코-조작 컨트롤러(ULC)를 제안합니다. 이는 루트 속도, 루트 높이, 몸통 회전 및 양팔 관절 위치를 종단 간 방식으로 동시에 추적하는 단일 정책 프레임워크로, 성능 저하 없이 통합 제어의 실현 가능성을 입증합니다. 우리는 핵심 기술을 통해 이 통합 제어를 달성합니다: 점진적 학습 복잡성을 위한 시퀀스 스킬 획득, 세밀한 제어 조정을 위한 잔여 동작 모델링, 부드러운 동작 전환을 위한 명령 다항식 보간, 배포 변동에 대한 강건성을 위한 무작위 지연 해제, 외부 교란에 대한 일반화를 위한 부하 무작위화, 안정성 유지를 위한 명시적 정책 기울기 제공을 위한 무게 중심 추적. 우리는 3-DOF(자유도) 허리를 가진 Unitree G1 휴머노이드 로봇에서 우리의 방법을 검증합니다. 강력한 기준선과 비교하여 ULC는 분리된 방법보다 더 나은 추적 성능을 보여주고 더 넓은 작업 공간 범위를 입증합니다. 통합된 양팔 추적은 외부 부하 하에서 정밀한 조작을 가능하게 하면서 복잡한 로코-조작 작업을 위한 조정된 전신 제어를 유지합니다.

## 핵심 내용
휴머노이드 로봇을 위한 로코-조작(Loco-Manipulation)은 로봇이 이동성과 상체 추적 기능을 통합할 수 있도록 하는 것을 목표로 합니다. 대부분의 기존 접근 방식은 제어를 분리된 상체(조작) 및 하체(보행) 정책으로 분해하는 계층적 아키텍처를 채택합니다. 이러한 분해는 훈련 복잡성을 줄이지만, 본질적으로 하위 시스템 간의 조정을 제한하고 인간이 보이는 통합된 전신 제어와 모순됩니다. 우리는 단일 통합 정책이 휴머노이드 로코-조작을 위한 추적 정확도, 넓은 작업 공간 및 강건성의 조합을 달성할 수 있음을 보여줍니다. 우리는 통합 로코-조작 컨트롤러(ULC)를 제안합니다. 이는 루트 속도, 루트 높이, 몸통 회전 및 양팔 관절 위치를 종단 간 방식으로 동시에 추적하는 단일 정책 프레임워크로, 성능 저하 없이 통합 제어의 실현 가능성을 입증합니다. 우리는 핵심 기술을 통해 이 통합 제어를 달성합니다: 점진적 학습 복잡성을 위한 시퀀스 스킬 획득, 세밀한 제어 조정을 위한 잔여 동작 모델링, 부드러운 동작 전환을 위한 명령 다항식 보간, 배포 변동에 대한 강건성을 위한 무작위 지연 해제, 외부 교란에 대한 일반화를 위한 부하 무작위화, 안정성 유지를 위한 명시적 정책 기울기 제공을 위한 무게 중심 추적. 우리는 3-DOF(자유도) 허리를 가진 Unitree G1 휴머노이드 로봇에서 우리의 방법을 검증합니다. 강력한 기준선과 비교하여 ULC는 분리된 방법보다 더 나은 추적 성능을 보여주고 더 넓은 작업 공간 범위를 입증합니다. 통합된 양팔 추적은 외부 부하 하에서 정밀한 조작을 가능하게 하면서 복잡한 로코-조작 작업을 위한 조정된 전신 제어를 유지합니다.
