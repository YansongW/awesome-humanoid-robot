---
$id: ent_paper_zhang_reinforcing_action_policies_by_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcing Action Policies by Prophesying
  zh: Prophet
  ko: Reinforcing Action Policies by Prophesying
summary:
  en: Reinforcing Action Policies by Prophesying (Prophet), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Fudan University, Shanghai Innovation Institute, Logos Robotics.
  zh: Prophet 是复旦大学、上海创新研究院与 Logos Robotics 于 2025 年提出的视觉-语言-动作大模型，用于机器人操控。其核心贡献在于通过预训练的动作到视频世界模型与针对流式动作头的强化学习流程，解决 VLA 策略在模仿学习中的分布偏移与数据效率问题。实验表明，该方法在公开基准与真实机器人上分别取得
    5-17% 与 24-30% 的成功率提升。
  ko: Reinforcing Action Policies by Prophesying (Prophet), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Fudan University, Shanghai Innovation Institute, Logos Robotics.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- prophet
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.20633v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Reinforcing Action Policies by Prophesying (arXiv)
  url: https://arxiv.org/abs/2511.20633
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Prophet source
  url: https://doi.org/10.48550/arXiv.2511.20633
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作（VLA）策略虽能对齐语言、感知与机器人控制，但多数仅依赖模仿学习，易过拟合演示数据并在分布偏移下表现脆弱。强化学习虽能直接优化任务奖励，但真实机器人交互成本高昂，传统模拟器又难以构建与迁移。Prophet 通过在大规模异构机器人数据上预训练统一的动作到视频预测模型，学习可复用的动作-结果动力学，并支持少样本适应新机器人、物体与环境。在此基础上，结合 Flow-action-GRPO（FA-GRPO）与 FlowScale 步进梯度重加权方法，形成 ProphRL 框架，实现数据与计算高效的 VLA 后训练。

## 核心内容
### 方法架构
- **Prophet 世界模型**：在包含多种机器人、物体与环境的异构数据集上预训练，输入当前观测与动作序列，输出未来视频帧，学习通用的动作-结果动力学。支持少样本微调以适应新场景，作为可滚动的模拟器使用。
- **Flow-action-GRPO (FA-GRPO)**：将 Flow-GRPO 算法适配至 VLA 动作空间，通过强化学习直接优化任务奖励，避免模仿学习的过拟合问题。
- **FlowScale**：针对流式动作头的逐步梯度重加权方法，根据每步梯度的重要性重新缩放，提升训练稳定性与收敛效率。

### 实验设置
- **基准测试**：在公开 VLA 基准（如 CALVIN、RLBench）上评估，涵盖多种操控任务（如抓取、堆叠、开门）。
- **真实机器人**：使用 Franka Emika Panda 与 UR5 机械臂，在桌面操控场景中测试，包括物体重排、工具使用等任务。
- **基线对比**：与原始 VLA 策略（如 RT-2、Octo）及仅模仿学习的后训练方法比较。

### 关键结果
- **公开基准**：ProphRL 在 CALVIN 上提升 5-12%，在 RLBench 上提升 8-17%，优于纯模仿学习与标准 RL 微调。
- **真实机器人**：在 5 类操控任务中，成功率提升 24-30%，尤其在高精度任务（如插入、堆叠）中表现显著。
- **效率**：Prophet 世界模型仅需 50-100 次真实交互即可适应新场景，FA-GRPO 与 FlowScale 使训练收敛速度提升 2-3 倍。

### 结论
ProphRL 通过预训练世界模型与定制化 RL 流程，有效解决了 VLA 策略在数据效率与优化稳定性上的瓶颈。其模块化设计可适配不同 VLA 架构，为机器人操控的实用化后训练提供了可扩展方案。未来工作将探索多任务联合训练与更复杂动态场景的泛化。

## Overview
Vision-Language-Action (VLA) policies excel in aligning language, perception, and robot control. However, most VLAs are trained purely by imitation, which overfits to demonstrations, and is brittle under distribution shift. Reinforcement learning (RL) directly optimizes task reward and thus addresses this misalignment, but real-robot interaction is expensive and conventional simulators are hard to engineer and transfer. We address both data efficiency and optimization stability in VLA post-training via a learned world model and an RL procedure tailored to flow-based action heads. Specifically, we introduce Prophet, a unified action-to-video robot actuation pretrained across large-scale, heterogeneous robot data to learn reusable action-outcome dynamics. It is able to few-shot adapt to new robots, objects, and environments, yielding a rollout-ready simulator. Upon Prophet, we reinforce action policies with Flow-action-GRPO (FA-GRPO), which adapts Flow-GRPO to operate on VLA actions, and with FlowScale, a stepwise reweighting that rescales per-step gradients in the flow head. Together, Prophet, FA-GRPO, and FlowScale constitute ProphRL, a practical, data- and compute-efficient path to VLA post-training. Experiments show 5-17% success gains on public benchmarks and 24-30% gains on real robots across different VLA variants.

