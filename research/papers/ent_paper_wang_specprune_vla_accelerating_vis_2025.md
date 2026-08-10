---
$id: ent_paper_wang_specprune_vla_accelerating_vis_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning'
  zh: SpecPrune-VLA
  ko: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning'
summary:
  en: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (SpecPrune-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Infinigence-AI,
    SII.'
  zh: SpecPrune-VLA 是由上海交通大学、Infinigence-AI 和 SII 于 2025 年提出的免训练加速方法，用于视觉-语言-动作模型（VLA）的机器人操作任务。其核心贡献在于提出动作感知的自推测剪枝策略，通过结合局部与全局上下文实现最高
    1.70 倍加速，且成功率几乎无下降。
  ko: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (SpecPrune-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Infinigence-AI,
    SII.'
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
- specprune_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.05614v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (861 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (arXiv)'
  url: https://arxiv.org/abs/2509.05614
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SpecPrune-VLA source
  url: https://doi.org/10.48550/arXiv.2509.05614
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 模型加速方法仅关注当前动作步骤的局部信息，忽略全局上下文，导致成功率下降超 20% 且加速效果有限。SpecPrune-VLA 基于 VLA 任务中连续步骤图像高度相似的空间-时间一致性，提出免训练的两级剪枝方法：动作级静态剪枝利用全局历史与局部注意力减少每动作的视觉 token，层级动态剪枝根据各层重要性自适应移除 token，轻量级动作感知控制器则依据末端执行器速度将动作分为粗粒度与细粒度并调整剪枝强度。实验表明，该方法在 LIBERO 仿真中实现 1.57 倍加速，在真实任务中达 1.70 倍，且成功率几乎无损失。

## 核心内容
### 方法架构
SpecPrune-VLA 包含三个核心组件：
- **动作级静态剪枝**：利用全局历史注意力与局部注意力，在每动作步骤中静态减少视觉 token 数量，保留与任务最相关的图像区域。
- **层级动态剪枝**：根据每层 Transformer 的注意力重要性得分，自适应地移除冗余 token，避免固定剪枝率导致的性能损失。
- **动作感知控制器**：通过末端执行器速度将动作分类为粗粒度（快速移动）与细粒度（精细操作），对粗粒度动作采用更激进的剪枝策略，细粒度动作则保留更多 token 以保证精度。

### 实验设置与关键数字
- **仿真环境**：LIBERO 基准，包含 10 个长时域操作任务。
- **真实场景**：机器人抓取与放置任务，使用 7 自由度机械臂。
- **加速效果**：LIBERO 仿真中达到 1.57 倍加速，真实任务中达 1.70 倍。
- **成功率**：相比未剪枝基线，成功率下降小于 1%，而现有方法（如 Token Merging）在类似加速比下成功率下降超 20%。

### 结论
SpecPrune-VLA 通过结合全局上下文与局部信息的剪枝策略，在保持任务成功率的同时显著提升 VLA 模型推理速度，且无需额外训练或微调。该方法为实时机器人操作中的大模型部署提供了高效解决方案。

## Overview
Pruning is a typical acceleration technique for compute-bound models by removing computation on unimportant values. Recently, it has been applied to accelerate Vision-Language-Action (VLA) model inference. However, existing acceleration methods focus on local information from the current action step and ignore the global context, leading to >20% success rate drop and limited speedup in some scenarios. In this paper, we point out spatial-temporal consistency in VLA tasks: input images in consecutive steps exhibit high similarity, and propose the key insight that token selection should combine local information with global context of the model. Based on this, we propose SpecPrune-VLA, a training-free, two-level pruning method with heuristic control. (1) Action-level static pruning. We leverage global history and local attention to statically reduce visual tokens per action. (2) Layer-level dynamic pruning. We prune tokens adaptively per layer based on layer-wise importance. (3) Lightweight action-aware controller: We classify actions as coarse- or fine-grained by the speed of the end effector and adjust pruning aggressiveness accordingly. Extensive experiments show that SpecPrune-VLA achieves up to 1.57$\times$ speedup in LIBERO simulation and 1.70$\times$ on real-world tasks, with negligible success rate degradation.

## 参考
- http://arxiv.org/abs/2509.05614v3

## 개요
기존 VLA 모델 가속 방법은 현재 동작 단계의 국소 정보만 고려하여 전역 컨텍스트를 무시하므로, 성공률이 20% 이상 하락하고 가속 효과도 제한적입니다. SpecPrune-VLA는 VLA 작업에서 연속 단계 이미지가 높은 유사성을 보이는 공간-시간 일관성에 기반하여, 훈련이 필요 없는 2단계 프루닝 방법을 제안합니다: 동작 수준 정적 프루닝은 전역 히스토리와 국소 어텐션을 활용하여 각 동작의 시각 토큰 수를 줄이고, 계층별 동적 프루닝은 각 계층의 중요도에 따라 토큰을 적응적으로 제거하며, 경량 동작 인식 컨트롤러는 엔드 이펙터 속도에 따라 동작을 조립(coarse-grained)과 세밀(fine-grained)로 분류하여 프루닝 강도를 조정합니다. 실험 결과, 이 방법은 LIBERO 시뮬레이션에서 1.57배 가속, 실제 작업에서 1.70배 가속을 달성하면서도 성공률 손실은 거의 없습니다.

## 핵심 내용
### 방법 아키텍처
SpecPrune-VLA는 세 가지 핵심 구성 요소를 포함합니다:
- **동작 수준 정적 프루닝**: 전역 히스토리 어텐션과 국소 어텐션을 활용하여 각 동작 단계에서 시각 토큰 수를 정적으로 줄이고, 작업과 가장 관련된 이미지 영역을 유지합니다.
- **계층별 동적 프루닝**: 각 Transformer 계층의 어텐션 중요도 점수에 따라 중복 토큰을 적응적으로 제거하여, 고정 프루닝 비율로 인한 성능 손실을 방지합니다.
- **동작 인식 컨트롤러**: 엔드 이펙터 속도를 통해 동작을 조립(빠른 이동)과 세밀(정밀 조작)로 분류하고, 조립 동작에는 더 공격적인 프루닝 전략을 적용하며, 세밀 동작에는 정밀도를 보장하기 위해 더 많은 토큰을 유지합니다.

### 실험 설정 및 주요 수치
- **시뮬레이션 환경**: LIBERO 벤치마크, 10개의 장시간 조작 작업 포함.
- **실제 시나리오**: 7자유도 로봇 팔을 사용한 로봇 그리핑 및 배치 작업.
- **가속 효과**: LIBERO 시뮬레이션에서 1.57배 가속, 실제 작업에서 1.70배 가속 달성.
- **성공률**: 프루닝되지 않은 기준선 대비 성공률 하락이 1% 미만이며, 기존 방법(예: Token Merging)은 유사한 가속 비율에서 성공률이 20% 이상 하락합니다.

### 결론
SpecPrune-VLA는 전역 컨텍스트와 국소 정보를 결합한 프루닝 전략을 통해 작업 성공률을 유지하면서 VLA 모델 추론 속도를 크게 향상시키며, 추가 훈련이나 미세 조정이 필요 없습니다. 이 방법은 실시간 로봇 조작에서 대규모 모델 배포를 위한 효율적인 솔루션을 제공합니다.
