---
$id: ent_paper_tang_mind_to_hand_purposeful_roboti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mind to Hand: Purposeful Robotic Control via Embodied Reasoning'
  zh: Mind to Hand
  ko: 'Mind to Hand: Purposeful Robotic Control via Embodied Reasoning'
summary:
  en: 'Mind to Hand: Purposeful Robotic Control via Embodied Reasoning (Mind to Hand), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Astribot.'
  zh: Mind to Hand 是 Astribot 于 2025 年提出的大型视觉-语言-动作模型 Lumo-1，用于机器人操作。其核心贡献在于通过三阶段预训练流水线，将预训练视觉-语言模型的通用多模态推理能力逐步扩展到具身推理与动作预测，并最终实现推理与动作的对齐。实验表明，Lumo-1
    在具身视觉-语言推理和真实世界机器人任务中均显著超越强基线，尤其在长时域任务和需要策略、概念与空间推理的自然语言指令响应上表现突出。
  ko: 'Mind to Hand: Purposeful Robotic Control via Embodied Reasoning (Mind to Hand), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Astribot.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- mind_to_hand
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.08580v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Mind to Hand: Purposeful Robotic Control via Embodied Reasoning (arXiv)'
  url: https://arxiv.org/abs/2512.08580
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Mind to Hand source
  url: https://doi.org/10.48550/arXiv.2512.08580
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Lumo-1 模型旨在弥合 AI 系统在互联网规模数据上获得的广泛推理能力与物理世界行动之间的鸿沟。它采用三阶段预训练策略：首先在精选的视觉-语言数据上继续预训练，以增强规划、空间理解和轨迹预测等具身推理技能；然后结合跨本体的机器人数据与视觉-语言数据进行协同训练；最后在 Astribot S1 双手机器人采集的轨迹数据上进行带推理过程的动作训练。此外，模型还集成了强化学习以进一步优化推理与动作的一致性。实验结果显示，Lumo-1 在具身推理和真实世界操作任务上均取得了显著性能提升，并展现出对新颖物体和环境的强泛化能力。

## 核心内容
### 方法概述
Lumo-1 是一个通用型视觉-语言-动作（VLA）模型，其设计核心是将机器人推理（"mind"）与动作（"hand"）统一。模型基于预训练的视觉-语言模型（VLM）构建，通过渐进式扩展实现具身推理与动作预测。

### 三阶段预训练流水线
1.  **第一阶段：继续 VLM 预训练**
    *   在精选的视觉-语言数据上继续训练，旨在增强具身推理能力，包括规划、空间理解和轨迹预测。
2.  **第二阶段：跨本体协同训练**
    *   将跨本体的机器人数据与视觉-语言数据混合进行协同训练，使模型适应不同机器人形态。
3.  **第三阶段：带推理过程的动作训练**
    *   在 Astribot S1 双手机器人（具备类人灵巧性与敏捷性）采集的轨迹数据上，进行带推理过程的动作训练，实现结构化推理与动作对齐。

### 强化学习集成
在预训练完成后，集成强化学习进一步优化推理与动作的一致性，形成语义推理与运动控制之间的闭环。

### 实验设置与结果
*   **评估任务**：涵盖多种具有挑战性的机器人操作任务，包括长时域任务、对新颖物体和环境的泛化，以及需要策略、概念和空间推理的自然语言指令响应。
*   **性能表现**：
    *   在具身视觉-语言推理任务上，Lumo-1 取得了显著的性能提升，这是通用机器人控制的关键组成部分。
    *   在真实世界评估中，Lumo-1 在所有任务上均超越了强基线模型。
    *   模型展现出强大的泛化能力，能够处理未见过的物体和环境。
    *   在长时域任务和需要复杂推理的自然语言指令响应上表现尤为突出。

## Overview
Humans act with context and intention, with reasoning playing a central role. While internet-scale data has enabled broad reasoning capabilities in AI systems, grounding these abilities in physical action remains a major challenge. We introduce Lumo-1, a generalist vision-language-action (VLA) model that unifies robot reasoning ("mind") with robot action ("hand"). Our approach builds upon the general multi-modal reasoning capabilities of pre-trained vision-language models (VLMs), progressively extending them to embodied reasoning and action prediction, and ultimately towards structured reasoning and reasoning-action alignment. This results in a three-stage pre-training pipeline: (1) Continued VLM pre-training on curated vision-language data to enhance embodied reasoning skills such as planning, spatial understanding, and trajectory prediction; (2) Co-training on cross-embodiment robot data alongside vision-language data; and (3) Action training with reasoning process on trajectories collected on Astribot S1, a bimanual mobile manipulator with human-like dexterity and agility. Finally, we integrate reinforcement learning to further refine reasoning-action consistency and close the loop between semantic inference and motor control. Extensive experiments demonstrate that Lumo-1 achieves significant performance improvements in embodied vision-language reasoning, a critical component for generalist robotic control. Real-world evaluations further show that Lumo-1 surpasses strong baselines across a wide range of challenging robotic tasks, with strong generalization to novel objects and environments, excelling particularly in long-horizon tasks and responding to human-natural instructions that require reasoning over strategy, concepts and space.

