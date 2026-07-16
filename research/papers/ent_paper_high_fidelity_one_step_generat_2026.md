---
$id: ent_paper_high_fidelity_one_step_generat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: High-Fidelity One-Step Generative Visuomotor Policy via Recursive Correction, Frequency Consistency, and Contrastive
    Flow Matching
  zh: High-Fidelity One-Step Generative Visuomotor Policy via Recursive Correction, Frequency Consistency, and Contrastive
    Flow Matching
  ko: High-Fidelity One-Step Generative Visuomotor Policy via Recursive Correction, Frequency Consistency, and Contrastive
    Flow Matching
summary:
  en: 'arXiv:2607.03865v1 Announce Type: new Abstract: Generative models such as diffusion and flow matching have advanced
    robotic visuomotor policies by modeling multimodal action distributions, but their multi-step sampling or ODE solving
    introduces inference latency. Existing one-step acceleration methods often compress the whole generation process into
    a single large update, leading to spatial deviation, frequency distortion, and mode averaging. This paper proposes a high-fidelity
    one-step generative visuomotor policy framework that addresses these issues with three complementary mechanisms. Recursive
    Consistent Action Flow (RCAF) uses recursive correction to compensate for spatial truncation errors and align one-step
    predictions with refined flow trajectories. Dual-Timestep Frequency Consistency (DTFC) preserves high-frequency manipulation
    details through adaptive spectral consistency across flow timesteps. Contrastive Flow Matching (CFM) separates entangled
    action flows with a margin-based repulsive objective, reducing ambiguous actions in multimodal manipulation. Experiments
    on RoboTwin, RoboTwin 2.0, Adroit, DexArt, and real-world robot platforms show that the proposed method achieves competitive
    or superior performance compared with strong 10-step generative policy baselines while requiring only one forward pass
    (1 NFE), enabling low-latency visuomotor control.'
  zh: 'arXiv:2607.03865v1 Announce Type: new Abstract: Generative models such as diffusion and flow matching have advanced
    robotic visuomotor policies by modeling multimodal action distributions, but their multi-step sampling or ODE solving
    introduces inference latency. Existing one-step acceleration methods often compress the whole generation process into
    a single large update, leading to spatial deviation, frequency distortion, and mode averaging. This paper proposes a high-fidelity
    one-step generative visuomotor policy framework that addresses these issues with three complementary mechanisms. Recursive
    Consistent Action Flow (RCAF) uses recursive correction to compensate for spatial truncation errors and align one-step
    predictions with refined flow trajectories. Dual-Timestep Frequency Consistency (DTFC) preserves high-frequency manipulation
    details through adaptive spectral consistency across flow timesteps. Contrastive Flow Matching (CFM) separates entangled
    action flows with a margin-based repulsive objective, reducing ambiguous actions in multimodal manipulation. Experiments
    on RoboTwin, RoboTwin 2.0, Adroit, DexArt, and real-world robot platforms show that the proposed method achieves competitive
    or superior performance compared with strong 10-step generative policy baselines while requiring only one forward pass
    (1 NFE), enabling low-latency visuomotor control.'
  ko: 'arXiv:2607.03865v1 Announce Type: new Abstract: Generative models such as diffusion and flow matching have advanced
    robotic visuomotor policies by modeling multimodal action distributions, but their multi-step sampling or ODE solving
    introduces inference latency. Existing one-step acceleration methods often compress the whole generation process into
    a single large update, leading to spatial deviation, frequency distortion, and mode averaging. This paper proposes a high-fidelity
    one-step generative visuomotor policy framework that addresses these issues with three complementary mechanisms. Recursive
    Consistent Action Flow (RCAF) uses recursive correction to compensate for spatial truncation errors and align one-step
    predictions with refined flow trajectories. Dual-Timestep Frequency Consistency (DTFC) preserves high-frequency manipulation
    details through adaptive spectral consistency across flow timesteps. Contrastive Flow Matching (CFM) separates entangled
    action flows with a margin-based repulsive objective, reducing ambiguous actions in multimodal manipulation. Experiments
    on RoboTwin, RoboTwin 2.0, Adroit, DexArt, and real-world robot platforms show that the proposed method achieves competitive
    or superior performance compared with strong 10-step generative policy baselines while requiring only one forward pass
    (1 NFE), enabling low-latency visuomotor control.'
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
- high_fidelity_one_step_generat
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03865v1.
sources:
- id: src_001
  type: paper
  title: High-Fidelity One-Step Generative Visuomotor Policy via Recursive Correction, Frequency Consistency, and Contrastive
    Flow Matching (arXiv)
  url: https://arxiv.org/abs/2607.03865
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Generative models such as diffusion and flow matching have advanced robotic visuomotor policies by modeling multimodal action distributions, but their multi-step sampling or ODE solving introduces inference latency. Existing one-step acceleration methods often compress the whole generation process into a single large update, leading to spatial deviation, frequency distortion, and mode averaging. This paper proposes a high-fidelity one-step generative visuomotor policy framework that addresses these issues with three complementary mechanisms. Recursive Consistent Action Flow (RCAF) uses recursive correction to compensate for spatial truncation errors and align one-step predictions with refined flow trajectories. Dual-Timestep Frequency Consistency (DTFC) preserves high-frequency manipulation details through adaptive spectral consistency across flow timesteps. Contrastive Flow Matching (CFM) separates entangled action flows with a margin-based repulsive objective, reducing ambiguous actions in multimodal manipulation. Experiments on RoboTwin, RoboTwin 2.0, Adroit, DexArt, and real-world robot platforms show that the proposed method achieves competitive or superior performance compared with strong 10-step generative policy baselines while requiring only one forward pass (1 NFE), enabling low-latency visuomotor control.

