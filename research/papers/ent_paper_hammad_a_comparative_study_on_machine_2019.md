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
  zh: 这篇2019年ROBIO会议论文比较了经典机器学习与深度学习分类器在壁跟随机器人方向预测任务上的表现。研究基于UCI Wall-Following Robot Navigation数据集，在24传感器、4传感器和2传感器三种输入格式上进行了实验。核心贡献包括：在简化格式上使用Decision
    Tree达到100%平均准确率，在完整格式上使用Gradient Boosting达到99.82%平均准确率。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1912.11856v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (744 chars, DeepSeek).'
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
该研究利用SCITOS G5移动机器人采集的公开数据集，包含24个超声波传感器读数及对应的方向标签。除了完整的24传感器格式外，数据集还提供了4传感器和2传感器的简化版本。作者提出了两个主要贡献：首先，在所有三种输入格式上实现了优于此前所有控制模型的准确率；其次，对不同机器学习与深度学习算法在该数据集上的表现进行了系统比较。所有模型均采用Monte-Carlo交叉验证进行评估。

## 核心内容
### 方法
- 使用UCI Wall-Following Robot Navigation数据集，数据由SCITOS G5机器人腰部安装的24个超声波传感器采集
- 数据集包含三种输入格式：完整24传感器、简化4传感器、简化2传感器
- 比较的算法包括：Decision Tree、Gradient Boosting、Random Forest、SVM、KNN、Neural Network等

### 实验设置
- 采用Monte-Carlo交叉验证进行模型评估
- 训练数据包含方向标签，用于预测机器人下一步的移动方向

### 关键结果
- **4传感器和2传感器格式**：Decision Tree Classifier达到100%平均准确率，实现完美解决方案
- **24传感器完整格式**：Gradient Boost Classifier达到99.82%平均准确率，优于此前所有模型
- 所有模型的准确率均高于此前文献中报道的结果

### 结论
- 研究表明，对于传感器融合问题，经典机器学习算法（如Decision Tree和Gradient Boosting）能够达到甚至超越深度学习方法的性能
- 该比较研究为类似传感器融合任务提供了算法选择的参考依据

## Overview
A comparison of the performance of various machine learning models to predict the direction of a wall following robot is presented in this paper. The models were trained using an open-source dataset that contains 24 ultrasound sensors readings and the corresponding direction for each sample. This dataset was captured using SCITOS G5 mobile robot by placing the sensors on the robot waist. In addition to the full format with 24 sensors per record, the dataset has two simplified formats with 4 and 2 input sensor readings per record. Several control models were proposed previously for this dataset using all three dataset formats. In this paper, two primary research contributions are presented. First, presenting machine learning models with accuracies higher than all previously proposed models for this dataset using all three formats. A perfect solution for the 4 and 2 inputs sensors formats is presented using Decision Tree Classifier by achieving a mean accuracy of 100%. On the other hand, a mean accuracy of 99.82% was achieves using the 24 sensor inputs by employing the Gradient Boost Classifier. Second, presenting a comparative study on the performance of different machine learning and deep learning algorithms on this dataset. Therefore, providing an overall insight on the performance of these algorithms for similar sensor fusion problems. All the models in this paper were evaluated using Monte-Carlo cross-validation.

## Overview
This paper presents a comparison of the performance of various machine learning models for predicting the direction of a wall-following robot. The models were trained using an open-source dataset containing 24 ultrasound sensor readings and the corresponding direction for each sample. This dataset was captured using the SCITOS G5 mobile robot, with sensors placed on the robot's waist. In addition to the full format with 24 sensors per record, the dataset includes two simplified formats with 4 and 2 input sensor readings per record. Several control models have been previously proposed for this dataset using all three formats. This paper makes two primary research contributions. First, it presents machine learning models with accuracies higher than all previously proposed models for this dataset across all three formats. A perfect solution for the 4 and 2 input sensor formats is achieved using the Decision Tree Classifier, with a mean accuracy of 100%. Meanwhile, a mean accuracy of 99.82% is achieved using the 24 sensor inputs with the Gradient Boost Classifier. Second, it presents a comparative study of the performance of different machine learning and deep learning algorithms on this dataset, thereby providing overall insights into the performance of these algorithms for similar sensor fusion problems. All models in this paper were evaluated using Monte-Carlo cross-validation.

