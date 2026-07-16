---
$id: ent_paper_dexcap_scalable_and_portable_m_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation'
  zh: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation'
  ko: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation'
summary:
  en: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation is a 2024 work on manipulation
    for humanoid robots, with open-source code available.'
  zh: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation is a 2024 work on manipulation
    for humanoid robots, with open-source code available.'
  ko: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation is a 2024 work on manipulation
    for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dexcap
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.07788v2.
sources:
- id: src_001
  type: paper
  title: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation (arXiv)'
  url: https://arxiv.org/abs/2403.07788
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation project page'
  url: https://dex-cap.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning from human hand motion data presents a promising avenue for imbuing robots with human-like dexterity in real-world manipulation tasks. Despite this potential, substantial challenges persist, particularly with the portability of existing hand motion capture (mocap) systems and the complexity of translating mocap data into effective robotic policies. To tackle these issues, we introduce DexCap, a portable hand motion capture system, alongside DexIL, a novel imitation algorithm for training dexterous robot skills directly from human hand mocap data. DexCap offers precise, occlusion-resistant tracking of wrist and finger motions based on SLAM and electromagnetic field together with 3D observations of the environment. Utilizing this rich dataset, DexIL employs inverse kinematics and point cloud-based imitation learning to seamlessly replicate human actions with robot hands. Beyond direct learning from human motion, DexCap also offers an optional human-in-the-loop correction mechanism during policy rollouts to refine and further improve task performance. Through extensive evaluation across six challenging dexterous manipulation tasks, our approach not only demonstrates superior performance but also showcases the system's capability to effectively learn from in-the-wild mocap data, paving the way for future data collection methods in the pursuit of human-level robot dexterity. More details can be found at https://dex-cap.github.io

## 核心内容
Imitation learning from human hand motion data presents a promising avenue for imbuing robots with human-like dexterity in real-world manipulation tasks. Despite this potential, substantial challenges persist, particularly with the portability of existing hand motion capture (mocap) systems and the complexity of translating mocap data into effective robotic policies. To tackle these issues, we introduce DexCap, a portable hand motion capture system, alongside DexIL, a novel imitation algorithm for training dexterous robot skills directly from human hand mocap data. DexCap offers precise, occlusion-resistant tracking of wrist and finger motions based on SLAM and electromagnetic field together with 3D observations of the environment. Utilizing this rich dataset, DexIL employs inverse kinematics and point cloud-based imitation learning to seamlessly replicate human actions with robot hands. Beyond direct learning from human motion, DexCap also offers an optional human-in-the-loop correction mechanism during policy rollouts to refine and further improve task performance. Through extensive evaluation across six challenging dexterous manipulation tasks, our approach not only demonstrates superior performance but also showcases the system's capability to effectively learn from in-the-wild mocap data, paving the way for future data collection methods in the pursuit of human-level robot dexterity. More details can be found at https://dex-cap.github.io

## 参考
- http://arxiv.org/abs/2403.07788v2

## Overview
Imitation learning from human hand motion data presents a promising avenue for imbuing robots with human-like dexterity in real-world manipulation tasks. Despite this potential, substantial challenges persist, particularly with the portability of existing hand motion capture (mocap) systems and the complexity of translating mocap data into effective robotic policies. To tackle these issues, we introduce DexCap, a portable hand motion capture system, alongside DexIL, a novel imitation algorithm for training dexterous robot skills directly from human hand mocap data. DexCap offers precise, occlusion-resistant tracking of wrist and finger motions based on SLAM and electromagnetic field together with 3D observations of the environment. Utilizing this rich dataset, DexIL employs inverse kinematics and point cloud-based imitation learning to seamlessly replicate human actions with robot hands. Beyond direct learning from human motion, DexCap also offers an optional human-in-the-loop correction mechanism during policy rollouts to refine and further improve task performance. Through extensive evaluation across six challenging dexterous manipulation tasks, our approach not only demonstrates superior performance but also showcases the system's capability to effectively learn from in-the-wild mocap data, paving the way for future data collection methods in the pursuit of human-level robot dexterity. More details can be found at https://dex-cap.github.io

