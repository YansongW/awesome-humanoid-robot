---
$id: ent_paper_yang_efficientvla_training_free_acc_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models'
  zh: EfficientVLA
  ko: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models'
summary:
  en: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models (EfficientVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, Shanghai
    Jiao Tong University, Harbin Institute of Technology, Xi’an Jiaotong University, University of Electronic Science and
    Technology of China, Anyverse Intelligence, and published at NIPS25.'
  zh: EfficientVLA 是由上海交通大学、哈尔滨工业大学、西安交通大学、电子科技大学及 Anyverse Intelligence 联合提出的训练无关推理加速框架，发表于 NIPS25。该框架通过协同利用语言模块剪枝、视觉令牌优化和扩散动作头特征缓存三种策略，在不需重新训练的情况下显著降低
    VLA 模型的计算与内存开销。在 CogACT 模型上应用后，实现了 1.93 倍推理加速，FLOPs 降至 28.9%，而 SIMPLER 基准的成功率仅下降 0.6%。
  ko: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models (EfficientVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, Shanghai
    Jiao Tong University, Harbin Institute of Technology, Xi’an Jiaotong University, University of Electronic Science and
    Technology of China, Anyverse Intelligence, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- efficientvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.10100v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2506.10100
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EfficientVLA source
  url: https://doi.org/10.48550/arXiv.2506.10100
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
EfficientVLA 针对视觉-语言-动作模型（尤其是扩散架构）在具身智能应用中面临的高计算与内存冗余问题，提出了一种无需训练的系统性加速方案。现有方法通常只解决单一瓶颈，而 EfficientVLA 通过三种协同策略全面消除冗余：首先，基于层间冗余分析剪除语言模块中功能无关的层；其次，采用任务感知策略选择紧凑且多样化的视觉令牌，平衡任务关键性与信息覆盖；最后，在迭代扩散动作头中缓存并复用关键中间特征以减少时间计算冗余。该方法在 CogACT 模型上验证，显著提升了推理效率，同时保持了极低的性能损失。

## 核心内容
### 方法架构
EfficientVLA 的核心在于无需额外训练即可系统性消除 VLA 模型中的多重冗余，具体包含三个协同模块：

- **语言模块剪枝**：通过分析 Transformer 层间的冗余度，识别并移除功能无关的层，从而减少计算和内存占用，而不影响模型的语言理解能力。
- **视觉路径优化**：采用任务感知策略，从视觉编码器输出中选择一组紧凑且多样化的视觉令牌。该策略通过平衡任务关键性（如目标物体的位置）与信息覆盖度（如场景全局特征），减少视觉令牌数量，降低后续处理的复杂度。
- **扩散动作头加速**：针对扩散模型迭代去噪过程中的时间计算冗余，设计中间特征缓存与复用机制。在连续时间步中，缓存关键层的中间表示，并在后续步骤中直接复用，避免重复计算。

### 实验设置与关键结果
- **基础模型**：以 CogACT 为标准 VLA 模型进行测试。
- **基准测试**：在 SIMPLER 基准上评估，涵盖多种机器人操作任务。
- **性能指标**：
  - 推理速度提升 1.93 倍。
  - FLOPs 降至原始模型的 28.9%。
  - 成功率仅下降 0.6%，表明加速方案对任务性能影响极小。

### 结论
EfficientVLA 通过训练无关的协同加速策略，有效解决了 VLA 模型在部署中的计算与内存瓶颈，为具身智能系统的实时应用提供了可行方案。其模块化设计可适配不同 VLA 架构，未来可进一步探索与模型量化、知识蒸馏等技术的结合。

## Overview
Vision-Language-Action (VLA) models, particularly diffusion-based architectures, demonstrate transformative potential for embodied intelligence but are severely hampered by high computational and memory demands stemming from extensive inherent and inference-time redundancies. While existing acceleration efforts often target isolated inefficiencies, such piecemeal solutions typically fail to holistically address the varied computational and memory bottlenecks across the entire VLA pipeline, thereby limiting practical deployability. We introduce EfficientVLA, a structured and training-free inference acceleration framework that systematically eliminates these barriers by cohesively exploiting multifaceted redundancies. EfficientVLA synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features. We apply our method to a standard VLA model CogACT, yielding a 1.93X inference speedup and reduces FLOPs to 28.9%, with only a 0.6% success rate drop in the SIMPLER benchmark.

## 개요
Vision-Language-Action (VLA) 모델, 특히 확산 기반 아키텍처는 구현된 지능에 혁신적인 잠재력을 보여주지만, 광범위한 고유 및 추론 시간 중복성으로 인한 높은 계산 및 메모리 요구 사항으로 인해 심각한 제약을 받습니다. 기존의 가속화 노력은 종종 고립된 비효율성을 대상으로 하지만, 이러한 부분적 솔루션은 일반적으로 전체 VLA 파이프라인 전반의 다양한 계산 및 메모리 병목 현상을 전체적으로 해결하지 못하여 실제 배포 가능성을 제한합니다. 우리는 구조화되고 훈련이 필요 없는 추론 가속화 프레임워크인 EfficientVLA를 소개합니다. 이는 다각적인 중복성을 응집력 있게 활용하여 이러한 장벽을 체계적으로 제거합니다. EfficientVLA는 세 가지 목표 전략을 시너지적으로 통합합니다: (1) 계층 간 중복성 분석에 기반한 언어 모듈의 기능적으로 중요하지 않은 계층 제거; (2) 작업 인식 전략을 통해 시각적 처리 경로를 최적화하여 작업 중요성과 정보 범위의 균형을 맞춘 간결하고 다양한 시각적 토큰 세트 선택; (3) 반복적 확산 기반 행동 헤드의 시간적 계산 중복성을 주요 중간 특징을 전략적으로 캐싱 및 재사용하여 완화. 우리는 이 방법을 표준 VLA 모델인 CogACT에 적용하여 1.93배의 추론 속도 향상과 FLOPs를 28.9%로 줄였으며, SIMPLER 벤치마크에서 성공률이 0.6%만 감소했습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델, 특히 확산 기반 아키텍처는 구현된 지능에 혁신적인 잠재력을 보여주지만, 광범위한 고유 및 추론 시간 중복성으로 인한 높은 계산 및 메모리 요구 사항으로 인해 심각한 제약을 받습니다. 기존의 가속화 노력은 종종 고립된 비효율성을 대상으로 하지만, 이러한 부분적 솔루션은 일반적으로 전체 VLA 파이프라인 전반의 다양한 계산 및 메모리 병목 현상을 전체적으로 해결하지 못하여 실제 배포 가능성을 제한합니다. 우리는 구조화되고 훈련이 필요 없는 추론 가속화 프레임워크인 EfficientVLA를 소개합니다. 이는 다각적인 중복성을 응집력 있게 활용하여 이러한 장벽을 체계적으로 제거합니다. EfficientVLA는 세 가지 목표 전략을 시너지적으로 통합합니다: (1) 계층 간 중복성 분석에 기반한 언어 모듈의 기능적으로 중요하지 않은 계층 제거; (2) 작업 인식 전략을 통해 시각적 처리 경로를 최적화하여 작업 중요성과 정보 범위의 균형을 맞춘 간결하고 다양한 시각적 토큰 세트 선택; (3) 반복적 확산 기반 행동 헤드의 시간적 계산 중복성을 주요 중간 특징을 전략적으로 캐싱 및 재사용하여 완화. 우리는 이 방법을 표준 VLA 모델인 CogACT에 적용하여 1.93배의 추론 속도 향상과 FLOPs를 28.9%로 줄였으며, SIMPLER 벤치마크에서 성공률이 0.6%만 감소했습니다.

## 参考
- http://arxiv.org/abs/2506.10100v1
