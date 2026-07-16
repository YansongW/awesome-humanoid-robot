---
$id: ent_paper_green_using_physiological_measures_g_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Using Physiological Measures, Gaze, and Facial Expressions to Model Human Trust in a Robot Partner
  zh: 利用生理指标、注视和面部表情建模人类对机器人伙伴的信任
  ko: 생리적 측정, 시선, 그리고 표정을 사용한 로봇 파트너에 대한 인간 신뢰 모델링
summary:
  en: This paper presents an in-person human-robot supervisory interaction study that collects multimodal physiological, gaze,
    and facial-expression data to train machine-learning classifiers predicting human trust in a Franka Emika Panda robot
    partner.
  zh: 本文开展了一项面对面的人机监督交互研究，采集多模态生理、注视和面部表情数据，训练机器学习分类器以预测人类对Franka Emika Panda机器人伙伴的信任度。
  ko: 본 논문은 대면 인간-로봇 감독 상호작용 연구를 수행하여 다중 모달 생리학적 데이터, 시선 데이터, 그리고 표정 데이터를 수집하고, 이를 기반으로 Franka Emika Panda 로봇 파트너에 대한 인간의
    신뢰를 예측하는 머신러닝 분류기를 학습시킨다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- human_robot_interaction
- trust_modeling
- physiological_sensing
- gaze_tracking
- facial_action_units
- multimodal_fusion
- machine_learning
- collaborative_robot
- supervisory_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.05291v1.
sources:
- id: src_001
  type: paper
  title: Using Physiological Measures, Gaze, and Facial Expressions to Model Human Trust in a Robot Partner
  url: https://arxiv.org/abs/2504.05291
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
With robots becoming increasingly prevalent in various domains, it has become crucial to equip them with tools to achieve greater fluency in interactions with humans. One of the promising areas for further exploration lies in human trust. A real-time, objective model of human trust could be used to maximize productivity, preserve safety, and mitigate failure. In this work, we attempt to use physiological measures, gaze, and facial expressions to model human trust in a robot partner. We are the first to design an in-person, human-robot supervisory interaction study to create a dedicated trust dataset. Using this dataset, we train machine learning algorithms to identify the objective measures that are most indicative of trust in a robot partner, advancing trust prediction in human-robot interactions. Our findings indicate that a combination of sensor modalities (blood volume pulse, electrodermal activity, skin temperature, and gaze) can enhance the accuracy of detecting human trust in a robot partner. Furthermore, the Extra Trees, Random Forest, and Decision Trees classifiers exhibit consistently better performance in measuring the person's trust in the robot partner. These results lay the groundwork for constructing a real-time trust model for human-robot interaction, which could foster more efficient interactions between humans and robots.

## 核心内容
With robots becoming increasingly prevalent in various domains, it has become crucial to equip them with tools to achieve greater fluency in interactions with humans. One of the promising areas for further exploration lies in human trust. A real-time, objective model of human trust could be used to maximize productivity, preserve safety, and mitigate failure. In this work, we attempt to use physiological measures, gaze, and facial expressions to model human trust in a robot partner. We are the first to design an in-person, human-robot supervisory interaction study to create a dedicated trust dataset. Using this dataset, we train machine learning algorithms to identify the objective measures that are most indicative of trust in a robot partner, advancing trust prediction in human-robot interactions. Our findings indicate that a combination of sensor modalities (blood volume pulse, electrodermal activity, skin temperature, and gaze) can enhance the accuracy of detecting human trust in a robot partner. Furthermore, the Extra Trees, Random Forest, and Decision Trees classifiers exhibit consistently better performance in measuring the person's trust in the robot partner. These results lay the groundwork for constructing a real-time trust model for human-robot interaction, which could foster more efficient interactions between humans and robots.

## 参考
- http://arxiv.org/abs/2504.05291v1

## Overview
With robots becoming increasingly prevalent in various domains, it has become crucial to equip them with tools to achieve greater fluency in interactions with humans. One of the promising areas for further exploration lies in human trust. A real-time, objective model of human trust could be used to maximize productivity, preserve safety, and mitigate failure. In this work, we attempt to use physiological measures, gaze, and facial expressions to model human trust in a robot partner. We are the first to design an in-person, human-robot supervisory interaction study to create a dedicated trust dataset. Using this dataset, we train machine learning algorithms to identify the objective measures that are most indicative of trust in a robot partner, advancing trust prediction in human-robot interactions. Our findings indicate that a combination of sensor modalities (blood volume pulse, electrodermal activity, skin temperature, and gaze) can enhance the accuracy of detecting human trust in a robot partner. Furthermore, the Extra Trees, Random Forest, and Decision Trees classifiers exhibit consistently better performance in measuring the person's trust in the robot partner. These results lay the groundwork for constructing a real-time trust model for human-robot interaction, which could foster more efficient interactions between humans and robots.

