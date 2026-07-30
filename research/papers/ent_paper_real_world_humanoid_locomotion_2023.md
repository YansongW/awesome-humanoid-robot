---
$id: ent_paper_real_world_humanoid_locomotion_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Real-World Humanoid Locomotion with Reinforcement Learning
  zh: Real-World Humanoid Locomotion with Reinforcement Learning
  ko: Real-World Humanoid Locomotion with Reinforcement Learning
summary:
  en: Real-World Humanoid Locomotion with Reinforcement Learning is a 2023 work on locomotion for humanoid robots.
  zh: 本文提出了一种基于强化学习的全学习型人形机器人运动控制方法。该方法由因果Transformer模型驱动，通过大规模模拟训练后零样本迁移至真实世界，使机器人能够在多种户外地形上稳健行走并抵抗外部干扰。
  ko: Real-World Humanoid Locomotion with Reinforcement Learning is a 2023 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- real_world_humanoid_locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.03381v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Real-World Humanoid Locomotion with Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2303.03381
  date: '2023'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Real-World Humanoid Locomotion with Reinforcement Learning project page
  url: https://learning-humanoid-locomotion.github.io/
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对传统人形机器人控制器泛化能力不足的问题，提出了一种完全基于学习的运动控制方案。核心创新在于使用因果Transformer架构，通过处理本体感知观测与动作的历史序列来预测下一步动作，利用上下文信息实现行为自适应而无需更新模型权重。模型在模拟环境中通过无模型强化学习进行大规模训练，并在多样化随机化环境中完成学习后，直接部署到真实人形机器人上实现零样本迁移。实验证明，该控制器能够使机器人在多种户外地形上稳定行走，并具备抵抗外部干扰和上下文自适应能力。

## 核心内容
### 方法架构
- **控制器设计**：采用因果Transformer模型，输入为历史本体感知观测（如关节角度、IMU数据）与动作序列，输出为下一步动作指令。
- **核心假设**：观测-动作历史序列蕴含环境动态信息，Transformer可通过上下文学习（in-context learning）自适应调整行为，无需权重更新。

### 训练策略
- **强化学习框架**：使用无模型（model-free）强化学习算法，在模拟环境中进行大规模训练。
- **环境随机化**：构建包含多种地形、摩擦系数、外部扰动等参数的随机化环境集合，增强模型泛化能力。
- **零样本迁移**：训练完成后直接部署至真实人形机器人，无需额外微调或领域适配。

### 实验设置与结果
- **硬件平台**：未明确指定具体人形机器人型号，但强调在真实世界户外场景测试。
- **性能表现**：
  - 能够稳定行走于草地、碎石路、斜坡等多种户外地形。
  - 对外部推挤、负载变化等干扰具有鲁棒性。
  - 通过上下文历史信息实现实时行为调整（如根据地形变化自动调整步态）。
- **关键数字**：未提供具体成功率或步态参数，但强调零样本迁移的成功实现。

### 结论
该工作证明了纯学习型方法在真实世界人形机器人运动控制中的可行性，Transformer的上下文自适应能力为复杂环境下的泛化提供了新路径。

## Overview
Humanoid robots that can autonomously operate in diverse environments have the potential to help address labour shortages in factories, assist elderly at homes, and colonize new planets. While classical controllers for humanoid robots have shown impressive results in a number of settings, they are challenging to generalize and adapt to new environments. Here, we present a fully learning-based approach for real-world humanoid locomotion. Our controller is a causal transformer that takes the history of proprioceptive observations and actions as input and predicts the next action. We hypothesize that the observation-action history contains useful information about the world that a powerful transformer model can use to adapt its behavior in-context, without updating its weights. We train our model with large-scale model-free reinforcement learning on an ensemble of randomized environments in simulation and deploy it to the real world zero-shot. Our controller can walk over various outdoor terrains, is robust to external disturbances, and can adapt in context.

## 개요
다양한 환경에서 자율적으로 작동할 수 있는 휴머노이드 로봇은 공장의 노동력 부족 해소, 가정에서의 노인 지원, 새로운 행성 개척에 기여할 잠재력을 가지고 있습니다. 휴머노이드 로봇을 위한 기존 제어기는 여러 환경에서 인상적인 결과를 보여주었지만, 새로운 환경에 일반화하고 적응하는 데 어려움이 있습니다. 본 연구에서는 실제 환경에서의 휴머노이드 보행을 위한 완전 학습 기반 접근법을 제시합니다. 우리의 제어기는 인과적 트랜스포머로, 고유수용성 관측과 행동의 이력을 입력으로 받아 다음 행동을 예측합니다. 우리는 관측-행동 이력에 세계에 대한 유용한 정보가 포함되어 있으며, 강력한 트랜스포머 모델이 가중치를 업데이트하지 않고도 맥락 내에서 행동을 적응시키는 데 사용할 수 있다고 가정합니다. 우리는 시뮬레이션에서 무작위화된 환경 집합에 대해 대규모 모델 프리 강화 학습으로 모델을 훈련하고, 제로샷으로 실제 환경에 배포합니다. 우리의 제어기는 다양한 야외 지형을 걸을 수 있고, 외부 교란에 강하며, 맥락 내에서 적응할 수 있습니다.

## 핵심 내용
다양한 환경에서 자율적으로 작동할 수 있는 휴머노이드 로봇은 공장의 노동력 부족 해소, 가정에서의 노인 지원, 새로운 행성 개척에 기여할 잠재력을 가지고 있습니다. 휴머노이드 로봇을 위한 기존 제어기는 여러 환경에서 인상적인 결과를 보여주었지만, 새로운 환경에 일반화하고 적응하는 데 어려움이 있습니다. 본 연구에서는 실제 환경에서의 휴머노이드 보행을 위한 완전 학습 기반 접근법을 제시합니다. 우리의 제어기는 인과적 트랜스포머로, 고유수용성 관측과 행동의 이력을 입력으로 받아 다음 행동을 예측합니다. 우리는 관측-행동 이력에 세계에 대한 유용한 정보가 포함되어 있으며, 강력한 트랜스포머 모델이 가중치를 업데이트하지 않고도 맥락 내에서 행동을 적응시키는 데 사용할 수 있다고 가정합니다. 우리는 시뮬레이션에서 무작위화된 환경 집합에 대해 대규모 모델 프리 강화 학습으로 모델을 훈련하고, 제로샷으로 실제 환경에 배포합니다. 우리의 제어기는 다양한 야외 지형을 걸을 수 있고, 외부 교란에 강하며, 맥락 내에서 적응할 수 있습니다.

## 参考
- http://arxiv.org/abs/2303.03381v2
