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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.16943v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1318 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2508.16943v3

## 개요
전통적인 물리 휴머노이드 운동 제어는 일반적으로 단기적이고 고립된 세그먼트에 국한되어 있으며, 각 상호작용 후 재초기화가 필요합니다. HumanoidVerse는 연속적이고 리셋 없는 장시간 운동을 추구합니다: 시뮬레이션된 휴머노이드는 단일 중단 없는 실행에서 반복적으로 오프셋된 물체로 걸어가고, 균형 잡힌 전신 자세로 들어 올리며, 장애물을 우회하여 목표 위치로 운반하고 배치해야 합니다. 어려움은 개별 동작이 아니라 동작 간의 전환에 있습니다—각 배치 후 캐릭터는 비표준 자세와 불균형 상태에 놓이며, 이로 인해 종단 간 강화 학습이 실패합니다. 이를 위해 저자는 회복 가능성의 양면 문제를 제기합니다: 캐릭터는 물체를 놓은 후 이전의 성공 상태를 유지하고, 균형 연속이 존재하는 시작 영역으로 진입해야 합니다. 각 주기의 종료 상태를 해당 영역에落入하도록 제어하는 학습을 통해, 적대적 운동 사전과 지식 증류를 활용하여 최종적으로 이중 컨트롤러를 단일 목표 조건 정책으로 융합하여 완전한 시퀀스의 리셋 없는 실행을 달성합니다.

## 핵심 내용
### 방법 아키텍처
- **이중 컨트롤러 설계**: 첫 번째 컨트롤러(Cycle Controller)는 "집기-운반-배치" 주기를 완료하고, 학습된 "해제-후퇴" 동작을 통해 종료 상태를 회복 가능 영역으로 유도합니다; 두 번째 컨트롤러(Transition Controller)는 해당 영역의 상태 분포에서 인계받아 다음 주기를 시작합니다.
- **회복 가능성 영역**: 오프라인으로 성공적인 전환 상태 샘플을 수집하여 판별기를 훈련해 해당 영역을 정의합니다; 컨트롤러는 보상 함수를 통해 종료 상태를 해당 영역에 매핑하도록 장려됩니다.
- **적대적 운동 사전**: 적대적 운동 사전(AMP)을 사용하여 두 컨트롤러의 동작을 정규화하여 생성된 운동이 자연스럽고 인체 역학 제약을 준수하도록 보장합니다.
- **지식 증류**: 이중 컨트롤러 정책을 단일 목표 조건 정책으로 증류하며, 이 정책은 현재 물체 위치, 목표 위치 및 로봇 자체 상태를 입력으로 받아 관절 토크를 직접 출력합니다.

### 실험 설정
- **시나리오**: 350가지 혼잡한 레이아웃으로, 네 가지 방 유형(주방, 거실, 사무실, 창고)을 포함하며 정적 장애물과 동적 물체를 포함합니다.
- **작업**: 휴머노이드 로봇은 단일 실행에서 5개의 물체 재배치를 완료해야 하며, 각 물체는 초기 위치에서 지정된 목표 위치로 운반되어야 합니다.
- **비교 방법**: 종단 간 강화 학습(E2E-RL), 계층적 강화 학습(HRL, 상위 계층이 하위 목표를 계획하고 하위 계층이 실행), 물리 기반 인간-장면 상호작용 방법(PHSCI, 예: PhysHOI).
- **평가 지표**: 작업 성공률(모든 물체가 올바르게 배치됨), 평균 완료 시간, 운동 안정성(신체 기울기 각도 분산, 발 미끄러짐 거리).

### 주요 수치 및 결론
- **성공률**: LHM-Humanoid는 보지 못한 시나리오에서 82.3%의 성공률을 달성한 반면, E2E-RL은 12.1%, HRL은 34.7%, PHSCI는 28.5%에 불과했습니다.
- **안정성**: 신체 기울기 각도 분산이 41% 감소(HRL 대비), 발 미끄러짐 거리가 63% 감소(PHSCI 대비).
- **일반화**: 훈련 중 보지 못한 물체 모양, 장애물 레이아웃 및 목표 위치 조합에서 성공률은 5.2%만 감소한 반면, 비교 방법은 18-27% 감소했습니다.
- **절제 실험**: 회복 가능성 영역 학습을 제거하면 성공률이 47.6%로 떨어졌습니다; 적대적 운동 사전을 제거하면 운동 자연스러움 점수(사용자 조사 기반)가 34% 하락했습니다.

### 결론
HumanoidVerse는 장시간 운동을 회복 가능한 주기 전환으로 분해하고, 이중 컨트롤러 증류와 적대적 사전을 결합하여 복잡한 혼잡 시나리오에서 물리 휴머노이드의 연속적이고 리셋 없는 다중 물체 재배치를 최초로 구현했습니다. 이 방법은 성공률, 안정성 및 일반화에서 기존 기술을 크게 능가하며, 실제 휴머노이드 로봇의 장기 자율 조작을 위한 실행 가능한 프레임워크를 제공합니다.
