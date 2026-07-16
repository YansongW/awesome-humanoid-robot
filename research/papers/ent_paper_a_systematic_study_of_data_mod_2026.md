---
$id: ent_paper_a_systematic_study_of_data_mod_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation
  zh: A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation
  ko: A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation
summary:
  en: A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation is
    a 2026 work on manipulation for humanoid robots.
  zh: A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation is
    a 2026 work on manipulation for humanoid robots.
  ko: A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation is
    a 2026 work on manipulation for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_systematic_study_of_data_mod
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.01067v1.
sources:
- id: src_001
  type: website
  title: A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation
    project page
  url: https://co-training-lbm.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Large behavior models have shown strong dexterous manipulation capabilities by extending imitation learning to large-scale training on multi-task robot data, yet their generalization remains limited by the insufficient robot data coverage. To expand this coverage without costly additional data collection, recent work relies on co-training: jointly learning from target robot data and heterogeneous data modalities. However, how different co-training data modalities and strategies affect policy performance remains poorly understood. We present a large-scale empirical study examining five co-training data modalities: standard vision-language data, dense language annotations for robot trajectories, cross-embodiment robot data, human videos, and discrete robot action tokens across single- and multi-phase training strategies. Our study leverages 4,000 hours of robot and human manipulation data and 50M vision-language samples to train vision-language-action policies. We evaluate 89 policies over 58,000 simulation rollouts and 2,835 real-world rollouts. Our results show that co-training with forms of vision-language and cross-embodiment robot data substantially improves generalization to distribution shifts, unseen tasks, and language following, while discrete action token variants yield no significant benefits. Combining effective modalities produces cumulative gains and enables rapid adaptation to unseen long-horizon dexterous tasks via fine-tuning. Training exclusively on robot data degrades the visiolinguistic understanding of the vision-language model backbone, while co-training with effective modalities restores these capabilities. Explicitly conditioning action generation on chain-of-thought traces learned from co-training data does not improve performance in our simulation benchmark. Together, these results provide practical guidance for building scalable generalist robot policies.

## 核心内容
Large behavior models have shown strong dexterous manipulation capabilities by extending imitation learning to large-scale training on multi-task robot data, yet their generalization remains limited by the insufficient robot data coverage. To expand this coverage without costly additional data collection, recent work relies on co-training: jointly learning from target robot data and heterogeneous data modalities. However, how different co-training data modalities and strategies affect policy performance remains poorly understood. We present a large-scale empirical study examining five co-training data modalities: standard vision-language data, dense language annotations for robot trajectories, cross-embodiment robot data, human videos, and discrete robot action tokens across single- and multi-phase training strategies. Our study leverages 4,000 hours of robot and human manipulation data and 50M vision-language samples to train vision-language-action policies. We evaluate 89 policies over 58,000 simulation rollouts and 2,835 real-world rollouts. Our results show that co-training with forms of vision-language and cross-embodiment robot data substantially improves generalization to distribution shifts, unseen tasks, and language following, while discrete action token variants yield no significant benefits. Combining effective modalities produces cumulative gains and enables rapid adaptation to unseen long-horizon dexterous tasks via fine-tuning. Training exclusively on robot data degrades the visiolinguistic understanding of the vision-language model backbone, while co-training with effective modalities restores these capabilities. Explicitly conditioning action generation on chain-of-thought traces learned from co-training data does not improve performance in our simulation benchmark. Together, these results provide practical guidance for building scalable generalist robot policies.

## 参考
- http://arxiv.org/abs/2602.01067v1

