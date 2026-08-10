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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.10100v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (912 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2506.10100v1

## 개요
EfficientVLA는 시각-언어-행동 모델(특히 확산 아키텍처)이 구현 지능 애플리케이션에서 직면하는 높은 계산 및 메모리 중복 문제를 해결하기 위해, 훈련이 필요 없는 체계적인 가속화 방안을 제안합니다. 기존 방법은 일반적으로 단일 병목 현상만 해결하는 반면, EfficientVLA는 세 가지 협력 전략을 통해 중복을 전면적으로 제거합니다: 첫째, 계층 간 중복 분석을 기반으로 언어 모듈에서 기능과 무관한 계층을 제거합니다; 둘째, 작업 인식 전략을 채택하여 작업 핵심성과 정보 범위를 균형 있게 맞추는 컴팩트하고 다양한 시각 토큰을 선택합니다; 마지막으로, 반복 확산 동작 헤드에서 핵심 중간 특징을 캐시하고 재사용하여 시간 계산 중복을 줄입니다. 이 방법은 CogACT 모델에서 검증되었으며, 추론 효율성을 크게 향상시키면서도 매우 낮은 성능 손실을 유지합니다.

## 핵심 내용
### 방법 아키텍처
EfficientVLA의 핵심은 추가 훈련 없이 VLA 모델의 다중 중복을 체계적으로 제거하는 데 있으며, 구체적으로 세 가지 협력 모듈을 포함합니다:

- **언어 모듈 가지치기**: Transformer 계층 간의 중복도를 분석하여 기능과 무관한 계층을 식별하고 제거함으로써, 모델의 언어 이해 능력에 영향을 주지 않으면서 계산 및 메모리 사용량을 줄입니다.
- **시각 경로 최적화**: 작업 인식 전략을 채택하여 시각 인코더 출력에서 컴팩트하고 다양한 시각 토큰 세트를 선택합니다. 이 전략은 작업 핵심성(예: 대상 객체의 위치)과 정보 범위(예: 장면 전역 특징)를 균형 있게 맞춰 시각 토큰 수를 줄이고 후속 처리의 복잡성을 낮춥니다.
- **확산 동작 헤드 가속화**: 확산 모델의 반복 잡음 제거 과정에서 발생하는 시간 계산 중복을 해결하기 위해 중간 특징 캐시 및 재사용 메커니즘을 설계합니다. 연속 시간 단계에서 핵심 계층의 중간 표현을 캐시하고 후속 단계에서 직접 재사용하여 중복 계산을 방지합니다.

### 실험 설정 및 주요 결과
- **기본 모델**: CogACT를 표준 VLA 모델로 테스트했습니다.
- **벤치마크 테스트**: SIMPLER 벤치마크에서 평가했으며, 다양한 로봇 조작 작업을 포함합니다.
- **성능 지표**:
  - 추론 속도 1.93배 향상.
  - FLOPs가 원래 모델의 28.9%로 감소.
  - 성공률은 0.6%만 하락하여, 가속화 방안이 작업 성능에 미치는 영향이 매우 적음을 나타냅니다.

### 결론
EfficientVLA는 훈련과 무관한 협력 가속화 전략을 통해 VLA 모델 배포 시의 계산 및 메모리 병목 문제를 효과적으로 해결하며, 구현 지능 시스템의 실시간 애플리케이션에 실현 가능한 방안을 제공합니다. 모듈식 설계는 다양한 VLA 아키텍처에 적용할 수 있으며, 향후 모델 양자화, 지식 증류 등의 기술과의 결합을 더 탐구할 수 있습니다.
