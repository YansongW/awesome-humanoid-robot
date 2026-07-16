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
  zh: 'arXiv:2607.04609v1 Announce Type: new Abstract: Vision-Language-Action (VLA) policies that execute fixed-length action
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04609v1.
sources:
- id: src_001
  type: paper
  title: 'SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action Policies (arXiv)'
  url: https://arxiv.org/abs/2607.04609
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Vision-Language-Action (VLA) policies that execute fixed-length action chunks can exhibit multimodal bifurcation: a cross-chunk inconsistency in which adjacent chunks generated from independent Gaussian latents can converge to incompatible trajectory modes, producing abrupt discontinuities at chunk boundaries. Existing remedies either require backpropagation through the policy at each denoising step, rely on rejection sampling, or require retraining, each trading computational cost or task reliability for smoother transitions. We propose SEAM (Smooth Execution of Action-Chunked Motion), a training-free inference-time method for flow matching VLAs. SEAM exploits a simple synchronous-execution insight: after the robot consumes the executed prefix, the previous chunk's unexecuted tail is already available as an analytic consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS), derives a time-dependent target from this tail and applies a closed-form correction after each Euler step without backpropagating through the policy network. On LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition discontinuity by 27%, preserves baseline-level task success, and keeps denoising-loop cost near the unguided baseline.

## 核心内容
Vision-Language-Action (VLA) policies that execute fixed-length action chunks can exhibit multimodal bifurcation: a cross-chunk inconsistency in which adjacent chunks generated from independent Gaussian latents can converge to incompatible trajectory modes, producing abrupt discontinuities at chunk boundaries. Existing remedies either require backpropagation through the policy at each denoising step, rely on rejection sampling, or require retraining, each trading computational cost or task reliability for smoother transitions. We propose SEAM (Smooth Execution of Action-Chunked Motion), a training-free inference-time method for flow matching VLAs. SEAM exploits a simple synchronous-execution insight: after the robot consumes the executed prefix, the previous chunk's unexecuted tail is already available as an analytic consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS), derives a time-dependent target from this tail and applies a closed-form correction after each Euler step without backpropagating through the policy network. On LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition discontinuity by 27%, preserves baseline-level task success, and keeps denoising-loop cost near the unguided baseline.

## 参考
- http://arxiv.org/abs/2607.04609v1

## Overview
Vision-Language-Action (VLA) policies that execute fixed-length action chunks can exhibit multimodal bifurcation: a cross-chunk inconsistency in which adjacent chunks generated from independent Gaussian latents can converge to incompatible trajectory modes, producing abrupt discontinuities at chunk boundaries. Existing remedies either require backpropagation through the policy at each denoising step, rely on rejection sampling, or require retraining, each trading computational cost or task reliability for smoother transitions. We propose SEAM (Smooth Execution of Action-Chunked Motion), a training-free inference-time method for flow matching VLAs. SEAM exploits a simple synchronous-execution insight: after the robot consumes the executed prefix, the previous chunk's unexecuted tail is already available as an analytic consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS), derives a time-dependent target from this tail and applies a closed-form correction after each Euler step without backpropagating through the policy network. On LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition discontinuity by 27%, preserves baseline-level task success, and keeps denoising-loop cost near the unguided baseline.

## Content
Vision-Language-Action (VLA) policies that execute fixed-length action chunks can exhibit multimodal bifurcation: a cross-chunk inconsistency in which adjacent chunks generated from independent Gaussian latents can converge to incompatible trajectory modes, producing abrupt discontinuities at chunk boundaries. Existing remedies either require backpropagation through the policy at each denoising step, rely on rejection sampling, or require retraining, each trading computational cost or task reliability for smoother transitions. We propose SEAM (Smooth Execution of Action-Chunked Motion), a training-free inference-time method for flow matching VLAs. SEAM exploits a simple synchronous-execution insight: after the robot consumes the executed prefix, the previous chunk's unexecuted tail is already available as an analytic consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS), derives a time-dependent target from this tail and applies a closed-form correction after each Euler step without backpropagating through the policy network. On LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition discontinuity by 27%, preserves baseline-level task success, and keeps denoising-loop cost near the unguided baseline.

## 개요
고정 길이의 액션 청크를 실행하는 Vision-Language-Action (VLA) 정책은 다중 모드 분기(multimodal bifurcation)를 나타낼 수 있습니다. 이는 독립적인 가우시안 잠재 변수에서 생성된 인접 청크가 호환되지 않는 궤적 모드로 수렴하여 청크 경계에서 급격한 불연속성을 초래하는 청크 간 불일치입니다. 기존의 해결 방법은 각 디노이징 단계에서 정책을 통한 역전파를 필요로 하거나, 리젝션 샘플링에 의존하거나, 재학습을 요구하며, 각각 계산 비용이나 작업 신뢰성을 더 부드러운 전환과 맞바꿉니다. 우리는 SEAM (Smooth Execution of Action-Chunked Motion)을 제안합니다. 이는 플로우 매칭 VLA를 위한 학습 없이 추론 시간에 적용되는 방법입니다. SEAM은 간단한 동기 실행 통찰력을 활용합니다: 로봇이 실행된 접두사를 소비한 후, 이전 청크의 실행되지 않은 꼬리 부분이 이미 분석적 일관성 참조로 사용 가능합니다. 그 핵심 메커니즘인 Velocity-guided Loss Steering (VLS)은 이 꼬리에서 시간 의존적 목표를 도출하고, 정책 네트워크를 통한 역전파 없이 각 오일러 단계 후에 폐쇄형 보정을 적용합니다. LIBERO-10에서 pi_0.5를 사용한 실험에서 SEAM은 경계 저크를 28% 감소시키고, 청크 전환 불연속성을 27% 감소시키며, 기준선 수준의 작업 성공률을 유지하고, 디노이징 루프 비용을 비유도 기준선에 가깝게 유지합니다.

## 핵심 내용
고정 길이의 액션 청크를 실행하는 Vision-Language-Action (VLA) 정책은 다중 모드 분기(multimodal bifurcation)를 나타낼 수 있습니다. 이는 독립적인 가우시안 잠재 변수에서 생성된 인접 청크가 호환되지 않는 궤적 모드로 수렴하여 청크 경계에서 급격한 불연속성을 초래하는 청크 간 불일치입니다. 기존의 해결 방법은 각 디노이징 단계에서 정책을 통한 역전파를 필요로 하거나, 리젝션 샘플링에 의존하거나, 재학습을 요구하며, 각각 계산 비용이나 작업 신뢰성을 더 부드러운 전환과 맞바꿉니다. 우리는 SEAM (Smooth Execution of Action-Chunked Motion)을 제안합니다. 이는 플로우 매칭 VLA를 위한 학습 없이 추론 시간에 적용되는 방법입니다. SEAM은 간단한 동기 실행 통찰력을 활용합니다: 로봇이 실행된 접두사를 소비한 후, 이전 청크의 실행되지 않은 꼬리 부분이 이미 분석적 일관성 참조로 사용 가능합니다. 그 핵심 메커니즘인 Velocity-guided Loss Steering (VLS)은 이 꼬리에서 시간 의존적 목표를 도출하고, 정책 네트워크를 통한 역전파 없이 각 오일러 단계 후에 폐쇄형 보정을 적용합니다. LIBERO-10에서 pi_0.5를 사용한 실험에서 SEAM은 경계 저크를 28% 감소시키고, 청크 전환 불연속성을 27% 감소시키며, 기준선 수준의 작업 성공률을 유지하고, 디노이징 루프 비용을 비유도 기준선에 가깝게 유지합니다.
