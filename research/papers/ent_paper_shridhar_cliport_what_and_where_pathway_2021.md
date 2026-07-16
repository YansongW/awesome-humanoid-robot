---
$id: ent_paper_shridhar_cliport_what_and_where_pathway_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLIPort: What and Where Pathways for Robotic Manipulation'
  zh: CLIPort
  ko: 'CLIPort: What and Where Pathways for Robotic Manipulation'
summary:
  en: 'CLIPort: What and Where Pathways for Robotic Manipulation (CLIPort), is a 2021 generalized vision-language-action model
    for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2021.'
  zh: 'CLIPort: What and Where Pathways for Robotic Manipulation (CLIPort), is a 2021 generalized vision-language-action model
    for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2021.'
  ko: 'CLIPort: What and Where Pathways for Robotic Manipulation (CLIPort), is a 2021 generalized vision-language-action model
    for robotic manipulation, introduced by University of Washington, NVIDIA, and published at CoRL 2021.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cliport
- generalist_policy
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2109.12098v1.
sources:
- id: src_001
  type: paper
  title: CLIPort source
  url: https://proceedings.mlr.press/v164/shridhar22a.html
  date: '2021'
  accessed_at: '2026-07-01'
---
## 概述
How can we imbue robots with the ability to manipulate objects precisely but also to reason about them in terms of abstract concepts? Recent works in manipulation have shown that end-to-end networks can learn dexterous skills that require precise spatial reasoning, but these methods often fail to generalize to new goals or quickly learn transferable concepts across tasks. In parallel, there has been great progress in learning generalizable semantic representations for vision and language by training on large-scale internet data, however these representations lack the spatial understanding necessary for fine-grained manipulation. To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation. Specifically, we present CLIPort, a language-conditioned imitation-learning agent that combines the broad semantic understanding (what) of CLIP [1] with the spatial precision (where) of Transporter [2]. Our end-to-end framework is capable of solving a variety of language-specified tabletop tasks from packing unseen objects to folding cloths, all without any explicit representations of object poses, instance segmentations, memory, symbolic states, or syntactic structures. Experiments in simulated and real-world settings show that our approach is data efficient in few-shot settings and generalizes effectively to seen and unseen semantic concepts. We even learn one multi-task policy for 10 simulated and 9 real-world tasks that is better or comparable to single-task policies.

## 核心内容
How can we imbue robots with the ability to manipulate objects precisely but also to reason about them in terms of abstract concepts? Recent works in manipulation have shown that end-to-end networks can learn dexterous skills that require precise spatial reasoning, but these methods often fail to generalize to new goals or quickly learn transferable concepts across tasks. In parallel, there has been great progress in learning generalizable semantic representations for vision and language by training on large-scale internet data, however these representations lack the spatial understanding necessary for fine-grained manipulation. To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation. Specifically, we present CLIPort, a language-conditioned imitation-learning agent that combines the broad semantic understanding (what) of CLIP [1] with the spatial precision (where) of Transporter [2]. Our end-to-end framework is capable of solving a variety of language-specified tabletop tasks from packing unseen objects to folding cloths, all without any explicit representations of object poses, instance segmentations, memory, symbolic states, or syntactic structures. Experiments in simulated and real-world settings show that our approach is data efficient in few-shot settings and generalizes effectively to seen and unseen semantic concepts. We even learn one multi-task policy for 10 simulated and 9 real-world tasks that is better or comparable to single-task policies.

## 参考
- http://arxiv.org/abs/2109.12098v1

## Overview
How can we imbue robots with the ability to manipulate objects precisely but also to reason about them in terms of abstract concepts? Recent works in manipulation have shown that end-to-end networks can learn dexterous skills that require precise spatial reasoning, but these methods often fail to generalize to new goals or quickly learn transferable concepts across tasks. In parallel, there has been great progress in learning generalizable semantic representations for vision and language by training on large-scale internet data, however these representations lack the spatial understanding necessary for fine-grained manipulation. To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation. Specifically, we present CLIPort, a language-conditioned imitation-learning agent that combines the broad semantic understanding (what) of CLIP [1] with the spatial precision (where) of Transporter [2]. Our end-to-end framework is capable of solving a variety of language-specified tabletop tasks from packing unseen objects to folding cloths, all without any explicit representations of object poses, instance segmentations, memory, symbolic states, or syntactic structures. Experiments in simulated and real-world settings show that our approach is data efficient in few-shot settings and generalizes effectively to seen and unseen semantic concepts. We even learn one multi-task policy for 10 simulated and 9 real-world tasks that is better or comparable to single-task policies.

