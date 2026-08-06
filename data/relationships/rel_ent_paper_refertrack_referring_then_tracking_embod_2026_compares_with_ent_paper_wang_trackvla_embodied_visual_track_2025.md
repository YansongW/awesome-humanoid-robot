---
$id: rel_ent_paper_refertrack_referring_then_tracking_embod_2026_compares_with_ent_paper_wang_trackvla_embodied_visual_track_2025
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: compares_with
source:
  id: ent_paper_refertrack_referring_then_tracking_embod_2026
  name:
    en: 'ReferTrack: Referring Then Tracking for Embodied Visual Tracking'
    zh: 'ReferTrack: Referring Then Tracking for Embodied Visual Tracking'
target:
  id: ent_paper_wang_trackvla_embodied_visual_track_2025
  name:
    en: 'TrackVLA: Embodied Visual Tracking in the Wild'
    zh: TrackVLA
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'ReferTrack: Referring Then Tracking for Embodied Visual Tracking compares with TrackVLA: Embodied Visual Tracking in
    the Wild.'
  zh: 'ReferTrack: Referring Then Tracking for Embodied Visual Trackingcompares_withTrackVLA。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文将TrackVLA++作为最强单视图基线进行对比，并声称超越它。 | 证据: 作者基于
    Qwen3-4B 构建双分支 VLA，通过 Refer-CoT token 与 TVBI 历史注入，在单前视相机、无 RL 的 SFT 设置下，于 EVT-Bench 上显著超越最强单视图基线 TrackVLA++，尤其在歧义跟踪（AT）任务上
    SR 提升 22.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_refertrack_referring_then_tracking_embod_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_refertrack_referring_then_tracking_embod_2026/
  accessed_at: '2026-08-06'
---
