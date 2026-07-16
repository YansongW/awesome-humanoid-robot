---
$id: ent_paper_hammad_a_comparative_study_on_machine_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Comparative Study on Machine Learning Algorithms for the Control of a Wall Following Robot
  zh: 壁面跟随机器人控制的机器学习算法比较研究
  ko: 벽면 추종 로봇 제어를 위한 기계 학습 알고리즘 비교 연구
summary:
  en: This 2019 ROBIO paper compares classical machine learning and deep learning classifiers for predicting the direction
    of a wall-following robot using the UCI Wall-Following Robot Navigation dataset with 24-, 4-, and 2-sensor formats, achieving
    100% mean accuracy on simplified formats with a Decision Tree and 99.82% on the full format with Gradient Boosting.
  zh: 这篇2019年ROBIO论文使用UCI壁面跟随机器人导航数据集的24、4和2传感器格式，比较了经典机器学习和深度学习分类器在预测壁面跟随机器人方向上的性能，其中决策树在简化格式上达到100%平均准确率，梯度提升在完整格式上达到99.82%。
  ko: 이 2019년 ROBIO 논문은 UCI 벽면 추종 로봇 내비게이션 데이터셋의 24, 4, 2 센서 형식을 사용하여 벽면 추종 로봇의 방향을 예측하기 위한 고전적 기계 학습 및 심층 학습 분류기를 비교하였으며,
    의사결정나무는 단순화된 형식에서 100% 평균 정확도를, 그래디언트 부스팅은 전체 형식에서 99.82%를 달성했다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- machine_learning
- sensor_fusion
- wall_following
- navigation
- decision_tree
- gradient_boosting
- ultrasound_sensor
- learned_controller
- mobile_robot
- monte_carlo_cross_validation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1912.11856v2.
sources:
- id: src_001
  type: paper
  title: A Comparative Study on Machine Learning Algorithms for the Control of a Wall Following Robot
  url: https://arxiv.org/abs/1912.11856
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
A comparison of the performance of various machine learning models to predict the direction of a wall following robot is presented in this paper. The models were trained using an open-source dataset that contains 24 ultrasound sensors readings and the corresponding direction for each sample. This dataset was captured using SCITOS G5 mobile robot by placing the sensors on the robot waist. In addition to the full format with 24 sensors per record, the dataset has two simplified formats with 4 and 2 input sensor readings per record. Several control models were proposed previously for this dataset using all three dataset formats. In this paper, two primary research contributions are presented. First, presenting machine learning models with accuracies higher than all previously proposed models for this dataset using all three formats. A perfect solution for the 4 and 2 inputs sensors formats is presented using Decision Tree Classifier by achieving a mean accuracy of 100%. On the other hand, a mean accuracy of 99.82% was achieves using the 24 sensor inputs by employing the Gradient Boost Classifier. Second, presenting a comparative study on the performance of different machine learning and deep learning algorithms on this dataset. Therefore, providing an overall insight on the performance of these algorithms for similar sensor fusion problems. All the models in this paper were evaluated using Monte-Carlo cross-validation.

## 核心内容
A comparison of the performance of various machine learning models to predict the direction of a wall following robot is presented in this paper. The models were trained using an open-source dataset that contains 24 ultrasound sensors readings and the corresponding direction for each sample. This dataset was captured using SCITOS G5 mobile robot by placing the sensors on the robot waist. In addition to the full format with 24 sensors per record, the dataset has two simplified formats with 4 and 2 input sensor readings per record. Several control models were proposed previously for this dataset using all three dataset formats. In this paper, two primary research contributions are presented. First, presenting machine learning models with accuracies higher than all previously proposed models for this dataset using all three formats. A perfect solution for the 4 and 2 inputs sensors formats is presented using Decision Tree Classifier by achieving a mean accuracy of 100%. On the other hand, a mean accuracy of 99.82% was achieves using the 24 sensor inputs by employing the Gradient Boost Classifier. Second, presenting a comparative study on the performance of different machine learning and deep learning algorithms on this dataset. Therefore, providing an overall insight on the performance of these algorithms for similar sensor fusion problems. All the models in this paper were evaluated using Monte-Carlo cross-validation.

## 参考
- http://arxiv.org/abs/1912.11856v2

## Overview
This paper presents a comparison of the performance of various machine learning models for predicting the direction of a wall-following robot. The models were trained using an open-source dataset containing 24 ultrasound sensor readings and the corresponding direction for each sample. This dataset was captured using the SCITOS G5 mobile robot, with sensors placed on the robot's waist. In addition to the full format with 24 sensors per record, the dataset includes two simplified formats with 4 and 2 input sensor readings per record. Several control models have been previously proposed for this dataset using all three formats. This paper makes two primary research contributions. First, it presents machine learning models with accuracies higher than all previously proposed models for this dataset across all three formats. A perfect solution for the 4 and 2 input sensor formats is achieved using the Decision Tree Classifier, with a mean accuracy of 100%. Meanwhile, a mean accuracy of 99.82% is achieved using the 24 sensor inputs with the Gradient Boost Classifier. Second, it presents a comparative study of the performance of different machine learning and deep learning algorithms on this dataset, thereby providing overall insights into the performance of these algorithms for similar sensor fusion problems. All models in this paper were evaluated using Monte-Carlo cross-validation.

