---
$id: ent_paper_smap_self_supervised_motion_ad_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control'
  zh: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control'
  ko: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control'
summary:
  en: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control is a 2025 work on loco-manipulation
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
- loco_manipulation
- smap
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.19463v1.
sources:
- id: src_001
  type: paper
  title: 'SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control (arXiv)'
  url: https://arxiv.org/abs/2505.19463
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents a novel framework that enables real-world humanoid robots to maintain stability while performing human-like motion. Current methods train a policy which allows humanoid robots to follow human body using the massive retargeted human data via reinforcement learning. However, due to the heterogeneity between human and humanoid robot motion, directly using retargeted human motion reduces training efficiency and stability. To this end, we introduce SMAP, a novel whole-body tracking framework that bridges the gap between human and humanoid action spaces, enabling accurate motion mimicry by humanoid robots. The core idea is to use a vector-quantized periodic autoencoder to capture generic atomic behaviors and adapt human motion into physically plausible humanoid motion. This adaptation accelerates training convergence and improves stability when handling novel or challenging motions. We then employ a privileged teacher to distill precise mimicry skills into the student policy with a proposed decoupled reward. We conduct experiments in simulation and real world to demonstrate the superiority stability and performance of SMAP over SOTA methods, offering practical guidelines for advancing whole-body control in humanoid robots.

## 核心内容
This paper presents a novel framework that enables real-world humanoid robots to maintain stability while performing human-like motion. Current methods train a policy which allows humanoid robots to follow human body using the massive retargeted human data via reinforcement learning. However, due to the heterogeneity between human and humanoid robot motion, directly using retargeted human motion reduces training efficiency and stability. To this end, we introduce SMAP, a novel whole-body tracking framework that bridges the gap between human and humanoid action spaces, enabling accurate motion mimicry by humanoid robots. The core idea is to use a vector-quantized periodic autoencoder to capture generic atomic behaviors and adapt human motion into physically plausible humanoid motion. This adaptation accelerates training convergence and improves stability when handling novel or challenging motions. We then employ a privileged teacher to distill precise mimicry skills into the student policy with a proposed decoupled reward. We conduct experiments in simulation and real world to demonstrate the superiority stability and performance of SMAP over SOTA methods, offering practical guidelines for advancing whole-body control in humanoid robots.

## 参考
- http://arxiv.org/abs/2505.19463v1

## Overview
This paper presents a novel framework that enables real-world humanoid robots to maintain stability while performing human-like motion. Current methods train a policy which allows humanoid robots to follow human body using the massive retargeted human data via reinforcement learning. However, due to the heterogeneity between human and humanoid robot motion, directly using retargeted human motion reduces training efficiency and stability. To this end, we introduce SMAP, a novel whole-body tracking framework that bridges the gap between human and humanoid action spaces, enabling accurate motion mimicry by humanoid robots. The core idea is to use a vector-quantized periodic autoencoder to capture generic atomic behaviors and adapt human motion into physically plausible humanoid motion. This adaptation accelerates training convergence and improves stability when handling novel or challenging motions. We then employ a privileged teacher to distill precise mimicry skills into the student policy with a proposed decoupled reward. We conduct experiments in simulation and real world to demonstrate the superiority stability and performance of SMAP over SOTA methods, offering practical guidelines for advancing whole-body control in humanoid robots.

## Content
This paper presents a novel framework that enables real-world humanoid robots to maintain stability while performing human-like motion. Current methods train a policy which allows humanoid robots to follow human body using the massive retargeted human data via reinforcement learning. However, due to the heterogeneity between human and humanoid robot motion, directly using retargeted human motion reduces training efficiency and stability. To this end, we introduce SMAP, a novel whole-body tracking framework that bridges the gap between human and humanoid action spaces, enabling accurate motion mimicry by humanoid robots. The core idea is to use a vector-quantized periodic autoencoder to capture generic atomic behaviors and adapt human motion into physically plausible humanoid motion. This adaptation accelerates training convergence and improves stability when handling novel or challenging motions. We then employ a privileged teacher to distill precise mimicry skills into the student policy with a proposed decoupled reward. We conduct experiments in simulation and real world to demonstrate the superiority stability and performance of SMAP over SOTA methods, offering practical guidelines for advancing whole-body control in humanoid robots.

## 개요
본 논문은 실제 휴머노이드 로봇이 인간과 유사한 동작을 수행하면서 안정성을 유지할 수 있도록 하는 새로운 프레임워크를 제시합니다. 현재 방법들은 강화 학습을 통해 대규모 리타겟팅된 인간 데이터를 사용하여 휴머노이드 로봇이 인간의 신체를 따라할 수 있는 정책을 훈련합니다. 그러나 인간과 휴머노이드 로봇 동작 간의 이질성으로 인해 리타겟팅된 인간 동작을 직접 사용하면 훈련 효율성과 안정성이 저하됩니다. 이를 해결하기 위해 우리는 SMAP을 소개합니다. 이는 인간과 휴머노이드 행동 공간 간의 격차를 해소하여 휴머노이드 로봇이 정확한 동작 모방을 가능하게 하는 새로운 전신 추적 프레임워크입니다. 핵심 아이디어는 벡터 양자화 주기적 오토인코더를 사용하여 일반적인 원자적 행동을 포착하고 인간 동작을 물리적으로 타당한 휴머노이드 동작으로 적응시키는 것입니다. 이러한 적응은 훈련 수렴을 가속화하고 새롭거나 도전적인 동작을 처리할 때 안정성을 향상시킵니다. 그런 다음 특권 교사를 사용하여 제안된 분리 보상으로 학생 정책에 정밀한 모방 기술을 증류합니다. 우리는 시뮬레이션과 실제 환경에서 실험을 수행하여 SMAP이 최신 방법보다 우수한 안정성과 성능을 입증하고, 휴머노이드 로봇의 전신 제어 발전을 위한 실용적인 지침을 제공합니다.

## 핵심 내용
본 논문은 실제 휴머노이드 로봇이 인간과 유사한 동작을 수행하면서 안정성을 유지할 수 있도록 하는 새로운 프레임워크를 제시합니다. 현재 방법들은 강화 학습을 통해 대규모 리타겟팅된 인간 데이터를 사용하여 휴머노이드 로봇이 인간의 신체를 따라할 수 있는 정책을 훈련합니다. 그러나 인간과 휴머노이드 로봇 동작 간의 이질성으로 인해 리타겟팅된 인간 동작을 직접 사용하면 훈련 효율성과 안정성이 저하됩니다. 이를 해결하기 위해 우리는 SMAP을 소개합니다. 이는 인간과 휴머노이드 행동 공간 간의 격차를 해소하여 휴머노이드 로봇이 정확한 동작 모방을 가능하게 하는 새로운 전신 추적 프레임워크입니다. 핵심 아이디어는 벡터 양자화 주기적 오토인코더를 사용하여 일반적인 원자적 행동을 포착하고 인간 동작을 물리적으로 타당한 휴머노이드 동작으로 적응시키는 것입니다. 이러한 적응은 훈련 수렴을 가속화하고 새롭거나 도전적인 동작을 처리할 때 안정성을 향상시킵니다. 그런 다음 특권 교사를 사용하여 제안된 분리 보상으로 학생 정책에 정밀한 모방 기술을 증류합니다. 우리는 시뮬레이션과 실제 환경에서 실험을 수행하여 SMAP이 최신 방법보다 우수한 안정성과 성능을 입증하고, 휴머노이드 로봇의 전신 제어 발전을 위한 실용적인 지침을 제공합니다.
