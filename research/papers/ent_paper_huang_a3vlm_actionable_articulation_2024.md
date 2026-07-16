---
$id: ent_paper_huang_a3vlm_actionable_articulation_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'A3VLM: Actionable Articulation-Aware Vision Language Model'
  zh: A3VLM
  ko: 'A3VLM: Actionable Articulation-Aware Vision Language Model'
summary:
  en: 'A3VLM: Actionable Articulation-Aware Vision Language Model (A3VLM), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by SJTU, Shanghai AI Lab, Rutgers University, Yuandao AI, PKU, CUHK MMLab, and published
    at CoRL24.'
  zh: 'A3VLM: Actionable Articulation-Aware Vision Language Model (A3VLM), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by SJTU, Shanghai AI Lab, Rutgers University, Yuandao AI, PKU, CUHK MMLab, and published
    at CoRL24.'
  ko: 'A3VLM: Actionable Articulation-Aware Vision Language Model (A3VLM), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by SJTU, Shanghai AI Lab, Rutgers University, Yuandao AI, PKU, CUHK MMLab, and published
    at CoRL24.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a3vlm
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.07549v2.
sources:
- id: src_001
  type: paper
  title: A3VLM source
  url: https://proceedings.mlr.press/v270/huang25b.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Vision Language Models (VLMs) have received significant attention in recent years in the robotics community. VLMs are shown to be able to perform complex visual reasoning and scene understanding tasks, which makes them regarded as a potential universal solution for general robotics problems such as manipulation and navigation. However, previous VLMs for robotics such as RT-1, RT-2, and ManipLLM have focused on directly learning robot-centric actions. Such approaches require collecting a significant amount of robot interaction data, which is extremely costly in the real world. Thus, we propose A3VLM, an object-centric, actionable, articulation-aware vision language model. A3VLM focuses on the articulation structure and action affordances of objects. Its representation is robot-agnostic and can be translated into robot actions using simple action primitives. Extensive experiments in both simulation benchmarks and real-world settings demonstrate the effectiveness and stability of A3VLM. We release our code and other materials at https://github.com/changhaonan/A3VLM.

## 核心内容
Vision Language Models (VLMs) have received significant attention in recent years in the robotics community. VLMs are shown to be able to perform complex visual reasoning and scene understanding tasks, which makes them regarded as a potential universal solution for general robotics problems such as manipulation and navigation. However, previous VLMs for robotics such as RT-1, RT-2, and ManipLLM have focused on directly learning robot-centric actions. Such approaches require collecting a significant amount of robot interaction data, which is extremely costly in the real world. Thus, we propose A3VLM, an object-centric, actionable, articulation-aware vision language model. A3VLM focuses on the articulation structure and action affordances of objects. Its representation is robot-agnostic and can be translated into robot actions using simple action primitives. Extensive experiments in both simulation benchmarks and real-world settings demonstrate the effectiveness and stability of A3VLM. We release our code and other materials at https://github.com/changhaonan/A3VLM.

## 参考
- http://arxiv.org/abs/2406.07549v2

## Overview
Vision Language Models (VLMs) have received significant attention in recent years in the robotics community. VLMs are shown to be able to perform complex visual reasoning and scene understanding tasks, which makes them regarded as a potential universal solution for general robotics problems such as manipulation and navigation. However, previous VLMs for robotics such as RT-1, RT-2, and ManipLLM have focused on directly learning robot-centric actions. Such approaches require collecting a significant amount of robot interaction data, which is extremely costly in the real world. Thus, we propose A3VLM, an object-centric, actionable, articulation-aware vision language model. A3VLM focuses on the articulation structure and action affordances of objects. Its representation is robot-agnostic and can be translated into robot actions using simple action primitives. Extensive experiments in both simulation benchmarks and real-world settings demonstrate the effectiveness and stability of A3VLM. We release our code and other materials at https://github.com/changhaonan/A3VLM.

## Content
Vision Language Models (VLMs) have received significant attention in recent years in the robotics community. VLMs are shown to be able to perform complex visual reasoning and scene understanding tasks, which makes them regarded as a potential universal solution for general robotics problems such as manipulation and navigation. However, previous VLMs for robotics such as RT-1, RT-2, and ManipLLM have focused on directly learning robot-centric actions. Such approaches require collecting a significant amount of robot interaction data, which is extremely costly in the real world. Thus, we propose A3VLM, an object-centric, actionable, articulation-aware vision language model. A3VLM focuses on the articulation structure and action affordances of objects. Its representation is robot-agnostic and can be translated into robot actions using simple action primitives. Extensive experiments in both simulation benchmarks and real-world settings demonstrate the effectiveness and stability of A3VLM. We release our code and other materials at https://github.com/changhaonan/A3VLM.

## 개요
Vision Language Models(VLM)은 최근 로봇 공학 커뮤니티에서 큰 주목을 받고 있습니다. VLM은 복잡한 시각적 추론 및 장면 이해 작업을 수행할 수 있는 것으로 입증되었으며, 이는 조작 및 내비게이션과 같은 일반 로봇 공학 문제에 대한 잠재적인 보편적 솔루션으로 간주됩니다. 그러나 RT-1, RT-2, ManipLLM과 같은 이전의 로봇 공학용 VLM은 로봇 중심의 동작을 직접 학습하는 데 초점을 맞추었습니다. 이러한 접근 방식은 상당한 양의 로봇 상호작용 데이터를 수집해야 하며, 이는 실제 환경에서 매우 비용이 많이 듭니다. 따라서 우리는 객체 중심적이고 실행 가능하며 관절 구조를 인식하는 비전 언어 모델인 A3VLM을 제안합니다. A3VLM은 객체의 관절 구조와 동작 가능성(action affordances)에 초점을 맞춥니다. 그 표현은 로봇에 구애받지 않으며(robot-agnostic), 간단한 동작 프리미티브를 사용하여 로봇 동작으로 변환될 수 있습니다. 시뮬레이션 벤치마크와 실제 환경 모두에서의 광범위한 실험을 통해 A3VLM의 효과성과 안정성이 입증되었습니다. 코드 및 기타 자료는 https://github.com/changhaonan/A3VLM에서 공개합니다.

## 핵심 내용
Vision Language Models(VLM)은 최근 로봇 공학 커뮤니티에서 큰 주목을 받고 있습니다. VLM은 복잡한 시각적 추론 및 장면 이해 작업을 수행할 수 있는 것으로 입증되었으며, 이는 조작 및 내비게이션과 같은 일반 로봇 공학 문제에 대한 잠재적인 보편적 솔루션으로 간주됩니다. 그러나 RT-1, RT-2, ManipLLM과 같은 이전의 로봇 공학용 VLM은 로봇 중심의 동작을 직접 학습하는 데 초점을 맞추었습니다. 이러한 접근 방식은 상당한 양의 로봇 상호작용 데이터를 수집해야 하며, 이는 실제 환경에서 매우 비용이 많이 듭니다. 따라서 우리는 객체 중심적이고 실행 가능하며 관절 구조를 인식하는 비전 언어 모델인 A3VLM을 제안합니다. A3VLM은 객체의 관절 구조와 동작 가능성(action affordances)에 초점을 맞춥니다. 그 표현은 로봇에 구애받지 않으며(robot-agnostic), 간단한 동작 프리미티브를 사용하여 로봇 동작으로 변환될 수 있습니다. 시뮬레이션 벤치마크와 실제 환경 모두에서의 광범위한 실험을 통해 A3VLM의 효과성과 안정성이 입증되었습니다. 코드 및 기타 자료는 https://github.com/changhaonan/A3VLM에서 공개합니다.
