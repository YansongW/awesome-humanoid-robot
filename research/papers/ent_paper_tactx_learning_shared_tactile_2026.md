---
$id: ent_paper_tactx_learning_shared_tactile_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TactX: Learning Shared Tactile Representations Across Diverse Sensors'
  zh: 'TactX: Learning Shared Tactile Representations Across Diverse Sensors'
  ko: ''
summary:
  en: "arXiv:2606.31236v1 Announce Type: new \nAbstract: Tactile sensors provide critical\
    \ information for contact-rich manipulation, yet tactile representations and policies\
    \ remain tightly coupled to each specific sensor, limiting transferability across\
    \ robots and hardware platforms. We propose TactX, a framework for learning a\
    \ transferable tactile representation across sensors spanning three fundamentally\
    \ different transduction modalities: resistive, magnetic, and vision-based. TactX\
    \ maps heterogeneous tactile observations into a shared latent space through modality-specific\
    \ encoders trained on paired contact data. Such paired interactions provide a\
    \ natural alignment signal across modalities, and the encoders are jointly trained\
    \ across all sensor pairs, inducing a consistent latent space for all sensor types.\
    \ Our experiments show that TactX aligns tactile representations across sensors\
    \ while preserving object-level contact information, as evidenced by sensor-identity\
    \ prediction and object classification in the learned latent space. We evaluate\
    \ TactX on four contact-rich manipulation tasks: pick-and-place, plug insertion,\
    \ board wiping, and object reorientation, and show that policies trained with\
    \ one sensor transfer zero-shot to physically distinct sensors through the shared\
    \ latent. This improves the average success rate from 27.5% for vision-only policy\
    \ to 45.9%, providing a step toward sensor-agnostic tactile manipulation."
  zh: "arXiv:2606.31236v1 Announce Type: new \nAbstract: Tactile sensors provide critical\
    \ information for contact-rich manipulation, yet tactile representations and policies\
    \ remain tightly coupled to each specific sensor, limiting transferability across\
    \ robots and hardware platforms. We propose TactX, a framework for learning a\
    \ transferable tactile representation across sensors spanning three fundamentally\
    \ different transduction modalities: resistive, magnetic, and vision-based. TactX\
    \ maps heterogeneous tactile observations into a shared latent space through modality-specific\
    \ encoders trained on paired contact data. Such paired interactions provide a\
    \ natural alignment signal across modalities, and the encoders are jointly trained\
    \ across all sensor pairs, inducing a consistent latent space for all sensor types.\
    \ Our experiments show that TactX aligns tactile representations across sensors\
    \ while preserving object-level contact information, as evidenced by sensor-identity\
    \ prediction and object classification in the learned latent space. We evaluate\
    \ TactX on four contact-rich manipulation tasks: pick-and-place, plug insertion,\
    \ board wiping, and object reorientation, and show that policies trained with\
    \ one sensor transfer zero-shot to physically distinct sensors through the shared\
    \ latent. This improves the average success rate from 27.5% for vision-only policy\
    \ to 45.9%, providing a step toward sensor-agnostic tactile manipulation."
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
- robotics
- tactx
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
  title: 'TactX: Learning Shared Tactile Representations Across Diverse Sensors'
  url: https://arxiv.org/abs/2606.31236
  date: '2026'
  accessed_at: '2026-07-01'
---

arXiv:2606.31236v1 Announce Type: new 
Abstract: Tactile sensors provide critical information for contact-rich manipulation, yet tactile representations and policies remain tightly coupled to each specific sensor, limiting transferability across robots and hardware platforms. We propose TactX, a framework for learning a transferable tactile representation across sensors spanning three fundamentally different transduction modalities: resistive, magnetic, and vision-based. TactX maps heterogeneous tactile observations into a shared latent space through modality-specific encoders trained on paired contact data. Such paired interactions provide a natural alignment signal across modalities, and the encoders are jointly trained across all sensor pairs, inducing a consistent latent space for all sensor types. Our experiments show that TactX aligns tactile representations across sensors while preserving object-level contact information, as evidenced by sensor-identity prediction and object classification in the learned latent space. We evaluate TactX on four contact-rich manipulation tasks: pick-and-place, plug insertion, board wiping, and object reorientation, and show that policies trained with one sensor transfer zero-shot to physically distinct sensors through the shared latent. This improves the average success rate from 27.5% for vision-only policy to 45.9%, providing a step toward sensor-agnostic tactile manipulation.
