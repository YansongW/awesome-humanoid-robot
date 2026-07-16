---
$id: ent_paper_learning_to_ball_composing_pol_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves'
  zh: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves'
  ko: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves'
summary:
  en: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves is a 2025 work on physics-based character animation
    for humanoid robots.'
  zh: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves is a 2025 work on physics-based character animation
    for humanoid robots.'
  ko: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves is a 2025 work on physics-based character animation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- learning_to_ball
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22442v1.
sources:
- id: src_001
  type: paper
  title: 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves (arXiv)'
  url: https://arxiv.org/abs/2509.22442
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning a control policy for a multi-phase, long-horizon task, such as basketball maneuvers, remains challenging for reinforcement learning approaches due to the need for seamless policy composition and transitions between skills. A long-horizon task typically consists of distinct subtasks with well-defined goals, separated by transitional subtasks with unclear goals but critical to the success of the entire task. Existing methods like the mixture of experts and skill chaining struggle with tasks where individual policies do not share significant commonly explored states or lack well-defined initial and terminal states between different phases. In this paper, we introduce a novel policy integration framework to enable the composition of drastically different motor skills in multi-phase long-horizon tasks with ill-defined intermediate states. Based on that, we further introduce a high-level soft router to enable seamless and robust transitions between the subtasks. We evaluate our framework on a set of fundamental basketball skills and challenging transitions. Policies trained by our approach can effectively control the simulated character to interact with the ball and accomplish the long-horizon task specified by real-time user commands, without relying on ball trajectory references.

## 核心内容
Learning a control policy for a multi-phase, long-horizon task, such as basketball maneuvers, remains challenging for reinforcement learning approaches due to the need for seamless policy composition and transitions between skills. A long-horizon task typically consists of distinct subtasks with well-defined goals, separated by transitional subtasks with unclear goals but critical to the success of the entire task. Existing methods like the mixture of experts and skill chaining struggle with tasks where individual policies do not share significant commonly explored states or lack well-defined initial and terminal states between different phases. In this paper, we introduce a novel policy integration framework to enable the composition of drastically different motor skills in multi-phase long-horizon tasks with ill-defined intermediate states. Based on that, we further introduce a high-level soft router to enable seamless and robust transitions between the subtasks. We evaluate our framework on a set of fundamental basketball skills and challenging transitions. Policies trained by our approach can effectively control the simulated character to interact with the ball and accomplish the long-horizon task specified by real-time user commands, without relying on ball trajectory references.

## 参考
- http://arxiv.org/abs/2509.22442v1

## Overview
Learning a control policy for a multi-phase, long-horizon task, such as basketball maneuvers, remains challenging for reinforcement learning approaches due to the need for seamless policy composition and transitions between skills. A long-horizon task typically consists of distinct subtasks with well-defined goals, separated by transitional subtasks with unclear goals but critical to the success of the entire task. Existing methods like the mixture of experts and skill chaining struggle with tasks where individual policies do not share significant commonly explored states or lack well-defined initial and terminal states between different phases. In this paper, we introduce a novel policy integration framework to enable the composition of drastically different motor skills in multi-phase long-horizon tasks with ill-defined intermediate states. Based on that, we further introduce a high-level soft router to enable seamless and robust transitions between the subtasks. We evaluate our framework on a set of fundamental basketball skills and challenging transitions. Policies trained by our approach can effectively control the simulated character to interact with the ball and accomplish the long-horizon task specified by real-time user commands, without relying on ball trajectory references.

## Content
Learning a control policy for a multi-phase, long-horizon task, such as basketball maneuvers, remains challenging for reinforcement learning approaches due to the need for seamless policy composition and transitions between skills. A long-horizon task typically consists of distinct subtasks with well-defined goals, separated by transitional subtasks with unclear goals but critical to the success of the entire task. Existing methods like the mixture of experts and skill chaining struggle with tasks where individual policies do not share significant commonly explored states or lack well-defined initial and terminal states between different phases. In this paper, we introduce a novel policy integration framework to enable the composition of drastically different motor skills in multi-phase long-horizon tasks with ill-defined intermediate states. Based on that, we further introduce a high-level soft router to enable seamless and robust transitions between the subtasks. We evaluate our framework on a set of fundamental basketball skills and challenging transitions. Policies trained by our approach can effectively control the simulated character to interact with the ball and accomplish the long-horizon task specified by real-time user commands, without relying on ball trajectory references.

## 개요
농구 동작과 같은 다단계 장기 과제를 위한 제어 정책을 학습하는 것은 강화 학습 접근법에서 정책 구성과 기술 간 전환의 원활함이 필요하기 때문에 여전히 어려운 과제로 남아 있습니다. 장기 과제는 일반적으로 명확한 목표를 가진 개별 하위 과제와, 목표는 불명확하지만 전체 과제의 성공에 중요한 전환 하위 과제로 구성됩니다. 전문가 혼합(mixture of experts) 및 기술 체이닝(skill chaining)과 같은 기존 방법은 개별 정책이 공통적으로 탐색된 상태를 충분히 공유하지 않거나, 서로 다른 단계 간에 명확한 초기 및 종료 상태가 부족한 과제에서 어려움을 겪습니다. 본 논문에서는 중간 상태가 불명확한 다단계 장기 과제에서 극도로 다른 운동 기술을 구성할 수 있는 새로운 정책 통합 프레임워크를 소개합니다. 이를 바탕으로, 하위 과제 간 원활하고 강건한 전환을 가능하게 하는 고수준 소프트 라우터(high-level soft router)를 추가로 도입합니다. 우리는 기본적인 농구 기술과 도전적인 전환 과제 세트에서 이 프레임워크를 평가합니다. 우리의 접근법으로 훈련된 정책은 공 궤적 참조에 의존하지 않고, 시뮬레이션된 캐릭터가 공과 상호작용하며 실시간 사용자 명령으로 지정된 장기 과제를 효과적으로 수행할 수 있게 합니다.

## 핵심 내용
농구 동작과 같은 다단계 장기 과제를 위한 제어 정책을 학습하는 것은 강화 학습 접근법에서 정책 구성과 기술 간 전환의 원활함이 필요하기 때문에 여전히 어려운 과제로 남아 있습니다. 장기 과제는 일반적으로 명확한 목표를 가진 개별 하위 과제와, 목표는 불명확하지만 전체 과제의 성공에 중요한 전환 하위 과제로 구성됩니다. 전문가 혼합(mixture of experts) 및 기술 체이닝(skill chaining)과 같은 기존 방법은 개별 정책이 공통적으로 탐색된 상태를 충분히 공유하지 않거나, 서로 다른 단계 간에 명확한 초기 및 종료 상태가 부족한 과제에서 어려움을 겪습니다. 본 논문에서는 중간 상태가 불명확한 다단계 장기 과제에서 극도로 다른 운동 기술을 구성할 수 있는 새로운 정책 통합 프레임워크를 소개합니다. 이를 바탕으로, 하위 과제 간 원활하고 강건한 전환을 가능하게 하는 고수준 소프트 라우터(high-level soft router)를 추가로 도입합니다. 우리는 기본적인 농구 기술과 도전적인 전환 과제 세트에서 이 프레임워크를 평가합니다. 우리의 접근법으로 훈련된 정책은 공 궤적 참조에 의존하지 않고, 시뮬레이션된 캐릭터가 공과 상호작용하며 실시간 사용자 명령으로 지정된 장기 과제를 효과적으로 수행할 수 있게 합니다.
