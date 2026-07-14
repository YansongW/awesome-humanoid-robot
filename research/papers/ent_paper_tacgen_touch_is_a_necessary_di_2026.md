---
$id: ent_paper_tacgen_touch_is_a_necessary_di_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TacGen: Touch Is a Necessary Dimension of Physical-World Representation -- Addressing Tactile Data Scarcity with Scalable
    Vision-to-Touch Alignment and Generation'
  zh: 'TacGen: Touch Is a Necessary Dimension of Physical-World Representation -- Addressing Tactile Data Scarcity with Scalable
    Vision-to-Touch Alignment and Generation'
  ko: 'TacGen: Touch Is a Necessary Dimension of Physical-World Representation -- Addressing Tactile Data Scarcity with Scalable
    Vision-to-Touch Alignment and Generation'
summary:
  en: "arXiv:2606.29173v2 Announce Type: replace \nAbstract: Touch resolves the physical-property ambiguity left by vision:\
    \ exploratory contact recovers shape, texture, compliance, and material, and visuo-haptic object representations converge\
    \ in ventral visual cortex. We ask whether representation learning can reproduce this grounding. TacGen mitigates the\
    \ tactile-data scarcity bottleneck by combining pre-specified V+T contrastive alignment with a latent-space residual-MLP\
    \ V->T generator that synthesizes tactile latents from RGB for tactile-data scaling. With matched DINOv2 backbones, splits,\
    \ and probes, V+T improves matched V-only on mass (Delta R^2=+0.570), density (Delta acc=+0.067), hardness (+0.117), and\
    \ uncertainty-banded force labels (Delta R^2=+0.281); all CIs exclude zero. The same representation lifts matched-capacity\
    \ TACTO manipulation 0.246->0.979 while V-only capacity scaling accounts for only 4.5% of the gap, preserving 95.5%. The\
    \ generator reaches cross-seed +0.589, with real tactile +0.585 inside the seed interval; the architecture comparison\
    \ shows a 13pp downstream gap between reconstruction quality and representation utility. Across five-seed SSVTP/TVL reproductions,\
    \ YCB-Sight transfer, three-backbone checks, permutation/random-feature controls, hash-verified manifests, and measured-force\
    \ validation checks, the evidence supports the claim that touch supplies a necessary physical evidence channel for representations\
    \ of contact-dependent properties."
  zh: "arXiv:2606.29173v2 Announce Type: replace \nAbstract: Touch resolves the physical-property ambiguity left by vision:\
    \ exploratory contact recovers shape, texture, compliance, and material, and visuo-haptic object representations converge\
    \ in ventral visual cortex. We ask whether representation learning can reproduce this grounding. TacGen mitigates the\
    \ tactile-data scarcity bottleneck by combining pre-specified V+T contrastive alignment with a latent-space residual-MLP\
    \ V->T generator that synthesizes tactile latents from RGB for tactile-data scaling. With matched DINOv2 backbones, splits,\
    \ and probes, V+T improves matched V-only on mass (Delta R^2=+0.570), density (Delta acc=+0.067), hardness (+0.117), and\
    \ uncertainty-banded force labels (Delta R^2=+0.281); all CIs exclude zero. The same representation lifts matched-capacity\
    \ TACTO manipulation 0.246->0.979 while V-only capacity scaling accounts for only 4.5% of the gap, preserving 95.5%. The\
    \ generator reaches cross-seed +0.589, with real tactile +0.585 inside the seed interval; the architecture comparison\
    \ shows a 13pp downstream gap between reconstruction quality and representation utility. Across five-seed SSVTP/TVL reproductions,\
    \ YCB-Sight transfer, three-backbone checks, permutation/random-feature controls, hash-verified manifests, and measured-force\
    \ validation checks, the evidence supports the claim that touch supplies a necessary physical evidence channel for representations\
    \ of contact-dependent properties."
  ko: "arXiv:2606.29173v2 Announce Type: replace \nAbstract: Touch resolves the physical-property ambiguity left by vision:\
    \ exploratory contact recovers shape, texture, compliance, and material, and visuo-haptic object representations converge\
    \ in ventral visual cortex. We ask whether representation learning can reproduce this grounding. TacGen mitigates the\
    \ tactile-data scarcity bottleneck by combining pre-specified V+T contrastive alignment with a latent-space residual-MLP\
    \ V->T generator that synthesizes tactile latents from RGB for tactile-data scaling. With matched DINOv2 backbones, splits,\
    \ and probes, V+T improves matched V-only on mass (Delta R^2=+0.570), density (Delta acc=+0.067), hardness (+0.117), and\
    \ uncertainty-banded force labels (Delta R^2=+0.281); all CIs exclude zero. The same representation lifts matched-capacity\
    \ TACTO manipulation 0.246->0.979 while V-only capacity scaling accounts for only 4.5% of the gap, preserving 95.5%. The\
    \ generator reaches cross-seed +0.589, with real tactile +0.585 inside the seed interval; the architecture comparison\
    \ shows a 13pp downstream gap between reconstruction quality and representation utility. Across five-seed SSVTP/TVL reproductions,\
    \ YCB-Sight transfer, three-backbone checks, permutation/random-feature controls, hash-verified manifests, and measured-force\
    \ validation checks, the evidence supports the claim that touch supplies a necessary physical evidence channel for representations\
    \ of contact-dependent properties."
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
- tacgen
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.29173v2.
sources:
- id: src_001
  type: paper
  title: 'TacGen: Touch Is a Necessary Dimension of Physical-World Representation -- Addressing Tactile Data Scarcity with
    Scalable Vision-to-Touch Alignment and Generation'
  url: https://arxiv.org/abs/2606.29173
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Touch resolves the physical-property ambiguity left by vision: exploratory contact recovers shape, texture, compliance, and material, and visuo-haptic object representations converge in ventral visual cortex. We ask whether representation learning can reproduce this grounding. TacGen mitigates the tactile-data scarcity bottleneck by combining pre-specified V+T contrastive alignment with a latent-space residual-MLP V->T generator that synthesizes tactile latents from RGB for tactile-data scaling. With matched DINOv2 backbones, splits, and probes, V+T improves matched V-only on mass (Delta R^2=+0.570), density (Delta acc=+0.067), hardness (+0.117), and uncertainty-banded force labels (Delta R^2=+0.281); all CIs exclude zero. The same representation lifts matched-capacity TACTO manipulation 0.246->0.979 while V-only capacity scaling accounts for only 4.5% of the gap, preserving 95.5%. The generator reaches cross-seed +0.589, with real tactile +0.585 inside the seed interval; the architecture comparison shows a 13pp downstream gap between reconstruction quality and representation utility. Across five-seed SSVTP/TVL reproductions, YCB-Sight transfer, three-backbone checks, permutation/random-feature controls, hash-verified manifests, and measured-force validation checks, the evidence supports the claim that touch supplies a necessary physical evidence channel for representations of contact-dependent properties.

