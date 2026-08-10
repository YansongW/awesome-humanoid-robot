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
  zh: DreamPolicy 是2025年提出的一种面向人形机器人行走的统一框架，由研究团队开发。其核心贡献在于利用扩散世界模型整合离线数据，使单一策略能同时适应已知与未知地形，无需手工设计奖励函数。在未见地形上性能提升最高达27%，组合地形上达38%。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.18780v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (763 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2505.18780
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有方法通常通过蒸馏多个地形专用教师策略来训练统一学生策略，但这种方式难以有机组合基础运动技能以应对复杂环境，导致对训练中未见过的新型组合地形泛化能力差。DreamPolicy 通过引入基于自回归扩散的世界模型，从专用策略的聚合轨迹中学习物理可行的未来轨迹，并将其作为条件策略的动态目标。该方法无需人工奖励工程，且能随离线数据规模扩大而持续提升技能多样性，实现了对未见组合地形的零样本迁移。

## 核心内容
### 方法架构
- **核心挑战**：传统蒸馏方法将多个地形专用教师策略压缩为统一学生策略，但无法有机组合基础运动原语，导致对训练中未见的复合地形泛化能力差。
- **DreamPolicy 框架**：由两个关键组件构成：
  - **地形感知世界模型**：基于自回归扩散模型，在专用策略的聚合轨迹上训练，能合成物理合理的未来轨迹。
  - **条件策略**：以世界模型生成的动态目标为输入，直接输出动作，完全绕过手工奖励函数设计。
- **数据扩展性**：离线数据集规模扩大时，扩散世界模型持续获取更丰富的技能，使策略自然具备可扩展性。

### 实验设置与结果
- **基准对比**：在未见地形上，DreamPolicy 超越最强基线方法达27%；在组合地形上，性能提升达38%。
- **零样本迁移**：无需针对新地形重新训练，直接泛化到训练中未出现的复合地形。
- **关键优势**：相比蒸馏方法，世界模型捕获了可泛化的运动技能，而非仅记忆特定地形模式。

### 结论
DreamPolicy 通过统一基于世界模型的规划与策略学习，打破了“一个任务一个策略”的瓶颈，建立了可扩展的数据驱动通用人形控制范式。其核心创新在于用扩散世界模型替代手工奖励工程，并实现数据规模与技能多样性的正相关增长。

## Overview
Achieving versatile humanoid locomotion with a single policy presents a critical scalability challenge. Prevailing methods often rely on distilling multiple terrain-specific teacher policies into a unified student policy. However, while such distillation captures basic locomotion primitives, it struggles to organically compose these skills to adapt to complex environments, resulting in poor generalization to novel composite terrains unseen during training. To overcome this, we present DreamPolicy, a unified framework that integrates offline data with a diffusion-based world model, enabling a single policy to master both known and unseen terrains. Central to our approach is a terrain-aware world model, driven by an autoregressive diffusion world model trained on aggregated rollouts from specialized policies. This model synthesizes physically plausible future trajectories, which serve as dynamic objectives for a conditioned policy, thereby bypassing manual reward engineering. Unlike distillation, our world model captures generalizable locomotion skills, allowing for robust zero-shot transfer to unseen composite terrains. DreamPolicy naturally scales with data availability. As the offline dataset expands, the diffusion world model continuously acquires richer skills. Experiments demonstrate that DreamPolicy outperforms the strongest baseline by up to 27\% on unseen terrains and 38\% on combined terrains. By unifying world model-based planning and policy learning, DreamPolicy breaks the "one task, one policy" bottleneck and establishes a scalable, data-driven paradigm for generalist humanoid control.

## 参考
- http://arxiv.org/abs/2505.18780v3

## 개요
기존 방법들은 일반적으로 여러 지형 전용 교사 정책을 증류하여 통합 학생 정책을 훈련하지만, 이러한 방식은 복잡한 환경에 대처하기 위해 기본 운동 기술을 유기적으로 결합하기 어렵고, 훈련 중 보지 못한 새로운 조합 지형에 대한 일반화 성능이 낮다. DreamPolicy는 자기회귀 확산 기반 세계 모델을 도입하여 전용 정책의 집계 궤적으로부터 물리적으로 실현 가능한 미래 궤적을 학습하고, 이를 조건부 정책의 동적 목표로 사용한다. 이 방법은 수동 보상 엔지니어링이 필요 없으며, 오프라인 데이터 규모가 확장됨에 따라 기술 다양성을 지속적으로 향상시켜 보지 못한 조합 지형에 대한 제로샷 전이를 구현한다.

## 핵심 내용
### 방법 구조
- **핵심 과제**: 기존 증류 방법은 여러 지형 전용 교사 정책을 통합 학생 정책으로 압축하지만, 기본 운동 원시 요소를 유기적으로 결합하지 못하여 훈련 중 보지 못한 복합 지형에 대한 일반화 성능이 낮다.
- **DreamPolicy 프레임워크**: 두 가지 핵심 구성 요소로 이루어짐:
  - **지형 인식 세계 모델**: 자기회귀 확산 모델 기반으로, 전용 정책의 집계 궤적에서 훈련되어 물리적으로 타당한 미래 궤적을 합성할 수 있다.
  - **조건부 정책**: 세계 모델이 생성한 동적 목표를 입력으로 받아 직접 행동을 출력하며, 수동 보상 함수 설계를 완전히 우회한다.
- **데이터 확장성**: 오프라인 데이터 세트 규모가 확장됨에 따라 확산 세계 모델은 더 풍부한 기술을 지속적으로 획득하여 정책이 자연스럽게 확장 가능성을 갖게 된다.

### 실험 설정 및 결과
- **기준 비교**: 보지 못한 지형에서 DreamPolicy는 가장 강력한 기준선 방법보다 27% 우수하며, 조합 지형에서는 성능이 38% 향상된다.
- **제로샷 전이**: 새로운 지형에 대해 재훈련 없이 훈련 중 나타나지 않은 복합 지형에 직접 일반화된다.
- **핵심 장점**: 증류 방법과 비교하여 세계 모델은 일반화 가능한 운동 기술을 포착하며, 특정 지형 패턴만 기억하는 것이 아니다.

### 결론
DreamPolicy는 세계 모델 기반 계획과 정책 학습을 통합하여 '하나의 작업에 하나의 정책'이라는 병목을 깨고, 확장 가능한 데이터 기반 범용 휴머노이드 제어 패러다임을 확립한다. 핵심 혁신은 수동 보상 엔지니어링을 확산 세계 모델로 대체하고, 데이터 규모와 기술 다양성의 정적 상관 성장을 구현한 것이다.
