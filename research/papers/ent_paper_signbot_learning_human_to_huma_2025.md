---
$id: ent_paper_signbot_learning_human_to_huma_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SignBot: Learning Human-to-Humanoid Sign Language Interaction'
  zh: 'SignBot: Learning Human-to-Humanoid Sign Language Interaction'
  ko: 'SignBot: Learning Human-to-Humanoid Sign Language Interaction'
summary:
  en: 'SignBot: Learning Human-to-Humanoid Sign Language Interaction is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'SignBot: Learning Human-to-Humanoid Sign Language Interaction is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'SignBot: Learning Human-to-Humanoid Sign Language Interaction is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
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
- loco_manipulation
- signbot
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.24266v4.
sources:
- id: src_001
  type: paper
  title: 'SignBot: Learning Human-to-Humanoid Sign Language Interaction (arXiv)'
  url: https://arxiv.org/abs/2505.24266
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Sign language is a natural and visual form of language that uses movements and expressions to convey meaning, serving as a crucial means of communication for individuals who are deaf or hard-of-hearing (DHH). However, the number of people proficient in sign language remains limited, highlighting the need for technological advancements to bridge communication gaps and foster interactions with minorities. Based on recent advancements in embodied humanoid robots, we propose SignBot, a novel framework for human-robot sign language interaction. SignBot integrates a cerebellum-inspired motion control component and a cerebral-oriented module for comprehension and interaction. Specifically, SignBot consists of: 1) Motion Retargeting, which converts human sign language datasets into robot-compatible kinematics; 2) Motion Control, which leverages a learning-based paradigm to develop a robust humanoid control policy for tracking sign language gestures; and 3) Generative Interaction, which incorporates translator, responser, and generator of sign language, thereby enabling natural and effective communication between robots and humans. Simulation and real-world experimental results demonstrate that SignBot can effectively facilitate human-robot interaction and perform sign language motions with diverse robots and datasets. SignBot represents a significant advancement in automatic sign language interaction on embodied humanoid robot platforms, providing a promising solution to improve communication accessibility for the DHH community.

## 核心内容
Sign language is a natural and visual form of language that uses movements and expressions to convey meaning, serving as a crucial means of communication for individuals who are deaf or hard-of-hearing (DHH). However, the number of people proficient in sign language remains limited, highlighting the need for technological advancements to bridge communication gaps and foster interactions with minorities. Based on recent advancements in embodied humanoid robots, we propose SignBot, a novel framework for human-robot sign language interaction. SignBot integrates a cerebellum-inspired motion control component and a cerebral-oriented module for comprehension and interaction. Specifically, SignBot consists of: 1) Motion Retargeting, which converts human sign language datasets into robot-compatible kinematics; 2) Motion Control, which leverages a learning-based paradigm to develop a robust humanoid control policy for tracking sign language gestures; and 3) Generative Interaction, which incorporates translator, responser, and generator of sign language, thereby enabling natural and effective communication between robots and humans. Simulation and real-world experimental results demonstrate that SignBot can effectively facilitate human-robot interaction and perform sign language motions with diverse robots and datasets. SignBot represents a significant advancement in automatic sign language interaction on embodied humanoid robot platforms, providing a promising solution to improve communication accessibility for the DHH community.

## 参考
- http://arxiv.org/abs/2505.24266v4

## Overview
Sign language is a natural and visual form of language that uses movements and expressions to convey meaning, serving as a crucial means of communication for individuals who are deaf or hard-of-hearing (DHH). However, the number of people proficient in sign language remains limited, highlighting the need for technological advancements to bridge communication gaps and foster interactions with minorities. Based on recent advancements in embodied humanoid robots, we propose SignBot, a novel framework for human-robot sign language interaction. SignBot integrates a cerebellum-inspired motion control component and a cerebral-oriented module for comprehension and interaction. Specifically, SignBot consists of: 1) Motion Retargeting, which converts human sign language datasets into robot-compatible kinematics; 2) Motion Control, which leverages a learning-based paradigm to develop a robust humanoid control policy for tracking sign language gestures; and 3) Generative Interaction, which incorporates translator, responser, and generator of sign language, thereby enabling natural and effective communication between robots and humans. Simulation and real-world experimental results demonstrate that SignBot can effectively facilitate human-robot interaction and perform sign language motions with diverse robots and datasets. SignBot represents a significant advancement in automatic sign language interaction on embodied humanoid robot platforms, providing a promising solution to improve communication accessibility for the DHH community.

