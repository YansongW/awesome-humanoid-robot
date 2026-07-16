---
$id: ent_paper_learning_visuotactile_skills_w_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Visuotactile Skills with Two Multifingered Hands
  zh: Learning Visuotactile Skills with Two Multifingered Hands
  ko: Learning Visuotactile Skills with Two Multifingered Hands
summary:
  en: Learning Visuotactile Skills with Two Multifingered Hands is a 2024 work on manipulation for humanoid robots, with open-source
    code available.
  zh: Learning Visuotactile Skills with Two Multifingered Hands is a 2024 work on manipulation for humanoid robots, with open-source
    code available.
  ko: Learning Visuotactile Skills with Two Multifingered Hands is a 2024 work on manipulation for humanoid robots, with open-source
    code available.
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
- learning_visuotactile_skills_w
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2404.16823v2.
sources:
- id: src_001
  type: paper
  title: Learning Visuotactile Skills with Two Multifingered Hands (arXiv)
  url: https://arxiv.org/abs/2404.16823
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Learning Visuotactile Skills with Two Multifingered Hands project page
  url: https://toruowo.github.io/hato/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Aiming to replicate human-like dexterity, perceptual experiences, and motion patterns, we explore learning from human demonstrations using a bimanual system with multifingered hands and visuotactile data. Two significant challenges exist: the lack of an affordable and accessible teleoperation system suitable for a dual-arm setup with multifingered hands, and the scarcity of multifingered hand hardware equipped with touch sensing. To tackle the first challenge, we develop HATO, a low-cost hands-arms teleoperation system that leverages off-the-shelf electronics, complemented with a software suite that enables efficient data collection; the comprehensive software suite also supports multimodal data processing, scalable policy learning, and smooth policy deployment. To tackle the latter challenge, we introduce a novel hardware adaptation by repurposing two prosthetic hands equipped with touch sensors for research. Using visuotactile data collected from our system, we learn skills to complete long-horizon, high-precision tasks which are difficult to achieve without multifingered dexterity and touch feedback. Furthermore, we empirically investigate the effects of dataset size, sensing modality, and visual input preprocessing on policy learning. Our results mark a promising step forward in bimanual multifingered manipulation from visuotactile data. Videos, code, and datasets can be found at https://toruowo.github.io/hato/ .

## 核心内容
Aiming to replicate human-like dexterity, perceptual experiences, and motion patterns, we explore learning from human demonstrations using a bimanual system with multifingered hands and visuotactile data. Two significant challenges exist: the lack of an affordable and accessible teleoperation system suitable for a dual-arm setup with multifingered hands, and the scarcity of multifingered hand hardware equipped with touch sensing. To tackle the first challenge, we develop HATO, a low-cost hands-arms teleoperation system that leverages off-the-shelf electronics, complemented with a software suite that enables efficient data collection; the comprehensive software suite also supports multimodal data processing, scalable policy learning, and smooth policy deployment. To tackle the latter challenge, we introduce a novel hardware adaptation by repurposing two prosthetic hands equipped with touch sensors for research. Using visuotactile data collected from our system, we learn skills to complete long-horizon, high-precision tasks which are difficult to achieve without multifingered dexterity and touch feedback. Furthermore, we empirically investigate the effects of dataset size, sensing modality, and visual input preprocessing on policy learning. Our results mark a promising step forward in bimanual multifingered manipulation from visuotactile data. Videos, code, and datasets can be found at https://toruowo.github.io/hato/ .

## 参考
- http://arxiv.org/abs/2404.16823v2

## Overview
Aiming to replicate human-like dexterity, perceptual experiences, and motion patterns, we explore learning from human demonstrations using a bimanual system with multifingered hands and visuotactile data. Two significant challenges exist: the lack of an affordable and accessible teleoperation system suitable for a dual-arm setup with multifingered hands, and the scarcity of multifingered hand hardware equipped with touch sensing. To tackle the first challenge, we develop HATO, a low-cost hands-arms teleoperation system that leverages off-the-shelf electronics, complemented with a software suite that enables efficient data collection; the comprehensive software suite also supports multimodal data processing, scalable policy learning, and smooth policy deployment. To tackle the latter challenge, we introduce a novel hardware adaptation by repurposing two prosthetic hands equipped with touch sensors for research. Using visuotactile data collected from our system, we learn skills to complete long-horizon, high-precision tasks which are difficult to achieve without multifingered dexterity and touch feedback. Furthermore, we empirically investigate the effects of dataset size, sensing modality, and visual input preprocessing on policy learning. Our results mark a promising step forward in bimanual multifingered manipulation from visuotactile data. Videos, code, and datasets can be found at https://toruowo.github.io/hato/ .

