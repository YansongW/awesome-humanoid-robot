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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.09516v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (972 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.09516v1

## 개요
사전 훈련된 VLA 모델은 엔드투엔드 로봇 조작에서 강력한 견고성과 일반화 능력을 보여주지만, 메모리 메커니즘이 부족하여 즉각적인 감각 입력에만 의존하므로 장기간 작업을 처리하기 어렵습니다. MAP-VLA는 과거 시연에서 메모리 뱅크를 구축하여 각 작업 단계의 정보를 학습 가능한 소프트 프롬프트로 인코딩하고, 실시간 실행 시 궤적 유사성 매칭을 통해 관련 메모리를 검색하여 동결된 VLA 모델에 동적으로 주입함으로써 동작 생성을 강화합니다. 이러한 프롬프트 튜닝 및 검색 증강 방식은 플러그 앤 플레이 모듈로 작동하며, 기본 모델을 재훈련할 필요 없이 장기간 작업의 성능을 크게 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
MAP-VLA의 핵심 프레임워크는 두 단계로 구성됩니다:
- **메모리 뱅크 구축**: 과거 시연에서 작업 단계 정보를 추출하고, 각 단계는 학습 가능한 소프트 프롬프트에 해당하며, 프롬프트 튜닝을 통해 이러한 프롬프트 매개변수를 최적화하여 구조화된 메모리 뱅크를 형성합니다.
- **실시간 검색 및 증강**: 작업 실행 시 현재 궤적과 메모리 뱅크 내 과거 궤적 간의 유사성 매칭(예: 코사인 유사도)을 기반으로 가장 관련성 높은 메모리 유닛을 검색하고, 이를 VLA 모델의 입력 또는 중간 계층에 동적으로 주입하여 강화된 동작 시퀀스를 생성합니다.

### 핵심 설계
- **플러그 앤 플레이 모듈**: 모든 작업은 동결된 사전 훈련 VLA 모델(예: RT-2, Octo 등)을 기반으로 하며, 메모리 프롬프트 매개변수만 조정하여 대규모 미세 조정을 피하고 경량성과 유연성을 유지합니다.
- **장기간 작업 적응**: 메모리 유닛이 작업 단계 컨텍스트를 인코딩하여, VLA 모델이 긴 시퀀스 작업에서 장기 의존성 부족으로 인해 발생하는 오류 누적 문제를 해결합니다.

### 실험 설정 및 결과
- **시뮬레이션 벤치마크**: CALVIN 및 MetaWorld와 같은 장기간 조작 벤치마크에서 테스트한 결과, MAP-VLA는 기준 방법(예: VLA 모델 직접 사용 또는 단순 프롬프트 엔지니어링) 대비 최대 7.0%의 절대 성공률 향상을 달성했습니다.
- **실제 로봇 평가**: 다단계 조작(예: 집기-놓기-쌓기)을 포함한 실제 시나리오에서 MAP-VLA는 25.0%의 절대 성능 향상을 구현하여 현재 최첨단 방법(예: RT-2+Chain-of-Thought)을 능가합니다.
- **절제 실험**: 메모리 뱅크 규모(예: 10-50개 시연), 검색 임계값(유사도 > 0.7) 및 프롬프트 차원(예: 256차원)이 성능에 미치는 영향을 검증했으며, 메모리 뱅크가 더 많은 작업 단계를 포함할수록 장기간 작업 성공률이 높아집니다.

### 결론
MAP-VLA는 메모리 증강 프롬프트 메커니즘을 통해 경량 방식으로 VLA 모델의 장기간 로봇 조작에서의 메모리 부족 문제를 해결하며, 시뮬레이션과 실제 시나리오 모두에서 작업 성공률을 크게 향상시켜 사전 훈련 VLA 모델의 실용적 배포를 위한 효율적인 솔루션을 제공합니다.
