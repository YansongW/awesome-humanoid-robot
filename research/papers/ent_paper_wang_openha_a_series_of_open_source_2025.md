---
$id: ent_paper_wang_openha_a_series_of_open_source_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft'
  zh: OpenHA
  ko: 'OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft'
summary:
  en: 'OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft (OpenHA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University.'
  zh: 'OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft (OpenHA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University.'
  ko: 'OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft (OpenHA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University.'
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
- openha
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.13347v1.
sources:
- id: src_001
  type: paper
  title: 'OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft (arXiv)'
  url: https://arxiv.org/abs/2509.13347
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OpenHA source
  url: https://doi.org/10.48550/arXiv.2509.13347
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The choice of action spaces is a critical yet unresolved challenge in developing capable, end-to-end trainable agents. This paper first presents a large-scale, systematic comparison of prominent abstracted action spaces and tokenizers for Vision-Language-Action (VLA) or hierarchical agent models in the open-ended Minecraft. Our analysis reveals that no single action space is universally optimal; instead, the most effective abstraction is highly task-dependent, creating a dilemma for building generalist agents. To resolve this, we introduce Chain of Action (CoA), a novel framework that unifies high-level planning and low-level control within a single, monolithic VLA model. CoA treats an abstracted action not as a command for a separate policy, but as an intermediate reasoning step--akin to a chain of thought--that guides the generation of the final, executable action. Furthermore, we demonstrate that an All-in-One agent trained on a diverse mixture of action spaces using the CoA paradigm learns a more robust and generalizable policy. This unified agent achieves a new state-of-the-art, improving the overall task success rate over strong, specialized baselines. To foster reproducible research, we release the OpenHA (Open Hierarchical Agents) suite, which includes our comprehensive benchmark of over 800 distinct tasks, curated datasets, source code, and all pretrained model checkpoints at https://github.com/CraftJarvis/OpenHA

## 核心内容
The choice of action spaces is a critical yet unresolved challenge in developing capable, end-to-end trainable agents. This paper first presents a large-scale, systematic comparison of prominent abstracted action spaces and tokenizers for Vision-Language-Action (VLA) or hierarchical agent models in the open-ended Minecraft. Our analysis reveals that no single action space is universally optimal; instead, the most effective abstraction is highly task-dependent, creating a dilemma for building generalist agents. To resolve this, we introduce Chain of Action (CoA), a novel framework that unifies high-level planning and low-level control within a single, monolithic VLA model. CoA treats an abstracted action not as a command for a separate policy, but as an intermediate reasoning step--akin to a chain of thought--that guides the generation of the final, executable action. Furthermore, we demonstrate that an All-in-One agent trained on a diverse mixture of action spaces using the CoA paradigm learns a more robust and generalizable policy. This unified agent achieves a new state-of-the-art, improving the overall task success rate over strong, specialized baselines. To foster reproducible research, we release the OpenHA (Open Hierarchical Agents) suite, which includes our comprehensive benchmark of over 800 distinct tasks, curated datasets, source code, and all pretrained model checkpoints at https://github.com/CraftJarvis/OpenHA

## 参考
- http://arxiv.org/abs/2509.13347v1

