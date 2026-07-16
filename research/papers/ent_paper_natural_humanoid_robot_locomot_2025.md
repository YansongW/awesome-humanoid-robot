---
$id: ent_paper_natural_humanoid_robot_locomot_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Natural Humanoid Robot Locomotion with Generative Motion Prior
  zh: Natural Humanoid Robot Locomotion with Generative Motion Prior
  ko: Natural Humanoid Robot Locomotion with Generative Motion Prior
summary:
  en: Natural Humanoid Robot Locomotion with Generative Motion Prior is a 2025 work on locomotion for humanoid robots.
  zh: Natural Humanoid Robot Locomotion with Generative Motion Prior is a 2025 work on locomotion for humanoid robots.
  ko: Natural Humanoid Robot Locomotion with Generative Motion Prior is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- natural_humanoid_robot_locomot
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.09015v1.
sources:
- id: src_001
  type: paper
  title: Natural Humanoid Robot Locomotion with Generative Motion Prior (arXiv)
  url: https://arxiv.org/abs/2503.09015
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Natural and lifelike locomotion remains a fundamental challenge for humanoid robots to interact with human society. However, previous methods either neglect motion naturalness or rely on unstable and ambiguous style rewards. In this paper, we propose a novel Generative Motion Prior (GMP) that provides fine-grained motion-level supervision for the task of natural humanoid robot locomotion. To leverage natural human motions, we first employ whole-body motion retargeting to effectively transfer them to the robot. Subsequently, we train a generative model offline to predict future natural reference motions for the robot based on a conditional variational auto-encoder. During policy training, the generative motion prior serves as a frozen online motion generator, delivering precise and comprehensive supervision at the trajectory level, including joint angles and keypoint positions. The generative motion prior significantly enhances training stability and improves interpretability by offering detailed and dense guidance throughout the learning process. Experimental results in both simulation and real-world environments demonstrate that our method achieves superior motion naturalness compared to existing approaches. Project page can be found at https://sites.google.com/view/humanoid-gmp

## 核心内容
Natural and lifelike locomotion remains a fundamental challenge for humanoid robots to interact with human society. However, previous methods either neglect motion naturalness or rely on unstable and ambiguous style rewards. In this paper, we propose a novel Generative Motion Prior (GMP) that provides fine-grained motion-level supervision for the task of natural humanoid robot locomotion. To leverage natural human motions, we first employ whole-body motion retargeting to effectively transfer them to the robot. Subsequently, we train a generative model offline to predict future natural reference motions for the robot based on a conditional variational auto-encoder. During policy training, the generative motion prior serves as a frozen online motion generator, delivering precise and comprehensive supervision at the trajectory level, including joint angles and keypoint positions. The generative motion prior significantly enhances training stability and improves interpretability by offering detailed and dense guidance throughout the learning process. Experimental results in both simulation and real-world environments demonstrate that our method achieves superior motion naturalness compared to existing approaches. Project page can be found at https://sites.google.com/view/humanoid-gmp

## 参考
- http://arxiv.org/abs/2503.09015v1

## Overview
Natural and lifelike locomotion remains a fundamental challenge for humanoid robots to interact with human society. However, previous methods either neglect motion naturalness or rely on unstable and ambiguous style rewards. In this paper, we propose a novel Generative Motion Prior (GMP) that provides fine-grained motion-level supervision for the task of natural humanoid robot locomotion. To leverage natural human motions, we first employ whole-body motion retargeting to effectively transfer them to the robot. Subsequently, we train a generative model offline to predict future natural reference motions for the robot based on a conditional variational auto-encoder. During policy training, the generative motion prior serves as a frozen online motion generator, delivering precise and comprehensive supervision at the trajectory level, including joint angles and keypoint positions. The generative motion prior significantly enhances training stability and improves interpretability by offering detailed and dense guidance throughout the learning process. Experimental results in both simulation and real-world environments demonstrate that our method achieves superior motion naturalness compared to existing approaches. Project page can be found at https://sites.google.com/view/humanoid-gmp

