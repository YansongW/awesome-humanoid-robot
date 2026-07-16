---
$id: ent_paper_feeling_the_unexpected_restacv_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Feeling the Unexpected: ResTacVLA for Contact-Rich Manipulation via Residual Tactile Representation'
  zh: 'Feeling the Unexpected: ResTacVLA for Contact-Rich Manipulation via Residual Tactile Representation'
  ko: 'Feeling the Unexpected: ResTacVLA for Contact-Rich Manipulation via Residual Tactile Representation'
summary:
  en: 'arXiv:2607.03387v1 Announce Type: new Abstract: Tactile perception is indispensable for contact-rich manipulation,
    yet integrating it into Vision-Language-Action (VLA) models often induces modality collapse, where high-bandwidth visual
    features overshadow sparse tactile cues. Inspired by Predictive Coding, a neural mechanism where the brain attenuates
    predictable inputs to prioritize surprising stimuli, we propose ResTacVLA. Rather than treating tactile data as raw input,
    we reformulate it as a Residual Tactile Representation capturing the discrepancy between visual priors and physical sensations.
    By filtering out visually predictable dynamics, this formulation transforms sparse tactile signals into dense, high-value
    information gain, thereby inherently resolving the bandwidth mismatch. These residuals are discretized through a Vector
    Quantized (VQ) bottleneck into Latent Contact Primitives that capture critical events missed by vision. Analogous to the
    neural surprise signal, we leverage the uncertainty of the visual prior to adaptively gate tactile integration, prioritizing
    residuals specifically during visually unreliable phases to explicitly prevent visual dominance. Experimental results
    show that ResTacVLA consistently outperforms all baselines on a diverse set of contact-rich manipulation tasks, while
    remaining robust to unexpected dynamic disturbances. Project page: https://awilekong.github.io/ResTacVLA-Website/'
  zh: 'arXiv:2607.03387v1 Announce Type: new Abstract: Tactile perception is indispensable for contact-rich manipulation,
    yet integrating it into Vision-Language-Action (VLA) models often induces modality collapse, where high-bandwidth visual
    features overshadow sparse tactile cues. Inspired by Predictive Coding, a neural mechanism where the brain attenuates
    predictable inputs to prioritize surprising stimuli, we propose ResTacVLA. Rather than treating tactile data as raw input,
    we reformulate it as a Residual Tactile Representation capturing the discrepancy between visual priors and physical sensations.
    By filtering out visually predictable dynamics, this formulation transforms sparse tactile signals into dense, high-value
    information gain, thereby inherently resolving the bandwidth mismatch. These residuals are discretized through a Vector
    Quantized (VQ) bottleneck into Latent Contact Primitives that capture critical events missed by vision. Analogous to the
    neural surprise signal, we leverage the uncertainty of the visual prior to adaptively gate tactile integration, prioritizing
    residuals specifically during visually unreliable phases to explicitly prevent visual dominance. Experimental results
    show that ResTacVLA consistently outperforms all baselines on a diverse set of contact-rich manipulation tasks, while
    remaining robust to unexpected dynamic disturbances. Project page: https://awilekong.github.io/ResTacVLA-Website/'
  ko: 'arXiv:2607.03387v1 Announce Type: new Abstract: Tactile perception is indispensable for contact-rich manipulation,
    yet integrating it into Vision-Language-Action (VLA) models often induces modality collapse, where high-bandwidth visual
    features overshadow sparse tactile cues. Inspired by Predictive Coding, a neural mechanism where the brain attenuates
    predictable inputs to prioritize surprising stimuli, we propose ResTacVLA. Rather than treating tactile data as raw input,
    we reformulate it as a Residual Tactile Representation capturing the discrepancy between visual priors and physical sensations.
    By filtering out visually predictable dynamics, this formulation transforms sparse tactile signals into dense, high-value
    information gain, thereby inherently resolving the bandwidth mismatch. These residuals are discretized through a Vector
    Quantized (VQ) bottleneck into Latent Contact Primitives that capture critical events missed by vision. Analogous to the
    neural surprise signal, we leverage the uncertainty of the visual prior to adaptively gate tactile integration, prioritizing
    residuals specifically during visually unreliable phases to explicitly prevent visual dominance. Experimental results
    show that ResTacVLA consistently outperforms all baselines on a diverse set of contact-rich manipulation tasks, while
    remaining robust to unexpected dynamic disturbances. Project page: https://awilekong.github.io/ResTacVLA-Website/'
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
- feeling_the_unexpected
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03387v2.
sources:
- id: src_001
  type: paper
  title: 'Feeling the Unexpected: ResTacVLA for Contact-Rich Manipulation via Residual Tactile Representation (arXiv)'
  url: https://arxiv.org/abs/2607.03387
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Tactile perception is indispensable for contact-rich manipulation, yet integrating it into Vision-Language-Action (VLA) models often induces modality collapse, where high-bandwidth visual features overshadow sparse tactile cues. Inspired by Predictive Coding, a neural mechanism where the brain attenuates predictable inputs to prioritize surprising stimuli, we propose ResTacVLA. Rather than treating tactile data as raw input, we reformulate it as a Residual Tactile Representation capturing the discrepancy between visual priors and physical sensations. By filtering out visually predictable dynamics, this formulation transforms sparse tactile signals into dense, high-value information gain, thereby inherently resolving the bandwidth mismatch. These residuals are discretized through a Vector Quantized (VQ) bottleneck into Latent Contact Primitives that capture critical events missed by vision. Analogous to the neural surprise signal, we leverage the uncertainty of the visual prior to adaptively gate tactile integration, prioritizing residuals specifically during visually unreliable phases to explicitly prevent visual dominance. Experimental results show that ResTacVLA consistently outperforms all baselines on a diverse set of contact-rich manipulation tasks, while remaining robust to unexpected dynamic disturbances. Project page: https://awilekong.github.io/ResTacVLA/