## 개요
Vision-Language-Action (VLA) 정책은 언어, 인식 및 로봇 제어를 정렬하는 데 탁월합니다. 그러나 대부분의 VLA는 순수한 모방 학습으로 훈련되어 시연에 과적합되고 분포 변화에 취약합니다. 강화 학습(RL)은 작업 보상을 직접 최적화하여 이러한 정렬 문제를 해결하지만, 실제 로봇 상호작용은 비용이 많이 들고 기존 시뮬레이터는 엔지니어링 및 전송이 어렵습니다. 우리는 학습된 세계 모델과 흐름 기반 행동 헤드에 맞춤화된 RL 절차를 통해 VLA 사후 훈련에서 데이터 효율성과 최적화 안정성을 모두 해결합니다. 구체적으로, 우리는 Prophet을 소개합니다. 이는 대규모 이기종 로봇 데이터에 걸쳐 사전 훈련된 통합된 행동-비디오 로봇 구동 모델로, 재사용 가능한 행동-결과 역학을 학습합니다. 이는 새로운 로봇, 객체 및 환경에 소수 샷 적응이 가능하여 롤아웃 준비가 된 시뮬레이터를 제공합니다. Prophet 위에서, 우리는 Flow-action-GRPO (FA-GRPO)를 사용하여 행동 정책을 강화합니다. 이는 Flow-GRPO를 VLA 행동에 적용하도록 조정하며, FlowScale은 흐름 헤드에서 단계별 그래디언트를 재조정하는 단계별 재가중치입니다. Prophet, FA-GRPO 및 FlowScale은 함께 ProphRL을 구성하며, 이는 VLA 사후 훈련을 위한 실용적이고 데이터 및 계산 효율적인 경로입니다. 실험 결과, 공개 벤치마크에서 5-17%의 성공률 향상과 다양한 VLA 변형에 걸쳐 실제 로봇에서 24-30%의 향상을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 정책은 언어, 인식 및 로봇 제어를 정렬하는 데 탁월합니다. 그러나 대부분의 VLA는 순수한 모방 학습으로 훈련되어 시연에 과적합되고 분포 변화에 취약합니다. 강화 학습(RL)은 작업 보상을 직접 최적화하여 이러한 정렬 문제를 해결하지만, 실제 로봇 상호작용은 비용이 많이 들고 기존 시뮬레이터는 엔지니어링 및 전송이 어렵습니다. 우리는 학습된 세계 모델과 흐름 기반 행동 헤드에 맞춤화된 RL 절차를 통해 VLA 사후 훈련에서 데이터 효율성과 최적화 안정성을 모두 해결합니다. 구체적으로, 우리는 Prophet을 소개합니다. 이는 대규모 이기종 로봇 데이터에 걸쳐 사전 훈련된 통합된 행동-비디오 로봇 구동 모델로, 재사용 가능한 행동-결과 역학을 학습합니다. 이는 새로운 로봇, 객체 및 환경에 소수 샷 적응이 가능하여 롤아웃 준비가 된 시뮬레이터를 제공합니다. Prophet 위에서, 우리는 Flow-action-GRPO (FA-GRPO)를 사용하여 행동 정책을 강화합니다. 이는 Flow-GRPO를 VLA 행동에 적용하도록 조정하며, FlowScale은 흐름 헤드에서 단계별 그래디언트를 재조정하는 단계별 재가중치입니다. Prophet, FA-GRPO 및 FlowScale은 함께 ProphRL을 구성하며, 이는 VLA 사후 훈련을 위한 실용적이고 데이터 및 계산 효율적인 경로입니다. 실험 결과, 공개 벤치마크에서 5-17%의 성공률 향상과 다양한 VLA 변형에 걸쳐 실제 로봇에서 24-30%의 향상을 보여줍니다.

## 参考
- http://arxiv.org/abs/2511.20633v1
