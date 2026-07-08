---
$id: ent_paper_lara_latent_action_representat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LARA: Latent Action Representation Alignment for Vision-Language-Action Models'
  zh: 'LARA: Latent Action Representation Alignment for Vision-Language-Action Models'
  ko: ''
summary:
  en: "arXiv:2606.07100v2 Announce Type: replace-cross \nAbstract: Visual-language\
    \ action (VLA) models enable robots to predict actions directly from observations\
    \ and language instructions, but their performance depends on large-scale, high-quality\
    \ data and is limited by the scarcity of real-world robot action datasets. To\
    \ facilitate VLA model learning with abundant unlabeled human videos, Latent Action\
    \ Models (LAM) learn latent action representations from visual dynamics to provide\
    \ additional supervision for VLA learning. However, LAM and VLA are typically\
    \ trained separately, leaving LAM ungrounded during VLA training and VLA models\
    \ constrained by frozen LAM representations. To address these issues, we propose\
    \ Latent Action Representation Alignment (LARA), a plug-and-play framework that\
    \ jointly optimizes LAM and VLA via representation alignment. This enables reciprocal\
    \ benefits where LAMs learn with action trajectories to avoid spurious visual\
    \ changes, while VLAs are regularized by forward dynamics learned within LAMs\
    \ to reduce hallucinations of functionally ineffective trajectories. We demonstrate\
    \ LARA versatility and effectiveness for pre-training, post-training enhancement\
    \ of pre-trained VLA models, and LAM refinement, achieving an average of ~10%,\
    \ ~5%, and ~15% improvement over 3 simulation and 1 meticulously designed real-world\
    \ robotic manipulation benchmarks."
  zh: "arXiv:2606.07100v2 Announce Type: replace-cross \nAbstract: Visual-language\
    \ action (VLA) models enable robots to predict actions directly from observations\
    \ and language instructions, but their performance depends on large-scale, high-quality\
    \ data and is limited by the scarcity of real-world robot action datasets. To\
    \ facilitate VLA model learning with abundant unlabeled human videos, Latent Action\
    \ Models (LAM) learn latent action representations from visual dynamics to provide\
    \ additional supervision for VLA learning. However, LAM and VLA are typically\
    \ trained separately, leaving LAM ungrounded during VLA training and VLA models\
    \ constrained by frozen LAM representations. To address these issues, we propose\
    \ Latent Action Representation Alignment (LARA), a plug-and-play framework that\
    \ jointly optimizes LAM and VLA via representation alignment. This enables reciprocal\
    \ benefits where LAMs learn with action trajectories to avoid spurious visual\
    \ changes, while VLAs are regularized by forward dynamics learned within LAMs\
    \ to reduce hallucinations of functionally ineffective trajectories. We demonstrate\
    \ LARA versatility and effectiveness for pre-training, post-training enhancement\
    \ of pre-trained VLA models, and LAM refinement, achieving an average of ~10%,\
    \ ~5%, and ~15% improvement over 3 simulation and 1 meticulously designed real-world\
    \ robotic manipulation benchmarks."
  ko: ''
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
- lara
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported from arXiv cs.RO RSS feed.
sources:
- id: src_001
  type: paper
  title: 'LARA: Latent Action Representation Alignment for Vision-Language-Action
    Models'
  url: https://arxiv.org/abs/2606.07100
  date: '2026'
  accessed_at: '2026-07-01'
---

arXiv:2606.07100v2 Announce Type: replace-cross 
Abstract: Visual-language action (VLA) models enable robots to predict actions directly from observations and language instructions, but their performance depends on large-scale, high-quality data and is limited by the scarcity of real-world robot action datasets. To facilitate VLA model learning with abundant unlabeled human videos, Latent Action Models (LAM) learn latent action representations from visual dynamics to provide additional supervision for VLA learning. However, LAM and VLA are typically trained separately, leaving LAM ungrounded during VLA training and VLA models constrained by frozen LAM representations. To address these issues, we propose Latent Action Representation Alignment (LARA), a plug-and-play framework that jointly optimizes LAM and VLA via representation alignment. This enables reciprocal benefits where LAMs learn with action trajectories to avoid spurious visual changes, while VLAs are regularized by forward dynamics learned within LAMs to reduce hallucinations of functionally ineffective trajectories. We demonstrate LARA versatility and effectiveness for pre-training, post-training enhancement of pre-trained VLA models, and LAM refinement, achieving an average of ~10%, ~5%, and ~15% improvement over 3 simulation and 1 meticulously designed real-world robotic manipulation benchmarks.
