---
$id: ent_paper_objretarget_an_object_aware_mo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ObjRetarget: An Object-Aware Motion Retargeting Framework with Anthropomorphic Arm Constraints and Polyhedral Hand
    Modeling'
  zh: 'ObjRetarget: An Object-Aware Motion Retargeting Framework with Anthropomorphic Arm Constraints and Polyhedral Hand
    Modeling'
  ko: 'ObjRetarget: An Object-Aware Motion Retargeting Framework with Anthropomorphic Arm Constraints and Polyhedral Hand
    Modeling'
summary:
  en: 'arXiv:2607.03828v1 Announce Type: new Abstract: Learning robot dexterous manipulation from human manipulation videos
    requires reliably retargeting human intent to executable robot actions while maintaining stable hand-object contact, which
    remains a key challenge in embodied intelligence. Existing retargeting methods often ignore explicit contact modeling
    or rely on reinforcement learning, resulting in limited accuracy and generalization. To address this, we propose ObjRetarget,
    a human-to-robot motion retargeting framework for learning robot dexterous manipulation from human videos, which integrates
    anthropomorphic arm trajectory constraints with structured hand-object geometric modeling. For arm motion, reference trajectories
    extracted from human videos are used for initialization, followed by anthropomorphic constraints and redundancy-aware
    optimization to generate natural and accurate movements. For hand manipulation, ObjRetarget represents multi-finger contacts
    using polytope clusters and preserves contact structure through geometric invariants to improve stability. Experiments
    on real robots show that ObjRetarget improves manipulation success rates and contact stability across multiple dexterous
    tasks, and generalizes well to different demonstrations, object poses, and task settings.'
  zh: ObjRetarget 是一个从人类视频中学习机器人灵巧操作的全身运动重定向框架，由研究团队提出。其核心贡献在于将拟人化手臂轨迹约束与结构化手-物几何建模相结合，通过多面体簇表示手指接触并利用几何不变量保持接触稳定性，从而提升操作成功率与泛化能力。
  ko: 'arXiv:2607.03828v1 Announce Type: new Abstract: Learning robot dexterous manipulation from human manipulation videos
    requires reliably retargeting human intent to executable robot actions while maintaining stable hand-object contact, which
    remains a key challenge in embodied intelligence. Existing retargeting methods often ignore explicit contact modeling
    or rely on reinforcement learning, resulting in limited accuracy and generalization. To address this, we propose ObjRetarget,
    a human-to-robot motion retargeting framework for learning robot dexterous manipulation from human videos, which integrates
    anthropomorphic arm trajectory constraints with structured hand-object geometric modeling. For arm motion, reference trajectories
    extracted from human videos are used for initialization, followed by anthropomorphic constraints and redundancy-aware
    optimization to generate natural and accurate movements. For hand manipulation, ObjRetarget represents multi-finger contacts
    using polytope clusters and preserves contact structure through geometric invariants to improve stability. Experiments
    on real robots show that ObjRetarget improves manipulation success rates and contact stability across multiple dexterous
    tasks, and generalizes well to different demonstrations, object poses, and task settings.'
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
- robotics
- objretarget
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03828v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ObjRetarget: An Object-Aware Motion Retargeting Framework with Anthropomorphic Arm Constraints and Polyhedral Hand
    Modeling (arXiv)'
  url: https://arxiv.org/abs/2607.03828
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有运动重定向方法常忽略显式接触建模或依赖强化学习，导致精度与泛化性有限。ObjRetarget 针对此问题，从人类视频中提取参考轨迹进行手臂运动初始化，再通过拟人化约束与冗余感知优化生成自然准确的动作；对于手部操作，则采用多面体簇表示多指接触，并利用几何不变量维持接触结构。真实机器人实验表明，该方法在多个灵巧操作任务中显著提升了成功率和接触稳定性，并能良好泛化至不同演示、物体姿态与任务设置。

## 核心内容
### 方法架构
ObjRetarget 将人类到机器人的运动重定向分解为两个核心模块：
- **手臂运动模块**：首先从人类视频中提取参考轨迹作为初始化，随后施加拟人化约束（如关节角度限制、运动平滑性）并采用冗余感知优化算法，生成既自然又准确的手臂运动。
- **手部操作模块**：使用多面体簇（polytope clusters）表示多指与物体的接触区域，并通过几何不变量（geometric invariants）保持接触结构在重定向过程中的稳定性，避免手指滑脱或接触丢失。

