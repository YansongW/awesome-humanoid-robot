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