## 核心内容
Tactile perception is indispensable for contact-rich manipulation, yet integrating it into Vision-Language-Action (VLA) models often induces modality collapse, where high-bandwidth visual features overshadow sparse tactile cues. Inspired by Predictive Coding, a neural mechanism where the brain attenuates predictable inputs to prioritize surprising stimuli, we propose ResTacVLA. Rather than treating tactile data as raw input, we reformulate it as a Residual Tactile Representation capturing the discrepancy between visual priors and physical sensations. By filtering out visually predictable dynamics, this formulation transforms sparse tactile signals into dense, high-value information gain, thereby inherently resolving the bandwidth mismatch. These residuals are discretized through a Vector Quantized (VQ) bottleneck into Latent Contact Primitives that capture critical events missed by vision. Analogous to the neural surprise signal, we leverage the uncertainty of the visual prior to adaptively gate tactile integration, prioritizing residuals specifically during visually unreliable phases to explicitly prevent visual dominance. Experimental results show that ResTacVLA consistently outperforms all baselines on a diverse set of contact-rich manipulation tasks, while remaining robust to unexpected dynamic disturbances. Project page: https://awilekong.github.io/ResTacVLA/

## 参考
- http://arxiv.org/abs/2607.03387v2

## Overview
Tactile perception is indispensable for contact-rich manipulation, yet integrating it into Vision-Language-Action (VLA) models often induces modality collapse, where high-bandwidth visual features overshadow sparse tactile cues. Inspired by Predictive Coding, a neural mechanism where the brain attenuates predictable inputs to prioritize surprising stimuli, we propose ResTacVLA. Rather than treating tactile data as raw input, we reformulate it as a Residual Tactile Representation capturing the discrepancy between visual priors and physical sensations. By filtering out visually predictable dynamics, this formulation transforms sparse tactile signals into dense, high-value information gain, thereby inherently resolving the bandwidth mismatch. These residuals are discretized through a Vector Quantized (VQ) bottleneck into Latent Contact Primitives that capture critical events missed by vision. Analogous to the neural surprise signal, we leverage the uncertainty of the visual prior to adaptively gate tactile integration, prioritizing residuals specifically during visually unreliable phases to explicitly prevent visual dominance. Experimental results show that ResTacVLA consistently outperforms all baselines on a diverse set of contact-rich manipulation tasks, while remaining robust to unexpected dynamic disturbances. Project page: https://awilekong.github.io/ResTacVLA/

