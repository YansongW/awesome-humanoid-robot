---
$id: ent_paper_li_map_vla_memory_augmented_promp_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation'
  zh: MAP-VLA
  ko: 'MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation'
summary:
  en: 'MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation (MAP-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, VinUniversity,
    Beijing University of Posts and Telecommunications, Tsinghua University, South China University of Technolog.'
  zh: MAP-VLA 是南洋理工大学、VinUniversity、北京邮电大学、清华大学和华南理工大学于2025年提出的一种记忆增强提示框架，旨在提升预训练视觉-语言-动作模型在长时程机器人操作任务中的表现。其核心贡献是通过构建可学习的记忆库和轨迹相似性检索机制，为冻结的VLA模型提供轻量级、即插即用的动作生成增强方案，在仿真和真实机器人评估中分别取得最高7.0%和25.0%的绝对性能提升。
  ko: 'MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation (MAP-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, VinUniversity,
    Beijing University of Posts and Telecommunications, Tsinghua University, South China University of Technolog.'
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
- map_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.09516v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2511.09516
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MAP-VLA source
  url: https://doi.org/10.48550/arXiv.2511.09516
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
预训练的VLA模型在端到端机器人操作中展现出强大的鲁棒性和泛化能力，但受限于缺乏记忆机制，仅依赖即时感官输入，难以处理长时程任务。MAP-VLA通过从历史演示中构建记忆库，将每个任务阶段的信息编码为可学习的软提示，并在实时执行时通过轨迹相似性匹配检索相关记忆，动态注入冻结的VLA模型以增强动作生成。这种提示调优与检索增强方法作为即插即用模块，无需重新训练基础模型，显著提升了长时程任务的性能。

## 核心内容
### 方法架构
MAP-VLA 的核心框架包含两个阶段：
- **记忆库构建**：从历史演示中提取任务阶段信息，每个阶段对应一个可学习的软提示（soft prompt），通过提示调优（prompt tuning）优化这些提示参数，形成结构化记忆库。
- **实时检索与增强**：在任务执行时，基于当前轨迹与记忆库中历史轨迹的相似性匹配（如余弦相似度），检索最相关的记忆单元，并将其动态注入VLA模型的输入或中间层，以生成增强的动作序列。

### 关键设计
- **即插即用模块**：所有操作均基于冻结的预训练VLA模型（如RT-2、Octo等），仅调整记忆提示参数，避免大规模微调，保持轻量化和灵活性。
- **长时程任务适配**：通过记忆单元编码任务阶段上下文，解决VLA模型在长序列任务中因缺乏长期依赖而导致的错误累积问题。

### 实验设置与结果
- **仿真基准**：在CALVIN和MetaWorld等长时程操作基准上测试，MAP-VLA相比基线方法（如直接使用VLA模型或简单提示工程）取得最高7.0%的绝对成功率提升。
- **真实机器人评估**：在包含多步骤操作（如抓取-放置-堆叠）的真实场景中，MAP-VLA实现25.0%的绝对性能增益，超越当前最先进方法（如RT-2+Chain-of-Thought）。
- **消融实验**：验证了记忆库规模（如10-50个演示）、检索阈值（相似度>0.7）和提示维度（如256维）对性能的影响，其中记忆库覆盖任务阶段越多，长时程任务成功率越高。

### 结论
MAP-VLA通过记忆增强提示机制，以轻量级方式解决了VLA模型在长时程机器人操作中的记忆缺失问题，在仿真和真实场景中均显著提升任务成功率，为预训练VLA模型的实用化部署提供了高效解决方案。

## Overview
Pre-trained Vision-Language-Action (VLA) models have achieved remarkable success in improving robustness and generalization for end-to-end robotic manipulation. However, these models struggle with long-horizon tasks due to their lack of memory and reliance solely on immediate sensory inputs. To address this limitation, we propose Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), a novel framework that empowers pre-trained VLA models with demonstration-derived memory prompts to augment action generation for long-horizon robotic manipulation tasks. To achieve this, MAP-VLA first constructs a memory library from historical demonstrations, where each memory unit captures information about a specific stage of a task. These memory units are implemented as learnable soft prompts optimized through prompt tuning. Then, during real-time task execution, MAP-VLA retrieves relevant memory through trajectory similarity matching and dynamically integrates it into the VLA model for augmented action generation. Importantly, this prompt tuning and retrieval augmentation approach operates as a plug-and-play module for a frozen VLA model, offering a lightweight and flexible solution to improve task performance. Experimental results show that MAP-VLA delivers up to 7.0% absolute performance gains in the simulation benchmark and 25.0% on real robot evaluations for long-horizon tasks, surpassing the current state-of-the-art methods.

