---
$id: ent_paper_jabbour_dont_run_with_scissors_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dont Run with Scissors
  zh: GLUESTICK
  ko: Dont Run with Scissors
summary:
  en: Dont Run with Scissors (GLUESTICK), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by FieldAI, Harvard University.
  zh: GLUESTICK（Dont Run with Scissors）是2025年由FieldAI与哈佛大学联合提出的一种后剪枝恢复方法，用于提升视觉-语言-动作（VLA）模型在资源受限硬件上的部署效率。其核心贡献在于通过一次性的权重空间插值计算修正项，在不重新训练的前提下恢复剪枝模型的功能，显著降低安全违规率并保持稀疏性优势。
  ko: Dont Run with Scissors (GLUESTICK), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by FieldAI, Harvard University.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gluestick
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.08464v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Dont Run with Scissors (arXiv)
  url: https://arxiv.org/abs/2510.08464
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
VLA模型虽提升了机器人操作能力，但在资源有限硬件上部署困难。现有剪枝技术虽能压缩大语言模型，但在机器人领域研究不足。研究发现直接剪枝VLA模型会导致性能急剧下降和安全违规增加。GLUESTICK通过一次性的密集模型与剪枝模型权重空间插值计算修正项，在推理时由每个剪枝层调用该修正项以恢复丢失能力，且仅引入一个控制效率与精度权衡的超参数。该方法无需额外训练，与剪枝算法无关，在多种VLA架构及操作、导航任务中实现了竞争性的内存效率，同时显著恢复成功率并减少安全违规。

## 核心内容
### 方法
- **核心思想**：在权重空间中对密集模型与剪枝模型进行一次性插值，计算修正项。推理时每个剪枝层使用该修正项恢复功能，仅增加极小的计算开销。
- **关键特性**：无需重新训练；与具体剪枝算法无关；仅需一个超参数控制效率与精度的权衡。

### 实验设置
- **模型架构**：涵盖多种VLA架构，包括操作与导航任务。
- **评估指标**：成功率、内存效率、安全违规率。

### 关键结果
- **性能恢复**：在多种任务上，GLUESTICK显著恢复剪枝模型的成功率，接近密集模型水平。
- **安全改进**：有效降低安全违规率，解决剪枝导致的安全风险。
- **效率优势**：保持剪枝带来的内存节省，实现竞争性的内存效率。

### 结论
GLUESTICK为VLA模型剪枝后恢复提供了一种轻量级、无需训练的解决方案，在资源受限的机器人部署场景中具有实用价值。更多细节见项目网站：https://gluestick-vla.github.io/。

## Overview
Vision-Language-Action (VLA) models have advanced robotic capabilities but remain challenging to deploy on resource-limited hardware. Pruning has enabled efficient compression of large language models (LLMs), yet it is largely understudied in robotics. Surprisingly, we observe that pruning VLA models leads to drastic degradation and increased safety violations. We introduce GLUESTICK, a post-pruning recovery method that restores much of the original model's functionality while retaining sparsity benefits. Our method performs a one-time interpolation between the dense and pruned models in weight-space to compute a corrective term. This correction is used during inference by each pruned layer to recover lost capabilities with minimal overhead. GLUESTICK requires no additional training, is agnostic to the pruning algorithm, and introduces a single hyperparameter that controls the tradeoff between efficiency and accuracy. Across diverse VLA architectures and tasks in manipulation and navigation, GLUESTICK achieves competitive memory efficiency while substantially recovering success rates and reducing safety violations. Additional material can be found at: https://gluestick-vla.github.io/.

## 개요
Vision-Language-Action (VLA) 모델은 로봇의 성능을 향상시켰지만, 자원이 제한된 하드웨어에 배포하는 것은 여전히 어려운 과제입니다. Pruning(가지치기)은 대규모 언어 모델(LLM)의 효율적인 압축을 가능하게 했지만, 로봇 공학 분야에서는 거의 연구되지 않았습니다. 놀랍게도, VLA 모델을 가지치기하면 성능이 급격히 저하되고 안전 위반이 증가하는 것을 관찰했습니다. 우리는 GLUESTICK을 소개합니다. 이는 가지치기 후 복구 방법으로, 희소성(sparsity)의 이점을 유지하면서 원래 모델의 기능 대부분을 복원합니다. 이 방법은 밀집(dense) 모델과 가지치기된 모델 간의 가중치 공간에서 일회성 보간(interpolation)을 수행하여 보정 항(corrective term)을 계산합니다. 이 보정은 추론 중 각 가지치기된 레이어에서 최소한의 오버헤드로 손실된 기능을 복구하는 데 사용됩니다. GLUESTICK은 추가 학습이 필요 없고, 가지치기 알고리즘에 구애받지 않으며, 효율성과 정확성 간의 균형을 제어하는 단일 하이퍼파라미터를 도입합니다. 조작 및 탐색 작업에서 다양한 VLA 아키텍처와 작업에 걸쳐 GLUESTICK은 경쟁력 있는 메모리 효율성을 달성하면서 성공률을 크게 회복하고 안전 위반을 줄입니다. 추가 자료는 https://gluestick-vla.github.io/에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 로봇의 성능을 향상시켰지만, 자원이 제한된 하드웨어에 배포하는 것은 여전히 어려운 과제입니다. Pruning(가지치기)은 대규모 언어 모델(LLM)의 효율적인 압축을 가능하게 했지만, 로봇 공학 분야에서는 거의 연구되지 않았습니다. 놀랍게도, VLA 모델을 가지치기하면 성능이 급격히 저하되고 안전 위반이 증가하는 것을 관찰했습니다. 우리는 GLUESTICK을 소개합니다. 이는 가지치기 후 복구 방법으로, 희소성(sparsity)의 이점을 유지하면서 원래 모델의 기능 대부분을 복원합니다. 이 방법은 밀집(dense) 모델과 가지치기된 모델 간의 가중치 공간에서 일회성 보간(interpolation)을 수행하여 보정 항(corrective term)을 계산합니다. 이 보정은 추론 중 각 가지치기된 레이어에서 최소한의 오버헤드로 손실된 기능을 복구하는 데 사용됩니다. GLUESTICK은 추가 학습이 필요 없고, 가지치기 알고리즘에 구애받지 않으며, 효율성과 정확성 간의 균형을 제어하는 단일 하이퍼파라미터를 도입합니다. 조작 및 탐색 작업에서 다양한 VLA 아키텍처와 작업에 걸쳐 GLUESTICK은 경쟁력 있는 메모리 효율성을 달성하면서 성공률을 크게 회복하고 안전 위반을 줄입니다. 추가 자료는 https://gluestick-vla.github.io/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2510.08464v1
