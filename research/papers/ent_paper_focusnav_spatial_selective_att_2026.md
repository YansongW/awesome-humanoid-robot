---
$id: ent_paper_focusnav_spatial_selective_att_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation'
  zh: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation'
  ko: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation'
summary:
  en: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation is a 2026 work on navigation
    for humanoid robots.'
  zh: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation is a 2026 work on navigation
    for humanoid robots.'
  ko: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation is a 2026 work on navigation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- focusnav
- humanoid
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.12790v1.
sources:
- id: src_001
  type: paper
  title: 'FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation (arXiv)'
  url: https://arxiv.org/abs/2601.12790
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Robust local navigation in unstructured and dynamic environments remains a significant challenge for humanoid robots, requiring a delicate balance between long-range navigation targets and immediate motion stability. In this paper, we propose FocusNav, a spatial selective attention framework that adaptively modulates the robot's perceptual field based on navigational intent and real-time stability. FocusNav features a Waypoint-Guided Spatial Cross-Attention (WGSCA) mechanism that anchors environmental feature aggregation to a sequence of predicted collision-free waypoints, ensuring task-relevant perception along the planned trajectory. To enhance robustness in complex terrains, the Stability-Aware Selective Gating (SASG) module autonomously truncates distal information when detecting instability, compelling the policy to prioritize immediate foothold safety. Extensive experiments on the Unitree G1 humanoid robot demonstrate that FocusNav significantly improves navigation success rates in challenging scenarios, outperforming baselines in both collision avoidance and motion stability, achieving robust navigation in dynamic and complex environments.

## 核心内容
Robust local navigation in unstructured and dynamic environments remains a significant challenge for humanoid robots, requiring a delicate balance between long-range navigation targets and immediate motion stability. In this paper, we propose FocusNav, a spatial selective attention framework that adaptively modulates the robot's perceptual field based on navigational intent and real-time stability. FocusNav features a Waypoint-Guided Spatial Cross-Attention (WGSCA) mechanism that anchors environmental feature aggregation to a sequence of predicted collision-free waypoints, ensuring task-relevant perception along the planned trajectory. To enhance robustness in complex terrains, the Stability-Aware Selective Gating (SASG) module autonomously truncates distal information when detecting instability, compelling the policy to prioritize immediate foothold safety. Extensive experiments on the Unitree G1 humanoid robot demonstrate that FocusNav significantly improves navigation success rates in challenging scenarios, outperforming baselines in both collision avoidance and motion stability, achieving robust navigation in dynamic and complex environments.

## 参考
- http://arxiv.org/abs/2601.12790v1

