---
$id: ent_paper_zhan_mathcale_0_enhancing_generaliz_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '$\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion'
  zh: Epsilon0
  ko: '$\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion'
summary:
  en: '$\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion
    (Epsilon0), is a 2025 large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University,
    Guangdong Key Laboratory of Big Data Analysis and Processing, X-Era AI Lab, Guangdong University of Technology.'
  zh: '$\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion
    (Epsilon0), is a 2025 large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University,
    Guangdong Key Laboratory of Big Data Analysis and Processing, X-Era AI Lab, Guangdong University of Technology.'
  ko: '$\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion
    (Epsilon0), is a 2025 large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University,
    Guangdong Key Laboratory of Big Data Analysis and Processing, X-Era AI Lab, Guangdong University of Technology.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- epsilon0
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.21542v2.
sources:
- id: src_001
  type: paper
  title: '$\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion
    (arXiv)'
  url: https://arxiv.org/abs/2511.21542
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Epsilon0 source
  url: https://doi.org/10.48550/arXiv.2511.21542
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models offer a unified framework for robotic manipulation by integrating visual perception, language understanding, and control generation. However, existing VLA systems still struggle to generalize across diverse tasks, scenes, and camera viewpoints, and often produce coarse or unstable actions. We argue that these limitations are closely tied to the structural properties of actions in VLA settings, including the inherent multi-peaked nature of action distributions, the token-based symbolic reasoning of pretrained VLM/VLA backbones, and the effective finite resolution imposed by real-world robotic control. Motivated by these properties, we introduce E0, a tweedie discrete diffusion framework that formulates action generation as iterative denoising over quantized action tokens. By operating in a discrete action space with a principled diffusion process, E0 naturally aligns with token-based reasoning, supports fine-grained yet executable action control, and avoids the distributional mismatch of masking-based discrete diffusion. We further introduce a spherical viewpoint perturbation augmentation to enhance robustness to camera shifts without additional data. Experiments on LIBERO, VLABench, ManiSkill, and a real-world Franka arm demonstrate that E0 achieves state-of-the-art performance across 14 diverse environments, outperforming strong baselines by 10.7% on average.

## 核心内容
Vision-Language-Action (VLA) models offer a unified framework for robotic manipulation by integrating visual perception, language understanding, and control generation. However, existing VLA systems still struggle to generalize across diverse tasks, scenes, and camera viewpoints, and often produce coarse or unstable actions. We argue that these limitations are closely tied to the structural properties of actions in VLA settings, including the inherent multi-peaked nature of action distributions, the token-based symbolic reasoning of pretrained VLM/VLA backbones, and the effective finite resolution imposed by real-world robotic control. Motivated by these properties, we introduce E0, a tweedie discrete diffusion framework that formulates action generation as iterative denoising over quantized action tokens. By operating in a discrete action space with a principled diffusion process, E0 naturally aligns with token-based reasoning, supports fine-grained yet executable action control, and avoids the distributional mismatch of masking-based discrete diffusion. We further introduce a spherical viewpoint perturbation augmentation to enhance robustness to camera shifts without additional data. Experiments on LIBERO, VLABench, ManiSkill, and a real-world Franka arm demonstrate that E0 achieves state-of-the-art performance across 14 diverse environments, outperforming strong baselines by 10.7% on average.

## 参考
- http://arxiv.org/abs/2511.21542v2

