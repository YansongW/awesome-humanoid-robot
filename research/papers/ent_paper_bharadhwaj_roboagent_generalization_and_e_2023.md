---
$id: ent_paper_bharadhwaj_roboagent_generalization_and_e_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking'
  zh: MT-ACT
  ko: 'RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking'
summary:
  en: 'RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking (MT-ACT),
    is a 2023 generalized vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University,
    FAIR-MetaAI, and published at ICRA 2023.'
  zh: 'RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking (MT-ACT),
    is a 2023 generalized vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University,
    FAIR-MetaAI, and published at ICRA 2023.'
  ko: 'RoboAgent: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking (MT-ACT),
    is a 2023 generalized vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University,
    FAIR-MetaAI, and published at ICRA 2023.'
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
- mt_act
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.01918v1.
sources:
- id: src_001
  type: website
  title: MT-ACT source
  url: https://doi.org/10.1109/ICRA57147.2024.10611293
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
The grand aim of having a single robot that can manipulate arbitrary objects in diverse settings is at odds with the paucity of robotics datasets. Acquiring and growing such datasets is strenuous due to manual efforts, operational costs, and safety challenges. A path toward such an universal agent would require a structured framework capable of wide generalization but trained within a reasonable data budget. In this paper, we develop an efficient system (RoboAgent) for training universal agents capable of multi-task manipulation skills using (a) semantic augmentations that can rapidly multiply existing datasets and (b) action representations that can extract performant policies with small yet diverse multi-modal datasets without overfitting. In addition, reliable task conditioning and an expressive policy architecture enable our agent to exhibit a diverse repertoire of skills in novel situations specified using language commands. Using merely 7500 demonstrations, we are able to train a single agent capable of 12 unique skills, and demonstrate its generalization over 38 tasks spread across common daily activities in diverse kitchen scenes. On average, RoboAgent outperforms prior methods by over 40% in unseen situations while being more sample efficient and being amenable to capability improvements and extensions through fine-tuning. Videos at https://robopen.github.io/

## 核心内容
The grand aim of having a single robot that can manipulate arbitrary objects in diverse settings is at odds with the paucity of robotics datasets. Acquiring and growing such datasets is strenuous due to manual efforts, operational costs, and safety challenges. A path toward such an universal agent would require a structured framework capable of wide generalization but trained within a reasonable data budget. In this paper, we develop an efficient system (RoboAgent) for training universal agents capable of multi-task manipulation skills using (a) semantic augmentations that can rapidly multiply existing datasets and (b) action representations that can extract performant policies with small yet diverse multi-modal datasets without overfitting. In addition, reliable task conditioning and an expressive policy architecture enable our agent to exhibit a diverse repertoire of skills in novel situations specified using language commands. Using merely 7500 demonstrations, we are able to train a single agent capable of 12 unique skills, and demonstrate its generalization over 38 tasks spread across common daily activities in diverse kitchen scenes. On average, RoboAgent outperforms prior methods by over 40% in unseen situations while being more sample efficient and being amenable to capability improvements and extensions through fine-tuning. Videos at https://robopen.github.io/

## 参考
- http://arxiv.org/abs/2309.01918v1

## Overview
The grand aim of having a single robot that can manipulate arbitrary objects in diverse settings is at odds with the paucity of robotics datasets. Acquiring and growing such datasets is strenuous due to manual efforts, operational costs, and safety challenges. A path toward such an universal agent would require a structured framework capable of wide generalization but trained within a reasonable data budget. In this paper, we develop an efficient system (RoboAgent) for training universal agents capable of multi-task manipulation skills using (a) semantic augmentations that can rapidly multiply existing datasets and (b) action representations that can extract performant policies with small yet diverse multi-modal datasets without overfitting. In addition, reliable task conditioning and an expressive policy architecture enable our agent to exhibit a diverse repertoire of skills in novel situations specified using language commands. Using merely 7500 demonstrations, we are able to train a single agent capable of 12 unique skills, and demonstrate its generalization over 38 tasks spread across common daily activities in diverse kitchen scenes. On average, RoboAgent outperforms prior methods by over 40% in unseen situations while being more sample efficient and being amenable to capability improvements and extensions through fine-tuning. Videos at https://robopen.github.io/

