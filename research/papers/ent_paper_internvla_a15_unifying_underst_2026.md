---
$id: ent_paper_internvla_a15_unifying_underst_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization'
  zh: 'InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization'
  ko: 'InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization'
summary:
  en: 'arXiv:2607.04988v1 Announce Type: new Abstract: Unified models for robot manipulation aim to equip one policy with
    both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice,
    existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives,
    and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited.
    We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA and subtask prediction,
    and attaches a lightweight unified expert for continuous action generation. Future prediction is recast as a latent-querying
    problem, where a small set of learnable foresight tokens condenses the task-relevant future into a compact latent code
    under the supervision of a frozen pretrained video generation model, so the policy inherits world-model dynamics priors
    without ever learning pixel-level generation. The video branch is discarded at inference, keeping real-time control. Pretrained
    on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves the best overall results on all six simulation
    benchmarks. In the real world, the preserved semantics deliver the strongest compositional generalization on held-out
    instruction bindings, and the two designs together sustain long-horizon execution.'
  zh: 'arXiv:2607.04988v1 Announce Type: new Abstract: Unified models for robot manipulation aim to equip one policy with
    both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice,
    existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives,
    and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited.
    We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA and subtask prediction,
    and attaches a lightweight unified expert for continuous action generation. Future prediction is recast as a latent-querying
    problem, where a small set of learnable foresight tokens condenses the task-relevant future into a compact latent code
    under the supervision of a frozen pretrained video generation model, so the policy inherits world-model dynamics priors
    without ever learning pixel-level generation. The video branch is discarded at inference, keeping real-time control. Pretrained
    on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves the best overall results on all six simulation
    benchmarks. In the real world, the preserved semantics deliver the strongest compositional generalization on held-out
    instruction bindings, and the two designs together sustain long-horizon execution.'
  ko: 'arXiv:2607.04988v1 Announce Type: new Abstract: Unified models for robot manipulation aim to equip one policy with
    both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice,
    existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives,
    and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited.
    We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA and subtask prediction,
    and attaches a lightweight unified expert for continuous action generation. Future prediction is recast as a latent-querying
    problem, where a small set of learnable foresight tokens condenses the task-relevant future into a compact latent code
    under the supervision of a frozen pretrained video generation model, so the policy inherits world-model dynamics priors
    without ever learning pixel-level generation. The video branch is discarded at inference, keeping real-time control. Pretrained
    on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves the best overall results on all six simulation
    benchmarks. In the real world, the preserved semantics deliver the strongest compositional generalization on held-out
    instruction bindings, and the two designs together sustain long-horizon execution.'
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
- internvla_a15
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04988v1.
sources:
- id: src_001
  type: paper
  title: 'InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization (arXiv)'
  url: https://arxiv.org/abs/2607.04988
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Unified models for robot manipulation aim to equip one policy with both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice, existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives, and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited. We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA and subtask prediction, and attaches a lightweight unified expert for continuous action generation. Future prediction is recast as a latent-querying problem, where a small set of learnable foresight tokens condenses the task-relevant future into a compact latent code under the supervision of a frozen pretrained video generation model, so the policy inherits world-model dynamics priors without ever learning pixel-level generation. The video branch is discarded at inference, keeping real-time control. Pretrained on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves the best overall results on all six simulation benchmarks. In the real world, the preserved semantics deliver the strongest compositional generalization on held-out instruction bindings, and the two designs together sustain long-horizon execution.

## 核心内容
Unified models for robot manipulation aim to equip one policy with both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice, existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives, and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited. We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA and subtask prediction, and attaches a lightweight unified expert for continuous action generation. Future prediction is recast as a latent-querying problem, where a small set of learnable foresight tokens condenses the task-relevant future into a compact latent code under the supervision of a frozen pretrained video generation model, so the policy inherits world-model dynamics priors without ever learning pixel-level generation. The video branch is discarded at inference, keeping real-time control. Pretrained on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves the best overall results on all six simulation benchmarks. In the real world, the preserved semantics deliver the strongest compositional generalization on held-out instruction bindings, and the two designs together sustain long-horizon execution.

## 参考
- http://arxiv.org/abs/2607.04988v1

