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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00971v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
휴머노이드 로보틱스의 급속한 발전은 다양한 플랫폼에서 안정적이고 효율적인 보행을 가능하게 하는 강력하고 적응 가능한 제어기의 필요성을 증가시켰습니다. 그러나 기존 솔루션은 특정 로봇 설계에 맞춰져 있어 각 구현체마다 보상 함수, 물리적 매개변수 및 훈련 하이퍼파라미터를 광범위하게 조정해야 하기 때문에 이러한 제어기를 개발하는 것은 여전히 큰 과제로 남아 있습니다. 이 문제를 해결하기 위해 우리는 일반화 가능한 휴머노이드 기본 정책을 학습하는 교차 휴머노이드 보행 사전 훈련 파이프라인인 H-Zero를 소개합니다. 제한된 구현체 집합에 대한 사전 훈련이 최소한의 미세 조정만으로 새로운 휴머노이드 로봇에 대한 제로샷 및 퓨샷 전이를 가능하게 함을 보여줍니다. 평가 결과, 사전 훈련된 정책은 시뮬레이션에서 보지 못한 로봇에 대해 전체 에피소드 지속 시간의 최대 81%를 유지하며, 30분 이내의 미세 조정으로 보지 못한 휴머노이드 및 직립 사족 로봇에 대한 퓨샷 전이를 가능하게 합니다.

## 핵심 내용
휴머노이드 로보틱스의 급속한 발전은 다양한 플랫폼에서 안정적이고 효율적인 보행을 가능하게 하는 강력하고 적응 가능한 제어기의 필요성을 증가시켰습니다. 그러나 기존 솔루션은 특정 로봇 설계에 맞춰져 있어 각 구현체마다 보상 함수, 물리적 매개변수 및 훈련 하이퍼파라미터를 광범위하게 조정해야 하기 때문에 이러한 제어기를 개발하는 것은 여전히 큰 과제로 남아 있습니다. 이 문제를 해결하기 위해 우리는 일반화 가능한 휴머노이드 기본 정책을 학습하는 교차 휴머노이드 보행 사전 훈련 파이프라인인 H-Zero를 소개합니다. 제한된 구현체 집합에 대한 사전 훈련이 최소한의 미세 조정만으로 새로운 휴머노이드 로봇에 대한 제로샷 및 퓨샷 전이를 가능하게 함을 보여줍니다. 평가 결과, 사전 훈련된 정책은 시뮬레이션에서 보지 못한 로봇에 대해 전체 에피소드 지속 시간의 최대 81%를 유지하며, 30분 이내의 미세 조정으로 보지 못한 휴머노이드 및 직립 사족 로봇에 대한 퓨샷 전이를 가능하게 합니다.

## 参考
- http://arxiv.org/abs/2512.00971v1