## Content
With robots becoming increasingly prevalent in various domains, it has become crucial to equip them with tools to achieve greater fluency in interactions with humans. One of the promising areas for further exploration lies in human trust. A real-time, objective model of human trust could be used to maximize productivity, preserve safety, and mitigate failure. In this work, we attempt to use physiological measures, gaze, and facial expressions to model human trust in a robot partner. We are the first to design an in-person, human-robot supervisory interaction study to create a dedicated trust dataset. Using this dataset, we train machine learning algorithms to identify the objective measures that are most indicative of trust in a robot partner, advancing trust prediction in human-robot interactions. Our findings indicate that a combination of sensor modalities (blood volume pulse, electrodermal activity, skin temperature, and gaze) can enhance the accuracy of detecting human trust in a robot partner. Furthermore, the Extra Trees, Random Forest, and Decision Trees classifiers exhibit consistently better performance in measuring the person's trust in the robot partner. These results lay the groundwork for constructing a real-time trust model for human-robot interaction, which could foster more efficient interactions between humans and robots.

## 개요
로봇이 다양한 분야에서 점점 더 보편화됨에 따라, 인간과의 상호작용에서 더 큰 유창성을 달성할 수 있는 도구를 로봇에 탑재하는 것이 중요해졌습니다. 추가 탐구가 필요한 유망한 영역 중 하나는 인간의 신뢰입니다. 실시간으로 객관적인 인간 신뢰 모델은 생산성을 극대화하고 안전을 유지하며 실패를 완화하는 데 사용될 수 있습니다. 본 연구에서는 생리적 측정, 시선, 표정을 사용하여 로봇 파트너에 대한 인간의 신뢰를 모델링하려고 시도합니다. 우리는 최초로 대면 인간-로봇 감독 상호작용 연구를 설계하여 전용 신뢰 데이터셋을 생성했습니다. 이 데이터셋을 사용하여 머신러닝 알고리즘을 훈련시켜 로봇 파트너에 대한 신뢰를 가장 잘 나타내는 객관적 측정치를 식별함으로써 인간-로봇 상호작용에서의 신뢰 예측을 발전시킵니다. 연구 결과는 센서 모달리티(혈액량 맥파, 전기피부활동, 피부 온도, 시선)의 조합이 로봇 파트너에 대한 인간의 신뢰 감지 정확도를 향상시킬 수 있음을 보여줍니다. 또한, Extra Trees, Random Forest, Decision Trees 분류기가 로봇 파트너에 대한 개인의 신뢰를 측정하는 데 일관되게 더 나은 성능을 보였습니다. 이러한 결과는 인간-로봇 상호작용을 위한 실시간 신뢰 모델 구축의 기초를 마련하며, 이는 인간과 로봇 간의 더 효율적인 상호작용을 촉진할 수 있습니다.

## 핵심 내용
로봇이 다양한 분야에서 점점 더 보편화됨에 따라, 인간과의 상호작용에서 더 큰 유창성을 달성할 수 있는 도구를 로봇에 탑재하는 것이 중요해졌습니다. 추가 탐구가 필요한 유망한 영역 중 하나는 인간의 신뢰입니다. 실시간으로 객관적인 인간 신뢰 모델은 생산성을 극대화하고 안전을 유지하며 실패를 완화하는 데 사용될 수 있습니다. 본 연구에서는 생리적 측정, 시선, 표정을 사용하여 로봇 파트너에 대한 인간의 신뢰를 모델링하려고 시도합니다. 우리는 최초로 대면 인간-로봇 감독 상호작용 연구를 설계하여 전용 신뢰 데이터셋을 생성했습니다. 이 데이터셋을 사용하여 머신러닝 알고리즘을 훈련시켜 로봇 파트너에 대한 신뢰를 가장 잘 나타내는 객관적 측정치를 식별함으로써 인간-로봇 상호작용에서의 신뢰 예측을 발전시킵니다. 연구 결과는 센서 모달리티(혈액량 맥파, 전기피부활동, 피부 온도, 시선)의 조합이 로봇 파트너에 대한 인간의 신뢰 감지 정확도를 향상시킬 수 있음을 보여줍니다. 또한, Extra Trees, Random Forest, Decision Trees 분류기가 로봇 파트너에 대한 개인의 신뢰를 측정하는 데 일관되게 더 나은 성능을 보였습니다. 이러한 결과는 인간-로봇 상호작용을 위한 실시간 신뢰 모델 구축의 기초를 마련하며, 이는 인간과 로봇 간의 더 효율적인 상호작용을 촉진할 수 있습니다.
