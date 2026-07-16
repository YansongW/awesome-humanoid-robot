---
$id: ent_paper_cac_vla_context_gated_action_c_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models'
  zh: 'CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models'
  ko: 'CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models'
summary:
  en: 'arXiv:2607.04816v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have become a promising paradigm
    for generalist robot manipulation, where visual-language representations are used to condition continuous action generation.
    However, these representations are not explicitly optimized for action conditioning, leaving the action expert to bridge
    the gap between multimodal understanding and precise motor control. Recent action-reasoning methods introduce additional
    modules to generate explicit action plans or action-space reasoning signals, demonstrating the benefit of action-level
    guidance but often requiring separate action-generation frameworks. We propose CAC-VLA, a Context-Gated Action Conditioning
    framework that learns a lightweight latent-action interface directly within the VLM. Instead of generating executable
    trajectories, CAC-VLA trains the VLM to predict coarse-to-fine latent actions, which are structured representations encoded
    from future action segments, and adaptively leverages them to condition the action expert via a context gate. This enables
    VLM-native action conditioning while calibrating the influence of latent-action guidance on expert action generation.
    Experiments on LIBERO and LIBERO-Plus demonstrate the effectiveness of CAC-VLA, achieving 98.3% average success rate on
    LIBERO and 89.5% LIBERO-Plus, suggesting that context-gated latent-action conditioning is an effective interface for continuous
    expert control.'
  zh: 'arXiv:2607.04816v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have become a promising paradigm
    for generalist robot manipulation, where visual-language representations are used to condition continuous action generation.
    However, these representations are not explicitly optimized for action conditioning, leaving the action expert to bridge
    the gap between multimodal understanding and precise motor control. Recent action-reasoning methods introduce additional
    modules to generate explicit action plans or action-space reasoning signals, demonstrating the benefit of action-level
    guidance but often requiring separate action-generation frameworks. We propose CAC-VLA, a Context-Gated Action Conditioning
    framework that learns a lightweight latent-action interface directly within the VLM. Instead of generating executable
    trajectories, CAC-VLA trains the VLM to predict coarse-to-fine latent actions, which are structured representations encoded
    from future action segments, and adaptively leverages them to condition the action expert via a context gate. This enables
    VLM-native action conditioning while calibrating the influence of latent-action guidance on expert action generation.
    Experiments on LIBERO and LIBERO-Plus demonstrate the effectiveness of CAC-VLA, achieving 98.3% average success rate on
    LIBERO and 89.5% LIBERO-Plus, suggesting that context-gated latent-action conditioning is an effective interface for continuous
    expert control.'
  ko: 'arXiv:2607.04816v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have become a promising paradigm
    for generalist robot manipulation, where visual-language representations are used to condition continuous action generation.
    However, these representations are not explicitly optimized for action conditioning, leaving the action expert to bridge
    the gap between multimodal understanding and precise motor control. Recent action-reasoning methods introduce additional
    modules to generate explicit action plans or action-space reasoning signals, demonstrating the benefit of action-level
    guidance but often requiring separate action-generation frameworks. We propose CAC-VLA, a Context-Gated Action Conditioning
    framework that learns a lightweight latent-action interface directly within the VLM. Instead of generating executable
    trajectories, CAC-VLA trains the VLM to predict coarse-to-fine latent actions, which are structured representations encoded
    from future action segments, and adaptively leverages them to condition the action expert via a context gate. This enables
    VLM-native action conditioning while calibrating the influence of latent-action guidance on expert action generation.
    Experiments on LIBERO and LIBERO-Plus demonstrate the effectiveness of CAC-VLA, achieving 98.3% average success rate on
    LIBERO and 89.5% LIBERO-Plus, suggesting that context-gated latent-action conditioning is an effective interface for continuous
    expert control.'
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
- robotics
- cac_vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04816v1.
sources:
- id: src_001
  type: paper
  title: 'CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2607.04816
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Vision-Language-Action (VLA) models have become a promising paradigm for generalist robot manipulation, where visual-language representations are used to condition continuous action generation. However, these representations are not explicitly optimized for action conditioning, leaving the action expert to bridge the gap between multimodal understanding and precise motor control. Recent action-reasoning methods introduce additional modules to generate explicit action plans or action-space reasoning signals, demonstrating the benefit of action-level guidance but often requiring separate action-generation frameworks. We propose CAC-VLA, a Context-Gated Action Conditioning framework that learns a lightweight latent-action interface directly within the VLM. Instead of generating executable trajectories, CAC-VLA trains the VLM to predict coarse-to-fine latent actions, which are structured representations encoded from future action segments, and adaptively leverages them to condition the action expert via a context gate. This enables VLM-native action conditioning while calibrating the influence of latent-action guidance on expert action generation. Experiments on LIBERO and LIBERO-Plus demonstrate the effectiveness of CAC-VLA, achieving 98.3% average success rate on LIBERO and 89.5% LIBERO-Plus, suggesting that context-gated latent-action conditioning is an effective interface for continuous expert control.

