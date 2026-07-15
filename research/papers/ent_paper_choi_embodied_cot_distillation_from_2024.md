---
$id: ent_paper_choi_embodied_cot_distillation_from_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Embodied CoT Distillation From LLM To Off-the-shelf Agents
  zh: Embodied CoT Distillation From LLM To Off-the-shelf Agents
  ko: Embodied CoT Distillation From LLM To Off-the-shelf Agents
summary:
  en: Embodied CoT Distillation From LLM To Off-the-shelf Agents (Embodied CoT Distillation From LLM To Off-the-shelf Agents),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Sungkyunkwan University, Department
    of Computer Science and Engineering, Sungkyunkwan University, and published at ICML 2024.
  zh: Embodied CoT Distillation From LLM To Off-the-shelf Agents (Embodied CoT Distillation From LLM To Off-the-shelf Agents),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Sungkyunkwan University, Department
    of Computer Science and Engineering, Sungkyunkwan University, and published at ICML 2024.
  ko: Embodied CoT Distillation From LLM To Off-the-shelf Agents (Embodied CoT Distillation From LLM To Off-the-shelf Agents),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Sungkyunkwan University, Department
    of Computer Science and Engineering, Sungkyunkwan University, and published at ICML 2024.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embodied_cot_distillation_from
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.11499v1.
sources:
- id: src_001
  type: paper
  title: Embodied CoT Distillation From LLM To Off-the-shelf Agents source
  url: https://openreview.net/forum?id=M4Htd52HMH
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
We address the challenge of utilizing large language models (LLMs) for complex embodied tasks, in the environment where decision-making systems operate timely on capacity-limited, off-the-shelf devices. We present DeDer, a framework for decomposing and distilling the embodied reasoning capabilities from LLMs to efficient, small language model (sLM)-based policies. In DeDer, the decision-making process of LLM-based strategies is restructured into a hierarchy with a reasoning-policy and planning-policy. The reasoning-policy is distilled from the data that is generated through the embodied in-context learning and self-verification of an LLM, so it can produce effective rationales. The planning-policy, guided by the rationales, can render optimized plans efficiently. In turn, DeDer allows for adopting sLMs for both policies, deployed on off-the-shelf devices. Furthermore, to enhance the quality of intermediate rationales, specific to embodied tasks, we devise the embodied knowledge graph, and to generate multiple rationales timely through a single inference, we also use the contrastively prompted attention model. Our experiments with the ALFRED benchmark demonstrate that DeDer surpasses leading language planning and distillation approaches, indicating the applicability and efficiency of sLM-based embodied policies derived through DeDer.

## 核心内容
We address the challenge of utilizing large language models (LLMs) for complex embodied tasks, in the environment where decision-making systems operate timely on capacity-limited, off-the-shelf devices. We present DeDer, a framework for decomposing and distilling the embodied reasoning capabilities from LLMs to efficient, small language model (sLM)-based policies. In DeDer, the decision-making process of LLM-based strategies is restructured into a hierarchy with a reasoning-policy and planning-policy. The reasoning-policy is distilled from the data that is generated through the embodied in-context learning and self-verification of an LLM, so it can produce effective rationales. The planning-policy, guided by the rationales, can render optimized plans efficiently. In turn, DeDer allows for adopting sLMs for both policies, deployed on off-the-shelf devices. Furthermore, to enhance the quality of intermediate rationales, specific to embodied tasks, we devise the embodied knowledge graph, and to generate multiple rationales timely through a single inference, we also use the contrastively prompted attention model. Our experiments with the ALFRED benchmark demonstrate that DeDer surpasses leading language planning and distillation approaches, indicating the applicability and efficiency of sLM-based embodied policies derived through DeDer.

## 参考
- http://arxiv.org/abs/2412.11499v1

