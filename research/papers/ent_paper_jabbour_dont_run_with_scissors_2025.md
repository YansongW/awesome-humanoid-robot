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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.08464v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (684 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2510.08464v1

## 개요
VLA 모델은 로봇 조작 능력을 향상시켰지만, 자원이 제한된 하드웨어에서의 배포는 어렵다. 기존 가지치기 기술은 대규모 언어 모델을 압축할 수 있지만, 로봇 분야에서의 연구는 부족하다. 연구에 따르면 VLA 모델을 직접 가지치기하면 성능이 급격히 저하되고 안전 위반이 증가한다. GLUESTICK은 일회성으로 밀집 모델과 가지치기 모델의 가중치 공간 보간을 통해 수정 항을 계산하며, 추론 시 각 가지치기 레이어가 이 수정 항을 호출하여 손실된 능력을 복구하고, 효율성과 정확성 간의 균형을 제어하는 단일 하이퍼파라미터만 도입한다. 이 방법은 추가 훈련이 필요 없고 가지치기 알고리즘과 무관하며, 다양한 VLA 아키텍처 및 조작, 내비게이션 작업에서 경쟁력 있는 메모리 효율성을 달성하면서 성공률을 크게 회복하고 안전 위반을 줄인다.

## 핵심 내용
### 방법
- **핵심 아이디어**: 가중치 공간에서 밀집 모델과 가지치기 모델을 일회성으로 보간하여 수정 항을 계산한다. 추론 시 각 가지치기 레이어가 이 수정 항을 사용하여 기능을 복구하며, 극히 작은 계산 오버헤드만 추가된다.
- **주요 특성**: 재훈련 불필요; 특정 가지치기 알고리즘과 무관; 효율성과 정확성의 균형을 제어하는 단일 하이퍼파라미터만 필요.

### 실험 설정
- **모델 아키텍처**: 조작 및 내비게이션 작업을 포함한 다양한 VLA 아키텍처를 포괄.
- **평가 지표**: 성공률, 메모리 효율성, 안전 위반율.

### 주요 결과
- **성능 회복**: 다양한 작업에서 GLUESTICK은 가지치기 모델의 성공률을 크게 회복하여 밀집 모델 수준에 근접한다.
- **안전 개선**: 안전 위반율을 효과적으로 낮추어 가지치기로 인한 안전 위험을 해결한다.
- **효율성 이점**: 가지치기로 인한 메모리 절약을 유지하며 경쟁력 있는 메모리 효율성을 달성한다.

### 결론
GLUESTICK은 VLA 모델 가지치기 후 복구를 위한 경량화되고 훈련이 필요 없는 솔루션을 제공하며, 자원이 제한된 로봇 배포 시나리오에서 실용적 가치가 있다. 더 많은 세부 사항은 프로젝트 웹사이트에서 확인할 수 있다: https://gluestick-vla.github.io/.