## 核心内容
Vision-Language-Action (VLA) models have become a promising paradigm for generalist robot manipulation, where visual-language representations are used to condition continuous action generation. However, these representations are not explicitly optimized for action conditioning, leaving the action expert to bridge the gap between multimodal understanding and precise motor control. Recent action-reasoning methods introduce additional modules to generate explicit action plans or action-space reasoning signals, demonstrating the benefit of action-level guidance but often requiring separate action-generation frameworks. We propose CAC-VLA, a Context-Gated Action Conditioning framework that learns a lightweight latent-action interface directly within the VLM. Instead of generating executable trajectories, CAC-VLA trains the VLM to predict coarse-to-fine latent actions, which are structured representations encoded from future action segments, and adaptively leverages them to condition the action expert via a context gate. This enables VLM-native action conditioning while calibrating the influence of latent-action guidance on expert action generation. Experiments on LIBERO and LIBERO-Plus demonstrate the effectiveness of CAC-VLA, achieving 98.3% average success rate on LIBERO and 89.5% LIBERO-Plus, suggesting that context-gated latent-action conditioning is an effective interface for continuous expert control.

## 参考
- http://arxiv.org/abs/2607.04816v1

## Overview
Vision-Language-Action (VLA) models have become a promising paradigm for generalist robot manipulation, where visual-language representations are used to condition continuous action generation. However, these representations are not explicitly optimized for action conditioning, leaving the action expert to bridge the gap between multimodal understanding and precise motor control. Recent action-reasoning methods introduce additional modules to generate explicit action plans or action-space reasoning signals, demonstrating the benefit of action-level guidance but often requiring separate action-generation frameworks. We propose CAC-VLA, a Context-Gated Action Conditioning framework that learns a lightweight latent-action interface directly within the VLM. Instead of generating executable trajectories, CAC-VLA trains the VLM to predict coarse-to-fine latent actions, which are structured representations encoded from future action segments, and adaptively leverages them to condition the action expert via a context gate. This enables VLM-native action conditioning while calibrating the influence of latent-action guidance on expert action generation. Experiments on LIBERO and LIBERO-Plus demonstrate the effectiveness of CAC-VLA, achieving 98.3% average success rate on LIBERO and 89.5% LIBERO-Plus, suggesting that context-gated latent-action conditioning is an effective interface for continuous expert control.

## Content
Vision-Language-Action (VLA) models have become a promising paradigm for generalist robot manipulation, where visual-language representations are used to condition continuous action generation. However, these representations are not explicitly optimized for action conditioning, leaving the action expert to bridge the gap between multimodal understanding and precise motor control. Recent action-reasoning methods introduce additional modules to generate explicit action plans or action-space reasoning signals, demonstrating the benefit of action-level guidance but often requiring separate action-generation frameworks. We propose CAC-VLA, a Context-Gated Action Conditioning framework that learns a lightweight latent-action interface directly within the VLM. Instead of generating executable trajectories, CAC-VLA trains the VLM to predict coarse-to-fine latent actions, which are structured representations encoded from future action segments, and adaptively leverages them to condition the action expert via a context gate. This enables VLM-native action conditioning while calibrating the influence of latent-action guidance on expert action generation. Experiments on LIBERO and LIBERO-Plus demonstrate the effectiveness of CAC-VLA, achieving 98.3% average success rate on LIBERO and 89.5% LIBERO-Plus, suggesting that context-gated latent-action conditioning is an effective interface for continuous expert control.

