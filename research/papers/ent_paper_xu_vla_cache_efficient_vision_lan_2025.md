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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.02175v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Vision-Language-Action (VLA) 모델은 강력한 다중 모달 추론 능력을 입증하며, 시각적 인식과 언어 명령으로부터 종단 간 방식으로 직접 행동을 생성할 수 있게 합니다. 그러나 이들의 상당한 계산 비용은 빠른 의사 결정이 필수적인 실시간 로봇 제어에 도전 과제를 제기합니다. 본 논문은 VLA-Cache를 소개합니다. 이는 학습 없이 추론 가속화를 제공하는 방법으로, 프레임 간 정적 시각적 토큰을 적응적으로 캐싱하고 재사용하여 계산 오버헤드를 줄입니다. 로봇 조작의 시간적 연속성을 활용하여, VLA-Cache는 인접 프레임 간 변화가 최소인 토큰을 식별하고 이들의 캐시된 키-값 표현을 재사용함으로써 중복 계산을 회피합니다. 또한, 행동 정밀도를 유지하기 위해 VLA-Cache는 환경에 민감한 작업 관련 토큰을 선택적으로 재계산하여 중요한 시각 정보의 충실도를 보장합니다. 효율성을 더욱 최적화하기 위해, 우리는 디코더 레이어 간 주의 집중도에 따라 재사용 비율을 동적으로 조정하고 중요한 토큰을 재계산에 우선시하는 레이어 적응형 토큰 재사용 전략을 도입합니다. 두 시뮬레이션 플랫폼(LIBERO 및 SIMPLER)과 실제 로봇 시스템에서의 광범위한 실험을 통해 VLA-Cache가 CUDA 지연 시간에서 최대 1.7배 속도 향상과 제어 주파수에서 15% 증가를 달성하며, 작업 성공률에서 무시할 수 있는 손실을 보임을 입증합니다. 코드와 비디오는 프로젝트 페이지(https://vla-cache.github.io)에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 강력한 다중 모달 추론 능력을 입증하며, 시각적 인식과 언어 명령으로부터 종단 간 방식으로 직접 행동을 생성할 수 있게 합니다. 그러나 이들의 상당한 계산 비용은 빠른 의사 결정이 필수적인 실시간 로봇 제어에 도전 과제를 제기합니다. 본 논문은 VLA-Cache를 소개합니다. 이는 학습 없이 추론 가속화를 제공하는 방법으로, 프레임 간 정적 시각적 토큰을 적응적으로 캐싱하고 재사용하여 계산 오버헤드를 줄입니다. 로봇 조작의 시간적 연속성을 활용하여, VLA-Cache는 인접 프레임 간 변화가 최소인 토큰을 식별하고 이들의 캐시된 키-값 표현을 재사용함으로써 중복 계산을 회피합니다. 또한, 행동 정밀도를 유지하기 위해 VLA-Cache는 환경에 민감한 작업 관련 토큰을 선택적으로 재계산하여 중요한 시각 정보의 충실도를 보장합니다. 효율성을 더욱 최적화하기 위해, 우리는 디코더 레이어 간 주의 집중도에 따라 재사용 비율을 동적으로 조정하고 중요한 토큰을 재계산에 우선시하는 레이어 적응형 토큰 재사용 전략을 도입합니다. 두 시뮬레이션 플랫폼(LIBERO 및 SIMPLER)과 실제 로봇 시스템에서의 광범위한 실험을 통해 VLA-Cache가 CUDA 지연 시간에서 최대 1.7배 속도 향상과 제어 주파수에서 15% 증가를 달성하며, 작업 성공률에서 무시할 수 있는 손실을 보임을 입증합니다. 코드와 비디오는 프로젝트 페이지(https://vla-cache.github.io)에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2502.02175v2