## Content
Natural and lifelike locomotion remains a fundamental challenge for humanoid robots to interact with human society. However, previous methods either neglect motion naturalness or rely on unstable and ambiguous style rewards. In this paper, we propose a novel Generative Motion Prior (GMP) that provides fine-grained motion-level supervision for the task of natural humanoid robot locomotion. To leverage natural human motions, we first employ whole-body motion retargeting to effectively transfer them to the robot. Subsequently, we train a generative model offline to predict future natural reference motions for the robot based on a conditional variational auto-encoder. During policy training, the generative motion prior serves as a frozen online motion generator, delivering precise and comprehensive supervision at the trajectory level, including joint angles and keypoint positions. The generative motion prior significantly enhances training stability and improves interpretability by offering detailed and dense guidance throughout the learning process. Experimental results in both simulation and real-world environments demonstrate that our method achieves superior motion naturalness compared to existing approaches. Project page can be found at https://sites.google.com/view/humanoid-gmp

## 개요
자연스럽고 생생한 보행은 인간형 로봇이 인간 사회와 상호작용하기 위한 근본적인 과제로 남아 있습니다. 그러나 기존 방법들은 동작의 자연스러움을 무시하거나 불안정하고 모호한 스타일 보상에 의존합니다. 본 논문에서는 자연스러운 인간형 로봇 보행 작업을 위해 세분화된 동작 수준의 감독을 제공하는 새로운 생성적 동작 사전(Generative Motion Prior, GMP)을 제안합니다. 자연스러운 인간 동작을 활용하기 위해 먼저 전신 동작 리타겟팅(whole-body motion retargeting)을 적용하여 이를 로봇에 효과적으로 전이합니다. 이후 조건부 변분 오토인코더(conditional variational auto-encoder)를 기반으로 로봇의 미래 자연스러운 참조 동작을 예측하는 생성 모델을 오프라인에서 학습합니다. 정책 학습 중에 생성적 동작 사전은 고정된 온라인 동작 생성기(frozen online motion generator)로 작동하여 관절 각도와 키포인트 위치를 포함한 궤적 수준에서 정밀하고 포괄적인 감독을 제공합니다. 생성적 동작 사전은 학습 과정 전반에 걸쳐 상세하고 밀집된 지침을 제공함으로써 학습 안정성을 크게 향상시키고 해석 가능성을 개선합니다. 시뮬레이션 및 실제 환경에서의 실험 결과는 우리의 방법이 기존 접근 방식에 비해 우수한 동작 자연스러움을 달성함을 보여줍니다. 프로젝트 페이지는 https://sites.google.com/view/humanoid-gmp 에서 확인할 수 있습니다.

## 핵심 내용
자연스럽고 생생한 보행은 인간형 로봇이 인간 사회와 상호작용하기 위한 근본적인 과제로 남아 있습니다. 그러나 기존 방법들은 동작의 자연스러움을 무시하거나 불안정하고 모호한 스타일 보상에 의존합니다. 본 논문에서는 자연스러운 인간형 로봇 보행 작업을 위해 세분화된 동작 수준의 감독을 제공하는 새로운 생성적 동작 사전(Generative Motion Prior, GMP)을 제안합니다. 자연스러운 인간 동작을 활용하기 위해 먼저 전신 동작 리타겟팅을 적용하여 이를 로봇에 효과적으로 전이합니다. 이후 조건부 변분 오토인코더를 기반으로 로봇의 미래 자연스러운 참조 동작을 예측하는 생성 모델을 오프라인에서 학습합니다. 정책 학습 중에 생성적 동작 사전은 고정된 온라인 동작 생성기로 작동하여 관절 각도와 키포인트 위치를 포함한 궤적 수준에서 정밀하고 포괄적인 감독을 제공합니다. 생성적 동작 사전은 학습 과정 전반에 걸쳐 상세하고 밀집된 지침을 제공함으로써 학습 안정성을 크게 향상시키고 해석 가능성을 개선합니다. 시뮬레이션 및 실제 환경에서의 실험 결과는 우리의 방법이 기존 접근 방식에 비해 우수한 동작 자연스러움을 달성함을 보여줍니다. 프로젝트 페이지는 https://sites.google.com/view/humanoid-gmp 에서 확인할 수 있습니다.
