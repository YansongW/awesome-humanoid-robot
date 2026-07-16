---
$id: ent_paper_intelligence_05_a_vision_language_action_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'π0.5: a Vision-Language-Action Model with Open-World Generalization'
  zh: π0.5
  ko: 'π0.5: a Vision-Language-Action Model with Open-World Generalization'
summary:
  en: 'π0.5: a Vision-Language-Action Model with Open-World Generalization (π0.5), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, and published at CoRL25.'
  zh: 'π0.5: a Vision-Language-Action Model with Open-World Generalization (π0.5), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, and published at CoRL25.'
  ko: 'π0.5: a Vision-Language-Action Model with Open-World Generalization (π0.5), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- '05'
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.16054v1.
sources:
- id: src_001
  type: paper
  title: 'π0.5: a Vision-Language-Action Model with Open-World Generalization (arXiv)'
  url: https://arxiv.org/abs/2504.16054
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: π0.5 source
  url: https://doi.org/10.48550/arXiv.2504.16054
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In order for robots to be useful, they must perform practically relevant tasks in the real world, outside of the lab. While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the wild. We describe $π_{0.5}$, a new model based on $π_{0}$ that uses co-training on heterogeneous tasks to enable broad generalization. $π_{0.5}$\ uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation. Our system uses a combination of co-training and hybrid multi-modal examples that combine image observations, language commands, object detections, semantic subtask prediction, and low-level actions. Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end learning-enabled robotic system can perform long-horizon and dexterous manipulation skills, such as cleaning a kitchen or bedroom, in entirely new homes.

## 核心内容
In order for robots to be useful, they must perform practically relevant tasks in the real world, outside of the lab. While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the wild. We describe $π_{0.5}$, a new model based on $π_{0}$ that uses co-training on heterogeneous tasks to enable broad generalization. $π_{0.5}$\ uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation. Our system uses a combination of co-training and hybrid multi-modal examples that combine image observations, language commands, object detections, semantic subtask prediction, and low-level actions. Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end learning-enabled robotic system can perform long-horizon and dexterous manipulation skills, such as cleaning a kitchen or bedroom, in entirely new homes.

## 参考
- http://arxiv.org/abs/2504.16054v1

## Overview
In order for robots to be useful, they must perform practically relevant tasks in the real world, outside of the lab. While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the wild. We describe $π_{0.5}$, a new model based on $π_{0}$ that uses co-training on heterogeneous tasks to enable broad generalization. $π_{0.5}$ uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation. Our system uses a combination of co-training and hybrid multi-modal examples that combine image observations, language commands, object detections, semantic subtask prediction, and low-level actions. Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end learning-enabled robotic system can perform long-horizon and dexterous manipulation skills, such as cleaning a kitchen or bedroom, in entirely new homes.

## Content
In order for robots to be useful, they must perform practically relevant tasks in the real world, outside of the lab. While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the wild. We describe $π_{0.5}$, a new model based on $π_{0}$ that uses co-training on heterogeneous tasks to enable broad generalization. $π_{0.5}$ uses data from multiple robots, high-level semantic prediction, web data, and other sources to enable broadly generalizable real-world robotic manipulation. Our system uses a combination of co-training and hybrid multi-modal examples that combine image observations, language commands, object detections, semantic subtask prediction, and low-level actions. Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end learning-enabled robotic system can perform long-horizon and dexterous manipulation skills, such as cleaning a kitchen or bedroom, in entirely new homes.

## 개요
로봇이 유용하려면 실험실 밖 실제 세계에서 실질적으로 관련된 작업을 수행해야 합니다. 비전-언어-행동(VLA) 모델은 엔드투엔드 로봇 제어에서 인상적인 결과를 보여주었지만, 이러한 모델이 실제 환경에서 얼마나 일반화될 수 있는지는 여전히 미해결 과제입니다. 우리는 $π_{0}$를 기반으로 한 새로운 모델 $π_{0.5}$를 설명하며, 이 모델은 이질적인 작업에 대한 공동 훈련을 통해 광범위한 일반화를 가능하게 합니다. $π_{0.5}$는 여러 로봇의 데이터, 고수준 의미 예측, 웹 데이터 및 기타 소스를 활용하여 광범위하게 일반화 가능한 실제 세계 로봇 조작을 구현합니다. 우리 시스템은 이미지 관찰, 언어 명령, 객체 탐지, 의미 하위 작업 예측 및 저수준 행동을 결합한 공동 훈련과 하이브리드 멀티모달 예제의 조합을 사용합니다. 실험 결과는 이러한 종류의 지식 전이가 효과적인 일반화에 필수적임을 보여주며, 엔드투엔드 학습 기반 로봇 시스템이 완전히 새로운 가정에서 주방이나 침실 청소와 같은 장기적이고 정교한 조작 기술을 수행할 수 있음을 처음으로 입증합니다.

## 핵심 내용
로봇이 유용하려면 실험실 밖 실제 세계에서 실질적으로 관련된 작업을 수행해야 합니다. 비전-언어-행동(VLA) 모델은 엔드투엔드 로봇 제어에서 인상적인 결과를 보여주었지만, 이러한 모델이 실제 환경에서 얼마나 일반화될 수 있는지는 여전히 미해결 과제입니다. 우리는 $π_{0}$를 기반으로 한 새로운 모델 $π_{0.5}$를 설명하며, 이 모델은 이질적인 작업에 대한 공동 훈련을 통해 광범위한 일반화를 가능하게 합니다. $π_{0.5}$는 여러 로봇의 데이터, 고수준 의미 예측, 웹 데이터 및 기타 소스를 활용하여 광범위하게 일반화 가능한 실제 세계 로봇 조작을 구현합니다. 우리 시스템은 이미지 관찰, 언어 명령, 객체 탐지, 의미 하위 작업 예측 및 저수준 행동을 결합한 공동 훈련과 하이브리드 멀티모달 예제의 조합을 사용합니다. 실험 결과는 이러한 종류의 지식 전이가 효과적인 일반화에 필수적임을 보여주며, 엔드투엔드 학습 기반 로봇 시스템이 완전히 새로운 가정에서 주방이나 침실 청소와 같은 장기적이고 정교한 조작 기술을 수행할 수 있음을 처음으로 입증합니다.