## 개요
Vision-Language-Action (VLA) 모델은 일반화된 로봇 조작을 위한 유망한 패러다임으로 자리 잡았으며, 시각-언어 표현을 사용하여 연속적인 행동 생성을 조건화합니다. 그러나 이러한 표현은 행동 조건화를 위해 명시적으로 최적화되지 않아, 행동 전문가가 다중 모드 이해와 정밀한 모터 제어 사이의 간극을 메워야 합니다. 최근의 행동 추론 방법은 추가 모듈을 도입하여 명시적인 행동 계획이나 행동 공간 추론 신호를 생성하며, 행동 수준의 지침의 이점을 보여주지만 종종 별도의 행동 생성 프레임워크가 필요합니다. 우리는 CAC-VLA, 즉 컨텍스트 게이트 행동 조건화 프레임워크를 제안하며, 이는 VLM 내에서 직접 경량의 잠재 행동 인터페이스를 학습합니다. 실행 가능한 궤적을 생성하는 대신, CAC-VLA는 VLM이 미래 행동 세그먼트에서 인코딩된 구조화된 표현인 거칠고 세밀한 잠재 행동을 예측하도록 훈련하고, 컨텍스트 게이트를 통해 이를 적응적으로 활용하여 행동 전문가를 조건화합니다. 이를 통해 VLM 고유의 행동 조건화를 가능하게 하면서, 잠재 행동 지침이 전문가 행동 생성에 미치는 영향을 조정합니다. LIBERO 및 LIBERO-Plus에서의 실험은 CAC-VLA의 효과성을 입증하며, LIBERO에서 98.3%, LIBERO-Plus에서 89.5%의 평균 성공률을 달성하여, 컨텍스트 게이트 잠재 행동 조건화가 연속적인 전문가 제어를 위한 효과적인 인터페이스임을 시사합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 일반화된 로봇 조작을 위한 유망한 패러다임으로 자리 잡았으며, 시각-언어 표현을 사용하여 연속적인 행동 생성을 조건화합니다. 그러나 이러한 표현은 행동 조건화를 위해 명시적으로 최적화되지 않아, 행동 전문가가 다중 모드 이해와 정밀한 모터 제어 사이의 간극을 메워야 합니다. 최근의 행동 추론 방법은 추가 모듈을 도입하여 명시적인 행동 계획이나 행동 공간 추론 신호를 생성하며, 행동 수준의 지침의 이점을 보여주지만 종종 별도의 행동 생성 프레임워크가 필요합니다. 우리는 CAC-VLA, 즉 컨텍스트 게이트 행동 조건화 프레임워크를 제안하며, 이는 VLM 내에서 직접 경량의 잠재 행동 인터페이스를 학습합니다. 실행 가능한 궤적을 생성하는 대신, CAC-VLA는 VLM이 미래 행동 세그먼트에서 인코딩된 구조화된 표현인 거칠고 세밀한 잠재 행동을 예측하도록 훈련하고, 컨텍스트 게이트를 통해 이를 적응적으로 활용하여 행동 전문가를 조건화합니다. 이를 통해 VLM 고유의 행동 조건화를 가능하게 하면서, 잠재 행동 지침이 전문가 행동 생성에 미치는 영향을 조정합니다. LIBERO 및 LIBERO-Plus에서의 실험은 CAC-VLA의 효과성을 입증하며, LIBERO에서 98.3%, LIBERO-Plus에서 89.5%의 평균 성공률을 달성하여, 컨텍스트 게이트 잠재 행동 조건화가 연속적인 전문가 제어를 위한 효과적인 인터페이스임을 시사합니다.