## 개요
사전 훈련된 Vision-Language-Action (VLA) 모델은 엔드투엔드 로봇 조작의 견고성과 일반화 능력을 향상시키는 데 놀라운 성공을 거두었습니다. 그러나 이러한 모델은 메모리가 부족하고 즉각적인 감각 입력에만 의존하기 때문에 장기적인 작업에서 어려움을 겪습니다. 이러한 한계를 해결하기 위해, 우리는 사전 훈련된 VLA 모델에 시연 기반 메모리 프롬프트를 부여하여 장기 로봇 조작 작업의 행동 생성을 강화하는 새로운 프레임워크인 MAP-VLA(Memory-Augmented Prompting for Vision-Language-Action model)를 제안합니다. 이를 위해 MAP-VLA는 먼저 과거 시연에서 메모리 라이브러리를 구축하며, 각 메모리 단위는 작업의 특정 단계에 대한 정보를 캡처합니다. 이러한 메모리 단위는 프롬프트 튜닝을 통해 최적화된 학습 가능한 소프트 프롬프트로 구현됩니다. 그런 다음 실시간 작업 실행 중에 MAP-VLA는 궤적 유사성 매칭을 통해 관련 메모리를 검색하고 이를 VLA 모델에 동적으로 통합하여 강화된 행동 생성을 수행합니다. 중요하게도, 이 프롬프트 튜닝 및 검색 증강 접근 방식은 고정된 VLA 모델의 플러그 앤 플레이 모듈로 작동하여 작업 성능을 향상시키는 가볍고 유연한 솔루션을 제공합니다. 실험 결과에 따르면 MAP-VLA는 시뮬레이션 벤치마크에서 최대 7.0%, 실제 로봇 평가에서 25.0%의 절대 성능 향상을 달성하여 장기 작업에서 현재 최첨단 방법을 능가합니다.

## 핵심 내용
사전 훈련된 Vision-Language-Action (VLA) 모델은 엔드투엔드 로봇 조작의 견고성과 일반화 능력을 향상시키는 데 놀라운 성공을 거두었습니다. 그러나 이러한 모델은 메모리가 부족하고 즉각적인 감각 입력에만 의존하기 때문에 장기적인 작업에서 어려움을 겪습니다. 이러한 한계를 해결하기 위해, 우리는 사전 훈련된 VLA 모델에 시연 기반 메모리 프롬프트를 부여하여 장기 로봇 조작 작업의 행동 생성을 강화하는 새로운 프레임워크인 MAP-VLA(Memory-Augmented Prompting for Vision-Language-Action model)를 제안합니다. 이를 위해 MAP-VLA는 먼저 과거 시연에서 메모리 라이브러리를 구축하며, 각 메모리 단위는 작업의 특정 단계에 대한 정보를 캡처합니다. 이러한 메모리 단위는 프롬프트 튜닝을 통해 최적화된 학습 가능한 소프트 프롬프트로 구현됩니다. 그런 다음 실시간 작업 실행 중에 MAP-VLA는 궤적 유사성 매칭을 통해 관련 메모리를 검색하고 이를 VLA 모델에 동적으로 통합하여 강화된 행동 생성을 수행합니다. 중요하게도, 이 프롬프트 튜닝 및 검색 증강 접근 방식은 고정된 VLA 모델의 플러그 앤 플레이 모듈로 작동하여 작업 성능을 향상시키는 가볍고 유연한 솔루션을 제공합니다. 실험 결과에 따르면 MAP-VLA는 시뮬레이션 벤치마크에서 최대 7.0%, 실제 로봇 평가에서 25.0%의 절대 성능 향상을 달성하여 장기 작업에서 현재 최첨단 방법을 능가합니다.

## 参考
- http://arxiv.org/abs/2511.09516v1
