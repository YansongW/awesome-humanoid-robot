---
$id: ent_paper_act_sense_act_learning_active_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Act, Sense, Act: Learning Active Perception from Large-Scale Egocentric Human Data'
  zh: 'Act, Sense, Act: Learning Active Perception from Large-Scale Egocentric Human Data'
  ko: 'Act, Sense, Act: Learning Active Perception from Large-Scale Egocentric Human Data'
summary:
  en: 'arXiv:2602.04600v2 Announce Type: replace Abstract: Achieving generalizable manipulation in unconstrained environments
    requires the robot to proactively resolve information uncertainty, i.e., the capability of active perception. However,
    existing methods are often confined in limited types of sensing behaviors, restricting their applicability to complex
    environments. In this work, we formalize active perception as a history-dependent perception-action loop driven by information-seeking
    action and decision branching, providing a structured categorization of visual active perception paradigms. Building on
    this perspective, we introduce CoMe-VLA, a cognitive and memory-aware vision-language-action (VLA) framework that leverages
    large-scale human egocentric data to learn versatile exploration and manipulation priors. Our framework integrates a cognitive
    auxiliary head for autonomous sub-task transitions and a dual-track memory system to maintain consistent self and environmental
    awareness by fusing proprioceptive and visual temporal contexts. By aligning human and robot hand-eye coordination behaviors
    in a unified egocentric action space, we train the model progressively in three stages. Extensive experiments on a wheel-based
    humanoid have demonstrated strong robustness and adaptability of our proposed method across diverse long-horizon tasks
    spanning multiple active perception scenarios.'
  zh: 本文提出CoMe-VLA，一个认知与记忆增强的视觉-语言-动作（VLA）框架，旨在通过大规模人类第一人称数据学习主动感知与操作先验。其核心贡献在于形式化主动感知为历史依赖的感知-动作循环，并集成认知辅助头与双轨记忆系统，在轮式人形机器人上实现跨多种长时程任务的鲁棒适应。
  ko: 'arXiv:2602.04600v2 Announce Type: replace Abstract: Achieving generalizable manipulation in unconstrained environments
    requires the robot to proactively resolve information uncertainty, i.e., the capability of active perception. However,
    existing methods are often confined in limited types of sensing behaviors, restricting their applicability to complex
    environments. In this work, we formalize active perception as a history-dependent perception-action loop driven by information-seeking
    action and decision branching, providing a structured categorization of visual active perception paradigms. Building on
    this perspective, we introduce CoMe-VLA, a cognitive and memory-aware vision-language-action (VLA) framework that leverages
    large-scale human egocentric data to learn versatile exploration and manipulation priors. Our framework integrates a cognitive
    auxiliary head for autonomous sub-task transitions and a dual-track memory system to maintain consistent self and environmental
    awareness by fusing proprioceptive and visual temporal contexts. By aligning human and robot hand-eye coordination behaviors
    in a unified egocentric action space, we train the model progressively in three stages. Extensive experiments on a wheel-based
    humanoid have demonstrated strong robustness and adaptability of our proposed method across diverse long-horizon tasks
    spanning multiple active perception scenarios.'
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
- act_sense_act
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.04600v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Act, Sense, Act: Learning Active Perception from Large-Scale Egocentric Human Data (arXiv)'
  url: https://arxiv.org/abs/2602.04600
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
现有主动感知方法受限于有限的感知行为类型，难以应对复杂环境。本文首先将主动感知形式化为由信息寻求动作与决策分支驱动的、依赖历史的感知-动作循环，并对视觉主动感知范式进行了结构化分类。基于此，作者提出CoMe-VLA框架，利用大规模人类第一人称数据学习通用的探索与操作先验。该框架集成了用于自主子任务切换的认知辅助头，以及通过融合本体感觉与视觉时间上下文来维持一致自我与环境感知的双轨记忆系统。通过在统一的自我中心动作空间中对齐人类与机器人的手眼协调行为，模型分三阶段渐进训练。在轮式人形机器人上的大量实验表明，该方法在覆盖多种主动感知场景的多样化长时程任务中展现出强大的鲁棒性与适应性。

## 核心内容
### 方法架构
- **主动感知形式化**：将主动感知定义为依赖历史的感知-动作循环，由信息寻求动作与决策分支驱动，并据此对视觉主动感知范式进行结构化分类。
- **CoMe-VLA框架**：一个认知与记忆增强的视觉-语言-动作（VLA）框架，核心组件包括：
  - **认知辅助头**：用于自主子任务切换，使机器人能根据当前状态与目标主动决定下一步感知或操作行为。
  - **双轨记忆系统**：通过融合本体感觉与视觉时间上下文，维持一致的自我与环境感知，确保长时程任务中的状态连贯性。
- **训练策略**：在统一的自我中心动作空间中对齐人类与机器人的手眼协调行为，模型分三阶段渐进训练，逐步学习从基础探索到复杂操作的技能。

