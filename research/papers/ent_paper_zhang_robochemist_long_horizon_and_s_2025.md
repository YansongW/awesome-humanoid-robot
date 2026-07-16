---
$id: ent_paper_zhang_robochemist_long_horizon_and_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation'
  zh: RoboChemist
  ko: 'RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation'
summary:
  en: 'RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation (RoboChemist), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, and published at CoRL25.'
  zh: 'RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation (RoboChemist), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, and published at CoRL25.'
  ko: 'RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation (RoboChemist), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, and published at CoRL25.'
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
- robochemist
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.08820v1.
sources:
- id: src_001
  type: paper
  title: 'RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation (arXiv)'
  url: https://arxiv.org/abs/2509.08820
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboChemist source
  url: https://doi.org/10.48550/arXiv.2509.08820
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robotic chemists promise to both liberate human experts from repetitive tasks and accelerate scientific discovery, yet remain in their infancy. Chemical experiments involve long-horizon procedures over hazardous and deformable substances, where success requires not only task completion but also strict compliance with experimental norms. To address these challenges, we propose \textit{RoboChemist}, a dual-loop framework that integrates Vision-Language Models (VLMs) with Vision-Language-Action (VLA) models. Unlike prior VLM-based systems (e.g., VoxPoser, ReKep) that rely on depth perception and struggle with transparent labware, and existing VLA systems (e.g., RDT, pi0) that lack semantic-level feedback for complex tasks, our method leverages a VLM to serve as (1) a planner to decompose tasks into primitive actions, (2) a visual prompt generator to guide VLA models, and (3) a monitor to assess task success and regulatory compliance. Notably, we introduce a VLA interface that accepts image-based visual targets from the VLM, enabling precise, goal-conditioned control. Our system successfully executes both primitive actions and complete multi-step chemistry protocols. Results show 23.57% higher average success rate and a 0.298 average increase in compliance rate over state-of-the-art VLA baselines, while also demonstrating strong generalization to objects and tasks.

## 核心内容
Robotic chemists promise to both liberate human experts from repetitive tasks and accelerate scientific discovery, yet remain in their infancy. Chemical experiments involve long-horizon procedures over hazardous and deformable substances, where success requires not only task completion but also strict compliance with experimental norms. To address these challenges, we propose \textit{RoboChemist}, a dual-loop framework that integrates Vision-Language Models (VLMs) with Vision-Language-Action (VLA) models. Unlike prior VLM-based systems (e.g., VoxPoser, ReKep) that rely on depth perception and struggle with transparent labware, and existing VLA systems (e.g., RDT, pi0) that lack semantic-level feedback for complex tasks, our method leverages a VLM to serve as (1) a planner to decompose tasks into primitive actions, (2) a visual prompt generator to guide VLA models, and (3) a monitor to assess task success and regulatory compliance. Notably, we introduce a VLA interface that accepts image-based visual targets from the VLM, enabling precise, goal-conditioned control. Our system successfully executes both primitive actions and complete multi-step chemistry protocols. Results show 23.57% higher average success rate and a 0.298 average increase in compliance rate over state-of-the-art VLA baselines, while also demonstrating strong generalization to objects and tasks.

## 参考
- http://arxiv.org/abs/2509.08820v1

## Overview
Robotic chemists promise to both liberate human experts from repetitive tasks and accelerate scientific discovery, yet remain in their infancy. Chemical experiments involve long-horizon procedures over hazardous and deformable substances, where success requires not only task completion but also strict compliance with experimental norms. To address these challenges, we propose \textit{RoboChemist}, a dual-loop framework that integrates Vision-Language Models (VLMs) with Vision-Language-Action (VLA) models. Unlike prior VLM-based systems (e.g., VoxPoser, ReKep) that rely on depth perception and struggle with transparent labware, and existing VLA systems (e.g., RDT, pi0) that lack semantic-level feedback for complex tasks, our method leverages a VLM to serve as (1) a planner to decompose tasks into primitive actions, (2) a visual prompt generator to guide VLA models, and (3) a monitor to assess task success and regulatory compliance. Notably, we introduce a VLA interface that accepts image-based visual targets from the VLM, enabling precise, goal-conditioned control. Our system successfully executes both primitive actions and complete multi-step chemistry protocols. Results show 23.57% higher average success rate and a 0.298 average increase in compliance rate over state-of-the-art VLA baselines, while also demonstrating strong generalization to objects and tasks.

