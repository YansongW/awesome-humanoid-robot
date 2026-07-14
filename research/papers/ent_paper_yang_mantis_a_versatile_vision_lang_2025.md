---
$id: ent_paper_yang_mantis_a_versatile_vision_lang_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight'
  zh: Mantis
  ko: 'Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight'
summary:
  en: 'Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight (Mantis), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, SII, Nanjing University of Posts and Telecommunications,
    Fudan University, Bosch.'
  zh: 'Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight (Mantis), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, SII, Nanjing University of Posts and Telecommunications,
    Fudan University, Bosch.'
  ko: 'Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight (Mantis), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, SII, Nanjing University of Posts and Telecommunications,
    Fudan University, Bosch.'
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
- mantis
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16175v2.
sources:
- id: src_001
  type: paper
  title: 'Mantis: A Versatile Vision-Language-Action Model with Disentangled Visual Foresight (arXiv)'
  url: https://arxiv.org/abs/2511.16175
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Mantis source
  url: https://doi.org/10.48550/arXiv.2511.16175
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in Vision-Language-Action (VLA) models demonstrate that visual signals can effectively complement sparse action supervisions. However, letting VLA directly predict high-dimensional visual states can distribute model capacity and incur prohibitive training cost, while compressing visual states into more compact supervisory signals inevitably incurs information bottlenecks. Moreover, existing methods often suffer from poor comprehension and reasoning capabilities due to the neglect of language supervision. This paper introduces Mantis, a novel framework featuring a Disentangled Visual Foresight (DVF) to tackle these issues. Specifically, Mantis decouples visual foresight prediction from the backbone with the combination of meta queries and a diffusion Transformer (DiT) head. With the current visual state provided to the DiT via a residual connection, a simple next-state prediction objective enables the meta queries to automatically capture the latent actions that delineate the visual trajectory, and hence boost the learning of explicit actions. The disentanglement reduces the burden of the VLA backbone, enabling it to maintain comprehension and reasoning capabilities through language supervision. Empirically, pretrained on human manipulation videos, robot demonstrations, and image-text pairs, Mantis achieves a 96.7% success rate on LIBERO benchmark after fine-tuning, surpassing powerful baselines while exhibiting high convergence speed. Real-world evaluations show that Mantis outperforms $π_{0.5}$, a leading open-source VLA model, particularly in instruction-following capability, generalization to unseen instructions, and reasoning ability. Code and weights are released to support the open-source community.

## 核心内容
Recent advances in Vision-Language-Action (VLA) models demonstrate that visual signals can effectively complement sparse action supervisions. However, letting VLA directly predict high-dimensional visual states can distribute model capacity and incur prohibitive training cost, while compressing visual states into more compact supervisory signals inevitably incurs information bottlenecks. Moreover, existing methods often suffer from poor comprehension and reasoning capabilities due to the neglect of language supervision. This paper introduces Mantis, a novel framework featuring a Disentangled Visual Foresight (DVF) to tackle these issues. Specifically, Mantis decouples visual foresight prediction from the backbone with the combination of meta queries and a diffusion Transformer (DiT) head. With the current visual state provided to the DiT via a residual connection, a simple next-state prediction objective enables the meta queries to automatically capture the latent actions that delineate the visual trajectory, and hence boost the learning of explicit actions. The disentanglement reduces the burden of the VLA backbone, enabling it to maintain comprehension and reasoning capabilities through language supervision. Empirically, pretrained on human manipulation videos, robot demonstrations, and image-text pairs, Mantis achieves a 96.7% success rate on LIBERO benchmark after fine-tuning, surpassing powerful baselines while exhibiting high convergence speed. Real-world evaluations show that Mantis outperforms $π_{0.5}$, a leading open-source VLA model, particularly in instruction-following capability, generalization to unseen instructions, and reasoning ability. Code and weights are released to support the open-source community.

## 参考
- http://arxiv.org/abs/2511.16175v2

