---
$id: ent_paper_liu_unified_embodied_vlm_reasoning_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training
  zh: ERIQ
  ko: Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training
summary:
  en: Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training (ERIQ), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AgiBot Research, AgiBot, Shanghai Innovation Institute.
  zh: Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training (ERIQ), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AgiBot Research, AgiBot, Shanghai Innovation Institute.
  ko: Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training (ERIQ), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AgiBot Research, AgiBot, Shanghai Innovation Institute.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- eriq
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.24125v2.
sources:
- id: src_001
  type: paper
  title: Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training (arXiv)
  url: https://arxiv.org/abs/2512.24125
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ERIQ source
  url: https://doi.org/10.48550/arXiv.2512.24125
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
General-purpose robotic systems operating in open-world environments must achieve both broad generalization and high-precision action execution, a combination that remains challenging for existing Vision-Language-Action (VLA) models. While large Vision-Language Models (VLMs) improve semantic generalization, insufficient embodied reasoning leads to brittle behavior, and conversely, strong reasoning alone is inadequate without precise control. To provide a decoupled and quantitative assessment of this bottleneck, we introduce Embodied Reasoning Intelligence Quotient (ERIQ), a large-scale embodied reasoning benchmark in robotic manipulation, comprising 6K+ question-answer pairs across four reasoning dimensions. By decoupling reasoning from execution, ERIQ enables systematic evaluation and reveals a strong positive correlation between embodied reasoning capability and end-to-end VLA generalization. To bridge the gap from reasoning to precise execution, we propose FACT, a flow-matching-based action tokenizer that converts continuous control into discrete sequences while preserving high-fidelity trajectory reconstruction. The resulting GenieReasoner jointly optimizes reasoning and action in a unified space, outperforming both continuous-action and prior discrete-action baselines in real-world tasks. Together, ERIQ and FACT provide a principled framework for diagnosing and overcoming the reasoning-precision trade-off, advancing robust, general-purpose robotic manipulation. Project page: https://geniereasoner.github.io/GenieReasoner/

## 核心内容
General-purpose robotic systems operating in open-world environments must achieve both broad generalization and high-precision action execution, a combination that remains challenging for existing Vision-Language-Action (VLA) models. While large Vision-Language Models (VLMs) improve semantic generalization, insufficient embodied reasoning leads to brittle behavior, and conversely, strong reasoning alone is inadequate without precise control. To provide a decoupled and quantitative assessment of this bottleneck, we introduce Embodied Reasoning Intelligence Quotient (ERIQ), a large-scale embodied reasoning benchmark in robotic manipulation, comprising 6K+ question-answer pairs across four reasoning dimensions. By decoupling reasoning from execution, ERIQ enables systematic evaluation and reveals a strong positive correlation between embodied reasoning capability and end-to-end VLA generalization. To bridge the gap from reasoning to precise execution, we propose FACT, a flow-matching-based action tokenizer that converts continuous control into discrete sequences while preserving high-fidelity trajectory reconstruction. The resulting GenieReasoner jointly optimizes reasoning and action in a unified space, outperforming both continuous-action and prior discrete-action baselines in real-world tasks. Together, ERIQ and FACT provide a principled framework for diagnosing and overcoming the reasoning-precision trade-off, advancing robust, general-purpose robotic manipulation. Project page: https://geniereasoner.github.io/GenieReasoner/

## 参考
- http://arxiv.org/abs/2512.24125v2

