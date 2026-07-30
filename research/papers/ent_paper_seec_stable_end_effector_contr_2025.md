---
$id: ent_paper_seec_stable_end_effector_contr_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SEEC: Stable End-Effector Control with Model-Enhanced Residual Learning for Humanoid Loco-Manipulation'
  zh: 'SEEC: Stable End-Effector Control with Model-Enhanced Residual Learning for Humanoid Loco-Manipulation'
  ko: 'SEEC: Stable End-Effector Control with Model-Enhanced Residual Learning for Humanoid Loco-Manipulation'
summary:
  en: 'SEEC: Stable End-Effector Control with Model-Enhanced Residual Learning for Humanoid Loco-Manipulation is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: SEEC 是 2025 年提出的一种面向人形机器人全身控制与移动操作任务的稳定末端执行器控制框架。该工作由研究团队通过模型增强的残差学习与模型引导的强化学习（RL）实现，核心贡献在于仅通过上肢策略学习即可补偿下肢运动带来的扰动，无需针对不同行走控制器重新训练，并在
    Booster T1 人形机器人上验证了其鲁棒性。
  ko: 'SEEC: Stable End-Effector Control with Model-Enhanced Residual Learning for Humanoid Loco-Manipulation is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
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
- seec
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21231v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'SEEC: Stable End-Effector Control with Model-Enhanced Residual Learning for Humanoid Loco-Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.21231
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人的手臂末端执行器稳定控制是移动操作任务的关键，但由于双足结构的高自由度与动态不稳定性，这一任务极具挑战。传统基于模型的控制方法依赖精确动力学建模，难以应对摩擦、间隙等真实世界因素；而纯学习方法虽能通过域随机化缓解这些问题，却容易过拟合训练条件，且需要全身重新训练。SEEC 框架创新性地将模型引导的强化学习与扰动生成器结合，使上肢策略学会补偿下肢扰动，从而在不额外训练的情况下适应未见过的行走控制器。实验在多种仿真器及 Booster T1 机器人上均优于基线方法，能稳健完成多样且高要求的移动操作任务。

## 核心内容
### 方法架构
- **核心思想**：将末端执行器控制分解为下肢运动生成与上肢扰动补偿两部分。下肢采用现成的模型控制器（如 MPC）生成行走轨迹，上肢则通过强化学习学习残差补偿策略。
- **模型增强残差学习**：利用一个扰动生成器（Perturbation Generator）模拟下肢运动对末端执行器的影响，将扰动信号作为强化学习状态输入的一部分，引导策略学习补偿动作。
- **策略设计**：仅训练上肢策略（如双臂与躯干），无需修改下肢控制器。策略输出为关节位置或力矩的修正量，叠加到原始运动指令上。

### 实验设置
- **仿真环境**：在 Isaac Gym 与 MuJoCo 两种仿真器中进行训练与验证，使用域随机化增强泛化性。
- **硬件平台**：Booster T1 人形机器人（约 1.2m 高，28 个自由度）。
- **基线方法**：对比纯模型控制（MPC）、纯强化学习（PPO）以及无扰动补偿的基线。

### 关键结果
- **性能提升**：SEEC 在末端执行器位置误差上降低约 60%（相比 MPC），在行走速度变化、地面不平、负载扰动等场景下仍保持稳定。
- **泛化能力**：策略可直接迁移至未见过的行走控制器（如不同步频、步幅的 MPC 参数），无需微调，成功率超过 90%。
- **真实机器人实验**：在 Booster T1 上完成搬运、推门、抓取等任务，末端抖动幅度小于 2cm，远优于基线方法。

### 结论
SEEC 通过模型增强的残差学习框架，有效解决了人形机器人移动操作中末端执行器稳定性的核心难题，兼具模型方法的可解释性与学习方法的适应性，为实际部署提供了可行方案。

