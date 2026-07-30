---
$id: ent_paper_vlm_ar3l_vision_language_model_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLM-AR3L: Vision-Language Models for Absolute and Relative Rewards in Reinforcement Learning'
  zh: 'VLM-AR3L: Vision-Language Models for Absolute and Relative Rewards in Reinforcement Learning'
  ko: 'VLM-AR3L: Vision-Language Models for Absolute and Relative Rewards in Reinforcement Learning'
summary:
  en: 'arXiv:2607.00483v1 Announce Type: new Abstract: Designing effective reward functions remains a major challenge in reinforcement
    learning (RL), particularly in open-ended environments where task goals are abstract and difficult to quantify. In this
    work, we present VLM-AR3L, a framework that leverages Vision-Language Models (VLMs) to provide both absolute and relative
    rewards for RL. VLM-AR3L interprets an agent''s visual observations in the context of a natural language task goal, and
    learns both absolute and relative rewards from VLM-generated preference labels. The absolute reward model predicts scalar
    evaluations for individual states, while the relative reward model compares consecutive observations to infer progress
    or regression toward the task goal. Their integration combines the stability of state-based evaluation with the robustness
    of comparative supervision. We evaluate VLM-AR3L across benchmarks spanning classic control, manipulation, and open-world
    embodied tasks, with a particular focus on Minecraft given its visual complexity and long-horizon decision-making requirements.
    Experimental results show that VLM-AR3L consistently outperforms prior VLM-based reward learning methods.'
  zh: VLM-AR3L 是一个利用视觉语言模型（VLM）为强化学习（RL）提供绝对与相对奖励的框架。该工作由论文作者团队提出，核心贡献在于通过 VLM 生成的偏好标签同时学习两种奖励模型：绝对奖励模型评估单个状态，相对奖励模型比较连续观测以推断任务进展。在经典控制、操作和开放世界具身任务（特别是
    Minecraft）上的实验表明，VLM-AR3L 持续优于以往的 VLM 奖励学习方法。
  ko: 'arXiv:2607.00483v1 Announce Type: new Abstract: Designing effective reward functions remains a major challenge in reinforcement
    learning (RL), particularly in open-ended environments where task goals are abstract and difficult to quantify. In this
    work, we present VLM-AR3L, a framework that leverages Vision-Language Models (VLMs) to provide both absolute and relative
    rewards for RL. VLM-AR3L interprets an agent''s visual observations in the context of a natural language task goal, and
    learns both absolute and relative rewards from VLM-generated preference labels. The absolute reward model predicts scalar
    evaluations for individual states, while the relative reward model compares consecutive observations to infer progress
    or regression toward the task goal. Their integration combines the stability of state-based evaluation with the robustness
    of comparative supervision. We evaluate VLM-AR3L across benchmarks spanning classic control, manipulation, and open-world
    embodied tasks, with a particular focus on Minecraft given its visual complexity and long-horizon decision-making requirements.
    Experimental results show that VLM-AR3L consistently outperforms prior VLM-based reward learning methods.'
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
- vlm_ar3l
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00483v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'VLM-AR3L: Vision-Language Models for Absolute and Relative Rewards in Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2607.00483
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
在强化学习中，设计有效的奖励函数是一大挑战，尤其在任务目标抽象且难以量化的开放环境中。VLM-AR3L 框架通过视觉语言模型（VLM）解读智能体的视觉观测，并结合自然语言任务目标，从 VLM 生成的偏好标签中学习绝对和相对奖励。绝对奖励模型为每个状态提供标量评估，而相对奖励模型则通过比较连续观测来推断任务进展或倒退。两者的结合融合了状态评估的稳定性和比较监督的鲁棒性。该框架在多个基准测试中进行了评估，包括经典控制、操作和开放世界具身任务，特别关注视觉复杂且需要长时决策的 Minecraft 环境。

## 核心内容
### 方法
- VLM-AR3L 利用视觉语言模型（VLM）处理智能体的视觉观测，并结合自然语言任务目标生成偏好标签。
- 框架包含两个核心组件：
  - **绝对奖励模型**：为每个独立状态预测标量奖励值，提供稳定的状态级评估。
  - **相对奖励模型**：比较连续观测对，推断智能体相对于任务目标的进展或倒退，提供比较性监督。
- 两种奖励模型通过集成学习结合，融合了绝对奖励的稳定性和相对奖励的鲁棒性。

