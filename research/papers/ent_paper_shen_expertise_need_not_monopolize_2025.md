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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.14300v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Vision-Language-Action (VLA) 모델은 빠르게 발전하며 로봇 조작 작업에서 유망한 성능을 보여주고 있습니다. 그러나 VLA 모델의 확장은 몇 가지 중요한 도전 과제를 제기합니다: (1) 새로운 VLA 모델을 처음부터 훈련하려면 상당한 계산 자원과 방대한 데이터셋이 필요합니다. 현재 로봇 데이터가 부족한 상황에서, 확장 과정에서 잘 사전 훈련된 VLA 모델 가중치를 완전히 활용하는 것이 특히 중요합니다. (2) 실시간 제어는 모델 용량과 계산 효율성 사이의 신중한 균형을 요구합니다. 이러한 도전 과제를 해결하기 위해, 우리는 AdaMoE를 제안합니다. 이는 밀집 VLA 모델의 사전 훈련 가중치를 상속받고, 피드포워드 레이어를 희소 활성화된 MoE 레이어로 대체하여 액션 전문가를 확장하는 Mixture-of-Experts (MoE) 아키텍처입니다. AdaMoE는 전통적인 라우터와 함께 작동하는 독립적인 스케일 어댑터를 통해 전문가 선택과 전문가 가중치를 분리하는 분리 기술을 사용합니다. 이를 통해 작업 관련성에 따라 전문가를 선택하면서 독립적으로 제어된 가중치로 기여할 수 있어, 승자 독식 동역학이 아닌 협력적 전문가 활용이 가능합니다. 우리의 접근 방식은 전문성이 독점될 필요가 없음을 보여줍니다. 대신, 협력적 전문가 활용을 통해 계산 효율성을 유지하면서 우수한 성능을 달성할 수 있습니다. AdaMoE는 주요 벤치마크에서 기준 모델을 일관되게 능가하며, LIBERO에서 1.8%, RoboTwin에서 9.3%의 성능 향상을 제공합니다. 가장 중요한 것은 실제 실험에서 21.5%의 상당한 개선이 로봇 조작 작업에 대한 실용적 효과를 입증한다는 점입니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 빠르게 발전하며 로봇 조작 작업에서 유망한 성능을 보여주고 있습니다. 그러나 VLA 모델의 확장은 몇 가지 중요한 도전 과제를 제기합니다: (1) 새로운 VLA 모델을 처음부터 훈련하려면 상당한 계산 자원과 방대한 데이터셋이 필요합니다. 현재 로봇 데이터가 부족한 상황에서, 확장 과정에서 잘 사전 훈련된 VLA 모델 가중치를 완전히 활용하는 것이 특히 중요합니다. (2) 실시간 제어는 모델 용량과 계산 효율성 사이의 신중한 균형을 요구합니다. 이러한 도전 과제를 해결하기 위해, 우리는 AdaMoE를 제안합니다. 이는 밀집 VLA 모델의 사전 훈련 가중치를 상속받고, 피드포워드 레이어를 희소 활성화된 MoE 레이어로 대체하여 액션 전문가를 확장하는 Mixture-of-Experts (MoE) 아키텍처입니다. AdaMoE는 전통적인 라우터와 함께 작동하는 독립적인 스케일 어댑터를 통해 전문가 선택과 전문가 가중치를 분리하는 분리 기술을 사용합니다. 이를 통해 작업 관련성에 따라 전문가를 선택하면서 독립적으로 제어된 가중치로 기여할 수 있어, 승자 독식 동역학이 아닌 협력적 전문가 활용이 가능합니다. 우리의 접근 방식은 전문성이 독점될 필요가 없음을 보여줍니다. 대신, 협력적 전문가 활용을 통해 계산 효율성을 유지하면서 우수한 성능을 달성할 수 있습니다. AdaMoE는 주요 벤치마크에서 기준 모델을 일관되게 능가하며, LIBERO에서 1.8%, RoboTwin에서 9.3%의 성능 향상을 제공합니다. 가장 중요한 것은 실제 실험에서 21.5%의 상당한 개선이 로봇 조작 작업에 대한 실용적 효과를 입증한다는 점입니다.

## 参考
- http://arxiv.org/abs/2510.14300v1
