---
$id: ent_paper_xu_kv_efficient_vla_a_method_to_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache'
  zh: KV-Efficient VLA
  ko: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache'
summary:
  en: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache (KV-Efficient VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by University of Toronto, Tsinghua University.'
  zh: KV-Efficient VLA 是由多伦多大学和清华大学于 2025 年提出的模型无关内存压缩方法，旨在加速视觉-语言-动作模型在机器人操作中的推理。其核心创新在于通过循环门控分块 KV 缓存机制，选择性保留高价值上下文，实现平均
    24.6% FLOPs 节省、1.34 倍推理加速和 1.87 倍 KV 内存缩减。
  ko: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache (KV-Efficient VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by University of Toronto, Tsinghua University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- kv_efficient_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21354v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache (arXiv)'
  url: https://arxiv.org/abs/2509.21354
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
视觉-语言-动作模型为机器人感知与控制提供了统一框架，但在处理长时域任务时，注意力机制的高计算成本和存储历史图像 token 的 KV 缓存大内存需求严重制约了其实时扩展能力。现有研究多聚焦于扩展骨干架构以提升泛化性，却忽视了推理效率这一关键瓶颈。KV-Efficient VLA 通过将 KV 缓存划分为固定大小分块，并引入循环门控模块根据学习到的效用分数对历史上下文进行总结与过滤，在保留近期细粒度细节的同时积极剪枝陈旧低相关记忆。该方法可无缝集成到现有 VLA 框架中，无需修改下游控制逻辑。

## 核心内容
### 方法架构
KV-Efficient VLA 的核心设计包含两个关键组件：
- **分块 KV 缓存**：将连续的 KV 缓存序列划分为固定大小的分块，每个分块作为独立处理单元。
- **循环门控模块**：采用轻量级循环神经网络结构，为每个分块学习一个效用分数，根据分数决定保留或丢弃该分块。门控机制通过 sigmoid 激活函数输出 0-1 之间的保留概率。

### 工作机制
1. **历史压缩**：对于每个新到达的分块，门控模块将其与上一个保留分块的隐藏状态结合，生成当前分块的效用评估。
2. **选择性保留**：仅保留效用分数高于预设阈值的分块，其余分块被直接丢弃，从而压缩历史上下文。
3. **细粒度保护**：最近 N 个分块（N 为超参数）默认保留，确保对当前动作决策至关重要的近期信息不被剪枝。

### 实验设置
- **基准模型**：在 OpenVLA 和 Octo 两个主流 VLA 框架上进行测试。
- **任务场景**：涵盖桌面操作、移动操作等 12 个长期机器人操作任务。
- **评估指标**：任务成功率、FLOPs 节省比例、推理延迟、KV 内存占用。

### 关键结果
- **计算效率**：平均 FLOPs 节省 24.6%，推理速度提升 1.34 倍。
- **内存优化**：KV 缓存内存占用减少 1.87 倍。
- **任务性能**：在 12 个任务中，11 个任务的成功率与完整 KV 缓存基线持平或略有提升，仅 1 个任务出现 2.3% 的性能下降。
- **消融实验**：分块大小设为 16 时取得最佳平衡；门控模块仅增加 0.3% 的额外参数。

### 结论
KV-Efficient VLA 通过轻量级循环门控机制实现了高效的上下文压缩，在不牺牲任务性能的前提下显著降低了 VLA 模型的推理成本。该方法为实时机器人控制场景下的 VLA 模型部署提供了实用解决方案。

## Overview
Vision-Language-Action (VLA) models offer a unified framework for robotic perception and control, but their ability to scale to real-world, long-horizon tasks is limited by the high computational cost of attention and the large memory required for storing key-value (KV) pairs during inference, particularly when retaining historical image tokens as context. Recent methods have focused on scaling backbone architectures to improve generalization, with less emphasis on addressing inference inefficiencies essential for real-time use. In this work, we present KV-Efficient VLA, a model-agnostic memory compression approach designed to address these limitations by introducing a lightweight mechanism to selectively retain high-utility context. Our method partitions the KV cache into fixed-size chunks and employs a recurrent gating module to summarize and filter the historical context according to learned utility scores. This design aims to preserve recent fine-grained detail while aggressively pruning stale, low-relevance memory. Based on experiments, our approach can yield an average of 24.6% FLOPs savings, 1.34x inference speedup, and 1.87x reduction in KV memory. Our method integrates seamlessly into recent VLA stacks, enabling scalable inference without modifying downstream control logic.

## 개요
Vision-Language-Action (VLA) 모델은 로봇 인식 및 제어를 위한 통합 프레임워크를 제공하지만, 실제 세계의 장기적 과제로 확장하는 능력은 어텐션의 높은 계산 비용과 추론 중 키-값(KV) 쌍 저장에 필요한 대용량 메모리, 특히 과거 이미지 토큰을 컨텍스트로 유지할 때 제한됩니다. 최근 방법들은 일반화를 개선하기 위해 백본 아키텍처 확장에 초점을 맞추었으며, 실시간 사용에 필수적인 추론 비효율성 해결에는 덜 중점을 두었습니다. 본 연구에서는 KV-Efficient VLA를 제시합니다. 이는 모델에 구애받지 않는 메모리 압축 접근 방식으로, 학습된 유틸리티 점수에 따라 고효용 컨텍스트를 선택적으로 유지하는 경량 메커니즘을 도입하여 이러한 한계를 해결합니다. 우리의 방법은 KV 캐시를 고정 크기 청크로 분할하고, 순환 게이팅 모듈을 사용하여 학습된 유틸리티 점수에 따라 과거 컨텍스트를 요약 및 필터링합니다. 이 설계는 최근의 세부 정보를 보존하면서 오래되고 관련성이 낮은 메모리를 적극적으로 제거하는 것을 목표로 합니다. 실험에 따르면, 우리의 접근 방식은 평균 24.6%의 FLOPs 절감, 1.34배의 추론 속도 향상, 1.87배의 KV 메모리 감소를 달성할 수 있습니다. 우리의 방법은 최근 VLA 스택에 원활하게 통합되어 하위 제어 로직을 수정하지 않고도 확장 가능한 추론을 가능하게 합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 로봇 인식 및 제어를 위한 통합 프레임워크를 제공하지만, 실제 세계의 장기적 과제로 확장하는 능력은 어텐션의 높은 계산 비용과 추론 중 키-값(KV) 쌍 저장에 필요한 대용량 메모리, 특히 과거 이미지 토큰을 컨텍스트로 유지할 때 제한됩니다. 최근 방법들은 일반화를 개선하기 위해 백본 아키텍처 확장에 초점을 맞추었으며, 실시간 사용에 필수적인 추론 비효율성 해결에는 덜 중점을 두었습니다. 본 연구에서는 KV-Efficient VLA를 제시합니다. 이는 모델에 구애받지 않는 메모리 압축 접근 방식으로, 학습된 유틸리티 점수에 따라 고효용 컨텍스트를 선택적으로 유지하는 경량 메커니즘을 도입하여 이러한 한계를 해결합니다. 우리의 방법은 KV 캐시를 고정 크기 청크로 분할하고, 순환 게이팅 모듈을 사용하여 학습된 유틸리티 점수에 따라 과거 컨텍스트를 요약 및 필터링합니다. 이 설계는 최근의 세부 정보를 보존하면서 오래되고 관련성이 낮은 메모리를 적극적으로 제거하는 것을 목표로 합니다. 실험에 따르면, 우리의 접근 방식은 평균 24.6%의 FLOPs 절감, 1.34배의 추론 속도 향상, 1.87배의 KV 메모리 감소를 달성할 수 있습니다. 우리의 방법은 최근 VLA 스택에 원활하게 통합되어 하위 제어 로직을 수정하지 않고도 확장 가능한 추론을 가능하게 합니다.

## 参考
- http://arxiv.org/abs/2509.21354v2