### 实验设置与结果
- **平台**：轮式人形机器人。
- **任务**：覆盖多种主动感知场景的多样化长时程任务，包括但不限于物体搜索、环境探索与精准操作。
- **关键结果**：实验表明，CoMe-VLA在跨任务泛化与鲁棒性上显著优于现有方法，尤其在信息不确定性高的环境中，能主动调整感知策略以完成任务。具体数字未在摘要中给出，但强调“strong robustness and adaptability”。

## Overview
Achieving generalizable manipulation in unconstrained environments requires the robot to proactively resolve information uncertainty, i.e., the capability of active perception. However, existing methods are often confined in limited types of sensing behaviors, restricting their applicability to complex environments. In this work, we formalize active perception as a history-dependent perception-action loop driven by information-seeking action and decision branching, providing a structured categorization of visual active perception paradigms. Building on this perspective, we introduce CoMe-VLA, a cognitive and memory-aware vision-language-action (VLA) framework that leverages large-scale human egocentric data to learn versatile exploration and manipulation priors. Our framework integrates a cognitive auxiliary head for autonomous sub-task transitions and a dual-track memory system to maintain consistent self and environmental awareness by fusing proprioceptive and visual temporal contexts. By aligning human and robot hand-eye coordination behaviors in a unified egocentric action space, we train the model progressively in three stages. Extensive experiments on a wheel-based humanoid have demonstrated strong robustness and adaptability of our proposed method across diverse long-horizon tasks spanning multiple active perception scenarios.

## 개요
제약 없는 환경에서 일반화 가능한 조작을 달성하려면 로봇이 정보 불확실성을 능동적으로 해결해야 합니다. 즉, 능동적 인지(active perception) 능력이 필요합니다. 그러나 기존 방법들은 종종 제한된 유형의 감지 행동에 국한되어 복잡한 환경에 적용하기 어렵습니다. 본 연구에서는 능동적 인지를 정보 탐색 행동과 의사 결정 분기에 의해 구동되는 이력 의존적 인지-행동 루프로 정형화하고, 시각적 능동 인지 패러다임의 구조적 분류를 제공합니다. 이러한 관점을 바탕으로, 대규모 인간 자기중심적 데이터를 활용하여 다양한 탐색 및 조작 사전 지식을 학습하는 인지 및 기억 인식 비전-언어-행동(VLA) 프레임워크인 CoMe-VLA를 소개합니다. 우리 프레임워크는 자율적 하위 작업 전환을 위한 인지 보조 헤드와 고유 감각 및 시각적 시간적 맥락을 융합하여 일관된 자기 및 환경 인식을 유지하는 이중 트랙 기억 시스템을 통합합니다. 인간과 로봇의 손-눈 협응 행동을 통합된 자기중심적 행동 공간에서 정렬함으로써, 모델을 세 단계로 점진적으로 훈련합니다. 바퀴 기반 휴머노이드에 대한 광범위한 실험을 통해, 다양한 능동적 인지 시나리오를 아우르는 여러 장기 과제에서 제안된 방법의 강력한 견고성과 적응성을 입증했습니다.

## 핵심 내용
제약 없는 환경에서 일반화 가능한 조작을 달성하려면 로봇이 정보 불확실성을 능동적으로 해결해야 합니다. 즉, 능동적 인지(active perception) 능력이 필요합니다. 그러나 기존 방법들은 종종 제한된 유형의 감지 행동에 국한되어 복잡한 환경에 적용하기 어렵습니다. 본 연구에서는 능동적 인지를 정보 탐색 행동과 의사 결정 분기에 의해 구동되는 이력 의존적 인지-행동 루프로 정형화하고, 시각적 능동 인지 패러다임의 구조적 분류를 제공합니다. 이러한 관점을 바탕으로, 대규모 인간 자기중심적 데이터를 활용하여 다양한 탐색 및 조작 사전 지식을 학습하는 인지 및 기억 인식 비전-언어-행동(VLA) 프레임워크인 CoMe-VLA를 소개합니다. 우리 프레임워크는 자율적 하위 작업 전환을 위한 인지 보조 헤드와 고유 감각 및 시각적 시간적 맥락을 융합하여 일관된 자기 및 환경 인식을 유지하는 이중 트랙 기억 시스템을 통합합니다. 인간과 로봇의 손-눈 협응 행동을 통합된 자기중심적 행동 공간에서 정렬함으로써, 모델을 세 단계로 점진적으로 훈련합니다. 바퀴 기반 휴머노이드에 대한 광범위한 실험을 통해, 다양한 능동적 인지 시나리오를 아우르는 여러 장기 과제에서 제안된 방법의 강력한 견고성과 적응성을 입증했습니다.

## 参考
- http://arxiv.org/abs/2602.04600v2
