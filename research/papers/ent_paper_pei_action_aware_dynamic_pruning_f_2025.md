---
$id: ent_paper_pei_action_aware_dynamic_pruning_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation
  zh: ADP
  ko: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation
summary:
  en: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation (ADP), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science, The University of Sydney.
  zh: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation (ADP), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science, The University of Sydney.
  ko: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation (ADP), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science, The University of Sydney.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- adp
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22093v1.
sources:
- id: src_001
  type: paper
  title: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation (arXiv)
  url: https://arxiv.org/abs/2509.22093
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ADP source
  url: https://doi.org/10.48550/arXiv.2509.22093
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robotic manipulation with Vision-Language-Action models requires efficient inference over long-horizon multi-modal context, where attention to dense visual tokens dominates computational cost. Existing methods optimize inference speed by reducing visual redundancy within VLA models, but they overlook the varying redundancy across robotic manipulation stages. We observe that the visual token redundancy is higher in coarse manipulation phase than in fine-grained operations, and is strongly correlated with the action dynamic. Motivated by this observation, we propose \textbf{A}ction-aware \textbf{D}ynamic \textbf{P}runing (\textbf{ADP}), a multi-modal pruning framework that integrates text-driven token selection with action-aware trajectory gating. Our method introduces a gating mechanism that conditions the pruning signal on recent action trajectories, using past motion windows to adaptively adjust token retention ratios in accordance with dynamics, thereby balancing computational efficiency and perceptual precision across different manipulation stages. Extensive experiments on the LIBERO suites and diverse real-world scenarios demonstrate that our method significantly reduces FLOPs and action inference latency (\textit{e.g.} $1.35 \times$ speed up on OpenVLA-OFT) while maintaining competitive success rates (\textit{e.g.} 25.8\% improvements with OpenVLA) compared to baselines, thereby providing a simple plug-in path to efficient robot policies that advances the efficiency and performance frontier of robotic manipulation. Our project website is: \href{https://vla-adp.github.io/}{ADP.com}.

## 核心内容
Robotic manipulation with Vision-Language-Action models requires efficient inference over long-horizon multi-modal context, where attention to dense visual tokens dominates computational cost. Existing methods optimize inference speed by reducing visual redundancy within VLA models, but they overlook the varying redundancy across robotic manipulation stages. We observe that the visual token redundancy is higher in coarse manipulation phase than in fine-grained operations, and is strongly correlated with the action dynamic. Motivated by this observation, we propose \textbf{A}ction-aware \textbf{D}ynamic \textbf{P}runing (\textbf{ADP}), a multi-modal pruning framework that integrates text-driven token selection with action-aware trajectory gating. Our method introduces a gating mechanism that conditions the pruning signal on recent action trajectories, using past motion windows to adaptively adjust token retention ratios in accordance with dynamics, thereby balancing computational efficiency and perceptual precision across different manipulation stages. Extensive experiments on the LIBERO suites and diverse real-world scenarios demonstrate that our method significantly reduces FLOPs and action inference latency (\textit{e.g.} $1.35 \times$ speed up on OpenVLA-OFT) while maintaining competitive success rates (\textit{e.g.} 25.8\% improvements with OpenVLA) compared to baselines, thereby providing a simple plug-in path to efficient robot policies that advances the efficiency and performance frontier of robotic manipulation. Our project website is: \href{https://vla-adp.github.io/}{ADP.com}.

## 参考
- http://arxiv.org/abs/2509.22093v1

