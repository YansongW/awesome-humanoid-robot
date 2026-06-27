---
$id: ent_paper_green_using_physiological_measures_g_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Using Physiological Measures, Gaze, and Facial Expressions to Model Human Trust
    in a Robot Partner
  zh: 利用生理指标、注视和面部表情建模人类对机器人伙伴的信任
  ko: 생리적 측정, 시선, 그리고 표정을 사용한 로봇 파트너에 대한 인간 신뢰 모델링
summary:
  en: This paper presents an in-person human-robot supervisory interaction study that
    collects multimodal physiological, gaze, and facial-expression data to train machine-learning
    classifiers predicting human trust in a Franka Emika Panda robot partner.
  zh: 本文开展了一项面对面的人机监督交互研究，采集多模态生理、注视和面部表情数据，训练机器学习分类器以预测人类对Franka Emika Panda机器人伙伴的信任度。
  ko: 본 논문은 대면 인간-로봇 감독 상호작용 연구를 수행하여 다중 모달 생리학적 데이터, 시선 데이터, 그리고 표정 데이터를 수집하고, 이를
    기반으로 Franka Emika Panda 로봇 파트너에 대한 인간의 신뢰를 예측하는 머신러닝 분류기를 학습시킨다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; full-text review is
    required before marking verified.
sources:
- id: src_001
  type: paper
  title: Using Physiological Measures, Gaze, and Facial Expressions to Model Human
    Trust in a Robot Partner
  url: https://arxiv.org/abs/2504.05291
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Green and Iqbal conduct an in-person, supervisory human-robot interaction study to build a dedicated dataset for modeling human trust in a robot partner. Participants interacted with a Franka Emika Panda robot arm while wearing an Empatica E4 wristwatch, Pupil Invisible eye-tracking glasses, and being recorded by a high-definition camera. The recorded modalities include blood volume pulse (BVP), electrodermal activity (EDA), skin temperature (TEMP), gaze data, and facial action units extracted via OpenFace. Trust is treated as a scaled Likert value rather than a binary label in order to capture its dynamic nature.

The authors train and evaluate six shallow machine-learning classifiers—Random Forest (RF), Extra Trees (ET), Linear Discriminant Analysis (LDA), Logistic Regression (LR), Decision Tree (DT), and Support Vector Machine (SVM)—using 10-fold cross-validation. The results show that combining sensor modalities improves classification accuracy and that tree-based classifiers (ET, RF, DT) consistently outperform LDA, LR, and SVM. Gaze, EDA, and TEMP are identified as strong predictors of trust, whereas facial action units introduced noise and reduced predictive value under the study's recording conditions.

The paper positions its contribution as foundational work toward a real-time, objective trust model for human-robot interaction. Such a model could enhance productivity, preserve safety, and mitigate failure in collaborative and supervisory settings where humans work alongside robots.

## Key Contributions

- Introduced a novel in-person human-robot trust dataset with multimodal physiological, gaze, and facial-expression data.
- Demonstrated that combining EDA, BVP, TEMP, and gaze improves trust classification accuracy compared with single-modality baselines.
- Showed that Extra Trees, Random Forest, and Decision Trees outperform LDA, Logistic Regression, and SVM on this trust-prediction task.
- Provided evidence that gaze, EDA, and TEMP are strong predictors of human trust in a supervisory robot partner.
- Framed trust as a scaled Likert value to capture its dynamic nature rather than collapsing it to a binary label.

## Relevance to Humanoid Robotics

Real-time, objective trust estimation is a key enabling capability for safe and productive deployment of humanoid robots alongside human workers. In manufacturing, logistics, and service scenarios, a robot that can infer human trust can adapt its behavior to maintain collaboration quality and safety. The multimodal sensing pipeline and shallow-classifier benchmarks developed in this paper are directly transferable to humanoid platforms that include comparable sensors. Although the experiment uses a robot arm rather than a full humanoid, the trust-modeling method and dataset-collection protocol address a cross-cutting interaction problem relevant to humanoid deployment.
