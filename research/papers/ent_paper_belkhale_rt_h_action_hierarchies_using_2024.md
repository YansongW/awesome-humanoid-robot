---
$id: ent_paper_belkhale_rt_h_action_hierarchies_using_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RT-H: Action Hierarchies Using Language'
  zh: RT-H
  ko: 'RT-H: Action Hierarchies Using Language'
summary:
  en: 'RT-H: Action Hierarchies Using Language (RT-H), is a 2024 large vision-language-action model for robotic manipulation,
    introduced by Google DeepMind, and published at Robotics - Science and Systems 2024.'
  zh: 'RT-H: Action Hierarchies Using Language (RT-H), is a 2024 large vision-language-action model for robotic manipulation,
    introduced by Google DeepMind, and published at Robotics - Science and Systems 2024.'
  ko: 'RT-H: Action Hierarchies Using Language (RT-H), is a 2024 large vision-language-action model for robotic manipulation,
    introduced by Google DeepMind, and published at Robotics - Science and Systems 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- rt_h
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.01823v2.
sources:
- id: src_001
  type: website
  title: RT-H source
  url: https://doi.org/10.15607/RSS.2024.XX.049
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Language provides a way to break down complex concepts into digestible pieces. Recent works in robot imitation learning use language-conditioned policies that predict actions given visual observations and the high-level task specified in language. These methods leverage the structure of natural language to share data between semantically similar tasks (e.g., "pick coke can" and "pick an apple") in multi-task datasets. However, as tasks become more semantically diverse (e.g., "pick coke can" and "pour cup"), sharing data between tasks becomes harder, so learning to map high-level tasks to actions requires much more demonstration data. To bridge tasks and actions, our insight is to teach the robot the language of actions, describing low-level motions with more fine-grained phrases like "move arm forward". Predicting these language motions as an intermediate step between tasks and actions forces the policy to learn the shared structure of low-level motions across seemingly disparate tasks. Furthermore, a policy that is conditioned on language motions can easily be corrected during execution through human-specified language motions. This enables a new paradigm for flexible policies that can learn from human intervention in language. Our method RT-H builds an action hierarchy using language motions: it first learns to predict language motions, and conditioned on this and the high-level task, it predicts actions, using visual context at all stages. We show that RT-H leverages this language-action hierarchy to learn policies that are more robust and flexible by effectively tapping into multi-task datasets. We show that these policies not only allow for responding to language interventions, but can also learn from such interventions and outperform methods that learn from teleoperated interventions. Our website and videos are found at https://rt-hierarchy.github.io.

## 核心内容
Language provides a way to break down complex concepts into digestible pieces. Recent works in robot imitation learning use language-conditioned policies that predict actions given visual observations and the high-level task specified in language. These methods leverage the structure of natural language to share data between semantically similar tasks (e.g., "pick coke can" and "pick an apple") in multi-task datasets. However, as tasks become more semantically diverse (e.g., "pick coke can" and "pour cup"), sharing data between tasks becomes harder, so learning to map high-level tasks to actions requires much more demonstration data. To bridge tasks and actions, our insight is to teach the robot the language of actions, describing low-level motions with more fine-grained phrases like "move arm forward". Predicting these language motions as an intermediate step between tasks and actions forces the policy to learn the shared structure of low-level motions across seemingly disparate tasks. Furthermore, a policy that is conditioned on language motions can easily be corrected during execution through human-specified language motions. This enables a new paradigm for flexible policies that can learn from human intervention in language. Our method RT-H builds an action hierarchy using language motions: it first learns to predict language motions, and conditioned on this and the high-level task, it predicts actions, using visual context at all stages. We show that RT-H leverages this language-action hierarchy to learn policies that are more robust and flexible by effectively tapping into multi-task datasets. We show that these policies not only allow for responding to language interventions, but can also learn from such interventions and outperform methods that learn from teleoperated interventions. Our website and videos are found at https://rt-hierarchy.github.io.

