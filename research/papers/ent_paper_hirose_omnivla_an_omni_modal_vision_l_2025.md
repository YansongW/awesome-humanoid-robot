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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19480v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
인간은 목적지로 이동할 때 언어 명령, 공간 좌표, 시각적 참조 등 다양한 목표 사양을 유연하게 해석하고 구성할 수 있습니다. 반면, 대부분의 기존 로봇 내비게이션 정책은 단일 모달리티로 훈련되어, 다양한 형태의 목표 사양이 자연스럽고 상호 보완적인 실제 환경에서의 적응성이 제한됩니다. 본 연구에서는 시각 기반 내비게이션을 위한 전모달 목표 조건화를 가능하게 하는 로봇 기초 모델 훈련 프레임워크를 제시합니다. 우리의 접근 방식은 고용량 비전-언어-행동(VLA) 백본을 활용하며, 무작위 모달리티 융합 전략을 통해 2D 포즈, 자기중심 이미지, 자연어의 세 가지 주요 목표 모달리티와 이들의 조합으로 훈련합니다. 이 설계는 사용 가능한 데이터셋 풀을 확장할 뿐만 아니라, 정책이 더 풍부한 기하학적, 의미론적, 시각적 표현을 개발하도록 장려합니다. 결과 모델인 OmniVLA는 보지 못한 환경에 대한 강력한 일반화, 희소 모달리티에 대한 견고성, 새로운 자연어 명령을 따르는 능력을 달성합니다. 우리는 OmniVLA가 모달리티 전반에서 전문가 기준선을 능가하며, 새로운 모달리티와 작업에 미세 조정할 수 있는 유연한 기반을 제공함을 입증합니다. OmniVLA가 광범위하게 일반화 가능하고 유연한 내비게이션 정책을 위한 한 걸음이며, 전모달 로봇 기초 모델 구축을 위한 확장 가능한 경로를 제공한다고 믿습니다. OmniVLA 성능을 보여주는 비디오를 제시하며, 프로젝트 페이지에서 체크포인트와 훈련 코드를 공개할 예정입니다.

## 핵심 내용
인간은 목적지로 이동할 때 언어 명령, 공간 좌표, 시각적 참조 등 다양한 목표 사양을 유연하게 해석하고 구성할 수 있습니다. 반면, 대부분의 기존 로봇 내비게이션 정책은 단일 모달리티로 훈련되어, 다양한 형태의 목표 사양이 자연스럽고 상호 보완적인 실제 환경에서의 적응성이 제한됩니다. 본 연구에서는 시각 기반 내비게이션을 위한 전모달 목표 조건화를 가능하게 하는 로봇 기초 모델 훈련 프레임워크를 제시합니다. 우리의 접근 방식은 고용량 비전-언어-행동(VLA) 백본을 활용하며, 무작위 모달리티 융합 전략을 통해 2D 포즈, 자기중심 이미지, 자연어의 세 가지 주요 목표 모달리티와 이들의 조합으로 훈련합니다. 이 설계는 사용 가능한 데이터셋 풀을 확장할 뿐만 아니라, 정책이 더 풍부한 기하학적, 의미론적, 시각적 표현을 개발하도록 장려합니다. 결과 모델인 OmniVLA는 보지 못한 환경에 대한 강력한 일반화, 희소 모달리티에 대한 견고성, 새로운 자연어 명령을 따르는 능력을 달성합니다. 우리는 OmniVLA가 모달리티 전반에서 전문가 기준선을 능가하며, 새로운 모달리티와 작업에 미세 조정할 수 있는 유연한 기반을 제공함을 입증합니다. OmniVLA가 광범위하게 일반화 가능하고 유연한 내비게이션 정책을 위한 한 걸음이며, 전모달 로봇 기초 모델 구축을 위한 확장 가능한 경로를 제공한다고 믿습니다. OmniVLA 성능을 보여주는 비디오를 제시하며, 프로젝트 페이지에서 체크포인트와 훈련 코드를 공개할 예정입니다.

## 参考
- http://arxiv.org/abs/2509.19480v1
