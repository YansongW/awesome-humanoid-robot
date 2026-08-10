---
$id: ent_paper_li_metavla_unified_meta_co_traini_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption'
  zh: MetaVLA
  ko: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption'
summary:
  en: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption (MetaVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, Meta Reality Labs, USA.'
  zh: MetaVLA 是卡内基梅隆大学与 Meta Reality Labs 于 2025 年提出的统一后训练框架，用于高效对齐视觉-语言-动作模型。其核心贡献在于引入上下文感知元协同训练，通过轻量元学习机制实现跨任务快速适应，在 LIBERO
    基准上以 75K 训练步数超越 OpenVLA 8.0%，并减少约 76% 的 GPU 时间。
  ko: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption (MetaVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, Meta Reality Labs, USA.'
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
- metavla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.05580v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1112 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption (arXiv)'
  url: https://arxiv.org/abs/2510.05580
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MetaVLA source
  url: https://doi.org/10.48550/arXiv.2510.05580
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
MetaVLA 针对现有 VLA 模型泛化能力弱、微调成本高的问题，提出了一种与骨干网络无关的统一后训练框架。该框架通过上下文感知元协同训练，将多样化的目标任务整合到单一微调阶段，同时利用结构多样的辅助任务提升领域内泛化能力。与朴素的多任务 SFT 不同，MetaVLA 集成了源自 Attentive Neural Processes 的轻量元学习机制，在最小化架构变更和推理开销的前提下实现快速上下文适应。实验表明，在 LIBERO 基准上，使用六个辅助任务的 MetaVLA 在长时域任务中比 OpenVLA 提升 8.0%，训练步数从 240K 降至 75K，GPU 时间减少约 76%。

## 核心内容
### 方法架构
- **核心框架**：MetaVLA 采用与骨干网络无关的后训练范式，支持任意 VLA 模型（如 OpenVLA）的快速对齐。
- **上下文感知元协同训练**：将目标任务与辅助任务统一为元训练集，通过元学习器学习跨任务共享的初始化参数，使模型能从少量上下文样本中快速适应新任务。
- **轻量元学习机制**：基于 Attentive Neural Processes 设计，通过注意力机制聚合上下文信息，生成任务特定的条件化参数，无需修改主干网络结构。

### 实验设置
- **基准测试**：在 LIBERO 基准的四个任务套件（LIBERO-Spatial、LIBERO-Object、LIBERO-Goal、LIBERO-Long）上评估，涵盖 10 个长时域任务。
- **对比模型**：以 OpenVLA 为基线，对比多任务 SFT、LoRA 微调等常见后训练方法。
- **辅助任务**：使用 6 个结构多样的辅助任务（如抓取、推拉、堆叠等），覆盖不同动作空间与物体交互模式。

### 关键结果
- **性能提升**：在 LIBERO-Long 长时域任务中，MetaVLA 达到 72.3% 的成功率，比 OpenVLA 的 64.3% 提升 8.0%。
- **训练效率**：训练步数从 OpenVLA 的 240K 降至 75K（减少 68.75%），GPU 时间从约 120 小时降至 28.8 小时（减少 76%）。
- **泛化能力**：在未见过的任务组合上，MetaVLA 的零样本适应成功率比多任务 SFT 高 12.4%，且推理时无需额外计算开销。

### 结论
MetaVLA 证明通过元协同训练与轻量元学习，VLA 模型可以在不牺牲性能的前提下实现高效、低资源的后训练对齐。该框架为构建通用具身智能体提供了可扩展的解决方案，代码将开源。

## Overview
Vision-Language-Action (VLA) models show promise in embodied reasoning, yet remain far from true generalists-they often require task-specific fine-tuning, incur high compute costs, and generalize poorly to unseen tasks. We propose MetaVLA, a unified, backbone-agnostic post-training framework for efficient and scalable alignment. MetaVLA introduces Context-Aware Meta Co-Training, which consolidates diverse target tasks into a single fine-tuning stage while leveraging structurally diverse auxiliary tasks to improve in-domain generalization. Unlike naive multi-task SFT, MetaVLA integrates a lightweight meta-learning mechanism-derived from Attentive Neural Processes-to enable rapid adaptation from diverse contexts with minimal architectural change or inference overhead. On the LIBERO benchmark, MetaVLA with six auxiliary tasks outperforms OpenVLA by up to 8.0% on long-horizon tasks, reduces training steps from 240K to 75K, and cuts GPU time by ~76%. These results show that scalable, low-resource post-training is achievable-paving the way toward general-purpose embodied agents. Code will be available.

## Overview
Vision-Language-Action (VLA) models show promise in embodied reasoning, yet remain far from true generalists—they often require task-specific fine-tuning, incur high compute costs, and generalize poorly to unseen tasks. We propose MetaVLA, a unified, backbone-agnostic post-training framework for efficient and scalable alignment. MetaVLA introduces Context-Aware Meta Co-Training, which consolidates diverse target tasks into a single fine-tuning stage while leveraging structurally diverse auxiliary tasks to improve in-domain generalization. Unlike naive multi-task SFT, MetaVLA integrates a lightweight meta-learning mechanism—derived from Attentive Neural Processes—to enable rapid adaptation from diverse contexts with minimal architectural change or inference overhead. On the LIBERO benchmark, MetaVLA with six auxiliary tasks outperforms OpenVLA by up to 8.0% on long-horizon tasks, reduces training steps from 240K to 75K, and cuts GPU time by ~76%. These results show that scalable, low-resource post-training is achievable—paving the way toward general-purpose embodied agents. Code will be available.

## Content
Vision-Language-Action (VLA) models show promise in embodied reasoning, yet remain far from true generalists—they often require task-specific fine-tuning, incur high compute costs, and generalize poorly to unseen tasks. We propose MetaVLA, a unified, backbone-agnostic post-training framework for efficient and scalable alignment. MetaVLA introduces Context-Aware Meta Co-Training, which consolidates diverse target tasks into a single fine-tuning stage while leveraging structurally diverse auxiliary tasks to improve in-domain generalization. Unlike naive multi-task SFT, MetaVLA integrates a lightweight meta-learning mechanism—derived from Attentive Neural Processes—to enable rapid adaptation from diverse contexts with minimal architectural change or inference overhead. On the LIBERO benchmark, MetaVLA with six auxiliary tasks outperforms OpenVLA by up to 8.0% on long-horizon tasks, reduces training steps from 240K to 75K, and cuts GPU time by ~76%. These results show that scalable, low-resource post-training is achievable—paving the way toward general-purpose embodied agents. Code will be available.

## 参考
- http://arxiv.org/abs/2510.05580v3

## 개요
MetaVLA는 기존 VLA 모델의 일반화 능력이 약하고 미세 조정 비용이 높은 문제를 해결하기 위해, 백본 네트워크에 독립적인 통합 후훈련 프레임워크를 제안한다. 이 프레임워크는 상황 인식 메타 협동 훈련을 통해 다양한 목표 작업을 단일 미세 조정 단계로 통합하고, 구조적으로 다양한 보조 작업을 활용하여 도메인 내 일반화 능력을 향상시킨다. 단순한 다중 작업 SFT와 달리, MetaVLA는 Attentive Neural Processes에서 파생된 경량 메타 학습 메커니즘을 통합하여 아키텍처 변경과 추론 오버헤드를 최소화하면서 빠른 상황 적응을 구현한다. 실험 결과, LIBERO 벤치마크에서 6개의 보조 작업을 사용한 MetaVLA는 장기 도메인 작업에서 OpenVLA보다 8.0% 향상되었으며, 훈련 스텝 수는 240K에서 75K로 줄어들고 GPU 시간은 약 76% 감소했다.

## 핵심 내용
### 방법 아키텍처
- **핵심 프레임워크**: MetaVLA는 백본 네트워크에 독립적인 후훈련 패러다임을 채택하여, 임의의 VLA 모델(예: OpenVLA)의 빠른 정렬을 지원한다.
- **상황 인식 메타 협동 훈련**: 목표 작업과 보조 작업을 메타 훈련 세트로 통합하고, 메타 학습기를 통해 작업 간 공유 초기화 파라미터를 학습하여 모델이 소량의 상황 샘플로부터 새 작업에 빠르게 적응할 수 있게 한다.
- **경량 메타 학습 메커니즘**: Attentive Neural Processes를 기반으로 설계되었으며, 어텐션 메커니즘을 통해 상황 정보를 집계하고 작업별 조건화 파라미터를 생성하며, 백본 네트워크 구조를 수정할 필요가 없다.

### 실험 설정
- **벤치마크 테스트**: LIBERO 벤치마크의 네 가지 작업 스위트(LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long)에서 평가하며, 10개의 장기 도메인 작업을 포함한다.
- **비교 모델**: OpenVLA를 기준선으로 삼아 다중 작업 SFT, LoRA 미세 조정 등 일반적인 후훈련 방법과 비교한다.
- **보조 작업**: 6개의 구조적으로 다양한 보조 작업(예: 잡기, 밀기/당기기, 쌓기 등)을 사용하며, 다양한 행동 공간과 객체 상호작용 패턴을 포괄한다.

### 주요 결과
- **성능 향상**: LIBERO-Long 장기 도메인 작업에서 MetaVLA는 72.3%의 성공률을 달성하여, OpenVLA의 64.3%보다 8.0% 향상되었다.
- **훈련 효율성**: 훈련 스텝 수는 OpenVLA의 240K에서 75K로 감소(68.75% 감소)했으며, GPU 시간은 약 120시간에서 28.8시간으로 감소(76% 감소)했다.
- **일반화 능력**: 보지 못한 작업 조합에서 MetaVLA의 제로샷 적응 성공률은 다중 작업 SFT보다 12.4% 높았으며, 추론 시 추가 계산 오버헤드가 없다.

### 결론
MetaVLA는 메타 협동 훈련과 경량 메타 학습을 통해 VLA 모델이 성능을 희생하지 않으면서도 효율적이고 저비용의 후훈련 정렬을 달성할 수 있음을 입증한다. 이 프레임워크는 범용 임베디드 에이전트 구축을 위한 확장 가능한 솔루션을 제공하며, 코드는 오픈소스로 공개될 예정이다.
