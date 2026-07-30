---
$id: ent_paper_it_takes_two_learning_interact_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots'
  zh: 'It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots'
  ko: 'It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots'
summary:
  en: 'It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.'
  zh: Harmanoid 是一个面向双人形机器人的全身交互运动模仿框架，由研究团队于2025年提出。其核心贡献在于通过接触感知运动重定向与交互驱动运动控制器，解决了单机器人框架忽略双体动力学导致的接触错位与运动不真实问题。
  ko: 'It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.'
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
- it_takes_two
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10206v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2510.10206
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Harmanoid 框架专门针对双人形机器人间的物理交互场景设计，突破了传统单机器人自主性研究的局限。该框架包含两个关键模块：接触感知运动重定向模块通过将 SMPL 人体模型的接触点映射到机器人顶点，恢复双体间的协调运动；交互驱动运动控制器则利用交互特定奖励函数，强制实现关键点协同与物理合理的接触。实验表明，Harmanoid 在交互运动模仿任务中显著优于现有单机器人框架，后者在双体交互场景中几乎完全失效。

## 核心内容
### 方法架构
Harmanoid 框架由两个核心组件构成：
- **接触感知运动重定向**：通过建立 SMPL 人体模型接触点与机器人顶点之间的映射关系，恢复双机器人间的肢体协调运动，避免接触错位与穿透问题。
- **交互驱动运动控制器**：设计交互特定奖励函数，强制实现双机器人关键点的协同运动与物理合理的接触行为，确保运动学保真度与物理真实性。

### 实验设置
- 采用双人形机器人平台进行交互运动模仿实验
- 对比基线为现有单机器人全身控制框架
- 评估指标包括运动学保真度（关键点误差）与物理合理性（接触穿透率）

### 关键结果
- Harmanoid 在交互运动模仿任务中显著超越所有单机器人基线方法
- 单机器人框架在双体交互场景中几乎完全失效，表现为接触错位、穿透与不自然运动
- 通过显式建模双体接触与交互感知动力学，Harmanoid 成功捕捉了单机器人框架无法处理的耦合行为

### 结论
Harmanoid 证明了显式建模双机器人间接触与交互动力学对于实现物理合理的人形机器人交互至关重要，为未来多机器人协作任务（如搬运、装配）提供了基础框架。

## Overview
The true promise of humanoid robotics lies beyond single-agent autonomy: two or more humanoids must engage in physically grounded, socially meaningful whole-body interactions that echo the richness of human social interaction. However, single-humanoid methods suffer from the isolation issue, ignoring inter-agent dynamics and causing misaligned contacts, interpenetrations, and unrealistic motions. To address this, we present Harmanoid , a dual-humanoid motion imitation framework that transfers interacting human motions to two robots while preserving both kinematic fidelity and physical realism. Harmanoid comprises two key components: (i) contact-aware motion retargeting, which restores inter-body coordination by aligning SMPL contacts with robot vertices, and (ii) interaction-driven motion controller, which leverages interaction-specific rewards to enforce coordinated keypoints and physically plausible contacts. By explicitly modeling inter-agent contacts and interaction-aware dynamics, Harmanoid captures the coupled behaviors between humanoids that single-humanoid frameworks inherently overlook. Experiments demonstrate that Harmanoid significantly improves interactive motion imitation, surpassing existing single-humanoid frameworks that largely fail in such scenarios.

## Overview
The true promise of humanoid robotics lies beyond single-agent autonomy: two or more humanoids must engage in physically grounded, socially meaningful whole-body interactions that echo the richness of human social interaction. However, single-humanoid methods suffer from the isolation issue, ignoring inter-agent dynamics and causing misaligned contacts, interpenetrations, and unrealistic motions. To address this, we present Harmanoid, a dual-humanoid motion imitation framework that transfers interacting human motions to two robots while preserving both kinematic fidelity and physical realism. Harmanoid comprises two key components: (i) contact-aware motion retargeting, which restores inter-body coordination by aligning SMPL contacts with robot vertices, and (ii) interaction-driven motion controller, which leverages interaction-specific rewards to enforce coordinated keypoints and physically plausible contacts. By explicitly modeling inter-agent contacts and interaction-aware dynamics, Harmanoid captures the coupled behaviors between humanoids that single-humanoid frameworks inherently overlook. Experiments demonstrate that Harmanoid significantly improves interactive motion imitation, surpassing existing single-humanoid frameworks that largely fail in such scenarios.

