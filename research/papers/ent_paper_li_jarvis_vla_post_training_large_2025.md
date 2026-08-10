---
$id: ent_paper_li_jarvis_vla_post_training_large_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse'
  zh: JARVIS-VLA
  ko: 'JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse'
summary:
  en: 'JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse (JARVIS-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University, and published
    at ACL 2025.'
  zh: JARVIS-VLA 是由北京大学提出的2025年大型视觉-语言-动作模型，发表于 ACL 2025。其核心贡献在于通过视觉与语言引导的自监督后训练方法，增强基础视觉语言模型的世界知识、视觉识别与空间定位能力，从而在Minecraft中实现超过1000种原子任务的指令跟随，性能较最佳基线提升40%。
  ko: 'JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse (JARVIS-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University, and published
    at ACL 2025.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- jarvis_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.16365v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1042 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: JARVIS-VLA source
  url: https://aclanthology.org/2025.findings-acl.920/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
JARVIS-VLA 针对开放世界环境中基于动作的决策任务，提出了一种名为“视觉语言后训练驱动动作”的新方法。该方法在自监督框架下，利用视觉与语言信号对视觉语言模型进行后训练，显著提升了模型在开放世界中的世界知识、视觉识别与空间定位能力。基于此范式，JARVIS-VLA 成为首个能在Minecraft中遵循人类指令执行超过1000种原子任务（包括合成、冶炼、烹饪、采矿与击杀）的VLA模型。实验表明，在非轨迹任务上的后训练带来了40%的性能提升，超越了传统模仿学习策略，达到当前最优水平。项目代码、模型与数据集已开源。

## 核心内容
### 方法概述
JARVIS-VLA 的核心创新在于“视觉语言后训练”（Act from Visual Language Post-Training），该方法通过自监督方式，利用视觉与语言引导对基础视觉语言模型进行后训练，而非仅关注动作后训练。这一过程增强了模型在开放世界中的三项关键能力：
- **世界知识**：理解环境中的物体、规则与因果关系。
- **视觉识别**：准确感知场景中的视觉元素。
- **空间定位**：在三维空间中定位物体与自身位置。

### 架构与训练
- **基础模型**：基于大规模网络数据集预训练的视觉语言模型。
- **后训练范式**：采用非轨迹任务（如视觉问答、空间推理）进行自监督学习，而非仅依赖动作序列数据。
- **动作生成**：后训练后的模型通过键盘与鼠标控制，在Minecraft中执行原子任务。

### 实验设置
- **环境**：Minecraft 开放世界，涵盖超过1000种原子任务，包括 crafting、smelting、cooking、mining 与 killing。
- **基线**：对比传统模仿学习策略与最佳智能体基线。
- **评估指标**：任务成功率。

### 关键结果
- **性能提升**：后训练在非轨迹任务上带来 **40%** 的提升，超越最佳智能体基线。
- **SOTA 表现**：在Minecraft中达到当前最优性能，优于传统模仿学习策略。
- **任务覆盖**：成功执行超过1000种不同原子任务，支持人类指令跟随。

### 结论
JARVIS-VLA 证明了通过视觉与语言后训练增强基础模型，而非仅聚焦动作后训练，能显著提升开放世界决策能力。该工作为VLA模型在复杂环境中的应用提供了新范式，并开源了代码、模型与数据集以促进后续研究。

## Overview
Recently, action-based decision-making in open-world environments has gained significant attention. Visual Language Action (VLA) models, pretrained on large-scale web datasets, have shown promise in decision-making tasks. However, previous work has primarily focused on action post-training, often neglecting enhancements to the foundational model itself. In response, we introduce a novel approach, Act from Visual Language Post-Training, which refines Visual Language Models (VLMs) through visual and linguistic guidance in a self-supervised manner. This enhancement improves the models' capabilities in world knowledge, visual recognition, and spatial grounding in open-world environments. Following the above post-training paradigms, we obtain the first VLA models in Minecraft that can follow human instructions on over 1k different atomic tasks, including crafting, smelting, cooking, mining, and killing. Our experiments demonstrate that post-training on non-trajectory tasks leads to a significant 40% improvement over the best agent baseline on a diverse set of atomic tasks. Furthermore, we demonstrate that our approach surpasses traditional imitation learning-based policies in Minecraft, achieving state-of-the-art performance. We have open-sourced the code, models, and datasets to foster further research. The project page can be found in https://craftjarvis.github.io/JarvisVLA.