## 参考
- http://arxiv.org/abs/2403.01823v2

## Overview
Language provides a way to break down complex concepts into digestible pieces. Recent works in robot imitation learning use language-conditioned policies that predict actions given visual observations and the high-level task specified in language. These methods leverage the structure of natural language to share data between semantically similar tasks (e.g., "pick coke can" and "pick an apple") in multi-task datasets. However, as tasks become more semantically diverse (e.g., "pick coke can" and "pour cup"), sharing data between tasks becomes harder, so learning to map high-level tasks to actions requires much more demonstration data. To bridge tasks and actions, our insight is to teach the robot the language of actions, describing low-level motions with more fine-grained phrases like "move arm forward". Predicting these language motions as an intermediate step between tasks and actions forces the policy to learn the shared structure of low-level motions across seemingly disparate tasks. Furthermore, a policy that is conditioned on language motions can easily be corrected during execution through human-specified language motions. This enables a new paradigm for flexible policies that can learn from human intervention in language. Our method RT-H builds an action hierarchy using language motions: it first learns to predict language motions, and conditioned on this and the high-level task, it predicts actions, using visual context at all stages. We show that RT-H leverages this language-action hierarchy to learn policies that are more robust and flexible by effectively tapping into multi-task datasets. We show that these policies not only allow for responding to language interventions, but can also learn from such interventions and outperform methods that learn from teleoperated interventions. Our website and videos are found at https://rt-hierarchy.github.io.

## Content
Language provides a way to break down complex concepts into digestible pieces. Recent works in robot imitation learning use language-conditioned policies that predict actions given visual observations and the high-level task specified in language. These methods leverage the structure of natural language to share data between semantically similar tasks (e.g., "pick coke can" and "pick an apple") in multi-task datasets. However, as tasks become more semantically diverse (e.g., "pick coke can" and "pour cup"), sharing data between tasks becomes harder, so learning to map high-level tasks to actions requires much more demonstration data. To bridge tasks and actions, our insight is to teach the robot the language of actions, describing low-level motions with more fine-grained phrases like "move arm forward". Predicting these language motions as an intermediate step between tasks and actions forces the policy to learn the shared structure of low-level motions across seemingly disparate tasks. Furthermore, a policy that is conditioned on language motions can easily be corrected during execution through human-specified language motions. This enables a new paradigm for flexible policies that can learn from human intervention in language. Our method RT-H builds an action hierarchy using language motions: it first learns to predict language motions, and conditioned on this and the high-level task, it predicts actions, using visual context at all stages. We show that RT-H leverages this language-action hierarchy to learn policies that are more robust and flexible by effectively tapping into multi-task datasets. We show that these policies not only allow for responding to language interventions, but can also learn from such interventions and outperform methods that learn from teleoperated interventions. Our website and videos are found at https://rt-hierarchy.github.io.

