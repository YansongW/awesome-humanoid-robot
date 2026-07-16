---
$id: ent_paper_wam4d_fast_4d_world_action_mod_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WAM4D: Fast 4D World Action Model via Spatial Register Tokens'
  zh: 'WAM4D: Fast 4D World Action Model via Spatial Register Tokens'
  ko: 'WAM4D: Fast 4D World Action Model via Spatial Register Tokens'
summary:
  en: 'arXiv:2606.14048v2 Announce Type: replace-cross Abstract: World action models (WAMs) have recently shown promise in
    jointly modeling future observations and executable robot actions. However, most existing WAMs still operate in 2D video
    or latent spaces, where visually plausible rollouts miss the 3D spatial constraints and occluded contact geometry required
    for precise manipulation. While geometric foundation models offer strong priors for recovering dense 3D structure and
    motion from visual observations, forcing WAMs to predict the dense 4D representation introduces costly geometric decoding
    and slows down causal action generation. To address the trade-off, we present WAM4D, a fast 4D world action model that
    uses lightweight spatial register tokens as training-time future-depth readouts to transfer pretrained geometric priors
    into a causal video-action transformer, then removes the register branch for lightweight action inference. To prevent
    non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone, defining
    modality-specific visibility among video, action, and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging
    real-world manipulation tasks show that WAM4D improves spatial consistency and achieves competitive action prediction
    while maintaining efficient inference.'
  zh: 'arXiv:2606.14048v2 Announce Type: replace-cross Abstract: World action models (WAMs) have recently shown promise in
    jointly modeling future observations and executable robot actions. However, most existing WAMs still operate in 2D video
    or latent spaces, where visually plausible rollouts miss the 3D spatial constraints and occluded contact geometry required
    for precise manipulation. While geometric foundation models offer strong priors for recovering dense 3D structure and
    motion from visual observations, forcing WAMs to predict the dense 4D representation introduces costly geometric decoding
    and slows down causal action generation. To address the trade-off, we present WAM4D, a fast 4D world action model that
    uses lightweight spatial register tokens as training-time future-depth readouts to transfer pretrained geometric priors
    into a causal video-action transformer, then removes the register branch for lightweight action inference. To prevent
    non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone, defining
    modality-specific visibility among video, action, and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging
    real-world manipulation tasks show that WAM4D improves spatial consistency and achieves competitive action prediction
    while maintaining efficient inference.'
  ko: 'arXiv:2606.14048v2 Announce Type: replace-cross Abstract: World action models (WAMs) have recently shown promise in
    jointly modeling future observations and executable robot actions. However, most existing WAMs still operate in 2D video
    or latent spaces, where visually plausible rollouts miss the 3D spatial constraints and occluded contact geometry required
    for precise manipulation. While geometric foundation models offer strong priors for recovering dense 3D structure and
    motion from visual observations, forcing WAMs to predict the dense 4D representation introduces costly geometric decoding
    and slows down causal action generation. To address the trade-off, we present WAM4D, a fast 4D world action model that
    uses lightweight spatial register tokens as training-time future-depth readouts to transfer pretrained geometric priors
    into a causal video-action transformer, then removes the register branch for lightweight action inference. To prevent
    non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone, defining
    modality-specific visibility among video, action, and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging
    real-world manipulation tasks show that WAM4D improves spatial consistency and achieves competitive action prediction
    while maintaining efficient inference.'
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
- wam4d
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.14048v3.
sources:
- id: src_001
  type: paper
  title: 'WAM4D: Fast 4D World Action Model via Spatial Register Tokens (arXiv)'
  url: https://arxiv.org/abs/2606.14048
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
World action models (WAMs) have recently shown promise in jointly modeling future observations and executable robot actions. However, most existing WAMs still operate in 2D video or latent spaces, where visually plausible rollouts miss the 3D spatial constraints and occluded contact geometry required for precise manipulation. While geometric foundation models offer strong priors for recovering dense 3D structure and motion from visual observations, forcing WAMs to predict the dense 4D representation introduces costly geometric decoding and slows down causal action generation. To address the trade-off, we present WAM4D, a fast 4D world action model that uses lightweight spatial register tokens as training-time future-depth readouts to transfer pretrained geometric priors into a causal video-action transformer, then removes the register branch for lightweight action inference. To prevent non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone, defining modality-specific visibility among video, action, and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging real-world manipulation tasks show that WAM4D improves spatial consistency and achieves competitive action prediction while maintaining efficient inference.

## 核心内容
World action models (WAMs) have recently shown promise in jointly modeling future observations and executable robot actions. However, most existing WAMs still operate in 2D video or latent spaces, where visually plausible rollouts miss the 3D spatial constraints and occluded contact geometry required for precise manipulation. While geometric foundation models offer strong priors for recovering dense 3D structure and motion from visual observations, forcing WAMs to predict the dense 4D representation introduces costly geometric decoding and slows down causal action generation. To address the trade-off, we present WAM4D, a fast 4D world action model that uses lightweight spatial register tokens as training-time future-depth readouts to transfer pretrained geometric priors into a causal video-action transformer, then removes the register branch for lightweight action inference. To prevent non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone, defining modality-specific visibility among video, action, and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging real-world manipulation tasks show that WAM4D improves spatial consistency and achieves competitive action prediction while maintaining efficient inference.

## 参考
- http://arxiv.org/abs/2606.14048v3

