---
$id: ent_paper_joglekar_towards_natural_language_drive_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Natural Language-Driven Assembly Using Foundation Models
  zh: Towards Natural Language-Driven Assembly Using Foundation Models
  ko: Towards Natural Language-Driven Assembly Using Foundation Models
summary:
  en: Towards Natural Language-Driven Assembly Using Foundation Models (Towards Natural Language-Driven Assembly Using Foundation
    Models), is a 2024 large vision-language-action model for robotic manipulation, introduced by Bosch Center for Artificial
    Intelligence, Tel Aviv University.
  zh: Towards Natural Language-Driven Assembly Using Foundation Models (Towards Natural Language-Driven Assembly Using Foundation
    Models), is a 2024 large vision-language-action model for robotic manipulation, introduced by Bosch Center for Artificial
    Intelligence, Tel Aviv University.
  ko: Towards Natural Language-Driven Assembly Using Foundation Models (Towards Natural Language-Driven Assembly Using Foundation
    Models), is a 2024 large vision-language-action model for robotic manipulation, introduced by Bosch Center for Artificial
    Intelligence, Tel Aviv University.
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
- robotic_manipulation
- towards_natural_language_drive
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.16093v1.
sources:
- id: src_001
  type: paper
  title: Towards Natural Language-Driven Assembly Using Foundation Models (arXiv)
  url: https://arxiv.org/abs/2406.16093
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Towards Natural Language-Driven Assembly Using Foundation Models source
  url: https://doi.org/10.48550/arXiv.2406.16093
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Large Language Models (LLMs) and strong vision models have enabled rapid research and development in the field of Vision-Language-Action models that enable robotic control. The main objective of these methods is to develop a generalist policy that can control robots with various embodiments. However, in industrial robotic applications such as automated assembly and disassembly, some tasks, such as insertion, demand greater accuracy and involve intricate factors like contact engagement, friction handling, and refined motor skills. Implementing these skills using a generalist policy is challenging because these policies might integrate further sensory data, including force or torque measurements, for enhanced precision. In our method, we present a global control policy based on LLMs that can transfer the control policy to a finite set of skills that are specifically trained to perform high-precision tasks through dynamic context switching. The integration of LLMs into this framework underscores their significance in not only interpreting and processing language inputs but also in enriching the control mechanisms for diverse and intricate robotic operations.

## 核心内容
Large Language Models (LLMs) and strong vision models have enabled rapid research and development in the field of Vision-Language-Action models that enable robotic control. The main objective of these methods is to develop a generalist policy that can control robots with various embodiments. However, in industrial robotic applications such as automated assembly and disassembly, some tasks, such as insertion, demand greater accuracy and involve intricate factors like contact engagement, friction handling, and refined motor skills. Implementing these skills using a generalist policy is challenging because these policies might integrate further sensory data, including force or torque measurements, for enhanced precision. In our method, we present a global control policy based on LLMs that can transfer the control policy to a finite set of skills that are specifically trained to perform high-precision tasks through dynamic context switching. The integration of LLMs into this framework underscores their significance in not only interpreting and processing language inputs but also in enriching the control mechanisms for diverse and intricate robotic operations.

## 参考
- http://arxiv.org/abs/2406.16093v1

## Overview
Large Language Models (LLMs) and strong vision models have enabled rapid research and development in the field of Vision-Language-Action models that enable robotic control. The main objective of these methods is to develop a generalist policy that can control robots with various embodiments. However, in industrial robotic applications such as automated assembly and disassembly, some tasks, such as insertion, demand greater accuracy and involve intricate factors like contact engagement, friction handling, and refined motor skills. Implementing these skills using a generalist policy is challenging because these policies might integrate further sensory data, including force or torque measurements, for enhanced precision. In our method, we present a global control policy based on LLMs that can transfer the control policy to a finite set of skills that are specifically trained to perform high-precision tasks through dynamic context switching. The integration of LLMs into this framework underscores their significance in not only interpreting and processing language inputs but also in enriching the control mechanisms for diverse and intricate robotic operations.

## Content
Large Language Models (LLMs) and strong vision models have enabled rapid research and development in the field of Vision-Language-Action models that enable robotic control. The main objective of these methods is to develop a generalist policy that can control robots with various embodiments. However, in industrial robotic applications such as automated assembly and disassembly, some tasks, such as insertion, demand greater accuracy and involve intricate factors like contact engagement, friction handling, and refined motor skills. Implementing these skills using a generalist policy is challenging because these policies might integrate further sensory data, including force or torque measurements, for enhanced precision. In our method, we present a global control policy based on LLMs that can transfer the control policy to a finite set of skills that are specifically trained to perform high-precision tasks through dynamic context switching. The integration of LLMs into this framework underscores their significance in not only interpreting and processing language inputs but also in enriching the control mechanisms for diverse and intricate robotic operations.

## 개요
대규모 언어 모델(LLM)과 강력한 비전 모델은 로봇 제어를 가능하게 하는 비전-언어-행동 모델 분야의 빠른 연구 및 개발을 촉진했습니다. 이러한 방법의 주요 목표는 다양한 형태의 로봇을 제어할 수 있는 범용 정책을 개발하는 것입니다. 그러나 자동 조립 및 분해와 같은 산업용 로봇 응용 분야에서 삽입과 같은 일부 작업은 더 높은 정밀도를 요구하며 접촉 결합, 마찰 처리 및 정교한 운동 기술과 같은 복잡한 요소를 포함합니다. 이러한 기술을 범용 정책으로 구현하는 것은 어려운데, 이러한 정책이 정밀도 향상을 위해 힘이나 토크 측정과 같은 추가 감각 데이터를 통합할 수 있기 때문입니다. 본 방법에서는 LLM 기반의 글로벌 제어 정책을 제시하며, 이는 동적 컨텍스트 전환을 통해 고정밀 작업을 수행하도록 특별히 훈련된 유한한 기술 집합으로 제어 정책을 전환할 수 있습니다. 이 프레임워크에 LLM을 통합함으로써 언어 입력을 해석하고 처리하는 것뿐만 아니라 다양하고 복잡한 로봇 작업을 위한 제어 메커니즘을 풍부하게 하는 데 있어 그 중요성이 강조됩니다.

## 핵심 내용
대규모 언어 모델(LLM)과 강력한 비전 모델은 로봇 제어를 가능하게 하는 비전-언어-행동 모델 분야의 빠른 연구 및 개발을 촉진했습니다. 이러한 방법의 주요 목표는 다양한 형태의 로봇을 제어할 수 있는 범용 정책을 개발하는 것입니다. 그러나 자동 조립 및 분해와 같은 산업용 로봇 응용 분야에서 삽입과 같은 일부 작업은 더 높은 정밀도를 요구하며 접촉 결합, 마찰 처리 및 정교한 운동 기술과 같은 복잡한 요소를 포함합니다. 이러한 기술을 범용 정책으로 구현하는 것은 어려운데, 이러한 정책이 정밀도 향상을 위해 힘이나 토크 측정과 같은 추가 감각 데이터를 통합할 수 있기 때문입니다. 본 방법에서는 LLM 기반의 글로벌 제어 정책을 제시하며, 이는 동적 컨텍스트 전환을 통해 고정밀 작업을 수행하도록 특별히 훈련된 유한한 기술 집합으로 제어 정책을 전환할 수 있습니다. 이 프레임워크에 LLM을 통합함으로써 언어 입력을 해석하고 처리하는 것뿐만 아니라 다양하고 복잡한 로봇 작업을 위한 제어 메커니즘을 풍부하게 하는 데 있어 그 중요성이 강조됩니다.
