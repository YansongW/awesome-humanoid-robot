---
$id: ent_paper_egomimic_scaling_imitation_lea_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoMimic: Scaling Imitation Learning via Egocentric Video'
  zh: 'EgoMimic: Scaling Imitation Learning via Egocentric Video'
  ko: 'EgoMimic: Scaling Imitation Learning via Egocentric Video'
summary:
  en: 'EgoMimic: Scaling Imitation Learning via Egocentric Video is a 2024 work on manipulation for humanoid robots, with
    open-source code available.'
  zh: 'EgoMimic: Scaling Imitation Learning via Egocentric Video is a 2024 work on manipulation for humanoid robots, with
    open-source code available.'
  ko: 'EgoMimic: Scaling Imitation Learning via Egocentric Video is a 2024 work on manipulation for humanoid robots, with
    open-source code available.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egomimic
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.24221v1.
sources:
- id: src_001
  type: paper
  title: 'EgoMimic: Scaling Imitation Learning via Egocentric Video (arXiv)'
  url: https://arxiv.org/abs/2410.24221
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'EgoMimic: Scaling Imitation Learning via Egocentric Video project page'
  url: https://egomimic.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
The scale and diversity of demonstration data required for imitation learning is a significant challenge. We present EgoMimic, a full-stack framework which scales manipulation via human embodiment data, specifically egocentric human videos paired with 3D hand tracking. EgoMimic achieves this through: (1) a system to capture human embodiment data using the ergonomic Project Aria glasses, (2) a low-cost bimanual manipulator that minimizes the kinematic gap to human data, (3) cross-domain data alignment techniques, and (4) an imitation learning architecture that co-trains on human and robot data. Compared to prior works that only extract high-level intent from human videos, our approach treats human and robot data equally as embodied demonstration data and learns a unified policy from both data sources. EgoMimic achieves significant improvement on a diverse set of long-horizon, single-arm and bimanual manipulation tasks over state-of-the-art imitation learning methods and enables generalization to entirely new scenes. Finally, we show a favorable scaling trend for EgoMimic, where adding 1 hour of additional hand data is significantly more valuable than 1 hour of additional robot data. Videos and additional information can be found at https://egomimic.github.io/

## 核心内容
The scale and diversity of demonstration data required for imitation learning is a significant challenge. We present EgoMimic, a full-stack framework which scales manipulation via human embodiment data, specifically egocentric human videos paired with 3D hand tracking. EgoMimic achieves this through: (1) a system to capture human embodiment data using the ergonomic Project Aria glasses, (2) a low-cost bimanual manipulator that minimizes the kinematic gap to human data, (3) cross-domain data alignment techniques, and (4) an imitation learning architecture that co-trains on human and robot data. Compared to prior works that only extract high-level intent from human videos, our approach treats human and robot data equally as embodied demonstration data and learns a unified policy from both data sources. EgoMimic achieves significant improvement on a diverse set of long-horizon, single-arm and bimanual manipulation tasks over state-of-the-art imitation learning methods and enables generalization to entirely new scenes. Finally, we show a favorable scaling trend for EgoMimic, where adding 1 hour of additional hand data is significantly more valuable than 1 hour of additional robot data. Videos and additional information can be found at https://egomimic.github.io/

## 参考
- http://arxiv.org/abs/2410.24221v1

## Overview
The scale and diversity of demonstration data required for imitation learning is a significant challenge. We present EgoMimic, a full-stack framework which scales manipulation via human embodiment data, specifically egocentric human videos paired with 3D hand tracking. EgoMimic achieves this through: (1) a system to capture human embodiment data using the ergonomic Project Aria glasses, (2) a low-cost bimanual manipulator that minimizes the kinematic gap to human data, (3) cross-domain data alignment techniques, and (4) an imitation learning architecture that co-trains on human and robot data. Compared to prior works that only extract high-level intent from human videos, our approach treats human and robot data equally as embodied demonstration data and learns a unified policy from both data sources. EgoMimic achieves significant improvement on a diverse set of long-horizon, single-arm and bimanual manipulation tasks over state-of-the-art imitation learning methods and enables generalization to entirely new scenes. Finally, we show a favorable scaling trend for EgoMimic, where adding 1 hour of additional hand data is significantly more valuable than 1 hour of additional robot data. Videos and additional information can be found at https://egomimic.github.io/

