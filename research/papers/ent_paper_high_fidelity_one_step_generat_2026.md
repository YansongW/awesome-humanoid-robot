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
  en: "arXiv:2607.03865v1 Announce Type: new \nAbstract: Generative models such as diffusion and flow matching have advanced\
    \ robotic visuomotor policies by modeling multimodal action distributions, but their multi-step sampling or ODE solving\
    \ introduces inference latency. Existing one-step acceleration methods often compress the whole generation process into\
    \ a single large update, leading to spatial deviation, frequency distortion, and mode averaging. This paper proposes a\
    \ high-fidelity one-step generative visuomotor policy framework that addresses these issues with three complementary mechanisms.\
    \ Recursive Consistent Action Flow (RCAF) uses recursive correction to compensate for spatial truncation errors and align\
    \ one-step predictions with refined flow trajectories. Dual-Timestep Frequency Consistency (DTFC) preserves high-frequency\
    \ manipulation details through adaptive spectral consistency across flow timesteps. Contrastive Flow Matching (CFM) separates\
    \ entangled action flows with a margin-based repulsive objective, reducing ambiguous actions in multimodal manipulation.\
    \ Experiments on RoboTwin, RoboTwin 2.0, Adroit, DexArt, and real-world robot platforms show that the proposed method\
    \ achieves competitive or superior performance compared with strong 10-step generative policy baselines while requiring\
    \ only one forward pass (1 NFE), enabling low-latency visuomotor control."
  zh: "arXiv:2607.03865v1 Announce Type: new \nAbstract: Generative models such as diffusion and flow matching have advanced\
    \ robotic visuomotor policies by modeling multimodal action distributions, but their multi-step sampling or ODE solving\
    \ introduces inference latency. Existing one-step acceleration methods often compress the whole generation process into\
    \ a single large update, leading to spatial deviation, frequency distortion, and mode averaging. This paper proposes a\
    \ high-fidelity one-step generative visuomotor policy framework that addresses these issues with three complementary mechanisms.\
    \ Recursive Consistent Action Flow (RCAF) uses recursive correction to compensate for spatial truncation errors and align\
    \ one-step predictions with refined flow trajectories. Dual-Timestep Frequency Consistency (DTFC) preserves high-frequency\
    \ manipulation details through adaptive spectral consistency across flow timesteps. Contrastive Flow Matching (CFM) separates\
    \ entangled action flows with a margin-based repulsive objective, reducing ambiguous actions in multimodal manipulation.\
    \ Experiments on RoboTwin, RoboTwin 2.0, Adroit, DexArt, and real-world robot platforms show that the proposed method\
    \ achieves competitive or superior performance compared with strong 10-step generative policy baselines while requiring\
    \ only one forward pass (1 NFE), enabling low-latency visuomotor control."
  ko: "arXiv:2607.03865v1 Announce Type: new \nAbstract: Generative models such as diffusion and flow matching have advanced\
    \ robotic visuomotor policies by modeling multimodal action distributions, but their multi-step sampling or ODE solving\
    \ introduces inference latency. Existing one-step acceleration methods often compress the whole generation process into\
    \ a single large update, leading to spatial deviation, frequency distortion, and mode averaging. This paper proposes a\
    \ high-fidelity one-step generative visuomotor policy framework that addresses these issues with three complementary mechanisms.\
    \ Recursive Consistent Action Flow (RCAF) uses recursive correction to compensate for spatial truncation errors and align\
    \ one-step predictions with refined flow trajectories. Dual-Timestep Frequency Consistency (DTFC) preserves high-frequency\
    \ manipulation details through adaptive spectral consistency across flow timesteps. Contrastive Flow Matching (CFM) separates\
    \ entangled action flows with a margin-based repulsive objective, reducing ambiguous actions in multimodal manipulation.\
    \ Experiments on RoboTwin, RoboTwin 2.0, Adroit, DexArt, and real-world robot platforms show that the proposed method\
    \ achieves competitive or superior performance compared with strong 10-step generative policy baselines while requiring\
    \ only one forward pass (1 NFE), enabling low-latency visuomotor control."
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

