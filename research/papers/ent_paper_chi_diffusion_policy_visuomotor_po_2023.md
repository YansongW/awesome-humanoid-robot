---
$id: ent_paper_chi_diffusion_policy_visuomotor_po_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion'
  zh: 扩散策略：通过动作扩散实现视觉运动策略学习
  ko: '디퓨전 정책: 행동 확산을 통한 시각운동 정책 학습'
summary:
  en: Diffusion Policy represents robot visuomotor policies as conditional denoising diffusion processes over the action space,
    learning the score gradient of action distributions and iteratively denoising actions via stochastic Langevin dynamics
    conditioned on visual observations. Evaluated across 15 tasks from four manipulation benchmarks and real-world robot setups,
    it outperforms prior state-of-the-art robot learning methods by an average of 46.9%.
  zh: Diffusion Policy 由哥伦比亚大学提出，将机器人视觉运动策略表示为动作空间上的条件去噪扩散过程。该方法通过随机 Langevin 动力学迭代去噪动作，在 15 个任务上平均超越先前最优方法 46.9%。
  ko: 디퓨전 정책은 로봇의 시각운동 정책을 동작 공간에 대한 조건부 노이즈 제거 확산 과정으로 모델링하여, 시각 관찰을 조건으로 행동 분포의 점수 기울기를 학습하고 확률적 랑주뱅 동역학을 통해 반복적으로 노이즈를
    제거한다. 4개의 조작 벤치마크에서 15개 작업과 실제 로봇 설정에서 평가한 결과, 기존 최신 로봇 학습 방법보다 평균 46.9% 향상된 성능을 보였다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_policy
- imitation_learning
- visuomotor_policy
- behavior_cloning
- robot_manipulation
- action_diffusion
- langevin_dynamics
- score_matching
- receding_horizon_control
- multimodal_actions
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.04137v5. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Diffusion Policy: Visuomotor Policy Learning via Action Diffusion'
  url: https://arxiv.org/abs/2303.04137
  date: '2023'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---
## 概述
Diffusion Policy 将机器人视觉运动策略建模为条件去噪扩散过程，学习动作分布得分函数的梯度，并在推理时通过随机 Langevin 动力学步骤迭代优化。该方法在 4 个操作基准的 12 个不同任务上进行了评估，平均性能提升 46.9%。扩散公式为机器人策略带来了多项优势，包括优雅处理多模态动作分布、适应高维动作空间以及出色的训练稳定性。为在实体机器人上充分释放扩散模型的潜力，该工作提出了关键技术创新，包括引入滚动时域控制、视觉条件以及时间序列扩散 Transformer。

## 核心内容
### 方法架构
Diffusion Policy 的核心是将机器人视觉运动策略表示为条件去噪扩散过程。具体而言，它学习动作分布得分函数的梯度，并在推理时通过一系列随机 Langevin 动力学步骤，根据该梯度场进行迭代优化。

### 关键技术贡献
- **滚动时域控制 (Receding Horizon Control)**：通过预测未来一段时间的动作序列，并仅执行第一步，然后重新规划，实现了闭环控制。
- **视觉条件 (Visual Conditioning)**：将视觉观测作为扩散过程的条件，使策略能够根据当前场景生成合适的动作。
- **时间序列扩散 Transformer (Time-Series Diffusion Transformer)**：专门设计的 Transformer 架构，用于处理动作序列的时间依赖性，提升生成动作的连贯性。

### 实验设置与结果
- **基准与任务**：在 4 个不同的机器人操作基准上，涵盖 12 个不同任务进行评测。
- **性能提升**：相比现有最优的机器人学习方法，平均性能提升 46.9%。
- **核心优势**：
  - 优雅处理多模态动作分布，能够生成多种可行的动作方案。
  - 适应高维动作空间，适用于复杂机器人系统。
  - 训练稳定性出色，降低了调参难度。

### 结论
Diffusion Policy 通过将扩散模型引入机器人视觉运动策略学习，显著提升了性能，并展示了扩散模型在机器人领域的巨大潜力。代码、数据和训练细节已公开于 diffusion-policy.cs.columbia.edu。

