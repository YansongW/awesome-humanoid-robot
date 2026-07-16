---
$id: ent_paper_one_policy_but_many_worlds_a_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion'
  zh: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion'
  ko: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion'
summary:
  en: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- one_policy_but_many_worlds
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.18780v3.
sources:
- id: src_001
  type: paper
  title: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2505.18780
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Achieving versatile humanoid locomotion with a single policy presents a critical scalability challenge. Prevailing methods often rely on distilling multiple terrain-specific teacher policies into a unified student policy. However, while such distillation captures basic locomotion primitives, it struggles to organically compose these skills to adapt to complex environments, resulting in poor generalization to novel composite terrains unseen during training. To overcome this, we present DreamPolicy, a unified framework that integrates offline data with a diffusion-based world model, enabling a single policy to master both known and unseen terrains. Central to our approach is a terrain-aware world model, driven by an autoregressive diffusion world model trained on aggregated rollouts from specialized policies. This model synthesizes physically plausible future trajectories, which serve as dynamic objectives for a conditioned policy, thereby bypassing manual reward engineering. Unlike distillation, our world model captures generalizable locomotion skills, allowing for robust zero-shot transfer to unseen composite terrains. DreamPolicy naturally scales with data availability. As the offline dataset expands, the diffusion world model continuously acquires richer skills. Experiments demonstrate that DreamPolicy outperforms the strongest baseline by up to 27\% on unseen terrains and 38\% on combined terrains. By unifying world model-based planning and policy learning, DreamPolicy breaks the "one task, one policy" bottleneck and establishes a scalable, data-driven paradigm for generalist humanoid control.

## 核心内容
Achieving versatile humanoid locomotion with a single policy presents a critical scalability challenge. Prevailing methods often rely on distilling multiple terrain-specific teacher policies into a unified student policy. However, while such distillation captures basic locomotion primitives, it struggles to organically compose these skills to adapt to complex environments, resulting in poor generalization to novel composite terrains unseen during training. To overcome this, we present DreamPolicy, a unified framework that integrates offline data with a diffusion-based world model, enabling a single policy to master both known and unseen terrains. Central to our approach is a terrain-aware world model, driven by an autoregressive diffusion world model trained on aggregated rollouts from specialized policies. This model synthesizes physically plausible future trajectories, which serve as dynamic objectives for a conditioned policy, thereby bypassing manual reward engineering. Unlike distillation, our world model captures generalizable locomotion skills, allowing for robust zero-shot transfer to unseen composite terrains. DreamPolicy naturally scales with data availability. As the offline dataset expands, the diffusion world model continuously acquires richer skills. Experiments demonstrate that DreamPolicy outperforms the strongest baseline by up to 27\% on unseen terrains and 38\% on combined terrains. By unifying world model-based planning and policy learning, DreamPolicy breaks the "one task, one policy" bottleneck and establishes a scalable, data-driven paradigm for generalist humanoid control.

## 参考
- http://arxiv.org/abs/2505.18780v3

## Overview
Achieving versatile humanoid locomotion with a single policy presents a critical scalability challenge. Prevailing methods often rely on distilling multiple terrain-specific teacher policies into a unified student policy. However, while such distillation captures basic locomotion primitives, it struggles to organically compose these skills to adapt to complex environments, resulting in poor generalization to novel composite terrains unseen during training. To overcome this, we present DreamPolicy, a unified framework that integrates offline data with a diffusion-based world model, enabling a single policy to master both known and unseen terrains. Central to our approach is a terrain-aware world model, driven by an autoregressive diffusion world model trained on aggregated rollouts from specialized policies. This model synthesizes physically plausible future trajectories, which serve as dynamic objectives for a conditioned policy, thereby bypassing manual reward engineering. Unlike distillation, our world model captures generalizable locomotion skills, allowing for robust zero-shot transfer to unseen composite terrains. DreamPolicy naturally scales with data availability. As the offline dataset expands, the diffusion world model continuously acquires richer skills. Experiments demonstrate that DreamPolicy outperforms the strongest baseline by up to 27\% on unseen terrains and 38\% on combined terrains. By unifying world model-based planning and policy learning, DreamPolicy breaks the "one task, one policy" bottleneck and establishes a scalable, data-driven paradigm for generalist humanoid control.

