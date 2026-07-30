---
$id: ent_paper_zheng_flare_robot_learning_with_impl_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FLARE: Robot Learning with Implicit World Modeling'
  zh: FLARE
  ko: 'FLARE: Robot Learning with Implicit World Modeling'
summary:
  en: 'FLARE: Robot Learning with Implicit World Modeling (FLARE), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by California Institute of Technology, and published at CoRL25.'
  zh: FLARE 是加州理工学院于 2025 年 CoRL25 会议提出的大型视觉-语言-动作模型，通过将隐式世界模型与扩散 Transformer 策略结合，使机器人能预测未来观测的潜在表征。该方法仅需对标准 VLA 模型进行极小的架构修改，即可在单臂和人形桌面操作任务中实现最高
    26% 的性能提升，并支持利用无动作标签的人类视频进行协同训练。
  ko: 'FLARE: Robot Learning with Implicit World Modeling (FLARE), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by California Institute of Technology, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- flare
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.15659v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'FLARE: Robot Learning with Implicit World Modeling (arXiv)'
  url: https://arxiv.org/abs/2505.15659
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FLARE source
  url: https://doi.org/10.48550/arXiv.2505.15659
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
FLARE 的核心创新在于将预测性潜在世界模型集成到机器人策略学习中，通过对齐扩散 Transformer 的特征与未来观测的潜在嵌入，使策略在生成动作时能推理长期后果。该方法极其轻量，仅需在标准视觉-语言-动作模型上添加少量 token 即可实现显著性能提升。在两项多任务仿真模仿学习基准测试中，FLARE 均达到最先进水平，性能超越先前基线方法最高达 26%。此外，FLARE 还能与无动作标签的人类第一人称视频进行协同训练，仅需单次机器人演示即可显著提升策略对未见几何形状新物体的泛化能力。

## 核心内容
### 方法架构
FLARE 的核心框架名为“未来潜在表征对齐”，其关键设计包括：
- **预测性潜在世界模型**：将扩散 Transformer 的特征与未来观测的潜在嵌入进行对齐，使策略能隐式预测未来状态。
- **轻量级修改**：仅需在标准 VLA 模型上添加少量 token，无需改变模型主体结构。
- **高频控制兼容**：在保持高频率机器人控制的同时，融入隐式世界模型的推理能力。

### 实验设置与关键数字
- **基准测试**：在两项多任务仿真模仿学习基准上评估，涵盖单臂和人形桌面操作任务。
- **性能提升**：相比先前策略学习基线方法，FLARE 的性能提升最高达 26%。
- **泛化能力**：通过协同训练人类第一人称视频（无动作标签），仅需单次机器人演示即可显著提升对未见几何形状新物体的泛化能力。

### 结论
FLARE 被证明是一种通用且可扩展的方法，能够将隐式世界模型与高频机器人控制有效结合，为机器人策略学习提供了新的范式。

## Overview
We introduce $\textbf{F}$uture $\textbf{LA}$tent $\textbf{RE}$presentation Alignment ($\textbf{FLARE}$), a novel framework that integrates predictive latent world modeling into robot policy learning. By aligning features from a diffusion transformer with latent embeddings of future observations, $\textbf{FLARE}$ enables a diffusion transformer policy to anticipate latent representations of future observations, allowing it to reason about long-term consequences while generating actions. Remarkably lightweight, $\textbf{FLARE}$ requires only minimal architectural modifications -- adding a few tokens to standard vision-language-action (VLA) models -- yet delivers substantial performance gains. Across two challenging multitask simulation imitation learning benchmarks spanning single-arm and humanoid tabletop manipulation, $\textbf{FLARE}$ achieves state-of-the-art performance, outperforming prior policy learning baselines by up to 26%. Moreover, $\textbf{FLARE}$ unlocks the ability to co-train with human egocentric video demonstrations without action labels, significantly boosting policy generalization to a novel object with unseen geometry with as few as a single robot demonstration. Our results establish $\textbf{FLARE}$ as a general and scalable approach for combining implicit world modeling with high-frequency robotic control.

## 개요
우리는 $\textbf{F}$uture $\textbf{LA}$tent $\textbf{RE}$presentation Alignment ($\textbf{FLARE}$)를 소개합니다. 이는 예측적 잠재 세계 모델링을 로봇 정책 학습에 통합하는 새로운 프레임워크입니다. 확산 트랜스포머의 특징을 미래 관측의 잠재 임베딩과 정렬함으로써, $\textbf{FLARE}$는 확산 트랜스포머 정책이 미래 관측의 잠재 표현을 예측할 수 있게 하여, 행동을 생성하는 동안 장기적 결과를 추론할 수 있도록 합니다. 놀랍도록 가벼운 $\textbf{FLARE}$는 최소한의 아키텍처 수정만 필요로 합니다 — 표준 시각-언어-행동(VLA) 모델에 몇 개의 토큰을 추가하는 것 — 그럼에도 상당한 성능 향상을 제공합니다. 단일 암 및 휴머노이드 탁상 조작을 포함한 두 가지 도전적인 멀티태스크 시뮬레이션 모방 학습 벤치마크에서 $\textbf{FLARE}$는 최첨단 성능을 달성하며, 이전 정책 학습 기준선보다 최대 26% 향상된 결과를 보여줍니다. 또한, $\textbf{FLARE}$는 행동 레이블 없이 인간의 자기중심적 비디오 데모와 공동 학습할 수 있는 능력을 열어주어, 단 하나의 로봇 데모만으로도 보이지 않는 형상을 가진 새로운 객체에 대한 정책 일반화를 크게 향상시킵니다. 우리의 결과는 $\textbf{FLARE}$를 암묵적 세계 모델링과 고주파 로봇 제어를 결합하는 일반적이고 확장 가능한 접근 방식으로 확립합니다.

## 핵심 내용
우리는 $\textbf{F}$uture $\textbf{LA}$tent $\textbf{RE}$presentation Alignment ($\textbf{FLARE}$)를 소개합니다. 이는 예측적 잠재 세계 모델링을 로봇 정책 학습에 통합하는 새로운 프레임워크입니다. 확산 트랜스포머의 특징을 미래 관측의 잠재 임베딩과 정렬함으로써, $\textbf{FLARE}$는 확산 트랜스포머 정책이 미래 관측의 잠재 표현을 예측할 수 있게 하여, 행동을 생성하는 동안 장기적 결과를 추론할 수 있도록 합니다. 놀랍도록 가벼운 $\textbf{FLARE}$는 최소한의 아키텍처 수정만 필요로 합니다 — 표준 시각-언어-행동(VLA) 모델에 몇 개의 토큰을 추가하는 것 — 그럼에도 상당한 성능 향상을 제공합니다. 단일 암 및 휴머노이드 탁상 조작을 포함한 두 가지 도전적인 멀티태스크 시뮬레이션 모방 학습 벤치마크에서 $\textbf{FLARE}$는 최첨단 성능을 달성하며, 이전 정책 학습 기준선보다 최대 26% 향상된 결과를 보여줍니다. 또한, $\textbf{FLARE}$는 행동 레이블 없이 인간의 자기중심적 비디오 데모와 공동 학습할 수 있는 능력을 열어주어, 단 하나의 로봇 데모만으로도 보이지 않는 형상을 가진 새로운 객체에 대한 정책 일반화를 크게 향상시킵니다. 우리의 결과는 $\textbf{FLARE}$를 암묵적 세계 모델링과 고주파 로봇 제어를 결합하는 일반적이고 확장 가능한 접근 방식으로 확립합니다.

## 参考
- http://arxiv.org/abs/2505.15659v1
