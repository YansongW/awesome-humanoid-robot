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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.05614v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Pruning은 중요하지 않은 값에 대한 연산을 제거하여 계산 집약적 모델을 가속화하는 대표적인 기술입니다. 최근에는 Vision-Language-Action(VLA) 모델 추론을 가속화하는 데 적용되었습니다. 그러나 기존 가속 방법은 현재 행동 단계의 지역적 정보에만 집중하고 전역적 맥락을 무시하여, 일부 시나리오에서 20% 이상의 성공률 감소와 제한된 속도 향상을 초래합니다. 본 논문에서는 VLA 작업에서 시공간적 일관성(연속된 단계의 입력 이미지가 높은 유사성을 보임)을 지적하고, 토큰 선택이 지역 정보와 모델의 전역적 맥락을 결합해야 한다는 핵심 통찰을 제안합니다. 이를 바탕으로 훈련이 필요 없고 휴리스틱 제어를 적용한 이중 수준 가지치기 방법인 SpecPrune-VLA를 제안합니다. (1) 행동 수준 정적 가지치기: 전역 기록과 지역 주의를 활용하여 각 행동당 시각적 토큰을 정적으로 줄입니다. (2) 계층 수준 동적 가지치기: 계층별 중요도에 따라 각 계층에서 적응적으로 토큰을 제거합니다. (3) 경량 행동 인식 제어기: 종단 효과기의 속도에 따라 행동을 조립 또는 세밀하게 분류하고, 이에 따라 가지치기 공격성을 조정합니다. 광범위한 실험 결과, SpecPrune-VLA는 LIBERO 시뮬레이션에서 최대 1.57배, 실제 작업에서 최대 1.70배의 속도 향상을 달성하며 성공률 저하는 무시할 수준입니다.

## 핵심 내용
Pruning은 중요하지 않은 값에 대한 연산을 제거하여 계산 집약적 모델을 가속화하는 대표적인 기술입니다. 최근에는 Vision-Language-Action(VLA) 모델 추론을 가속화하는 데 적용되었습니다. 그러나 기존 가속 방법은 현재 행동 단계의 지역적 정보에만 집중하고 전역적 맥락을 무시하여, 일부 시나리오에서 20% 이상의 성공률 감소와 제한된 속도 향상을 초래합니다. 본 논문에서는 VLA 작업에서 시공간적 일관성(연속된 단계의 입력 이미지가 높은 유사성을 보임)을 지적하고, 토큰 선택이 지역 정보와 모델의 전역적 맥락을 결합해야 한다는 핵심 통찰을 제안합니다. 이를 바탕으로 훈련이 필요 없고 휴리스틱 제어를 적용한 이중 수준 가지치기 방법인 SpecPrune-VLA를 제안합니다. (1) 행동 수준 정적 가지치기: 전역 기록과 지역 주의를 활용하여 각 행동당 시각적 토큰을 정적으로 줄입니다. (2) 계층 수준 동적 가지치기: 계층별 중요도에 따라 각 계층에서 적응적으로 토큰을 제거합니다. (3) 경량 행동 인식 제어기: 종단 효과기의 속도에 따라 행동을 조립 또는 세밀하게 분류하고, 이에 따라 가지치기 공격성을 조정합니다. 광범위한 실험 결과, SpecPrune-VLA는 LIBERO 시뮬레이션에서 최대 1.57배, 실제 작업에서 최대 1.70배의 속도 향상을 달성하며 성공률 저하는 무시할 수준입니다.

## 参考
- http://arxiv.org/abs/2509.05614v3
