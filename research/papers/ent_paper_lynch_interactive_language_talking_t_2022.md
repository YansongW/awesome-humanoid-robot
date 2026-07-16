---
$id: ent_paper_lynch_interactive_language_talking_t_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Interactive Language: Talking to Robots in Real Time'
  zh: Interactive Language
  ko: 'Interactive Language: Talking to Robots in Real Time'
summary:
  en: 'Interactive Language: Talking to Robots in Real Time (Interactive Language), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google.'
  zh: 'Interactive Language: Talking to Robots in Real Time (Interactive Language), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google.'
  ko: 'Interactive Language: Talking to Robots in Real Time (Interactive Language), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google.'
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
- interactive_language
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2210.06407v1.
sources:
- id: src_001
  type: paper
  title: 'Interactive Language: Talking to Robots in Real Time (arXiv)'
  url: https://arxiv.org/abs/2210.06407
  date: '2022'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Interactive Language source
  url: https://doi.org/10.48550/arXiv.2210.06407
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
We present a framework for building interactive, real-time, natural language-instructable robots in the real world, and we open source related assets (dataset, environment, benchmark, and policies). Trained with behavioral cloning on a dataset of hundreds of thousands of language-annotated trajectories, a produced policy can proficiently execute an order of magnitude more commands than previous works: specifically we estimate a 93.5% success rate on a set of 87,000 unique natural language strings specifying raw end-to-end visuo-linguo-motor skills in the real world. We find that the same policy is capable of being guided by a human via real-time language to address a wide range of precise long-horizon rearrangement goals, e.g. "make a smiley face out of blocks". The dataset we release comprises nearly 600,000 language-labeled trajectories, an order of magnitude larger than prior available datasets. We hope the demonstrated results and associated assets enable further advancement of helpful, capable, natural-language-interactable robots. See videos at https://interactive-language.github.io.

## 核心内容
We present a framework for building interactive, real-time, natural language-instructable robots in the real world, and we open source related assets (dataset, environment, benchmark, and policies). Trained with behavioral cloning on a dataset of hundreds of thousands of language-annotated trajectories, a produced policy can proficiently execute an order of magnitude more commands than previous works: specifically we estimate a 93.5% success rate on a set of 87,000 unique natural language strings specifying raw end-to-end visuo-linguo-motor skills in the real world. We find that the same policy is capable of being guided by a human via real-time language to address a wide range of precise long-horizon rearrangement goals, e.g. "make a smiley face out of blocks". The dataset we release comprises nearly 600,000 language-labeled trajectories, an order of magnitude larger than prior available datasets. We hope the demonstrated results and associated assets enable further advancement of helpful, capable, natural-language-interactable robots. See videos at https://interactive-language.github.io.

## 参考
- http://arxiv.org/abs/2210.06407v1

## Overview
We present a framework for building interactive, real-time, natural language-instructable robots in the real world, and we open source related assets (dataset, environment, benchmark, and policies). Trained with behavioral cloning on a dataset of hundreds of thousands of language-annotated trajectories, a produced policy can proficiently execute an order of magnitude more commands than previous works: specifically we estimate a 93.5% success rate on a set of 87,000 unique natural language strings specifying raw end-to-end visuo-linguo-motor skills in the real world. We find that the same policy is capable of being guided by a human via real-time language to address a wide range of precise long-horizon rearrangement goals, e.g. "make a smiley face out of blocks". The dataset we release comprises nearly 600,000 language-labeled trajectories, an order of magnitude larger than prior available datasets. We hope the demonstrated results and associated assets enable further advancement of helpful, capable, natural-language-interactable robots. See videos at https://interactive-language.github.io.

## Content
We present a framework for building interactive, real-time, natural language-instructable robots in the real world, and we open source related assets (dataset, environment, benchmark, and policies). Trained with behavioral cloning on a dataset of hundreds of thousands of language-annotated trajectories, a produced policy can proficiently execute an order of magnitude more commands than previous works: specifically we estimate a 93.5% success rate on a set of 87,000 unique natural language strings specifying raw end-to-end visuo-linguo-motor skills in the real world. We find that the same policy is capable of being guided by a human via real-time language to address a wide range of precise long-horizon rearrangement goals, e.g. "make a smiley face out of blocks". The dataset we release comprises nearly 600,000 language-labeled trajectories, an order of magnitude larger than prior available datasets. We hope the demonstrated results and associated assets enable further advancement of helpful, capable, natural-language-interactable robots. See videos at https://interactive-language.github.io.

## 개요
우리는 실제 세계에서 상호작용 가능하고 실시간으로 자연어 명령을 수행할 수 있는 로봇을 구축하기 위한 프레임워크를 제시하며, 관련 자산(데이터셋, 환경, 벤치마크, 정책)을 오픈소스로 공개합니다. 수십만 개의 언어 주석이 달린 궤적 데이터셋을 행동 복제(behavioral cloning)로 학습한 결과, 생성된 정책은 이전 연구보다 한 자릿수 더 많은 명령을 능숙하게 실행할 수 있습니다. 구체적으로, 실제 세계에서 원시적인 종단 간 시각-언어-운동 기술을 지정하는 87,000개의 고유 자연어 문자열 집합에 대해 93.5%의 성공률을 추정했습니다. 또한 동일한 정책이 인간의 실시간 언어 안내를 통해 "블록으로 웃는 얼굴 만들기"와 같은 다양한 정밀한 장기 재배치 목표를 처리할 수 있음을 발견했습니다. 공개하는 데이터셋은 약 600,000개의 언어 레이블이 지정된 궤적으로 구성되어 있으며, 이는 기존 데이터셋보다 한 자릿수 더 큽니다. 입증된 결과와 관련 자산이 유용하고 능력 있는 자연어 상호작용 로봇의 추가 발전을 가능하게 하길 바랍니다. 동영상은 https://interactive-language.github.io에서 확인하세요.

## 핵심 내용
우리는 실제 세계에서 상호작용 가능하고 실시간으로 자연어 명령을 수행할 수 있는 로봇을 구축하기 위한 프레임워크를 제시하며, 관련 자산(데이터셋, 환경, 벤치마크, 정책)을 오픈소스로 공개합니다. 수십만 개의 언어 주석이 달린 궤적 데이터셋을 행동 복제(behavioral cloning)로 학습한 결과, 생성된 정책은 이전 연구보다 한 자릿수 더 많은 명령을 능숙하게 실행할 수 있습니다. 구체적으로, 실제 세계에서 원시적인 종단 간 시각-언어-운동 기술을 지정하는 87,000개의 고유 자연어 문자열 집합에 대해 93.5%의 성공률을 추정했습니다. 또한 동일한 정책이 인간의 실시간 언어 안내를 통해 "블록으로 웃는 얼굴 만들기"와 같은 다양한 정밀한 장기 재배치 목표를 처리할 수 있음을 발견했습니다. 공개하는 데이터셋은 약 600,000개의 언어 레이블이 지정된 궤적으로 구성되어 있으며, 이는 기존 데이터셋보다 한 자릿수 더 큽니다. 입증된 결과와 관련 자산이 유용하고 능력 있는 자연어 상호작용 로봇의 추가 발전을 가능하게 하길 바랍니다. 동영상은 https://interactive-language.github.io에서 확인하세요.
