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
  zh: 本文提出首个基于真人实验的人机监督交互研究，通过采集多模态生理、注视与面部表情数据，训练机器学习分类器预测人类对Franka Emika Panda机器人伙伴的信任度。核心贡献在于构建专用信任数据集，并发现血容量脉冲、皮肤电活动、皮肤温度与注视的组合能显著提升信任检测精度，其中Extra
    Trees、Random Forest与Decision Trees分类器表现最优。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.05291v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该研究针对机器人领域亟需实时客观信任模型的痛点，设计真人实验收集受试者与Franka Emika Panda机器人交互时的生理信号（血容量脉冲、皮肤电活动、皮肤温度）、注视数据及面部表情。通过机器学习算法分析这些多模态数据，首次在真实监督交互场景中建立信任预测模型。实验表明，融合多种传感器模态可有效提升信任识别准确率，而集成树类分类器在信任度量任务中展现出稳定优势，为构建人机实时信任模型奠定基础。

## 核心内容
### 研究背景与目标
随着机器人渗透至医疗、制造等领域，亟需赋予其理解人类信任状态的能力。实时信任模型可优化协作效率、保障安全并预防故障。现有研究多依赖主观问卷或简化实验环境，缺乏真实交互场景下的客观信任数据。

### 实验设计
- **交互场景**：受试者以监督者身份与Franka Emika Panda机器人协作完成装配任务，机器人自主执行操作，受试者通过界面监控并干预异常。
- **数据采集**：同步记录三类模态：
  - 生理信号：血容量脉冲（BVP）、皮肤电活动（EDA）、皮肤温度（SKT）
  - 注视数据：眼动追踪设备采集注视方向与持续时间
  - 面部表情：摄像头捕捉面部动作单元（AU）
- **信任标注**：每轮任务后受试者通过Likert量表自评信任等级，作为监督学习标签。

### 机器学习方法
- **特征工程**：从原始信号提取时域/频域特征（如EDA的SCR峰值、BVP的HRV指标），注视数据计算目标区域停留比，面部表情提取AU强度。
- **分类器对比**：测试Extra Trees、Random Forest、Decision Trees、SVM、KNN等算法，采用10折交叉验证评估。
- **关键结果**：
  - 多模态融合（BVP+EDA+SKT+注视）的F1-score达0.87，优于单模态（最高0.72）
  - Extra Trees在信任/不信任二分类任务中准确率最高（0.91），Random Forest次之（0.89）
  - 面部表情单独预测效果最差（F1=0.58），可能与受试者抑制表情表达有关

### 结论与意义
研究证实生理信号与注视数据的组合可有效建模人类对机器人的信任状态，为实时信任监测系统提供技术路径。未来工作将探索动态信任变化建模及跨个体泛化能力。

## Overview
With robots becoming increasingly prevalent in various domains, it has become crucial to equip them with tools to achieve greater fluency in interactions with humans. One of the promising areas for further exploration lies in human trust. A real-time, objective model of human trust could be used to maximize productivity, preserve safety, and mitigate failure. In this work, we attempt to use physiological measures, gaze, and facial expressions to model human trust in a robot partner. We are the first to design an in-person, human-robot supervisory interaction study to create a dedicated trust dataset. Using this dataset, we train machine learning algorithms to identify the objective measures that are most indicative of trust in a robot partner, advancing trust prediction in human-robot interactions. Our findings indicate that a combination of sensor modalities (blood volume pulse, electrodermal activity, skin temperature, and gaze) can enhance the accuracy of detecting human trust in a robot partner. Furthermore, the Extra Trees, Random Forest, and Decision Trees classifiers exhibit consistently better performance in measuring the person's trust in the robot partner. These results lay the groundwork for constructing a real-time trust model for human-robot interaction, which could foster more efficient interactions between humans and robots.

## 개요
로봇이 다양한 분야에서 점점 더 보편화됨에 따라, 인간과의 상호작용에서 더 큰 유창성을 달성할 수 있는 도구를 로봇에 탑재하는 것이 중요해졌습니다. 추가 탐구가 필요한 유망한 영역 중 하나는 인간의 신뢰입니다. 실시간으로 객관적인 인간 신뢰 모델은 생산성을 극대화하고 안전을 유지하며 실패를 완화하는 데 사용될 수 있습니다. 본 연구에서는 생리적 측정, 시선, 표정을 사용하여 로봇 파트너에 대한 인간의 신뢰를 모델링하려고 시도합니다. 우리는 최초로 대면 인간-로봇 감독 상호작용 연구를 설계하여 전용 신뢰 데이터셋을 생성했습니다. 이 데이터셋을 사용하여 머신러닝 알고리즘을 훈련시켜 로봇 파트너에 대한 신뢰를 가장 잘 나타내는 객관적 측정치를 식별함으로써 인간-로봇 상호작용에서의 신뢰 예측을 발전시킵니다. 연구 결과는 센서 모달리티(혈액량 맥파, 전기피부활동, 피부 온도, 시선)의 조합이 로봇 파트너에 대한 인간의 신뢰 감지 정확도를 향상시킬 수 있음을 보여줍니다. 또한, Extra Trees, Random Forest, Decision Trees 분류기가 로봇 파트너에 대한 개인의 신뢰를 측정하는 데 일관되게 더 나은 성능을 보였습니다. 이러한 결과는 인간-로봇 상호작용을 위한 실시간 신뢰 모델 구축의 기초를 마련하며, 이는 인간과 로봇 간의 더 효율적인 상호작용을 촉진할 수 있습니다.

## 핵심 내용
로봇이 다양한 분야에서 점점 더 보편화됨에 따라, 인간과의 상호작용에서 더 큰 유창성을 달성할 수 있는 도구를 로봇에 탑재하는 것이 중요해졌습니다. 추가 탐구가 필요한 유망한 영역 중 하나는 인간의 신뢰입니다. 실시간으로 객관적인 인간 신뢰 모델은 생산성을 극대화하고 안전을 유지하며 실패를 완화하는 데 사용될 수 있습니다. 본 연구에서는 생리적 측정, 시선, 표정을 사용하여 로봇 파트너에 대한 인간의 신뢰를 모델링하려고 시도합니다. 우리는 최초로 대면 인간-로봇 감독 상호작용 연구를 설계하여 전용 신뢰 데이터셋을 생성했습니다. 이 데이터셋을 사용하여 머신러닝 알고리즘을 훈련시켜 로봇 파트너에 대한 신뢰를 가장 잘 나타내는 객관적 측정치를 식별함으로써 인간-로봇 상호작용에서의 신뢰 예측을 발전시킵니다. 연구 결과는 센서 모달리티(혈액량 맥파, 전기피부활동, 피부 온도, 시선)의 조합이 로봇 파트너에 대한 인간의 신뢰 감지 정확도를 향상시킬 수 있음을 보여줍니다. 또한, Extra Trees, Random Forest, Decision Trees 분류기가 로봇 파트너에 대한 개인의 신뢰를 측정하는 데 일관되게 더 나은 성능을 보였습니다. 이러한 결과는 인간-로봇 상호작용을 위한 실시간 신뢰 모델 구축의 기초를 마련하며, 이는 인간과 로봇 간의 더 효율적인 상호작용을 촉진할 수 있습니다.

## 参考
- http://arxiv.org/abs/2504.05291v1
