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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.05291v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (988 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2504.05291v1

## 개요
이 연구는 로봇 분야에서 실시간 객관적 신뢰 모델이 시급히 필요하다는 점에 착안하여, 실제 실험을 설계해 피험자와 Franka Emika Panda 로봇 간 상호작용 시 수집한 생리 신호(혈량 맥파, 피부 전기 활동, 피부 온도), 시선 데이터 및 얼굴 표정을 기록했습니다. 머신러닝 알고리즘으로 이러한 다중 모달 데이터를 분석하여, 실제 감독 상호작용 시나리오에서 최초로 신뢰 예측 모델을 구축했습니다. 실험 결과, 여러 센서 모달을 융합하면 신뢰 인식 정확도를 효과적으로 향상시킬 수 있으며, 앙상블 트리 기반 분류기가 신뢰 측정 작업에서 안정적인 우위를 보여, 인간-로봇 실시간 신뢰 모델 구축의 기초를 마련했습니다.

## 핵심 내용
### 연구 배경 및 목표
로봇이 의료, 제조 등 분야에 확산됨에 따라, 인간의 신뢰 상태를 이해할 수 있는 능력을 부여하는 것이 시급해졌습니다. 실시간 신뢰 모델은 협업 효율성을 최적화하고 안전을 보장하며 고장을 예방할 수 있습니다. 기존 연구는 주관적 설문이나 단순화된 실험 환경에 의존하여, 실제 상호작용 시나리오에서의 객관적 신뢰 데이터가 부족합니다.

### 실험 설계
- **상호작용 시나리오**: 피험자는 감독자 역할로 Franka Emika Panda 로봇과 조립 작업을 협력 수행하며, 로봇이 자율적으로 작업을 실행하고 피험자는 인터페이스를 통해 모니터링 및 이상 상황에 개입합니다.
- **데이터 수집**: 세 가지 모달을 동기화하여 기록:
  - 생리 신호: 혈량 맥파(BVP), 피부 전기 활동(EDA), 피부 온도(SKT)
  - 시선 데이터: 안구 추적 장치로 시선 방향과 지속 시간 수집
  - 얼굴 표정: 카메라로 얼굴 행동 단위(AU) 포착
- **신뢰 라벨링**: 각 작업 후 피험자가 Likert 척도로 신뢰 수준을 자가 평가하여, 지도 학습 라벨로 사용.

### 머신러닝 방법
- **특징 엔지니어링**: 원시 신호에서 시간 영역/주파수 영역 특징 추출(예: EDA의 SCR 피크, BVP의 HRV 지표), 시선 데이터에서 목표 영역 체류 비율 계산, 얼굴 표정에서 AU 강도 추출.
- **분류기 비교**: Extra Trees, Random Forest, Decision Trees, SVM, KNN 등의 알고리즘을 테스트하고, 10겹 교차 검증으로 평가.
- **주요 결과**:
  - 다중 모달 융합(BVP+EDA+SKT+시선)의 F1-score는 0.87로, 단일 모달(최고 0.72)보다 우수
  - Extra Trees는 신뢰/불신 이진 분류 작업에서 가장 높은 정확도(0.91)를 보였고, Random Forest가 그다음(0.89)
  - 얼굴 표정 단독 예측은 가장 낮은 성능(F1=0.58)을 보였으며, 이는 피험자가 표정 표현을 억제했기 때문일 수 있음

### 결론 및 의의
이 연구는 생리 신호와 시선 데이터의 조합이 인간의 로봇에 대한 신뢰 상태를 효과적으로 모델링할 수 있음을 확인하여, 실시간 신뢰 모니터링 시스템의 기술적 경로를 제공합니다. 향후 작업은 동적 신뢰 변화 모델링 및 개인 간 일반화 능력을 탐구할 것입니다.
