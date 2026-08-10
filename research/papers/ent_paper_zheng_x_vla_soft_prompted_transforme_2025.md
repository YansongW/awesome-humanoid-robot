---
$id: ent_paper_zheng_x_vla_soft_prompted_transforme_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model'
  zh: X-VLA
  ko: 'X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model'
summary:
  en: 'X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model (X-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for AI Industry Research (AIR), Tsinghua
    University, Shanghai AI Lab, Peking University.'
  zh: X-VLA 是清华大学 AIR、上海 AI Lab 和北京大学于 2025 年提出的大型视觉-语言-动作模型，专为跨实体机器人操作设计。其核心贡献在于引入软提示（Soft Prompt）方法，通过为每个数据源添加少量可学习嵌入，使标准
    Transformer 编码器能够高效利用异构跨实体数据。该模型在 6 个仿真环境和 3 个真实机器人上达到 SOTA 性能，0.9B 参数版本展现出从灵巧操作到快速适应多种实体、环境和任务的广泛能力。
  ko: 'X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model (X-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for AI Industry Research (AIR), Tsinghua
    University, Shanghai AI Lab, Peking University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
- x_vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10274v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (934 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2510.10274
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: X-VLA source
  url: https://doi.org/10.48550/arXiv.2510.10274
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
X-VLA 旨在解决通用视觉-语言-动作模型在跨实体异构数据集上的训练挑战。研究团队创新性地将提示学习概念融入机器人学习，为每个不同数据源引入独立的可学习嵌入集，作为实体特定的软提示。这些嵌入使模型能够统一利用多样的跨实体特征，而无需大幅增加参数。X-VLA 架构基于流匹配（flow-matching）和标准 Transformer 编码器，兼具可扩展性与简洁性。在 6 个仿真环境和 3 个真实机器人上的评估中，X-VLA-0.9B 在多个基准测试中取得领先结果，展现了从灵活灵巧操作到快速适应不同实体、环境和任务的广泛能力。

## 核心内容
### 方法
- **软提示（Soft Prompt）机制**：为每个数据源（如不同机器人平台或数据集）引入一组独立的可学习嵌入，作为实体特定的提示。这些嵌入在训练中与模型参数共同优化，使 Transformer 能够区分并利用来自不同来源的异构特征。
- **架构**：基于流匹配（flow-matching）的 VLA 架构，完全依赖软提示增强的标准 Transformer 编码器。这种设计避免了复杂的多模态融合模块，保持了模型的简洁性和可扩展性。

### 实验设置
- **训练数据**：使用大规模、跨实体、异构数据集，涵盖多种机器人平台和操作任务。
- **评估环境**：6 个仿真环境（具体名称未在正文中列出）和 3 个真实机器人平台。
- **模型规模**：主要评估 0.9B 参数版本（X-VLA-0.9B）。

### 关键结果
- **性能**：在多个基准测试中达到 SOTA 性能，优于现有跨实体 VLA 模型。
- **能力维度**：展现出灵活灵巧操作（flexible dexterity）和快速适应能力，能够跨不同实体、环境和任务进行迁移。
- **可扩展性**：软提示方法仅增加极少量参数，使模型能够高效利用异构数据，同时保持训练和推理的简洁性。

### 结论
X-VLA 通过软提示方法有效解决了跨实体机器人学习中的数据异构性问题，为构建通用、可扩展的 VLA 模型提供了新思路。其 0.9B 参数版本在仿真和真实场景中均验证了有效性，未来可进一步扩展至更多实体和任务。

## Overview
Successful generalist Vision-Language-Action (VLA) models rely on effective training across diverse robotic platforms with large-scale, cross-embodiment, heterogeneous datasets. To facilitate and leverage the heterogeneity in rich, diverse robotic data sources, we propose a novel Soft Prompt approach with minimally added parameters, by infusing prompt learning concepts into cross-embodiment robot learning and introducing separate sets of learnable embeddings for each distinct data source. These embeddings serve as embodiment-specific prompts, which in unity empower VLA models with effective exploitation of varying cross-embodiment features. Our new X-VLA, a neat flow-matching-based VLA architecture, relies exclusively on soft-prompted standard Transformer encoders, enjoying both scalability and simplicity. Evaluated across 6 simulations as well as 3 real-world robots, our 0.9B instantiation-X-VLA-0.9B simultaneously achieves SOTA performance over a sweep of benchmarks, demonstrating superior results on a wide axes of capabilities, from flexible dexterity to quick adaptation across embodiments, environments, and tasks. Website: https://thu-air-dream.github.io/X-VLA/

## 参考
- http://arxiv.org/abs/2510.10274v1

## 개요
X-VLA는 범용 비전-언어-행동 모델이 이기종 엔티티 데이터셋에서 훈련할 때 발생하는 과제를 해결하는 것을 목표로 합니다. 연구팀은 프롬프트 학습 개념을 로봇 학습에 혁신적으로 도입하여, 각 데이터 소스별로 독립적인 학습 가능한 임베딩 세트를 엔티티 특정 소프트 프롬프트로 제공합니다. 이러한 임베딩은 매개변수를 크게 늘리지 않고도 모델이 다양한 교차 엔티티 특징을 통합적으로 활용할 수 있게 합니다. X-VLA 아키텍처는 플로우 매칭(flow-matching)과 표준 Transformer 인코더를 기반으로 하며, 확장성과 간결성을 모두 갖추고 있습니다. 6개의 시뮬레이션 환경과 3개의 실제 로봇에서 평가한 결과, X-VLA-0.9B는 여러 벤치마크에서 선도적인 결과를 달성하여 유연한 정밀 조작부터 다양한 엔티티, 환경, 작업에 대한 빠른 적응까지 폭넓은 능력을 입증했습니다.

## 핵심 내용
### 방법
- **소프트 프롬프트(Soft Prompt) 메커니즘**: 각 데이터 소스(예: 서로 다른 로봇 플랫폼 또는 데이터셋)에 대해 독립적인 학습 가능한 임베딩 세트를 엔티티 특정 프롬프트로 도입합니다. 이러한 임베딩은 훈련 중 모델 매개변수와 함께 최적화되어 Transformer가 서로 다른 소스의 이기종 특징을 구별하고 활용할 수 있게 합니다.
- **아키텍처**: 플로우 매칭(flow-matching) 기반의 VLA 아키텍처로, 소프트 프롬프트로 강화된 표준 Transformer 인코더에 전적으로 의존합니다. 이 설계는 복잡한 다중 모달 융합 모듈을 피하면서 모델의 간결성과 확장성을 유지합니다.

### 실험 설정
- **훈련 데이터**: 여러 로봇 플랫폼과 조작 작업을 포괄하는 대규모, 교차 엔티티, 이기종 데이터셋을 사용합니다.
- **평가 환경**: 6개의 시뮬레이션 환경(구체적인 이름은 본문에 나열되지 않음)과 3개의 실제 로봇 플랫폼.
- **모델 규모**: 주로 0.9B 매개변수 버전(X-VLA-0.9B)을 평가합니다.

### 주요 결과
- **성능**: 여러 벤치마크에서 SOTA 성능을 달성하여 기존 교차 엔티티 VLA 모델보다 우수합니다.
- **능력 차원**: 유연한 정밀 조작(flexible dexterity)과 빠른 적응 능력을 보여주며, 서로 다른 엔티티, 환경, 작업 간 전이가 가능합니다.
- **확장성**: 소프트 프롬프트 방법은 극소량의 매개변수만 추가하므로 모델이 이기종 데이터를 효율적으로 활용하면서 훈련 및 추론의 간결성을 유지할 수 있습니다.

### 결론
X-VLA는 소프트 프롬프트 방법을 통해 교차 엔티티 로봇 학습에서의 데이터 이기종성 문제를 효과적으로 해결하여, 범용적이고 확장 가능한 VLA 모델 구축에 새로운 접근 방식을 제시합니다. 0.9B 매개변수 버전은 시뮬레이션과 실제 시나리오 모두에서 유효성을 검증했으며, 향후 더 많은 엔티티와 작업으로 확장할 수 있습니다.
