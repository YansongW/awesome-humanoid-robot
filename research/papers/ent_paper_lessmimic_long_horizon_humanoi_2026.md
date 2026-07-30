---
$id: ent_paper_lessmimic_long_horizon_humanoi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations'
  zh: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations'
  ko: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations'
summary:
  en: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: LessMimic 是 2026 年提出的一种用于人形机器人长时域交互的统一距离场表示方法。它通过单一策略实现无参考运动推理、几何泛化与多技能组合，在 PickUp 和 SitStand 任务上对 0.4x 至 1.6x 尺寸物体保持
    80-100% 成功率，并支持多达 40 个连续组合任务。
  ko: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- lessmimic
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.21723v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations (arXiv)'
  url: https://arxiv.org/abs/2602.21723
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations project page'
  url: https://yzhu.io/preprint/humanoid2026lessmimic/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
LessMimic 利用距离场作为统一交互表示，使单一全身控制策略能够基于距离场导出的几何线索（表面距离、梯度、速度分解）进行推理，无需运动参考或任务特定奖励。该方法通过变分自编码器编码交互隐变量，并采用对抗性交互先验在强化学习下进行后训练。通过 DAgger 风格的知识蒸馏，将距离场隐变量与以自我为中心的深度特征对齐，LessMimic 可无缝迁移至纯视觉部署，无需动作捕捉基础设施。实验表明，单一策略在物体尺寸变化时保持高成功率，并在长序列任务中保持鲁棒性。

## 核心内容
### 方法架构
- **距离场表示**：将交互建模为距离场导出的几何线索，包括表面距离、梯度与速度分解，替代传统运动参考或任务特定奖励。
- **隐变量编码**：使用变分自编码器（VAE）编码交互隐变量，并通过对抗性交互先验（AIP）在强化学习（RL）框架下进行后训练。
- **视觉迁移**：采用 DAgger 风格蒸馏，将距离场隐变量与以自我为中心的深度特征对齐，实现纯视觉部署，无需 MoCap 基础设施。

### 实验设置与关键结果
- **物体尺寸泛化**：在 PickUp 和 SitStand 任务中，对 0.4x 至 1.6x 尺寸物体，LessMimic 保持 80-100% 成功率，而基线方法性能急剧下降。
- **多任务组合**：在 5 个任务实例轨迹上达到 62.1% 成功率，并支持多达 40 个连续组合任务。
- **无参考推理**：无需运动参考或任务特定奖励，通过局部几何交互实现泛化与技能组合。

### 结论
LessMimic 通过将交互锚定于局部几何而非演示，为人形机器人在非结构化环境中的泛化、技能组合与故障恢复提供了可扩展路径。

## Overview
Humanoid robots that autonomously interact with physical environments over extended horizons represent a central goal of embodied intelligence. Existing approaches rely on reference motions or task-specific rewards, tightly coupling policies to particular object geometries and precluding multi-skill generalization within a single framework. A unified interaction representation enabling reference-free inference, geometric generalization, and long-horizon skill composition within one policy remains an open challenge. Here we show that Distance Field (DF) provides such a representation: LessMimic conditions a single whole-body policy on DF-derived geometric cues--surface distances, gradients, and velocity decompositions--removing the need for motion references, with interaction latents encoded via a Variational Auto-Encoder (VAE) and post-trained using Adversarial Interaction Priors (AIP) under Reinforcement Learning (RL). Through DAgger-style distillation that aligns DF latents with egocentric depth features, LessMimic further transfers seamlessly to vision-only deployment without motion capture (MoCap) infrastructure. A single LessMimic policy achieves 80--100% success across object scales from 0.4x to 1.6x on PickUp and SitStand where baselines degrade sharply, attains 62.1% success on 5 task instances trajectories, and remains viable up to 40 sequentially composed tasks. By grounding interaction in local geometry rather than demonstrations, LessMimic offers a scalable path toward humanoid robots that generalize, compose skills, and recover from failures in unstructured environments.

