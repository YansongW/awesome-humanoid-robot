---
$id: ent_paper_zhang_iflybot_vla_technical_report_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: iFlyBot-VLA Technical Report
  zh: iFlyBot-VLA
  ko: iFlyBot-VLA Technical Report
summary:
  en: iFlyBot-VLA Technical Report (iFlyBot-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by iFlyTek Reasearch and Development Group, LindenBot.
  zh: iFlyBot-VLA Technical Report (iFlyBot-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by iFlyTek Reasearch and Development Group, LindenBot.
  ko: iFlyBot-VLA Technical Report (iFlyBot-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by iFlyTek Reasearch and Development Group, LindenBot.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- iflybot_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.01914v1.
sources:
- id: src_001
  type: paper
  title: iFlyBot-VLA Technical Report (arXiv)
  url: https://arxiv.org/abs/2511.01914
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: iFlyBot-VLA source
  url: https://doi.org/10.48550/arXiv.2511.01914
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce iFlyBot-VLA, a large-scale Vision-Language-Action (VLA) model trained under a novel framework. The main contributions are listed as follows: (1) a latent action model thoroughly trained on large-scale human and robotic manipulation videos; (2) a dual-level action representation framework that jointly supervises both the Vision-Language Model (VLM) and the action expert during training; (3) a mixed training strategy that combines robot trajectory data with general QA and spatial QA datasets, effectively enhancing the 3D perceptual and reasoning capabilities of the VLM backbone. Specifically, the VLM is trained to predict two complementary forms of actions: latent actions, derived from our latent action model pretrained on cross-embodiment manipulation data, which capture implicit high-level intentions; and structured discrete action tokens, obtained through frequency-domain transformations of continuous control signals, which encode explicit low-level dynamics. This dual supervision aligns the representation spaces of language, vision, and action, enabling the VLM to directly contribute to action generation. Experimental results on the LIBERO Franka benchmark demonstrate the superiority of our frame-work, while real-world evaluations further show that iFlyBot-VLA achieves competitive success rates across diverse and challenging manipulation tasks. Furthermore, we plan to open-source a portion of our self-constructed dataset to support future research in the community

## 核心内容
We introduce iFlyBot-VLA, a large-scale Vision-Language-Action (VLA) model trained under a novel framework. The main contributions are listed as follows: (1) a latent action model thoroughly trained on large-scale human and robotic manipulation videos; (2) a dual-level action representation framework that jointly supervises both the Vision-Language Model (VLM) and the action expert during training; (3) a mixed training strategy that combines robot trajectory data with general QA and spatial QA datasets, effectively enhancing the 3D perceptual and reasoning capabilities of the VLM backbone. Specifically, the VLM is trained to predict two complementary forms of actions: latent actions, derived from our latent action model pretrained on cross-embodiment manipulation data, which capture implicit high-level intentions; and structured discrete action tokens, obtained through frequency-domain transformations of continuous control signals, which encode explicit low-level dynamics. This dual supervision aligns the representation spaces of language, vision, and action, enabling the VLM to directly contribute to action generation. Experimental results on the LIBERO Franka benchmark demonstrate the superiority of our frame-work, while real-world evaluations further show that iFlyBot-VLA achieves competitive success rates across diverse and challenging manipulation tasks. Furthermore, we plan to open-source a portion of our self-constructed dataset to support future research in the community

## 参考
- http://arxiv.org/abs/2511.01914v1

