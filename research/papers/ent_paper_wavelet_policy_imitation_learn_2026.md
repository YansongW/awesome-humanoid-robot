---
$id: ent_paper_wavelet_policy_imitation_learn_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Wavelet Policy: Imitation Learning in the Scale Domain with World Prior Memory'
  zh: 'Wavelet Policy: Imitation Learning in the Scale Domain with World Prior Memory'
  ko: ''
summary:
  en: "arXiv:2504.04991v5 Announce Type: replace \nAbstract: Conventional visuomotor\
    \ imitation learning usually predicts future robot actions directly in the time\
    \ domain. Such formulations often have limited physical scene awareness and weak\
    \ memory. In this work, we propose Wavelet Policy, a lightweight imitation learning\
    \ framework that combines World Prior Memory (WPM) with wavelet-based multi-scale\
    \ action modeling. Our key idea is to encode persistent physical scene structure\
    \ from static background images into compact memory tokens, which are fused into\
    \ world-prior tokens and injected into the encoder during forward propagation.\
    \ Based on this memory-conditioned representation, we further perform wavelet-domain\
    \ decomposition over horizon-aligned latent action tokens and adopt a Single-Encoder\
    \ Multiple-Decoder (SE2MD) architecture to model latent components at different\
    \ temporal scales. The resulting latent subbands are reconstructed through inverse\
    \ wavelet transform and finally projected into executable action chunks. To facilitate\
    \ efficient world prior learning, we introduce a world-prior adaptation loss,\
    \ encouraging the background encoder to retain persistent scene knowledge while\
    \ remaining lightweight and stable. Extensive experiments on four simulated and\
    \ six real-world robotic manipulation tasks show that Wavelet Policy consistently\
    \ outperforms strong baselines. These results demonstrate that combining scale-domain\
    \ action modeling with world-prior memory provides an effective and efficient\
    \ solution for embodied manipulation."
  zh: "arXiv:2504.04991v5 Announce Type: replace \nAbstract: Conventional visuomotor\
    \ imitation learning usually predicts future robot actions directly in the time\
    \ domain. Such formulations often have limited physical scene awareness and weak\
    \ memory. In this work, we propose Wavelet Policy, a lightweight imitation learning\
    \ framework that combines World Prior Memory (WPM) with wavelet-based multi-scale\
    \ action modeling. Our key idea is to encode persistent physical scene structure\
    \ from static background images into compact memory tokens, which are fused into\
    \ world-prior tokens and injected into the encoder during forward propagation.\
    \ Based on this memory-conditioned representation, we further perform wavelet-domain\
    \ decomposition over horizon-aligned latent action tokens and adopt a Single-Encoder\
    \ Multiple-Decoder (SE2MD) architecture to model latent components at different\
    \ temporal scales. The resulting latent subbands are reconstructed through inverse\
    \ wavelet transform and finally projected into executable action chunks. To facilitate\
    \ efficient world prior learning, we introduce a world-prior adaptation loss,\
    \ encouraging the background encoder to retain persistent scene knowledge while\
    \ remaining lightweight and stable. Extensive experiments on four simulated and\
    \ six real-world robotic manipulation tasks show that Wavelet Policy consistently\
    \ outperforms strong baselines. These results demonstrate that combining scale-domain\
    \ action modeling with world-prior memory provides an effective and efficient\
    \ solution for embodied manipulation."
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
- wavelet_policy
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
  title: 'Wavelet Policy: Imitation Learning in the Scale Domain with World Prior
    Memory'
  url: https://arxiv.org/abs/2504.04991
  date: '2026'
  accessed_at: '2026-07-01'
---

arXiv:2504.04991v5 Announce Type: replace 
Abstract: Conventional visuomotor imitation learning usually predicts future robot actions directly in the time domain. Such formulations often have limited physical scene awareness and weak memory. In this work, we propose Wavelet Policy, a lightweight imitation learning framework that combines World Prior Memory (WPM) with wavelet-based multi-scale action modeling. Our key idea is to encode persistent physical scene structure from static background images into compact memory tokens, which are fused into world-prior tokens and injected into the encoder during forward propagation. Based on this memory-conditioned representation, we further perform wavelet-domain decomposition over horizon-aligned latent action tokens and adopt a Single-Encoder Multiple-Decoder (SE2MD) architecture to model latent components at different temporal scales. The resulting latent subbands are reconstructed through inverse wavelet transform and finally projected into executable action chunks. To facilitate efficient world prior learning, we introduce a world-prior adaptation loss, encouraging the background encoder to retain persistent scene knowledge while remaining lightweight and stable. Extensive experiments on four simulated and six real-world robotic manipulation tasks show that Wavelet Policy consistently outperforms strong baselines. These results demonstrate that combining scale-domain action modeling with world-prior memory provides an effective and efficient solution for embodied manipulation.
