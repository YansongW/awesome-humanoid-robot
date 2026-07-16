---
$id: ent_paper_clap_direct_vlm_to_vla_adaptat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding'
  zh: 'CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding'
  ko: 'CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding'
summary:
  en: 'arXiv:2607.08974v1 Announce Type: new Abstract: Vision-language-action models (VLAs) inherit semantic capabilities
    from pretrained VLMs, yet large-scale post-training on robot data and architectural modifications can reshape the backbone
    so extensively that it becomes difficult to isolate what the VLM contributes to control. Directly converting pretrained
    VLMs into VLAs with minimal architectural change offers a more transparent path to understanding how VLM capabilities
    transfer across model scales. The core obstacle is output-distribution mismatch: predicting actions as bare numeric token
    sequences moves generation away from the VLM''s pretrained language distribution, degrading the capabilities we seek to
    preserve. To address this, we propose CLAP (Causal Language-Action Prediction), which prepends each numeric action sequence
    with a natural-language action description, causally conditioning precise action-token prediction on a language-action
    plan without modifying the backbone architecture. With single-epoch fine-tuning alone, 2B CLAP achieves 90.8% on LIBERO
    (+14.9 pt over VLA-0) and improves robustness on LIBERO-PRO under language, object, and spatial perturbations. We will
    release CLAP at 0.8B, 2B, and 4B as an open-weight, multi-scale compact VLA family from a single VLM lineage, enabling
    controlled analysis of VLM-to-VLA capability transfer.'
  zh: 'arXiv:2607.08974v1 Announce Type: new Abstract: Vision-language-action models (VLAs) inherit semantic capabilities
    from pretrained VLMs, yet large-scale post-training on robot data and architectural modifications can reshape the backbone
    so extensively that it becomes difficult to isolate what the VLM contributes to control. Directly converting pretrained
    VLMs into VLAs with minimal architectural change offers a more transparent path to understanding how VLM capabilities
    transfer across model scales. The core obstacle is output-distribution mismatch: predicting actions as bare numeric token
    sequences moves generation away from the VLM''s pretrained language distribution, degrading the capabilities we seek to
    preserve. To address this, we propose CLAP (Causal Language-Action Prediction), which prepends each numeric action sequence
    with a natural-language action description, causally conditioning precise action-token prediction on a language-action
    plan without modifying the backbone architecture. With single-epoch fine-tuning alone, 2B CLAP achieves 90.8% on LIBERO
    (+14.9 pt over VLA-0) and improves robustness on LIBERO-PRO under language, object, and spatial perturbations. We will
    release CLAP at 0.8B, 2B, and 4B as an open-weight, multi-scale compact VLA family from a single VLM lineage, enabling
    controlled analysis of VLM-to-VLA capability transfer.'
  ko: 'arXiv:2607.08974v1 Announce Type: new Abstract: Vision-language-action models (VLAs) inherit semantic capabilities
    from pretrained VLMs, yet large-scale post-training on robot data and architectural modifications can reshape the backbone
    so extensively that it becomes difficult to isolate what the VLM contributes to control. Directly converting pretrained
    VLMs into VLAs with minimal architectural change offers a more transparent path to understanding how VLM capabilities
    transfer across model scales. The core obstacle is output-distribution mismatch: predicting actions as bare numeric token
    sequences moves generation away from the VLM''s pretrained language distribution, degrading the capabilities we seek to
    preserve. To address this, we propose CLAP (Causal Language-Action Prediction), which prepends each numeric action sequence
    with a natural-language action description, causally conditioning precise action-token prediction on a language-action
    plan without modifying the backbone architecture. With single-epoch fine-tuning alone, 2B CLAP achieves 90.8% on LIBERO
    (+14.9 pt over VLA-0) and improves robustness on LIBERO-PRO under language, object, and spatial perturbations. We will
    release CLAP at 0.8B, 2B, and 4B as an open-weight, multi-scale compact VLA family from a single VLM lineage, enabling
    controlled analysis of VLM-to-VLA capability transfer.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- clap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.08974v1.
sources:
- id: src_001
  type: paper
  title: 'CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding (arXiv)'
  url: https://arxiv.org/abs/2607.08974
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Vision-language-action models (VLAs) inherit semantic capabilities from pretrained VLMs, yet large-scale post-training on robot data and architectural modifications can reshape the backbone so extensively that it becomes difficult to isolate what the VLM contributes to control. Directly converting pretrained VLMs into VLAs with minimal architectural change offers a more transparent path to understanding how VLM capabilities transfer across model scales. The core obstacle is output-distribution mismatch: predicting actions as bare numeric token sequences moves generation away from the VLM's pretrained language distribution, degrading the capabilities we seek to preserve. To address this, we propose CLAP (Causal Language-Action Prediction), which prepends each numeric action sequence with a natural-language action description, causally conditioning precise action-token prediction on a language-action plan without modifying the backbone architecture. With single-epoch fine-tuning alone, 2B CLAP achieves 90.8% on LIBERO (+14.9 pt over VLA-0) and improves robustness on LIBERO-PRO under language, object, and spatial perturbations. We will release CLAP at 0.8B, 2B, and 4B as an open-weight, multi-scale compact VLA family from a single VLM lineage, enabling controlled analysis of VLM-to-VLA capability transfer.

## 核心内容
Vision-language-action models (VLAs) inherit semantic capabilities from pretrained VLMs, yet large-scale post-training on robot data and architectural modifications can reshape the backbone so extensively that it becomes difficult to isolate what the VLM contributes to control. Directly converting pretrained VLMs into VLAs with minimal architectural change offers a more transparent path to understanding how VLM capabilities transfer across model scales. The core obstacle is output-distribution mismatch: predicting actions as bare numeric token sequences moves generation away from the VLM's pretrained language distribution, degrading the capabilities we seek to preserve. To address this, we propose CLAP (Causal Language-Action Prediction), which prepends each numeric action sequence with a natural-language action description, causally conditioning precise action-token prediction on a language-action plan without modifying the backbone architecture. With single-epoch fine-tuning alone, 2B CLAP achieves 90.8% on LIBERO (+14.9 pt over VLA-0) and improves robustness on LIBERO-PRO under language, object, and spatial perturbations. We will release CLAP at 0.8B, 2B, and 4B as an open-weight, multi-scale compact VLA family from a single VLM lineage, enabling controlled analysis of VLM-to-VLA capability transfer.

## 参考
- http://arxiv.org/abs/2607.08974v1