## 개요
물리적 환경과 장기적으로 자율적으로 상호작용하는 휴머노이드 로봇은 구현된 지능의 핵심 목표입니다. 기존 접근 방식은 참조 동작이나 작업별 보상에 의존하여 정책을 특정 객체 형상에 밀접하게 결합시키고, 단일 프레임워크 내에서 다중 기술 일반화를 불가능하게 합니다. 참조 없는 추론, 기하학적 일반화, 장기 기술 구성을 단일 정책 내에서 가능하게 하는 통합된 상호작용 표현은 여전히 해결되지 않은 과제입니다. 본 연구에서는 거리장(Distance Field, DF)이 이러한 표현을 제공함을 보여줍니다: LessMimic은 DF에서 파생된 기하학적 단서(표면 거리, 기울기, 속도 분해)를 기반으로 단일 전신 정책을 조건화하여 동작 참조의 필요성을 제거하며, 상호작용 잠재 변수는 변분 오토인코더(Variational Auto-Encoder, VAE)를 통해 인코딩되고 강화 학습(Reinforcement Learning, RL) 하에서 적대적 상호작용 사전(Adversarial Interaction Priors, AIP)을 사용하여 사후 훈련됩니다. DAgger 스타일의 증류를 통해 DF 잠재 변수를 자기 중심 깊이 특징과 정렬함으로써, LessMimic은 모션 캡처(MoCap) 인프라 없이 시각 전용 배포로 원활하게 전환됩니다. 단일 LessMimic 정책은 PickUp 및 SitStand에서 기준선이 급격히 저하되는 객체 크기 0.4배에서 1.6배까지 80~100%의 성공률을 달성하고, 5개 작업 인스턴스 궤적에서 62.1%의 성공률을 기록하며, 최대 40개의 순차적으로 구성된 작업까지 유지됩니다. 상호작용을 시연이 아닌 국소 기하학에 기반함으로써, LessMimic은 비구조적 환경에서 일반화하고, 기술을 구성하며, 실패로부터 복구하는 휴머노이드 로봇을 위한 확장 가능한 경로를 제공합니다.

## 핵심 내용
물리적 환경과 장기적으로 자율적으로 상호작용하는 휴머노이드 로봇은 구현된 지능의 핵심 목표입니다. 기존 접근 방식은 참조 동작이나 작업별 보상에 의존하여 정책을 특정 객체 형상에 밀접하게 결합시키고, 단일 프레임워크 내에서 다중 기술 일반화를 불가능하게 합니다. 참조 없는 추론, 기하학적 일반화, 장기 기술 구성을 단일 정책 내에서 가능하게 하는 통합된 상호작용 표현은 여전히 해결되지 않은 과제입니다. 본 연구에서는 거리장(DF)이 이러한 표현을 제공함을 보여줍니다: LessMimic은 DF에서 파생된 기하학적 단서(표면 거리, 기울기, 속도 분해)를 기반으로 단일 전신 정책을 조건화하여 동작 참조의 필요성을 제거하며, 상호작용 잠재 변수는 변분 오토인코더(VAE)를 통해 인코딩되고 강화 학습(RL) 하에서 적대적 상호작용 사전(AIP)을 사용하여 사후 훈련됩니다. DAgger 스타일의 증류를 통해 DF 잠재 변수를 자기 중심 깊이 특징과 정렬함으로써, LessMimic은 모션 캡처(MoCap) 인프라 없이 시각 전용 배포로 원활하게 전환됩니다. 단일 LessMimic 정책은 PickUp 및 SitStand에서 기준선이 급격히 저하되는 객체 크기 0.4배에서 1.6배까지 80~100%의 성공률을 달성하고, 5개 작업 인스턴스 궤적에서 62.1%의 성공률을 기록하며, 최대 40개의 순차적으로 구성된 작업까지 유지됩니다. 상호작용을 시연이 아닌 국소 기하학에 기반함으로써, LessMimic은 비구조적 환경에서 일반화하고, 기술을 구성하며, 실패로부터 복구하는 휴머노이드 로봇을 위한 확장 가능한 경로를 제공합니다.

## 参考
- http://arxiv.org/abs/2602.21723v1
