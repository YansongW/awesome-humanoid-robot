---
$id: ent_paper_yang_egovla_learning_vision_languag_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos'
  zh: EgoVLA：从以自我视角人体视频中学习视觉-语言-动作模型
  ko: 'EgoVLA: 에고센트릭 인간 비디오로부터 비전-언어-행동 모델 학습'
summary:
  en: EgoVLA pretrains a vision-language-action model on egocentric human videos to predict wrist and hand actions, then retargets
    them via inverse kinematics to a Unitree H1 humanoid with Inspire dexterous hands and fine-tunes on limited robot demonstrations.
  zh: EgoVLA 在自我视角人体视频上预训练视觉-语言-动作模型以预测腕部和手部动作，然后通过逆运动学重定向到配备 Inspire 灵巧手的 Unitree H1 人形机器人，并在少量机器人演示上微调。
  ko: EgoVLA는 에고센트릭 인간 비디오로 VLA 모델을 사전 학습하여 손목과 손 동작을 예측한 후, 역운동학을 통해 Unitree H1 인간형 로봇(Inspire 영리한 손 장착)으로 재타깃팅하고 소량의 로봇
    시연으로 미세 조정한다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 10_evaluation_benchmarks
- 02_components
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- egovla
- vision_language_action_model
- vla
- imitation_learning
- egocentric_video
- humanoid_robot
- bimanual_manipulation
- dexterous_manipulation
- unitree_h1
- inspire_hands
- mano
- retargeting
- inverse_kinematics
- nvila
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.12440v3.
sources:
- id: src_001
  type: paper
  title: 'EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos'
  url: https://arxiv.org/abs/2507.12440
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Real robot data collection for imitation learning has led to significant advancements in robotic manipulation. However, the requirement for robot hardware in the process fundamentally constrains the scale of the data. In this paper, we explore training Vision-Language-Action (VLA) models using egocentric human videos. The benefit of using human videos is not only for their scale but more importantly for the richness of scenes and tasks. With a VLA trained on human video that predicts human wrist and hand actions, we can perform Inverse Kinematics and retargeting to convert the human actions to robot actions. We fine-tune the model using a few robot manipulation demonstrations to obtain the robot policy, namely EgoVLA. We propose a simulation benchmark called Ego Humanoid Manipulation Benchmark, where we design diverse bimanual manipulation tasks with demonstrations. We fine-tune and evaluate EgoVLA with Ego Humanoid Manipulation Benchmark and show significant improvements over baselines and ablate the importance of human data. Videos can be found on our website: https://rchalyang.github.io/EgoVLA

## 核心内容
Real robot data collection for imitation learning has led to significant advancements in robotic manipulation. However, the requirement for robot hardware in the process fundamentally constrains the scale of the data. In this paper, we explore training Vision-Language-Action (VLA) models using egocentric human videos. The benefit of using human videos is not only for their scale but more importantly for the richness of scenes and tasks. With a VLA trained on human video that predicts human wrist and hand actions, we can perform Inverse Kinematics and retargeting to convert the human actions to robot actions. We fine-tune the model using a few robot manipulation demonstrations to obtain the robot policy, namely EgoVLA. We propose a simulation benchmark called Ego Humanoid Manipulation Benchmark, where we design diverse bimanual manipulation tasks with demonstrations. We fine-tune and evaluate EgoVLA with Ego Humanoid Manipulation Benchmark and show significant improvements over baselines and ablate the importance of human data. Videos can be found on our website: https://rchalyang.github.io/EgoVLA

## 参考
- http://arxiv.org/abs/2507.12440v3

## Overview
Real robot data collection for imitation learning has led to significant advancements in robotic manipulation. However, the requirement for robot hardware in the process fundamentally constrains the scale of the data. In this paper, we explore training Vision-Language-Action (VLA) models using egocentric human videos. The benefit of using human videos is not only for their scale but more importantly for the richness of scenes and tasks. With a VLA trained on human video that predicts human wrist and hand actions, we can perform Inverse Kinematics and retargeting to convert the human actions to robot actions. We fine-tune the model using a few robot manipulation demonstrations to obtain the robot policy, namely EgoVLA. We propose a simulation benchmark called Ego Humanoid Manipulation Benchmark, where we design diverse bimanual manipulation tasks with demonstrations. We fine-tune and evaluate EgoVLA with Ego Humanoid Manipulation Benchmark and show significant improvements over baselines and ablate the importance of human data. Videos can be found on our website: https://rchalyang.github.io/EgoVLA