## 개요
인간은 맥락과 의도를 가지고 행동하며, 추론이 중심적인 역할을 합니다. 인터넷 규모의 데이터는 AI 시스템에 광범위한 추론 능력을 부여했지만, 이러한 능력을 물리적 행동에 기반하는 것은 여전히 주요 과제로 남아 있습니다. 우리는 로봇 추론("마음")과 로봇 행동("손")을 통합하는 범용 비전-언어-행동(VLA) 모델인 Lumo-1을 소개합니다. 우리의 접근 방식은 사전 훈련된 비전-언어 모델(VLM)의 일반적인 다중 모달 추론 능력을 기반으로, 이를 점진적으로 체화된 추론 및 행동 예측으로 확장하고, 궁극적으로 구조화된 추론 및 추론-행동 정렬로 발전시킵니다. 이는 세 단계의 사전 훈련 파이프라인으로 구성됩니다: (1) 계획, 공간 이해, 궤적 예측과 같은 체화된 추론 능력을 향상시키기 위해 선별된 비전-언어 데이터로 VLM 사전 훈련 지속; (2) 교차 체화 로봇 데이터와 비전-언어 데이터의 공동 훈련; (3) 인간과 유사한 손재주와 민첩성을 갖춘 양팔 이동형 조작기인 Astribot S1에서 수집된 궤적에 대한 추론 과정을 포함한 행동 훈련. 마지막으로, 강화 학습을 통합하여 추론-행동 일관성을 더욱 정제하고 의미 추론과 운동 제어 간의 순환을 완성합니다. 광범위한 실험을 통해 Lumo-1이 범용 로봇 제어의 핵심 구성 요소인 체화된 비전-언어 추론에서 상당한 성능 향상을 달성함을 입증합니다. 실제 환경 평가에서는 Lumo-1이 다양한 도전적인 로봇 작업에서 강력한 기준선을 능가하며, 새로운 객체와 환경에 대한 강력한 일반화 능력을 보여주고, 특히 장기 작업과 전략, 개념, 공간에 대한 추론이 필요한 인간의 자연스러운 명령에 응답하는 데 뛰어납니다.

## 핵심 내용
인간은 맥락과 의도를 가지고 행동하며, 추론이 중심적인 역할을 합니다. 인터넷 규모의 데이터는 AI 시스템에 광범위한 추론 능력을 부여했지만, 이러한 능력을 물리적 행동에 기반하는 것은 여전히 주요 과제로 남아 있습니다. 우리는 로봇 추론("마음")과 로봇 행동("손")을 통합하는 범용 비전-언어-행동(VLA) 모델인 Lumo-1을 소개합니다. 우리의 접근 방식은 사전 훈련된 비전-언어 모델(VLM)의 일반적인 다중 모달 추론 능력을 기반으로, 이를 점진적으로 체화된 추론 및 행동 예측으로 확장하고, 궁극적으로 구조화된 추론 및 추론-행동 정렬로 발전시킵니다. 이는 세 단계의 사전 훈련 파이프라인으로 구성됩니다: (1) 계획, 공간 이해, 궤적 예측과 같은 체화된 추론 능력을 향상시키기 위해 선별된 비전-언어 데이터로 VLM 사전 훈련 지속; (2) 교차 체화 로봇 데이터와 비전-언어 데이터의 공동 훈련; (3) 인간과 유사한 손재주와 민첩성을 갖춘 양팔 이동형 조작기인 Astribot S1에서 수집된 궤적에 대한 추론 과정을 포함한 행동 훈련. 마지막으로, 강화 학습을 통합하여 추론-행동 일관성을 더욱 정제하고 의미 추론과 운동 제어 간의 순환을 완성합니다. 광범위한 실험을 통해 Lumo-1이 범용 로봇 제어의 핵심 구성 요소인 체화된 비전-언어 추론에서 상당한 성능 향상을 달성함을 입증합니다. 실제 환경 평가에서는 Lumo-1이 다양한 도전적인 로봇 작업에서 강력한 기준선을 능가하며, 새로운 객체와 환경에 대한 강력한 일반화 능력을 보여주고, 특히 장기 작업과 전략, 개념, 공간에 대한 추론이 필요한 인간의 자연스러운 명령에 응답하는 데 뛰어납니다.

## 参考
- http://arxiv.org/abs/2512.08580v2