## Overview
Large behavior models have shown strong dexterous manipulation capabilities by extending imitation learning to large-scale training on multi-task robot data, yet their generalization remains limited by the insufficient robot data coverage. To expand this coverage without costly additional data collection, recent work relies on co-training: jointly learning from target robot data and heterogeneous data modalities. However, how different co-training data modalities and strategies affect policy performance remains poorly understood. We present a large-scale empirical study examining five co-training data modalities: standard vision-language data, dense language annotations for robot trajectories, cross-embodiment robot data, human videos, and discrete robot action tokens across single- and multi-phase training strategies. Our study leverages 4,000 hours of robot and human manipulation data and 50M vision-language samples to train vision-language-action policies. We evaluate 89 policies over 58,000 simulation rollouts and 2,835 real-world rollouts. Our results show that co-training with forms of vision-language and cross-embodiment robot data substantially improves generalization to distribution shifts, unseen tasks, and language following, while discrete action token variants yield no significant benefits. Combining effective modalities produces cumulative gains and enables rapid adaptation to unseen long-horizon dexterous tasks via fine-tuning. Training exclusively on robot data degrades the visiolinguistic understanding of the vision-language model backbone, while co-training with effective modalities restores these capabilities. Explicitly conditioning action generation on chain-of-thought traces learned from co-training data does not improve performance in our simulation benchmark. Together, these results provide practical guidance for building scalable generalist robot policies.

## Content
Large behavior models have shown strong dexterous manipulation capabilities by extending imitation learning to large-scale training on multi-task robot data, yet their generalization remains limited by the insufficient robot data coverage. To expand this coverage without costly additional data collection, recent work relies on co-training: jointly learning from target robot data and heterogeneous data modalities. However, how different co-training data modalities and strategies affect policy performance remains poorly understood. We present a large-scale empirical study examining five co-training data modalities: standard vision-language data, dense language annotations for robot trajectories, cross-embodiment robot data, human videos, and discrete robot action tokens across single- and multi-phase training strategies. Our study leverages 4,000 hours of robot and human manipulation data and 50M vision-language samples to train vision-language-action policies. We evaluate 89 policies over 58,000 simulation rollouts and 2,835 real-world rollouts. Our results show that co-training with forms of vision-language and cross-embodiment robot data substantially improves generalization to distribution shifts, unseen tasks, and language following, while discrete action token variants yield no significant benefits. Combining effective modalities produces cumulative gains and enables rapid adaptation to unseen long-horizon dexterous tasks via fine-tuning. Training exclusively on robot data degrades the visiolinguistic understanding of the vision-language model backbone, while co-training with effective modalities restores these capabilities. Explicitly conditioning action generation on chain-of-thought traces learned from co-training data does not improve performance in our simulation benchmark. Together, these results provide practical guidance for building scalable generalist robot policies.

## 개요
대규모 행동 모델(Large behavior models)은 모방 학습을 다중 작업 로봇 데이터에 대한 대규모 훈련으로 확장함으로써 강력한 정밀 조작 능력을 보여주었지만, 일반화 능력은 여전히 불충분한 로봇 데이터 범위로 인해 제한됩니다. 비용이 많이 드는 추가 데이터 수집 없이 이 범위를 확장하기 위해 최근 연구는 공동 훈련(co-training)에 의존합니다: 대상 로봇 데이터와 이질적인 데이터 양식(heterogeneous data modalities)으로부터 공동으로 학습하는 것입니다. 그러나 서로 다른 공동 훈련 데이터 양식과 전략이 정책 성능에 어떻게 영향을 미치는지는 아직 잘 이해되지 않고 있습니다. 우리는 다섯 가지 공동 훈련 데이터 양식(표준 시각-언어 데이터, 로봇 궤적에 대한 밀집 언어 주석, 교차 구현 로봇 데이터, 인간 비디오, 이산 로봇 행동 토큰)을 단일 단계 및 다단계 훈련 전략에 걸쳐 조사하는 대규모 경험적 연구를 제시합니다. 본 연구는 4,000시간의 로봇 및 인간 조작 데이터와 5천만 개의 시각-언어 샘플을 활용하여 시각-언어-행동 정책을 훈련합니다. 우리는 58,000회의 시뮬레이션 롤아웃과 2,835회의 실제 롤아웃에 걸쳐 89개의 정책을 평가합니다. 결과에 따르면 시각-언어 및 교차 구현 로봇 데이터 형태의 공동 훈련은 분포 변화, 보지 못한 작업, 언어 따르기(언어 지시 수행)에 대한 일반화를 크게 향상시키는 반면, 이산 행동 토큰 변형은 유의미한 이점을 제공하지 않습니다. 효과적인 양식을 결합하면 누적 이득이 발생하고 미세 조정을 통해 보지 못한 장기 정밀 작업에 대한 빠른 적응이 가능해집니다. 로봇 데이터만으로 훈련하면 시각-언어 모델 백본의 시각-언어 이해 능력이 저하되지만, 효과적인 양식으로 공동 훈련하면 이러한 능력이 회복됩니다. 공동 훈련 데이터에서 학습된 사고 사슬(chain-of-thought) 추적에 행동 생성을 명시적으로 조건화하는 것은 시뮬레이션 벤치마크에서 성능을 향상시키지 않습니다. 종합적으로, 이러한 결과는 확장 가능한 범용 로봇 정책을 구축하기 위한 실용적인 지침을 제공합니다.

