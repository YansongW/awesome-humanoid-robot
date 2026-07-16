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
  zh: 'Mind to Hand: Purposeful Robotic Control via Embodied Reasoning (Mind to Hand), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Astribot.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.08580v2.
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
Humans act with context and intention, with reasoning playing a central role. While internet-scale data has enabled broad reasoning capabilities in AI systems, grounding these abilities in physical action remains a major challenge. We introduce Lumo-1, a generalist vision-language-action (VLA) model that unifies robot reasoning ("mind") with robot action ("hand"). Our approach builds upon the general multi-modal reasoning capabilities of pre-trained vision-language models (VLMs), progressively extending them to embodied reasoning and action prediction, and ultimately towards structured reasoning and reasoning-action alignment. This results in a three-stage pre-training pipeline: (1) Continued VLM pre-training on curated vision-language data to enhance embodied reasoning skills such as planning, spatial understanding, and trajectory prediction; (2) Co-training on cross-embodiment robot data alongside vision-language data; and (3) Action training with reasoning process on trajectories collected on Astribot S1, a bimanual mobile manipulator with human-like dexterity and agility. Finally, we integrate reinforcement learning to further refine reasoning-action consistency and close the loop between semantic inference and motor control. Extensive experiments demonstrate that Lumo-1 achieves significant performance improvements in embodied vision-language reasoning, a critical component for generalist robotic control. Real-world evaluations further show that Lumo-1 surpasses strong baselines across a wide range of challenging robotic tasks, with strong generalization to novel objects and environments, excelling particularly in long-horizon tasks and responding to human-natural instructions that require reasoning over strategy, concepts and space.

## 核心内容
Humans act with context and intention, with reasoning playing a central role. While internet-scale data has enabled broad reasoning capabilities in AI systems, grounding these abilities in physical action remains a major challenge. We introduce Lumo-1, a generalist vision-language-action (VLA) model that unifies robot reasoning ("mind") with robot action ("hand"). Our approach builds upon the general multi-modal reasoning capabilities of pre-trained vision-language models (VLMs), progressively extending them to embodied reasoning and action prediction, and ultimately towards structured reasoning and reasoning-action alignment. This results in a three-stage pre-training pipeline: (1) Continued VLM pre-training on curated vision-language data to enhance embodied reasoning skills such as planning, spatial understanding, and trajectory prediction; (2) Co-training on cross-embodiment robot data alongside vision-language data; and (3) Action training with reasoning process on trajectories collected on Astribot S1, a bimanual mobile manipulator with human-like dexterity and agility. Finally, we integrate reinforcement learning to further refine reasoning-action consistency and close the loop between semantic inference and motor control. Extensive experiments demonstrate that Lumo-1 achieves significant performance improvements in embodied vision-language reasoning, a critical component for generalist robotic control. Real-world evaluations further show that Lumo-1 surpasses strong baselines across a wide range of challenging robotic tasks, with strong generalization to novel objects and environments, excelling particularly in long-horizon tasks and responding to human-natural instructions that require reasoning over strategy, concepts and space.

## 参考
- http://arxiv.org/abs/2512.08580v2

## Overview
Humans act with context and intention, with reasoning playing a central role. While internet-scale data has enabled broad reasoning capabilities in AI systems, grounding these abilities in physical action remains a major challenge. We introduce Lumo-1, a generalist vision-language-action (VLA) model that unifies robot reasoning ("mind") with robot action ("hand"). Our approach builds upon the general multi-modal reasoning capabilities of pre-trained vision-language models (VLMs), progressively extending them to embodied reasoning and action prediction, and ultimately towards structured reasoning and reasoning-action alignment. This results in a three-stage pre-training pipeline: (1) Continued VLM pre-training on curated vision-language data to enhance embodied reasoning skills such as planning, spatial understanding, and trajectory prediction; (2) Co-training on cross-embodiment robot data alongside vision-language data; and (3) Action training with reasoning process on trajectories collected on Astribot S1, a bimanual mobile manipulator with human-like dexterity and agility. Finally, we integrate reinforcement learning to further refine reasoning-action consistency and close the loop between semantic inference and motor control. Extensive experiments demonstrate that Lumo-1 achieves significant performance improvements in embodied vision-language reasoning, a critical component for generalist robotic control. Real-world evaluations further show that Lumo-1 surpasses strong baselines across a wide range of challenging robotic tasks, with strong generalization to novel objects and environments, excelling particularly in long-horizon tasks and responding to human-natural instructions that require reasoning over strategy, concepts and space.

