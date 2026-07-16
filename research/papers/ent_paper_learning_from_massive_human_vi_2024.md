---
$id: ent_paper_learning_from_massive_human_vi_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning from Massive Human Videos for Universal Humanoid Pose Control
  zh: Learning from Massive Human Videos for Universal Humanoid Pose Control
  ko: Learning from Massive Human Videos for Universal Humanoid Pose Control
summary:
  en: Learning from Massive Human Videos for Universal Humanoid Pose Control is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Learning from Massive Human Videos for Universal Humanoid Pose Control is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Learning from Massive Human Videos for Universal Humanoid Pose Control is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
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
- learning_from_massive_human_vi
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.14172v1.
sources:
- id: src_001
  type: paper
  title: Learning from Massive Human Videos for Universal Humanoid Pose Control (arXiv)
  url: https://arxiv.org/abs/2412.14172
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Learning from Massive Human Videos for Universal Humanoid Pose Control project page
  url: https://usc-gvl.github.io/UH-1/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Scalable learning of humanoid robots is crucial for their deployment in real-world applications. While traditional approaches primarily rely on reinforcement learning or teleoperation to achieve whole-body control, they are often limited by the diversity of simulated environments and the high costs of demonstration collection. In contrast, human videos are ubiquitous and present an untapped source of semantic and motion information that could significantly enhance the generalization capabilities of humanoid robots. This paper introduces Humanoid-X, a large-scale dataset of over 20 million humanoid robot poses with corresponding text-based motion descriptions, designed to leverage this abundant data. Humanoid-X is curated through a comprehensive pipeline: data mining from the Internet, video caption generation, motion retargeting of humans to humanoid robots, and policy learning for real-world deployment. With Humanoid-X, we further train a large humanoid model, UH-1, which takes text instructions as input and outputs corresponding actions to control a humanoid robot. Extensive simulated and real-world experiments validate that our scalable training approach leads to superior generalization in text-based humanoid control, marking a significant step toward adaptable, real-world-ready humanoid robots.

## 核心内容
Scalable learning of humanoid robots is crucial for their deployment in real-world applications. While traditional approaches primarily rely on reinforcement learning or teleoperation to achieve whole-body control, they are often limited by the diversity of simulated environments and the high costs of demonstration collection. In contrast, human videos are ubiquitous and present an untapped source of semantic and motion information that could significantly enhance the generalization capabilities of humanoid robots. This paper introduces Humanoid-X, a large-scale dataset of over 20 million humanoid robot poses with corresponding text-based motion descriptions, designed to leverage this abundant data. Humanoid-X is curated through a comprehensive pipeline: data mining from the Internet, video caption generation, motion retargeting of humans to humanoid robots, and policy learning for real-world deployment. With Humanoid-X, we further train a large humanoid model, UH-1, which takes text instructions as input and outputs corresponding actions to control a humanoid robot. Extensive simulated and real-world experiments validate that our scalable training approach leads to superior generalization in text-based humanoid control, marking a significant step toward adaptable, real-world-ready humanoid robots.

## 参考
- http://arxiv.org/abs/2412.14172v1

## Overview
Scalable learning of humanoid robots is crucial for their deployment in real-world applications. While traditional approaches primarily rely on reinforcement learning or teleoperation to achieve whole-body control, they are often limited by the diversity of simulated environments and the high costs of demonstration collection. In contrast, human videos are ubiquitous and present an untapped source of semantic and motion information that could significantly enhance the generalization capabilities of humanoid robots. This paper introduces Humanoid-X, a large-scale dataset of over 20 million humanoid robot poses with corresponding text-based motion descriptions, designed to leverage this abundant data. Humanoid-X is curated through a comprehensive pipeline: data mining from the Internet, video caption generation, motion retargeting of humans to humanoid robots, and policy learning for real-world deployment. With Humanoid-X, we further train a large humanoid model, UH-1, which takes text instructions as input and outputs corresponding actions to control a humanoid robot. Extensive simulated and real-world experiments validate that our scalable training approach leads to superior generalization in text-based humanoid control, marking a significant step toward adaptable, real-world-ready humanoid robots.