## Content
The scale and diversity of demonstration data required for imitation learning is a significant challenge. We present EgoMimic, a full-stack framework which scales manipulation via human embodiment data, specifically egocentric human videos paired with 3D hand tracking. EgoMimic achieves this through: (1) a system to capture human embodiment data using the ergonomic Project Aria glasses, (2) a low-cost bimanual manipulator that minimizes the kinematic gap to human data, (3) cross-domain data alignment techniques, and (4) an imitation learning architecture that co-trains on human and robot data. Compared to prior works that only extract high-level intent from human videos, our approach treats human and robot data equally as embodied demonstration data and learns a unified policy from both data sources. EgoMimic achieves significant improvement on a diverse set of long-horizon, single-arm and bimanual manipulation tasks over state-of-the-art imitation learning methods and enables generalization to entirely new scenes. Finally, we show a favorable scaling trend for EgoMimic, where adding 1 hour of additional hand data is significantly more valuable than 1 hour of additional robot data. Videos and additional information can be found at https://egomimic.github.io/

## 개요
모방 학습에 필요한 시연 데이터의 규모와 다양성은 중요한 도전 과제입니다. 우리는 인간 체화 데이터, 특히 3D 손 추적과 결합된 자기중심적 인간 비디오를 통해 조작을 확장하는 풀스택 프레임워크인 EgoMimic을 제시합니다. EgoMimic은 다음을 통해 이를 달성합니다: (1) 인체공학적 Project Aria 안경을 사용하여 인간 체화 데이터를 캡처하는 시스템, (2) 인간 데이터와의 운동학적 격차를 최소화하는 저비용 양손 조작기, (3) 교차 도메인 데이터 정렬 기술, (4) 인간 및 로봇 데이터를 공동 학습하는 모방 학습 아키텍처. 인간 비디오에서 고수준 의도만 추출하는 이전 연구와 달리, 우리의 접근 방식은 인간과 로봇 데이터를 동등한 체화 시연 데이터로 취급하고 두 데이터 소스에서 통합 정책을 학습합니다. EgoMimic은 최첨단 모방 학습 방법보다 다양한 장기, 단일 팔 및 양손 조작 작업에서 상당한 개선을 이루며 완전히 새로운 장면으로의 일반화를 가능하게 합니다. 마지막으로, EgoMimic에서 1시간의 추가 손 데이터가 1시간의 추가 로봇 데이터보다 훨씬 더 가치 있는 유리한 확장 추세를 보여줍니다. 비디오 및 추가 정보는 https://egomimic.github.io/에서 확인할 수 있습니다.

## 핵심 내용
모방 학습에 필요한 시연 데이터의 규모와 다양성은 중요한 도전 과제입니다. 우리는 인간 체화 데이터, 특히 3D 손 추적과 결합된 자기중심적 인간 비디오를 통해 조작을 확장하는 풀스택 프레임워크인 EgoMimic을 제시합니다. EgoMimic은 다음을 통해 이를 달성합니다: (1) 인체공학적 Project Aria 안경을 사용하여 인간 체화 데이터를 캡처하는 시스템, (2) 인간 데이터와의 운동학적 격차를 최소화하는 저비용 양손 조작기, (3) 교차 도메인 데이터 정렬 기술, (4) 인간 및 로봇 데이터를 공동 학습하는 모방 학습 아키텍처. 인간 비디오에서 고수준 의도만 추출하는 이전 연구와 달리, 우리의 접근 방식은 인간과 로봇 데이터를 동등한 체화 시연 데이터로 취급하고 두 데이터 소스에서 통합 정책을 학습합니다. EgoMimic은 최첨단 모방 학습 방법보다 다양한 장기, 단일 팔 및 양손 조작 작업에서 상당한 개선을 이루며 완전히 새로운 장면으로의 일반화를 가능하게 합니다. 마지막으로, EgoMimic에서 1시간의 추가 손 데이터가 1시간의 추가 로봇 데이터보다 훨씬 더 가치 있는 유리한 확장 추세를 보여줍니다. 비디오 및 추가 정보는 https://egomimic.github.io/에서 확인할 수 있습니다.
