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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03828v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (767 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.03828v1

## 개요
기존의 운동 재타겟팅 방법은 명시적 접촉 모델링을 무시하거나 강화 학습에 의존하는 경우가 많아 정밀도와 일반화 성능이 제한적입니다. ObjRetarget은 이 문제를 해결하기 위해 인간 비디오에서 참조 궤적을 추출하여 팔 운동을 초기화하고, 인간형 제약 조건과 중복 인식 최적화를 통해 자연스럽고 정확한 동작을 생성합니다. 손 조작의 경우 다면체 클러스터로 다지 접촉을 표현하고 기하학적 불변량을 이용해 접촉 구조를 유지합니다. 실제 로봇 실험 결과, 이 방법은 여러 정교한 조작 작업에서 성공률과 접촉 안정성을 크게 향상시켰으며, 다양한 시연, 물체 자세 및 작업 설정에 잘 일반화됩니다.

## 핵심 내용
### 방법 아키텍처
ObjRetarget은 인간에서 로봇으로의 운동 재타겟팅을 두 가지 핵심 모듈로 분해합니다:
- **팔 운동 모듈**: 먼저 인간 비디오에서 참조 궤적을 추출하여 초기화한 후, 인간형 제약 조건(예: 관절 각도 제한, 운동 평활성)을 적용하고 중복 인식 최적화 알고리즘을 사용하여 자연스럽고 정확한 팔 운동을 생성합니다.
- **손 조작 모듈**: 다면체 클러스터(polytope clusters)를 사용하여 다지와 물체의 접촉 영역을 표현하고, 기하학적 불변량(geometric invariants)을 통해 재타겟팅 과정에서 접촉 구조의 안정성을 유지하여 손가락 미끄러짐이나 접촉 손실을 방지합니다.

### 실험 설정 및 주요 결과
- **실험 플랫폼**: 실제 로봇에서 여러 정교한 조작 작업(예: 파지, 회전, 배치)을 수행합니다.
- **주요 지표**: 조작 성공률(success rate) 및 접촉 안정성(contact stability).
- **성능 향상**: 기존 방법과 비교하여 ObjRetarget은 여러 작업에서 성공률을 크게 향상시켰으며, 다음 변화에 대한 강력한 일반화 능력을 보여줍니다:
  - 다양한 인간 시연 비디오
  - 물체 자세 변화
  - 작업 설정 조정(예: 목표 위치, 물체 유형)

### 결론
ObjRetarget은 팔의 인간형 제약 조건과 손의 접촉 기하학을 명시적으로 모델링함으로써 인간 비디오에서 정교한 조작 학습 시 발생하는 재타겟팅 정밀도와 안정성 문제를 효과적으로 해결하며, 구현 지능에서의 기술 전이를 위한 신뢰할 수 있는 프레임워크를 제공합니다.
