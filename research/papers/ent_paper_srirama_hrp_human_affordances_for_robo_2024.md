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
  en: HRP extracts contact points, future hand poses, and active object bounding boxes from internet-scale human videos, then
    distills these affordances into pre-trained visual encoders via L2 regression with LayerNorm-only fine-tuning, improving
    robotic manipulation across diverse camera views and robot morphologies.
  zh: HRP从互联网规模的人类视频中提取接触点、未来手部姿态和活跃物体边界框，并通过仅微调LayerNorm的L2回归将这些可供性蒸馏到预训练视觉编码器中，以提升跨不同视角和机器人形态的操作性能。
  ko: HRP는 인터넷 규모의 인간 비디오에서 접촉점, 미래 손 자세, 활성 객체 경계 상자를 추출한 후 LayerNorm만 미세 조정하는 L2 회귀를 통해 이러한 어포던스를 사전 훈련된 시각 인코더에 증류하여 다양한
    카메라 시점과 로봇 형태에서 조작 성능을 향상시킨다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.18911v1.
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
## 概述
In order to *generalize* to various tasks in the wild, robotic agents will need a suitable representation (i.e., vision network) that enables the robot to predict optimal actions given high dimensional vision inputs. However, learning such a representation requires an extreme amount of diverse training data, which is prohibitively expensive to collect on a real robot. How can we overcome this problem? Instead of collecting more robot data, this paper proposes using internet-scale, human videos to extract "affordances," both at the environment and agent level, and distill them into a pre-trained representation. We present a simple framework for pre-training representations on hand, object, and contact "affordance labels" that highlight relevant objects in images and how to interact with them. These affordances are automatically extracted from human video data (with the help of off-the-shelf computer vision modules) and used to fine-tune existing representations. Our approach can efficiently fine-tune *any* existing representation, and results in models with stronger downstream robotic performance across the board. We experimentally demonstrate (using 3000+ robot trials) that this affordance pre-training scheme boosts performance by a minimum of 15% on 5 real-world tasks, which consider three diverse robot morphologies (including a dexterous hand). Unlike prior works in the space, these representations improve performance across 3 different camera views. Quantitatively, we find that our approach leads to higher levels of generalization in out-of-distribution settings. For code, weights, and data check: https://hrp-robot.github.io

## 核心内容
In order to *generalize* to various tasks in the wild, robotic agents will need a suitable representation (i.e., vision network) that enables the robot to predict optimal actions given high dimensional vision inputs. However, learning such a representation requires an extreme amount of diverse training data, which is prohibitively expensive to collect on a real robot. How can we overcome this problem? Instead of collecting more robot data, this paper proposes using internet-scale, human videos to extract "affordances," both at the environment and agent level, and distill them into a pre-trained representation. We present a simple framework for pre-training representations on hand, object, and contact "affordance labels" that highlight relevant objects in images and how to interact with them. These affordances are automatically extracted from human video data (with the help of off-the-shelf computer vision modules) and used to fine-tune existing representations. Our approach can efficiently fine-tune *any* existing representation, and results in models with stronger downstream robotic performance across the board. We experimentally demonstrate (using 3000+ robot trials) that this affordance pre-training scheme boosts performance by a minimum of 15% on 5 real-world tasks, which consider three diverse robot morphologies (including a dexterous hand). Unlike prior works in the space, these representations improve performance across 3 different camera views. Quantitatively, we find that our approach leads to higher levels of generalization in out-of-distribution settings. For code, weights, and data check: https://hrp-robot.github.io

## 参考
- http://arxiv.org/abs/2407.18911v1