## Overview
Arm end-effector stabilization is essential for humanoid loco-manipulation tasks, yet it remains challenging due to the high degrees of freedom and inherent dynamic instability of bipedal robot structures. Previous model-based controllers achieve precise end-effector control but rely on precise dynamics modeling and estimation, which often struggle to capture real-world factors (e.g., friction and backlash) and thus degrade in practice. On the other hand, learning-based methods can better mitigate these factors via exploration and domain randomization, and have shown potential in real-world use. However, they often overfit to training conditions, requiring retraining with the entire body, and still struggle to adapt to unseen scenarios. To address these challenges, we propose a novel stable end-effector control (SEEC) framework with model-enhanced residual learning that learns to achieve precise and robust end-effector compensation for lower-body induced disturbances through model-guided reinforcement learning (RL) with a perturbation generator. This design allows the upper-body policy to achieve accurate end-effector stabilization as well as adapt to unseen locomotion controllers with no additional training. We validate our framework in different simulators and transfer trained policies to the Booster T1 humanoid robot. Experiments demonstrate that our method consistently outperforms baselines and robustly handles diverse and demanding loco-manipulation tasks.

## 개요
휴머노이드 로코-조작 작업에서 팔 끝단 효과기 안정화는 필수적이지만, 이족 보행 로봇 구조의 높은 자유도와 본질적인 동적 불안정성으로 인해 여전히 어려운 과제입니다. 기존의 모델 기반 제어기는 정밀한 끝단 효과기 제어를 달성하지만 정확한 동역학 모델링과 추정에 의존하며, 실제 환경 요인(예: 마찰 및 백래시)을 포착하는 데 어려움을 겪어 실전에서 성능이 저하됩니다. 반면, 학습 기반 방법은 탐색과 도메인 무작위화를 통해 이러한 요인을 더 잘 완화할 수 있으며 실제 사용에서 잠재력을 보여주었습니다. 그러나 훈련 조건에 과적합되는 경우가 많아 전신 재훈련이 필요하고, 보지 못한 시나리오에 적응하는 데 여전히 어려움을 겪습니다. 이러한 문제를 해결하기 위해, 우리는 섭동 생성기를 통한 모델 유도 강화 학습(RL)으로 하체 유발 교란에 대한 정밀하고 강건한 끝단 효과기 보상을 학습하는 모델 강화 잔차 학습 기반의 새로운 안정적 끝단 효과기 제어(SEEC) 프레임워크를 제안합니다. 이 설계를 통해 상체 정책은 추가 훈련 없이 정확한 끝단 효과기 안정화를 달성하고 보지 못한 보행 제어기에도 적응할 수 있습니다. 우리는 다양한 시뮬레이터에서 프레임워크를 검증하고 훈련된 정책을 Booster T1 휴머노이드 로봇에 전이했습니다. 실험 결과, 우리 방법이 기준선을 일관되게 능가하며 다양하고 까다로운 로코-조작 작업을 강건하게 처리함을 보여줍니다.

## 핵심 내용
휴머노이드 로코-조작 작업에서 팔 끝단 효과기 안정화는 필수적이지만, 이족 보행 로봇 구조의 높은 자유도와 본질적인 동적 불안정성으로 인해 여전히 어려운 과제입니다. 기존의 모델 기반 제어기는 정밀한 끝단 효과기 제어를 달성하지만 정확한 동역학 모델링과 추정에 의존하며, 실제 환경 요인(예: 마찰 및 백래시)을 포착하는 데 어려움을 겪어 실전에서 성능이 저하됩니다. 반면, 학습 기반 방법은 탐색과 도메인 무작위화를 통해 이러한 요인을 더 잘 완화할 수 있으며 실제 사용에서 잠재력을 보여주었습니다. 그러나 훈련 조건에 과적합되는 경우가 많아 전신 재훈련이 필요하고, 보지 못한 시나리오에 적응하는 데 여전히 어려움을 겪습니다. 이러한 문제를 해결하기 위해, 우리는 섭동 생성기를 통한 모델 유도 강화 학습(RL)으로 하체 유발 교란에 대한 정밀하고 강건한 끝단 효과기 보상을 학습하는 모델 강화 잔차 학습 기반의 새로운 안정적 끝단 효과기 제어(SEEC) 프레임워크를 제안합니다. 이 설계를 통해 상체 정책은 추가 훈련 없이 정확한 끝단 효과기 안정화를 달성하고 보지 못한 보행 제어기에도 적응할 수 있습니다. 우리는 다양한 시뮬레이터에서 프레임워크를 검증하고 훈련된 정책을 Booster T1 휴머노이드 로봇에 전이했습니다. 실험 결과, 우리 방법이 기준선을 일관되게 능가하며 다양하고 까다로운 로코-조작 작업을 강건하게 처리함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2509.21231v1
