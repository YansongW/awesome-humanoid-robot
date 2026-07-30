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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10274v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
성공적인 범용 Vision-Language-Action(VLA) 모델은 다양한 로봇 플랫폼에서 대규모, 교차-임보디먼트, 이종 데이터셋을 활용한 효과적인 훈련에 의존합니다. 풍부하고 다양한 로봇 데이터 소스의 이질성을 활용하고 촉진하기 위해, 우리는 프롬프트 학습 개념을 교차-임보디먼트 로봇 학습에 주입하고 각각의 고유한 데이터 소스에 대해 별도의 학습 가능한 임베딩 세트를 도입하여 최소한의 추가 파라미터로 새로운 소프트 프롬프트 접근법을 제안합니다. 이러한 임베딩은 임보디먼트별 프롬프트 역할을 하며, 통합되어 VLA 모델이 다양한 교차-임보디먼트 특징을 효과적으로 활용할 수 있게 합니다. 우리의 새로운 X-VLA는 깔끔한 flow-matching 기반 VLA 아키텍처로, 소프트 프롬프트된 표준 Transformer 인코더에만 의존하여 확장성과 단순성을 모두 갖추고 있습니다. 6개의 시뮬레이션과 3개의 실제 로봇에서 평가된 우리의 0.9B 인스턴스인 X-VLA-0.9B는 다양한 벤치마크에서 동시에 최고 성능(SOTA)을 달성하며, 유연한 손재주부터 임보디먼트, 환경, 작업 전반에 걸친 빠른 적응에 이르기까지 광범위한 능력 축에서 뛰어난 결과를 보여줍니다. 웹사이트: https://thu-air-dream.github.io/X-VLA/

## 핵심 내용
성공적인 범용 Vision-Language-Action(VLA) 모델은 다양한 로봇 플랫폼에서 대규모, 교차-임보디먼트, 이종 데이터셋을 활용한 효과적인 훈련에 의존합니다. 풍부하고 다양한 로봇 데이터 소스의 이질성을 활용하고 촉진하기 위해, 우리는 프롬프트 학습 개념을 교차-임보디먼트 로봇 학습에 주입하고 각각의 고유한 데이터 소스에 대해 별도의 학습 가능한 임베딩 세트를 도입하여 최소한의 추가 파라미터로 새로운 소프트 프롬프트 접근법을 제안합니다. 이러한 임베딩은 임보디먼트별 프롬프트 역할을 하며, 통합되어 VLA 모델이 다양한 교차-임보디먼트 특징을 효과적으로 활용할 수 있게 합니다. 우리의 새로운 X-VLA는 깔끔한 flow-matching 기반 VLA 아키텍처로, 소프트 프롬프트된 표준 Transformer 인코더에만 의존하여 확장성과 단순성을 모두 갖추고 있습니다. 6개의 시뮬레이션과 3개의 실제 로봇에서 평가된 우리의 0.9B 인스턴스인 X-VLA-0.9B는 다양한 벤치마크에서 동시에 최고 성능(SOTA)을 달성하며, 유연한 손재주부터 임보디먼트, 환경, 작업 전반에 걸친 빠른 적응에 이르기까지 광범위한 능력 축에서 뛰어난 결과를 보여줍니다. 웹사이트: https://thu-air-dream.github.io/X-VLA/

## 参考
- http://arxiv.org/abs/2510.10274v1
