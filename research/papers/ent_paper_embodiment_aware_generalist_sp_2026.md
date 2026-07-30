---
$id: ent_paper_embodiment_aware_generalist_sp_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control
  zh: Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control
  ko: Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control
summary:
  en: Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: EAGLE 是一种迭代式通用专家蒸馏框架，用于生成统一的全身控制策略，可控制多种异构人形机器人（如 Unitree H1、G1、Fourier N1），无需针对每台机器人单独调整奖励函数。该工作由 2026 年研究团队提出，核心贡献在于通过通用-专家循环蒸馏实现跨本体迁移与丰富行为（如蹲、倾斜）的泛化能力。
  ko: Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embodiment_aware_generalist_sp
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.02960v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control (arXiv)
  url: https://arxiv.org/abs/2602.02960
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有基于强化学习的人形机器人全身控制器虽性能优异，但大多针对单一机器人本体设计，难以应对动力学、自由度与运动学拓扑的差异。EAGLE 通过迭代式通用-专家蒸馏框架解决此问题：在每个循环中，从当前通用策略分叉出本体专属专家策略，在对应机器人上微调，再将新技能蒸馏回通用策略。重复此过程至性能收敛，最终得到可在模拟（5 种机器人）与真实环境（4 种机器人）中验证的鲁棒全身控制器。实验表明，EAGLE 在跟踪精度与鲁棒性上优于其他方法，向可扩展的集群级人形控制迈出一步。

## 核心内容
### 方法架构
- **EAGLE 框架**：采用迭代式通用-专家蒸馏（Generalist-Specialist Distillation）。每轮循环中：
  1. **分叉专家**：从当前通用策略复制出多个本体专属专家策略。
  2. **专家微调**：每个专家在对应机器人上通过强化学习进行微调，学习特定本体的技能。
  3. **蒸馏回通用**：将所有专家策略的知识通过蒸馏训练回通用策略，训练数据来自所有本体的混合经验池。
- **循环终止条件**：重复上述步骤直至性能收敛，最终通用策略可同时控制多种异构人形机器人。

### 实验设置
- **机器人平台**：模拟环境测试 5 种机器人（包括 Unitree H1、G1、Fourier N1），真实环境测试 4 种机器人。
- **任务范围**：涵盖行走、蹲、倾斜等丰富行为，以及全身协调的移动-操作（loco-manipulation）任务。
- **对比方法**：与单本体专用策略及其他跨本体迁移方法进行定量比较。

### 关键结果
- **跟踪精度**：EAGLE 在多种机器人上均实现高跟踪精度，显著优于未使用蒸馏的基线方法。
- **鲁棒性**：面对动力学参数变化与外部扰动时，EAGLE 策略保持稳定控制。
- **泛化能力**：无需针对每台机器人调整奖励函数，即可直接部署到新本体上。
- **可扩展性**：框架支持逐步添加新机器人本体，无需重新训练整个策略。

### 结论
EAGLE 通过迭代蒸馏框架解决了人形机器人全身控制中的跨本体迁移难题，为未来集群级人形机器人控制提供了可扩展的解决方案。更多细节与演示见项目网站：https://eagle-wbc.github.io/

## Overview
Humanoid Whole-Body Controllers trained with reinforcement learning (RL) have recently achieved remarkable performance, yet many target a single robot embodiment. Variations in dynamics, degrees of freedom (DoFs), and kinematic topology still hinder a single policy from commanding diverse humanoids. Moreover, obtaining a generalist policy that not only transfers across embodiments but also supports richer behaviors-beyond simple walking to squatting, leaning-remains especially challenging. In this work, we tackle these obstacles by introducing EAGLE, an iterative generalist-specialist distillation framework that produces a single unified policy that controls multiple heterogeneous humanoids without per-robot reward tuning. During each cycle, embodiment-specific specialists are forked from the current generalist, refined on their respective robots, and new skills are distilled back into the generalist by training on the pooled embodiment set. Repeating this loop until performance convergence produces a robust Whole-Body Controller validated on robots such as Unitree H1, G1, and Fourier N1. We conducted experiments on five different robots in simulation and four in real-world settings. Through quantitative evaluations, EAGLE achieves high tracking accuracy and robustness compared to other methods, marking a step toward scalable, fleet-level humanoid control. See more details at https://eagle-wbc.github.io/

## Overview
Humanoid Whole-Body Controllers trained with reinforcement learning (RL) have recently achieved remarkable performance, yet many target a single robot embodiment. Variations in dynamics, degrees of freedom (DoFs), and kinematic topology still hinder a single policy from commanding diverse humanoids. Moreover, obtaining a generalist policy that not only transfers across embodiments but also supports richer behaviors—beyond simple walking to squatting, leaning—remains especially challenging. In this work, we tackle these obstacles by introducing EAGLE, an iterative generalist-specialist distillation framework that produces a single unified policy that controls multiple heterogeneous humanoids without per-robot reward tuning. During each cycle, embodiment-specific specialists are forked from the current generalist, refined on their respective robots, and new skills are distilled back into the generalist by training on the pooled embodiment set. Repeating this loop until performance convergence produces a robust Whole-Body Controller validated on robots such as Unitree H1, G1, and Fourier N1. We conducted experiments on five different robots in simulation and four in real-world settings. Through quantitative evaluations, EAGLE achieves high tracking accuracy and robustness compared to other methods, marking a step toward scalable, fleet-level humanoid control. See more details at https://eagle-wbc.github.io/

