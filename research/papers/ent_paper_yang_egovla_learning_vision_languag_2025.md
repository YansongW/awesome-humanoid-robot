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
  en: EgoVLA pretrains a vision-language-action model on egocentric human videos to
    predict wrist and hand actions, then retargets them via inverse kinematics to
    a Unitree H1 humanoid with Inspire dexterous hands and fine-tunes on limited robot
    demonstrations.
  zh: EgoVLA 在自我视角人体视频上预训练视觉-语言-动作模型以预测腕部和手部动作，然后通过逆运动学重定向到配备 Inspire 灵巧手的 Unitree
    H1 人形机器人，并在少量机器人演示上微调。
  ko: EgoVLA는 에고센트릭 인간 비디오로 VLA 모델을 사전 학습하여 손목과 손 동작을 예측한 후, 역운동학을 통해 Unitree H1 인간형
    로봇(Inspire 영리한 손 장착)으로 재타깃팅하고 소량의 로봇 시연으로 미세 조정한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
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

## Overview

EgoVLA addresses the data bottleneck in robot imitation learning by training a Vision-Language-Action (VLA) model on large-scale egocentric human videos rather than relying primarily on costly robot teleoperation data. The model predicts 3D wrist and finger actions parameterized by the MANO hand model, enabling a representation that is shared between human and humanoid robot embodiments. This shared action space is central to the paper's claim that human videos can serve as an effective pretraining source for robot manipulation.

After pretraining on human videos, the predicted human wrist and hand trajectories are converted to robot actions through inverse kinematics and retargeting, producing a policy for a Unitree H1 humanoid equipped with Inspire dexterous hands. The policy is then fine-tuned on a relatively small number of robot manipulation demonstrations to adapt it to the robot's morphology and dynamics. The authors frame this pipeline as a scalable alternative to collecting large amounts of real robot data.

The paper also introduces the Ego Humanoid Manipulation Benchmark, a simulation benchmark built in NVIDIA Isaac Lab containing 12 diverse bimanual manipulation tasks. Demonstrations for these tasks are collected using Meta Quest 3 teleoperation. EgoVLA is fine-tuned and evaluated on this benchmark, where it outperforms baselines and ablations and shows generalization to out-of-distribution tasks.

## Key Contributions

- EgoVLA, a VLA pretrained on large-scale egocentric human videos for dexterous manipulation.
- A unified MANO hand-parameter action space that bridges human and humanoid robot embodiments.
- The Ego Humanoid Manipulation Benchmark, a simulated benchmark of 12 bimanual tasks in NVIDIA Isaac Lab.
- Empirical demonstration that human video pretraining enables strong in-domain and out-of-domain humanoid manipulation with limited robot data.

## Relevance to Humanoid Robotics

The paper is highly relevant to humanoid robotics because it directly targets bimanual, dexterous manipulation on a Unitree H1 humanoid with Inspire hands. By showing that egocentric human video pretraining can substantially reduce the amount of robot teleoperation data required, it addresses one of the central scaling challenges for humanoid deployment in real-world environments.

Furthermore, the focus on bimanual tasks, vision-language grounding, and retargeting from human to humanoid embodiment aligns with key technical requirements for industrial and service humanoid applications. The introduced benchmark also provides a structured evaluation setting specifically designed for humanoid manipulation, which is valuable for the research community and industry benchmarking.