## Content
Aiming to replicate human-like dexterity, perceptual experiences, and motion patterns, we explore learning from human demonstrations using a bimanual system with multifingered hands and visuotactile data. Two significant challenges exist: the lack of an affordable and accessible teleoperation system suitable for a dual-arm setup with multifingered hands, and the scarcity of multifingered hand hardware equipped with touch sensing. To tackle the first challenge, we develop HATO, a low-cost hands-arms teleoperation system that leverages off-the-shelf electronics, complemented with a software suite that enables efficient data collection; the comprehensive software suite also supports multimodal data processing, scalable policy learning, and smooth policy deployment. To tackle the latter challenge, we introduce a novel hardware adaptation by repurposing two prosthetic hands equipped with touch sensors for research. Using visuotactile data collected from our system, we learn skills to complete long-horizon, high-precision tasks which are difficult to achieve without multifingered dexterity and touch feedback. Furthermore, we empirically investigate the effects of dataset size, sensing modality, and visual input preprocessing on policy learning. Our results mark a promising step forward in bimanual multifingered manipulation from visuotactile data. Videos, code, and datasets can be found at https://toruowo.github.io/hato/ .

## 개요
인간과 유사한 손재주, 지각 경험 및 움직임 패턴을 재현하는 것을 목표로, 우리는 다지 손과 시각-촉각 데이터를 갖춘 양손 시스템을 사용하여 인간 시연으로부터 학습하는 방법을 탐구합니다. 두 가지 주요 과제가 존재합니다: 다지 손을 갖춘 이중 팔 설정에 적합한 저렴하고 접근 가능한 원격 조작 시스템의 부족, 그리고 촉각 감지 기능이 장착된 다지 손 하드웨어의 희소성입니다. 첫 번째 과제를 해결하기 위해, 우리는 기성 전자 부품을 활용한 저비용 손-팔 원격 조작 시스템인 HATO를 개발하고, 효율적인 데이터 수집을 가능하게 하는 소프트웨어 제품군을 함께 제공합니다. 이 포괄적인 소프트웨어 제품군은 다중 모드 데이터 처리, 확장 가능한 정책 학습, 그리고 원활한 정책 배포도 지원합니다. 두 번째 과제를 해결하기 위해, 우리는 연구 목적으로 촉각 센서가 장착된 두 개의 의수(prosthetic hand)를 재활용하는 새로운 하드웨어 적응 방식을 도입합니다. 우리 시스템에서 수집된 시각-촉각 데이터를 사용하여, 다지 손재주와 촉각 피드백 없이는 달성하기 어려운 장기적이고 고정밀 작업을 완료하는 기술을 학습합니다. 또한, 데이터 세트 크기, 감지 양식, 그리고 시각 입력 전처리가 정책 학습에 미치는 영향을 실증적으로 조사합니다. 우리의 결과는 시각-촉각 데이터를 활용한 양손 다지 조작 분야에서 유망한 진전을 의미합니다. 비디오, 코드 및 데이터 세트는 https://toruowo.github.io/hato/ 에서 확인할 수 있습니다.

## 핵심 내용
인간과 유사한 손재주, 지각 경험 및 움직임 패턴을 재현하는 것을 목표로, 우리는 다지 손과 시각-촉각 데이터를 갖춘 양손 시스템을 사용하여 인간 시연으로부터 학습하는 방법을 탐구합니다. 두 가지 주요 과제가 존재합니다: 다지 손을 갖춘 이중 팔 설정에 적합한 저렴하고 접근 가능한 원격 조작 시스템의 부족, 그리고 촉각 감지 기능이 장착된 다지 손 하드웨어의 희소성입니다. 첫 번째 과제를 해결하기 위해, 우리는 기성 전자 부품을 활용한 저비용 손-팔 원격 조작 시스템인 HATO를 개발하고, 효율적인 데이터 수집을 가능하게 하는 소프트웨어 제품군을 함께 제공합니다. 이 포괄적인 소프트웨어 제품군은 다중 모드 데이터 처리, 확장 가능한 정책 학습, 그리고 원활한 정책 배포도 지원합니다. 두 번째 과제를 해결하기 위해, 우리는 연구 목적으로 촉각 센서가 장착된 두 개의 의수를 재활용하는 새로운 하드웨어 적응 방식을 도입합니다. 우리 시스템에서 수집된 시각-촉각 데이터를 사용하여, 다지 손재주와 촉각 피드백 없이는 달성하기 어려운 장기적이고 고정밀 작업을 완료하는 기술을 학습합니다. 또한, 데이터 세트 크기, 감지 양식, 그리고 시각 입력 전처리가 정책 학습에 미치는 영향을 실증적으로 조사합니다. 우리의 결과는 시각-촉각 데이터를 활용한 양손 다지 조작 분야에서 유망한 진전을 의미합니다. 비디오, 코드 및 데이터 세트는 https://toruowo.github.io/hato/ 에서 확인할 수 있습니다.