## Content
Humanoid Whole-Body Controllers trained with reinforcement learning (RL) have recently achieved remarkable performance, yet many target a single robot embodiment. Variations in dynamics, degrees of freedom (DoFs), and kinematic topology still hinder a single policy from commanding diverse humanoids. Moreover, obtaining a generalist policy that not only transfers across embodiments but also supports richer behaviors—beyond simple walking to squatting, leaning—remains especially challenging. In this work, we tackle these obstacles by introducing EAGLE, an iterative generalist-specialist distillation framework that produces a single unified policy that controls multiple heterogeneous humanoids without per-robot reward tuning. During each cycle, embodiment-specific specialists are forked from the current generalist, refined on their respective robots, and new skills are distilled back into the generalist by training on the pooled embodiment set. Repeating this loop until performance convergence produces a robust Whole-Body Controller validated on robots such as Unitree H1, G1, and Fourier N1. We conducted experiments on five different robots in simulation and four in real-world settings. Through quantitative evaluations, EAGLE achieves high tracking accuracy and robustness compared to other methods, marking a step toward scalable, fleet-level humanoid control. See more details at https://eagle-wbc.github.io/

## 개요
강화 학습(RL)으로 훈련된 휴머노이드 전신 제어기는 최근 놀라운 성능을 달성했지만, 대부분은 단일 로봇 형상을 대상으로 합니다. 동역학, 자유도(DoF) 및 운동학적 토폴로지의 차이로 인해 단일 정책이 다양한 휴머노이드를 제어하는 것은 여전히 어렵습니다. 또한, 다양한 형상 간 전이뿐만 아니라 단순한 보행을 넘어 쪼그려 앉기, 기울이기와 같은 더 풍부한 행동을 지원하는 범용 정책을 얻는 것은 특히 어려운 과제로 남아 있습니다. 본 연구에서는 이러한 장애물을 해결하기 위해 EAGLE을 도입합니다. EAGLE은 반복적인 범용-전문가 증류 프레임워크로, 로봇별 보상 조정 없이 여러 이종 휴머노이드를 제어하는 단일 통합 정책을 생성합니다. 각 주기에서 현재 범용 정책에서 형상별 전문가를 분기하여 각 로봇에 맞게 미세 조정하고, 새로운 기술을 통합 형상 집합에 대한 훈련을 통해 범용 정책으로 다시 증류합니다. 성능이 수렴할 때까지 이 루프를 반복하면 Unitree H1, G1, Fourier N1과 같은 로봇에서 검증된 강력한 전신 제어기가 생성됩니다. 우리는 시뮬레이션에서 5가지, 실제 환경에서 4가지의 서로 다른 로봇으로 실험을 수행했습니다. 정량적 평가를 통해 EAGLE은 다른 방법에 비해 높은 추적 정확도와 견고성을 달성하여 확장 가능한 함대 수준의 휴머노이드 제어를 위한 한 걸음을 내디뎠습니다. 자세한 내용은 https://eagle-wbc.github.io/에서 확인하세요.

## 핵심 내용
강화 학습(RL)으로 훈련된 휴머노이드 전신 제어기는 최근 놀라운 성능을 달성했지만, 대부분은 단일 로봇 형상을 대상으로 합니다. 동역학, 자유도(DoF) 및 운동학적 토폴로지의 차이로 인해 단일 정책이 다양한 휴머노이드를 제어하는 것은 여전히 어렵습니다. 또한, 다양한 형상 간 전이뿐만 아니라 단순한 보행을 넘어 쪼그려 앉기, 기울이기와 같은 더 풍부한 행동을 지원하는 범용 정책을 얻는 것은 특히 어려운 과제로 남아 있습니다. 본 연구에서는 이러한 장애물을 해결하기 위해 EAGLE을 도입합니다. EAGLE은 반복적인 범용-전문가 증류 프레임워크로, 로봇별 보상 조정 없이 여러 이종 휴머노이드를 제어하는 단일 통합 정책을 생성합니다. 각 주기에서 현재 범용 정책에서 형상별 전문가를 분기하여 각 로봇에 맞게 미세 조정하고, 새로운 기술을 통합 형상 집합에 대한 훈련을 통해 범용 정책으로 다시 증류합니다. 성능이 수렴할 때까지 이 루프를 반복하면 Unitree H1, G1, Fourier N1과 같은 로봇에서 검증된 강력한 전신 제어기가 생성됩니다. 우리는 시뮬레이션에서 5가지, 실제 환경에서 4가지의 서로 다른 로봇으로 실험을 수행했습니다. 정량적 평가를 통해 EAGLE은 다른 방법에 비해 높은 추적 정확도와 견고성을 달성하여 확장 가능한 함대 수준의 휴머노이드 제어를 위한 한 걸음을 내디뎠습니다. 자세한 내용은 https://eagle-wbc.github.io/에서 확인하세요.

## 参考
- http://arxiv.org/abs/2602.02960v2
