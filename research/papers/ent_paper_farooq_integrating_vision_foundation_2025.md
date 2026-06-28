---
$id: ent_paper_farooq_integrating_vision_foundation_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Integrating Vision Foundation Models with Reinforcement Learning for Enhanced
    Object Interaction
  zh: 融合视觉基础模型与强化学习以增强物体交互
  ko: 비전 기초 모델과 강화 학습의 통합을 통한 향상된 객체 상호작용
summary:
  en: This paper integrates the Segment Anything Model (SAM) and YOLOv5 into the observation
    pipeline of a Proximal Policy Optimization (PPO) agent trained in AI2-THOR, achieving
    a 52.5% higher object-interaction success rate and 68.2% higher average cumulative
    reward than a raw-RGB baseline across four kitchen floor plans.
  zh: 本文将Segment Anything Model（SAM）和YOLOv5集成到在AI2-THOR中训练的近端策略优化（PPO）智能体的观测流程中，在四个厨房场景中将物体交互成功率提高52.5%、平均累积奖励提高68.2%。
  ko: 본 논문은 AI2-THOR에서 학습된 PPO(Proximal Policy Optimization) 에이전트의 관측 파이프라인에 SAM(Segment
    Anything Model)과 YOLOv5를 통합하여 4개의 주방 환경에서 원시 RGB 기준선 대비 객체 상호작용 성공률을 52.5%, 평균
    누적 보상을 68.2% 향상시켰다.
domains:
- 07_ai_models_algorithms
- 10_evaluation_benchmarks
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vision_foundation_model
- reinforcement_learning
- object_interaction
- sam
- yolov5
- ppo
- ai2_thor
- indoor_navigation
- visual_perception
- simulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from arXiv preprint and ACM metadata; quantitative values verified
    against Table I and Section V.A of the paper. Requires human review before final
    verification.
sources:
- id: src_001
  type: paper
  title: Integrating Vision Foundation Models with Reinforcement Learning for Enhanced
    Object Interaction
  url: https://arxiv.org/abs/2508.05838
  date: '2025'
  accessed_at: '2026-06-28'
  doi: 10.1145/3747393.3747399
theoretical_depth:
- method
---

## Overview

Autonomous agents still struggle to combine rich visual perception with effective decision-making when interacting with objects in complex indoor scenes. This paper addresses that gap by embedding two vision foundation models—YOLOv5 for object detection and the Segment Anything Model (SAM) for segmentation—into the observation pipeline of a reinforcement-learning agent. The agent is trained with Proximal Policy Optimization (PPO) inside the AI2-THOR simulator and evaluated on navigation-to-interaction tasks across four distinct kitchen floor plans.

The perception pipeline works as follows. YOLOv5 processes each first-person RGB frame and outputs object bounding boxes and class labels. These bounding boxes are fed as prompts to SAM, which produces segmentation masks that capture precise object contours and spatial relationships. The combined outputs (bounding boxes, class labels, and masks) are then encoded by a convolutional neural network (CNN) into a feature representation φ(s_t) that feeds both the policy and value heads of the PPO network. The reward function r_t = α·Δd_t + β·s_t − γ·c_t combines progress toward the target object, a success indicator for successful interaction, and a collision/invalid-action penalty.

The perception-enhanced agent is compared against a baseline PPO agent that receives only raw RGB observations. Across five runs per condition, the proposed method achieves a success rate of 73.5 ± 2.1% versus 48.2 ± 4.5% for the baseline (a 52.5% improvement), an average cumulative reward of 136.4 ± 5.6 versus 81.1 ± 9.3 (a 68.2% increase), and navigation efficiency of 82.1 ± 1.9% versus 61.7 ± 3.1% (a 33.1% increase). Training is performed for 1 × 10^6 time steps on a workstation with an NVIDIA RTX 3080 GPU and 64 GB of RAM, implemented in PyTorch.

## Key Contributions

- A framework that integrates vision foundation models (SAM and YOLOv5) with reinforcement learning to enhance object interaction capabilities.
- Techniques for efficiently incorporating advanced perception outputs into the RL observation space while managing computational overhead through optimized inference and batch processing.
- Experimental demonstration of substantial improvements over a raw-RGB baseline in success rate, cumulative reward, navigation efficiency, and interaction efficiency.
- Discussion of the implications of merging foundation-model perception with RL and identification of future directions such as domain randomization, model optimization, and sim-to-real transfer.

## Relevance to Humanoid Robotics

The perception-driven RL pipeline developed in this work—object detection, segmentation, navigation, and manipulation in cluttered indoor environments—is directly transferable to humanoid robots. Humanoids deployed in homes, warehouses, and factories must likewise locate target objects, plan collision-free paths, and position themselves for grasping or interaction. The use of foundation vision models to enrich the observation space without task-specific fine-tuning is especially relevant for humanoids that need to generalize across diverse objects and scenes with limited onboard training data.

However, the paper's experiments are confined to AI2-THOR simulation and four kitchen floor plans, so the sim-to-real gap and real-world computational constraints remain open questions for humanoid deployment. The authors explicitly note these limitations and identify future work in domain randomization, model compression, and sim-to-real transfer—topics that are critical for bringing such perception-RL systems to physical humanoid platforms.