## Content
Scalable learning of humanoid robots is crucial for their deployment in real-world applications. While traditional approaches primarily rely on reinforcement learning or teleoperation to achieve whole-body control, they are often limited by the diversity of simulated environments and the high costs of demonstration collection. In contrast, human videos are ubiquitous and present an untapped source of semantic and motion information that could significantly enhance the generalization capabilities of humanoid robots. This paper introduces Humanoid-X, a large-scale dataset of over 20 million humanoid robot poses with corresponding text-based motion descriptions, designed to leverage this abundant data. Humanoid-X is curated through a comprehensive pipeline: data mining from the Internet, video caption generation, motion retargeting of humans to humanoid robots, and policy learning for real-world deployment. With Humanoid-X, we further train a large humanoid model, UH-1, which takes text instructions as input and outputs corresponding actions to control a humanoid robot. Extensive simulated and real-world experiments validate that our scalable training approach leads to superior generalization in text-based humanoid control, marking a significant step toward adaptable, real-world-ready humanoid robots.

## 개요
휴머노이드 로봇의 확장 가능한 학습은 실제 환경에서의 배치에 매우 중요합니다. 전통적인 접근 방식은 주로 강화 학습이나 원격 조작을 통해 전신 제어를 달성하지만, 시뮬레이션 환경의 다양성 부족과 시연 수집의 높은 비용으로 인해 제한되는 경우가 많습니다. 반면, 인간 비디오는 어디에나 존재하며 휴머노이드 로봇의 일반화 능력을 크게 향상시킬 수 있는 활용되지 않은 의미 및 동작 정보 소스입니다. 본 논문은 이러한 풍부한 데이터를 활용하기 위해 설계된 2천만 개 이상의 휴머노이드 로봇 포즈와 해당 텍스트 기반 동작 설명을 포함한 대규모 데이터셋 Humanoid-X를 소개합니다. Humanoid-X는 인터넷 데이터 마이닝, 비디오 캡션 생성, 인간에서 휴머노이드 로봇으로의 동작 리타겟팅, 실제 배치를 위한 정책 학습으로 구성된 포괄적인 파이프라인을 통해 구축되었습니다. Humanoid-X를 기반으로, 텍스트 명령을 입력으로 받아 휴머노이드 로봇을 제어하는 해당 동작을 출력하는 대규모 휴머노이드 모델 UH-1을 추가로 학습시킵니다. 광범위한 시뮬레이션 및 실제 실험을 통해 우리의 확장 가능한 학습 접근 방식이 텍스트 기반 휴머노이드 제어에서 뛰어난 일반화 성능을 보여줌을 입증하며, 이는 적응 가능하고 실제 환경에 적용 가능한 휴머노이드 로봇을 향한 중요한 진전을 의미합니다.

## 핵심 내용
휴머노이드 로봇의 확장 가능한 학습은 실제 환경에서의 배치에 매우 중요합니다. 전통적인 접근 방식은 주로 강화 학습이나 원격 조작을 통해 전신 제어를 달성하지만, 시뮬레이션 환경의 다양성 부족과 시연 수집의 높은 비용으로 인해 제한되는 경우가 많습니다. 반면, 인간 비디오는 어디에나 존재하며 휴머노이드 로봇의 일반화 능력을 크게 향상시킬 수 있는 활용되지 않은 의미 및 동작 정보 소스입니다. 본 논문은 이러한 풍부한 데이터를 활용하기 위해 설계된 2천만 개 이상의 휴머노이드 로봇 포즈와 해당 텍스트 기반 동작 설명을 포함한 대규모 데이터셋 Humanoid-X를 소개합니다. Humanoid-X는 인터넷 데이터 마이닝, 비디오 캡션 생성, 인간에서 휴머노이드 로봇으로의 동작 리타겟팅, 실제 배치를 위한 정책 학습으로 구성된 포괄적인 파이프라인을 통해 구축되었습니다. Humanoid-X를 기반으로, 텍스트 명령을 입력으로 받아 휴머노이드 로봇을 제어하는 해당 동작을 출력하는 대규모 휴머노이드 모델 UH-1을 추가로 학습시킵니다. 광범위한 시뮬레이션 및 실제 실험을 통해 우리의 확장 가능한 학습 접근 방식이 텍스트 기반 휴머노이드 제어에서 뛰어난 일반화 성능을 보여줌을 입증하며, 이는 적응 가능하고 실제 환경에 적용 가능한 휴머노이드 로봇을 향한 중요한 진전을 의미합니다.