## 핵심 내용
대규모 행동 모델(Large behavior models)은 모방 학습을 다중 작업 로봇 데이터에 대한 대규모 훈련으로 확장함으로써 강력한 정밀 조작 능력을 보여주었지만, 일반화 능력은 여전히 불충분한 로봇 데이터 범위로 인해 제한됩니다. 비용이 많이 드는 추가 데이터 수집 없이 이 범위를 확장하기 위해 최근 연구는 공동 훈련(co-training)에 의존합니다: 대상 로봇 데이터와 이질적인 데이터 양식(heterogeneous data modalities)으로부터 공동으로 학습하는 것입니다. 그러나 서로 다른 공동 훈련 데이터 양식과 전략이 정책 성능에 어떻게 영향을 미치는지는 아직 잘 이해되지 않고 있습니다. 우리는 다섯 가지 공동 훈련 데이터 양식(표준 시각-언어 데이터, 로봇 궤적에 대한 밀집 언어 주석, 교차 구현 로봇 데이터, 인간 비디오, 이산 로봇 행동 토큰)을 단일 단계 및 다단계 훈련 전략에 걸쳐 조사하는 대규모 경험적 연구를 제시합니다. 본 연구는 4,000시간의 로봇 및 인간 조작 데이터와 5천만 개의 시각-언어 샘플을 활용하여 시각-언어-행동 정책을 훈련합니다. 우리는 58,000회의 시뮬레이션 롤아웃과 2,835회의 실제 롤아웃에 걸쳐 89개의 정책을 평가합니다. 결과에 따르면 시각-언어 및 교차 구현 로봇 데이터 형태의 공동 훈련은 분포 변화, 보지 못한 작업, 언어 따르기(언어 지시 수행)에 대한 일반화를 크게 향상시키는 반면, 이산 행동 토큰 변형은 유의미한 이점을 제공하지 않습니다. 효과적인 양식을 결합하면 누적 이득이 발생하고 미세 조정을 통해 보지 못한 장기 정밀 작업에 대한 빠른 적응이 가능해집니다. 로봇 데이터만으로 훈련하면 시각-언어 모델 백본의 시각-언어 이해 능력이 저하되지만, 효과적인 양식으로 공동 훈련하면 이러한 능력이 회복됩니다. 공동 훈련 데이터에서 학습된 사고 사슬(chain-of-thought) 추적에 행동 생성을 명시적으로 조건화하는 것은 시뮬레이션 벤치마크에서 성능을 향상시키지 않습니다. 종합적으로, 이러한 결과는 확장 가능한 범용 로봇 정책을 구축하기 위한 실용적인 지침을 제공합니다.
