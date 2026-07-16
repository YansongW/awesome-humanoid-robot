---
$id: ent_paper_gu_rt_trajectory_robotic_task_gen_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches'
  zh: RT-Trajectory
  ko: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches'
summary:
  en: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches (RT-Trajectory), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, University of California San Diego,
    Stanford University, Intrinsic, and published at ICLR 2023.'
  zh: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches (RT-Trajectory), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, University of California San Diego,
    Stanford University, Intrinsic, and published at ICLR 2023.'
  ko: 'RT-Trajectory: Robotic Task Generalization via Hindsight Trajectory Sketches (RT-Trajectory), is a 2023 generalized
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, University of California San Diego,
    Stanford University, Intrinsic, and published at ICLR 2023.'
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
- rt_trajectory
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2311.01977v2.
sources:
- id: src_001
  type: paper
  title: RT-Trajectory source
  url: https://openreview.net/forum?id=F1TKzG8LJO
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Generalization remains one of the most important desiderata for robust robot learning systems. While recently proposed approaches show promise in generalization to novel objects, semantic concepts, or visual distribution shifts, generalization to new tasks remains challenging. For example, a language-conditioned policy trained on pick-and-place tasks will not be able to generalize to a folding task, even if the arm trajectory of folding is similar to pick-and-place. Our key insight is that this kind of generalization becomes feasible if we represent the task through rough trajectory sketches. We propose a policy conditioning method using such rough trajectory sketches, which we call RT-Trajectory, that is practical, easy to specify, and allows the policy to effectively perform new tasks that would otherwise be challenging to perform. We find that trajectory sketches strike a balance between being detailed enough to express low-level motion-centric guidance while being coarse enough to allow the learned policy to interpret the trajectory sketch in the context of situational visual observations. In addition, we show how trajectory sketches can provide a useful interface to communicate with robotic policies: they can be specified through simple human inputs like drawings or videos, or through automated methods such as modern image-generating or waypoint-generating methods. We evaluate RT-Trajectory at scale on a variety of real-world robotic tasks, and find that RT-Trajectory is able to perform a wider range of tasks compared to language-conditioned and goal-conditioned policies, when provided the same training data.

## 核心内容
Generalization remains one of the most important desiderata for robust robot learning systems. While recently proposed approaches show promise in generalization to novel objects, semantic concepts, or visual distribution shifts, generalization to new tasks remains challenging. For example, a language-conditioned policy trained on pick-and-place tasks will not be able to generalize to a folding task, even if the arm trajectory of folding is similar to pick-and-place. Our key insight is that this kind of generalization becomes feasible if we represent the task through rough trajectory sketches. We propose a policy conditioning method using such rough trajectory sketches, which we call RT-Trajectory, that is practical, easy to specify, and allows the policy to effectively perform new tasks that would otherwise be challenging to perform. We find that trajectory sketches strike a balance between being detailed enough to express low-level motion-centric guidance while being coarse enough to allow the learned policy to interpret the trajectory sketch in the context of situational visual observations. In addition, we show how trajectory sketches can provide a useful interface to communicate with robotic policies: they can be specified through simple human inputs like drawings or videos, or through automated methods such as modern image-generating or waypoint-generating methods. We evaluate RT-Trajectory at scale on a variety of real-world robotic tasks, and find that RT-Trajectory is able to perform a wider range of tasks compared to language-conditioned and goal-conditioned policies, when provided the same training data.

## 参考
- http://arxiv.org/abs/2311.01977v2

## Overview
Generalization remains one of the most important desiderata for robust robot learning systems. While recently proposed approaches show promise in generalization to novel objects, semantic concepts, or visual distribution shifts, generalization to new tasks remains challenging. For example, a language-conditioned policy trained on pick-and-place tasks will not be able to generalize to a folding task, even if the arm trajectory of folding is similar to pick-and-place. Our key insight is that this kind of generalization becomes feasible if we represent the task through rough trajectory sketches. We propose a policy conditioning method using such rough trajectory sketches, which we call RT-Trajectory, that is practical, easy to specify, and allows the policy to effectively perform new tasks that would otherwise be challenging to perform. We find that trajectory sketches strike a balance between being detailed enough to express low-level motion-centric guidance while being coarse enough to allow the learned policy to interpret the trajectory sketch in the context of situational visual observations. In addition, we show how trajectory sketches can provide a useful interface to communicate with robotic policies: they can be specified through simple human inputs like drawings or videos, or through automated methods such as modern image-generating or waypoint-generating methods. We evaluate RT-Trajectory at scale on a variety of real-world robotic tasks, and find that RT-Trajectory is able to perform a wider range of tasks compared to language-conditioned and goal-conditioned policies, when provided the same training data.

