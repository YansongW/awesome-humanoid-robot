---
$id: ent_paper_zhu_unified_world_models_coupling_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets'
  zh: UWM
  ko: 'Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets'
summary:
  en: 'Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (UWM), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Paul G. Allen School of Computer Science and
    Engineering, University of Washington, Toyota Research Institute, and published at RSS26.'
  zh: 'Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (UWM), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Paul G. Allen School of Computer Science and
    Engineering, University of Washington, Toyota Research Institute, and published at RSS26.'
  ko: 'Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (UWM), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Paul G. Allen School of Computer Science and
    Engineering, University of Washington, Toyota Research Institute, and published at RSS26.'
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
- uwm
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.02792v3.
sources:
- id: src_001
  type: paper
  title: 'Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (arXiv)'
  url: https://arxiv.org/abs/2504.02792
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UWM source
  url: https://doi.org/10.48550/arXiv.2504.02792
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning has emerged as a promising approach towards building generalist robots. However, scaling imitation learning for large robot foundation models remains challenging due to its reliance on high-quality expert demonstrations. Meanwhile, large amounts of video data depicting a wide range of environments and diverse behaviors are readily available. This data provides a rich source of information about real-world dynamics and agent-environment interactions. Leveraging this data directly for imitation learning, however, has proven difficult due to the lack of action annotation. In this work, we present Unified World Models (UWM), a framework that allows for leveraging both video and action data for policy learning. Specifically, a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality. By controlling each diffusion timestep, UWM can flexibly represent a policy, a forward dynamics, an inverse dynamics, and a video generator. Through simulated and real-world experiments, we show that: (1) UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable and robust policies than imitation learning, (2) UWM naturally facilitates learning from action-free video data through independent control of modality-specific diffusion timesteps, further improving the performance of finetuned policies. Our results suggest that UWM offers a promising step toward harnessing large, heterogeneous datasets for scalable robot learning, and provides a simple unification between the often disparate paradigms of imitation learning and world modeling. Videos and code are available at https://weirdlabuw.github.io/uwm/.

## 核心内容
Imitation learning has emerged as a promising approach towards building generalist robots. However, scaling imitation learning for large robot foundation models remains challenging due to its reliance on high-quality expert demonstrations. Meanwhile, large amounts of video data depicting a wide range of environments and diverse behaviors are readily available. This data provides a rich source of information about real-world dynamics and agent-environment interactions. Leveraging this data directly for imitation learning, however, has proven difficult due to the lack of action annotation. In this work, we present Unified World Models (UWM), a framework that allows for leveraging both video and action data for policy learning. Specifically, a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality. By controlling each diffusion timestep, UWM can flexibly represent a policy, a forward dynamics, an inverse dynamics, and a video generator. Through simulated and real-world experiments, we show that: (1) UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable and robust policies than imitation learning, (2) UWM naturally facilitates learning from action-free video data through independent control of modality-specific diffusion timesteps, further improving the performance of finetuned policies. Our results suggest that UWM offers a promising step toward harnessing large, heterogeneous datasets for scalable robot learning, and provides a simple unification between the often disparate paradigms of imitation learning and world modeling. Videos and code are available at https://weirdlabuw.github.io/uwm/.

## 参考
- http://arxiv.org/abs/2504.02792v3

