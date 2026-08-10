---
$id: ent_paper_seam_smooth_execution_of_actio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action Policies'
  zh: 'SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action Policies'
  ko: 'SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action Policies'
summary:
  en: 'arXiv:2607.04609v1 Announce Type: new Abstract: Vision-Language-Action (VLA) policies that execute fixed-length action
    chunks can exhibit multimodal bifurcation: a cross-chunk inconsistency in which adjacent chunks generated from independent
    Gaussian latents can converge to incompatible trajectory modes, producing abrupt discontinuities at chunk boundaries.
    Existing remedies either require backpropagation through the policy at each denoising step, rely on rejection sampling,
    or require retraining, each trading computational cost or task reliability for smoother transitions. We propose SEAM (Smooth
    Execution of Action-Chunked Motion), a training-free inference-time method for flow matching VLAs. SEAM exploits a simple
    synchronous-execution insight: after the robot consumes the executed prefix, the previous chunk''s unexecuted tail is
    already available as an analytic consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS), derives
    a time-dependent target from this tail and applies a closed-form correction after each Euler step without backpropagating
    through the policy network. On LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition discontinuity
    by 27%, preserves baseline-level task success, and keeps denoising-loop cost near the unguided baseline.'
  zh: SEAM是一种无需训练的推理时方法，用于解决视觉-语言-动作（VLA）策略中固定长度动作块执行时的多模态分叉问题。其核心机制Velocity-guided Loss Steering (VLS)通过利用前一块未执行尾部作为一致性参考，在每次Euler步骤后施加闭式修正，无需反向传播。在LIBERO-10基准上结合pi_0.5模型，SEAM将边界急动度降低28%，块过渡不连续性降低27%，同时保持任务成功率与基线持平。
  ko: 'arXiv:2607.04609v1 Announce Type: new Abstract: Vision-Language-Action (VLA) policies that execute fixed-length action
    chunks can exhibit multimodal bifurcation: a cross-chunk inconsistency in which adjacent chunks generated from independent
    Gaussian latents can converge to incompatible trajectory modes, producing abrupt discontinuities at chunk boundaries.
    Existing remedies either require backpropagation through the policy at each denoising step, rely on rejection sampling,
    or require retraining, each trading computational cost or task reliability for smoother transitions. We propose SEAM (Smooth
    Execution of Action-Chunked Motion), a training-free inference-time method for flow matching VLAs. SEAM exploits a simple
    synchronous-execution insight: after the robot consumes the executed prefix, the previous chunk''s unexecuted tail is
    already available as an analytic consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS), derives
    a time-dependent target from this tail and applies a closed-form correction after each Euler step without backpropagating
    through the policy network. On LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition discontinuity
    by 27%, preserves baseline-level task success, and keeps denoising-loop cost near the unguided baseline.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- seam
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04609v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (751 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action Policies (arXiv)'
  url: https://arxiv.org/abs/2607.04609
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
VLA策略在执行固定长度动作块时，因相邻块由独立高斯潜变量生成，可能收敛到不兼容的轨迹模式，导致块边界处出现突变。现有解决方案需在每次去噪步骤中通过策略反向传播、依赖拒绝采样或重新训练，均以计算成本或任务可靠性换取平滑过渡。SEAM提出一种同步执行洞察：机器人消耗已执行前缀后，前一块未执行尾部可作为分析一致性参考。其VLS机制从该尾部推导时变目标，并在每个Euler步骤后施加闭式修正，无需通过策略网络反向传播。实验表明，在LIBERO-10上使用pi_0.5时，SEAM有效降低边界急动度和过渡不连续性，且不牺牲任务成功率。

## 核心内容
### 方法
- **问题定义**：VLA策略生成固定长度动作块时，相邻块因独立高斯潜变量产生多模态分叉，导致块边界处轨迹不连续。
- **核心洞察**：同步执行过程中，前一块未执行尾部可作为后一块的显式一致性参考，无需额外计算。
- **VLS机制**：
  - 从已执行前缀的未执行尾部推导时变目标。
  - 在每次Euler步骤后应用闭式修正，避免反向传播。
  - 修正公式直接作用于速度场，保持去噪循环成本接近无引导基线。

### 实验设置
- **基准**：LIBERO-10
- **模型**：pi_0.5（流匹配VLA）
- **评估指标**：边界急动度、块过渡不连续性、任务成功率、去噪循环成本

### 关键结果
- 边界急动度降低28%
- 块过渡不连续性降低27%
- 任务成功率与基线持平
- 去噪循环成本接近无引导基线

### 结论
SEAM通过无需训练的推理时修正，有效缓解VLA策略的动作块边界不连续问题，在保持任务性能的同时显著提升运动平滑性。其闭式修正机制避免了额外计算开销，适用于实时机器人控制场景。

## Overview
Vision-Language-Action (VLA) policies that execute fixed-length action chunks can exhibit multimodal bifurcation: a cross-chunk inconsistency in which adjacent chunks generated from independent Gaussian latents can converge to incompatible trajectory modes, producing abrupt discontinuities at chunk boundaries. Existing remedies either require backpropagation through the policy at each denoising step, rely on rejection sampling, or require retraining, each trading computational cost or task reliability for smoother transitions. We propose SEAM (Smooth Execution of Action-Chunked Motion), a training-free inference-time method for flow matching VLAs. SEAM exploits a simple synchronous-execution insight: after the robot consumes the executed prefix, the previous chunk's unexecuted tail is already available as an analytic consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS), derives a time-dependent target from this tail and applies a closed-form correction after each Euler step without backpropagating through the policy network. On LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition discontinuity by 27%, preserves baseline-level task success, and keeps denoising-loop cost near the unguided baseline.

## 参考
- http://arxiv.org/abs/2607.04609v1

## 개요
VLA 정책이 고정 길이 동작 블록을 실행할 때, 인접 블록이 독립적인 가우시안 잠재 변수로 생성되므로 호환되지 않는 궤적 패턴으로 수렴할 수 있으며, 이로 인해 블록 경계에서 급격한 변화가 발생할 수 있습니다. 기존 해결책은 매 denoising 단계에서 정책 역전파, 거부 샘플링 의존 또는 재훈련이 필요하며, 모두 계산 비용이나 작업 신뢰성을 희생하여 부드러운 전환을 얻습니다. SEAM은 동기 실행 통찰력을 제안합니다: 로봇이 실행된 접두사를 소비한 후, 이전 블록의 실행되지 않은 꼬리 부분이 일관성 참조로 사용될 수 있습니다. VLS 메커니즘은 이 꼬리 부분에서 시간 변화 목표를 도출하고, 각 Euler 단계 후에 폐쇄형 수정을 적용하여 정책 네트워크를 통한 역전파 없이 수행합니다. 실험에서 LIBERO-10에서 pi_0.5를 사용할 때, SEAM은 경계 급격성과 전환 불연속성을 효과적으로 줄이면서 작업 성공률을 희생하지 않습니다.

## 핵심 내용
### 방법
- **문제 정의**: VLA 정책이 고정 길이 동작 블록을 생성할 때, 인접 블록이 독립적인 가우시안 잠재 변수로 인해 다중 모드 분기로 이어져 블록 경계에서 궤적 불연속성이 발생합니다.
- **핵심 통찰력**: 동기 실행 과정에서 이전 블록의 실행되지 않은 꼬리 부분이 다음 블록의 명시적 일관성 참조로 사용될 수 있으며, 추가 계산이 필요 없습니다.
- **VLS 메커니즘**:
  - 실행된 접두사의 실행되지 않은 꼬리 부분에서 시간 변화 목표를 도출합니다.
  - 각 Euler 단계 후에 폐쇄형 수정을 적용하여 역전파를 피합니다.
  - 수정 공식은 속도 필드에 직접 작용하여 denoising 루프 비용을 가이드 없는 기준선에 가깝게 유지합니다.

### 실험 설정
- **벤치마크**: LIBERO-10
- **모델**: pi_0.5 (흐름 매칭 VLA)
- **평가 지표**: 경계 급격성, 블록 전환 불연속성, 작업 성공률, denoising 루프 비용

### 주요 결과
- 경계 급격성 28% 감소
- 블록 전환 불연속성 27% 감소
- 작업 성공률은 기준선과 동일
- denoising 루프 비용은 가이드 없는 기준선에 근접

### 결론
SEAM은 훈련 없는 추론 시 수정을 통해 VLA 정책의 동작 블록 경계 불연속성 문제를 효과적으로 완화하며, 작업 성능을 유지하면서 운동 부드러움을 크게 향상시킵니다. 폐쇄형 수정 메커니즘은 추가 계산 오버헤드를 피하여 실시간 로봇 제어 시나리오에 적합합니다.