## Content
This paper presents a comparison of the performance of various machine learning models for predicting the direction of a wall-following robot. The models were trained using an open-source dataset containing 24 ultrasound sensor readings and the corresponding direction for each sample. This dataset was captured using the SCITOS G5 mobile robot, with sensors placed on the robot's waist. In addition to the full format with 24 sensors per record, the dataset includes two simplified formats with 4 and 2 input sensor readings per record. Several control models have been previously proposed for this dataset using all three formats. This paper makes two primary research contributions. First, it presents machine learning models with accuracies higher than all previously proposed models for this dataset across all three formats. A perfect solution for the 4 and 2 input sensor formats is achieved using the Decision Tree Classifier, with a mean accuracy of 100%. Meanwhile, a mean accuracy of 99.82% is achieved using the 24 sensor inputs with the Gradient Boost Classifier. Second, it presents a comparative study of the performance of different machine learning and deep learning algorithms on this dataset, thereby providing overall insights into the performance of these algorithms for similar sensor fusion problems. All models in this paper were evaluated using Monte-Carlo cross-validation.

## 개요
본 논문에서는 벽면 추종 로봇의 방향을 예측하기 위한 다양한 머신러닝 모델의 성능을 비교합니다. 모델은 24개의 초음파 센서 판독값과 각 샘플에 해당하는 방향을 포함하는 오픈소스 데이터셋을 사용하여 훈련되었습니다. 이 데이터셋은 SCITOS G5 모바일 로봇을 사용하여 센서를 로봇 허리에 배치하여 수집되었습니다. 레코드당 24개의 센서를 포함하는 전체 형식 외에도, 데이터셋은 레코드당 4개 및 2개의 입력 센서 판독값을 가진 두 가지 단순화된 형식을 제공합니다. 이전에는 세 가지 데이터셋 형식을 모두 사용하여 이 데이터셋에 대한 여러 제어 모델이 제안되었습니다. 본 논문에서는 두 가지 주요 연구 기여를 제시합니다. 첫째, 세 가지 형식을 모두 사용하여 이 데이터셋에 대해 이전에 제안된 모든 모델보다 높은 정확도를 가진 머신러닝 모델을 제시합니다. 4개 및 2개 입력 센서 형식에 대해서는 Decision Tree Classifier를 사용하여 평균 정확도 100%를 달성하는 완벽한 솔루션을 제시합니다. 반면, 24개 센서 입력에 대해서는 Gradient Boost Classifier를 사용하여 평균 정확도 99.82%를 달성했습니다. 둘째, 이 데이터셋에 대한 다양한 머신러닝 및 딥러닝 알고리즘의 성능에 대한 비교 연구를 제시합니다. 따라서 유사한 센서 융합 문제에 대한 이러한 알고리즘의 성능에 대한 전반적인 통찰력을 제공합니다. 본 논문의 모든 모델은 Monte-Carlo 교차 검증을 사용하여 평가되었습니다.

## 핵심 내용
본 논문에서는 벽면 추종 로봇의 방향을 예측하기 위한 다양한 머신러닝 모델의 성능을 비교합니다. 모델은 24개의 초음파 센서 판독값과 각 샘플에 해당하는 방향을 포함하는 오픈소스 데이터셋을 사용하여 훈련되었습니다. 이 데이터셋은 SCITOS G5 모바일 로봇을 사용하여 센서를 로봇 허리에 배치하여 수집되었습니다. 레코드당 24개의 센서를 포함하는 전체 형식 외에도, 데이터셋은 레코드당 4개 및 2개의 입력 센서 판독값을 가진 두 가지 단순화된 형식을 제공합니다. 이전에는 세 가지 데이터셋 형식을 모두 사용하여 이 데이터셋에 대한 여러 제어 모델이 제안되었습니다. 본 논문에서는 두 가지 주요 연구 기여를 제시합니다. 첫째, 세 가지 형식을 모두 사용하여 이 데이터셋에 대해 이전에 제안된 모든 모델보다 높은 정확도를 가진 머신러닝 모델을 제시합니다. 4개 및 2개 입력 센서 형식에 대해서는 Decision Tree Classifier를 사용하여 평균 정확도 100%를 달성하는 완벽한 솔루션을 제시합니다. 반면, 24개 센서 입력에 대해서는 Gradient Boost Classifier를 사용하여 평균 정확도 99.82%를 달성했습니다. 둘째, 이 데이터셋에 대한 다양한 머신러닝 및 딥러닝 알고리즘의 성능에 대한 비교 연구를 제시합니다. 따라서 유사한 센서 융합 문제에 대한 이러한 알고리즘의 성능에 대한 전반적인 통찰력을 제공합니다. 본 논문의 모든 모델은 Monte-Carlo 교차 검증을 사용하여 평가되었습니다.
