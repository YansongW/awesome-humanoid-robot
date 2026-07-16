---
$id: ent_paper_learning_perceptive_humanoid_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Perceptive Humanoid Locomotion over Challenging Terrain
  zh: Learning Perceptive Humanoid Locomotion over Challenging Terrain
  ko: Learning Perceptive Humanoid Locomotion over Challenging Terrain
summary:
  en: Learning Perceptive Humanoid Locomotion over Challenging Terrain is a 2025 work on locomotion for humanoid robots.
  zh: Learning Perceptive Humanoid Locomotion over Challenging Terrain is a 2025 work on locomotion for humanoid robots.
  ko: Learning Perceptive Humanoid Locomotion over Challenging Terrain is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_perceptive_humanoid_l
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.00692v3.
sources:
- id: src_001
  type: paper
  title: Learning Perceptive Humanoid Locomotion over Challenging Terrain (arXiv)
  url: https://arxiv.org/abs/2503.00692
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots are engineered to navigate terrains akin to those encountered by humans, which necessitates human-like locomotion and perceptual abilities. Currently, the most reliable controllers for humanoid motion rely exclusively on proprioception, a reliance that becomes both dangerous and unreliable when coping with rugged terrain. Although the integration of height maps into perception can enable proactive gait planning, robust utilization of this information remains a significant challenge, especially when exteroceptive perception is noisy. To surmount these challenges, we propose a solution based on a teacher-student distillation framework. In this paradigm, an oracle policy accesses noise-free data to establish an optimal reference policy, while the student policy not only imitates the teacher's actions but also simultaneously trains a world model with a variational information bottleneck for sensor denoising and state estimation. Extensive evaluations demonstrate that our approach markedly enhances performance in scenarios characterized by unreliable terrain estimations. Moreover, we conducted rigorous testing in both challenging urban settings and off-road environments, the model successfully traverse 2 km of varied terrain without external intervention.

## 核心内容
Humanoid robots are engineered to navigate terrains akin to those encountered by humans, which necessitates human-like locomotion and perceptual abilities. Currently, the most reliable controllers for humanoid motion rely exclusively on proprioception, a reliance that becomes both dangerous and unreliable when coping with rugged terrain. Although the integration of height maps into perception can enable proactive gait planning, robust utilization of this information remains a significant challenge, especially when exteroceptive perception is noisy. To surmount these challenges, we propose a solution based on a teacher-student distillation framework. In this paradigm, an oracle policy accesses noise-free data to establish an optimal reference policy, while the student policy not only imitates the teacher's actions but also simultaneously trains a world model with a variational information bottleneck for sensor denoising and state estimation. Extensive evaluations demonstrate that our approach markedly enhances performance in scenarios characterized by unreliable terrain estimations. Moreover, we conducted rigorous testing in both challenging urban settings and off-road environments, the model successfully traverse 2 km of varied terrain without external intervention.

## 参考
- http://arxiv.org/abs/2503.00692v3

## Overview
Humanoid robots are engineered to navigate terrains akin to those encountered by humans, which necessitates human-like locomotion and perceptual abilities. Currently, the most reliable controllers for humanoid motion rely exclusively on proprioception, a reliance that becomes both dangerous and unreliable when coping with rugged terrain. Although the integration of height maps into perception can enable proactive gait planning, robust utilization of this information remains a significant challenge, especially when exteroceptive perception is noisy. To surmount these challenges, we propose a solution based on a teacher-student distillation framework. In this paradigm, an oracle policy accesses noise-free data to establish an optimal reference policy, while the student policy not only imitates the teacher's actions but also simultaneously trains a world model with a variational information bottleneck for sensor denoising and state estimation. Extensive evaluations demonstrate that our approach markedly enhances performance in scenarios characterized by unreliable terrain estimations. Moreover, we conducted rigorous testing in both challenging urban settings and off-road environments, the model successfully traverse 2 km of varied terrain without external intervention.

