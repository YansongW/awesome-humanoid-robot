---
$id: ent_paper_h_zero_cross_humanoid_locomoti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer'
  zh: 'H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer'
  ko: 'H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer'
summary:
  en: 'H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer is a 2025 work on locomotion
    for humanoid robots.'
  zh: H-Zero 是 2025 年提出的一种跨人形机器人运动预训练框架，由研究团队开发。其核心贡献在于通过有限机器人形态的预训练，实现对新形态人形机器人的零样本与小样本迁移，仅需 30 分钟微调即可适应新平台。
  ko: 'H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- h_zero
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00971v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (700 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer (arXiv)'
  url: https://arxiv.org/abs/2512.00971
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有的人形机器人运动控制器通常针对特定机器人设计，需要为每种形态单独调整奖励函数、物理参数和训练超参数，导致开发成本高昂。H-Zero 通过跨形态预训练学习通用的人形基础策略，在模拟环境中对未见过的机器人能保持高达 81% 的完整运动时长。该框架支持在 30 分钟微调内迁移到新的人形机器人甚至直立四足机器人，显著降低了新形态部署的工程负担。

## 核心内容
### 方法架构
H-Zero 采用跨形态预训练流水线，核心思想是在多种人形机器人形态上联合训练一个通用基础策略。该策略通过共享网络结构学习不同形态间的共同运动特征，避免为每种机器人单独设计控制器。

### 实验设置
- **训练形态**：在有限数量的人形机器人形态上进行预训练，涵盖不同尺寸、关节配置和动力学特性。
- **测试形态**：包括未见过的全新人形机器人以及直立四足机器人，评估零样本与小样本迁移能力。
- **微调时间**：小样本迁移仅需 30 分钟微调，即可适应新形态。

### 关键结果
- **零样本迁移**：预训练策略在模拟环境中对未见过的机器人能维持高达 81% 的完整运动时长，表明其具备强大的泛化能力。
- **小样本迁移**：通过 30 分钟微调，策略可成功迁移到新的人形机器人和直立四足机器人，验证了跨形态迁移的可行性。
- **效率提升**：相比从头训练，H-Zero 大幅减少了新形态部署所需的时间和计算资源。

### 结论
H-Zero 证明了跨形态预训练在人形机器人运动控制中的有效性，为构建通用、可迁移的机器人控制器提供了新范式。未来工作可探索更广泛的形态覆盖和真实机器人部署。

## Overview
The rapid advancement of humanoid robotics has intensified the need for robust and adaptable controllers to enable stable and efficient locomotion across diverse platforms. However, developing such controllers remains a significant challenge because existing solutions are tailored to specific robot designs, requiring extensive tuning of reward functions, physical parameters, and training hyperparameters for each embodiment. To address this challenge, we introduce H-Zero, a cross-humanoid locomotion pretraining pipeline that learns a generalizable humanoid base policy. We show that pretraining on a limited set of embodiments enables zero-shot and few-shot transfer to novel humanoid robots with minimal fine-tuning. Evaluations show that the pretrained policy maintains up to 81% of the full episode duration on unseen robots in simulation while enabling few-shot transfer to unseen humanoids and upright quadrupeds within 30 minutes of fine-tuning.

## 参考
- http://arxiv.org/abs/2512.00971v1

## 개요
기존의 휴머노이드 로봇 운동 제어기는 특정 로봇에 맞춰 설계되어, 각 형태에 따라 보상 함수, 물리 파라미터, 훈련 하이퍼파라미터를 개별적으로 조정해야 하므로 개발 비용이 높습니다. H-Zero는 교차 형태 사전 훈련을 통해 일반적인 휴머노이드 기반 정책을 학습하며, 시뮬레이션 환경에서 본 적 없는 로봇에 대해 최대 81%의 전체 운동 지속 시간을 유지합니다. 이 프레임워크는 30분 미세 조정 내에 새로운 휴머노이드 로봇이나 직립 사족 로봇으로 전이할 수 있어, 새로운 형태 배포의 엔지니어링 부담을 크게 줄입니다.

## 핵심 내용
### 방법 아키텍처
H-Zero는 교차 형태 사전 훈련 파이프라인을 채택하며, 핵심 아이디어는 여러 휴머노이드 로봇 형태에서 공통 기반 정책을 공동 훈련하는 것입니다. 이 정책은 공유 네트워크 구조를 통해 다양한 형태 간의 공통 운동 특징을 학습하여, 각 로봇에 대해 개별 제어기를 설계할 필요를 없앱니다.

### 실험 설정
- **훈련 형태**: 제한된 수의 휴머노이드 로봇 형태에서 사전 훈련하며, 다양한 크기, 관절 구성, 동역학 특성을 포함합니다.
- **테스트 형태**: 본 적 없는 새로운 휴머노이드 로봇과 직립 사족 로봇을 포함하여, 제로샷 및 소수 샷 전이 능력을 평가합니다.
- **미세 조정 시간**: 소수 샷 전이는 30분 미세 조정만으로 새로운 형태에 적응할 수 있습니다.

### 주요 결과
- **제로샷 전이**: 사전 훈련된 정책은 시뮬레이션 환경에서 본 적 없는 로봇에 대해 최대 81%의 전체 운동 지속 시간을 유지하여, 강력한 일반화 능력을 입증합니다.
- **소수 샷 전이**: 30분 미세 조정을 통해 정책은 새로운 휴머노이드 로봇과 직립 사족 로봇으로 성공적으로 전이되어, 교차 형태 전이의 실현 가능성을 검증합니다.
- **효율성 향상**: 처음부터 훈련하는 것에 비해, H-Zero는 새로운 형태 배포에 필요한 시간과 계산 자원을 크게 줄입니다.

### 결론
H-Zero는 휴머노이드 로봇 운동 제어에서 교차 형태 사전 훈련의 효과를 입증하며, 일반적이고 전이 가능한 로봇 제어기를 구축하는 새로운 패러다임을 제공합니다. 향후 연구는 더 넓은 형태 범위와 실제 로봇 배포를 탐구할 수 있습니다.
