---
$id: ent_paper_yin_deepthinkvla_enhancing_reasoni_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models'
  zh: DeepThinkVLA
  ko: 'DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models'
summary:
  en: 'DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models (DeepThinkVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Wechat AI, Tencent Inc..'
  zh: 'DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models (DeepThinkVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Wechat AI, Tencent Inc..'
  ko: 'DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models (DeepThinkVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Wechat AI, Tencent Inc..'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- deepthinkvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.15669v2.
sources:
- id: src_001
  type: paper
  title: 'DeepThinkVLA: Enhancing Reasoning Capability of Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.15669
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DeepThinkVLA source
  url: https://doi.org/10.48550/arXiv.2511.15669
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Does Chain-of-Thought (CoT) reasoning genuinely improve Vision-Language-Action (VLA) models, or does it merely add overhead? Existing CoT-VLA systems report limited and inconsistent gains, yet no prior work has rigorously diagnosed when and why CoT helps robots act. Through systematic experiments, we identify two necessary conditions that must be jointly satisfied for CoT to be effective in VLA: (1) Decoding Alignment -- CoT and actions must be generated with modality-appropriate mechanisms; forcing both through a single autoregressive decoder is not merely suboptimal but actively harmful, degrading performance by 4.2 percentage points; (2) Causal Alignment -- CoT must be causally linked to task success via outcome-based optimization; without it, supervised CoT is indistinguishable from no reasoning at all under distribution shift, exhibiting a 32.0\,pp performance drop nearly identical to the 31.6\,pp drop of a reasoning-free baseline. Guided by these findings, we build DeepThinkVLA: a hybrid-attention decoder satisfies Condition~1 by pairing causal attention for language with bidirectional attention for parallel action decoding, while a two-stage SFT-then-RL pipeline satisfies Condition~2 by aligning the full reasoning--action chain with sparse task-success rewards. DeepThinkVLA achieves 97.0\% success on LIBERO, 79.0\% robustness on LIBERO-Plus (vs.\ 61.6\% for $π_0$-FAST), and 59.3\% success on RoboTwin~2.0, exceeding the strongest baseline by 21.7 points. Furthermore, we validate the practical effectiveness of our approach through real-world robot experiments. Code available at https://github.com/OpenBMB/DeepThinkVLA

## 核心内容
Does Chain-of-Thought (CoT) reasoning genuinely improve Vision-Language-Action (VLA) models, or does it merely add overhead? Existing CoT-VLA systems report limited and inconsistent gains, yet no prior work has rigorously diagnosed when and why CoT helps robots act. Through systematic experiments, we identify two necessary conditions that must be jointly satisfied for CoT to be effective in VLA: (1) Decoding Alignment -- CoT and actions must be generated with modality-appropriate mechanisms; forcing both through a single autoregressive decoder is not merely suboptimal but actively harmful, degrading performance by 4.2 percentage points; (2) Causal Alignment -- CoT must be causally linked to task success via outcome-based optimization; without it, supervised CoT is indistinguishable from no reasoning at all under distribution shift, exhibiting a 32.0\,pp performance drop nearly identical to the 31.6\,pp drop of a reasoning-free baseline. Guided by these findings, we build DeepThinkVLA: a hybrid-attention decoder satisfies Condition~1 by pairing causal attention for language with bidirectional attention for parallel action decoding, while a two-stage SFT-then-RL pipeline satisfies Condition~2 by aligning the full reasoning--action chain with sparse task-success rewards. DeepThinkVLA achieves 97.0\% success on LIBERO, 79.0\% robustness on LIBERO-Plus (vs.\ 61.6\% for $π_0$-FAST), and 59.3\% success on RoboTwin~2.0, exceeding the strongest baseline by 21.7 points. Furthermore, we validate the practical effectiveness of our approach through real-world robot experiments. Code available at https://github.com/OpenBMB/DeepThinkVLA

## 参考
- http://arxiv.org/abs/2511.15669v2