## Content
Humanoid robots are engineered to navigate terrains akin to those encountered by humans, which necessitates human-like locomotion and perceptual abilities. Currently, the most reliable controllers for humanoid motion rely exclusively on proprioception, a reliance that becomes both dangerous and unreliable when coping with rugged terrain. Although the integration of height maps into perception can enable proactive gait planning, robust utilization of this information remains a significant challenge, especially when exteroceptive perception is noisy. To surmount these challenges, we propose a solution based on a teacher-student distillation framework. In this paradigm, an oracle policy accesses noise-free data to establish an optimal reference policy, while the student policy not only imitates the teacher's actions but also simultaneously trains a world model with a variational information bottleneck for sensor denoising and state estimation. Extensive evaluations demonstrate that our approach markedly enhances performance in scenarios characterized by unreliable terrain estimations. Moreover, we conducted rigorous testing in both challenging urban settings and off-road environments, the model successfully traverse 2 km of varied terrain without external intervention.

## 개요
휴머노이드 로봇은 인간이 마주하는 지형과 유사한 환경을 탐색하도록 설계되었으며, 이는 인간과 유사한 보행 및 인지 능력을 필요로 합니다. 현재 휴머노이드 동작을 위한 가장 신뢰할 수 있는 제어기는 고유수용감각에만 의존하는데, 이는 험준한 지형을 다룰 때 위험하고 신뢰할 수 없게 됩니다. 높이 맵을 인식에 통합하면 능동적인 보행 계획이 가능해지지만, 특히 외부 수용 감각에 노이즈가 있을 때 이 정보를 강건하게 활용하는 것은 여전히 중요한 과제입니다. 이러한 문제를 극복하기 위해 우리는 교사-학생 증류 프레임워크에 기반한 해결책을 제안합니다. 이 패러다임에서 오라클 정책은 노이즈가 없는 데이터에 접근하여 최적의 참조 정책을 수립하고, 학생 정책은 교사의 행동을 모방할 뿐만 아니라 동시에 센서 노이즈 제거 및 상태 추정을 위한 변분 정보 병목을 갖춘 세계 모델을 훈련합니다. 광범위한 평가를 통해 우리의 접근 방식이 신뢰할 수 없는 지형 추정이 특징인 시나리오에서 성능을 현저히 향상시킴을 입증했습니다. 또한 까다로운 도시 환경과 오프로드 환경 모두에서 엄격한 테스트를 수행한 결과, 모델은 외부 개입 없이 2km의 다양한 지형을 성공적으로 주행했습니다.

## 핵심 내용
휴머노이드 로봇은 인간이 마주하는 지형과 유사한 환경을 탐색하도록 설계되었으며, 이는 인간과 유사한 보행 및 인지 능력을 필요로 합니다. 현재 휴머노이드 동작을 위한 가장 신뢰할 수 있는 제어기는 고유수용감각에만 의존하는데, 이는 험준한 지형을 다룰 때 위험하고 신뢰할 수 없게 됩니다. 높이 맵을 인식에 통합하면 능동적인 보행 계획이 가능해지지만, 특히 외부 수용 감각에 노이즈가 있을 때 이 정보를 강건하게 활용하는 것은 여전히 중요한 과제입니다. 이러한 문제를 극복하기 위해 우리는 교사-학생 증류 프레임워크에 기반한 해결책을 제안합니다. 이 패러다임에서 오라클 정책은 노이즈가 없는 데이터에 접근하여 최적의 참조 정책을 수립하고, 학생 정책은 교사의 행동을 모방할 뿐만 아니라 동시에 센서 노이즈 제거 및 상태 추정을 위한 변분 정보 병목을 갖춘 세계 모델을 훈련합니다. 광범위한 평가를 통해 우리의 접근 방식이 신뢰할 수 없는 지형 추정이 특징인 시나리오에서 성능을 현저히 향상시킴을 입증했습니다. 또한 까다로운 도시 환경과 오프로드 환경 모두에서 엄격한 테스트를 수행한 결과, 모델은 외부 개입 없이 2km의 다양한 지형을 성공적으로 주행했습니다.
