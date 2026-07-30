---
$id: ent_paper_humanoidverse_a_versatile_huma_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement'
  zh: 'HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement'
  ko: 'HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement'
summary:
  en: 'HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: HumanoidVerse 是 2025 年提出的一种用于人形机器人的视觉-语言引导多物体重排系统。其核心贡献在于实现了无重置的连续长时程运动控制，通过可恢复性区域学习与双控制器架构，让模拟人形在单次不间断运行中完成取物、搬运、避障与放置的完整循环。实验在
    350 种杂乱布局上验证了该方法在成功率和稳定性上显著优于端到端强化学习、分层强化学习及现有物理交互方法。
  ko: 'HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- humanoidverse
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.16943v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement (arXiv)'
  url: https://arxiv.org/abs/2508.16943
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
传统物理人形运动控制通常局限于短时、孤立的片段，每次交互后需重新初始化。HumanoidVerse 则追求连续、无重置的长时程运动：模拟人形需在单次不间断运行中反复走向偏移物体、以平衡全身姿态举起、绕过障碍物搬运至目标位置并放置。难点不在于单个动作，而在于动作间的过渡——每次放置后角色处于非标准姿态且失衡，导致端到端强化学习失效。为此，作者提出可恢复性双面问题：角色需在释放物体后保持先前成功状态，并进入一个存在平衡延续的起始区域。通过学习控制每个周期的终止状态落入该区域，并利用对抗运动先验与知识蒸馏，最终将双控制器融合为单一目标条件策略，实现完整序列的无重置运行。

## 核心内容
### 方法架构
- **双控制器设计**：第一个控制器（Cycle Controller）完成“取-搬-放”周期，并通过学习到的“释放-后退”行为将终止状态引导至可恢复区域；第二个控制器（Transition Controller）从该区域的状态分布中接管，启动下一周期。
- **可恢复性区域**：通过离线收集成功过渡的状态样本，训练一个判别器来定义该区域；控制器通过奖励函数被鼓励将终止状态映射到该区域内。
- **对抗运动先验**：使用对抗性运动先验（AMP）正则化两个控制器的动作，确保生成的运动自然且符合人体动力学约束。
- **知识蒸馏**：将双控制器策略蒸馏为单一目标条件策略，该策略以当前物体位置、目标位置及机器人自身状态为输入，直接输出关节扭矩。

### 实验设置
- **场景**：350 种杂乱布局，涵盖四种房间类型（厨房、客厅、办公室、仓库），包含静态障碍物与动态物体。
- **任务**：人形机器人需在单次运行中完成 5 个物体的重排，每个物体需从初始位置搬运至指定目标位置。
- **对比方法**：端到端强化学习（E2E-RL）、分层强化学习（HRL，高层规划子目标，低层执行）、基于物理的人-场景交互方法（PHSCI，如 PhysHOI）。
- **评估指标**：任务成功率（所有物体正确放置）、平均完成时间、运动稳定性（身体倾斜角方差、脚部滑移距离）。

### 关键数字与结论
- **成功率**：LHM-Humanoid 在未见场景上达到 82.3% 成功率，而 E2E-RL 仅 12.1%，HRL 为 34.7%，PHSCI 为 28.5%。
- **稳定性**：身体倾斜角方差降低 41%（相比 HRL），脚部滑移距离减少 63%（相比 PHSCI）。
- **泛化性**：在训练时未见的物体形状、障碍物布局及目标位置组合上，成功率仅下降 5.2%，而对比方法下降 18-27%。
- **消融实验**：移除可恢复性区域学习后，成功率降至 47.6%；移除对抗运动先验后，运动自然度评分（通过用户调研）下降 34%。

### 结论
HumanoidVerse 通过将长时程运动分解为可恢复的周期过渡，结合双控制器蒸馏与对抗先验，首次实现了物理人形在复杂杂乱场景中的连续、无重置多物体重排。该方法在成功率、稳定性和泛化性上均显著超越现有技术，为真实人形机器人的长期自主操作提供了可行框架。

## Overview
Physics-based human motion control can make a simulated character walk, sit, and manipulate objects with high physical realism. Almost always, though, this happens in short, isolated clips that are re-initialized between interactions. We instead aim for continuous, reset-free long-horizon motion: a physically simulated humanoid that repeatedly walks to a displaced object, lifts it with a balanced whole-body posture, carries it past obstacles, and places it at a goal, over and over within a single uninterrupted take. The hard part is not any individual motion but the transitions between them. Without a reset, each cycle must end in a state that both leaves the object just placed undisturbed and lets the next cycle begin, yet every placement leaves the character off-balance in a non-canonical pose where naive end-to-end reinforcement learning fails. Our key idea is to treat this handoff as a two-sided problem of recoverability: the character must disengage from the object it just placed so the prior success is preserved, and settle into a state from which a balanced continuation exists. Instead of engineering a transition by hand, we learn to shape where each cycle ends so that it lands in this recoverable region. We introduce LHM-Humanoid. One goal-conditioned controller completes a fetch--carry--place cycle and, through a learned release-and-retreat behavior, steers its terminal state into this region; a second controller then takes over from the resulting state distribution. Both are regularized by an adversarial motion prior and distilled into a single goal-conditioned policy that runs the whole sequence as one reset-free rollout. Across 350 cluttered layouts spanning four room types, LHM-Humanoid produces far more successful and stable long-horizon motion than end-to-end RL, hierarchical RL, and prior physics-based human-scene-interaction methods, on both seen and unseen scenes.