## Content
Robotic chemists promise to both liberate human experts from repetitive tasks and accelerate scientific discovery, yet remain in their infancy. Chemical experiments involve long-horizon procedures over hazardous and deformable substances, where success requires not only task completion but also strict compliance with experimental norms. To address these challenges, we propose \textit{RoboChemist}, a dual-loop framework that integrates Vision-Language Models (VLMs) with Vision-Language-Action (VLA) models. Unlike prior VLM-based systems (e.g., VoxPoser, ReKep) that rely on depth perception and struggle with transparent labware, and existing VLA systems (e.g., RDT, pi0) that lack semantic-level feedback for complex tasks, our method leverages a VLM to serve as (1) a planner to decompose tasks into primitive actions, (2) a visual prompt generator to guide VLA models, and (3) a monitor to assess task success and regulatory compliance. Notably, we introduce a VLA interface that accepts image-based visual targets from the VLM, enabling precise, goal-conditioned control. Our system successfully executes both primitive actions and complete multi-step chemistry protocols. Results show 23.57% higher average success rate and a 0.298 average increase in compliance rate over state-of-the-art VLA baselines, while also demonstrating strong generalization to objects and tasks.

## 개요
로봇 화학자는 인간 전문가를 반복적인 작업에서 해방시키고 과학적 발견을 가속화할 것을 약속하지만, 아직 초기 단계에 머물러 있습니다. 화학 실험은 위험하고 변형 가능한 물질을 다루는 장기적인 절차를 포함하며, 성공을 위해서는 작업 완료뿐만 아니라 실험 규범을 엄격히 준수해야 합니다. 이러한 과제를 해결하기 위해, 우리는 Vision-Language Models(VLM)과 Vision-Language-Action(VLA) 모델을 통합한 이중 루프 프레임워크인 \textit{RoboChemist}를 제안합니다. 깊이 인식에 의존하고 투명한 실험 도구에 어려움을 겪는 기존 VLM 기반 시스템(예: VoxPoser, ReKep)과 복잡한 작업에 대한 의미 수준의 피드백이 부족한 기존 VLA 시스템(예: RDT, pi0)과 달리, 우리의 방법은 VLM을 (1) 작업을 기본 동작으로 분해하는 계획자, (2) VLA 모델을 안내하는 시각적 프롬프트 생성기, (3) 작업 성공 및 규정 준수를 평가하는 모니터로 활용합니다. 특히, 우리는 VLM의 이미지 기반 시각적 목표를 수용하는 VLA 인터페이스를 도입하여 정밀하고 목표 조건화된 제어를 가능하게 합니다. 우리 시스템은 기본 동작과 완전한 다단계 화학 프로토콜을 모두 성공적으로 실행합니다. 결과는 최신 VLA 기준선 대비 평균 성공률이 23.57% 더 높고, 준수율이 평균 0.298 증가했으며, 객체와 작업에 대한 강력한 일반화 능력을 보여줍니다.

## 핵심 내용
로봇 화학자는 인간 전문가를 반복적인 작업에서 해방시키고 과학적 발견을 가속화할 것을 약속하지만, 아직 초기 단계에 머물러 있습니다. 화학 실험은 위험하고 변형 가능한 물질을 다루는 장기적인 절차를 포함하며, 성공을 위해서는 작업 완료뿐만 아니라 실험 규범을 엄격히 준수해야 합니다. 이러한 과제를 해결하기 위해, 우리는 Vision-Language Models(VLM)과 Vision-Language-Action(VLA) 모델을 통합한 이중 루프 프레임워크인 \textit{RoboChemist}를 제안합니다. 깊이 인식에 의존하고 투명한 실험 도구에 어려움을 겪는 기존 VLM 기반 시스템(예: VoxPoser, ReKep)과 복잡한 작업에 대한 의미 수준의 피드백이 부족한 기존 VLA 시스템(예: RDT, pi0)과 달리, 우리의 방법은 VLM을 (1) 작업을 기본 동작으로 분해하는 계획자, (2) VLA 모델을 안내하는 시각적 프롬프트 생성기, (3) 작업 성공 및 규정 준수를 평가하는 모니터로 활용합니다. 특히, 우리는 VLM의 이미지 기반 시각적 목표를 수용하는 VLA 인터페이스를 도입하여 정밀하고 목표 조건화된 제어를 가능하게 합니다. 우리 시스템은 기본 동작과 완전한 다단계 화학 프로토콜을 모두 성공적으로 실행합니다. 결과는 최신 VLA 기준선 대비 평균 성공률이 23.57% 더 높고, 준수율이 평균 0.298 증가했으며, 객체와 작업에 대한 강력한 일반화 능력을 보여줍니다.
