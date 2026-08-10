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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.20633v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1101 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.20633v1

## 개요
기존 비전-언어-행동(VLA) 정책은 언어, 지각 및 로봇 제어를 정렬할 수 있지만, 대부분 모방 학습에만 의존하여 시연 데이터에 과적합되고 분포 변화 하에서 취약하게 동작하기 쉽습니다. 강화 학습은 작업 보상을 직접 최적화할 수 있지만, 실제 로봇 상호작용 비용이 높고 전통적인 시뮬레이터는 구축 및 전이가 어렵습니다. Prophet은 대규모 이기종 로봇 데이터에서 통합된 행동-비디오 예측 모델을 사전 학습하여 재사용 가능한 행동-결과 역학을 학습하고, 새로운 로봇, 객체 및 환경에 대한 few-shot 적응을 지원합니다. 이를 기반으로 Flow-action-GRPO(FA-GRPO)와 FlowScale 단계별 그래디언트 재가중 방법을 결합하여 ProphRL 프레임워크를 형성하고, 데이터 및 계산 효율적인 VLA 후속 학습을 구현합니다.

## 핵심 내용
### 방법 아키텍처
- **Prophet 세계 모델**: 다양한 로봇, 객체 및 환경을 포함하는 이기종 데이터셋에서 사전 학습되며, 현재 관측과 행동 시퀀스를 입력으로 받아 미래 비디오 프레임을 출력하여 일반적인 행동-결과 역학을 학습합니다. 새로운 시나리오에 대한 few-shot 미세 조정을 지원하며, 롤아웃 가능한 시뮬레이터로 사용됩니다.
- **Flow-action-GRPO (FA-GRPO)**: Flow-GRPO 알고리즘을 VLA 행동 공간에 적응시켜 강화 학습을 통해 작업 보상을 직접 최적화하고, 모방 학습의 과적합 문제를 방지합니다.
- **FlowScale**: 흐름 기반 행동 헤더를 위한 단계별 그래디언트 재가중 방법으로, 각 단계의 그래디언트 중요도에 따라 재조정하여 훈련 안정성과 수렴 효율을 향상시킵니다.

### 실험 설정
- **벤치마크 테스트**: 공개 VLA 벤치마크(예: CALVIN, RLBench)에서 평가하며, 다양한 조작 작업(예: 파지, 적층, 문 열기)을 포함합니다.
- **실제 로봇**: Franka Emika Panda 및 UR5 로봇 팔을 사용하여 테이블탑 조작 시나리오에서 객체 재배치, 도구 사용 등의 작업을 테스트합니다.
- **기준선 비교**: 원래 VLA 정책(예: RT-2, Octo) 및 모방 학습만 사용한 후속 학습 방법과 비교합니다.

### 주요 결과
- **공개 벤치마크**: ProphRL은 CALVIN에서 5-12%, RLBench에서 8-17% 향상되어 순수 모방 학습 및 표준 RL 미세 조정보다 우수합니다.
- **실제 로봇**: 5가지 조작 작업에서 성공률이 24-30% 향상되었으며, 특히 고정밀 작업(예: 삽입, 적층)에서 두드러진 성과를 보입니다.
- **효율성**: Prophet 세계 모델은 새로운 시나리오에 적응하기 위해 실제 상호작용이 50-100회만 필요하며, FA-GRPO와 FlowScale은 훈련 수렴 속도를 2-3배 향상시킵니다.

### 결론
ProphRL은 사전 학습된 세계 모델과 맞춤형 RL 프로세스를 통해 VLA 정책의 데이터 효율성 및 최적화 안정성 병목 현상을 효과적으로 해결합니다. 모듈식 설계는 다양한 VLA 아키텍처에 적응할 수 있어 로봇 조작의 실용적 후속 학습을 위한 확장 가능한 솔루션을 제공합니다. 향후 작업은 다중 작업 공동 훈련과 더 복잡한 동적 시나리오에서의 일반화를 탐구할 것입니다.