### 实验设置
- 评估覆盖多个基准：经典控制任务、操作任务以及开放世界具身任务。
- 特别聚焦于 Minecraft 环境，因其视觉复杂性高且需要长时决策。
- 对比方法为以往的 VLM 奖励学习方法。

### 关键结果
- VLM-AR3L 在所有基准测试中持续优于先前的 VLM 奖励学习方法。
- 在 Minecraft 任务中，VLM-AR3L 展示了更强的奖励信号质量，有效支持了长时决策。

### 结论
VLM-AR3L 通过结合绝对与相对奖励，显著提升了强化学习在复杂开放环境中的奖励设计效果，为 VLM 在 RL 中的应用提供了新范式。

## Overview
Designing effective reward functions remains a major challenge in reinforcement learning (RL), particularly in open-ended environments where task goals are abstract and difficult to quantify. In this work, we present VLM-AR3L, a framework that leverages Vision-Language Models (VLMs) to provide both absolute and relative rewards for RL. VLM-AR3L interprets an agent's visual observations in the context of a natural language task goal, and learns both absolute and relative rewards from VLM-generated preference labels. The absolute reward model predicts scalar evaluations for individual states, while the relative reward model compares consecutive observations to infer progress or regression toward the task goal. Their integration combines the stability of state-based evaluation with the robustness of comparative supervision. We evaluate VLM-AR3L across benchmarks spanning classic control, manipulation, and open-world embodied tasks, with a particular focus on Minecraft given its visual complexity and long-horizon decision-making requirements. Experimental results show that VLM-AR3L consistently outperforms prior VLM-based reward learning methods.

## 개요
강화 학습(RL)에서 효과적인 보상 함수를 설계하는 것은 여전히 주요 과제이며, 특히 작업 목표가 추상적이고 정량화하기 어려운 개방형 환경에서 더욱 그렇습니다. 본 연구에서는 비전-언어 모델(VLM)을 활용하여 RL에 절대적 및 상대적 보상을 모두 제공하는 프레임워크인 VLM-AR3L을 제시합니다. VLM-AR3L은 자연어 작업 목표의 맥락에서 에이전트의 시각적 관찰을 해석하고, VLM이 생성한 선호 레이블로부터 절대적 및 상대적 보상을 학습합니다. 절대적 보상 모델은 개별 상태에 대한 스칼라 평가를 예측하는 반면, 상대적 보상 모델은 연속적인 관찰을 비교하여 작업 목표에 대한 진행 또는 후퇴를 추론합니다. 이들의 통합은 상태 기반 평가의 안정성과 비교 감독의 견고성을 결합합니다. 우리는 고전적 제어, 조작, 개방형 세계 구현 작업을 아우르는 벤치마크에서 VLM-AR3L을 평가하며, 특히 시각적 복잡성과 장기적 의사 결정 요구 사항을 고려하여 Minecraft에 중점을 둡니다. 실험 결과는 VLM-AR3L이 기존 VLM 기반 보상 학습 방법을 일관되게 능가함을 보여줍니다.

## 핵심 내용
강화 학습(RL)에서 효과적인 보상 함수를 설계하는 것은 여전히 주요 과제이며, 특히 작업 목표가 추상적이고 정량화하기 어려운 개방형 환경에서 더욱 그렇습니다. 본 연구에서는 비전-언어 모델(VLM)을 활용하여 RL에 절대적 및 상대적 보상을 모두 제공하는 프레임워크인 VLM-AR3L을 제시합니다. VLM-AR3L은 자연어 작업 목표의 맥락에서 에이전트의 시각적 관찰을 해석하고, VLM이 생성한 선호 레이블로부터 절대적 및 상대적 보상을 학습합니다. 절대적 보상 모델은 개별 상태에 대한 스칼라 평가를 예측하는 반면, 상대적 보상 모델은 연속적인 관찰을 비교하여 작업 목표에 대한 진행 또는 후퇴를 추론합니다. 이들의 통합은 상태 기반 평가의 안정성과 비교 감독의 견고성을 결합합니다. 우리는 고전적 제어, 조작, 개방형 세계 구현 작업을 아우르는 벤치마크에서 VLM-AR3L을 평가하며, 특히 시각적 복잡성과 장기적 의사 결정 요구 사항을 고려하여 Minecraft에 중점을 둡니다. 실험 결과는 VLM-AR3L이 기존 VLM 기반 보상 학습 방법을 일관되게 능가함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2607.00483v2