## Content
How can we imbue robots with the ability to manipulate objects precisely but also to reason about them in terms of abstract concepts? Recent works in manipulation have shown that end-to-end networks can learn dexterous skills that require precise spatial reasoning, but these methods often fail to generalize to new goals or quickly learn transferable concepts across tasks. In parallel, there has been great progress in learning generalizable semantic representations for vision and language by training on large-scale internet data, however these representations lack the spatial understanding necessary for fine-grained manipulation. To this end, we propose a framework that combines the best of both worlds: a two-stream architecture with semantic and spatial pathways for vision-based manipulation. Specifically, we present CLIPort, a language-conditioned imitation-learning agent that combines the broad semantic understanding (what) of CLIP [1] with the spatial precision (where) of Transporter [2]. Our end-to-end framework is capable of solving a variety of language-specified tabletop tasks from packing unseen objects to folding cloths, all without any explicit representations of object poses, instance segmentations, memory, symbolic states, or syntactic structures. Experiments in simulated and real-world settings show that our approach is data efficient in few-shot settings and generalizes effectively to seen and unseen semantic concepts. We even learn one multi-task policy for 10 simulated and 9 real-world tasks that is better or comparable to single-task policies.

## 개요
로봇이 물체를 정밀하게 조작할 수 있을 뿐만 아니라 추상적 개념으로 사고할 수 있는 능력을 어떻게 부여할 수 있을까? 최근 조작 분야 연구들은 정밀한 공간 추론이 필요한 능숙한 기술을 종단간(end-to-end) 네트워크가 학습할 수 있음을 보여주었지만, 이러한 방법들은 새로운 목표에 일반화하거나 작업 간 전이 가능한 개념을 빠르게 학습하는 데 종종 실패합니다. 이와 동시에 대규모 인터넷 데이터 학습을 통해 시각 및 언어에 대한 일반화 가능한 의미 표현을 학습하는 데 큰 진전이 있었지만, 이러한 표현들은 세밀한 조작에 필요한 공간 이해가 부족합니다. 이러한 문제를 해결하기 위해 우리는 두 가지 장점을 결합한 프레임워크, 즉 시각 기반 조작을 위한 의미 경로와 공간 경로를 가진 이중 스트림(two-stream) 아키텍처를 제안합니다. 구체적으로, 우리는 CLIP [1]의 광범위한 의미 이해(무엇)와 Transporter [2]의 공간 정밀도(어디)를 결합한 언어 조건 모방 학습 에이전트 CLIPort를 제시합니다. 우리의 종단간 프레임워크는 물체 자세, 인스턴스 분할, 메모리, 기호 상태 또는 구문 구조에 대한 명시적 표현 없이도 보지 못한 물체 포장부터 천 접기까지 다양한 언어로 지정된 테이블탑 작업을 해결할 수 있습니다. 시뮬레이션 및 실제 환경 실험은 우리의 접근 방식이 소수 샷(few-shot) 설정에서 데이터 효율적이며, 본 및 미본 의미 개념에 효과적으로 일반화됨을 보여줍니다. 또한 10개의 시뮬레이션 작업과 9개의 실제 작업에 대해 단일 작업 정책보다 더 우수하거나 동등한 성능을 보이는 하나의 멀티태스크 정책을 학습했습니다.

## 핵심 내용
로봇이 물체를 정밀하게 조작할 수 있을 뿐만 아니라 추상적 개념으로 사고할 수 있는 능력을 어떻게 부여할 수 있을까? 최근 조작 분야 연구들은 정밀한 공간 추론이 필요한 능숙한 기술을 종단간 네트워크가 학습할 수 있음을 보여주었지만, 이러한 방법들은 새로운 목표에 일반화하거나 작업 간 전이 가능한 개념을 빠르게 학습하는 데 종종 실패합니다. 이와 동시에 대규모 인터넷 데이터 학습을 통해 시각 및 언어에 대한 일반화 가능한 의미 표현을 학습하는 데 큰 진전이 있었지만, 이러한 표현들은 세밀한 조작에 필요한 공간 이해가 부족합니다. 이러한 문제를 해결하기 위해 우리는 두 가지 장점을 결합한 프레임워크, 즉 시각 기반 조작을 위한 의미 경로와 공간 경로를 가진 이중 스트림 아키텍처를 제안합니다. 구체적으로, 우리는 CLIP [1]의 광범위한 의미 이해(무엇)와 Transporter [2]의 공간 정밀도(어디)를 결합한 언어 조건 모방 학습 에이전트 CLIPort를 제시합니다. 우리의 종단간 프레임워크는 물체 자세, 인스턴스 분할, 메모리, 기호 상태 또는 구문 구조에 대한 명시적 표현 없이도 보지 못한 물체 포장부터 천 접기까지 다양한 언어로 지정된 테이블탑 작업을 해결할 수 있습니다. 시뮬레이션 및 실제 환경 실험은 우리의 접근 방식이 소수 샷 설정에서 데이터 효율적이며, 본 및 미본 의미 개념에 효과적으로 일반화됨을 보여줍니다. 또한 10개의 시뮬레이션 작업과 9개의 실제 작업에 대해 단일 작업 정책보다 더 우수하거나 동등한 성능을 보이는 하나의 멀티태스크 정책을 학습했습니다.
