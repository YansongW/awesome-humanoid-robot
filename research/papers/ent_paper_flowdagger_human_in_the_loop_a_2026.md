---
$id: ent_paper_flowdagger_human_in_the_loop_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent
    Space'
  zh: 'FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent
    Space'
  ko: ''
summary:
  en: "arXiv:2607.08877v1 Announce Type: new \nAbstract: Pretrained generative robot\
    \ policies based on flow matching and diffusion have achieved impressive results\
    \ across a wide range of manipulation tasks. Yet real-world deployments routinely\
    \ expose failure modes outside the pretraining distribution. Closing these gaps\
    \ typically requires large-scale data collection or online reinforcement learning\
    \ on physical hardware, which is impractical for rapid and safe adaptation. We\
    \ present FlowDAgger, a sample- and compute-efficient method for adapting frozen\
    \ generative robot policies from human interventions in latent space. Our key\
    \ idea is action inversion: each human expert action is mapped to the noise that\
    \ would have produced it under the frozen base policy, using reverse-time integration\
    \ followed by local refinement. The resulting inverted noise provides supervision\
    \ for a lightweight latent policy that steers the base model at deployment time,\
    \ enabling rapid skill acquisition while preserving its behavioral priors. We\
    \ evaluate FlowDAgger in simulation and on real-world bimanual and single-arm\
    \ manipulation, adapting both action-head VLAs and world-action models from a\
    \ handful of interventions. FlowDAgger outperforms supervised fine-tuning and\
    \ latent-space RL baselines and preserves pretrained skills on held-out tasks,\
    \ offering a practical path for adapting robot foundation models in the real world.\
    \ Website: https://microsoft.github.io/FlowDAgger"
  zh: "arXiv:2607.08877v1 Announce Type: new \nAbstract: Pretrained generative robot\
    \ policies based on flow matching and diffusion have achieved impressive results\
    \ across a wide range of manipulation tasks. Yet real-world deployments routinely\
    \ expose failure modes outside the pretraining distribution. Closing these gaps\
    \ typically requires large-scale data collection or online reinforcement learning\
    \ on physical hardware, which is impractical for rapid and safe adaptation. We\
    \ present FlowDAgger, a sample- and compute-efficient method for adapting frozen\
    \ generative robot policies from human interventions in latent space. Our key\
    \ idea is action inversion: each human expert action is mapped to the noise that\
    \ would have produced it under the frozen base policy, using reverse-time integration\
    \ followed by local refinement. The resulting inverted noise provides supervision\
    \ for a lightweight latent policy that steers the base model at deployment time,\
    \ enabling rapid skill acquisition while preserving its behavioral priors. We\
    \ evaluate FlowDAgger in simulation and on real-world bimanual and single-arm\
    \ manipulation, adapting both action-head VLAs and world-action models from a\
    \ handful of interventions. FlowDAgger outperforms supervised fine-tuning and\
    \ latent-space RL baselines and preserves pretrained skills on held-out tasks,\
    \ offering a practical path for adapting robot foundation models in the real world.\
    \ Website: https://microsoft.github.io/FlowDAgger"
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
- flowdagger
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-13'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in
    Latent Space (arXiv)'
  url: https://arxiv.org/abs/2607.08877
  date: '2026'
  accessed_at: '2026-07-13'
---

arXiv:2607.08877v1 Announce Type: new 
Abstract: Pretrained generative robot policies based on flow matching and diffusion have achieved impressive results across a wide range of manipulation tasks. Yet real-world deployments routinely expose failure modes outside the pretraining distribution. Closing these gaps typically requires large-scale data collection or online reinforcement learning on physical hardware, which is impractical for rapid and safe adaptation. We present FlowDAgger, a sample- and compute-efficient method for adapting frozen generative robot policies from human interventions in latent space. Our key idea is action inversion: each human expert action is mapped to the noise that would have produced it under the frozen base policy, using reverse-time integration followed by local refinement. The resulting inverted noise provides supervision for a lightweight latent policy that steers the base model at deployment time, enabling rapid skill acquisition while preserving its behavioral priors. We evaluate FlowDAgger in simulation and on real-world bimanual and single-arm manipulation, adapting both action-head VLAs and world-action models from a handful of interventions. FlowDAgger outperforms supervised fine-tuning and latent-space RL baselines and preserves pretrained skills on held-out tasks, offering a practical path for adapting robot foundation models in the real world. Website: https://microsoft.github.io/FlowDAgger