## 核心内容
Generative models such as diffusion and flow matching have advanced robotic visuomotor policies by modeling multimodal action distributions, but their multi-step sampling or ODE solving introduces inference latency. Existing one-step acceleration methods often compress the whole generation process into a single large update, leading to spatial deviation, frequency distortion, and mode averaging. This paper proposes a high-fidelity one-step generative visuomotor policy framework that addresses these issues with three complementary mechanisms. Recursive Consistent Action Flow (RCAF) uses recursive correction to compensate for spatial truncation errors and align one-step predictions with refined flow trajectories. Dual-Timestep Frequency Consistency (DTFC) preserves high-frequency manipulation details through adaptive spectral consistency across flow timesteps. Contrastive Flow Matching (CFM) separates entangled action flows with a margin-based repulsive objective, reducing ambiguous actions in multimodal manipulation. Experiments on RoboTwin, RoboTwin 2.0, Adroit, DexArt, and real-world robot platforms show that the proposed method achieves competitive or superior performance compared with strong 10-step generative policy baselines while requiring only one forward pass (1 NFE), enabling low-latency visuomotor control.

## 参考
- http://arxiv.org/abs/2607.03865v1

## Overview
Generative models such as diffusion and flow matching have advanced robotic visuomotor policies by modeling multimodal action distributions, but their multi-step sampling or ODE solving introduces inference latency. Existing one-step acceleration methods often compress the whole generation process into a single large update, leading to spatial deviation, frequency distortion, and mode averaging. This paper proposes a high-fidelity one-step generative visuomotor policy framework that addresses these issues with three complementary mechanisms. Recursive Consistent Action Flow (RCAF) uses recursive correction to compensate for spatial truncation errors and align one-step predictions with refined flow trajectories. Dual-Timestep Frequency Consistency (DTFC) preserves high-frequency manipulation details through adaptive spectral consistency across flow timesteps. Contrastive Flow Matching (CFM) separates entangled action flows with a margin-based repulsive objective, reducing ambiguous actions in multimodal manipulation. Experiments on RoboTwin, RoboTwin 2.0, Adroit, DexArt, and real-world robot platforms show that the proposed method achieves competitive or superior performance compared with strong 10-step generative policy baselines while requiring only one forward pass (1 NFE), enabling low-latency visuomotor control.

