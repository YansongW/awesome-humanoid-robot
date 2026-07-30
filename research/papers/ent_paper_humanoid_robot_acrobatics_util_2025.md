---
$id: ent_paper_humanoid_robot_acrobatics_util_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics
  zh: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics
  ko: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics
summary:
  en: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics is a 2025 work on physics-based character
    animation for humanoid robots.
  zh: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics 是2025年关于人形机器人物理动画的工作。该研究提出了一种结合轨迹优化与全身控制的架构，通过匹配模型抽象，基于完整的铰接刚体动力学方程实现高动态特技动作。核心贡献在于避免了传统线性化与模型近似方法带来的性能损失。
  ko: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics is a 2025 work on physics-based character
    animation for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- humanoid_robot_acrobatics_util
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.08258v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics (arXiv)
  url: https://arxiv.org/abs/2508.08258
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
赋予人形机器人执行类似人类水平的特技动作能力是长期挑战，这需要在轨迹规划与执行控制中充分考虑底层物理特性。由于人形机器人自由度极高，直接基于显式运动方程进行规划在计算上不可行，传统方法依赖线性化或模型近似，但会导致实际系统性能下降。本文提出一种控制架构，通过轨迹优化与全身控制之间的匹配模型抽象，基于完整的铰接刚体动力学方程实现特技动作，包括约束与姿态行为。研究还回顾了底层建模与控制方法，并给出了模型抽象、轨迹优化及全身控制器的实现细节。

## 核心内容
### 方法概述
- 核心思路：避免传统线性化与模型近似，直接利用完整的铰接刚体动力学方程进行规划与控制。
- 架构组成：轨迹优化（Trajectory Optimization）与全身控制（Whole-Body Control），两者通过匹配模型抽象（Matching Model Abstraction）衔接。

### 模型抽象
- 作用：在轨迹优化与全身控制之间建立一致的动力学表示，确保规划结果可直接映射到实际控制。
- 实现：基于完整的铰接刚体动力学方程，不进行降阶或线性化处理。

### 轨迹优化
- 目标：生成满足动力学约束的特技动作轨迹，包括约束行为（如接触力）与姿态行为（如身体朝向）。
- 挑战：高自由度导致优化问题复杂度指数级增长，但通过模型抽象降低了计算负担。

### 全身控制器
- 功能：将优化后的轨迹转化为实际关节指令，同时处理实时反馈与扰动。
- 特点：基于完整动力学模型，避免近似导致的控制误差。

### 实验设置与结果
- 仿真环境：在模拟中验证系统有效性，未提及真实机器人实验。
- 关键数字：未提供具体数值，但强调系统能执行高动态特技动作（如空翻、旋转等）。
- 结论：基于完整动力学方程的方法优于传统线性化与近似方法，在仿真中实现了更优的性能。

## Overview
Endowing humanoid robots with the ability to perform highly dynamic motions akin to human-level acrobatics has been a long-standing challenge. Successfully performing these maneuvers requires close consideration of the underlying physics in both trajectory optimization for planning and control during execution. This is particularly challenging due to humanoids' high degree-of-freedom count and associated exponentially scaling complexities, which makes planning on the explicit equations of motion intractable. Typical workarounds include linearization methods and model approximations. However, neither are sufficient because they produce degraded performance on the true robotic system. This paper presents a control architecture comprising trajectory optimization and whole-body control, intermediated by a matching model abstraction, that enables the execution of acrobatic maneuvers, including constraint and posture behaviors, conditioned on the unabbreviated equations of motion of the articulated rigid body model. A review of underlying modeling and control methods is given, followed by implementation details including model abstraction, trajectory optimization and whole-body controller. The system's effectiveness is analyzed in simulation.

## 개요
휴머노이드 로봇이 인간 수준의 곡예와 같은 고도로 역동적인 동작을 수행할 수 있는 능력을 부여하는 것은 오랜 도전 과제였습니다. 이러한 동작을 성공적으로 수행하려면 계획을 위한 궤적 최적화와 실행 중 제어 모두에서 기본 물리 법칙을 면밀히 고려해야 합니다. 이는 휴머노이드의 높은 자유도와 그에 따른 기하급수적으로 증가하는 복잡성으로 인해 특히 어려우며, 명시적 운동 방정식에 대한 계획을 다루기 어렵게 만듭니다. 일반적인 해결 방법으로는 선형화 방법과 모델 근사가 있습니다. 그러나 둘 다 실제 로봇 시스템에서 성능 저하를 초래하기 때문에 충분하지 않습니다. 본 논문은 궤적 최적화와 전신 제어로 구성된 제어 아키텍처를 제시하며, 이는 일치하는 모델 추상화에 의해 중재되어 관절 강체 모델의 축약되지 않은 운동 방정식에 기반한 제약 및 자세 동작을 포함한 곡예 동작의 실행을 가능하게 합니다. 기본 모델링 및 제어 방법에 대한 검토가 제공되며, 모델 추상화, 궤적 최적화 및 전신 제어기를 포함한 구현 세부 사항이 이어집니다. 시스템의 효과는 시뮬레이션에서 분석됩니다.

## 핵심 내용
휴머노이드 로봇이 인간 수준의 곡예와 같은 고도로 역동적인 동작을 수행할 수 있는 능력을 부여하는 것은 오랜 도전 과제였습니다. 이러한 동작을 성공적으로 수행하려면 계획을 위한 궤적 최적화와 실행 중 제어 모두에서 기본 물리 법칙을 면밀히 고려해야 합니다. 이는 휴머노이드의 높은 자유도와 그에 따른 기하급수적으로 증가하는 복잡성으로 인해 특히 어려우며, 명시적 운동 방정식에 대한 계획을 다루기 어렵게 만듭니다. 일반적인 해결 방법으로는 선형화 방법과 모델 근사가 있습니다. 그러나 둘 다 실제 로봇 시스템에서 성능 저하를 초래하기 때문에 충분하지 않습니다. 본 논문은 궤적 최적화와 전신 제어로 구성된 제어 아키텍처를 제시하며, 이는 일치하는 모델 추상화에 의해 중재되어 관절 강체 모델의 축약되지 않은 운동 방정식에 기반한 제약 및 자세 동작을 포함한 곡예 동작의 실행을 가능하게 합니다. 기본 모델링 및 제어 방법에 대한 검토가 제공되며, 모델 추상화, 궤적 최적화 및 전신 제어기를 포함한 구현 세부 사항이 이어집니다. 시스템의 효과는 시뮬레이션에서 분석됩니다.

## 参考
- http://arxiv.org/abs/2508.08258v1