## Overview
World action models (WAMs) have recently shown promise in jointly modeling future observations and executable robot actions. However, most existing WAMs still operate in 2D video or latent spaces, where visually plausible rollouts miss the 3D spatial constraints and occluded contact geometry required for precise manipulation. While geometric foundation models offer strong priors for recovering dense 3D structure and motion from visual observations, forcing WAMs to predict the dense 4D representation introduces costly geometric decoding and slows down causal action generation. To address the trade-off, we present WAM4D, a fast 4D world action model that uses lightweight spatial register tokens as training-time future-depth readouts to transfer pretrained geometric priors into a causal video-action transformer, then removes the register branch for lightweight action inference. To prevent non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone, defining modality-specific visibility among video, action, and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging real-world manipulation tasks show that WAM4D improves spatial consistency and achieves competitive action prediction while maintaining efficient inference.

## Content
World action models (WAMs) have recently shown promise in jointly modeling future observations and executable robot actions. However, most existing WAMs still operate in 2D video or latent spaces, where visually plausible rollouts miss the 3D spatial constraints and occluded contact geometry required for precise manipulation. While geometric foundation models offer strong priors for recovering dense 3D structure and motion from visual observations, forcing WAMs to predict the dense 4D representation introduces costly geometric decoding and slows down causal action generation. To address the trade-off, we present WAM4D, a fast 4D world action model that uses lightweight spatial register tokens as training-time future-depth readouts to transfer pretrained geometric priors into a causal video-action transformer, then removes the register branch for lightweight action inference. To prevent non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone, defining modality-specific visibility among video, action, and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging real-world manipulation tasks show that WAM4D improves spatial consistency and achieves competitive action prediction while maintaining efficient inference.

## 개요
World action models (WAMs)는 최근 미래 관측과 실행 가능한 로봇 동작을 공동으로 모델링하는 데 유망한 성과를 보여주고 있습니다. 그러나 대부분의 기존 WAM은 여전히 2D 비디오 또는 잠재 공간에서 작동하며, 시각적으로 그럴듯한 롤아웃은 정밀한 조작에 필요한 3D 공간 제약과 가려진 접촉 기하학을 놓치고 있습니다. 기하학 기반 모델은 시각적 관측에서 밀집된 3D 구조와 움직임을 복원하기 위한 강력한 사전 지식을 제공하지만, WAM이 밀집된 4D 표현을 예측하도록 강제하면 비용이 많이 드는 기하학적 디코딩이 도입되고 인과적 동작 생성이 느려집니다. 이러한 트레이드오프를 해결하기 위해, 우리는 WAM4D를 제안합니다. 이는 경량 공간 레지스터 토큰을 훈련 시간 미래 깊이 판독값으로 사용하여 사전 훈련된 기하학적 사전 지식을 인과적 비디오-동작 트랜스포머로 전이한 후, 레지스터 브랜치를 제거하여 경량 동작 추론을 수행하는 빠른 4D 월드 액션 모델입니다. 비인과적 지름길을 방지하기 위해, 우리는 Mixture-of-Transformers (MoT) WAM 백본을 위한 인과적 혼합 어텐션을 추가로 설계하여 비디오, 동작 및 기하학 토큰 간의 모달리티별 가시성을 정의합니다. RoboTwin 2.0 및 도전적인 실제 세계 조작 작업에 대한 포괄적인 실험은 WAM4D가 공간 일관성을 개선하고 효율적인 추론을 유지하면서 경쟁력 있는 동작 예측을 달성함을 보여줍니다.

## 핵심 내용
World action models (WAMs)는 최근 미래 관측과 실행 가능한 로봇 동작을 공동으로 모델링하는 데 유망한 성과를 보여주고 있습니다. 그러나 대부분의 기존 WAM은 여전히 2D 비디오 또는 잠재 공간에서 작동하며, 시각적으로 그럴듯한 롤아웃은 정밀한 조작에 필요한 3D 공간 제약과 가려진 접촉 기하학을 놓치고 있습니다. 기하학 기반 모델은 시각적 관측에서 밀집된 3D 구조와 움직임을 복원하기 위한 강력한 사전 지식을 제공하지만, WAM이 밀집된 4D 표현을 예측하도록 강제하면 비용이 많이 드는 기하학적 디코딩이 도입되고 인과적 동작 생성이 느려집니다. 이러한 트레이드오프를 해결하기 위해, 우리는 WAM4D를 제안합니다. 이는 경량 공간 레지스터 토큰을 훈련 시간 미래 깊이 판독값으로 사용하여 사전 훈련된 기하학적 사전 지식을 인과적 비디오-동작 트랜스포머로 전이한 후, 레지스터 브랜치를 제거하여 경량 동작 추론을 수행하는 빠른 4D 월드 액션 모델입니다. 비인과적 지름길을 방지하기 위해, 우리는 Mixture-of-Transformers (MoT) WAM 백본을 위한 인과적 혼합 어텐션을 추가로 설계하여 비디오, 동작 및 기하학 토큰 간의 모달리티별 가시성을 정의합니다. RoboTwin 2.0 및 도전적인 실제 세계 조작 작업에 대한 포괄적인 실험은 WAM4D가 공간 일관성을 개선하고 효율적인 추론을 유지하면서 경쟁력 있는 동작 예측을 달성함을 보여줍니다.