## Content
Generative models such as diffusion and flow matching have advanced robotic visuomotor policies by modeling multimodal action distributions, but their multi-step sampling or ODE solving introduces inference latency. Existing one-step acceleration methods often compress the whole generation process into a single large update, leading to spatial deviation, frequency distortion, and mode averaging. This paper proposes a high-fidelity one-step generative visuomotor policy framework that addresses these issues with three complementary mechanisms. Recursive Consistent Action Flow (RCAF) uses recursive correction to compensate for spatial truncation errors and align one-step predictions with refined flow trajectories. Dual-Timestep Frequency Consistency (DTFC) preserves high-frequency manipulation details through adaptive spectral consistency across flow timesteps. Contrastive Flow Matching (CFM) separates entangled action flows with a margin-based repulsive objective, reducing ambiguous actions in multimodal manipulation. Experiments on RoboTwin, RoboTwin 2.0, Adroit, DexArt, and real-world robot platforms show that the proposed method achieves competitive or superior performance compared with strong 10-step generative policy baselines while requiring only one forward pass (1 NFE), enabling low-latency visuomotor control.

## 개요
확산(diffusion) 및 흐름 매칭(flow matching)과 같은 생성 모델은 다중 모드 행동 분포를 모델링하여 로봇 시각-운동 정책을 발전시켰지만, 다단계 샘플링 또는 ODE 풀이 과정에서 추론 지연이 발생합니다. 기존의 단일 단계 가속 방법은 종종 전체 생성 과정을 하나의 큰 업데이트로 압축하여 공간적 편차, 주파수 왜곡 및 모드 평균화를 초래합니다. 본 논문은 이러한 문제를 세 가지 상호 보완 메커니즘으로 해결하는 고충실도 단일 단계 생성 시각-운동 정책 프레임워크를 제안합니다. 재귀적 일관성 있는 행동 흐름(RCAF)은 재귀적 보정을 사용하여 공간적 절단 오차를 보상하고 단일 단계 예측을 정제된 흐름 궤적과 정렬합니다. 이중 시간 단계 주파수 일관성(DTFC)은 흐름 시간 단계에 걸친 적응형 스펙트럼 일관성을 통해 고주파수 조작 세부 사항을 보존합니다. 대조적 흐름 매칭(CFM)은 마진 기반 반발 목표를 사용하여 얽힌 행동 흐름을 분리함으로써 다중 모드 조작에서 모호한 행동을 줄입니다. RoboTwin, RoboTwin 2.0, Adroit, DexArt 및 실제 로봇 플랫폼에서의 실험 결과, 제안된 방법은 단 한 번의 순방향 패스(1 NFE)만 필요로 하면서 강력한 10단계 생성 정책 기준선과 비교하여 경쟁력 있거나 우수한 성능을 달성하여 저지연 시각-운동 제어를 가능하게 합니다.

## 핵심 내용
확산(diffusion) 및 흐름 매칭(flow matching)과 같은 생성 모델은 다중 모드 행동 분포를 모델링하여 로봇 시각-운동 정책을 발전시켰지만, 다단계 샘플링 또는 ODE 풀이 과정에서 추론 지연이 발생합니다. 기존의 단일 단계 가속 방법은 종종 전체 생성 과정을 하나의 큰 업데이트로 압축하여 공간적 편차, 주파수 왜곡 및 모드 평균화를 초래합니다. 본 논문은 이러한 문제를 세 가지 상호 보완 메커니즘으로 해결하는 고충실도 단일 단계 생성 시각-운동 정책 프레임워크를 제안합니다. 재귀적 일관성 있는 행동 흐름(RCAF)은 재귀적 보정을 사용하여 공간적 절단 오차를 보상하고 단일 단계 예측을 정제된 흐름 궤적과 정렬합니다. 이중 시간 단계 주파수 일관성(DTFC)은 흐름 시간 단계에 걸친 적응형 스펙트럼 일관성을 통해 고주파수 조작 세부 사항을 보존합니다. 대조적 흐름 매칭(CFM)은 마진 기반 반발 목표를 사용하여 얽힌 행동 흐름을 분리함으로써 다중 모드 조작에서 모호한 행동을 줄입니다. RoboTwin, RoboTwin 2.0, Adroit, DexArt 및 실제 로봇 플랫폼에서의 실험 결과, 제안된 방법은 단 한 번의 순방향 패스(1 NFE)만 필요로 하면서 강력한 10단계 생성 정책 기준선과 비교하여 경쟁력 있거나 우수한 성능을 달성하여 저지연 시각-운동 제어를 가능하게 합니다.