## Overview
This paper introduces Diffusion Policy, a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process. We benchmark Diffusion Policy across 12 different tasks from 4 different robot manipulation benchmarks and find that it consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9%. Diffusion Policy learns the gradient of the action-distribution score function and iteratively optimizes with respect to this gradient field during inference via a series of stochastic Langevin dynamics steps. We find that the diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for high-dimensional action spaces, and exhibiting impressive training stability. To fully unlock the potential of diffusion models for visuomotor policy learning on physical robots, this paper presents a set of key technical contributions including the incorporation of receding horizon control, visual conditioning, and the time-series diffusion transformer. We hope this work will help motivate a new generation of policy learning techniques that are able to leverage the powerful generative modeling capabilities of diffusion models. Code, data, and training details is publicly available diffusion-policy.cs.columbia.edu

## 개요
이 논문은 로봇의 시각-운동 정책을 조건부 잡음 제거 확산 과정으로 표현하여 로봇 행동을 생성하는 새로운 방법인 Diffusion Policy를 소개합니다. 우리는 4가지 다른 로봇 조작 벤치마크의 12가지 다양한 작업에서 Diffusion Policy를 평가했으며, 평균 46.9%의 성능 향상으로 기존 최첨단 로봇 학습 방법을 일관되게 능가한다는 것을 발견했습니다. Diffusion Policy는 행동 분포 점수 함수의 기울기를 학습하고, 일련의 확률적 Langevin 역학 단계를 통해 추론 중에 이 기울기 필드에 대해 반복적으로 최적화합니다. 우리는 확산 공식이 로봇 정책에 사용될 때 다중 모드 행동 분포를 우아하게 처리하고, 고차원 행동 공간에 적합하며, 인상적인 훈련 안정성을 보여주는 등 강력한 이점을 제공한다는 것을 발견했습니다. 물리적 로봇에서 시각-운동 정책 학습을 위한 확산 모델의 잠재력을 완전히 활용하기 위해, 이 논문은 후퇴 수평 제어, 시각적 조건화, 시계열 확산 트랜스포머의 통합을 포함한 일련의 핵심 기술적 기여를 제시합니다. 이 연구가 확산 모델의 강력한 생성 모델링 능력을 활용할 수 있는 새로운 세대의 정책 학습 기술을 촉진하는 데 도움이 되기를 바랍니다. 코드, 데이터 및 훈련 세부 사항은 diffusion-policy.cs.columbia.edu에서 공개적으로 제공됩니다.

## 핵심 내용
이 논문은 로봇의 시각-운동 정책을 조건부 잡음 제거 확산 과정으로 표현하여 로봇 행동을 생성하는 새로운 방법인 Diffusion Policy를 소개합니다. 우리는 4가지 다른 로봇 조작 벤치마크의 12가지 다양한 작업에서 Diffusion Policy를 평가했으며, 평균 46.9%의 성능 향상으로 기존 최첨단 로봇 학습 방법을 일관되게 능가한다는 것을 발견했습니다. Diffusion Policy는 행동 분포 점수 함수의 기울기를 학습하고, 일련의 확률적 Langevin 역학 단계를 통해 추론 중에 이 기울기 필드에 대해 반복적으로 최적화합니다. 우리는 확산 공식이 로봇 정책에 사용될 때 다중 모드 행동 분포를 우아하게 처리하고, 고차원 행동 공간에 적합하며, 인상적인 훈련 안정성을 보여주는 등 강력한 이점을 제공한다는 것을 발견했습니다. 물리적 로봇에서 시각-운동 정책 학습을 위한 확산 모델의 잠재력을 완전히 활용하기 위해, 이 논문은 후퇴 수평 제어, 시각적 조건화, 시계열 확산 트랜스포머의 통합을 포함한 일련의 핵심 기술적 기여를 제시합니다. 이 연구가 확산 모델의 강력한 생성 모델링 능력을 활용할 수 있는 새로운 세대의 정책 학습 기술을 촉진하는 데 도움이 되기를 바랍니다. 코드, 데이터 및 훈련 세부 사항은 diffusion-policy.cs.columbia.edu에서 공개적으로 제공됩니다.

## 参考
- http://arxiv.org/abs/2303.04137v5
