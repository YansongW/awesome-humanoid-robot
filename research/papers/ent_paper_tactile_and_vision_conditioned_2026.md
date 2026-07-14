---
$id: ent_paper_tactile_and_vision_conditioned_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation
  zh: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation
  ko: ''
summary:
  en: "arXiv:2607.09218v1 Announce Type: new \nAbstract: Whole-arm manipulation involves\
    \ direct contact with the environment while the robot completes a task by distributing\
    \ contact across multiple links as contacts form, slide, and break. This setting\
    \ breaks common implicit assumptions in many learning-based manipulation pipelines:\
    \ arm configuration tightly couples motion and contact forces, contact state is\
    \ partially observed under occlusion, and purely learned rollouts can become physically\
    \ inconsistent under distribution shift because many multi-link contact configurations\
    \ are sparsely represented in the data. To address this, we propose TACTIC (Tactile\
    \ and Vision Conditioned Contact-Centric Control), a receding-horizon controller\
    \ for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive\
    \ model that combines RGB-D, distributed tactile sensing, and a compact 2D proximity\
    \ representation. The model couples a learned, action-conditioned latent dynamics\
    \ model with analytical kinematics through contact Jacobians, enabling rollouts\
    \ of future contact configurations and interaction forces. TACTIC integrates these\
    \ rollouts into a sampling-based MPC planner with contact-aware action sampling:\
    \ contact Jacobian-based projections steer sampled action sequences toward force-modulating\
    \ directions, and objectives defined over predicted proximity and interaction\
    \ forces trade task progress against whole-arm force regulation. We evaluate TACTIC\
    \ in simulation against state-of-the-art model-based and model-free methods, and\
    \ perform ablations that isolate the contribution of each design choice. TACTIC\
    \ consistently outperforms other methods. We further demonstrate real-world performance\
    \ on a robot with distributed tactile sensing across three whole-arm manipulation\
    \ tasks that require multi-contact trajectories: turning over and repositioning\
    \ a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic"
  zh: "arXiv:2607.09218v1 Announce Type: new \nAbstract: Whole-arm manipulation involves\
    \ direct contact with the environment while the robot completes a task by distributing\
    \ contact across multiple links as contacts form, slide, and break. This setting\
    \ breaks common implicit assumptions in many learning-based manipulation pipelines:\
    \ arm configuration tightly couples motion and contact forces, contact state is\
    \ partially observed under occlusion, and purely learned rollouts can become physically\
    \ inconsistent under distribution shift because many multi-link contact configurations\
    \ are sparsely represented in the data. To address this, we propose TACTIC (Tactile\
    \ and Vision Conditioned Contact-Centric Control), a receding-horizon controller\
    \ for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive\
    \ model that combines RGB-D, distributed tactile sensing, and a compact 2D proximity\
    \ representation. The model couples a learned, action-conditioned latent dynamics\
    \ model with analytical kinematics through contact Jacobians, enabling rollouts\
    \ of future contact configurations and interaction forces. TACTIC integrates these\
    \ rollouts into a sampling-based MPC planner with contact-aware action sampling:\
    \ contact Jacobian-based projections steer sampled action sequences toward force-modulating\
    \ directions, and objectives defined over predicted proximity and interaction\
    \ forces trade task progress against whole-arm force regulation. We evaluate TACTIC\
    \ in simulation against state-of-the-art model-based and model-free methods, and\
    \ perform ablations that isolate the contribution of each design choice. TACTIC\
    \ consistently outperforms other methods. We further demonstrate real-world performance\
    \ on a robot with distributed tactile sensing across three whole-arm manipulation\
    \ tasks that require multi-contact trajectories: turning over and repositioning\
    \ a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic"
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
- tactile_and_vision_conditioned
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation
    (arXiv)
  url: https://arxiv.org/abs/2607.09218
  date: '2026'
  accessed_at: '2026-07-14'
---

arXiv:2607.09218v1 Announce Type: new 
Abstract: Whole-arm manipulation involves direct contact with the environment while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories: turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic
