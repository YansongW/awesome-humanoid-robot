---
$id: ent_paper_xu_vla_cache_efficient_vision_lan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching'
  zh: VLA-Cache
  ko: 'VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching'
summary:
  en: 'VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching (VLA-Cache), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Sydney, Shanghai Jiao Tong University, and published at NIPS25.'
  zh: VLA-Cache 是由悉尼大学和上海交通大学于 2025 年提出的训练无关推理加速方法，旨在提升视觉-语言-动作模型在机器人操控中的实时性。其核心贡献是通过自适应缓存与复用帧间静态视觉 token，在 LIBERO 和 SIMPLER
    仿真平台及真实机器人系统上实现最高 1.7 倍 CUDA 延迟加速和 15% 控制频率提升，且任务成功率几乎无损。
  ko: 'VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching (VLA-Cache), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Sydney, Shanghai Jiao Tong University, and published at NIPS25.'
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
- vision_language_action
- vla
- vla_cache
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.02175v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (884 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching (arXiv)'
  url: https://arxiv.org/abs/2502.02175
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-Cache source
  url: https://doi.org/10.48550/arXiv.2502.02175
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
VLA-Cache 针对 VLA 模型计算开销大、难以满足实时机器人控制需求的问题，提出无需额外训练的推理加速方案。该方法利用机器人操控场景中相邻帧的时序连续性，识别变化极小的视觉 token 并复用其缓存的键值表示，从而避免冗余计算。同时，为保持动作精度，VLA-Cache 选择性地重新计算对环境敏感的任务相关 token，并引入层自适应 token 复用策略，根据解码器各层的注意力集中程度动态调整复用比例。实验在 LIBERO 和 SIMPLER 两个仿真平台及真实机器人系统上验证，结果显示该方法在显著提升速度的同时，任务成功率几乎不受影响。

## 核心内容
### 方法架构
VLA-Cache 的核心设计围绕三个关键机制展开：
- **自适应 token 缓存与复用**：基于相邻帧间视觉 token 的变化幅度，识别出变化极小的静态 token，直接复用其缓存的键值表示，跳过重复计算。
- **选择性重新计算**：对与环境交互密切、影响动作精度的任务相关 token，VLA-Cache 会重新计算其表示，确保关键视觉信息的保真度。
- **层自适应 token 复用策略**：根据解码器各层注意力分布的集中程度，动态调整 token 复用比例，优先将计算资源分配给关键 token 的重新计算。

### 实验设置与结果
- **仿真平台**：在 LIBERO 和 SIMPLER 两个基准上进行评估，涵盖多种操控任务。
- **真实机器人系统**：部署于实际机器人平台，验证方法的泛化能力。
- **关键性能指标**：
  - CUDA 延迟最高加速 1.7 倍。
  - 控制频率提升 15%。
  - 任务成功率几乎无下降，表明加速未显著牺牲动作精度。
- **代码与视频**：项目页面提供完整代码和演示视频：https://vla-cache.github.io。

### 结论
VLA-Cache 通过训练无关的推理加速策略，有效解决了 VLA 模型在实时机器人控制中的计算瓶颈，为高频率、低延迟的操控任务提供了可行方案。

## Overview
Vision-Language-Action (VLA) models have demonstrated strong multi-modal reasoning capabilities, enabling direct action generation from visual perception and language instructions in an end-to-end manner. However, their substantial computational cost poses a challenge for real-time robotic control, where rapid decision-making is essential. This paper introduces VLA-Cache, a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames. Exploiting the temporal continuity in robotic manipulation, VLA-Cache identifies minimally changed tokens between adjacent frames and reuses their cached key-value representations, thereby circumventing redundant computations. Additionally, to maintain action precision, VLA-Cache selectively re-computes task-relevant tokens that are environmentally sensitive, ensuring the fidelity of critical visual information. To further optimize efficiency, we introduce a layer adaptive token reusing strategy that dynamically adjusts the reuse ratio based on attention concentration across decoder layers, prioritizing critical tokens for recomputation. Extensive experiments on two simulation platforms (LIBERO and SIMPLER) and a real-world robotic system demonstrate that VLA-Cache achieves up to 1.7x speedup in CUDA latency and a 15% increase in control frequency, with negligible loss on task success rate. The code and videos can be found at our project page: https://vla-cache.github.io.

## 参考
- http://arxiv.org/abs/2502.02175v2

## 개요
VLA-Cache는 VLA 모델의 높은 계산 비용과 실시간 로봇 제어 요구를 충족하기 어려운 문제를 해결하기 위해, 추가 훈련이 필요 없는 추론 가속화 방안을 제안한다. 이 방법은 로봇 조작 시나리오에서 인접 프레임 간의 시간적 연속성을 활용하여 변화가 극히 적은 시각적 토큰을 식별하고, 해당 토큰의 캐시된 키-값 표현을 재사용함으로써 중복 계산을 방지한다. 동시에 동작 정밀도를 유지하기 위해, VLA-Cache는 환경에 민감한 작업 관련 토큰을 선택적으로 재계산하며, 디코더 각 층의 주의 집중 정도에 따라 재사용 비율을 동적으로 조정하는 층 적응형 토큰 재사용 전략을 도입한다. 실험은 LIBERO와 SIMPLER 두 시뮬레이션 플랫폼 및 실제 로봇 시스템에서 검증되었으며, 결과는 이 방법이 속도를 크게 향상시키면서도 작업 성공률은 거의 영향을 받지 않음을 보여준다.

## 핵심 내용
### 방법 아키텍처
VLA-Cache의 핵심 설계는 세 가지 주요 메커니즘을 중심으로 구성된다:
- **적응형 토큰 캐싱 및 재사용**: 인접 프레임 간 시각적 토큰의 변화 폭을 기반으로 변화가 극히 적은 정적 토큰을 식별하고, 해당 토큰의 캐시된 키-값 표현을 직접 재사용하여 중복 계산을 건너뛴다.
- **선택적 재계산**: 환경과 밀접하게 상호작용하고 동작 정밀도에 영향을 미치는 작업 관련 토큰에 대해, VLA-Cache는 해당 토큰의 표현을 재계산하여 핵심 시각 정보의 충실도를 보장한다.
- **층 적응형 토큰 재사용 전략**: 디코더 각 층의 주의 분포 집중 정도에 따라 토큰 재사용 비율을 동적으로 조정하며, 계산 자원을 핵심 토큰의 재계산에 우선적으로 할당한다.

### 실험 설정 및 결과
- **시뮬레이션 플랫폼**: LIBERO와 SIMPLER 두 벤치마크에서 평가를 수행하며, 다양한 조작 작업을 포함한다.
- **실제 로봇 시스템**: 실제 로봇 플랫폼에 배포하여 방법의 일반화 능력을 검증한다.
- **주요 성능 지표**:
  - CUDA 지연 시간 최대 1.7배 가속.
  - 제어 주파수 15% 향상.
  - 작업 성공률은 거의 감소하지 않아, 가속이 동작 정밀도를 크게 희생하지 않았음을 나타낸다.
- **코드 및 비디오**: 프로젝트 페이지에서 전체 코드와 데모 비디오를 제공한다: https://vla-cache.github.io.

### 결론
VLA-Cache는 훈련과 무관한 추론 가속화 전략을 통해 VLA 모델의 실시간 로봇 제어에서의 계산 병목을 효과적으로 해결하며, 고주파수·저지연 조작 작업에 실현 가능한 방안을 제공한다.
