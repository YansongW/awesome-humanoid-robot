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
  zh: 'MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation (MAP-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, VinUniversity,
    Beijing University of Posts and Telecommunications, Tsinghua University, South China University of Technolog.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.09516v1.
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
Pre-trained Vision-Language-Action (VLA) models have achieved remarkable success in improving robustness and generalization for end-to-end robotic manipulation. However, these models struggle with long-horizon tasks due to their lack of memory and reliance solely on immediate sensory inputs. To address this limitation, we propose Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), a novel framework that empowers pre-trained VLA models with demonstration-derived memory prompts to augment action generation for long-horizon robotic manipulation tasks. To achieve this, MAP-VLA first constructs a memory library from historical demonstrations, where each memory unit captures information about a specific stage of a task. These memory units are implemented as learnable soft prompts optimized through prompt tuning. Then, during real-time task execution, MAP-VLA retrieves relevant memory through trajectory similarity matching and dynamically integrates it into the VLA model for augmented action generation. Importantly, this prompt tuning and retrieval augmentation approach operates as a plug-and-play module for a frozen VLA model, offering a lightweight and flexible solution to improve task performance. Experimental results show that MAP-VLA delivers up to 7.0% absolute performance gains in the simulation benchmark and 25.0% on real robot evaluations for long-horizon tasks, surpassing the current state-of-the-art methods.

## 核心内容
Pre-trained Vision-Language-Action (VLA) models have achieved remarkable success in improving robustness and generalization for end-to-end robotic manipulation. However, these models struggle with long-horizon tasks due to their lack of memory and reliance solely on immediate sensory inputs. To address this limitation, we propose Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), a novel framework that empowers pre-trained VLA models with demonstration-derived memory prompts to augment action generation for long-horizon robotic manipulation tasks. To achieve this, MAP-VLA first constructs a memory library from historical demonstrations, where each memory unit captures information about a specific stage of a task. These memory units are implemented as learnable soft prompts optimized through prompt tuning. Then, during real-time task execution, MAP-VLA retrieves relevant memory through trajectory similarity matching and dynamically integrates it into the VLA model for augmented action generation. Importantly, this prompt tuning and retrieval augmentation approach operates as a plug-and-play module for a frozen VLA model, offering a lightweight and flexible solution to improve task performance. Experimental results show that MAP-VLA delivers up to 7.0% absolute performance gains in the simulation benchmark and 25.0% on real robot evaluations for long-horizon tasks, surpassing the current state-of-the-art methods.

## 参考
- http://arxiv.org/abs/2511.09516v1

## Overview
Pre-trained Vision-Language-Action (VLA) models have achieved remarkable success in improving robustness and generalization for end-to-end robotic manipulation. However, these models struggle with long-horizon tasks due to their lack of memory and reliance solely on immediate sensory inputs. To address this limitation, we propose Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), a novel framework that empowers pre-trained VLA models with demonstration-derived memory prompts to augment action generation for long-horizon robotic manipulation tasks. To achieve this, MAP-VLA first constructs a memory library from historical demonstrations, where each memory unit captures information about a specific stage of a task. These memory units are implemented as learnable soft prompts optimized through prompt tuning. Then, during real-time task execution, MAP-VLA retrieves relevant memory through trajectory similarity matching and dynamically integrates it into the VLA model for augmented action generation. Importantly, this prompt tuning and retrieval augmentation approach operates as a plug-and-play module for a frozen VLA model, offering a lightweight and flexible solution to improve task performance. Experimental results show that MAP-VLA delivers up to 7.0% absolute performance gains in the simulation benchmark and 25.0% on real robot evaluations for long-horizon tasks, surpassing the current state-of-the-art methods.

## Content
Pre-trained Vision-Language-Action (VLA) models have achieved remarkable success in improving robustness and generalization for end-to-end robotic manipulation. However, these models struggle with long-horizon tasks due to their lack of memory and reliance solely on immediate sensory inputs. To address this limitation, we propose Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), a novel framework that empowers pre-trained VLA models with demonstration-derived memory prompts to augment action generation for long-horizon robotic manipulation tasks. To achieve this, MAP-VLA first constructs a memory library from historical demonstrations, where each memory unit captures information about a specific stage of a task. These memory units are implemented as learnable soft prompts optimized through prompt tuning. Then, during real-time task execution, MAP-VLA retrieves relevant memory through trajectory similarity matching and dynamically integrates it into the VLA model for augmented action generation. Importantly, this prompt tuning and retrieval augmentation approach operates as a plug-and-play module for a frozen VLA model, offering a lightweight and flexible solution to improve task performance. Experimental results show that MAP-VLA delivers up to 7.0% absolute performance gains in the simulation benchmark and 25.0% on real robot evaluations for long-horizon tasks, surpassing the current state-of-the-art methods.