## 개요
언어는 복잡한 개념을 이해하기 쉬운 조각으로 분해하는 방법을 제공합니다. 최근 로봇 모방 학습 연구에서는 시각적 관찰과 언어로 지정된 고수준 작업이 주어졌을 때 행동을 예측하는 언어 조건화 정책을 사용합니다. 이러한 방법은 자연어의 구조를 활용하여 다중 작업 데이터셋에서 의미적으로 유사한 작업(예: "콜라 캔 집기"와 "사과 집기") 간에 데이터를 공유합니다. 그러나 작업이 의미적으로 더 다양해질수록(예: "콜라 캔 집기"와 "컵 따르기") 작업 간 데이터 공유가 어려워지므로, 고수준 작업을 행동에 매핑하는 방법을 학습하려면 훨씬 더 많은 시연 데이터가 필요합니다. 작업과 행동을 연결하기 위해, 우리의 통찰은 로봇에게 행동의 언어를 가르쳐 "팔을 앞으로 움직이기"와 같은 더 세분화된 구문으로 저수준 동작을 설명하는 것입니다. 이러한 언어 동작을 작업과 행동 사이의 중간 단계로 예측하면, 정책이 겉보기에 서로 다른 작업 간에 저수준 동작의 공유 구조를 학습하도록 강제합니다. 또한, 언어 동작에 조건화된 정책은 실행 중 인간이 지정한 언어 동작을 통해 쉽게 수정될 수 있습니다. 이는 언어로 된 인간의 개입으로부터 학습할 수 있는 유연한 정책을 위한 새로운 패러다임을 가능하게 합니다. 우리의 방법 RT-H는 언어 동작을 사용하여 행동 계층 구조를 구축합니다. 먼저 언어 동작을 예측하는 방법을 학습하고, 이를 고수준 작업과 함께 조건화하여 모든 단계에서 시각적 맥락을 사용하여 행동을 예측합니다. 우리는 RT-H가 이 언어-행동 계층 구조를 활용하여 다중 작업 데이터셋을 효과적으로 활용함으로써 더 강건하고 유연한 정책을 학습함을 보여줍니다. 이러한 정책은 언어 개입에 응답할 수 있을 뿐만 아니라, 이러한 개입으로부터 학습하여 원격 조작 개입으로부터 학습하는 방법보다 뛰어난 성능을 보입니다. 우리의 웹사이트와 비디오는 https://rt-hierarchy.github.io에서 확인할 수 있습니다.

## 핵심 내용
언어는 복잡한 개념을 이해하기 쉬운 조각으로 분해하는 방법을 제공합니다. 최근 로봇 모방 학습 연구에서는 시각적 관찰과 언어로 지정된 고수준 작업이 주어졌을 때 행동을 예측하는 언어 조건화 정책을 사용합니다. 이러한 방법은 자연어의 구조를 활용하여 다중 작업 데이터셋에서 의미적으로 유사한 작업(예: "콜라 캔 집기"와 "사과 집기") 간에 데이터를 공유합니다. 그러나 작업이 의미적으로 더 다양해질수록(예: "콜라 캔 집기"와 "컵 따르기") 작업 간 데이터 공유가 어려워지므로, 고수준 작업을 행동에 매핑하는 방법을 학습하려면 훨씬 더 많은 시연 데이터가 필요합니다. 작업과 행동을 연결하기 위해, 우리의 통찰은 로봇에게 행동의 언어를 가르쳐 "팔을 앞으로 움직이기"와 같은 더 세분화된 구문으로 저수준 동작을 설명하는 것입니다. 이러한 언어 동작을 작업과 행동 사이의 중간 단계로 예측하면, 정책이 겉보기에 서로 다른 작업 간에 저수준 동작의 공유 구조를 학습하도록 강제합니다. 또한, 언어 동작에 조건화된 정책은 실행 중 인간이 지정한 언어 동작을 통해 쉽게 수정될 수 있습니다. 이는 언어로 된 인간의 개입으로부터 학습할 수 있는 유연한 정책을 위한 새로운 패러다임을 가능하게 합니다. 우리의 방법 RT-H는 언어 동작을 사용하여 행동 계층 구조를 구축합니다. 먼저 언어 동작을 예측하는 방법을 학습하고, 이를 고수준 작업과 함께 조건화하여 모든 단계에서 시각적 맥락을 사용하여 행동을 예측합니다. 우리는 RT-H가 이 언어-행동 계층 구조를 활용하여 다중 작업 데이터셋을 효과적으로 활용함으로써 더 강건하고 유연한 정책을 학습함을 보여줍니다. 이러한 정책은 언어 개입에 응답할 수 있을 뿐만 아니라, 이러한 개입으로부터 학습하여 원격 조작 개입으로부터 학습하는 방법보다 뛰어난 성능을 보입니다. 우리의 웹사이트와 비디오는 https://rt-hierarchy.github.io에서 확인할 수 있습니다.
