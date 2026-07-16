---
$id: ent_paper_telegate_whole_body_humanoid_t_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior'
  zh: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior'
  ko: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior'
summary:
  en: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior is a 2026 work on teleoperation
    for humanoid robots.'
  zh: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior is a 2026 work on teleoperation
    for humanoid robots.'
  ko: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior is a 2026 work on teleoperation
    for humanoid robots.'
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
- telegate
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.09628v2.
sources:
- id: src_001
  type: paper
  title: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior (arXiv)'
  url: https://arxiv.org/abs/2602.09628
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Real-time whole-body teleoperation is a critical method for humanoid robots to perform complex tasks in unstructured environments. However, developing a unified controller that robustly supports diverse human motions remains a significant challenge. Existing methods typically distill multiple expert policies into a single general policy, which often inevitably leads to performance degradation, particularly on highly dynamic motions. This paper presents TeleGate, a unified whole-body teleoperation framework for humanoid robots that achieves high-precision tracking across various motions while avoiding the performance loss inherent in knowledge distillation. Our key idea is to preserve the full capability of domain-specific expert policies by training a lightweight gating network, which dynamically activates experts in real-time based on proprioceptive states and reference trajectories. Furthermore, to compensate for the absence of future reference trajectories in real-time teleoperation, we introduce a VAE-based motion prior module that extracts implicit future motion intent from historical observations, enabling anticipatory control for motions requiring prediction such as jumping and standing up. We conducted empirical evaluations in simulation and also deployed our technique on the Unitree G1 humanoid robot. Using only 2.5 hours of motion capture data for training, our TeleGate achieves high-precision real-time teleoperation across diverse dynamic motions (e.g., running, fall recovery, and jumping), significantly outperforming the baseline methods in both tracking accuracy and success rate.

## 核心内容
Real-time whole-body teleoperation is a critical method for humanoid robots to perform complex tasks in unstructured environments. However, developing a unified controller that robustly supports diverse human motions remains a significant challenge. Existing methods typically distill multiple expert policies into a single general policy, which often inevitably leads to performance degradation, particularly on highly dynamic motions. This paper presents TeleGate, a unified whole-body teleoperation framework for humanoid robots that achieves high-precision tracking across various motions while avoiding the performance loss inherent in knowledge distillation. Our key idea is to preserve the full capability of domain-specific expert policies by training a lightweight gating network, which dynamically activates experts in real-time based on proprioceptive states and reference trajectories. Furthermore, to compensate for the absence of future reference trajectories in real-time teleoperation, we introduce a VAE-based motion prior module that extracts implicit future motion intent from historical observations, enabling anticipatory control for motions requiring prediction such as jumping and standing up. We conducted empirical evaluations in simulation and also deployed our technique on the Unitree G1 humanoid robot. Using only 2.5 hours of motion capture data for training, our TeleGate achieves high-precision real-time teleoperation across diverse dynamic motions (e.g., running, fall recovery, and jumping), significantly outperforming the baseline methods in both tracking accuracy and success rate.

## 参考
- http://arxiv.org/abs/2602.09628v2

## Overview
Real-time whole-body teleoperation is a critical method for humanoid robots to perform complex tasks in unstructured environments. However, developing a unified controller that robustly supports diverse human motions remains a significant challenge. Existing methods typically distill multiple expert policies into a single general policy, which often inevitably leads to performance degradation, particularly on highly dynamic motions. This paper presents TeleGate, a unified whole-body teleoperation framework for humanoid robots that achieves high-precision tracking across various motions while avoiding the performance loss inherent in knowledge distillation. Our key idea is to preserve the full capability of domain-specific expert policies by training a lightweight gating network, which dynamically activates experts in real-time based on proprioceptive states and reference trajectories. Furthermore, to compensate for the absence of future reference trajectories in real-time teleoperation, we introduce a VAE-based motion prior module that extracts implicit future motion intent from historical observations, enabling anticipatory control for motions requiring prediction such as jumping and standing up. We conducted empirical evaluations in simulation and also deployed our technique on the Unitree G1 humanoid robot. Using only 2.5 hours of motion capture data for training, our TeleGate achieves high-precision real-time teleoperation across diverse dynamic motions (e.g., running, fall recovery, and jumping), significantly outperforming the baseline methods in both tracking accuracy and success rate.