## Content
The grand aim of having a single robot that can manipulate arbitrary objects in diverse settings is at odds with the paucity of robotics datasets. Acquiring and growing such datasets is strenuous due to manual efforts, operational costs, and safety challenges. A path toward such an universal agent would require a structured framework capable of wide generalization but trained within a reasonable data budget. In this paper, we develop an efficient system (RoboAgent) for training universal agents capable of multi-task manipulation skills using (a) semantic augmentations that can rapidly multiply existing datasets and (b) action representations that can extract performant policies with small yet diverse multi-modal datasets without overfitting. In addition, reliable task conditioning and an expressive policy architecture enable our agent to exhibit a diverse repertoire of skills in novel situations specified using language commands. Using merely 7500 demonstrations, we are able to train a single agent capable of 12 unique skills, and demonstrate its generalization over 38 tasks spread across common daily activities in diverse kitchen scenes. On average, RoboAgent outperforms prior methods by over 40% in unseen situations while being more sample efficient and being amenable to capability improvements and extensions through fine-tuning. Videos at https://robopen.github.io/

## 개요
다양한 환경에서 임의의 물체를 조작할 수 있는 단일 로봇이라는 거대한 목표는 로봇공학 데이터셋의 부족과 상충됩니다. 이러한 데이터셋을 획득하고 확장하는 것은 수동 작업, 운영 비용 및 안전 문제로 인해 어렵습니다. 이러한 범용 에이전트를 향한 길은 광범위한 일반화가 가능하면서도 합리적인 데이터 예산 내에서 훈련된 구조화된 프레임워크를 필요로 합니다. 본 논문에서는 (a) 기존 데이터셋을 빠르게 증대시킬 수 있는 의미론적 증강과 (b) 과적합 없이 작지만 다양한 다중 모달 데이터셋으로 성능 좋은 정책을 추출할 수 있는 행동 표현을 사용하여 다중 작업 조작 기술을 수행할 수 있는 범용 에이전트를 훈련하기 위한 효율적인 시스템(RoboAgent)을 개발합니다. 또한, 신뢰할 수 있는 작업 조건화와 표현력 있는 정책 아키텍처를 통해 에이전트는 언어 명령으로 지정된 새로운 상황에서 다양한 기술 레퍼토리를 보여줄 수 있습니다. 단 7500개의 시연만으로 12개의 고유 기술을 수행할 수 있는 단일 에이전트를 훈련할 수 있었으며, 다양한 주방 장면에서 일상적인 활동에 걸친 38개 작업에 대한 일반화를 입증했습니다. 평균적으로 RoboAgent는 보지 못한 상황에서 이전 방법보다 40% 이상 우수한 성능을 보였으며, 샘플 효율성이 더 높고 미세 조정을 통한 기능 개선 및 확장이 용이합니다. 동영상은 https://robopen.github.io/에서 확인할 수 있습니다.

## 핵심 내용
다양한 환경에서 임의의 물체를 조작할 수 있는 단일 로봇이라는 거대한 목표는 로봇공학 데이터셋의 부족과 상충됩니다. 이러한 데이터셋을 획득하고 확장하는 것은 수동 작업, 운영 비용 및 안전 문제로 인해 어렵습니다. 이러한 범용 에이전트를 향한 길은 광범위한 일반화가 가능하면서도 합리적인 데이터 예산 내에서 훈련된 구조화된 프레임워크를 필요로 합니다. 본 논문에서는 (a) 기존 데이터셋을 빠르게 증대시킬 수 있는 의미론적 증강과 (b) 과적합 없이 작지만 다양한 다중 모달 데이터셋으로 성능 좋은 정책을 추출할 수 있는 행동 표현을 사용하여 다중 작업 조작 기술을 수행할 수 있는 범용 에이전트를 훈련하기 위한 효율적인 시스템(RoboAgent)을 개발합니다. 또한, 신뢰할 수 있는 작업 조건화와 표현력 있는 정책 아키텍처를 통해 에이전트는 언어 명령으로 지정된 새로운 상황에서 다양한 기술 레퍼토리를 보여줄 수 있습니다. 단 7500개의 시연만으로 12개의 고유 기술을 수행할 수 있는 단일 에이전트를 훈련할 수 있었으며, 다양한 주방 장면에서 일상적인 활동에 걸친 38개 작업에 대한 일반화를 입증했습니다. 평균적으로 RoboAgent는 보지 못한 상황에서 이전 방법보다 40% 이상 우수한 성능을 보였으며, 샘플 효율성이 더 높고 미세 조정을 통한 기능 개선 및 확장이 용이합니다. 동영상은 https://robopen.github.io/에서 확인할 수 있습니다.
