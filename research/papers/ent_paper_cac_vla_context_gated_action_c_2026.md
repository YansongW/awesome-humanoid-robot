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
  zh: CAC-VLA 是一种面向视觉-语言-动作（VLA）模型的上下文门控动作条件框架，由研究团队提出。其核心贡献在于在视觉语言模型（VLM）内部学习轻量级潜在动作接口，通过预测从粗到细的潜在动作并利用上下文门控自适应调节其对动作专家的影响，从而提升机器人操作性能。在
    LIBERO 和 LIBERO-Plus 基准上分别达到 98.3% 和 89.5% 的平均成功率。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04816v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (645 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2607.04816
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
CAC-VLA 旨在解决 VLA 模型中视觉语言表示未针对动作条件进行显式优化的问题。现有方法通常引入额外模块生成显式动作计划，但需要独立的动作生成框架。CAC-VLA 直接在 VLM 内部学习轻量级潜在动作接口，通过预测从未来动作片段编码的粗到细潜在动作，并利用上下文门控自适应调节其对动作专家的影响，实现 VLM 原生的动作条件化。在 LIBERO 和 LIBERO-Plus 基准上的实验表明，该方法显著提升了连续动作控制的成功率。

## 核心内容
### 方法架构
CAC-VLA 的核心是**上下文门控动作条件框架**，其关键组件包括：
- **潜在动作接口**：在 VLM 内部学习轻量级表示，不生成可执行轨迹，而是预测从未来动作片段编码的粗到细潜在动作。
- **上下文门控机制**：自适应调节潜在动作指导对动作专家生成的影响，校准其作用强度。

### 实验设置
- **基准测试**：在 LIBERO 和 LIBERO-Plus 两个机器人操作基准上进行评估。
- **评价指标**：平均成功率（Average Success Rate）。

### 关键结果
- **LIBERO**：平均成功率达到 **98.3%**。
- **LIBERO-Plus**：平均成功率达到 **89.5%**。

### 结论
CAC-VLA 通过上下文门控的潜在动作条件化，为连续专家控制提供了有效接口，表明 VLM 原生动作条件化是提升 VLA 模型性能的可行方向。

## Overview
Vision-Language-Action (VLA) models have become a promising paradigm for generalist robot manipulation, where visual-language representations are used to condition continuous action generation. However, these representations are not explicitly optimized for action conditioning, leaving the action expert to bridge the gap between multimodal understanding and precise motor control. Recent action-reasoning methods introduce additional modules to generate explicit action plans or action-space reasoning signals, demonstrating the benefit of action-level guidance but often requiring separate action-generation frameworks. We propose CAC-VLA, a Context-Gated Action Conditioning framework that learns a lightweight latent-action interface directly within the VLM. Instead of generating executable trajectories, CAC-VLA trains the VLM to predict coarse-to-fine latent actions, which are structured representations encoded from future action segments, and adaptively leverages them to condition the action expert via a context gate. This enables VLM-native action conditioning while calibrating the influence of latent-action guidance on expert action generation. Experiments on LIBERO and LIBERO-Plus demonstrate the effectiveness of CAC-VLA, achieving 98.3% average success rate on LIBERO and 89.5% LIBERO-Plus, suggesting that context-gated latent-action conditioning is an effective interface for continuous expert control.

## 参考
- http://arxiv.org/abs/2607.04816v1

## 개요
CAC-VLA는 VLA 모델에서 시각-언어 표현이 동작 조건에 대해 명시적으로 최적화되지 않은 문제를 해결하는 것을 목표로 한다. 기존 방법들은 일반적으로 추가 모듈을 도입하여 명시적 동작 계획을 생성하지만, 독립적인 동작 생성 프레임워크가 필요하다. CAC-VLA는 VLM 내부에서 직접 경량 잠재 동작 인터페이스를 학습하여, 미래 동작 세그먼트에서 인코딩된 조대한-세밀한 잠재 동작을 예측하고, 컨텍스트 게이팅을 통해 동작 전문가에 대한 영향을 적응적으로 조절함으로써 VLM 고유의 동작 조건화를 실현한다. LIBERO 및 LIBERO-Plus 벤치마크에서의 실험은 이 방법이 연속 동작 제어의 성공률을 크게 향상시킨다는 것을 보여준다.

## 핵심 내용
### 방법 아키텍처
CAC-VLA의 핵심은 **컨텍스트 게이팅 동작 조건 프레임워크**이며, 주요 구성 요소는 다음과 같다:
- **잠재 동작 인터페이스**: VLM 내부에서 경량 표현을 학습하며, 실행 가능한 궤적을 생성하지 않고 미래 동작 세그먼트에서 인코딩된 조대한-세밀한 잠재 동작을 예측한다.
- **컨텍스트 게이팅 메커니즘**: 잠재 동작 지침이 동작 전문가 생성에 미치는 영향을 적응적으로 조절하여 그 작용 강도를 보정한다.

### 실험 설정
- **벤치마크 테스트**: LIBERO 및 LIBERO-Plus 두 로봇 조작 벤치마크에서 평가를 수행한다.
- **평가 지표**: 평균 성공률(Average Success Rate).

### 주요 결과
- **LIBERO**: 평균 성공률이 **98.3%**에 도달한다.
- **LIBERO-Plus**: 평균 성공률이 **89.5%**에 도달한다.

### 결론
CAC-VLA는 컨텍스트 게이팅 잠재 동작 조건화를 통해 연속 전문가 제어를 위한 효과적인 인터페이스를 제공하며, VLM 고유의 동작 조건화가 VLA 모델 성능을 향상시키는 실현 가능한 방향임을 보여준다.
