---
$id: ent_paper_internvla_a15_unifying_underst_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization'
  zh: 'InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization'
  ko: 'InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization'
summary:
  en: "arXiv:2607.04988v1 Announce Type: new \nAbstract: Unified models for robot manipulation aim to equip one policy with\
    \ both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice,\
    \ existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives,\
    \ and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators\
    \ unexploited. We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA\
    \ and subtask prediction, and attaches a lightweight unified expert for continuous action generation. Future prediction\
    \ is recast as a latent-querying problem, where a small set of learnable foresight tokens condenses the task-relevant\
    \ future into a compact latent code under the supervision of a frozen pretrained video generation model, so the policy\
    \ inherits world-model dynamics priors without ever learning pixel-level generation. The video branch is discarded at\
    \ inference, keeping real-time control. Pretrained on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves\
    \ the best overall results on all six simulation benchmarks. In the real world, the preserved semantics deliver the strongest\
    \ compositional generalization on held-out instruction bindings, and the two designs together sustain long-horizon execution."
  zh: "arXiv:2607.04988v1 Announce Type: new \nAbstract: Unified models for robot manipulation aim to equip one policy with\
    \ both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice,\
    \ existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives,\
    \ and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators\
    \ unexploited. We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA\
    \ and subtask prediction, and attaches a lightweight unified expert for continuous action generation. Future prediction\
    \ is recast as a latent-querying problem, where a small set of learnable foresight tokens condenses the task-relevant\
    \ future into a compact latent code under the supervision of a frozen pretrained video generation model, so the policy\
    \ inherits world-model dynamics priors without ever learning pixel-level generation. The video branch is discarded at\
    \ inference, keeping real-time control. Pretrained on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves\
    \ the best overall results on all six simulation benchmarks. In the real world, the preserved semantics deliver the strongest\
    \ compositional generalization on held-out instruction bindings, and the two designs together sustain long-horizon execution."
  ko: "arXiv:2607.04988v1 Announce Type: new \nAbstract: Unified models for robot manipulation aim to equip one policy with\
    \ both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice,\
    \ existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives,\
    \ and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators\
    \ unexploited. We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA\
    \ and subtask prediction, and attaches a lightweight unified expert for continuous action generation. Future prediction\
    \ is recast as a latent-querying problem, where a small set of learnable foresight tokens condenses the task-relevant\
    \ future into a compact latent code under the supervision of a frozen pretrained video generation model, so the policy\
    \ inherits world-model dynamics priors without ever learning pixel-level generation. The video branch is discarded at\
    \ inference, keeping real-time control. Pretrained on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves\
    \ the best overall results on all six simulation benchmarks. In the real world, the preserved semantics deliver the strongest\
    \ compositional generalization on held-out instruction bindings, and the two designs together sustain long-horizon execution."
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
- internvla_a15
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04988v1.
sources:
- id: src_001
  type: paper
  title: 'InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization (arXiv)'
  url: https://arxiv.org/abs/2607.04988
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Unified models for robot manipulation aim to equip one policy with both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice, existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives, and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited. We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA and subtask prediction, and attaches a lightweight unified expert for continuous action generation. Future prediction is recast as a latent-querying problem, where a small set of learnable foresight tokens condenses the task-relevant future into a compact latent code under the supervision of a frozen pretrained video generation model, so the policy inherits world-model dynamics priors without ever learning pixel-level generation. The video branch is discarded at inference, keeping real-time control. Pretrained on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves the best overall results on all six simulation benchmarks. In the real world, the preserved semantics deliver the strongest compositional generalization on held-out instruction bindings, and the two designs together sustain long-horizon execution.

## 核心内容
Unified models for robot manipulation aim to equip one policy with both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice, existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives, and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited. We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA and subtask prediction, and attaches a lightweight unified expert for continuous action generation. Future prediction is recast as a latent-querying problem, where a small set of learnable foresight tokens condenses the task-relevant future into a compact latent code under the supervision of a frozen pretrained video generation model, so the policy inherits world-model dynamics priors without ever learning pixel-level generation. The video branch is discarded at inference, keeping real-time control. Pretrained on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves the best overall results on all six simulation benchmarks. In the real world, the preserved semantics deliver the strongest compositional generalization on held-out instruction bindings, and the two designs together sustain long-horizon execution.

## 参考
- http://arxiv.org/abs/2607.04988v1

