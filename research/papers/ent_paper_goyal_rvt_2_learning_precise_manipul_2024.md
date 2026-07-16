---
$id: ent_paper_goyal_rvt_2_learning_precise_manipul_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RVT-2: Learning Precise Manipulation from Few Demonstrations'
  zh: RVT-2
  ko: 'RVT-2: Learning Precise Manipulation from Few Demonstrations'
summary:
  en: 'RVT-2: Learning Precise Manipulation from Few Demonstrations (RVT-2), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, and published at Robotics - Science and Systems 2024.'
  zh: 'RVT-2: Learning Precise Manipulation from Few Demonstrations (RVT-2), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, and published at Robotics - Science and Systems 2024.'
  ko: 'RVT-2: Learning Precise Manipulation from Few Demonstrations (RVT-2), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, and published at Robotics - Science and Systems 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- rvt_2
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.08545v1.
sources:
- id: src_001
  type: website
  title: RVT-2 source
  url: https://doi.org/10.15607/RSS.2024.XX.055
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
In this work, we study how to build a robotic system that can solve multiple 3D manipulation tasks given language instructions. To be useful in industrial and household domains, such a system should be capable of learning new tasks with few demonstrations and solving them precisely. Prior works, like PerAct and RVT, have studied this problem, however, they often struggle with tasks requiring high precision. We study how to make them more effective, precise, and fast. Using a combination of architectural and system-level improvements, we propose RVT-2, a multitask 3D manipulation model that is 6X faster in training and 2X faster in inference than its predecessor RVT. RVT-2 achieves a new state-of-the-art on RLBench, improving the success rate from 65% to 82%. RVT-2 is also effective in the real world, where it can learn tasks requiring high precision, like picking up and inserting plugs, with just 10 demonstrations. Visual results, code, and trained model are provided at: https://robotic-view-transformer-2.github.io/.

## 核心内容
In this work, we study how to build a robotic system that can solve multiple 3D manipulation tasks given language instructions. To be useful in industrial and household domains, such a system should be capable of learning new tasks with few demonstrations and solving them precisely. Prior works, like PerAct and RVT, have studied this problem, however, they often struggle with tasks requiring high precision. We study how to make them more effective, precise, and fast. Using a combination of architectural and system-level improvements, we propose RVT-2, a multitask 3D manipulation model that is 6X faster in training and 2X faster in inference than its predecessor RVT. RVT-2 achieves a new state-of-the-art on RLBench, improving the success rate from 65% to 82%. RVT-2 is also effective in the real world, where it can learn tasks requiring high precision, like picking up and inserting plugs, with just 10 demonstrations. Visual results, code, and trained model are provided at: https://robotic-view-transformer-2.github.io/.

## 参考
- http://arxiv.org/abs/2406.08545v1

## Overview
In this work, we study how to build a robotic system that can solve multiple 3D manipulation tasks given language instructions. To be useful in industrial and household domains, such a system should be capable of learning new tasks with few demonstrations and solving them precisely. Prior works, like PerAct and RVT, have studied this problem, however, they often struggle with tasks requiring high precision. We study how to make them more effective, precise, and fast. Using a combination of architectural and system-level improvements, we propose RVT-2, a multitask 3D manipulation model that is 6X faster in training and 2X faster in inference than its predecessor RVT. RVT-2 achieves a new state-of-the-art on RLBench, improving the success rate from 65% to 82%. RVT-2 is also effective in the real world, where it can learn tasks requiring high precision, like picking up and inserting plugs, with just 10 demonstrations. Visual results, code, and trained model are provided at: https://robotic-view-transformer-2.github.io/.

## Content
In this work, we study how to build a robotic system that can solve multiple 3D manipulation tasks given language instructions. To be useful in industrial and household domains, such a system should be capable of learning new tasks with few demonstrations and solving them precisely. Prior works, like PerAct and RVT, have studied this problem, however, they often struggle with tasks requiring high precision. We study how to make them more effective, precise, and fast. Using a combination of architectural and system-level improvements, we propose RVT-2, a multitask 3D manipulation model that is 6X faster in training and 2X faster in inference than its predecessor RVT. RVT-2 achieves a new state-of-the-art on RLBench, improving the success rate from 65% to 82%. RVT-2 is also effective in the real world, where it can learn tasks requiring high precision, like picking up and inserting plugs, with just 10 demonstrations. Visual results, code, and trained model are provided at: https://robotic-view-transformer-2.github.io/.

## 개요
본 연구에서는 언어 명령을 기반으로 여러 3D 조작 작업을 해결할 수 있는 로봇 시스템을 구축하는 방법을 연구합니다. 산업 및 가정 환경에서 유용하게 사용되기 위해서는 이러한 시스템이 적은 시연으로 새로운 작업을 학습하고 정밀하게 수행할 수 있어야 합니다. PerAct 및 RVT와 같은 이전 연구들에서 이 문제를 다루었지만, 높은 정밀도를 요구하는 작업에서는 종종 어려움을 겪었습니다. 본 연구에서는 이를 더 효과적이고 정밀하며 빠르게 만드는 방법을 탐구합니다. 아키텍처 및 시스템 수준의 개선을 결합하여, 이전 모델인 RVT보다 학습 속도가 6배, 추론 속도가 2배 빠른 멀티태스크 3D 조작 모델인 RVT-2를 제안합니다. RVT-2는 RLBench에서 새로운 최첨단 성능을 달성하여 성공률을 65%에서 82%로 향상시켰습니다. 또한 RVT-2는 실제 환경에서도 효과적이며, 플러그 집기 및 삽입과 같은 높은 정밀도를 요구하는 작업을 단 10회의 시연만으로 학습할 수 있습니다. 시각적 결과, 코드 및 학습된 모델은 다음에서 확인할 수 있습니다: https://robotic-view-transformer-2.github.io/.

## 핵심 내용
본 연구에서는 언어 명령을 기반으로 여러 3D 조작 작업을 해결할 수 있는 로봇 시스템을 구축하는 방법을 연구합니다. 산업 및 가정 환경에서 유용하게 사용되기 위해서는 이러한 시스템이 적은 시연으로 새로운 작업을 학습하고 정밀하게 수행할 수 있어야 합니다. PerAct 및 RVT와 같은 이전 연구들에서 이 문제를 다루었지만, 높은 정밀도를 요구하는 작업에서는 종종 어려움을 겪었습니다. 본 연구에서는 이를 더 효과적이고 정밀하며 빠르게 만드는 방법을 탐구합니다. 아키텍처 및 시스템 수준의 개선을 결합하여, 이전 모델인 RVT보다 학습 속도가 6배, 추론 속도가 2배 빠른 멀티태스크 3D 조작 모델인 RVT-2를 제안합니다. RVT-2는 RLBench에서 새로운 최첨단 성능을 달성하여 성공률을 65%에서 82%로 향상시켰습니다. 또한 RVT-2는 실제 환경에서도 효과적이며, 플러그 집기 및 삽입과 같은 높은 정밀도를 요구하는 작업을 단 10회의 시연만으로 학습할 수 있습니다. 시각적 결과, 코드 및 학습된 모델은 다음에서 확인할 수 있습니다: https://robotic-view-transformer-2.github.io/.
