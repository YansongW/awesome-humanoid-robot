---
$id: ent_paper_understanding_and_mitigating_t_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Understanding and Mitigating the Video-Action Generalization Gap via Temporal
    Ratio
  zh: Understanding and Mitigating the Video-Action Generalization Gap via Temporal
    Ratio
  ko: ''
summary:
  en: "arXiv:2607.08127v1 Announce Type: cross \nAbstract: Generative video foundation\
    \ models exhibit strong compositional priors, yet world-action models (WAMs) and\
    \ video-action models (VAMs) often lose these priors after finetuning on robotic\
    \ action data. We refer to this discrepancy as the video-action generalization\
    \ gap. In this paper, we systematically investigate this gap by evaluating a comprehensive\
    \ design space of VAMs, demonstrating that standard design choices yield no emergent\
    \ explanation pattern. To explain this behavior, we introduce the Temporal Ratio\
    \ (TR), an attention-based measure of how strongly the action head relies on future\
    \ latent rollouts relative to the anchored current frame. TR has two key properties:\
    \ first, a model's structural reliance on future-predictive latents, measured\
    \ via TR, acts as a predictor of its compositional generalization capacity; second,\
    \ it natively fluctuates based on task phase, shifting attention to future frames\
    \ during planning and reverting to the present frame for precise manipulation.\
    \ Finally, based on these findings, we propose an inference-time adaptive guidance\
    \ method, which exploits this intrinsic feature attention pattern to dynamically\
    \ amplify compositional video conditioning signals precisely when the policy relies\
    \ on future rollouts. Evaluated on the LIBERO benchmark and real-world tasks,\
    \ our approach mitigates the OOD-ID compositional generalization gap. More details:\
    \ https://umishra.me/temporal-ratio/"
  zh: "arXiv:2607.08127v1 Announce Type: cross \nAbstract: Generative video foundation\
    \ models exhibit strong compositional priors, yet world-action models (WAMs) and\
    \ video-action models (VAMs) often lose these priors after finetuning on robotic\
    \ action data. We refer to this discrepancy as the video-action generalization\
    \ gap. In this paper, we systematically investigate this gap by evaluating a comprehensive\
    \ design space of VAMs, demonstrating that standard design choices yield no emergent\
    \ explanation pattern. To explain this behavior, we introduce the Temporal Ratio\
    \ (TR), an attention-based measure of how strongly the action head relies on future\
    \ latent rollouts relative to the anchored current frame. TR has two key properties:\
    \ first, a model's structural reliance on future-predictive latents, measured\
    \ via TR, acts as a predictor of its compositional generalization capacity; second,\
    \ it natively fluctuates based on task phase, shifting attention to future frames\
    \ during planning and reverting to the present frame for precise manipulation.\
    \ Finally, based on these findings, we propose an inference-time adaptive guidance\
    \ method, which exploits this intrinsic feature attention pattern to dynamically\
    \ amplify compositional video conditioning signals precisely when the policy relies\
    \ on future rollouts. Evaluated on the LIBERO benchmark and real-world tasks,\
    \ our approach mitigates the OOD-ID compositional generalization gap. More details:\
    \ https://umishra.me/temporal-ratio/"
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
- understanding_and_mitigating_t
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
  title: Understanding and Mitigating the Video-Action Generalization Gap via Temporal
    Ratio (arXiv)
  url: https://arxiv.org/abs/2607.08127
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2607.08127v1 Announce Type: cross 
Abstract: Generative video foundation models exhibit strong compositional priors, yet world-action models (WAMs) and video-action models (VAMs) often lose these priors after finetuning on robotic action data. We refer to this discrepancy as the video-action generalization gap. In this paper, we systematically investigate this gap by evaluating a comprehensive design space of VAMs, demonstrating that standard design choices yield no emergent explanation pattern. To explain this behavior, we introduce the Temporal Ratio (TR), an attention-based measure of how strongly the action head relies on future latent rollouts relative to the anchored current frame. TR has two key properties: first, a model's structural reliance on future-predictive latents, measured via TR, acts as a predictor of its compositional generalization capacity; second, it natively fluctuates based on task phase, shifting attention to future frames during planning and reverting to the present frame for precise manipulation. Finally, based on these findings, we propose an inference-time adaptive guidance method, which exploits this intrinsic feature attention pattern to dynamically amplify compositional video conditioning signals precisely when the policy relies on future rollouts. Evaluated on the LIBERO benchmark and real-world tasks, our approach mitigates the OOD-ID compositional generalization gap. More details: https://umishra.me/temporal-ratio/
