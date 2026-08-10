---
$id: ent_paper_li_embodiment_transfer_learning_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Embodiment Transfer Learning for Vision-Language-Action Models
  zh: ET-VLA
  ko: Embodiment Transfer Learning for Vision-Language-Action Models
summary:
  en: Embodiment Transfer Learning for Vision-Language-Action Models (ET-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Shanghai University.
  zh: ET-VLA 是由上海大学提出的 2025 年大型视觉-语言-动作模型，专注于机器人操作。其核心贡献在于通过合成持续预训练（SCP）和具身图思维（Embodied Graph-of-Thought）技术，实现预训练 VLA 模型向多机器人（特别是双臂机器人）的高效迁移，在真实世界任务中相比
    OpenVLA 性能提升超过 53.2%。
  ko: Embodiment Transfer Learning for Vision-Language-Action Models (ET-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Shanghai University.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- et_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.01224v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (795 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Embodiment Transfer Learning for Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2511.01224
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ET-VLA source
  url: https://doi.org/10.48550/arXiv.2511.01224
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
ET-VLA 框架旨在解决现有自回归 VLA 模型在多机器人协作场景中的局限性。其核心创新是合成持续预训练（SCP），利用合成数据预热模型以适应新的具身形态，从而避免对真实人类演示的依赖并降低数据收集成本。此外，具身图思维（Embodied Graph-of-Thought）技术将每个子任务建模为节点，帮助模型区分不同机器人在任务执行中的功能与角色。该方法在模拟基准和真实机器人上针对三种不同的双臂具身形态进行了验证，显著提升了任务性能。

## 核心内容
### 方法架构
ET-VLA 框架包含两个核心阶段：
- **合成持续预训练（SCP）**：在迁移到新具身形态时，首先使用合成生成的数据对预训练 VLA 模型进行预热。该过程使模型学习正确的动作序列和精确的动作 token 数量，无需真实人类演示，大幅降低数据采集成本。
- **具身图思维（Embodied Graph-of-Thought）**：将复杂任务分解为多个子任务节点，每个节点对应一个子任务。模型通过图结构理解各机器人在任务执行中的角色分工，从而提升多机器人协作效率。

### 实验设置
- **验证场景**：在模拟基准和真实机器人上测试，覆盖三种不同的双臂具身形态（bimanual embodiments）。
- **对比基准**：以 OpenVLA 作为主要对比模型。

### 关键结果
- 在六个真实世界任务中，ET-VLA 相比 OpenVLA 平均性能提升 **53.2%**。
- SCP 有效解决了多机器人场景下动作 token 数量不匹配的问题。
- 具身图思维显著增强了模型对多机器人角色区分的理解能力。

### 结论
ET-VLA 通过合成数据预训练与任务图推理，为 VLA 模型向多机器人系统的迁移提供了高效、低成本的解决方案。所有代码将开源，以推动机器人学习社区的发展。

## Overview
Vision-language-action (VLA) models have significantly advanced robotic learning, enabling training on large-scale, cross-embodiment data and fine-tuning for specific robots. However, state-of-the-art autoregressive VLAs struggle with multi-robot collaboration. We introduce embodiment transfer learning, denoted as ET-VLA, a novel framework for efficient and effective transfer of pre-trained VLAs to multi-robot. ET-VLA's core is Synthetic Continued Pretraining (SCP), which uses synthetically generated data to warm up the model for the new embodiment, bypassing the need for real human demonstrations and reducing data collection costs. SCP enables the model to learn correct actions and precise action token numbers. Following SCP, the model is fine-tuned on target embodiment data. To further enhance the model performance on multi-embodiment, we present the Embodied Graph-of-Thought technique, a novel approach that formulates each sub-task as a node, that allows the VLA model to distinguish the functionalities and roles of each embodiment during task execution. Our work considers bimanual robots, a simple version of multi-robot to verify our approaches. We validate the effectiveness of our method on both simulation benchmarks and real robots covering three different bimanual embodiments. In particular, our proposed ET-VLA \space can outperform OpenVLA on six real-world tasks over 53.2%. We will open-source all codes to support the community in advancing VLA models for robot learning.

## 参考
- http://arxiv.org/abs/2511.01224v1

## 개요
ET-VLA 프레임워크는 기존 자기회귀 VLA 모델이 다중 로봇 협업 시나리오에서 가지는 한계를 해결하기 위해 설계되었습니다. 핵심 혁신은 합성 지속 사전학습(SCP)으로, 합성 데이터를 활용해 모델을 새로운 구현 형태에 맞게 예열함으로써 실제 인간 시연에 대한 의존을 피하고 데이터 수집 비용을 줄입니다. 또한, 구현 그래프 사고(Embodied Graph-of-Thought) 기술은 각 하위 작업을 노드로 모델링하여 모델이 작업 실행 중 서로 다른 로봇의 기능과 역할을 구분하도록 돕습니다. 이 방법은 시뮬레이션 벤치마크와 실제 로봇에서 세 가지 서로 다른 이중 팔 구현 형태를 대상으로 검증되었으며, 작업 성능을 크게 향상시켰습니다.

## 핵심 내용
### 방법 아키텍처
ET-VLA 프레임워크는 두 가지 핵심 단계를 포함합니다:
- **합성 지속 사전학습(SCP)**: 새로운 구현 형태로 전이할 때, 먼저 합성 생성 데이터를 사용하여 사전학습된 VLA 모델을 예열합니다. 이 과정은 실제 인간 시연 없이 모델이 올바른 동작 시퀀스와 정확한 동작 토큰 수를 학습하게 하여 데이터 수집 비용을 크게 줄입니다.
- **구현 그래프 사고(Embodied Graph-of-Thought)**: 복잡한 작업을 여러 하위 작업 노드로 분해하며, 각 노드는 하나의 하위 작업에 해당합니다. 모델은 그래프 구조를 통해 작업 실행 중 각 로봇의 역할 분담을 이해하여 다중 로봇 협업 효율을 향상시킵니다.

### 실험 설정
- **검증 시나리오**: 시뮬레이션 벤치마크와 실제 로봇에서 테스트하며, 세 가지 서로 다른 이중 팔 구현 형태를 포함합니다.
- **비교 기준**: OpenVLA를 주요 비교 모델로 사용합니다.

### 주요 결과
- 여섯 가지 실제 세계 작업에서 ET-VLA는 OpenVLA 대비 평균 성능이 **53.2%** 향상되었습니다.
- SCP는 다중 로봇 시나리오에서 동작 토큰 수 불일치 문제를 효과적으로 해결합니다.
- 구현 그래프 사고는 다중 로봇 역할 구분에 대한 모델의 이해 능력을 크게 강화합니다.

### 결론
ET-VLA는 합성 데이터 사전학습과 작업 그래프 추론을 통해 VLA 모델의 다중 로봇 시스템으로의 전이를 위한 효율적이고 저비용의 솔루션을 제공합니다. 모든 코드는 오픈소스로 공개되어 로봇 학습 커뮤니티의 발전을 촉진할 것입니다.