## Content
Real-time whole-body teleoperation is a critical method for humanoid robots to perform complex tasks in unstructured environments. However, developing a unified controller that robustly supports diverse human motions remains a significant challenge. Existing methods typically distill multiple expert policies into a single general policy, which often inevitably leads to performance degradation, particularly on highly dynamic motions. This paper presents TeleGate, a unified whole-body teleoperation framework for humanoid robots that achieves high-precision tracking across various motions while avoiding the performance loss inherent in knowledge distillation. Our key idea is to preserve the full capability of domain-specific expert policies by training a lightweight gating network, which dynamically activates experts in real-time based on proprioceptive states and reference trajectories. Furthermore, to compensate for the absence of future reference trajectories in real-time teleoperation, we introduce a VAE-based motion prior module that extracts implicit future motion intent from historical observations, enabling anticipatory control for motions requiring prediction such as jumping and standing up. We conducted empirical evaluations in simulation and also deployed our technique on the Unitree G1 humanoid robot. Using only 2.5 hours of motion capture data for training, our TeleGate achieves high-precision real-time teleoperation across diverse dynamic motions (e.g., running, fall recovery, and jumping), significantly outperforming the baseline methods in both tracking accuracy and success rate.

## 개요
실시간 전신 원격 조작은 인간형 로봇이 비정형 환경에서 복잡한 작업을 수행하기 위한 핵심 방법입니다. 그러나 다양한 인간 동작을 강건하게 지원하는 통합 제어기를 개발하는 것은 여전히 중요한 과제입니다. 기존 방법들은 일반적으로 여러 전문가 정책을 단일 일반 정책으로 증류하는데, 이는 특히 고동적 동작에서 성능 저하를 초래하는 경우가 많습니다. 본 논문은 지식 증류로 인한 성능 손실을 피하면서 다양한 동작에 걸쳐 고정밀 추적을 달성하는 인간형 로봇을 위한 통합 전신 원격 조작 프레임워크인 TeleGate를 제시합니다. 핵심 아이디어는 경량 게이팅 네트워크를 학습시켜 고유수용성 상태와 참조 궤적을 기반으로 실시간으로 전문가를 동적으로 활성화함으로써 도메인별 전문가 정책의 전체 성능을 보존하는 것입니다. 또한 실시간 원격 조작에서 미래 참조 궤적이 부재한 점을 보완하기 위해, VAE 기반 동작 사전 모듈을 도입하여 과거 관측에서 암시적 미래 동작 의도를 추출함으로써 점프나 기립과 같이 예측이 필요한 동작에 대한 예측 제어를 가능하게 합니다. 시뮬레이션에서 실증 평가를 수행하고 Unitree G1 인간형 로봇에 기술을 배포했습니다. 단 2.5시간의 모션 캡처 데이터로 학습한 TeleGate는 달리기, 낙상 회복, 점프 등 다양한 동적 동작에서 고정밀 실시간 원격 조작을 달성하며, 추적 정확도와 성공률 모두에서 기준 방법을 크게 능가합니다.

## 핵심 내용
실시간 전신 원격 조작은 인간형 로봇이 비정형 환경에서 복잡한 작업을 수행하기 위한 핵심 방법입니다. 그러나 다양한 인간 동작을 강건하게 지원하는 통합 제어기를 개발하는 것은 여전히 중요한 과제입니다. 기존 방법들은 일반적으로 여러 전문가 정책을 단일 일반 정책으로 증류하는데, 이는 특히 고동적 동작에서 성능 저하를 초래하는 경우가 많습니다. 본 논문은 지식 증류로 인한 성능 손실을 피하면서 다양한 동작에 걸쳐 고정밀 추적을 달성하는 인간형 로봇을 위한 통합 전신 원격 조작 프레임워크인 TeleGate를 제시합니다. 핵심 아이디어는 경량 게이팅 네트워크를 학습시켜 고유수용성 상태와 참조 궤적을 기반으로 실시간으로 전문가를 동적으로 활성화함으로써 도메인별 전문가 정책의 전체 성능을 보존하는 것입니다. 또한 실시간 원격 조작에서 미래 참조 궤적이 부재한 점을 보완하기 위해, VAE 기반 동작 사전 모듈을 도입하여 과거 관측에서 암시적 미래 동작 의도를 추출함으로써 점프나 기립과 같이 예측이 필요한 동작에 대한 예측 제어를 가능하게 합니다. 시뮬레이션에서 실증 평가를 수행하고 Unitree G1 인간형 로봇에 기술을 배포했습니다. 단 2.5시간의 모션 캡처 데이터로 학습한 TeleGate는 달리기, 낙상 회복, 점프 등 다양한 동적 동작에서 고정밀 실시간 원격 조작을 달성하며, 추적 정확도와 성공률 모두에서 기준 방법을 크게 능가합니다.
