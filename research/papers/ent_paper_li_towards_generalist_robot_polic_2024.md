---
$id: ent_paper_li_towards_generalist_robot_polic_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models'
  zh: RoboVLMs
  ko: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models'
summary:
  en: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models (RoboVLMs), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua University, ByteDance Research, CASIA MAIS-NLPR,
    Shanghai Jiao Tong University, National University of Singapore.'
  zh: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models (RoboVLMs), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua University, ByteDance Research, CASIA MAIS-NLPR,
    Shanghai Jiao Tong University, National University of Singapore.'
  ko: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models (RoboVLMs), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua University, ByteDance Research, CASIA MAIS-NLPR,
    Shanghai Jiao Tong University, National University of Singapore.'
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
- robovlms
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.14058v4.
sources:
- id: src_001
  type: paper
  title: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2412.14058
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboVLMs source
  url: https://doi.org/10.48550/arXiv.2412.14058
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
To utilize Foundation Vision Language Models (VLMs) for robotic tasks and motion planning, the community has proposed different methods for injecting action components into VLMs and building the Vision-Language-Action models (VLAs). In this work, we disclose the key factors that significantly influence the performance of VLA on robot manipulation problems and focus on answering three essential design choices: which backbone to select, how to formulate the VLA architectures, and when to add cross-embodiment data. The obtained results convince us firmly to explain why we prefer VLA and develop a new family of VLAs, RoboVLMs, which require very few manual designs and achieve a new state-of-the-art performance in three simulation tasks and real-world experiments. Through our extensive experiments, which include over 8 VLM backbones, 4 policy architectures, and over 600 distinct designed experiments, we provide a detailed guidebook for the future design of VLAs. In addition to the study, the highly flexible RoboVLMs framework, which supports easy integrations of new VLMs and free combinations of various design choices, is made public to facilitate future research. We open-source all details, including codes, models, datasets, and toolkits, along with detailed training and evaluation recipes at: robovlms.github.io.

## 核心内容
To utilize Foundation Vision Language Models (VLMs) for robotic tasks and motion planning, the community has proposed different methods for injecting action components into VLMs and building the Vision-Language-Action models (VLAs). In this work, we disclose the key factors that significantly influence the performance of VLA on robot manipulation problems and focus on answering three essential design choices: which backbone to select, how to formulate the VLA architectures, and when to add cross-embodiment data. The obtained results convince us firmly to explain why we prefer VLA and develop a new family of VLAs, RoboVLMs, which require very few manual designs and achieve a new state-of-the-art performance in three simulation tasks and real-world experiments. Through our extensive experiments, which include over 8 VLM backbones, 4 policy architectures, and over 600 distinct designed experiments, we provide a detailed guidebook for the future design of VLAs. In addition to the study, the highly flexible RoboVLMs framework, which supports easy integrations of new VLMs and free combinations of various design choices, is made public to facilitate future research. We open-source all details, including codes, models, datasets, and toolkits, along with detailed training and evaluation recipes at: robovlms.github.io.

## 参考
- http://arxiv.org/abs/2412.14058v4

## Overview
To utilize Foundation Vision Language Models (VLMs) for robotic tasks and motion planning, the community has proposed different methods for injecting action components into VLMs and building the Vision-Language-Action models (VLAs). In this work, we disclose the key factors that significantly influence the performance of VLA on robot manipulation problems and focus on answering three essential design choices: which backbone to select, how to formulate the VLA architectures, and when to add cross-embodiment data. The obtained results convince us firmly to explain why we prefer VLA and develop a new family of VLAs, RoboVLMs, which require very few manual designs and achieve a new state-of-the-art performance in three simulation tasks and real-world experiments. Through our extensive experiments, which include over 8 VLM backbones, 4 policy architectures, and over 600 distinct designed experiments, we provide a detailed guidebook for the future design of VLAs. In addition to the study, the highly flexible RoboVLMs framework, which supports easy integrations of new VLMs and free combinations of various design choices, is made public to facilitate future research. We open-source all details, including codes, models, datasets, and toolkits, along with detailed training and evaluation recipes at: robovlms.github.io.

