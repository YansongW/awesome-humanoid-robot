---
$id: ent_paper_xu_seeing_to_act_prompting_to_spe_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Seeing to Act Prompting to Specify
  zh: BayesVLA
  ko: Seeing to Act Prompting to Specify
summary:
  en: Seeing to Act Prompting to Specify (BayesVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Zhejiang University, UC Berkeley.
  zh: Seeing to Act Prompting to Specify (BayesVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Zhejiang University, UC Berkeley.
  ko: Seeing to Act Prompting to Specify (BayesVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Zhejiang University, UC Berkeley.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bayesvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.11218v1.
sources:
- id: src_001
  type: paper
  title: Seeing to Act Prompting to Specify (arXiv)
  url: https://arxiv.org/abs/2512.11218
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: BayesVLA source
  url: https://doi.org/10.48550/arXiv.2512.11218
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The pursuit of out-of-distribution generalization in Vision-Language-Action (VLA) models is often hindered by catastrophic forgetting of the Vision-Language Model (VLM) backbone during fine-tuning. While co-training with external reasoning data helps, it requires experienced tuning and data-related overhead. Beyond such external dependencies, we identify an intrinsic cause within VLA datasets: modality imbalance, where language diversity is much lower than visual and action diversity. This imbalance biases the model toward visual shortcuts and language forgetting. To address this, we introduce BayesVLA, a Bayesian factorization that decomposes the policy into a visual-action prior, supporting seeing-to-act, and a language-conditioned likelihood, enabling prompt-to-specify. This inherently preserves generalization and promotes instruction following. We further incorporate pre- and post-contact phases to better leverage pre-trained foundation models. Information-theoretic analysis formally validates our effectiveness in mitigating shortcut learning. Extensive experiments show superior generalization to unseen instructions, objects, and environments compared to existing methods. Project page is available at: https://xukechun.github.io/papers/BayesVLA.

## 核心内容
The pursuit of out-of-distribution generalization in Vision-Language-Action (VLA) models is often hindered by catastrophic forgetting of the Vision-Language Model (VLM) backbone during fine-tuning. While co-training with external reasoning data helps, it requires experienced tuning and data-related overhead. Beyond such external dependencies, we identify an intrinsic cause within VLA datasets: modality imbalance, where language diversity is much lower than visual and action diversity. This imbalance biases the model toward visual shortcuts and language forgetting. To address this, we introduce BayesVLA, a Bayesian factorization that decomposes the policy into a visual-action prior, supporting seeing-to-act, and a language-conditioned likelihood, enabling prompt-to-specify. This inherently preserves generalization and promotes instruction following. We further incorporate pre- and post-contact phases to better leverage pre-trained foundation models. Information-theoretic analysis formally validates our effectiveness in mitigating shortcut learning. Extensive experiments show superior generalization to unseen instructions, objects, and environments compared to existing methods. Project page is available at: https://xukechun.github.io/papers/BayesVLA.

## 参考
- http://arxiv.org/abs/2512.11218v1