## Content
This paper presents a comparison of the performance of various machine learning models for predicting the direction of a wall-following robot. The models were trained using an open-source dataset containing 24 ultrasound sensor readings and the corresponding direction for each sample. This dataset was captured using the SCITOS G5 mobile robot, with sensors placed on the robot's waist. In addition to the full format with 24 sensors per record, the dataset includes two simplified formats with 4 and 2 input sensor readings per record. Several control models have been previously proposed for this dataset using all three formats. This paper makes two primary research contributions. First, it presents machine learning models with accuracies higher than all previously proposed models for this dataset across all three formats. A perfect solution for the 4 and 2 input sensor formats is achieved using the Decision Tree Classifier, with a mean accuracy of 100%. Meanwhile, a mean accuracy of 99.82% is achieved using the 24 sensor inputs with the Gradient Boost Classifier. Second, it presents a comparative study of the performance of different machine learning and deep learning algorithms on this dataset, thereby providing overall insights into the performance of these algorithms for similar sensor fusion problems. All models in this paper were evaluated using Monte-Carlo cross-validation.

## 参考
- http://arxiv.org/abs/1912.11856v2

## 개요
이 연구는 SCITOS G5 모바일 로봇으로 수집된 공개 데이터셋을 활용하며, 24개의 초음파 센서 판독값과 해당 방향 레이블을 포함합니다. 전체 24센서 형식 외에도 데이터셋은 4센서 및 2센서 단순화 버전을 제공합니다. 저자들은 두 가지 주요 기여를 제시합니다: 첫째, 세 가지 입력 형식 모두에서 이전의 모든 제어 모델보다 우수한 정확도를 달성했습니다; 둘째, 해당 데이터셋에서 다양한 머신러닝 및 딥러닝 알고리즘의 성능을 체계적으로 비교했습니다. 모든 모델은 Monte-Carlo 교차 검증을 통해 평가되었습니다.

## 핵심 내용
### 방법
- UCI Wall-Following Robot Navigation 데이터셋을 사용하며, 데이터는 SCITOS G5 로봇의 허리에 장착된 24개의 초음파 센서로 수집되었습니다
- 데이터셋은 세 가지 입력 형식을 포함합니다: 전체 24센서, 단순화 4센서, 단순화 2센서
- 비교된 알고리즘에는 Decision Tree, Gradient Boosting, Random Forest, SVM, KNN, Neural Network 등이 포함됩니다

### 실험 설정
- Monte-Carlo 교차 검증을 사용하여 모델을 평가했습니다
- 훈련 데이터에는 로봇의 다음 이동 방향을 예측하기 위한 방향 레이블이 포함되어 있습니다

### 주요 결과
- **4센서 및 2센서 형식**: Decision Tree Classifier가 평균 정확도 100%를 달성하여 완벽한 솔루션을 구현했습니다
- **24센서 전체 형식**: Gradient Boost Classifier가 평균 정확도 99.82%를 달성하여 이전의 모든 모델보다 우수했습니다
- 모든 모델의 정확도는 이전 문헌에서 보고된 결과보다 높았습니다

### 결론
- 연구는 센서 융합 문제에 대해 Decision Tree 및 Gradient Boosting과 같은 고전 머신러닝 알고리즘이 딥러닝 방법의 성능에 도달하거나 이를 능가할 수 있음을 보여줍니다
- 이 비교 연구는 유사한 센서 융합 작업에 대한 알고리즘 선택의 참고 기준을 제공합니다
