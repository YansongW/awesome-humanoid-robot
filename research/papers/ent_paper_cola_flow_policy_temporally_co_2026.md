---
$id: ent_paper_cola_flow_policy_temporally_co_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoLA-Flow Policy: Temporally Coherent Imitation Learning via Continuous Latent Action Flow Matching for Robotic Manipulation'
  zh: 'CoLA-Flow Policy: Temporally Coherent Imitation Learning via Continuous Latent Action Flow Matching for Robotic Manipulation'
  ko: 'CoLA-Flow Policy: Temporally Coherent Imitation Learning via Continuous Latent Action Flow Matching for Robotic Manipulation'
summary:
  en: 'arXiv:2601.23087v5 Announce Type: replace Abstract: Learning long-horizon robotic manipulation requires jointly achieving
    expressive behavior modeling, real-time inference, and stable execution, which remains challenging for existing generative
    policies. Diffusion-based approaches offer strong modeling capacity but incur high inference latency, while flow matching
    enables fast, near-single-step generation yet often suffers from unstable execution when operating directly in the raw
    action space. We propose Continuous Latent Action Flow Policy (CoLA-Flow Policy), a trajectory-level imitation learning
    framework that performs flow matching in a continuous latent action space. By encoding action sequences into temporally
    coherent latent trajectories and learning an explicit latent-space flow, CoLA-Flow Policy decouples global motion structure
    from low-level control noise, enabling smooth and reliable long-horizon execution. The framework further integrates geometry-aware
    point cloud conditioning and execution-time multimodal modulation, using visual cues as a representative modality to enhance
    real-world robustness. Experiments in simulation and on real robots show that CoLA-Flow Policy achieves near-single-step
    inference, improves trajectory smoothness by up to 93.7% and task success by up to 25 percentage points over raw action-space
    flow baselines, while remaining significantly faster than diffusion-based policies.'
  zh: 'arXiv:2601.23087v5 Announce Type: replace Abstract: Learning long-horizon robotic manipulation requires jointly achieving
    expressive behavior modeling, real-time inference, and stable execution, which remains challenging for existing generative
    policies. Diffusion-based approaches offer strong modeling capacity but incur high inference latency, while flow matching
    enables fast, near-single-step generation yet often suffers from unstable execution when operating directly in the raw
    action space. We propose Continuous Latent Action Flow Policy (CoLA-Flow Policy), a trajectory-level imitation learning
    framework that performs flow matching in a continuous latent action space. By encoding action sequences into temporally
    coherent latent trajectories and learning an explicit latent-space flow, CoLA-Flow Policy decouples global motion structure
    from low-level control noise, enabling smooth and reliable long-horizon execution. The framework further integrates geometry-aware
    point cloud conditioning and execution-time multimodal modulation, using visual cues as a representative modality to enhance
    real-world robustness. Experiments in simulation and on real robots show that CoLA-Flow Policy achieves near-single-step
    inference, improves trajectory smoothness by up to 93.7% and task success by up to 25 percentage points over raw action-space
    flow baselines, while remaining significantly faster than diffusion-based policies.'
  ko: 'arXiv:2601.23087v5 Announce Type: replace Abstract: Learning long-horizon robotic manipulation requires jointly achieving
    expressive behavior modeling, real-time inference, and stable execution, which remains challenging for existing generative
    policies. Diffusion-based approaches offer strong modeling capacity but incur high inference latency, while flow matching
    enables fast, near-single-step generation yet often suffers from unstable execution when operating directly in the raw
    action space. We propose Continuous Latent Action Flow Policy (CoLA-Flow Policy), a trajectory-level imitation learning
    framework that performs flow matching in a continuous latent action space. By encoding action sequences into temporally
    coherent latent trajectories and learning an explicit latent-space flow, CoLA-Flow Policy decouples global motion structure
    from low-level control noise, enabling smooth and reliable long-horizon execution. The framework further integrates geometry-aware
    point cloud conditioning and execution-time multimodal modulation, using visual cues as a representative modality to enhance
    real-world robustness. Experiments in simulation and on real robots show that CoLA-Flow Policy achieves near-single-step
    inference, improves trajectory smoothness by up to 93.7% and task success by up to 25 percentage points over raw action-space
    flow baselines, while remaining significantly faster than diffusion-based policies.'
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
- cola_flow_policy
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.23087v5.
sources:
- id: src_001
  type: paper
  title: 'CoLA-Flow Policy: Temporally Coherent Imitation Learning via Continuous Latent Action Flow Matching for Robotic
    Manipulation (arXiv)'
  url: https://arxiv.org/abs/2601.23087
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Learning long-horizon robotic manipulation requires jointly achieving expressive behavior modeling, real-time inference, and stable execution, which remains challenging for existing generative policies. Diffusion-based approaches offer strong modeling capacity but incur high inference latency, while flow matching enables fast, near-single-step generation yet often suffers from unstable execution when operating directly in the raw action space. We propose Continuous Latent Action Flow Policy (CoLA-Flow Policy), a trajectory-level imitation learning framework that performs flow matching in a continuous latent action space. By encoding action sequences into temporally coherent latent trajectories and learning an explicit latent-space flow, CoLA-Flow Policy decouples global motion structure from low-level control noise, enabling smooth and reliable long-horizon execution. The framework further integrates geometry-aware point cloud conditioning and execution-time multimodal modulation, using visual cues as a representative modality to enhance real-world robustness. Experiments in simulation and on real robots show that CoLA-Flow Policy achieves near-single-step inference, improves trajectory smoothness by up to 93.7% and task success by up to 25 percentage points over raw action-space flow baselines, while remaining significantly faster than diffusion-based policies.

