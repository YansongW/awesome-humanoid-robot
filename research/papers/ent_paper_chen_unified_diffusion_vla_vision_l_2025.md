---
$id: ent_paper_chen_unified_diffusion_vla_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process'
  zh: UD-VLA
  ko: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process'
summary:
  en: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process (UD-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Westlake University, Zhejiang University,
    Monash University.'
  zh: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process (UD-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Westlake University, Zhejiang University,
    Monash University.'
  ko: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process (UD-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Westlake University, Zhejiang University,
    Monash University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- ud_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.01718v2.
sources:
- id: src_001
  type: paper
  title: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process (arXiv)'
  url: https://arxiv.org/abs/2511.01718
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UD-VLA source
  url: https://doi.org/10.48550/arXiv.2511.01718
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models aim to understand natural language instructions and visual observations and to execute corresponding actions as an embodied agent. Recent work integrates future images into the understanding-acting loop, yielding unified VLAs that jointly understand, generate, and act -- reading text and images and producing future images and actions. However, these models either rely on external experts for modality unification or treat image generation and action prediction as separate processes, limiting the benefits of direct synergy between these tasks. Our core philosophy is to optimize generation and action jointly through a synchronous denoising process, where the iterative refinement enables actions to evolve from initialization, under constant and sufficient visual guidance. We ground this philosophy in our proposed Unified Diffusion VLA and Joint Discrete Denoising Diffusion Process (JD3P), which is a joint diffusion process that integrates multiple modalities into a single denoising trajectory to serve as the key mechanism enabling understanding, generation, and acting to be intrinsically synergistic. Our model and theory are built on a unified tokenized space of all modalities and a hybrid attention mechanism. We further propose a two-stage training pipeline and several inference-time techniques that optimize performance and efficiency. Our approach achieves state-of-the-art performance on benchmarks such as CALVIN, LIBERO, and SimplerEnv with 4$\times$ faster inference than autoregressive methods, and we demonstrate its effectiveness through in-depth analysis and real-world evaluations. Our project page is available at https://irpn-eai.github.io/UD-VLA.github.io/.

## 核心内容
Vision-language-action (VLA) models aim to understand natural language instructions and visual observations and to execute corresponding actions as an embodied agent. Recent work integrates future images into the understanding-acting loop, yielding unified VLAs that jointly understand, generate, and act -- reading text and images and producing future images and actions. However, these models either rely on external experts for modality unification or treat image generation and action prediction as separate processes, limiting the benefits of direct synergy between these tasks. Our core philosophy is to optimize generation and action jointly through a synchronous denoising process, where the iterative refinement enables actions to evolve from initialization, under constant and sufficient visual guidance. We ground this philosophy in our proposed Unified Diffusion VLA and Joint Discrete Denoising Diffusion Process (JD3P), which is a joint diffusion process that integrates multiple modalities into a single denoising trajectory to serve as the key mechanism enabling understanding, generation, and acting to be intrinsically synergistic. Our model and theory are built on a unified tokenized space of all modalities and a hybrid attention mechanism. We further propose a two-stage training pipeline and several inference-time techniques that optimize performance and efficiency. Our approach achieves state-of-the-art performance on benchmarks such as CALVIN, LIBERO, and SimplerEnv with 4$\times$ faster inference than autoregressive methods, and we demonstrate its effectiveness through in-depth analysis and real-world evaluations. Our project page is available at https://irpn-eai.github.io/UD-VLA.github.io/.

## 参考
- http://arxiv.org/abs/2511.01718v2

