---
$id: ent_paper_cola_flow_policy_temporally_co_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoLA-Flow Policy: Temporally Coherent Imitation Learning via Continuous Latent
    Action Flow Matching for Robotic Manipulation'
  zh: 'CoLA-Flow Policy: Temporally Coherent Imitation Learning via Continuous Latent
    Action Flow Matching for Robotic Manipulation'
  ko: ''
summary:
  en: "arXiv:2601.23087v5 Announce Type: replace \nAbstract: Learning long-horizon\
    \ robotic manipulation requires jointly achieving expressive behavior modeling,\
    \ real-time inference, and stable execution, which remains challenging for existing\
    \ generative policies. Diffusion-based approaches offer strong modeling capacity\
    \ but incur high inference latency, while flow matching enables fast, near-single-step\
    \ generation yet often suffers from unstable execution when operating directly\
    \ in the raw action space. We propose Continuous Latent Action Flow Policy (CoLA-Flow\
    \ Policy), a trajectory-level imitation learning framework that performs flow\
    \ matching in a continuous latent action space. By encoding action sequences into\
    \ temporally coherent latent trajectories and learning an explicit latent-space\
    \ flow, CoLA-Flow Policy decouples global motion structure from low-level control\
    \ noise, enabling smooth and reliable long-horizon execution. The framework further\
    \ integrates geometry-aware point cloud conditioning and execution-time multimodal\
    \ modulation, using visual cues as a representative modality to enhance real-world\
    \ robustness. Experiments in simulation and on real robots show that CoLA-Flow\
    \ Policy achieves near-single-step inference, improves trajectory smoothness by\
    \ up to 93.7% and task success by up to 25 percentage points over raw action-space\
    \ flow baselines, while remaining significantly faster than diffusion-based policies."
  zh: "arXiv:2601.23087v5 Announce Type: replace \nAbstract: Learning long-horizon\
    \ robotic manipulation requires jointly achieving expressive behavior modeling,\
    \ real-time inference, and stable execution, which remains challenging for existing\
    \ generative policies. Diffusion-based approaches offer strong modeling capacity\
    \ but incur high inference latency, while flow matching enables fast, near-single-step\
    \ generation yet often suffers from unstable execution when operating directly\
    \ in the raw action space. We propose Continuous Latent Action Flow Policy (CoLA-Flow\
    \ Policy), a trajectory-level imitation learning framework that performs flow\
    \ matching in a continuous latent action space. By encoding action sequences into\
    \ temporally coherent latent trajectories and learning an explicit latent-space\
    \ flow, CoLA-Flow Policy decouples global motion structure from low-level control\
    \ noise, enabling smooth and reliable long-horizon execution. The framework further\
    \ integrates geometry-aware point cloud conditioning and execution-time multimodal\
    \ modulation, using visual cues as a representative modality to enhance real-world\
    \ robustness. Experiments in simulation and on real robots show that CoLA-Flow\
    \ Policy achieves near-single-step inference, improves trajectory smoothness by\
    \ up to 93.7% and task success by up to 25 percentage points over raw action-space\
    \ flow baselines, while remaining significantly faster than diffusion-based policies."
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
- cola_flow_policy
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
  title: 'CoLA-Flow Policy: Temporally Coherent Imitation Learning via Continuous
    Latent Action Flow Matching for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2601.23087
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2601.23087v5 Announce Type: replace 
Abstract: Learning long-horizon robotic manipulation requires jointly achieving expressive behavior modeling, real-time inference, and stable execution, which remains challenging for existing generative policies. Diffusion-based approaches offer strong modeling capacity but incur high inference latency, while flow matching enables fast, near-single-step generation yet often suffers from unstable execution when operating directly in the raw action space. We propose Continuous Latent Action Flow Policy (CoLA-Flow Policy), a trajectory-level imitation learning framework that performs flow matching in a continuous latent action space. By encoding action sequences into temporally coherent latent trajectories and learning an explicit latent-space flow, CoLA-Flow Policy decouples global motion structure from low-level control noise, enabling smooth and reliable long-horizon execution. The framework further integrates geometry-aware point cloud conditioning and execution-time multimodal modulation, using visual cues as a representative modality to enhance real-world robustness. Experiments in simulation and on real robots show that CoLA-Flow Policy achieves near-single-step inference, improves trajectory smoothness by up to 93.7% and task success by up to 25 percentage points over raw action-space flow baselines, while remaining significantly faster than diffusion-based policies.
