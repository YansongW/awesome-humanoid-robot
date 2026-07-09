---
$id: ent_paper_xs_vla_coupling_coarse_grained_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'XS-VLA: Coupling Coarse-grained Spatial Distillation with Latent Flow Matching
    for Lightweight Robotic Control'
  zh: 'XS-VLA: Coupling Coarse-grained Spatial Distillation with Latent Flow Matching
    for Lightweight Robotic Control'
  ko: ''
summary:
  en: "arXiv:2607.04171v1 Announce Type: new \nAbstract: Large Vision-Language Models\
    \ (LVLMs) have shown strong multimodal understanding and spatial grounding, but\
    \ their computational cost limits real-time robotic control. In contrast, lightweight\
    \ models are suitable for edge deployment but often suffer from \"spatial blindness\"\
    , namely weak native spatial prediction ability. Training Vision-Language-Action\
    \ (VLA) models on mixed human demonstrations can also degrade policy performance\
    \ due to highly diverse behaviors. To address these limitations, we propose XS-VLA,\
    \ a two-stage framework for efficient and spatially grounded robotic manipulation.\
    \ First, we distill spatial semantic knowledge from Qwen3-VL-4B into the SmolVLM2-0.25B\
    \ backbone by fine-tuning on curated coarse-grained spatial descriptions, turning\
    \ the lightweight model into a spatially grounded engine. Second, we use this\
    \ enhanced backbone to condition a Latent Flow Matching policy. Unlike deterministic\
    \ controllers, our policy combines a Conditional Variational Autoencoder (CVAE)\
    \ with Flow Matching dynamics to model complex multimodal action distributions.\
    \ On the LIBERO benchmark, XS-VLA achieves state-of-the-art performance among\
    \ models with fewer than 0.5B parameters. It improves average success rates by\
    \ up to 7.2 percent, including a 23 percent gain on LIBERO-Long, over the SmolVLA\
    \ 0.25B baseline, and outperforms the larger 2.2B vanilla SmolVLA. Ablations show\
    \ that spatial tuning and generative latent flow control substantially improve\
    \ lightweight VLA performance, delivering a 3.2 times speedup in mission execution\
    \ over the previous lightweight flow matching policy."
  zh: "arXiv:2607.04171v1 Announce Type: new \nAbstract: Large Vision-Language Models\
    \ (LVLMs) have shown strong multimodal understanding and spatial grounding, but\
    \ their computational cost limits real-time robotic control. In contrast, lightweight\
    \ models are suitable for edge deployment but often suffer from \"spatial blindness\"\
    , namely weak native spatial prediction ability. Training Vision-Language-Action\
    \ (VLA) models on mixed human demonstrations can also degrade policy performance\
    \ due to highly diverse behaviors. To address these limitations, we propose XS-VLA,\
    \ a two-stage framework for efficient and spatially grounded robotic manipulation.\
    \ First, we distill spatial semantic knowledge from Qwen3-VL-4B into the SmolVLM2-0.25B\
    \ backbone by fine-tuning on curated coarse-grained spatial descriptions, turning\
    \ the lightweight model into a spatially grounded engine. Second, we use this\
    \ enhanced backbone to condition a Latent Flow Matching policy. Unlike deterministic\
    \ controllers, our policy combines a Conditional Variational Autoencoder (CVAE)\
    \ with Flow Matching dynamics to model complex multimodal action distributions.\
    \ On the LIBERO benchmark, XS-VLA achieves state-of-the-art performance among\
    \ models with fewer than 0.5B parameters. It improves average success rates by\
    \ up to 7.2 percent, including a 23 percent gain on LIBERO-Long, over the SmolVLA\
    \ 0.25B baseline, and outperforms the larger 2.2B vanilla SmolVLA. Ablations show\
    \ that spatial tuning and generative latent flow control substantially improve\
    \ lightweight VLA performance, delivering a 3.2 times speedup in mission execution\
    \ over the previous lightweight flow matching policy."
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
- xs_vla
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
  title: 'XS-VLA: Coupling Coarse-grained Spatial Distillation with Latent Flow Matching
    for Lightweight Robotic Control (arXiv)'
  url: https://arxiv.org/abs/2607.04171
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2607.04171v1 Announce Type: new 
Abstract: Large Vision-Language Models (LVLMs) have shown strong multimodal understanding and spatial grounding, but their computational cost limits real-time robotic control. In contrast, lightweight models are suitable for edge deployment but often suffer from "spatial blindness", namely weak native spatial prediction ability. Training Vision-Language-Action (VLA) models on mixed human demonstrations can also degrade policy performance due to highly diverse behaviors. To address these limitations, we propose XS-VLA, a two-stage framework for efficient and spatially grounded robotic manipulation. First, we distill spatial semantic knowledge from Qwen3-VL-4B into the SmolVLM2-0.25B backbone by fine-tuning on curated coarse-grained spatial descriptions, turning the lightweight model into a spatially grounded engine. Second, we use this enhanced backbone to condition a Latent Flow Matching policy. Unlike deterministic controllers, our policy combines a Conditional Variational Autoencoder (CVAE) with Flow Matching dynamics to model complex multimodal action distributions. On the LIBERO benchmark, XS-VLA achieves state-of-the-art performance among models with fewer than 0.5B parameters. It improves average success rates by up to 7.2 percent, including a 23 percent gain on LIBERO-Long, over the SmolVLA 0.25B baseline, and outperforms the larger 2.2B vanilla SmolVLA. Ablations show that spatial tuning and generative latent flow control substantially improve lightweight VLA performance, delivering a 3.2 times speedup in mission execution over the previous lightweight flow matching policy.
