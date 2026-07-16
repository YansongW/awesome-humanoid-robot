---
$id: rel_ent_paper_do_vision_language_action_mode_2026_uses_ent_software_pinocchio
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_do_vision_language_action_mode_2026
  name:
    en: Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning
    zh: Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning
target:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 08_software_middleware
description:
  en: Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning uses Pinocchio.
  zh: Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning使用Pinocchio。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据说明他们通过一个名为Pinocchio的学习评判器来操作行为代理，表明使用了Pinocchio。
    | 证据: We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring
    observation grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied
    policy with r'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_do_vision_language_action_mode_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_do_vision_language_action_mode_2026/
  accessed_at: '2026-07-16'
---
