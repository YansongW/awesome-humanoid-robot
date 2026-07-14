---
$id: ent_paper_jing_mixture_of_horizons_in_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Mixture of Horizons in Action Chunking
  zh: MoH
  ko: Mixture of Horizons in Action Chunking
summary:
  en: Mixture of Horizons in Action Chunking (MoH), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by RUC, UNC, CUHK.
  zh: Mixture of Horizons in Action Chunking (MoH), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by RUC, UNC, CUHK.
  ko: Mixture of Horizons in Action Chunking (MoH), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by RUC, UNC, CUHK.
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
- moh
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19433v2.
sources:
- id: src_001
  type: paper
  title: Mixture of Horizons in Action Chunking (arXiv)
  url: https://arxiv.org/abs/2511.19433
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MoH source
  url: https://doi.org/10.48550/arXiv.2511.19433
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models have shown remarkable capabilities in robotic manipulation, but their performance is sensitive to the $\textbf{action chunk length}$ used during training, termed $\textbf{horizon}$. Our empirical study reveals an inherent trade-off: longer horizons provide stronger global foresight but degrade fine-grained accuracy, while shorter ones sharpen local control yet struggle on long-term tasks, implying fixed choice of single horizons being suboptimal. To mitigate the trade-off, we propose a $\textbf{mixture of horizons (MoH)}$ strategy. MoH rearranges the action chunk into several segments with different horizons, processes them in parallel with a shared action transformer, and fuses outputs with a light linear gate. It has three appealing benefits. 1) MoH exploits long-term foresight and short-term precision jointly within a single model, improving both performance and generalizability to complex tasks. 2) MoH is plug-and-play for full-attention action modules with minimal training or inference overhead. 3) MoH enables dynamic inference with adaptive horizons, which selects stable actions through cross-horizon consensus, achieving 2.5$\times$ higher throughput than baselines while preserving superior performance. Extensive experiments over flow-based policies $π_0$, $π_{0.5}$, and one-step regression policy $π_{\text{reg}}$ demonstrate that MoH yields consistent and significant gains on both simulations and real-world tasks. Notably, under mixed-task setting, $π_{0.5}$ with MoH reaches a new state-of-the-art with 99$\%$ average success rate on LIBERO after only $30k$ training iterations. Project page: https://timsty1.github.io/moh/

## 核心内容
Vision-language-action (VLA) models have shown remarkable capabilities in robotic manipulation, but their performance is sensitive to the $\textbf{action chunk length}$ used during training, termed $\textbf{horizon}$. Our empirical study reveals an inherent trade-off: longer horizons provide stronger global foresight but degrade fine-grained accuracy, while shorter ones sharpen local control yet struggle on long-term tasks, implying fixed choice of single horizons being suboptimal. To mitigate the trade-off, we propose a $\textbf{mixture of horizons (MoH)}$ strategy. MoH rearranges the action chunk into several segments with different horizons, processes them in parallel with a shared action transformer, and fuses outputs with a light linear gate. It has three appealing benefits. 1) MoH exploits long-term foresight and short-term precision jointly within a single model, improving both performance and generalizability to complex tasks. 2) MoH is plug-and-play for full-attention action modules with minimal training or inference overhead. 3) MoH enables dynamic inference with adaptive horizons, which selects stable actions through cross-horizon consensus, achieving 2.5$\times$ higher throughput than baselines while preserving superior performance. Extensive experiments over flow-based policies $π_0$, $π_{0.5}$, and one-step regression policy $π_{\text{reg}}$ demonstrate that MoH yields consistent and significant gains on both simulations and real-world tasks. Notably, under mixed-task setting, $π_{0.5}$ with MoH reaches a new state-of-the-art with 99$\%$ average success rate on LIBERO after only $30k$ training iterations. Project page: https://timsty1.github.io/moh/

## 参考
- http://arxiv.org/abs/2511.19433v2