## Content
The true promise of humanoid robotics lies beyond single-agent autonomy: two or more humanoids must engage in physically grounded, socially meaningful whole-body interactions that echo the richness of human social interaction. However, single-humanoid methods suffer from the isolation issue, ignoring inter-agent dynamics and causing misaligned contacts, interpenetrations, and unrealistic motions. To address this, we present Harmanoid, a dual-humanoid motion imitation framework that transfers interacting human motions to two robots while preserving both kinematic fidelity and physical realism. Harmanoid comprises two key components: (i) contact-aware motion retargeting, which restores inter-body coordination by aligning SMPL contacts with robot vertices, and (ii) interaction-driven motion controller, which leverages interaction-specific rewards to enforce coordinated keypoints and physically plausible contacts. By explicitly modeling inter-agent contacts and interaction-aware dynamics, Harmanoid captures the coupled behaviors between humanoids that single-humanoid frameworks inherently overlook. Experiments demonstrate that Harmanoid significantly improves interactive motion imitation, surpassing existing single-humanoid frameworks that largely fail in such scenarios.

## 개요
휴머노이드 로봇공학의 진정한 약속은 단일 에이전트 자율성을 넘어서는 데 있습니다. 두 대 이상의 휴머노이드가 물리적으로 기반을 둔, 사회적으로 의미 있는 전신 상호작용을 수행해야 하며, 이는 인간 사회적 상호작용의 풍부함을 반영해야 합니다. 그러나 단일 휴머노이드 방법은 고립 문제로 인해 에이전트 간 동역학을 무시하고, 정렬되지 않은 접촉, 상호 침투, 비현실적인 움직임을 초래합니다. 이를 해결하기 위해, 우리는 Harmanoid를 제안합니다. 이는 상호작용하는 인간의 움직임을 두 대의 로봇으로 전이하면서 운동학적 충실도와 물리적 현실성을 모두 보존하는 이중 휴머노이드 모션 모방 프레임워크입니다. Harmanoid는 두 가지 핵심 구성 요소로 이루어져 있습니다: (i) 접촉 인식 모션 리타겟팅으로, SMPL 접촉을 로봇 정점과 정렬하여 신체 간 조정을 복원하며, (ii) 상호작용 기반 모션 컨트롤러로, 상호작용 특화 보상을 활용하여 조정된 키포인트와 물리적으로 타당한 접촉을 강제합니다. 에이전트 간 접촉과 상호작용 인식 동역학을 명시적으로 모델링함으로써, Harmanoid는 단일 휴머노이드 프레임워크가 본질적으로 간과하는 휴머노이드 간 결합 행동을 포착합니다. 실험 결과, Harmanoid는 상호작용 모션 모방을 크게 개선하며, 이러한 시나리오에서 대부분 실패하는 기존 단일 휴머노이드 프레임워크를 능가합니다.

## 핵심 내용
휴머노이드 로봇공학의 진정한 약속은 단일 에이전트 자율성을 넘어서는 데 있습니다. 두 대 이상의 휴머노이드가 물리적으로 기반을 둔, 사회적으로 의미 있는 전신 상호작용을 수행해야 하며, 이는 인간 사회적 상호작용의 풍부함을 반영해야 합니다. 그러나 단일 휴머노이드 방법은 고립 문제로 인해 에이전트 간 동역학을 무시하고, 정렬되지 않은 접촉, 상호 침투, 비현실적인 움직임을 초래합니다. 이를 해결하기 위해, 우리는 Harmanoid를 제안합니다. 이는 상호작용하는 인간의 움직임을 두 대의 로봇으로 전이하면서 운동학적 충실도와 물리적 현실성을 모두 보존하는 이중 휴머노이드 모션 모방 프레임워크입니다. Harmanoid는 두 가지 핵심 구성 요소로 이루어져 있습니다: (i) 접촉 인식 모션 리타겟팅으로, SMPL 접촉을 로봇 정점과 정렬하여 신체 간 조정을 복원하며, (ii) 상호작용 기반 모션 컨트롤러로, 상호작용 특화 보상을 활용하여 조정된 키포인트와 물리적으로 타당한 접촉을 강제합니다. 에이전트 간 접촉과 상호작용 인식 동역학을 명시적으로 모델링함으로써, Harmanoid는 단일 휴머노이드 프레임워크가 본질적으로 간과하는 휴머노이드 간 결합 행동을 포착합니다. 실험 결과, Harmanoid는 상호작용 모션 모방을 크게 개선하며, 이러한 시나리오에서 대부분 실패하는 기존 단일 휴머노이드 프레임워크를 능가합니다.

## 参考
- http://arxiv.org/abs/2510.10206v1
