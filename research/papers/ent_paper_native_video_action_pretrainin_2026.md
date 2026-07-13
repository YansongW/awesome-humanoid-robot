---
$id: ent_paper_native_video_action_pretrainin_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Native Video-Action Pretraining for Generalizable Robot Control
  zh: Native Video-Action Pretraining for Generalizable Robot Control
  ko: ''
summary:
  en: "arXiv:2607.08639v1 Announce Type: new \nAbstract: The advent of video-action\
    \ models offers a promising path for robot control. Nevertheless, we argue that\
    \ repurposing video generative models designed for digital content creation is\
    \ inherently inadequate for physical environments. To bridge this gap, we present\
    \ LingBot-VA 2.0, a video-action foundation model built from the ground up for\
    \ embodiment. Four core design principles showcase its evolution from LingBot-VA.\
    \ (1) Departing from traditional reconstruction-focused VAEs, we introduce a semantic\
    \ visual-action tokenizer, which aligns visual representations with both semantics\
    \ and actions, improving instruction following and action precision in subsequent\
    \ policy learning. (2) Given the strictly causal nature of temporal dynamics,\
    \ we adopt a causal pretraining paradigm, training from scratch to circumvent\
    \ the catastrophic forgetting that frequently occurs when adapting bidirectional\
    \ architectures. (3) To meet the demands of high-frequency inference, our model\
    \ employs a sparse MoE backbone, expanding model capacity without compromising\
    \ efficiency. (4) Real-time closed-loop control is realized through an enhanced\
    \ asynchronous inference scheme, which predicts future latents in parallel with\
    \ action execution while re-grounding each rollout on the latest observation via\
    \ learned forward dynamics. Real-world deployment validates LingBot-VA 2.0 as\
    \ a robust foundation model, as evidenced by its few-shot generalization across\
    \ complex manipulation tasks."
  zh: "arXiv:2607.08639v1 Announce Type: new \nAbstract: The advent of video-action\
    \ models offers a promising path for robot control. Nevertheless, we argue that\
    \ repurposing video generative models designed for digital content creation is\
    \ inherently inadequate for physical environments. To bridge this gap, we present\
    \ LingBot-VA 2.0, a video-action foundation model built from the ground up for\
    \ embodiment. Four core design principles showcase its evolution from LingBot-VA.\
    \ (1) Departing from traditional reconstruction-focused VAEs, we introduce a semantic\
    \ visual-action tokenizer, which aligns visual representations with both semantics\
    \ and actions, improving instruction following and action precision in subsequent\
    \ policy learning. (2) Given the strictly causal nature of temporal dynamics,\
    \ we adopt a causal pretraining paradigm, training from scratch to circumvent\
    \ the catastrophic forgetting that frequently occurs when adapting bidirectional\
    \ architectures. (3) To meet the demands of high-frequency inference, our model\
    \ employs a sparse MoE backbone, expanding model capacity without compromising\
    \ efficiency. (4) Real-time closed-loop control is realized through an enhanced\
    \ asynchronous inference scheme, which predicts future latents in parallel with\
    \ action execution while re-grounding each rollout on the latest observation via\
    \ learned forward dynamics. Real-world deployment validates LingBot-VA 2.0 as\
    \ a robust foundation model, as evidenced by its few-shot generalization across\
    \ complex manipulation tasks."
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
- native_video_action_pretrainin
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-11'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: Native Video-Action Pretraining for Generalizable Robot Control (arXiv)
  url: https://arxiv.org/abs/2607.08639
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2607.08639v1 Announce Type: new 
Abstract: The advent of video-action models offers a promising path for robot control. Nevertheless, we argue that repurposing video generative models designed for digital content creation is inherently inadequate for physical environments. To bridge this gap, we present LingBot-VA 2.0, a video-action foundation model built from the ground up for embodiment. Four core design principles showcase its evolution from LingBot-VA. (1) Departing from traditional reconstruction-focused VAEs, we introduce a semantic visual-action tokenizer, which aligns visual representations with both semantics and actions, improving instruction following and action precision in subsequent policy learning. (2) Given the strictly causal nature of temporal dynamics, we adopt a causal pretraining paradigm, training from scratch to circumvent the catastrophic forgetting that frequently occurs when adapting bidirectional architectures. (3) To meet the demands of high-frequency inference, our model employs a sparse MoE backbone, expanding model capacity without compromising efficiency. (4) Real-time closed-loop control is realized through an enhanced asynchronous inference scheme, which predicts future latents in parallel with action execution while re-grounding each rollout on the latest observation via learned forward dynamics. Real-world deployment validates LingBot-VA 2.0 as a robust foundation model, as evidenced by its few-shot generalization across complex manipulation tasks.
