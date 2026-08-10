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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10206v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (711 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2510.10206v1

## 개요
Harmanoid 프레임워크는 두 휴머노이드 로봇 간의 물리적 상호작용 시나리오에 특화되어 설계되었으며, 기존 단일 로봇 자율성 연구의 한계를突破了. 이 프레임워크는 두 가지 핵심 모듈을 포함합니다: 접촉 인식 운동 리타게팅 모듈은 SMPL 인체 모델의 접촉점을 로봇 정점에 매핑하여 두 몸체 간의 조화로운 운동을 복원하고, 상호작용 구동 운동 컨트롤러는 상호작용 특정 보상 함수를 활용하여 핵심 지점의 협력과 물리적으로 합리적인 접촉을 강제합니다. 실험 결과, Harmanoid는 상호작용 운동 모방 작업에서 기존 단일 로봇 프레임워크보다 현저히 우수하며, 후자는 이중 몸체 상호작용 시나리오에서 거의 완전히 실패합니다.

## 핵심 내용
### 방법 아키텍처
Harmanoid 프레임워크는 두 가지 핵심 구성 요소로 이루어져 있습니다:
- **접촉 인식 운동 리타게팅**: SMPL 인체 모델의 접촉점과 로봇 정점 간의 매핑 관계를 구축하여 두 로봇 간의 사지 협력 운동을 복원하고, 접촉 오정렬 및 관통 문제를 방지합니다.
- **상호작용 구동 운동 컨트롤러**: 상호작용 특정 보상 함수를 설계하여 두 로봇의 핵심 지점 협력 운동과 물리적으로 합리적인 접촉 행동을 강제하며, 운동학적 충실도와 물리적 현실성을 보장합니다.

### 실험 설정
- 이중 휴머노이드 로봇 플랫폼을 사용하여 상호작용 운동 모방 실험을 수행
- 비교 기준은 기존 단일 로봇 전신 제어 프레임워크
- 평가 지표는 운동학적 충실도(핵심 지점 오차)와 물리적 합리성(접촉 관통률)을 포함

### 핵심 결과
- Harmanoid는 상호작용 운동 모방 작업에서 모든 단일 로봇 기준 방법을 현저히 능가
- 단일 로봇 프레임워크는 이중 몸체 상호작용 시나리오에서 거의 완전히 실패하며, 접촉 오정렬, 관통 및 부자연스러운 운동으로 나타남
- 이중 몸체 접촉과 상호작용 인식 동역학을 명시적으로 모델링함으로써, Harmanoid는 단일 로봇 프레임워크가 처리할 수 없는 결합 행동을 성공적으로 포착

### 결론
Harmanoid는 이중 로봇 간의 접촉과 상호작용 동역학을 명시적으로 모델링하는 것이 물리적으로 합리적인 휴머노이드 로봇 상호작용을 구현하는 데 필수적임을 증명하며, 향후 다중 로봇 협력 작업(예: 운반, 조립)을 위한 기반 프레임워크를 제공합니다.