## Content
Real robot data collection for imitation learning has led to significant advancements in robotic manipulation. However, the requirement for robot hardware in the process fundamentally constrains the scale of the data. In this paper, we explore training Vision-Language-Action (VLA) models using egocentric human videos. The benefit of using human videos is not only for their scale but more importantly for the richness of scenes and tasks. With a VLA trained on human video that predicts human wrist and hand actions, we can perform Inverse Kinematics and retargeting to convert the human actions to robot actions. We fine-tune the model using a few robot manipulation demonstrations to obtain the robot policy, namely EgoVLA. We propose a simulation benchmark called Ego Humanoid Manipulation Benchmark, where we design diverse bimanual manipulation tasks with demonstrations. We fine-tune and evaluate EgoVLA with Ego Humanoid Manipulation Benchmark and show significant improvements over baselines and ablate the importance of human data. Videos can be found on our website: https://rchalyang.github.io/EgoVLA

## 개요
모방 학습을 위한 실제 로봇 데이터 수집은 로봇 조작 분야에서 상당한 발전을 가져왔습니다. 그러나 이 과정에서 로봇 하드웨어가 필요하다는 점은 데이터의 규모를 근본적으로 제한합니다. 본 논문에서는 자기중심적 인간 비디오를 사용하여 Vision-Language-Action (VLA) 모델을 훈련하는 방법을 탐구합니다. 인간 비디오를 사용하는 이점은 그 규모뿐만 아니라, 더 중요하게는 장면과 작업의 풍부함에 있습니다. 인간의 손목과 손 동작을 예측하는 인간 비디오로 훈련된 VLA를 사용하면, 역기구학(Inverse Kinematics) 및 리타겟팅을 통해 인간의 동작을 로봇 동작으로 변환할 수 있습니다. 소수의 로봇 조작 시연을 사용하여 모델을 미세 조정함으로써 로봇 정책, 즉 EgoVLA를 얻습니다. 우리는 다양한 양손 조작 작업과 시연을 설계한 Ego Humanoid Manipulation Benchmark라는 시뮬레이션 벤치마크를 제안합니다. Ego Humanoid Manipulation Benchmark를 사용하여 EgoVLA를 미세 조정하고 평가한 결과, 기준선 대비 상당한 개선을 보였으며 인간 데이터의 중요성을 분석했습니다. 비디오는 당사 웹사이트(https://rchalyang.github.io/EgoVLA)에서 확인할 수 있습니다.

## 핵심 내용
모방 학습을 위한 실제 로봇 데이터 수집은 로봇 조작 분야에서 상당한 발전을 가져왔습니다. 그러나 이 과정에서 로봇 하드웨어가 필요하다는 점은 데이터의 규모를 근본적으로 제한합니다. 본 논문에서는 자기중심적 인간 비디오를 사용하여 Vision-Language-Action (VLA) 모델을 훈련하는 방법을 탐구합니다. 인간 비디오를 사용하는 이점은 그 규모뿐만 아니라, 더 중요하게는 장면과 작업의 풍부함에 있습니다. 인간의 손목과 손 동작을 예측하는 인간 비디오로 훈련된 VLA를 사용하면, 역기구학(Inverse Kinematics) 및 리타겟팅을 통해 인간의 동작을 로봇 동작으로 변환할 수 있습니다. 소수의 로봇 조작 시연을 사용하여 모델을 미세 조정함으로써 로봇 정책, 즉 EgoVLA를 얻습니다. 우리는 다양한 양손 조작 작업과 시연을 설계한 Ego Humanoid Manipulation Benchmark라는 시뮬레이션 벤치마크를 제안합니다. Ego Humanoid Manipulation Benchmark를 사용하여 EgoVLA를 미세 조정하고 평가한 결과, 기준선 대비 상당한 개선을 보였으며 인간 데이터의 중요성을 분석했습니다. 비디오는 당사 웹사이트(https://rchalyang.github.io/EgoVLA)에서 확인할 수 있습니다.