## Overview
Unified models for robot manipulation aim to equip one policy with both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice, existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives, and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited. We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA and subtask prediction, and attaches a lightweight unified expert for continuous action generation. Future prediction is recast as a latent-querying problem, where a small set of learnable foresight tokens condenses the task-relevant future into a compact latent code under the supervision of a frozen pretrained video generation model, so the policy inherits world-model dynamics priors without ever learning pixel-level generation. The video branch is discarded at inference, keeping real-time control. Pretrained on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves the best overall results on all six simulation benchmarks. In the real world, the preserved semantics deliver the strongest compositional generalization on held-out instruction bindings, and the two designs together sustain long-horizon execution.

## Content
Unified models for robot manipulation aim to equip one policy with both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice, existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives, and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited. We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA and subtask prediction, and attaches a lightweight unified expert for continuous action generation. Future prediction is recast as a latent-querying problem, where a small set of learnable foresight tokens condenses the task-relevant future into a compact latent code under the supervision of a frozen pretrained video generation model, so the policy inherits world-model dynamics priors without ever learning pixel-level generation. The video branch is discarded at inference, keeping real-time control. Pretrained on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves the best overall results on all six simulation benchmarks. In the real world, the preserved semantics deliver the strongest compositional generalization on held-out instruction bindings, and the two designs together sustain long-horizon execution.

## 개요
로봇 조작을 위한 통합 모델은 사전 훈련된 VLM의 의미적 사전 지식과 미래 예측을 통해 학습된 물리적 동역학을 하나의 정책에 탑재하는 것을 목표로 합니다. 실제로 기존 설계는 사전 훈련된 백본의 의미를 약화시키고, 이질적인 목표 간 간섭을 겪으며, 픽셀 공간에서 처음부터 미래 예측을 학습하여 사전 훈련된 비디오 생성기의 동역학 사전 지식을 활용하지 못하는 경향이 있습니다. 우리는 InternVLA-A1.5를 제시합니다. 이는 VQA 및 하위 작업 예측에 대해 지속적으로 훈련되는 네이티브 VLM 백본 위에 정책을 구축하고, 연속 동작 생성을 위한 경량 통합 전문가를 부착합니다. 미래 예측은 잠재 질의 문제로 재구성되며, 소수의 학습 가능한 예견 토큰이 동결된 사전 훈련된 비디오 생성 모델의 감독 하에 작업 관련 미래를 컴팩트한 잠재 코드로 압축하여, 정책이 픽셀 수준 생성을 학습하지 않고도 세계 모델 동역학 사전 지식을 상속받습니다. 비디오 분기는 추론 시 폐기되어 실시간 제어를 유지합니다. 120만 개의 로봇 에피소드와 300만 개의 멀티모달 샘플로 사전 훈련된 InternVLA-A1.5는 6개의 시뮬레이션 벤치마크 모두에서 최고의 종합 결과를 달성합니다. 실제 세계에서는 보존된 의미가 보류된 명령 바인딩에서 가장 강력한 구성적 일반화를 제공하며, 두 설계가 함께 장기 실행을 유지합니다.

## 핵심 내용
로봇 조작을 위한 통합 모델은 사전 훈련된 VLM의 의미적 사전 지식과 미래 예측을 통해 학습된 물리적 동역학을 하나의 정책에 탑재하는 것을 목표로 합니다. 실제로 기존 설계는 사전 훈련된 백본의 의미를 약화시키고, 이질적인 목표 간 간섭을 겪으며, 픽셀 공간에서 처음부터 미래 예측을 학습하여 사전 훈련된 비디오 생성기의 동역학 사전 지식을 활용하지 못하는 경향이 있습니다. 우리는 InternVLA-A1.5를 제시합니다. 이는 VQA 및 하위 작업 예측에 대해 지속적으로 훈련되는 네이티브 VLM 백본 위에 정책을 구축하고, 연속 동작 생성을 위한 경량 통합 전문가를 부착합니다. 미래 예측은 잠재 질의 문제로 재구성되며, 소수의 학습 가능한 예견 토큰이 동결된 사전 훈련된 비디오 생성 모델의 감독 하에 작업 관련 미래를 컴팩트한 잠재 코드로 압축하여, 정책이 픽셀 수준 생성을 학습하지 않고도 세계 모델 동역학 사전 지식을 상속받습니다. 비디오 분기는 추론 시 폐기되어 실시간 제어를 유지합니다. 120만 개의 로봇 에피소드와 300만 개의 멀티모달 샘플로 사전 훈련된 InternVLA-A1.5는 6개의 시뮬레이션 벤치마크 모두에서 최고의 종합 결과를 달성합니다. 실제 세계에서는 보존된 의미가 보류된 명령 바인딩에서 가장 강력한 구성적 일반화를 제공하며, 두 설계가 함께 장기 실행을 유지합니다.