## Content
Generalization remains one of the most important desiderata for robust robot learning systems. While recently proposed approaches show promise in generalization to novel objects, semantic concepts, or visual distribution shifts, generalization to new tasks remains challenging. For example, a language-conditioned policy trained on pick-and-place tasks will not be able to generalize to a folding task, even if the arm trajectory of folding is similar to pick-and-place. Our key insight is that this kind of generalization becomes feasible if we represent the task through rough trajectory sketches. We propose a policy conditioning method using such rough trajectory sketches, which we call RT-Trajectory, that is practical, easy to specify, and allows the policy to effectively perform new tasks that would otherwise be challenging to perform. We find that trajectory sketches strike a balance between being detailed enough to express low-level motion-centric guidance while being coarse enough to allow the learned policy to interpret the trajectory sketch in the context of situational visual observations. In addition, we show how trajectory sketches can provide a useful interface to communicate with robotic policies: they can be specified through simple human inputs like drawings or videos, or through automated methods such as modern image-generating or waypoint-generating methods. We evaluate RT-Trajectory at scale on a variety of real-world robotic tasks, and find that RT-Trajectory is able to perform a wider range of tasks compared to language-conditioned and goal-conditioned policies, when provided the same training data.

## 개요
일반화는 강건한 로봇 학습 시스템을 위한 가장 중요한 요구사항 중 하나로 남아 있습니다. 최근 제안된 접근법들은 새로운 객체, 의미론적 개념 또는 시각적 분포 변화에 대한 일반화에서 가능성을 보여주지만, 새로운 작업으로의 일반화는 여전히 어려운 과제입니다. 예를 들어, 집기-놓기 작업으로 훈련된 언어 조건화 정책은 접기 작업의 팔 궤적이 집기-놓기와 유사하더라도 접기 작업으로 일반화할 수 없습니다. 우리의 핵심 통찰은 이러한 종류의 일반화가 대략적인 궤적 스케치를 통해 작업을 표현할 때 가능해진다는 것입니다. 우리는 이러한 대략적인 궤적 스케치를 사용하는 정책 조건화 방법을 제안하며, 이를 RT-Trajectory라고 부릅니다. 이 방법은 실용적이고 지정하기 쉬우며, 정책이 그렇지 않으면 수행하기 어려운 새로운 작업을 효과적으로 수행할 수 있게 합니다. 우리는 궤적 스케치가 저수준 동작 중심 지침을 표현할 만큼 상세하면서도, 학습된 정책이 상황별 시각적 관찰 맥락에서 궤적 스케치를 해석할 수 있을 만큼 대략적인 균형을 이룬다는 것을 발견했습니다. 또한, 궤적 스케치가 로봇 정책과 소통하기 위한 유용한 인터페이스를 제공할 수 있음을 보여줍니다. 이는 그림이나 비디오와 같은 간단한 인간 입력, 또는 현대 이미지 생성 또는 웨이포인트 생성 방법과 같은 자동화된 방법을 통해 지정될 수 있습니다. 우리는 다양한 실제 로봇 작업에서 RT-Trajectory를 대규모로 평가했으며, 동일한 훈련 데이터가 제공될 때 RT-Trajectory가 언어 조건화 및 목표 조건화 정책보다 더 넓은 범위의 작업을 수행할 수 있음을 발견했습니다.

## 핵심 내용
일반화는 강건한 로봇 학습 시스템을 위한 가장 중요한 요구사항 중 하나로 남아 있습니다. 최근 제안된 접근법들은 새로운 객체, 의미론적 개념 또는 시각적 분포 변화에 대한 일반화에서 가능성을 보여주지만, 새로운 작업으로의 일반화는 여전히 어려운 과제입니다. 예를 들어, 집기-놓기 작업으로 훈련된 언어 조건화 정책은 접기 작업의 팔 궤적이 집기-놓기와 유사하더라도 접기 작업으로 일반화할 수 없습니다. 우리의 핵심 통찰은 이러한 종류의 일반화가 대략적인 궤적 스케치를 통해 작업을 표현할 때 가능해진다는 것입니다. 우리는 이러한 대략적인 궤적 스케치를 사용하는 정책 조건화 방법을 제안하며, 이를 RT-Trajectory라고 부릅니다. 이 방법은 실용적이고 지정하기 쉬우며, 정책이 그렇지 않으면 수행하기 어려운 새로운 작업을 효과적으로 수행할 수 있게 합니다. 우리는 궤적 스케치가 저수준 동작 중심 지침을 표현할 만큼 상세하면서도, 학습된 정책이 상황별 시각적 관찰 맥락에서 궤적 스케치를 해석할 수 있을 만큼 대략적인 균형을 이룬다는 것을 발견했습니다. 또한, 궤적 스케치가 로봇 정책과 소통하기 위한 유용한 인터페이스를 제공할 수 있음을 보여줍니다. 이는 그림이나 비디오와 같은 간단한 인간 입력, 또는 현대 이미지 생성 또는 웨이포인트 생성 방법과 같은 자동화된 방법을 통해 지정될 수 있습니다. 우리는 다양한 실제 로봇 작업에서 RT-Trajectory를 대규모로 평가했으며, 동일한 훈련 데이터가 제공될 때 RT-Trajectory가 언어 조건화 및 목표 조건화 정책보다 더 넓은 범위의 작업을 수행할 수 있음을 발견했습니다.
