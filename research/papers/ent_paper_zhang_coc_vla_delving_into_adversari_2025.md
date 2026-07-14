---
$id: ent_paper_zhang_coc_vla_delving_into_adversari_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model'
  zh: CoC-VLA
  ko: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model'
summary:
  en: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model (CoC-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University,
    National University of Singapore, University of Science and Technology of China, and published at NIPS25.'
  zh: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model (CoC-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University,
    National University of Singapore, University of Science and Technology of China, and published at NIPS25.'
  ko: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model (CoC-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University,
    National University of Singapore, University of Science and Technology of China, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- coc_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19914v1.
sources:
- id: src_001
  type: paper
  title: 'CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action
    Model (arXiv)'
  url: https://arxiv.org/abs/2511.19914
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CoC-VLA source
  url: https://doi.org/10.48550/arXiv.2511.19914
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Autonomous driving represents a prominent application of artificial intelligence. Recent approaches have shifted from focusing solely on common scenarios to addressing complex, long-tail situations such as subtle human behaviors, traffic accidents, and non-compliant driving patterns. Given the demonstrated capabilities of large language models (LLMs) in understanding visual and natural language inputs and following instructions, recent methods have integrated LLMs into autonomous driving systems to enhance reasoning, interpretability, and performance across diverse scenarios. However, existing methods typically rely either on real-world data, which is suitable for industrial deployment, or on simulation data tailored to rare or hard case scenarios. Few approaches effectively integrate the complementary advantages of both data sources. To address this limitation, we propose a novel VLM-guided, end-to-end adversarial transfer framework for autonomous driving that transfers long-tail handling capabilities from simulation to real-world deployment, named CoC-VLA. The framework comprises a teacher VLM model, a student VLM model, and a discriminator. Both the teacher and student VLM models utilize a shared base architecture, termed the Chain-of-Causality Visual-Language Model (CoC VLM), which integrates temporal information via an end-to-end text adapter. This architecture supports chain-of-thought reasoning to infer complex driving logic. The teacher and student VLM models are pre-trained separately on simulated and real-world datasets. The discriminator is trained adversarially to facilitate the transfer of long-tail handling capabilities from simulated to real-world environments by the student VLM model, using a novel backpropagation strategy.

## 核心内容
Autonomous driving represents a prominent application of artificial intelligence. Recent approaches have shifted from focusing solely on common scenarios to addressing complex, long-tail situations such as subtle human behaviors, traffic accidents, and non-compliant driving patterns. Given the demonstrated capabilities of large language models (LLMs) in understanding visual and natural language inputs and following instructions, recent methods have integrated LLMs into autonomous driving systems to enhance reasoning, interpretability, and performance across diverse scenarios. However, existing methods typically rely either on real-world data, which is suitable for industrial deployment, or on simulation data tailored to rare or hard case scenarios. Few approaches effectively integrate the complementary advantages of both data sources. To address this limitation, we propose a novel VLM-guided, end-to-end adversarial transfer framework for autonomous driving that transfers long-tail handling capabilities from simulation to real-world deployment, named CoC-VLA. The framework comprises a teacher VLM model, a student VLM model, and a discriminator. Both the teacher and student VLM models utilize a shared base architecture, termed the Chain-of-Causality Visual-Language Model (CoC VLM), which integrates temporal information via an end-to-end text adapter. This architecture supports chain-of-thought reasoning to infer complex driving logic. The teacher and student VLM models are pre-trained separately on simulated and real-world datasets. The discriminator is trained adversarially to facilitate the transfer of long-tail handling capabilities from simulated to real-world environments by the student VLM model, using a novel backpropagation strategy.

## 参考
- http://arxiv.org/abs/2511.19914v1

