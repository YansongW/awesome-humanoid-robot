---
$id: ent_paper_ultra_unified_multimodal_contr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation'
  zh: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation'
  ko: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation'
summary:
  en: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- loco_manipulation
- ultra
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.03279v1.
sources:
- id: src_001
  type: paper
  title: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation (arXiv)'
  url: https://arxiv.org/abs/2603.03279
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation project page'
  url: https://ultra-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Achieving autonomous and versatile whole-body loco-manipulation remains a central barrier to making humanoids practically useful. Yet existing approaches are fundamentally constrained: retargeted data are often scarce or low-quality; methods struggle to scale to large skill repertoires; and, most importantly, they rely on tracking predefined motion references rather than generating behavior from perception and high-level task specifications. To address these limitations, we propose ULTRA, a unified framework with two key components. First, we introduce a physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions. Second, we learn a unified multimodal controller that supports both dense references and sparse task specifications, under sensing ranging from accurate motion-capture state to noisy egocentric visual inputs. We distill a universal tracking policy into this controller, compress motor skills into a compact latent space, and apply reinforcement learning finetuning to expand coverage and improve robustness under out-of-distribution scenarios. This enables coordinated whole-body behavior from sparse intent without test-time reference motions. We evaluate ULTRA in simulation and on a real Unitree G1 humanoid. Results show that ULTRA generalizes to autonomous, goal-conditioned whole-body loco-manipulation from egocentric perception, consistently outperforming tracking-only baselines with limited skills.

## 核心内容
Achieving autonomous and versatile whole-body loco-manipulation remains a central barrier to making humanoids practically useful. Yet existing approaches are fundamentally constrained: retargeted data are often scarce or low-quality; methods struggle to scale to large skill repertoires; and, most importantly, they rely on tracking predefined motion references rather than generating behavior from perception and high-level task specifications. To address these limitations, we propose ULTRA, a unified framework with two key components. First, we introduce a physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions. Second, we learn a unified multimodal controller that supports both dense references and sparse task specifications, under sensing ranging from accurate motion-capture state to noisy egocentric visual inputs. We distill a universal tracking policy into this controller, compress motor skills into a compact latent space, and apply reinforcement learning finetuning to expand coverage and improve robustness under out-of-distribution scenarios. This enables coordinated whole-body behavior from sparse intent without test-time reference motions. We evaluate ULTRA in simulation and on a real Unitree G1 humanoid. Results show that ULTRA generalizes to autonomous, goal-conditioned whole-body loco-manipulation from egocentric perception, consistently outperforming tracking-only baselines with limited skills.

## 参考
- http://arxiv.org/abs/2603.03279v1

