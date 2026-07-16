---
$id: ent_paper_dc_motion_decoupling_structure_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DC-Motion: Decoupling Structure and Details via Discrete-Continuous Tokens for Human Motion Generation'
  zh: 'DC-Motion: Decoupling Structure and Details via Discrete-Continuous Tokens for Human Motion Generation'
  ko: 'DC-Motion: Decoupling Structure and Details via Discrete-Continuous Tokens for Human Motion Generation'
summary:
  en: 'arXiv:2606.14721v2 Announce Type: replace-cross Abstract: Text-to-motion generation requires modeling both global action
    structure and fine-grained motion dynamics from natural language. Existing approaches typically rely on either continuous
    diffusion models or vector-quantized discrete representations. Diffusion models generate smooth motions but lack explicit
    compositional structure for temporal planning, while discrete token-based methods improve controllability but compress
    motion into finite codebooks, losing fine-grained dynamics. We argue that this limitation stems from a representation
    mismatch: action semantics such as intent, phase transitions, and temporal layout are inherently discrete and compositional,
    whereas joint trajectories and motion dynamics are continuous and locally correlated. To address this, we propose DC-Motion,
    a discrete-continuous factorized framework for human motion generation. DC-Motion decomposes motion into discrete structural
    tokens capturing global action layout and continuous residual latents modeling fine-grained dynamics. A text-conditioned
    structure generator predicts discrete tokens via iterative masked modeling, and a diffusion-based residual generator produces
    continuous motion conditioned on the structure. Experiments on HumanML3D and KIT-ML demonstrate that DC-Motion achieves
    strong performance in both FID and R-Precision, outperforming representative diffusion-based and discrete-token baselines.'
  zh: 'arXiv:2606.14721v2 Announce Type: replace-cross Abstract: Text-to-motion generation requires modeling both global action
    structure and fine-grained motion dynamics from natural language. Existing approaches typically rely on either continuous
    diffusion models or vector-quantized discrete representations. Diffusion models generate smooth motions but lack explicit
    compositional structure for temporal planning, while discrete token-based methods improve controllability but compress
    motion into finite codebooks, losing fine-grained dynamics. We argue that this limitation stems from a representation
    mismatch: action semantics such as intent, phase transitions, and temporal layout are inherently discrete and compositional,
    whereas joint trajectories and motion dynamics are continuous and locally correlated. To address this, we propose DC-Motion,
    a discrete-continuous factorized framework for human motion generation. DC-Motion decomposes motion into discrete structural
    tokens capturing global action layout and continuous residual latents modeling fine-grained dynamics. A text-conditioned
    structure generator predicts discrete tokens via iterative masked modeling, and a diffusion-based residual generator produces
    continuous motion conditioned on the structure. Experiments on HumanML3D and KIT-ML demonstrate that DC-Motion achieves
    strong performance in both FID and R-Precision, outperforming representative diffusion-based and discrete-token baselines.'
  ko: 'arXiv:2606.14721v2 Announce Type: replace-cross Abstract: Text-to-motion generation requires modeling both global action
    structure and fine-grained motion dynamics from natural language. Existing approaches typically rely on either continuous
    diffusion models or vector-quantized discrete representations. Diffusion models generate smooth motions but lack explicit
    compositional structure for temporal planning, while discrete token-based methods improve controllability but compress
    motion into finite codebooks, losing fine-grained dynamics. We argue that this limitation stems from a representation
    mismatch: action semantics such as intent, phase transitions, and temporal layout are inherently discrete and compositional,
    whereas joint trajectories and motion dynamics are continuous and locally correlated. To address this, we propose DC-Motion,
    a discrete-continuous factorized framework for human motion generation. DC-Motion decomposes motion into discrete structural
    tokens capturing global action layout and continuous residual latents modeling fine-grained dynamics. A text-conditioned
    structure generator predicts discrete tokens via iterative masked modeling, and a diffusion-based residual generator produces
    continuous motion conditioned on the structure. Experiments on HumanML3D and KIT-ML demonstrate that DC-Motion achieves
    strong performance in both FID and R-Precision, outperforming representative diffusion-based and discrete-token baselines.'
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
- dc_motion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.14721v2.
sources:
- id: src_001
  type: paper
  title: 'DC-Motion: Decoupling Structure and Details via Discrete-Continuous Tokens for Human Motion Generation (arXiv)'
  url: https://arxiv.org/abs/2606.14721
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Text-to-motion generation requires modeling both global action structure and fine-grained motion dynamics from natural language. Existing approaches typically rely on either continuous diffusion models or vector-quantized discrete representations. Diffusion models generate smooth motions but lack explicit compositional structure for temporal planning, while discrete token-based methods improve controllability but compress motion into finite codebooks, losing fine-grained dynamics. We argue that this limitation stems from a representation mismatch: action semantics such as intent, phase transitions, and temporal layout are inherently discrete and compositional, whereas joint trajectories and motion dynamics are continuous and locally correlated. To address this, we propose DC-Motion, a discrete-continuous factorized framework for human motion generation. DC-Motion decomposes motion into discrete structural tokens capturing global action layout and continuous residual latents modeling fine-grained dynamics. A text-conditioned structure generator predicts discrete tokens via iterative masked modeling, and a diffusion-based residual generator produces continuous motion conditioned on the structure. Experiments on HumanML3D and KIT-ML demonstrate that DC-Motion achieves strong performance in both FID and R-Precision, outperforming representative diffusion-based and discrete-token baselines.

## 核心内容
Text-to-motion generation requires modeling both global action structure and fine-grained motion dynamics from natural language. Existing approaches typically rely on either continuous diffusion models or vector-quantized discrete representations. Diffusion models generate smooth motions but lack explicit compositional structure for temporal planning, while discrete token-based methods improve controllability but compress motion into finite codebooks, losing fine-grained dynamics. We argue that this limitation stems from a representation mismatch: action semantics such as intent, phase transitions, and temporal layout are inherently discrete and compositional, whereas joint trajectories and motion dynamics are continuous and locally correlated. To address this, we propose DC-Motion, a discrete-continuous factorized framework for human motion generation. DC-Motion decomposes motion into discrete structural tokens capturing global action layout and continuous residual latents modeling fine-grained dynamics. A text-conditioned structure generator predicts discrete tokens via iterative masked modeling, and a diffusion-based residual generator produces continuous motion conditioned on the structure. Experiments on HumanML3D and KIT-ML demonstrate that DC-Motion achieves strong performance in both FID and R-Precision, outperforming representative diffusion-based and discrete-token baselines.

## 参考
- http://arxiv.org/abs/2606.14721v2

