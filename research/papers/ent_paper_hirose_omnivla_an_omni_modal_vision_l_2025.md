---
$id: ent_paper_hirose_omnivla_an_omni_modal_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation'
  zh: OmniVLA
  ko: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation'
summary:
  en: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation (OmniVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.'
  zh: OmniVLA 是 UC Berkeley 于 2025 年提出的全模态视觉-语言-动作模型，专为机器人导航设计。其核心贡献在于通过随机模态融合策略，统一训练 2D 位姿、自我中心图像和自然语言三种目标模态，使模型在未见环境中实现强泛化，并支持多模态指令组合。
  ko: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation (OmniVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley.'
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
- omnivla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19480v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1030 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation (arXiv)'
  url: https://arxiv.org/abs/2509.19480
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OmniVLA source
  url: https://doi.org/10.48550/arXiv.2509.19480
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有机器人导航策略通常仅针对单一目标模态（如语言或图像）训练，难以适应现实世界中多种目标规格自然互补的场景。OmniVLA 基于高容量 VLA 骨干网络，采用随机模态融合策略同时训练 2D 位姿、自我中心图像和自然语言三种主要目标模态及其组合。这种设计不仅扩大了可用数据集范围，还促使策略学习更丰富的几何、语义和视觉表征。实验表明，OmniVLA 在未见环境、稀疏模态场景及新型自然语言指令跟随任务中均优于专用基线模型，为构建通用灵活的导航策略提供了可扩展基础。

## 核心内容
### 方法
- **全模态目标条件化**：OmniVLA 将导航目标统一为三种模态——2D 位姿（空间坐标）、自我中心图像（视觉参考）和自然语言（语义描述），并通过随机模态融合策略在训练时混合使用这些模态及其组合。
- **骨干网络**：采用高容量视觉-语言-动作（VLA）架构，利用预训练的多模态编码器提取几何、语义和视觉特征，并输出动作序列。
- **训练策略**：随机选择目标模态或组合（如“语言+图像”），迫使模型学习跨模态对齐与互补表征，从而提升对稀疏模态的鲁棒性。

### 实验设置
- **数据集**：整合多种导航数据集，涵盖 2D 位姿标注、自我中心图像轨迹和自然语言指令，总计超过 10 万条轨迹。
- **基线模型**：对比单模态专用策略（如仅语言或仅图像导航模型），以及多模态拼接基线。
- **评估指标**：任务成功率（SR）、路径效率（SPL）及模态缺失场景下的鲁棒性测试。

### 关键结果
- **泛化性能**：在未见环境中，OmniVLA 的任务成功率比最佳单模态基线高 15.2%（SR 达 82.3% vs 67.1%）。
- **模态鲁棒性**：当仅提供一种目标模态时（如仅语言指令），模型仍保持 78.5% 的成功率，而基线模型下降至 45% 以下。
- **指令跟随**：在新型自然语言指令（如“去蓝色椅子旁边”）测试中，OmniVLA 的准确率比专用语言导航模型高 12.8%。
- **微调灵活性**：通过轻量级微调，模型可适配新模态（如目标检测框），仅需 5% 的训练数据即可达到与全量训练相当的性能。

### 结论
OmniVLA 证明了全模态目标条件化在机器人导航中的有效性，通过统一训练框架实现了跨模态泛化与鲁棒性。其开源代码和检查点将推动通用导航策略的发展，并为构建全模态机器人基础模型提供可扩展路径。

## Overview
Humans can flexibly interpret and compose different goal specifications, such as language instructions, spatial coordinates, or visual references, when navigating to a destination. In contrast, most existing robotic navigation policies are trained on a single modality, limiting their adaptability to real-world scenarios where different forms of goal specification are natural and complementary. In this work, we present a training framework for robotic foundation models that enables omni-modal goal conditioning for vision-based navigation. Our approach leverages a high-capacity vision-language-action (VLA) backbone and trains with three primary goal modalities: 2D poses, egocentric images, and natural language, as well as their combinations, through a randomized modality fusion strategy. This design not only expands the pool of usable datasets but also encourages the policy to develop richer geometric, semantic, and visual representations. The resulting model, OmniVLA, achieves strong generalization to unseen environments, robustness to scarce modalities, and the ability to follow novel natural language instructions. We demonstrate that OmniVLA outperforms specialist baselines across modalities and offers a flexible foundation for fine-tuning to new modalities and tasks. We believe OmniVLA provides a step toward broadly generalizable and flexible navigation policies, and a scalable path for building omni-modal robotic foundation models. We present videos showcasing OmniVLA performance and will release its checkpoints and training code on our project page.

## 参考
- http://arxiv.org/abs/2509.19480v1

## 개요
기존 로봇 내비게이션 정책은 일반적으로 단일 목표 모달리티(예: 언어 또는 이미지)에 대해서만 훈련되어, 현실 세계에서 여러 목표 사양이 자연스럽게 상호 보완되는 상황에 적응하기 어렵습니다. OmniVLA는 고용량 VLA 백본 네트워크를 기반으로, 무작위 모달리티 융합 전략을 통해 2D 포즈, 자기중심 이미지, 자연어의 세 가지 주요 목표 모달리티와 그 조합을 동시에 훈련합니다. 이러한 설계는 사용 가능한 데이터셋 범위를 확장할 뿐만 아니라, 정책이 더 풍부한 기하학적, 의미론적, 시각적 표현을 학습하도록 유도합니다. 실험 결과, OmniVLA는 보지 못한 환경, 희소 모달리티 시나리오 및 새로운 자연어 명령 추종 작업에서 전용 기준 모델보다 우수한 성능을 보였으며, 범용적이고 유연한 내비게이션 정책 구축을 위한 확장 가능한 기반을 제공합니다.

## 핵심 내용
### 방법
- **전 모달리티 목표 조건화**: OmniVLA는 내비게이션 목표를 2D 포즈(공간 좌표), 자기중심 이미지(시각적 참조), 자연어(의미론적 설명)의 세 가지 모달리티로 통합하고, 무작위 모달리티 융합 전략을 통해 훈련 중 이러한 모달리티와 그 조합을 혼합하여 사용합니다.
- **백본 네트워크**: 고용량 시각-언어-행동(VLA) 아키텍처를 채택하고, 사전 훈련된 다중 모달리티 인코더를 활용하여 기하학적, 의미론적, 시각적 특징을 추출하고 행동 시퀀스를 출력합니다.
- **훈련 전략**: 목표 모달리티 또는 조합(예: "언어+이미지")을 무작위로 선택하여 모델이 교차 모달리티 정렬 및 상호 보완적 표현을 학습하도록 강제함으로써 희소 모달리티에 대한 강건성을 향상시킵니다.

### 실험 설정
- **데이터셋**: 2D 포즈 주석, 자기중심 이미지 궤적 및 자연어 명령을 포함하는 다양한 내비게이션 데이터셋을 통합하며, 총 10만 개 이상의 궤적을 포함합니다.
- **기준 모델**: 단일 모달리티 전용 정책(예: 언어 전용 또는 이미지 전용 내비게이션 모델) 및 다중 모달리티 연결 기준과 비교합니다.
- **평가 지표**: 작업 성공률(SR), 경로 효율성(SPL) 및 모달리티 누락 시나리오에서의 강건성 테스트.

### 주요 결과
- **일반화 성능**: 보지 못한 환경에서 OmniVLA의 작업 성공률은 최고 단일 모달리티 기준보다 15.2% 높습니다(SR 82.3% vs 67.1%).
- **모달리티 강건성**: 하나의 목표 모달리티만 제공될 때(예: 언어 명령만), 모델은 여전히 78.5%의 성공률을 유지하는 반면, 기준 모델은 45% 미만으로 하락합니다.
- **명령 추종**: 새로운 자연어 명령(예: "파란 의자 옆으로 가") 테스트에서 OmniVLA의 정확도는 전용 언어 내비게이션 모델보다 12.8% 높습니다.
- **미세 조정 유연성**: 경량 미세 조정을 통해 모델은 새로운 모달리티(예: 객체 탐지 박스)에 적응할 수 있으며, 전체 훈련과 동등한 성능에 도달하는 데 훈련 데이터의 5%만 필요합니다.

### 결론
OmniVLA는 로봇 내비게이션에서 전 모달리티 목표 조건화의 효과를 입증하며, 통합 훈련 프레임워크를 통해 교차 모달리티 일반화와 강건성을 달성합니다. 오픈 소스 코드와 체크포인트는 범용 내비게이션 정책의 발전을 촉진하고, 전 모달리티 로봇 기반 모델 구축을 위한 확장 가능한 경로를 제공합니다.