## Content
Achieving versatile humanoid locomotion with a single policy presents a critical scalability challenge. Prevailing methods often rely on distilling multiple terrain-specific teacher policies into a unified student policy. However, while such distillation captures basic locomotion primitives, it struggles to organically compose these skills to adapt to complex environments, resulting in poor generalization to novel composite terrains unseen during training. To overcome this, we present DreamPolicy, a unified framework that integrates offline data with a diffusion-based world model, enabling a single policy to master both known and unseen terrains. Central to our approach is a terrain-aware world model, driven by an autoregressive diffusion world model trained on aggregated rollouts from specialized policies. This model synthesizes physically plausible future trajectories, which serve as dynamic objectives for a conditioned policy, thereby bypassing manual reward engineering. Unlike distillation, our world model captures generalizable locomotion skills, allowing for robust zero-shot transfer to unseen composite terrains. DreamPolicy naturally scales with data availability. As the offline dataset expands, the diffusion world model continuously acquires richer skills. Experiments demonstrate that DreamPolicy outperforms the strongest baseline by up to 27\% on unseen terrains and 38\% on combined terrains. By unifying world model-based planning and policy learning, DreamPolicy breaks the "one task, one policy" bottleneck and establishes a scalable, data-driven paradigm for generalist humanoid control.

## 개요
단일 정책으로 다재다능한 인간형 보행을 달성하는 것은 확장성 측면에서 중요한 도전 과제입니다. 기존 방법들은 종종 여러 지형 특화 교사 정책을 하나의 통합 학생 정책으로 증류(distillation)하는 데 의존합니다. 그러나 이러한 증류는 기본적인 보행 원시 동작을 포착하지만, 이러한 기술들을 유기적으로 조합하여 복잡한 환경에 적응하는 데 어려움을 겪어, 훈련 중 보지 못한 새로운 복합 지형에 대한 일반화 성능이 낮습니다. 이를 극복하기 위해 우리는 DreamPolicy를 제안합니다. 이는 오프라인 데이터와 확산 기반 세계 모델을 통합한 프레임워크로, 단일 정책이 알려진 지형과 보지 못한 지형 모두를 마스터할 수 있게 합니다. 우리 접근법의 핵심은 특화 정책의 집계된 롤아웃(rollout)으로 훈련된 자기회귀 확산 세계 모델에 기반한 지형 인식 세계 모델입니다. 이 모델은 물리적으로 타당한 미래 궤적을 합성하며, 이는 조건부 정책의 동적 목표 역할을 하여 수동 보상 엔지니어링을 우회합니다. 증류와 달리, 우리의 세계 모델은 일반화 가능한 보행 기술을 포착하여 보지 못한 복합 지형에 대한 강력한 제로샷 전이를 가능하게 합니다. DreamPolicy는 데이터 가용성에 따라 자연스럽게 확장됩니다. 오프라인 데이터셋이 확장됨에 따라 확산 세계 모델은 지속적으로 더 풍부한 기술을 습득합니다. 실험 결과, DreamPolicy는 보지 못한 지형에서 최대 27%, 복합 지형에서 38%까지 가장 강력한 기준선을 능가합니다. 세계 모델 기반 계획과 정책 학습을 통합함으로써, DreamPolicy는 "하나의 작업, 하나의 정책" 병목 현상을 깨고 범용 인간형 제어를 위한 확장 가능한 데이터 기반 패러다임을 구축합니다.

## 핵심 내용
단일 정책으로 다재다능한 인간형 보행을 달성하는 것은 확장성 측면에서 중요한 도전 과제입니다. 기존 방법들은 종종 여러 지형 특화 교사 정책을 하나의 통합 학생 정책으로 증류하는 데 의존합니다. 그러나 이러한 증류는 기본적인 보행 원시 동작을 포착하지만, 이러한 기술들을 유기적으로 조합하여 복잡한 환경에 적응하는 데 어려움을 겪어, 훈련 중 보지 못한 새로운 복합 지형에 대한 일반화 성능이 낮습니다. 이를 극복하기 위해 우리는 DreamPolicy를 제안합니다. 이는 오프라인 데이터와 확산 기반 세계 모델을 통합한 프레임워크로, 단일 정책이 알려진 지형과 보지 못한 지형 모두를 마스터할 수 있게 합니다. 우리 접근법의 핵심은 특화 정책의 집계된 롤아웃으로 훈련된 자기회귀 확산 세계 모델에 기반한 지형 인식 세계 모델입니다. 이 모델은 물리적으로 타당한 미래 궤적을 합성하며, 이는 조건부 정책의 동적 목표 역할을 하여 수동 보상 엔지니어링을 우회합니다. 증류와 달리, 우리의 세계 모델은 일반화 가능한 보행 기술을 포착하여 보지 못한 복합 지형에 대한 강력한 제로샷 전이를 가능하게 합니다. DreamPolicy는 데이터 가용성에 따라 자연스럽게 확장됩니다. 오프라인 데이터셋이 확장됨에 따라 확산 세계 모델은 지속적으로 더 풍부한 기술을 습득합니다. 실험 결과, DreamPolicy는 보지 못한 지형에서 최대 27%, 복합 지형에서 38%까지 가장 강력한 기준선을 능가합니다. 세계 모델 기반 계획과 정책 학습을 통합함으로써, DreamPolicy는 "하나의 작업, 하나의 정책" 병목 현상을 깨고 범용 인간형 제어를 위한 확장 가능한 데이터 기반 패러다임을 구축합니다.