## Content
To utilize Foundation Vision Language Models (VLMs) for robotic tasks and motion planning, the community has proposed different methods for injecting action components into VLMs and building the Vision-Language-Action models (VLAs). In this work, we disclose the key factors that significantly influence the performance of VLA on robot manipulation problems and focus on answering three essential design choices: which backbone to select, how to formulate the VLA architectures, and when to add cross-embodiment data. The obtained results convince us firmly to explain why we prefer VLA and develop a new family of VLAs, RoboVLMs, which require very few manual designs and achieve a new state-of-the-art performance in three simulation tasks and real-world experiments. Through our extensive experiments, which include over 8 VLM backbones, 4 policy architectures, and over 600 distinct designed experiments, we provide a detailed guidebook for the future design of VLAs. In addition to the study, the highly flexible RoboVLMs framework, which supports easy integrations of new VLMs and free combinations of various design choices, is made public to facilitate future research. We open-source all details, including codes, models, datasets, and toolkits, along with detailed training and evaluation recipes at: robovlms.github.io.

## 개요
로봇 작업 및 동작 계획을 위해 Foundation Vision Language Models(VLM)을 활용하기 위해, 연구 커뮤니티는 VLM에 행동 구성 요소를 주입하고 Vision-Language-Action 모델(VLA)을 구축하는 다양한 방법을 제안해 왔습니다. 본 연구에서는 로봇 조작 문제에서 VLA 성능에 큰 영향을 미치는 핵심 요소를 공개하고, 세 가지 필수 설계 선택 사항(어떤 백본을 선택할지, VLA 아키텍처를 어떻게 구성할지, 언제 교차 구현 데이터를 추가할지)에 대한 답변에 초점을 맞춥니다. 얻은 결과는 VLA를 선호하는 이유를 설명하고, 수동 설계가 거의 필요 없으며 세 가지 시뮬레이션 작업과 실제 실험에서 새로운 최첨단 성능을 달성하는 새로운 VLA 계열인 RoboVLMs를 개발하게 된 확신을 굳건히 해줍니다. 8개 이상의 VLM 백본, 4개의 정책 아키텍처, 600개 이상의 개별 설계 실험을 포함한 광범위한 실험을 통해, 우리는 향후 VLA 설계를 위한 상세한 가이드북을 제공합니다. 연구 외에도, 새로운 VLM의 쉬운 통합과 다양한 설계 선택의 자유로운 조합을 지원하는 매우 유연한 RoboVLMs 프레임워크를 공개하여 향후 연구를 촉진합니다. 코드, 모델, 데이터셋, 툴킷을 포함한 모든 세부 사항과 상세한 학습 및 평가 레시피를 robovlms.github.io에서 오픈소스로 제공합니다.

## 핵심 내용
로봇 작업 및 동작 계획을 위해 Foundation Vision Language Models(VLM)을 활용하기 위해, 연구 커뮤니티는 VLM에 행동 구성 요소를 주입하고 Vision-Language-Action 모델(VLA)을 구축하는 다양한 방법을 제안해 왔습니다. 본 연구에서는 로봇 조작 문제에서 VLA 성능에 큰 영향을 미치는 핵심 요소를 공개하고, 세 가지 필수 설계 선택 사항(어떤 백본을 선택할지, VLA 아키텍처를 어떻게 구성할지, 언제 교차 구현 데이터를 추가할지)에 대한 답변에 초점을 맞춥니다. 얻은 결과는 VLA를 선호하는 이유를 설명하고, 수동 설계가 거의 필요 없으며 세 가지 시뮬레이션 작업과 실제 실험에서 새로운 최첨단 성능을 달성하는 새로운 VLA 계열인 RoboVLMs를 개발하게 된 확신을 굳건히 해줍니다. 8개 이상의 VLM 백본, 4개의 정책 아키텍처, 600개 이상의 개별 설계 실험을 포함한 광범위한 실험을 통해, 우리는 향후 VLA 설계를 위한 상세한 가이드북을 제공합니다. 연구 외에도, 새로운 VLM의 쉬운 통합과 다양한 설계 선택의 자유로운 조합을 지원하는 매우 유연한 RoboVLMs 프레임워크를 공개하여 향후 연구를 촉진합니다. 코드, 모델, 데이터셋, 툴킷을 포함한 모든 세부 사항과 상세한 학습 및 평가 레시피를 robovlms.github.io에서 오픈소스로 제공합니다.
