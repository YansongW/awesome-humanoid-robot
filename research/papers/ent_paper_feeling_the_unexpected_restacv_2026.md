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

