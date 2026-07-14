---
$id: ent_paper_farooq_integrating_vision_foundation_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Integrating Vision Foundation Models with Reinforcement Learning for Enhanced Object Interaction
  zh: 融合视觉基础模型与强化学习以增强物体交互
  ko: 비전 기초 모델과 강화 학습의 통합을 통한 향상된 객체 상호작용
summary:
  en: This paper integrates the Segment Anything Model (SAM) and YOLOv5 into the observation pipeline of a Proximal Policy
    Optimization (PPO) agent trained in AI2-THOR, achieving a 52.5% higher object-interaction success rate and 68.2% higher
    average cumulative reward than a raw-RGB baseline across four kitchen floor plans.
  zh: 本文将Segment Anything Model（SAM）和YOLOv5集成到在AI2-THOR中训练的近端策略优化（PPO）智能体的观测流程中，在四个厨房场景中将物体交互成功率提高52.5%、平均累积奖励提高68.2%。
  ko: 본 논문은 AI2-THOR에서 학습된 PPO(Proximal Policy Optimization) 에이전트의 관측 파이프라인에 SAM(Segment Anything Model)과 YOLOv5를 통합하여 4개의
    주방 환경에서 원시 RGB 기준선 대비 객체 상호작용 성공률을 52.5%, 평균 누적 보상을 68.2% 향상시켰다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.05838v1.
sources:
- id: src_001
  type: paper
  title: Integrating Vision Foundation Models with Reinforcement Learning for Enhanced Object Interaction
  url: https://arxiv.org/abs/2508.05838
  date: '2025'
  accessed_at: '2026-06-28'
  doi: 10.1145/3747393.3747399
theoretical_depth:
- method
---
## 概述
This paper presents a novel approach that integrates vision foundation models with reinforcement learning to enhance object interaction capabilities in simulated environments. By combining the Segment Anything Model (SAM) and YOLOv5 with a Proximal Policy Optimization (PPO) agent operating in the AI2-THOR simulation environment, we enable the agent to perceive and interact with objects more effectively. Our comprehensive experiments, conducted across four diverse indoor kitchen settings, demonstrate significant improvements in object interaction success rates and navigation efficiency compared to a baseline agent without advanced perception. The results show a 68% increase in average cumulative reward, a 52.5% improvement in object interaction success rate, and a 33% increase in navigation efficiency. These findings highlight the potential of integrating foundation models with reinforcement learning for complex robotic tasks, paving the way for more sophisticated and capable autonomous agents.

## 核心内容
This paper presents a novel approach that integrates vision foundation models with reinforcement learning to enhance object interaction capabilities in simulated environments. By combining the Segment Anything Model (SAM) and YOLOv5 with a Proximal Policy Optimization (PPO) agent operating in the AI2-THOR simulation environment, we enable the agent to perceive and interact with objects more effectively. Our comprehensive experiments, conducted across four diverse indoor kitchen settings, demonstrate significant improvements in object interaction success rates and navigation efficiency compared to a baseline agent without advanced perception. The results show a 68% increase in average cumulative reward, a 52.5% improvement in object interaction success rate, and a 33% increase in navigation efficiency. These findings highlight the potential of integrating foundation models with reinforcement learning for complex robotic tasks, paving the way for more sophisticated and capable autonomous agents.

## 参考
- http://arxiv.org/abs/2508.05838v1

