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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.21723v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (736 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2602.21723v1

## 개요
LessMimic은 거리장(distance field)을 통합 상호작용 표현으로 활용하여, 단일 전신 제어 정책이 거리장에서 도출된 기하학적 단서(표면 거리, 기울기, 속도 분해)를 기반으로 추론할 수 있게 하며, 동작 참조나 작업별 보상이 필요하지 않습니다. 이 방법은 변분 오토인코더(VAE)를 통해 상호작용 잠재 변수를 인코딩하고, 강화 학습(RL) 하에서 적대적 상호작용 사전(adversarial interaction prior)을 사용하여 사후 훈련을 수행합니다. DAgger 스타일의 지식 증류를 통해 거리장 잠재 변수와 자기 중심적 깊이 특징을 정렬함으로써, LessMimic은 모션 캡처 인프라 없이도 순수 비전 기반 배포로 원활하게 전환할 수 있습니다. 실험 결과, 단일 정책이 객체 크기 변화 시 높은 성공률을 유지하고, 긴 시퀀스 작업에서도 강건성을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **거리장 표현**: 상호작용을 거리장에서 도출된 기하학적 단서(표면 거리, 기울기, 속도 분해)로 모델링하여, 기존의 동작 참조나 작업별 보상을 대체합니다.
- **잠재 변수 인코딩**: 변분 오토인코더(VAE)를 사용하여 상호작용 잠재 변수를 인코딩하고, 적대적 상호작용 사전(AIP)을 통해 강화 학습(RL) 프레임워크에서 사후 훈련을 수행합니다.
- **비전 전이**: DAgger 스타일의 증류를 통해 거리장 잠재 변수와 자기 중심적 깊이 특징을 정렬하여, MoCap 인프라 없이 순수 비전 기반 배포를 구현합니다.

### 실험 설정 및 주요 결과
- **객체 크기 일반화**: PickUp 및 SitStand 작업에서 0.4x~1.6x 크기의 객체에 대해 LessMimic은 80~100% 성공률을 유지하는 반면, 기준 방법은 성능이 급격히 저하됩니다.
- **다중 작업 조합**: 5개의 작업 인스턴스 궤적에서 62.1% 성공률을 달성하고, 최대 40개의 연속 조합 작업을 지원합니다.
- **참조 없는 추론**: 동작 참조나 작업별 보상 없이 로컬 기하학적 상호작용을 통해 일반화와 기술 조합을 구현합니다.

### 결론
LessMimic은 상호작용을 데모가 아닌 로컬 기하학에 고정함으로써, 비구조화 환경에서 휴머노이드 로봇의 일반화, 기술 조합 및 오류 복구를 위한 확장 가능한 경로를 제공합니다.