## 参考
- http://arxiv.org/abs/2503.16365v2

## 개요
JARVIS-VLA는 개방형 세계 환경에서의 행동 기반 의사 결정 작업을 위해 "시각 언어 사후 훈련 기반 행동"이라는 새로운 방법을 제안합니다. 이 방법은 자기 지도 학습 프레임워크에서 시각 및 언어 신호를 활용하여 시각 언어 모델을 사후 훈련함으로써, 개방형 세계에서의 세계 지식, 시각 인식 및 공간 위치 파악 능력을 크게 향상시킵니다. 이 패러다임을 기반으로 JARVIS-VLA는 Minecraft에서 인간의 지시를 따라 1000가지 이상의 원자적 작업(합성, 제련, 요리, 채굴 및 처치 포함)을 수행할 수 있는 최초의 VLA 모델이 되었습니다. 실험 결과, 비궤적 작업에서의 사후 훈련은 40%의 성능 향상을 가져왔으며, 전통적인 모방 학습 전략을 능가하여 최첨단 수준에 도달했습니다. 프로젝트 코드, 모델 및 데이터셋은 오픈소스로 공개되었습니다.

## 핵심 내용
### 방법 개요
JARVIS-VLA의 핵심 혁신은 "시각 언어 사후 훈련"(Act from Visual Language Post-Training)으로, 이 방법은 행동 사후 훈련에만 초점을 맞추는 대신 자기 지도 학습 방식으로 시각 및 언어 지도를 활용하여 기초 시각 언어 모델을 사후 훈련합니다. 이 과정은 개방형 세계에서 모델의 세 가지 핵심 능력을 강화합니다:
- **세계 지식**: 환경의 객체, 규칙 및 인과 관계를 이해합니다.
- **시각 인식**: 장면의 시각적 요소를 정확히 인지합니다.
- **공간 위치 파악**: 3차원 공간에서 객체와 자신의 위치를 파악합니다.

### 아키텍처 및 훈련
- **기초 모델**: 대규모 웹 데이터셋으로 사전 훈련된 시각 언어 모델.
- **사후 훈련 패러다임**: 행동 시퀀스 데이터에만 의존하지 않고 비궤적 작업(예: 시각 질의 응답, 공간 추론)을 통한 자기 지도 학습을 채택합니다.
- **행동 생성**: 사후 훈련된 모델은 키보드와 마우스 제어를 통해 Minecraft에서 원자적 작업을 수행합니다.

### 실험 설정
- **환경**: Minecraft 개방형 세계로, crafting, smelting, cooking, mining 및 killing을 포함한 1000가지 이상의 원자적 작업을 다룹니다.
- **기준선**: 전통적인 모방 학습 전략 및 최고 에이전트 기준선과 비교합니다.
- **평가 지표**: 작업 성공률.

### 핵심 결과
- **성능 향상**: 비궤적 작업에서의 사후 훈련은 **40%** 의 향상을 가져오며 최고 에이전트 기준선을 능가합니다.
- **SOTA 성능**: Minecraft에서 최첨단 성능에 도달하며 전통적인 모방 학습 전략보다 우수합니다.
- **작업 범위**: 1000가지 이상의 다양한 원자적 작업을 성공적으로 수행하며 인간의 지시 따르기를 지원합니다.

### 결론
JARVIS-VLA는 행동 사후 훈련에만 초점을 맞추는 대신 시각 및 언어 사후 훈련을 통해 기초 모델을 강화하는 것이 개방형 세계 의사 결정 능력을 크게 향상시킬 수 있음을 입증했습니다. 이 연구는 복잡한 환경에서 VLA 모델의 응용을 위한 새로운 패러다임을 제공하며, 후속 연구를 촉진하기 위해 코드, 모델 및 데이터셋을 오픈소스로 공개했습니다.
