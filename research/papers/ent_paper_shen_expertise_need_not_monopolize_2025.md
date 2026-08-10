---
$id: ent_paper_shen_expertise_need_not_monopolize_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning'
  zh: AdaMoE
  ko: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning'
summary:
  en: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning (AdaMoE),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tsinghua
    University, The University of Hong Kong, Tongji University, D-Robotics, Key Laboratory of System Control and Information
    Processing, Shanghai Key Laboratory of Integrated Administration Technologies for Information Security.'
  zh: AdaMoE 是上海交通大学、清华大学、香港大学、同济大学、D-Robotics 等机构于 2025 年提出的视觉-语言-动作模型，通过混合专家架构在继承预训练权重的基础上扩展动作专家。其核心创新在于解耦专家选择与权重分配，实现专家协作而非垄断，在
    LIBERO 和 RoboTwin 基准上分别提升 1.8% 和 9.3%，真实实验性能提升 21.5%。
  ko: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning (AdaMoE),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Tsinghua
    University, The University of Hong Kong, Tongji University, D-Robotics, Key Laboratory of System Control and Information
    Processing, Shanghai Key Laboratory of Integrated Administration Technologies for Information Security.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- adamoe
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.14300v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (714 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning (arXiv)'
  url: https://arxiv.org/abs/2510.14300
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AdaMoE source
  url: https://doi.org/10.48550/arXiv.2510.14300
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
AdaMoE 针对视觉-语言-动作模型扩展中的两大挑战：计算资源需求大与实时控制效率平衡，提出了一种混合专家架构。该架构继承密集 VLA 模型的预训练权重，将前馈层替换为稀疏激活的 MoE 层以扩展动作专家。通过独立尺度适配器与传统路由器协同工作，AdaMoE 实现了专家选择与权重分配的解耦，使专家基于任务相关性被选择并以独立权重贡献，形成协作而非赢家通吃的动态机制。实验表明，该方法在保持计算效率的同时显著提升性能，尤其在真实机器人操作任务中表现突出。

## 核心内容
### 方法架构
- **核心挑战**：VLA 模型扩展面临两大问题：从头训练新模型需大量计算资源和数据集，而机器人数据稀缺；实时控制需平衡模型容量与计算效率。
- **AdaMoE 设计**：采用混合专家架构，继承密集 VLA 模型的预训练权重，通过将前馈层替换为稀疏激活的 MoE 层来扩展动作专家。
- **解耦技术**：引入独立尺度适配器与传统路由器协同工作，实现专家选择与权重分配的解耦。专家基于任务相关性被选择，并以独立控制的权重贡献，形成协作利用模式，避免赢家通吃。

### 实验设置与结果
- **基准测试**：在 LIBERO 基准上性能提升 1.8%，在 RoboTwin 基准上提升 9.3%。
- **真实实验**：在真实机器人操作任务中，性能提升达 21.5%，验证了其实际有效性。
- **效率优势**：通过稀疏激活机制，在扩展模型容量的同时保持计算效率，满足实时控制需求。

### 结论
AdaMoE 证明了专家无需垄断，通过协作利用可在保持计算效率的同时实现更优性能，为 VLA 模型扩展提供了有效方案。

## Overview
Vision-Language-Action (VLA) models are experiencing rapid development and demonstrating promising capabilities in robotic manipulation tasks. However, scaling up VLA models presents several critical challenges: (1) Training new VLA models from scratch demands substantial computational resources and extensive datasets. Given the current scarcity of robot data, it becomes particularly valuable to fully leverage well-pretrained VLA model weights during the scaling process. (2) Real-time control requires carefully balancing model capacity with computational efficiency. To address these challenges, We propose AdaMoE, a Mixture-of-Experts (MoE) architecture that inherits pretrained weights from dense VLA models, and scales up the action expert by substituting the feedforward layers into sparsely activated MoE layers. AdaMoE employs a decoupling technique that decouples expert selection from expert weighting through an independent scale adapter working alongside the traditional router. This enables experts to be selected based on task relevance while contributing with independently controlled weights, allowing collaborative expert utilization rather than winner-takes-all dynamics. Our approach demonstrates that expertise need not monopolize. Instead, through collaborative expert utilization, we can achieve superior performance while maintaining computational efficiency. AdaMoE consistently outperforms the baseline model across key benchmarks, delivering performance gains of 1.8% on LIBERO and 9.3% on RoboTwin. Most importantly, a substantial 21.5% improvement in real-world experiments validates its practical effectiveness for robotic manipulation tasks.

## 参考
- http://arxiv.org/abs/2510.14300v1

## 개요
AdaMoE는 시각-언어-행동 모델 확장에서의 두 가지 주요 과제, 즉 대규모 계산 자원 요구와 실시간 제어 효율성의 균형 문제를 해결하기 위해 혼합 전문가 아키텍처를 제안한다. 이 아키텍처는 밀집 VLA 모델의 사전 훈련 가중치를 계승하며, 피드포워드 계층을 희소 활성화 MoE 계층으로 대체하여 행동 전문가를 확장한다. 독립 스케일 어댑터와 전통적인 라우터가 협력하여 작동함으로써, AdaMoE는 전문가 선택과 가중치 할당의 분리를 실현하며, 전문가가 작업 관련성에 따라 선택되고 독립적인 가중치로 기여하여 승자 독식이 아닌 협력적 동적 메커니즘을 형성한다. 실험 결과, 이 방법은 계산 효율성을 유지하면서 성능을 크게 향상시키며, 특히 실제 로봇 조작 작업에서 두드러진 성과를 보인다.

## 핵심 내용
### 방법 아키텍처
- **핵심 과제**: VLA 모델 확장은 두 가지 주요 문제에 직면한다. 새 모델을 처음부터 훈련하려면 대규모 계산 자원과 데이터셋이 필요하며, 로봇 데이터는 희소하다. 또한 실시간 제어는 모델 용량과 계산 효율성의 균형을 요구한다.
- **AdaMoE 설계**: 혼합 전문가 아키텍처를 채택하여 밀집 VLA 모델의 사전 훈련 가중치를 계승하고, 피드포워드 계층을 희소 활성화 MoE 계층으로 대체하여 행동 전문가를 확장한다.
- **분리 기술**: 독립 스케일 어댑터와 전통적인 라우터가 협력하여 전문가 선택과 가중치 할당의 분리를 실현한다. 전문가는 작업 관련성에 따라 선택되며, 독립적으로 제어되는 가중치로 기여하여 승자 독식이 아닌 협력적 활용 패턴을 형성한다.

### 실험 설정 및 결과
- **벤치마크 테스트**: LIBERO 벤치마크에서 성능이 1.8% 향상되었고, RoboTwin 벤치마크에서 9.3% 향상되었다.
- **실제 실험**: 실제 로봇 조작 작업에서 성능이 21.5% 향상되어 실제 유효성을 검증했다.
- **효율성 이점**: 희소 활성화 메커니즘을 통해 모델 용량을 확장하면서도 계산 효율성을 유지하여 실시간 제어 요구를 충족한다.

### 결론
AdaMoE는 전문가가 독점할 필요 없이 협력적 활용을 통해 계산 효율성을 유지하면서 더 나은 성능을 달성할 수 있음을 입증하며, VLA 모델 확장을 위한 효과적인 솔루션을 제공한다.