## 核心内容
Learning long-horizon robotic manipulation requires jointly achieving expressive behavior modeling, real-time inference, and stable execution, which remains challenging for existing generative policies. Diffusion-based approaches offer strong modeling capacity but incur high inference latency, while flow matching enables fast, near-single-step generation yet often suffers from unstable execution when operating directly in the raw action space. We propose Continuous Latent Action Flow Policy (CoLA-Flow Policy), a trajectory-level imitation learning framework that performs flow matching in a continuous latent action space. By encoding action sequences into temporally coherent latent trajectories and learning an explicit latent-space flow, CoLA-Flow Policy decouples global motion structure from low-level control noise, enabling smooth and reliable long-horizon execution. The framework further integrates geometry-aware point cloud conditioning and execution-time multimodal modulation, using visual cues as a representative modality to enhance real-world robustness. Experiments in simulation and on real robots show that CoLA-Flow Policy achieves near-single-step inference, improves trajectory smoothness by up to 93.7% and task success by up to 25 percentage points over raw action-space flow baselines, while remaining significantly faster than diffusion-based policies.

## 参考
- http://arxiv.org/abs/2601.23087v5

## Overview
Learning long-horizon robotic manipulation requires jointly achieving expressive behavior modeling, real-time inference, and stable execution, which remains challenging for existing generative policies. Diffusion-based approaches offer strong modeling capacity but incur high inference latency, while flow matching enables fast, near-single-step generation yet often suffers from unstable execution when operating directly in the raw action space. We propose Continuous Latent Action Flow Policy (CoLA-Flow Policy), a trajectory-level imitation learning framework that performs flow matching in a continuous latent action space. By encoding action sequences into temporally coherent latent trajectories and learning an explicit latent-space flow, CoLA-Flow Policy decouples global motion structure from low-level control noise, enabling smooth and reliable long-horizon execution. The framework further integrates geometry-aware point cloud conditioning and execution-time multimodal modulation, using visual cues as a representative modality to enhance real-world robustness. Experiments in simulation and on real robots show that CoLA-Flow Policy achieves near-single-step inference, improves trajectory smoothness by up to 93.7% and task success by up to 25 percentage points over raw action-space flow baselines, while remaining significantly faster than diffusion-based policies.

## Content
Learning long-horizon robotic manipulation requires jointly achieving expressive behavior modeling, real-time inference, and stable execution, which remains challenging for existing generative policies. Diffusion-based approaches offer strong modeling capacity but incur high inference latency, while flow matching enables fast, near-single-step generation yet often suffers from unstable execution when operating directly in the raw action space. We propose Continuous Latent Action Flow Policy (CoLA-Flow Policy), a trajectory-level imitation learning framework that performs flow matching in a continuous latent action space. By encoding action sequences into temporally coherent latent trajectories and learning an explicit latent-space flow, CoLA-Flow Policy decouples global motion structure from low-level control noise, enabling smooth and reliable long-horizon execution. The framework further integrates geometry-aware point cloud conditioning and execution-time multimodal modulation, using visual cues as a representative modality to enhance real-world robustness. Experiments in simulation and on real robots show that CoLA-Flow Policy achieves near-single-step inference, improves trajectory smoothness by up to 93.7% and task success by up to 25 percentage points over raw action-space flow baselines, while remaining significantly faster than diffusion-based policies.