## Content
Humans act with context and intention, with reasoning playing a central role. While internet-scale data has enabled broad reasoning capabilities in AI systems, grounding these abilities in physical action remains a major challenge. We introduce Lumo-1, a generalist vision-language-action (VLA) model that unifies robot reasoning ("mind") with robot action ("hand"). Our approach builds upon the general multi-modal reasoning capabilities of pre-trained vision-language models (VLMs), progressively extending them to embodied reasoning and action prediction, and ultimately towards structured reasoning and reasoning-action alignment. This results in a three-stage pre-training pipeline: (1) Continued VLM pre-training on curated vision-language data to enhance embodied reasoning skills such as planning, spatial understanding, and trajectory prediction; (2) Co-training on cross-embodiment robot data alongside vision-language data; and (3) Action training with reasoning process on trajectories collected on Astribot S1, a bimanual mobile manipulator with human-like dexterity and agility. Finally, we integrate reinforcement learning to further refine reasoning-action consistency and close the loop between semantic inference and motor control. Extensive experiments demonstrate that Lumo-1 achieves significant performance improvements in embodied vision-language reasoning, a critical component for generalist robotic control. Real-world evaluations further show that Lumo-1 surpasses strong baselines across a wide range of challenging robotic tasks, with strong generalization to novel objects and environments, excelling particularly in long-horizon tasks and responding to human-natural instructions that require reasoning over strategy, concepts and space.

## 개요
인간은 맥락과 의도를 가지고 행동하며, 추론이 중심적인 역할을 합니다. 인터넷 규모의 데이터는 AI 시스템에 광범위한 추론 능력을 부여했지만, 이러한 능력을 물리적 행동에 기반하는 것은 여전히 주요 과제로 남아 있습니다. 우리는 로봇 추론("마음")과 로봇 행동("손")을 통합하는 범용 비전-언어-행동(VLA) 모델인 Lumo-1을 소개합니다. 우리의 접근 방식은 사전 훈련된 비전-언어 모델(VLM)의 일반적인 다중 모달 추론 능력을 기반으로, 이를 점진적으로 체화된 추론 및 행동 예측으로 확장하고, 궁극적으로 구조화된 추론 및 추론-행동 정렬로 발전시킵니다. 이는 세 단계의 사전 훈련 파이프라인으로 구성됩니다: (1) 계획, 공간 이해, 궤적 예측과 같은 체화된 추론 능력을 향상시키기 위해 선별된 비전-언어 데이터로 VLM 사전 훈련 지속; (2) 교차 체화 로봇 데이터와 비전-언어 데이터의 공동 훈련; (3) 인간과 유사한 손재주와 민첩성을 갖춘 양팔 이동형 조작기인 Astribot S1에서 수집된 궤적에 대한 추론 과정을 포함한 행동 훈련. 마지막으로, 강화 학습을 통합하여 추론-행동 일관성을 더욱 정제하고 의미 추론과 운동 제어 간의 순환을 완성합니다. 광범위한 실험을 통해 Lumo-1이 범용 로봇 제어의 핵심 구성 요소인 체화된 비전-언어 추론에서 상당한 성능 향상을 달성함을 입증합니다. 실제 환경 평가에서는 Lumo-1이 다양한 도전적인 로봇 작업에서 강력한 기준선을 능가하며, 새로운 객체와 환경에 대한 강력한 일반화 능력을 보여주고, 특히 장기 작업과 전략, 개념, 공간에 대한 추론이 필요한 인간의 자연스러운 명령에 응답하는 데 뛰어납니다.

## 핵심 내용
인간은 맥락과 의도를 가지고 행동하며, 추론이 중심적인 역할을 합니다. 인터넷 규모의 데이터는 AI 시스템에 광범위한 추론 능력을 부여했지만, 이러한 능력을 물리적 행동에 기반하는 것은 여전히 주요 과제로 남아 있습니다. 우리는 로봇 추론("마음")과 로봇 행동("손")을 통합하는 범용 비전-언어-행동(VLA) 모델인 Lumo-1을 소개합니다. 우리의 접근 방식은 사전 훈련된 비전-언어 모델(VLM)의 일반적인 다중 모달 추론 능력을 기반으로, 이를 점진적으로 체화된 추론 및 행동 예측으로 확장하고, 궁극적으로 구조화된 추론 및 추론-행동 정렬로 발전시킵니다. 이는 세 단계의 사전 훈련 파이프라인으로 구성됩니다: (1) 계획, 공간 이해, 궤적 예측과 같은 체화된 추론 능력을 향상시키기 위해 선별된 비전-언어 데이터로 VLM 사전 훈련 지속; (2) 교차 체화 로봇 데이터와 비전-언어 데이터의 공동 훈련; (3) 인간과 유사한 손재주와 민첩성을 갖춘 양팔 이동형 조작기인 Astribot S1에서 수집된 궤적에 대한 추론 과정을 포함한 행동 훈련. 마지막으로, 강화 학습을 통합하여 추론-행동 일관성을 더욱 정제하고 의미 추론과 운동 제어 간의 순환을 완성합니다. 광범위한 실험을 통해 Lumo-1이 범용 로봇 제어의 핵심 구성 요소인 체화된 비전-언어 추론에서 상당한 성능 향상을 달성함을 입증합니다. 실제 환경 평가에서는 Lumo-1이 다양한 도전적인 로봇 작업에서 강력한 기준선을 능가하며, 새로운 객체와 환경에 대한 강력한 일반화 능력을 보여주고, 특히 장기 작업과 전략, 개념, 공간에 대한 추론이 필요한 인간의 자연스러운 명령에 응답하는 데 뛰어납니다.
