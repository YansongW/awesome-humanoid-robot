---
$id: ent_paper_motion_planning_in_compressed_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Motion Planning in Compressed Representation Spaces
  zh: Motion Planning in Compressed Representation Spaces
  ko: ''
summary:
  en: "arXiv:2606.30940v1 Announce Type: new \nAbstract: Deep learning methods have\
    \ vastly expanded the capabilities of motion planning in robotics applications,\
    \ as learning priors from large-scale data has been shown to be essential in capturing\
    \ the highly complex behavior required for solving tasks such as manipulation\
    \ or navigation for autonomous vehicles. At the same time, model-based planning\
    \ algorithms based on search or optimization remain an essential tool due to their\
    \ flexibility, efficiency, and the ability to incorporate domain knowledge via\
    \ expert-designed algorithms and objective functions. We propose a new generative\
    \ framework to unify these two paradigms. First, we learn an autoencoder with\
    \ a high compression ratio and a latent space of hierarchically ordered, discrete-valued\
    \ tokens. Leveraging both the dimensionality reduction and the hierarchical coarse-to-fine\
    \ structure learned by this autoencoder, we then perform motion planning by directly\
    \ searching in the latent space of tokens. This search can optimize arbitrary\
    \ objective functions specified at test time, providing a large degree of flexibility\
    \ while maintaining efficiency and producing realistic solutions by relying on\
    \ the generative capabilities of the highly compressed autoencoder. We evaluate\
    \ our method on nuPlan and the Waymo Open Motion Dataset, showing how latent space\
    \ search can be used for a variety of guided behavior generation tasks, achieving\
    \ strong performance for closed-loop motion planning and multi-agent guided scenario\
    \ synthesis without requiring any task-specific training."
  zh: "arXiv:2606.30940v1 Announce Type: new \nAbstract: Deep learning methods have\
    \ vastly expanded the capabilities of motion planning in robotics applications,\
    \ as learning priors from large-scale data has been shown to be essential in capturing\
    \ the highly complex behavior required for solving tasks such as manipulation\
    \ or navigation for autonomous vehicles. At the same time, model-based planning\
    \ algorithms based on search or optimization remain an essential tool due to their\
    \ flexibility, efficiency, and the ability to incorporate domain knowledge via\
    \ expert-designed algorithms and objective functions. We propose a new generative\
    \ framework to unify these two paradigms. First, we learn an autoencoder with\
    \ a high compression ratio and a latent space of hierarchically ordered, discrete-valued\
    \ tokens. Leveraging both the dimensionality reduction and the hierarchical coarse-to-fine\
    \ structure learned by this autoencoder, we then perform motion planning by directly\
    \ searching in the latent space of tokens. This search can optimize arbitrary\
    \ objective functions specified at test time, providing a large degree of flexibility\
    \ while maintaining efficiency and producing realistic solutions by relying on\
    \ the generative capabilities of the highly compressed autoencoder. We evaluate\
    \ our method on nuPlan and the Waymo Open Motion Dataset, showing how latent space\
    \ search can be used for a variety of guided behavior generation tasks, achieving\
    \ strong performance for closed-loop motion planning and multi-agent guided scenario\
    \ synthesis without requiring any task-specific training."
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
- motion_planning_in_compressed
- robotics
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
  title: Motion Planning in Compressed Representation Spaces
  url: https://arxiv.org/abs/2606.30940
  date: '2026'
  accessed_at: '2026-07-01'
---

arXiv:2606.30940v1 Announce Type: new 
Abstract: Deep learning methods have vastly expanded the capabilities of motion planning in robotics applications, as learning priors from large-scale data has been shown to be essential in capturing the highly complex behavior required for solving tasks such as manipulation or navigation for autonomous vehicles. At the same time, model-based planning algorithms based on search or optimization remain an essential tool due to their flexibility, efficiency, and the ability to incorporate domain knowledge via expert-designed algorithms and objective functions. We propose a new generative framework to unify these two paradigms. First, we learn an autoencoder with a high compression ratio and a latent space of hierarchically ordered, discrete-valued tokens. Leveraging both the dimensionality reduction and the hierarchical coarse-to-fine structure learned by this autoencoder, we then perform motion planning by directly searching in the latent space of tokens. This search can optimize arbitrary objective functions specified at test time, providing a large degree of flexibility while maintaining efficiency and producing realistic solutions by relying on the generative capabilities of the highly compressed autoencoder. We evaluate our method on nuPlan and the Waymo Open Motion Dataset, showing how latent space search can be used for a variety of guided behavior generation tasks, achieving strong performance for closed-loop motion planning and multi-agent guided scenario synthesis without requiring any task-specific training.