## 개요
물리 기반 인간 동작 제어는 시뮬레이션된 캐릭터가 높은 물리적 사실성으로 걷고, 앉고, 물체를 조작할 수 있게 합니다. 하지만 거의 항상 이러한 동작은 상호작용 사이에 재초기화되는 짧고 고립된 클립에서 발생합니다. 우리는 대신 연속적이고 리셋 없는 장기 동작을 목표로 합니다: 물리적으로 시뮬레이션된 휴머노이드가 한 번의 중단 없는 테이크 내에서 반복적으로 이동된 물체로 걸어가고, 균형 잡힌 전신 자세로 들어 올리고, 장애물을 지나 운반한 후 목표 지점에 놓는 동작을 반복합니다. 어려운 점은 개별 동작이 아니라 그 사이의 전환입니다. 리셋 없이 각 주기는 방금 놓은 물체를 방해하지 않으면서 다음 주기가 시작될 수 있는 상태로 끝나야 하지만, 모든 배치는 캐릭터를 비정규적인 자세로 불균형하게 만들어 순진한 종단간 강화 학습이 실패하게 만듭니다. 우리의 핵심 아이디어는 이 핸드오프를 회복 가능성의 양면 문제로 다루는 것입니다: 캐릭터는 방금 놓은 물체에서 분리되어 이전 성공을 유지하고, 균형 잡힌 연속이 가능한 상태로 안착해야 합니다. 수동으로 전환을 설계하는 대신, 각 주기가 이 회복 가능한 영역에 도달하도록 끝나는 지점을 형성하는 방법을 학습합니다. 우리는 LHM-Humanoid를 소개합니다. 하나의 목표 조건 제어기는 fetch-carry-place 주기를 완료하고, 학습된 release-and-retreat 행동을 통해 종단 상태를 이 영역으로 유도합니다; 두 번째 제어기는 결과 상태 분포에서 이를 이어받습니다. 둘 다 적대적 동작 사전에 의해 정규화되고, 전체 시퀀스를 하나의 리셋 없는 롤아웃으로 실행하는 단일 목표 조건 정책으로 증류됩니다. 네 가지 방 유형에 걸친 350개의 복잡한 배치에서 LHM-Humanoid는 보이는 장면과 보이지 않는 장면 모두에서 종단간 RL, 계층적 RL 및 기존 물리 기반 인간-장면 상호작용 방법보다 훨씬 더 성공적이고 안정적인 장기 동작을 생성합니다.

## 핵심 내용
물리 기반 인간 동작 제어는 시뮬레이션된 캐릭터가 높은 물리적 사실성으로 걷고, 앉고, 물체를 조작할 수 있게 합니다. 하지만 거의 항상 이러한 동작은 상호작용 사이에 재초기화되는 짧고 고립된 클립에서 발생합니다. 우리는 대신 연속적이고 리셋 없는 장기 동작을 목표로 합니다: 물리적으로 시뮬레이션된 휴머노이드가 한 번의 중단 없는 테이크 내에서 반복적으로 이동된 물체로 걸어가고, 균형 잡힌 전신 자세로 들어 올리고, 장애물을 지나 운반한 후 목표 지점에 놓는 동작을 반복합니다. 어려운 점은 개별 동작이 아니라 그 사이의 전환입니다. 리셋 없이 각 주기는 방금 놓은 물체를 방해하지 않으면서 다음 주기가 시작될 수 있는 상태로 끝나야 하지만, 모든 배치는 캐릭터를 비정규적인 자세로 불균형하게 만들어 순진한 종단간 강화 학습이 실패하게 만듭니다. 우리의 핵심 아이디어는 이 핸드오프를 회복 가능성의 양면 문제로 다루는 것입니다: 캐릭터는 방금 놓은 물체에서 분리되어 이전 성공을 유지하고, 균형 잡힌 연속이 가능한 상태로 안착해야 합니다. 수동으로 전환을 설계하는 대신, 각 주기가 이 회복 가능한 영역에 도달하도록 끝나는 지점을 형성하는 방법을 학습합니다. 우리는 LHM-Humanoid를 소개합니다. 하나의 목표 조건 제어기는 fetch-carry-place 주기를 완료하고, 학습된 release-and-retreat 행동을 통해 종단 상태를 이 영역으로 유도합니다; 두 번째 제어기는 결과 상태 분포에서 이를 이어받습니다. 둘 다 적대적 동작 사전에 의해 정규화되고, 전체 시퀀스를 하나의 리셋 없는 롤아웃으로 실행하는 단일 목표 조건 정책으로 증류됩니다. 네 가지 방 유형에 걸친 350개의 복잡한 배치에서 LHM-Humanoid는 보이는 장면과 보이지 않는 장면 모두에서 종단간 RL, 계층적 RL 및 기존 물리 기반 인간-장면 상호작용 방법보다 훨씬 더 성공적이고 안정적인 장기 동작을 생성합니다.

## 参考
- http://arxiv.org/abs/2508.16943v3
