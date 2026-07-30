---
$id: ent_paper_wang_unified_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Vision-Language-Action Model
  zh: UniVLA
  ko: Unified Vision-Language-Action Model
summary:
  en: Unified Vision-Language-Action Model (UniVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by CASIA, BAAI, THU, HKISI.
  zh: UniVLA 是由中国科学院自动化研究所、北京智源人工智能研究院、清华大学和香港科技大学（深圳）联合提出的 2025 年大型视觉-语言-动作模型。其核心贡献在于将视觉、语言和动作信号统一建模为离散 token 序列，并通过后训练中的世界建模捕获视频中的因果动态，从而显著提升机器人操作性能。该模型在
    CALVIN、LIBERO 等模拟基准上达到新 SOTA，例如在 LIBERO 上平均成功率 95.5%，远超 pi0-FAST 的 85.5%。
  ko: Unified Vision-Language-Action Model (UniVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by CASIA, BAAI, THU, HKISI.
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
- robotic_manipulation
- univla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.19850v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Unified Vision-Language-Action Model (arXiv)
  url: https://arxiv.org/abs/2506.19850
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UniVLA source
  url: https://dblp.org/rec/journals/corr/abs-2506-19850
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
UniVLA 是一种统一原生多模态 VLA 模型，它通过自回归方式将视觉、语言和动作信号处理为离散 token 序列，突破了以往 VLA 模型仅依赖 VLM 通用理解能力的局限。这种设计使模型能够灵活学习多模态任务，尤其擅长从大规模视频数据中提取信息。在后训练阶段，UniVLA 引入世界建模，从视频中学习因果动力学，从而有效迁移到下游策略学习，特别适用于长时域任务。实验表明，UniVLA 在多个模拟基准上大幅超越先前方法，并在真实世界的 ALOHA 操作和自动驾驶场景中展示了广泛适用性。

## 核心内容
### 方法架构
UniVLA 的核心创新在于将视觉、语言和动作信号统一表示为离散 token 序列，并通过自回归方式建模。这种统一表示使得模型能够同时处理多种模态，尤其擅长从大规模视频数据中学习。后训练阶段引入的世界建模机制，使模型能够从视频中捕获因果动态，从而有效支持长时域任务的策略学习。

### 实验设置与关键结果
- **模拟基准测试**：UniVLA 在 CALVIN、LIBERO 和 Simplenv-Bridge 等广泛使用的模拟基准上取得了新 SOTA 结果。例如，在 LIBERO 基准上，UniVLA 的平均成功率达到 95.5%，显著超越 pi0-FAST 的 85.5%。
- **真实世界应用**：模型在真实世界的 ALOHA 操作和自动驾驶场景中展示了广泛适用性，验证了其跨领域迁移能力。

### 结论
UniVLA 通过统一多模态 token 序列建模和世界学习机制，有效解决了以往 VLA 模型忽略视觉观测中时间与因果结构的问题，在模拟和真实场景中均实现了显著性能提升。

## Overview
Vision-language-action models (VLAs) have garnered significant attention for their potential in advancing robotic manipulation. However, previous approaches predominantly rely on the general comprehension capabilities of vision-language models (VLMs) to generate action signals, often overlooking the rich temporal and causal structure embedded in visual observations. In this paper, we present UniVLA, a unified and native multimodal VLA model that autoregressively models vision, language, and action signals as discrete token sequences. This formulation enables flexible multimodal tasks learning, particularly from large-scale video data. By incorporating world modeling during post-training, UniVLA captures causal dynamics from videos, facilitating effective transfer to downstream policy learning--especially for long-horizon tasks. Our approach sets new state-of-the-art results across several widely used simulation benchmarks, including CALVIN, LIBERO, and Simplenv-Bridge, significantly surpassing previous methods. For example, UniVLA achieves 95.5% average success rate on LIBERO benchmark, surpassing pi0-FAST's 85.5%. We further demonstrate its broad applicability on real-world ALOHA manipulation and autonomous driving.

## 개요
Vision-language-action models (VLAs)는 로봇 조작 분야의 발전 가능성으로 인해 큰 주목을 받아왔습니다. 그러나 기존 접근법들은 주로 vision-language models (VLMs)의 일반적인 이해 능력에 의존하여 행동 신호를 생성하며, 시각적 관찰에 내재된 풍부한 시간적 및 인과적 구조를 간과하는 경우가 많았습니다. 본 논문에서는 UniVLA를 제안합니다. 이는 시각, 언어, 행동 신호를 이산 토큰 시퀀스로 자기회귀적으로 모델링하는 통합적이고 본질적인 멀티모달 VLA 모델입니다. 이러한 구성은 특히 대규모 비디오 데이터를 활용한 유연한 멀티모달 작업 학습을 가능하게 합니다. 사후 훈련 과정에서 세계 모델링을 통합함으로써, UniVLA는 비디오로부터 인과적 역학을 포착하여 다운스트림 정책 학습, 특히 장기적 작업에 효과적으로 전이할 수 있도록 합니다. 우리의 접근법은 CALVIN, LIBERO, Simplenv-Bridge를 포함한 여러 널리 사용되는 시뮬레이션 벤치마크에서 새로운 최첨단 결과를 달성하며, 이전 방법들을 크게 능가합니다. 예를 들어, UniVLA는 LIBERO 벤치마크에서 평균 95.5%의 성공률을 기록하여 pi0-FAST의 85.5%를 넘어섰습니다. 또한 실제 세계의 ALOHA 조작 및 자율 주행에서의 광범위한 적용 가능성을 입증합니다.

## 핵심 내용
Vision-language-action models (VLAs)는 로봇 조작 분야의 발전 가능성으로 인해 큰 주목을 받아왔습니다. 그러나 기존 접근법들은 주로 vision-language models (VLMs)의 일반적인 이해 능력에 의존하여 행동 신호를 생성하며, 시각적 관찰에 내재된 풍부한 시간적 및 인과적 구조를 간과하는 경우가 많았습니다. 본 논문에서는 UniVLA를 제안합니다. 이는 시각, 언어, 행동 신호를 이산 토큰 시퀀스로 자기회귀적으로 모델링하는 통합적이고 본질적인 멀티모달 VLA 모델입니다. 이러한 구성은 특히 대규모 비디오 데이터를 활용한 유연한 멀티모달 작업 학습을 가능하게 합니다. 사후 훈련 과정에서 세계 모델링을 통합함으로써, UniVLA는 비디오로부터 인과적 역학을 포착하여 다운스트림 정책 학습, 특히 장기적 작업에 효과적으로 전이할 수 있도록 합니다. 우리의 접근법은 CALVIN, LIBERO, Simplenv-Bridge를 포함한 여러 널리 사용되는 시뮬레이션 벤치마크에서 새로운 최첨단 결과를 달성하며, 이전 방법들을 크게 능가합니다. 예를 들어, UniVLA는 LIBERO 벤치마크에서 평균 95.5%의 성공률을 기록하여 pi0-FAST의 85.5%를 넘어섰습니다. 또한 실제 세계의 ALOHA 조작 및 자율 주행에서의 광범위한 적용 가능성을 입증합니다.

## 参考
- http://arxiv.org/abs/2506.19850v1