## 核心内容
Touch resolves the physical-property ambiguity left by vision: exploratory contact recovers shape, texture, compliance, and material, and visuo-haptic object representations converge in ventral visual cortex. We ask whether representation learning can reproduce this grounding. TacGen mitigates the tactile-data scarcity bottleneck by combining pre-specified V+T contrastive alignment with a latent-space residual-MLP V->T generator that synthesizes tactile latents from RGB for tactile-data scaling. With matched DINOv2 backbones, splits, and probes, V+T improves matched V-only on mass (Delta R^2=+0.570), density (Delta acc=+0.067), hardness (+0.117), and uncertainty-banded force labels (Delta R^2=+0.281); all CIs exclude zero. The same representation lifts matched-capacity TACTO manipulation 0.246->0.979 while V-only capacity scaling accounts for only 4.5% of the gap, preserving 95.5%. The generator reaches cross-seed +0.589, with real tactile +0.585 inside the seed interval; the architecture comparison shows a 13pp downstream gap between reconstruction quality and representation utility. Across five-seed SSVTP/TVL reproductions, YCB-Sight transfer, three-backbone checks, permutation/random-feature controls, hash-verified manifests, and measured-force validation checks, the evidence supports the claim that touch supplies a necessary physical evidence channel for representations of contact-dependent properties.

## 参考
- http://arxiv.org/abs/2606.29173v2