## 개요
사전 훈련된 Vision-Language-Action (VLA) 모델은 엔드투엔드 로봇 조작의 견고성과 일반화 능력을 향상시키는 데 놀라운 성공을 거두었습니다. 그러나 이러한 모델은 메모리가 부족하고 즉각적인 감각 입력에만 의존하기 때문에 장기적인 작업에서 어려움을 겪습니다. 이러한 한계를 해결하기 위해, 우리는 사전 훈련된 VLA 모델에 시연 기반 메모리 프롬프트를 부여하여 장기 로봇 조작 작업의 행동 생성을 강화하는 새로운 프레임워크인 MAP-VLA(Memory-Augmented Prompting for Vision-Language-Action model)를 제안합니다. 이를 위해 MAP-VLA는 먼저 과거 시연에서 메모리 라이브러리를 구축하며, 각 메모리 단위는 작업의 특정 단계에 대한 정보를 캡처합니다. 이러한 메모리 단위는 프롬프트 튜닝을 통해 최적화된 학습 가능한 소프트 프롬프트로 구현됩니다. 그런 다음 실시간 작업 실행 중에 MAP-VLA는 궤적 유사성 매칭을 통해 관련 메모리를 검색하고 이를 VLA 모델에 동적으로 통합하여 강화된 행동 생성을 수행합니다. 중요하게도, 이 프롬프트 튜닝 및 검색 증강 접근 방식은 고정된 VLA 모델의 플러그 앤 플레이 모듈로 작동하여 작업 성능을 향상시키는 가볍고 유연한 솔루션을 제공합니다. 실험 결과에 따르면 MAP-VLA는 시뮬레이션 벤치마크에서 최대 7.0%, 실제 로봇 평가에서 25.0%의 절대 성능 향상을 달성하여 장기 작업에서 현재 최첨단 방법을 능가합니다.

## 핵심 내용
사전 훈련된 Vision-Language-Action (VLA) 모델은 엔드투엔드 로봇 조작의 견고성과 일반화 능력을 향상시키는 데 놀라운 성공을 거두었습니다. 그러나 이러한 모델은 메모리가 부족하고 즉각적인 감각 입력에만 의존하기 때문에 장기적인 작업에서 어려움을 겪습니다. 이러한 한계를 해결하기 위해, 우리는 사전 훈련된 VLA 모델에 시연 기반 메모리 프롬프트를 부여하여 장기 로봇 조작 작업의 행동 생성을 강화하는 새로운 프레임워크인 MAP-VLA(Memory-Augmented Prompting for Vision-Language-Action model)를 제안합니다. 이를 위해 MAP-VLA는 먼저 과거 시연에서 메모리 라이브러리를 구축하며, 각 메모리 단위는 작업의 특정 단계에 대한 정보를 캡처합니다. 이러한 메모리 단위는 프롬프트 튜닝을 통해 최적화된 학습 가능한 소프트 프롬프트로 구현됩니다. 그런 다음 실시간 작업 실행 중에 MAP-VLA는 궤적 유사성 매칭을 통해 관련 메모리를 검색하고 이를 VLA 모델에 동적으로 통합하여 강화된 행동 생성을 수행합니다. 중요하게도, 이 프롬프트 튜닝 및 검색 증강 접근 방식은 고정된 VLA 모델의 플러그 앤 플레이 모듈로 작동하여 작업 성능을 향상시키는 가볍고 유연한 솔루션을 제공합니다. 실험 결과에 따르면 MAP-VLA는 시뮬레이션 벤치마크에서 최대 7.0%, 실제 로봇 평가에서 25.0%의 절대 성능 향상을 달성하여 장기 작업에서 현재 최첨단 방법을 능가합니다.
