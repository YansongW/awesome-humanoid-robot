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
  zh: 本文提出将视觉基础模型（Segment Anything Model 和 YOLOv5）集成到基于 Proximal Policy Optimization 的强化学习智能体观测流程中，在 AI2-THOR 模拟环境的四个厨房布局下，实现了物体交互成功率提升
    52.5%、平均累积奖励提升 68.2% 的效果，显著优于原始 RGB 基线。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.05838v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (936 chars, DeepSeek).'
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
该研究通过将 SAM 和 YOLOv5 作为感知模块嵌入 PPO 智能体的观测管道，解决了传统强化学习在复杂场景中物体感知与交互能力不足的问题。在 AI2-THOR 的四个不同厨房布局中进行的实验表明，融合视觉基础模型后，智能体不仅物体交互成功率提升 52.5%，平均累积奖励增加 68.2%，导航效率也提高了 33%。这一方法展示了将预训练视觉模型与强化学习结合，能够显著增强智能体在模拟环境中的自主操作能力。

## 核心内容
### 方法架构
- **感知模块**：将 SAM（Segment Anything Model）和 YOLOv5 作为视觉前端，对原始 RGB 图像进行实时分割与目标检测，生成结构化的物体级观测特征。
- **强化学习框架**：采用 PPO（Proximal Policy Optimization）算法，将上述感知特征作为状态输入，训练智能体在 AI2-THOR 环境中执行物体交互任务。
- **环境设置**：使用 AI2-THOR 模拟器中的四个不同厨房布局（floor plans），每个布局包含多种可交互物体（如抽屉、水龙头、微波炉等）。

### 实验设置
- **基线对比**：以仅使用原始 RGB 图像的 PPO 智能体作为基准（raw-RGB baseline）。
- **评估指标**：物体交互成功率（object-interaction success rate）、平均累积奖励（average cumulative reward）、导航效率（navigation efficiency）。
- **训练与测试**：所有智能体在相同环境配置下训练，并在四个厨房布局上分别测试。

### 关键结果
- **物体交互成功率**：融合模型相比基线提升 52.5%。
- **平均累积奖励**：提升 68.2%（原文中为 68% 与 68.2% 两种表述，此处取精确值 68.2%）。
- **导航效率**：提升 33%。
- **结论**：集成视觉基础模型显著增强了 PPO 智能体在复杂室内场景中的物体感知与操作能力，验证了将预训练视觉模型与强化学习结合的有效性，为开发更自主的机器人智能体提供了可行路径。

## Overview
This paper presents a novel approach that integrates vision foundation models with reinforcement learning to enhance object interaction capabilities in simulated environments. By combining the Segment Anything Model (SAM) and YOLOv5 with a Proximal Policy Optimization (PPO) agent operating in the AI2-THOR simulation environment, we enable the agent to perceive and interact with objects more effectively. Our comprehensive experiments, conducted across four diverse indoor kitchen settings, demonstrate significant improvements in object interaction success rates and navigation efficiency compared to a baseline agent without advanced perception. The results show a 68% increase in average cumulative reward, a 52.5% improvement in object interaction success rate, and a 33% increase in navigation efficiency. These findings highlight the potential of integrating foundation models with reinforcement learning for complex robotic tasks, paving the way for more sophisticated and capable autonomous agents.

## 参考
- http://arxiv.org/abs/2508.05838v1

## 개요
이 연구는 SAM과 YOLOv5를 인식 모듈로 PPO 에이전트의 관측 파이프라인에 통합하여, 복잡한 장면에서 전통적인 강화 학습의 객체 인식 및 상호작용 능력 부족 문제를 해결했습니다. AI2-THOR의 네 가지 서로 다른 주방 레이아웃에서 수행된 실험은, 비전 기반 모델을 통합한 후 에이전트의 객체 상호작용 성공률이 52.5% 향상되고, 평균 누적 보상이 68.2% 증가하며, 내비게이션 효율도 33% 개선되었음을 보여줍니다. 이 방법은 사전 훈련된 비전 모델과 강화 학습을 결합하면 시뮬레이션 환경에서 에이전트의 자율 조작 능력을 크게 향상시킬 수 있음을 입증합니다.

## 핵심 내용
### 방법 아키텍처
- **인식 모듈**: SAM(Segment Anything Model)과 YOLOv5를 비전 프론트엔드로 사용하여, 원본 RGB 이미지에 대해 실시간 분할 및 객체 탐지를 수행하고 구조화된 객체 수준 관측 특징을 생성합니다.
- **강화 학습 프레임워크**: PPO(Proximal Policy Optimization) 알고리즘을 채택하여, 위의 인식 특징을 상태 입력으로 사용하고, AI2-THOR 환경에서 객체 상호작용 작업을 수행하도록 에이전트를 훈련합니다.
- **환경 설정**: AI2-THOR 시뮬레이터의 네 가지 서로 다른 주방 레이아웃(floor plans)을 사용하며, 각 레이아웃에는 여러 상호작용 가능한 객체(예: 서랍, 수도꼭지, 전자레인지 등)가 포함됩니다.

### 실험 설정
- **기준 비교**: 원본 RGB 이미지만 사용하는 PPO 에이전트를 기준(raw-RGB baseline)으로 설정합니다.
- **평가 지표**: 객체 상호작용 성공률(object-interaction success rate), 평균 누적 보상(average cumulative reward), 내비게이션 효율(navigation efficiency).
- **훈련 및 테스트**: 모든 에이전트는 동일한 환경 구성에서 훈련되며, 네 가지 주방 레이아웃에서 각각 테스트됩니다.

### 주요 결과
- **객체 상호작용 성공률**: 통합 모델이 기준 대비 52.5% 향상.
- **평균 누적 보상**: 68.2% 증가(원문에는 68%와 68.2% 두 가지 표현이 있으며, 여기서는 정확한 값 68.2%를 사용).
- **내비게이션 효율**: 33% 향상.
- **결론**: 비전 기반 모델 통합은 복잡한 실내 장면에서 PPO 에이전트의 객체 인식 및 조작 능력을 크게 강화하며, 사전 훈련된 비전 모델과 강화 학습의 결합 효과를 검증하여 더 자율적인 로봇 에이전트 개발에 실현 가능한 경로를 제공합니다.