## 개요
장기간 로봇 조작 학습은 표현력 있는 행동 모델링, 실시간 추론, 안정적인 실행을 동시에 달성해야 하며, 이는 기존 생성 정책(generative policies)에 여전히 도전 과제로 남아 있습니다. 확산 기반 접근법은 강력한 모델링 능력을 제공하지만 높은 추론 지연 시간을 초래하는 반면, 흐름 매칭(flow matching)은 빠르고 거의 단일 단계에 가까운 생성을 가능하게 하지만 원시 행동 공간에서 직접 작동할 때 종종 불안정한 실행 문제를 겪습니다. 우리는 연속 잠재 행동 흐름 정책(CoLA-Flow Policy)을 제안합니다. 이는 연속 잠재 행동 공간에서 흐름 매칭을 수행하는 궤적 수준의 모방 학습 프레임워크입니다. 행동 시퀀스를 시간적으로 일관된 잠재 궤적으로 인코딩하고 명시적인 잠재 공간 흐름을 학습함으로써, CoLA-Flow Policy는 전역 운동 구조를 저수준 제어 노이즈로부터 분리하여 부드럽고 신뢰할 수 있는 장기간 실행을 가능하게 합니다. 이 프레임워크는 또한 기하학 인식 포인트 클라우드 조건화와 실행 시간 다중 모드 변조를 통합하며, 시각적 단서를 대표적인 모달리티로 사용하여 실제 환경에서의 강건성을 향상시킵니다. 시뮬레이션 및 실제 로봇 실험에서 CoLA-Flow Policy는 거의 단일 단계 추론을 달성하고, 원시 행동 공간 흐름 기준선 대비 궤적 부드러움을 최대 93.7% 개선하며 작업 성공률을 최대 25% 포인트 향상시키면서도 확산 기반 정책보다 훨씬 빠른 속도를 유지함을 보여줍니다.

## 핵심 내용
장기간 로봇 조작 학습은 표현력 있는 행동 모델링, 실시간 추론, 안정적인 실행을 동시에 달성해야 하며, 이는 기존 생성 정책(generative policies)에 여전히 도전 과제로 남아 있습니다. 확산 기반 접근법은 강력한 모델링 능력을 제공하지만 높은 추론 지연 시간을 초래하는 반면, 흐름 매칭(flow matching)은 빠르고 거의 단일 단계에 가까운 생성을 가능하게 하지만 원시 행동 공간에서 직접 작동할 때 종종 불안정한 실행 문제를 겪습니다. 우리는 연속 잠재 행동 흐름 정책(CoLA-Flow Policy)을 제안합니다. 이는 연속 잠재 행동 공간에서 흐름 매칭을 수행하는 궤적 수준의 모방 학습 프레임워크입니다. 행동 시퀀스를 시간적으로 일관된 잠재 궤적으로 인코딩하고 명시적인 잠재 공간 흐름을 학습함으로써, CoLA-Flow Policy는 전역 운동 구조를 저수준 제어 노이즈로부터 분리하여 부드럽고 신뢰할 수 있는 장기간 실행을 가능하게 합니다. 이 프레임워크는 또한 기하학 인식 포인트 클라우드 조건화와 실행 시간 다중 모드 변조를 통합하며, 시각적 단서를 대표적인 모달리티로 사용하여 실제 환경에서의 강건성을 향상시킵니다. 시뮬레이션 및 실제 로봇 실험에서 CoLA-Flow Policy는 거의 단일 단계 추론을 달성하고, 원시 행동 공간 흐름 기준선 대비 궤적 부드러움을 최대 93.7% 개선하며 작업 성공률을 최대 25% 포인트 향상시키면서도 확산 기반 정책보다 훨씬 빠른 속도를 유지함을 보여줍니다.
