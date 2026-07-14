---
$id: ent_paper_corridorvla_explicit_spatial_c_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse
    Anchors'
  zh: 'CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse
    Anchors'
  ko: 'CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse
    Anchors'
summary:
  en: "arXiv:2604.21241v2 Announce Type: replace \nAbstract: Vision--Language--Action\
    \ (VLA) models often use intermediate representations to connect multimodal inputs\
    \ with continuous control, yet spatial guidance is often injected implicitly through\
    \ latent features. We propose CorridorVLA, which predicts sparse spatial anchors\
    \ as incremental physical changes (e.g., end-effector $\\Delta$-positions) and\
    \ uses them to impose an explicit tolerance region in the training objective for\
    \ action generation. The anchors define a tolerance corridor that guides a flow-matching\
    \ action head: trajectories whose implied spatial evolution falls outside the\
    \ corridor receive corrective gradients, while trajectories within the corridor\
    \ are refined by a consistency objective. CorridorVLA improves SmolVLA by 4.45\
    \ percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and 7.98\
    \ percentage points, respectively, on the more challenging LIBERO-Plus benchmark.\
    \ Notably, under the same single-policy 4-in-1 setting, where one policy is jointly\
    \ trained and evaluated across all task suites, GR00T-Corr achieves an 83.21%\
    \ success rate. These results indicate that action-aligned physical cues can provide\
    \ direct and interpretable constraints for generative action policies, complementing\
    \ spatial guidance encoded in visual or latent forms. Code and released model\
    \ checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA."
  zh: "arXiv:2604.21241v2 Announce Type: replace \nAbstract: Vision--Language--Action\
    \ (VLA) models often use intermediate representations to connect multimodal inputs\
    \ with continuous control, yet spatial guidance is often injected implicitly through\
    \ latent features. We propose CorridorVLA, which predicts sparse spatial anchors\
    \ as incremental physical changes (e.g., end-effector $\\Delta$-positions) and\
    \ uses them to impose an explicit tolerance region in the training objective for\
    \ action generation. The anchors define a tolerance corridor that guides a flow-matching\
    \ action head: trajectories whose implied spatial evolution falls outside the\
    \ corridor receive corrective gradients, while trajectories within the corridor\
    \ are refined by a consistency objective. CorridorVLA improves SmolVLA by 4.45\
    \ percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and 7.98\
    \ percentage points, respectively, on the more challenging LIBERO-Plus benchmark.\
    \ Notably, under the same single-policy 4-in-1 setting, where one policy is jointly\
    \ trained and evaluated across all task suites, GR00T-Corr achieves an 83.21%\
    \ success rate. These results indicate that action-aligned physical cues can provide\
    \ direct and interpretable constraints for generative action policies, complementing\
    \ spatial guidance encoded in visual or latent forms. Code and released model\
    \ checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA."
  ko: "arXiv:2604.21241v2 Announce Type: replace \nAbstract: Vision--Language--Action\
    \ (VLA) models often use intermediate representations to connect multimodal inputs\
    \ with continuous control, yet spatial guidance is often injected implicitly through\
    \ latent features. We propose CorridorVLA, which predicts sparse spatial anchors\
    \ as incremental physical changes (e.g., end-effector $\\Delta$-positions) and\
    \ uses them to impose an explicit tolerance region in the training objective for\
    \ action generation. The anchors define a tolerance corridor that guides a flow-matching\
    \ action head: trajectories whose implied spatial evolution falls outside the\
    \ corridor receive corrective gradients, while trajectories within the corridor\
    \ are refined by a consistency objective. CorridorVLA improves SmolVLA by 4.45\
    \ percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and 7.98\
    \ percentage points, respectively, on the more challenging LIBERO-Plus benchmark.\
    \ Notably, under the same single-policy 4-in-1 setting, where one policy is jointly\
    \ trained and evaluated across all task suites, GR00T-Corr achieves an 83.21%\
    \ success rate. These results indicate that action-aligned physical cues can provide\
    \ direct and interpretable constraints for generative action policies, complementing\
    \ spatial guidance encoded in visual or latent forms. Code and released model\
    \ checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA."
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
- corridorvla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via
    Sparse Anchors (arXiv)'
  url: https://arxiv.org/abs/2604.21241
  date: '2026'
  accessed_at: '2026-07-08'
---

## 概述
arXiv:2604.21241v2 Announce Type: replace 
Abstract: Vision--Language--Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. We propose CorridorVLA, which predicts sparse spatial anchors as incremental physical changes (e.g., end-effector $\Delta$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation. The anchors define a tolerance corridor that guides a flow-matching action head: trajectories whose implied spatial evolution falls outside the corridor receive corrective gradients, while trajectories within the corridor are refined by a consistency objective. CorridorVLA improves SmolVLA by 4.45 percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and 7.98 percentage points, respectively, on the more challenging LIBERO-Plus benchmark. Notably, under the same single-policy 4-in-1 setting, where one policy is jointly trained and evaluated across all task suites, GR00T-Corr achieves an 83.21% success rate. These results indicate that action-aligned physical cues can provide direct and interpretable constraints for generative action policies, complementing spatial guidance encoded in visual or latent forms. Code and released model checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA.

## Overview
arXiv:2604.21241v2 Announce Type: replace 
Abstract: Vision--Language--Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. We propose CorridorVLA, which predicts sparse spatial anchors as incremental physical changes (e.g., end-effector $\Delta$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation. The anchors define a tolerance corridor that guides a flow-matching action head: trajectories whose implied spatial evolution falls outside the corridor receive corrective gradients, while trajectories within the corridor are refined by a consistency objective. CorridorVLA improves SmolVLA by 4.45 percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and 7.98 percentage points, respectively, on the more challenging LIBERO-Plus benchmark. Notably, under the same single-policy 4-in-1 setting, where one policy is jointly trained and evaluated across all task suites, GR00T-Corr achieves an 83.21% success rate. These results indicate that action-aligned physical cues can provide direct and interpretable constraints for generative action policies, complementing spatial guidance encoded in visual or latent forms. Code and released model checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA.

## 개요
arXiv:2604.21241v2 Announce Type: replace 
Abstract: Vision--Language--Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. We propose CorridorVLA, which predicts sparse spatial anchors as incremental physical changes (e.g., end-effector $\Delta$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation. The anchors define a tolerance corridor that guides a flow-matching action head: trajectories whose implied spatial evolution falls outside the corridor receive corrective gradients, while trajectories within the corridor are refined by a consistency objective. CorridorVLA improves SmolVLA by 4.45 percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and 7.98 percentage points, respectively, on the more challenging LIBERO-Plus benchmark. Notably, under the same single-policy 4-in-1 setting, where one policy is jointly trained and evaluated across all task suites, GR00T-Corr achieves an 83.21% success rate. These results indicate that action-aligned physical cues can provide direct and interpretable constraints for generative action policies, complementing spatial guidance encoded in visual or latent forms. Code and released model checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA.
