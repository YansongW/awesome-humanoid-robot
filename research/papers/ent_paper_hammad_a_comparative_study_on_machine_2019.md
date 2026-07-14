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

