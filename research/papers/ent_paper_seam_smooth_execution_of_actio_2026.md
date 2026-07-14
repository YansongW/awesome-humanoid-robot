---
$id: ent_paper_seam_smooth_execution_of_actio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action
    Policies'
  zh: 'SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action
    Policies'
  ko: 'SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action
    Policies'
summary:
  en: "arXiv:2607.04609v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA)\
    \ policies that execute fixed-length action chunks can exhibit multimodal bifurcation:\
    \ a cross-chunk inconsistency in which adjacent chunks generated from independent\
    \ Gaussian latents can converge to incompatible trajectory modes, producing abrupt\
    \ discontinuities at chunk boundaries. Existing remedies either require backpropagation\
    \ through the policy at each denoising step, rely on rejection sampling, or require\
    \ retraining, each trading computational cost or task reliability for smoother\
    \ transitions. We propose SEAM (Smooth Execution of Action-Chunked Motion), a\
    \ training-free inference-time method for flow matching VLAs. SEAM exploits a\
    \ simple synchronous-execution insight: after the robot consumes the executed\
    \ prefix, the previous chunk's unexecuted tail is already available as an analytic\
    \ consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS),\
    \ derives a time-dependent target from this tail and applies a closed-form correction\
    \ after each Euler step without backpropagating through the policy network. On\
    \ LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition\
    \ discontinuity by 27%, preserves baseline-level task success, and keeps denoising-loop\
    \ cost near the unguided baseline."
  zh: "arXiv:2607.04609v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA)\
    \ policies that execute fixed-length action chunks can exhibit multimodal bifurcation:\
    \ a cross-chunk inconsistency in which adjacent chunks generated from independent\
    \ Gaussian latents can converge to incompatible trajectory modes, producing abrupt\
    \ discontinuities at chunk boundaries. Existing remedies either require backpropagation\
    \ through the policy at each denoising step, rely on rejection sampling, or require\
    \ retraining, each trading computational cost or task reliability for smoother\
    \ transitions. We propose SEAM (Smooth Execution of Action-Chunked Motion), a\
    \ training-free inference-time method for flow matching VLAs. SEAM exploits a\
    \ simple synchronous-execution insight: after the robot consumes the executed\
    \ prefix, the previous chunk's unexecuted tail is already available as an analytic\
    \ consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS),\
    \ derives a time-dependent target from this tail and applies a closed-form correction\
    \ after each Euler step without backpropagating through the policy network. On\
    \ LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition\
    \ discontinuity by 27%, preserves baseline-level task success, and keeps denoising-loop\
    \ cost near the unguided baseline."
  ko: "arXiv:2607.04609v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA)\
    \ policies that execute fixed-length action chunks can exhibit multimodal bifurcation:\
    \ a cross-chunk inconsistency in which adjacent chunks generated from independent\
    \ Gaussian latents can converge to incompatible trajectory modes, producing abrupt\
    \ discontinuities at chunk boundaries. Existing remedies either require backpropagation\
    \ through the policy at each denoising step, rely on rejection sampling, or require\
    \ retraining, each trading computational cost or task reliability for smoother\
    \ transitions. We propose SEAM (Smooth Execution of Action-Chunked Motion), a\
    \ training-free inference-time method for flow matching VLAs. SEAM exploits a\
    \ simple synchronous-execution insight: after the robot consumes the executed\
    \ prefix, the previous chunk's unexecuted tail is already available as an analytic\
    \ consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS),\
    \ derives a time-dependent target from this tail and applies a closed-form correction\
    \ after each Euler step without backpropagating through the policy network. On\
    \ LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition\
    \ discontinuity by 27%, preserves baseline-level task success, and keeps denoising-loop\
    \ cost near the unguided baseline."
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
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action
    Policies (arXiv)'
  url: https://arxiv.org/abs/2607.04609
  date: '2026'
  accessed_at: '2026-07-08'
---

## 概述
arXiv:2607.04609v1 Announce Type: new 
Abstract: Vision-Language-Action (VLA) policies that execute fixed-length action chunks can exhibit multimodal bifurcation: a cross-chunk inconsistency in which adjacent chunks generated from independent Gaussian latents can converge to incompatible trajectory modes, producing abrupt discontinuities at chunk boundaries. Existing remedies either require backpropagation through the policy at each denoising step, rely on rejection sampling, or require retraining, each trading computational cost or task reliability for smoother transitions. We propose SEAM (Smooth Execution of Action-Chunked Motion), a training-free inference-time method for flow matching VLAs. SEAM exploits a simple synchronous-execution insight: after the robot consumes the executed prefix, the previous chunk's unexecuted tail is already available as an analytic consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS), derives a time-dependent target from this tail and applies a closed-form correction after each Euler step without backpropagating through the policy network. On LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition discontinuity by 27%, preserves baseline-level task success, and keeps denoising-loop cost near the unguided baseline.

## Overview
arXiv:2607.04609v1 Announce Type: new 
Abstract: Vision-Language-Action (VLA) policies that execute fixed-length action chunks can exhibit multimodal bifurcation: a cross-chunk inconsistency in which adjacent chunks generated from independent Gaussian latents can converge to incompatible trajectory modes, producing abrupt discontinuities at chunk boundaries. Existing remedies either require backpropagation through the policy at each denoising step, rely on rejection sampling, or require retraining, each trading computational cost or task reliability for smoother transitions. We propose SEAM (Smooth Execution of Action-Chunked Motion), a training-free inference-time method for flow matching VLAs. SEAM exploits a simple synchronous-execution insight: after the robot consumes the executed prefix, the previous chunk's unexecuted tail is already available as an analytic consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS), derives a time-dependent target from this tail and applies a closed-form correction after each Euler step without backpropagating through the policy network. On LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition discontinuity by 27%, preserves baseline-level task success, and keeps denoising-loop cost near the unguided baseline.

## 개요
arXiv:2607.04609v1 Announce Type: new 
Abstract: Vision-Language-Action (VLA) policies that execute fixed-length action chunks can exhibit multimodal bifurcation: a cross-chunk inconsistency in which adjacent chunks generated from independent Gaussian latents can converge to incompatible trajectory modes, producing abrupt discontinuities at chunk boundaries. Existing remedies either require backpropagation through the policy at each denoising step, rely on rejection sampling, or require retraining, each trading computational cost or task reliability for smoother transitions. We propose SEAM (Smooth Execution of Action-Chunked Motion), a training-free inference-time method for flow matching VLAs. SEAM exploits a simple synchronous-execution insight: after the robot consumes the executed prefix, the previous chunk's unexecuted tail is already available as an analytic consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS), derives a time-dependent target from this tail and applies a closed-form correction after each Euler step without backpropagating through the policy network. On LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition discontinuity by 27%, preserves baseline-level task success, and keeps denoising-loop cost near the unguided baseline.