## Content
Sign language is a natural and visual form of language that uses movements and expressions to convey meaning, serving as a crucial means of communication for individuals who are deaf or hard-of-hearing (DHH). However, the number of people proficient in sign language remains limited, highlighting the need for technological advancements to bridge communication gaps and foster interactions with minorities. Based on recent advancements in embodied humanoid robots, we propose SignBot, a novel framework for human-robot sign language interaction. SignBot integrates a cerebellum-inspired motion control component and a cerebral-oriented module for comprehension and interaction. Specifically, SignBot consists of: 1) Motion Retargeting, which converts human sign language datasets into robot-compatible kinematics; 2) Motion Control, which leverages a learning-based paradigm to develop a robust humanoid control policy for tracking sign language gestures; and 3) Generative Interaction, which incorporates translator, responser, and generator of sign language, thereby enabling natural and effective communication between robots and humans. Simulation and real-world experimental results demonstrate that SignBot can effectively facilitate human-robot interaction and perform sign language motions with diverse robots and datasets. SignBot represents a significant advancement in automatic sign language interaction on embodied humanoid robot platforms, providing a promising solution to improve communication accessibility for the DHH community.

## 개요
수화는 움직임과 표정을 통해 의미를 전달하는 자연스럽고 시각적인 언어 형태로, 청각 장애인(DHH)에게 중요한 의사소통 수단입니다. 그러나 수화에 능숙한 사람의 수는 여전히 제한적이어서, 기술 발전을 통해 의사소통 격차를 해소하고 소수 집단과의 상호작용을 촉진할 필요성이 대두되고 있습니다. 최근 구현형 휴머노이드 로봇의 발전을 바탕으로, 우리는 인간-로봇 수화 상호작용을 위한 새로운 프레임워크인 SignBot을 제안합니다. SignBot은 소뇌에서 영감을 받은 동작 제어 구성 요소와 이해 및 상호작용을 위한 대뇌 중심 모듈을 통합합니다. 구체적으로, SignBot은 다음으로 구성됩니다: 1) 인간 수화 데이터 세트를 로봇 호환 운동학으로 변환하는 모션 리타겟팅(Motion Retargeting); 2) 학습 기반 패러다임을 활용하여 수화 제스처를 추적하기 위한 강력한 휴머노이드 제어 정책을 개발하는 모션 제어(Motion Control); 3) 번역기, 응답기, 수화 생성기를 통합하여 로봇과 인간 간의 자연스럽고 효과적인 의사소통을 가능하게 하는 생성형 상호작용(Generative Interaction). 시뮬레이션 및 실제 실험 결과는 SignBot이 인간-로봇 상호작용을 효과적으로 촉진하고 다양한 로봇과 데이터 세트로 수화 동작을 수행할 수 있음을 보여줍니다. SignBot은 구현형 휴머노이드 로봇 플랫폼에서의 자동 수화 상호작용에 있어 중요한 진전을 나타내며, DHH 커뮤니티의 의사소통 접근성을 개선하기 위한 유망한 솔루션을 제공합니다.

## 핵심 내용
수화는 움직임과 표정을 통해 의미를 전달하는 자연스럽고 시각적인 언어 형태로, 청각 장애인(DHH)에게 중요한 의사소통 수단입니다. 그러나 수화에 능숙한 사람의 수는 여전히 제한적이어서, 기술 발전을 통해 의사소통 격차를 해소하고 소수 집단과의 상호작용을 촉진할 필요성이 대두되고 있습니다. 최근 구현형 휴머노이드 로봇의 발전을 바탕으로, 우리는 인간-로봇 수화 상호작용을 위한 새로운 프레임워크인 SignBot을 제안합니다. SignBot은 소뇌에서 영감을 받은 동작 제어 구성 요소와 이해 및 상호작용을 위한 대뇌 중심 모듈을 통합합니다. 구체적으로, SignBot은 다음으로 구성됩니다: 1) 인간 수화 데이터 세트를 로봇 호환 운동학으로 변환하는 모션 리타겟팅(Motion Retargeting); 2) 학습 기반 패러다임을 활용하여 수화 제스처를 추적하기 위한 강력한 휴머노이드 제어 정책을 개발하는 모션 제어(Motion Control); 3) 번역기, 응답기, 수화 생성기를 통합하여 로봇과 인간 간의 자연스럽고 효과적인 의사소통을 가능하게 하는 생성형 상호작용(Generative Interaction). 시뮬레이션 및 실제 실험 결과는 SignBot이 인간-로봇 상호작용을 효과적으로 촉진하고 다양한 로봇과 데이터 세트로 수화 동작을 수행할 수 있음을 보여줍니다. SignBot은 구현형 휴머노이드 로봇 플랫폼에서의 자동 수화 상호작용에 있어 중요한 진전을 나타내며, DHH 커뮤니티의 의사소통 접근성을 개선하기 위한 유망한 솔루션을 제공합니다.
