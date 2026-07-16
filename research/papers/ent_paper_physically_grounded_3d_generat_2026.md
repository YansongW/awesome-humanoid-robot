---
$id: ent_paper_physically_grounded_3d_generat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
  zh: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
  ko: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
summary:
  en: 'arXiv:2604.09100v2 Announce Type: replace-cross Abstract: We propose a multimodal, physically grounded approach for
    metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware
    3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the
    posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded
    regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact
    latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining
    on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility
    masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and
    differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the
    reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure
    estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines
    geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves
    completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only
    baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different
    from those used during training.'
  zh: 'arXiv:2604.09100v2 Announce Type: replace-cross Abstract: We propose a multimodal, physically grounded approach for
    metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware
    3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the
    posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded
    regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact
    latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining
    on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility
    masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and
    differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the
    reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure
    estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines
    geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves
    completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only
    baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different
    from those used during training.'
  ko: 'arXiv:2604.09100v2 Announce Type: replace-cross Abstract: We propose a multimodal, physically grounded approach for
    metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware
    3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the
    posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded
    regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact
    latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining
    on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility
    masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and
    differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the
    reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure
    estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines
    geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves
    completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only
    baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different
    from those used during training.'
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
- physically_grounded_3d_generat
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.09100v2.
sources:
- id: src_001
  type: paper
  title: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
  url: https://arxiv.org/abs/2604.09100
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
We propose a multimodal, physically grounded approach for metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware 3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different from those used during training.

## 核心内容
We propose a multimodal, physically grounded approach for metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware 3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different from those used during training.

## 参考
- http://arxiv.org/abs/2604.09100v2