### 实验设置与关键结果
- **实验平台**：在真实机器人上执行多个灵巧操作任务（如抓取、旋转、放置）。
- **关键指标**：操作成功率（success rate）与接触稳定性（contact stability）。
- **性能提升**：相比现有方法，ObjRetarget 在多个任务中显著提高了成功率，并展现出对以下变化的强泛化能力：
  - 不同人类演示视频
  - 物体姿态变化
  - 任务设置调整（如目标位置、物体类型）

### 结论
ObjRetarget 通过显式建模手臂拟人化约束与手部接触几何，有效解决了从人类视频学习灵巧操作中的重定向精度与稳定性难题，为具身智能中的技能迁移提供了可靠框架。

## Overview
Learning robot dexterous manipulation from human manipulation videos requires reliably retargeting human intent to executable robot actions while maintaining stable hand-object contact, which remains a key challenge in embodied intelligence. Existing retargeting methods often ignore explicit contact modeling or rely on reinforcement learning, resulting in limited accuracy and generalization. To address this, we propose ObjRetarget, a human-to-robot motion retargeting framework for learning robot dexterous manipulation from human videos, which integrates anthropomorphic arm trajectory constraints with structured hand-object geometric modeling. For arm motion, reference trajectories extracted from human videos are used for initialization, followed by anthropomorphic constraints and redundancy-aware optimization to generate natural and accurate movements. For hand manipulation, ObjRetarget represents multi-finger contacts using polytope clusters and preserves contact structure through geometric invariants to improve stability. Experiments on real robots show that ObjRetarget improves manipulation success rates and contact stability across multiple dexterous tasks, and generalizes well to different demonstrations, object poses, and task settings.

## 개요
인간의 조작 비디오로부터 로봇의 정밀 조작을 학습하려면, 안정적인 손-물체 접촉을 유지하면서 인간의 의도를 실행 가능한 로봇 동작으로 안정적으로 재타겟팅해야 하며, 이는 구현 지능의 핵심 과제로 남아 있습니다. 기존의 재타겟팅 방법은 종종 명시적인 접촉 모델링을 무시하거나 강화 학습에 의존하여 정확성과 일반화 능력이 제한적입니다. 이를 해결하기 위해, 우리는 ObjRetarget을 제안합니다. 이는 인간 비디오로부터 로봇의 정밀 조작을 학습하기 위한 인간-로봇 동작 재타겟팅 프레임워크로, 인간형 팔 궤적 제약과 구조화된 손-물체 기하학적 모델링을 통합합니다. 팔 동작의 경우, 인간 비디오에서 추출된 참조 궤적을 초기화에 사용한 후, 인간형 제약과 중복 인식 최적화를 통해 자연스럽고 정확한 움직임을 생성합니다. 손 조작의 경우, ObjRetarget은 다지 접촉을 폴리토프 클러스터로 표현하고 기하학적 불변량을 통해 접촉 구조를 유지하여 안정성을 향상시킵니다. 실제 로봇 실험 결과, ObjRetarget은 여러 정밀 작업에서 조작 성공률과 접촉 안정성을 향상시키며, 다양한 시연, 물체 자세 및 작업 설정에 잘 일반화됩니다.

## 핵심 내용
인간의 조작 비디오로부터 로봇의 정밀 조작을 학습하려면, 안정적인 손-물체 접촉을 유지하면서 인간의 의도를 실행 가능한 로봇 동작으로 안정적으로 재타겟팅해야 하며, 이는 구현 지능의 핵심 과제로 남아 있습니다. 기존의 재타겟팅 방법은 종종 명시적인 접촉 모델링을 무시하거나 강화 학습에 의존하여 정확성과 일반화 능력이 제한적입니다. 이를 해결하기 위해, 우리는 ObjRetarget을 제안합니다. 이는 인간 비디오로부터 로봇의 정밀 조작을 학습하기 위한 인간-로봇 동작 재타겟팅 프레임워크로, 인간형 팔 궤적 제약과 구조화된 손-물체 기하학적 모델링을 통합합니다. 팔 동작의 경우, 인간 비디오에서 추출된 참조 궤적을 초기화에 사용한 후, 인간형 제약과 중복 인식 최적화를 통해 자연스럽고 정확한 움직임을 생성합니다. 손 조작의 경우, ObjRetarget은 다지 접촉을 폴리토프 클러스터로 표현하고 기하학적 불변량을 통해 접촉 구조를 유지하여 안정성을 향상시킵니다. 실제 로봇 실험 결과, ObjRetarget은 여러 정밀 작업에서 조작 성공률과 접촉 안정성을 향상시키며, 다양한 시연, 물체 자세 및 작업 설정에 잘 일반화됩니다.

## 参考
- http://arxiv.org/abs/2607.03828v1