## Content
Imitation learning from human hand motion data presents a promising avenue for imbuing robots with human-like dexterity in real-world manipulation tasks. Despite this potential, substantial challenges persist, particularly with the portability of existing hand motion capture (mocap) systems and the complexity of translating mocap data into effective robotic policies. To tackle these issues, we introduce DexCap, a portable hand motion capture system, alongside DexIL, a novel imitation algorithm for training dexterous robot skills directly from human hand mocap data. DexCap offers precise, occlusion-resistant tracking of wrist and finger motions based on SLAM and electromagnetic field together with 3D observations of the environment. Utilizing this rich dataset, DexIL employs inverse kinematics and point cloud-based imitation learning to seamlessly replicate human actions with robot hands. Beyond direct learning from human motion, DexCap also offers an optional human-in-the-loop correction mechanism during policy rollouts to refine and further improve task performance. Through extensive evaluation across six challenging dexterous manipulation tasks, our approach not only demonstrates superior performance but also showcases the system's capability to effectively learn from in-the-wild mocap data, paving the way for future data collection methods in the pursuit of human-level robot dexterity. More details can be found at https://dex-cap.github.io

## 개요
인간 손 동작 데이터로부터의 모방 학습은 실제 조작 작업에서 로봇에 인간과 같은 손재주를 부여할 수 있는 유망한 접근법을 제시합니다. 이러한 잠재력에도 불구하고, 특히 기존 손 동작 캡처(mocap) 시스템의 휴대성과 mocap 데이터를 효과적인 로봇 정책으로 변환하는 복잡성 측면에서 상당한 과제가 남아 있습니다. 이러한 문제를 해결하기 위해 우리는 휴대용 손 동작 캡처 시스템인 DexCap과 인간 손 mocap 데이터로부터 직접 손재주 로봇 기술을 훈련하는 새로운 모방 알고리즘인 DexIL을 소개합니다. DexCap은 SLAM과 전자기장을 기반으로 한 정밀하고 폐색에 강한 손목 및 손가락 동작 추적과 함께 환경의 3D 관측을 제공합니다. 이 풍부한 데이터셋을 활용하여 DexIL은 역운동학과 포인트 클라우드 기반 모방 학습을 사용하여 로봇 손으로 인간 동작을 원활하게 재현합니다. 인간 동작으로부터의 직접 학습 외에도 DexCap은 정책 롤아웃 중 선택적 인간-인-더-루프 교정 메커니즘을 제공하여 작업 성능을 개선하고 추가로 향상시킵니다. 여섯 가지 도전적인 손재주 조작 작업에 대한 광범위한 평가를 통해 우리의 접근 방식은 뛰어난 성능을 입증할 뿐만 아니라 실제 환경의 mocap 데이터로부터 효과적으로 학습할 수 있는 시스템의 능력을 보여주며, 인간 수준의 로봇 손재주를 추구하는 미래 데이터 수집 방법의 길을 열어줍니다. 더 자세한 내용은 https://dex-cap.github.io 에서 확인할 수 있습니다.

## 핵심 내용
인간 손 동작 데이터로부터의 모방 학습은 실제 조작 작업에서 로봇에 인간과 같은 손재주를 부여할 수 있는 유망한 접근법을 제시합니다. 이러한 잠재력에도 불구하고, 특히 기존 손 동작 캡처(mocap) 시스템의 휴대성과 mocap 데이터를 효과적인 로봇 정책으로 변환하는 복잡성 측면에서 상당한 과제가 남아 있습니다. 이러한 문제를 해결하기 위해 우리는 휴대용 손 동작 캡처 시스템인 DexCap과 인간 손 mocap 데이터로부터 직접 손재주 로봇 기술을 훈련하는 새로운 모방 알고리즘인 DexIL을 소개합니다. DexCap은 SLAM과 전자기장을 기반으로 한 정밀하고 폐색에 강한 손목 및 손가락 동작 추적과 함께 환경의 3D 관측을 제공합니다. 이 풍부한 데이터셋을 활용하여 DexIL은 역운동학과 포인트 클라우드 기반 모방 학습을 사용하여 로봇 손으로 인간 동작을 원활하게 재현합니다. 인간 동작으로부터의 직접 학습 외에도 DexCap은 정책 롤아웃 중 선택적 인간-인-더-루프 교정 메커니즘을 제공하여 작업 성능을 개선하고 추가로 향상시킵니다. 여섯 가지 도전적인 손재주 조작 작업에 대한 광범위한 평가를 통해 우리의 접근 방식은 뛰어난 성능을 입증할 뿐만 아니라 실제 환경의 mocap 데이터로부터 효과적으로 학습할 수 있는 시스템의 능력을 보여주며, 인간 수준의 로봇 손재주를 추구하는 미래 데이터 수집 방법의 길을 열어줍니다. 더 자세한 내용은 https://dex-cap.github.io 에서 확인할 수 있습니다.