## Content
Tactile perception is indispensable for contact-rich manipulation, yet integrating it into Vision-Language-Action (VLA) models often induces modality collapse, where high-bandwidth visual features overshadow sparse tactile cues. Inspired by Predictive Coding, a neural mechanism where the brain attenuates predictable inputs to prioritize surprising stimuli, we propose ResTacVLA. Rather than treating tactile data as raw input, we reformulate it as a Residual Tactile Representation capturing the discrepancy between visual priors and physical sensations. By filtering out visually predictable dynamics, this formulation transforms sparse tactile signals into dense, high-value information gain, thereby inherently resolving the bandwidth mismatch. These residuals are discretized through a Vector Quantized (VQ) bottleneck into Latent Contact Primitives that capture critical events missed by vision. Analogous to the neural surprise signal, we leverage the uncertainty of the visual prior to adaptively gate tactile integration, prioritizing residuals specifically during visually unreliable phases to explicitly prevent visual dominance. Experimental results show that ResTacVLA consistently outperforms all baselines on a diverse set of contact-rich manipulation tasks, while remaining robust to unexpected dynamic disturbances. Project page: https://awilekong.github.io/ResTacVLA/

## 개요
촉각 인식은 접촉이 많은 조작 작업에 필수적이지만, 이를 Vision-Language-Action(VLA) 모델에 통합하면 고대역폭의 시각적 특징이 희소한 촉각 신호를 압도하는 모달리티 붕괴가 자주 발생합니다. 뇌가 예측 가능한 입력을 약화시켜 놀라운 자극을 우선 처리하는 신경 메커니즘인 예측 코딩(Predictive Coding)에서 영감을 받아, 우리는 ResTacVLA를 제안합니다. 촉각 데이터를 원시 입력으로 처리하는 대신, 시각적 사전 정보와 물리적 감각 간의 차이를 포착하는 잔차 촉각 표현(Residual Tactile Representation)으로 재구성합니다. 시각적으로 예측 가능한 동역학을 걸러냄으로써, 이 공식은 희소한 촉각 신호를 밀집된 고가치 정보 이득으로 변환하여 대역폭 불일치를 본질적으로 해결합니다. 이러한 잔차는 벡터 양자화(VQ) 병목을 통해 잠재 접촉 원시(Latent Contact Primitives)로 이산화되어 시각이 놓친 중요한 이벤트를 포착합니다. 신경 놀람 신호와 유사하게, 우리는 시각적 사전 정보의 불확실성을 활용하여 촉각 통합을 적응적으로 게이팅하며, 특히 시각적으로 신뢰할 수 없는 단계에서 잔차를 우선 처리하여 시각적 우세를 명시적으로 방지합니다. 실험 결과, ResTacVLA는 다양한 접촉이 많은 조작 작업에서 모든 기준 모델을 일관되게 능가하며, 예상치 못한 동적 교란에도 강건함을 보여줍니다. 프로젝트 페이지: https://awilekong.github.io/ResTacVLA/

## 핵심 내용
촉각 인식은 접촉이 많은 조작 작업에 필수적이지만, 이를 Vision-Language-Action(VLA) 모델에 통합하면 고대역폭의 시각적 특징이 희소한 촉각 신호를 압도하는 모달리티 붕괴가 자주 발생합니다. 뇌가 예측 가능한 입력을 약화시켜 놀라운 자극을 우선 처리하는 신경 메커니즘인 예측 코딩(Predictive Coding)에서 영감을 받아, 우리는 ResTacVLA를 제안합니다. 촉각 데이터를 원시 입력으로 처리하는 대신, 시각적 사전 정보와 물리적 감각 간의 차이를 포착하는 잔차 촉각 표현(Residual Tactile Representation)으로 재구성합니다. 시각적으로 예측 가능한 동역학을 걸러냄으로써, 이 공식은 희소한 촉각 신호를 밀집된 고가치 정보 이득으로 변환하여 대역폭 불일치를 본질적으로 해결합니다. 이러한 잔차는 벡터 양자화(VQ) 병목을 통해 잠재 접촉 원시(Latent Contact Primitives)로 이산화되어 시각이 놓친 중요한 이벤트를 포착합니다. 신경 놀람 신호와 유사하게, 우리는 시각적 사전 정보의 불확실성을 활용하여 촉각 통합을 적응적으로 게이팅하며, 특히 시각적으로 신뢰할 수 없는 단계에서 잔차를 우선 처리하여 시각적 우세를 명시적으로 방지합니다. 실험 결과, ResTacVLA는 다양한 접촉이 많은 조작 작업에서 모든 기준 모델을 일관되게 능가하며, 예상치 못한 동적 교란에도 강건함을 보여줍니다. 프로젝트 페이지: https://awilekong.github.io/ResTacVLA/
