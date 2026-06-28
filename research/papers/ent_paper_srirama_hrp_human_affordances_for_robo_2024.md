---
$id: ent_paper_srirama_hrp_human_affordances_for_robo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HRP: Human Affordances for Robotic Pre-Training'
  zh: HRP：面向机器人预训练的人类可供性学习
  ko: 'HRP: 로봇 사전 훈련을 위한 인간 어포던스'
summary:
  en: HRP extracts contact points, future hand poses, and active object bounding boxes
    from internet-scale human videos, then distills these affordances into pre-trained
    visual encoders via L2 regression with LayerNorm-only fine-tuning, improving robotic
    manipulation across diverse camera views and robot morphologies.
  zh: HRP从互联网规模的人类视频中提取接触点、未来手部姿态和活跃物体边界框，并通过仅微调LayerNorm的L2回归将这些可供性蒸馏到预训练视觉编码器中，以提升跨不同视角和机器人形态的操作性能。
  ko: HRP는 인터넷 규모의 인간 비디오에서 접촉점, 미래 손 자세, 활성 객체 경계 상자를 추출한 후 LayerNorm만 미세 조정하는 L2
    회귀를 통해 이러한 어포던스를 사전 훈련된 시각 인코더에 증류하여 다양한 카메라 시점과 로봇 형태에서 조작 성능을 향상시킨다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- affordance_pre_training
- visual_representation_learning
- imitation_learning
- human_video_learning
- diffusion_policy
- robotic_manipulation
- cross_view_generalization
- contact_point_prediction
- hand_pose_prediction
- active_object_detection
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review of
    the full paper before verification.; approved by autonomous review workflow.
sources:
- id: src_001
  type: paper
  title: 'HRP: Human Affordances for Robotic Pre-Training'
  url: https://arxiv.org/abs/2407.18911
  date: '2024'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

HRP (Human Affordances for Robotic Pre-Training) addresses the problem of learning generalizable visual representations for robotics without collecting prohibitively large amounts of real robot data. Instead of scaling robot data collection, the method leverages internet-scale human videos to extract affordance labels at the environment and agent level, then distills these labels into pre-trained visual encoders.

The framework extracts three types of affordance labels from human videos: contact points that indicate where interaction occurs, future hand poses that indicate how to interact, and active object bounding boxes that indicate what to interact with. These labels are obtained using off-the-shelf computer vision modules and are used to fine-tune existing representations via L2 regression with LayerNorm-only fine-tuning, which preserves pre-trained features while adapting them to robotic manipulation.

The authors evaluate HRP across more than 3000 real robot trials, covering five manipulation tasks (Stacking, Pouring, Toasting, Pot on Stove, Hand Lift Cup) and three robot morphologies, including a Franka Emika Panda arm, an xArm robot, and a custom dexterous hand. The method consistently improves downstream performance across three camera views and is compatible with diffusion policy, yielding a 20% performance gain.

## Key Contributions

- Semi-supervised HRP algorithm that leverages off-the-shelf human affordance models to learn robotic representations from human video.
- Application to six pre-trained representations, boosting performance across three camera views, three robot setups, and five manipulation tasks, validated by 3000+ real robot trials.
- Ablation study demonstrating that all three affordance objectives (hand, object, and contact) contribute to effective representation learning.
- HRP representations improve diffusion policy performance by 20%, showing compatibility across imitation learning frameworks.
- Best HRP representation and accompanying code/data are planned for open-source release.

## Relevance to Humanoid Robotics

HRP is highly relevant to humanoid robotics because it improves visual representations for manipulation by extracting human affordances from videos, enabling better generalization across camera views, robot morphologies, and tasks with limited robot data. This directly supports scalable perception for humanoid robot deployment, where collecting diverse real-world interaction data is expensive and time-consuming.

The method's reliance on human videos as a supervision source is particularly aligned with humanoid robots, which are designed to operate in human-centric environments and perform human-like manipulation. By learning from human affordances, humanoid systems can more effectively identify relevant objects and predict interaction parameters in unstructured, everyday settings.
