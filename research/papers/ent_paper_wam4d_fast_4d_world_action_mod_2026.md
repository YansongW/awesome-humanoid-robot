---
$id: ent_paper_wam4d_fast_4d_world_action_mod_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WAM4D: Fast 4D World Action Model via Spatial Register Tokens'
  zh: 'WAM4D: Fast 4D World Action Model via Spatial Register Tokens'
  ko: ''
summary:
  en: "arXiv:2606.14048v2 Announce Type: replace-cross \nAbstract: World action models\
    \ (WAMs) have recently shown promise in jointly modeling future observations and\
    \ executable robot actions. However, most existing WAMs still operate in 2D video\
    \ or latent spaces, where visually plausible rollouts miss the 3D spatial constraints\
    \ and occluded contact geometry required for precise manipulation. While geometric\
    \ foundation models offer strong priors for recovering dense 3D structure and\
    \ motion from visual observations, forcing WAMs to predict the dense 4D representation\
    \ introduces costly geometric decoding and slows down causal action generation.\
    \ To address the trade-off, we present WAM4D, a fast 4D world action model that\
    \ uses lightweight spatial register tokens as training-time future-depth readouts\
    \ to transfer pretrained geometric priors into a causal video-action transformer,\
    \ then removes the register branch for lightweight action inference. To prevent\
    \ non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers\
    \ (MoT) WAM backbone, defining modality-specific visibility among video, action,\
    \ and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging\
    \ real-world manipulation tasks show that WAM4D improves spatial consistency and\
    \ achieves competitive action prediction while maintaining efficient inference."
  zh: "arXiv:2606.14048v2 Announce Type: replace-cross \nAbstract: World action models\
    \ (WAMs) have recently shown promise in jointly modeling future observations and\
    \ executable robot actions. However, most existing WAMs still operate in 2D video\
    \ or latent spaces, where visually plausible rollouts miss the 3D spatial constraints\
    \ and occluded contact geometry required for precise manipulation. While geometric\
    \ foundation models offer strong priors for recovering dense 3D structure and\
    \ motion from visual observations, forcing WAMs to predict the dense 4D representation\
    \ introduces costly geometric decoding and slows down causal action generation.\
    \ To address the trade-off, we present WAM4D, a fast 4D world action model that\
    \ uses lightweight spatial register tokens as training-time future-depth readouts\
    \ to transfer pretrained geometric priors into a causal video-action transformer,\
    \ then removes the register branch for lightweight action inference. To prevent\
    \ non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers\
    \ (MoT) WAM backbone, defining modality-specific visibility among video, action,\
    \ and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging\
    \ real-world manipulation tasks show that WAM4D improves spatial consistency and\
    \ achieves competitive action prediction while maintaining efficient inference."
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
- wam4d
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
  title: 'WAM4D: Fast 4D World Action Model via Spatial Register Tokens (arXiv)'
  url: https://arxiv.org/abs/2606.14048
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2606.14048v2 Announce Type: replace-cross 
Abstract: World action models (WAMs) have recently shown promise in jointly modeling future observations and executable robot actions. However, most existing WAMs still operate in 2D video or latent spaces, where visually plausible rollouts miss the 3D spatial constraints and occluded contact geometry required for precise manipulation. While geometric foundation models offer strong priors for recovering dense 3D structure and motion from visual observations, forcing WAMs to predict the dense 4D representation introduces costly geometric decoding and slows down causal action generation. To address the trade-off, we present WAM4D, a fast 4D world action model that uses lightweight spatial register tokens as training-time future-depth readouts to transfer pretrained geometric priors into a causal video-action transformer, then removes the register branch for lightweight action inference. To prevent non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone, defining modality-specific visibility among video, action, and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging real-world manipulation tasks show that WAM4D improves spatial consistency and achieves competitive action prediction while maintaining efficient inference.
