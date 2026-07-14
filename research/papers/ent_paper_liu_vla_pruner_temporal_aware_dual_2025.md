---
$id: ent_paper_liu_vla_pruner_temporal_aware_dual_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference'
  zh: VLA-Pruner
  ko: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference'
summary:
  en: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference (VLA-Pruner),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by School of AI, Shanghai Jiao Tong
    University, University of Science and Technology of China, Harbin Institute of Technology (Shenzhen), BAAI.'
  zh: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference (VLA-Pruner),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by School of AI, Shanghai Jiao Tong
    University, University of Science and Technology of China, Harbin Institute of Technology (Shenzhen), BAAI.'
  ko: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference (VLA-Pruner),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by School of AI, Shanghai Jiao Tong
    University, University of Science and Technology of China, Harbin Institute of Technology (Shenzhen), BAAI.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
- vla_pruner
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16449v5.
sources:
- id: src_001
  type: paper
  title: 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference (arXiv)'
  url: https://arxiv.org/abs/2511.16449
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-Pruner source
  url: https://doi.org/10.48550/arXiv.2511.16449
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown great potential for embodied AI by integrating visual perception, language understanding, and action execution. In real-time deployment, these models must process continuous visual streams, incurring substantial computational overhead. Visual token pruning -- a mainstream technique for accelerating Vision-Language Models (VLMs) by retaining salient tokens while discarding redundant ones -- offers a natural candidate solution to this challenge. However, directly applying VLM-oriented pruning methods to VLA inference can cause severe degradation in manipulation performance. Our analysis attributes this degradation to a key mismatch: VLA inference exhibits distinct attention patterns between the vision-language prefill stage and the action-decode stage, so pruning based only on context-prefill semantic salience is biased toward semantic cues and may remove action-critical visual tokens. Motivated by this observation, we propose VLA-Pruner, an effective plug-and-play token pruning method grounded in the visual requirements of VLA inference, further exploiting the temporal continuity of robot manipulation. Specifically, VLA-Pruner estimates visual-token importance from both semantic prefilling and temporally smoothed action relevance, and then applies a Combine-then-Filter strategy to retain compact, non-redundant tokens under the compute budget. Experiments show that VLA-Pruner outperforms state-of-the-art approaches across multiple VLA architectures, achieving up to 1.99x speedup with comparable manipulation quality.

## 核心内容
Vision-Language-Action (VLA) models have shown great potential for embodied AI by integrating visual perception, language understanding, and action execution. In real-time deployment, these models must process continuous visual streams, incurring substantial computational overhead. Visual token pruning -- a mainstream technique for accelerating Vision-Language Models (VLMs) by retaining salient tokens while discarding redundant ones -- offers a natural candidate solution to this challenge. However, directly applying VLM-oriented pruning methods to VLA inference can cause severe degradation in manipulation performance. Our analysis attributes this degradation to a key mismatch: VLA inference exhibits distinct attention patterns between the vision-language prefill stage and the action-decode stage, so pruning based only on context-prefill semantic salience is biased toward semantic cues and may remove action-critical visual tokens. Motivated by this observation, we propose VLA-Pruner, an effective plug-and-play token pruning method grounded in the visual requirements of VLA inference, further exploiting the temporal continuity of robot manipulation. Specifically, VLA-Pruner estimates visual-token importance from both semantic prefilling and temporally smoothed action relevance, and then applies a Combine-then-Filter strategy to retain compact, non-redundant tokens under the compute budget. Experiments show that VLA-Pruner outperforms state-of-the-art approaches across multiple VLA architectures, achieving up to 1.99x speedup with comparable manipulation quality.

## 参考
- http://arxiv.org/abs/2511.16449v5

