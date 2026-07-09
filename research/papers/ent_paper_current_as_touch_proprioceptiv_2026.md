---
$id: ent_paper_current_as_touch_proprioceptiv_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation'
  zh: 'Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation'
  ko: ''
summary:
  en: "arXiv:2607.03529v1 Announce Type: new \nAbstract: Compliance is essential for\
    \ dexterous manipulation, yet existing solutions often rely on external tactile\
    \ or force sensors that are costly, fragile, and difficult to deploy on low-cost\
    \ robot hands. We propose a proprioception-driven framework that learns contact-aware\
    \ compliance cues from motor current and joint states. Since motor current is\
    \ closely related to actuator torque, it provides an intrinsic signal for perceiving\
    \ contact force, object resistance, and grasp stability without additional sensing\
    \ hardware. Rather than estimating external wrenches or commanding torque, our\
    \ method predicts a compliance reference position: an ideal joint-position target\
    \ for a standard PD controller whose induced position error generates appropriate\
    \ grasping force. This position-based formulation is compatible with mainstream\
    \ teleoperation and policy-learning pipelines, while enabling the robot to adapt\
    \ interaction forces from real-time proprioceptive feedback. Thus, motor current\
    \ serves not only as a force proxy but also as a learnable proprioceptive contact\
    \ signal for compliance reference prediction. Experiments on multiple dexterous\
    \ hands and contact-rich tasks, including fragile object handling, sustained surface\
    \ contact, thin-object retrieval, and dynamic load adaptation, show stable compliant\
    \ grasping, safer and more efficient teleoperation, and improved downstream policy\
    \ learning without external tactile or force sensors."
  zh: "arXiv:2607.03529v1 Announce Type: new \nAbstract: Compliance is essential for\
    \ dexterous manipulation, yet existing solutions often rely on external tactile\
    \ or force sensors that are costly, fragile, and difficult to deploy on low-cost\
    \ robot hands. We propose a proprioception-driven framework that learns contact-aware\
    \ compliance cues from motor current and joint states. Since motor current is\
    \ closely related to actuator torque, it provides an intrinsic signal for perceiving\
    \ contact force, object resistance, and grasp stability without additional sensing\
    \ hardware. Rather than estimating external wrenches or commanding torque, our\
    \ method predicts a compliance reference position: an ideal joint-position target\
    \ for a standard PD controller whose induced position error generates appropriate\
    \ grasping force. This position-based formulation is compatible with mainstream\
    \ teleoperation and policy-learning pipelines, while enabling the robot to adapt\
    \ interaction forces from real-time proprioceptive feedback. Thus, motor current\
    \ serves not only as a force proxy but also as a learnable proprioceptive contact\
    \ signal for compliance reference prediction. Experiments on multiple dexterous\
    \ hands and contact-rich tasks, including fragile object handling, sustained surface\
    \ contact, thin-object retrieval, and dynamic load adaptation, show stable compliant\
    \ grasping, safer and more efficient teleoperation, and improved downstream policy\
    \ learning without external tactile or force sensors."
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
- current_as_touch
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
  title: 'Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous
    Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.03529
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2607.03529v1 Announce Type: new 
Abstract: Compliance is essential for dexterous manipulation, yet existing solutions often rely on external tactile or force sensors that are costly, fragile, and difficult to deploy on low-cost robot hands. We propose a proprioception-driven framework that learns contact-aware compliance cues from motor current and joint states. Since motor current is closely related to actuator torque, it provides an intrinsic signal for perceiving contact force, object resistance, and grasp stability without additional sensing hardware. Rather than estimating external wrenches or commanding torque, our method predicts a compliance reference position: an ideal joint-position target for a standard PD controller whose induced position error generates appropriate grasping force. This position-based formulation is compatible with mainstream teleoperation and policy-learning pipelines, while enabling the robot to adapt interaction forces from real-time proprioceptive feedback. Thus, motor current serves not only as a force proxy but also as a learnable proprioceptive contact signal for compliance reference prediction. Experiments on multiple dexterous hands and contact-rich tasks, including fragile object handling, sustained surface contact, thin-object retrieval, and dynamic load adaptation, show stable compliant grasping, safer and more efficient teleoperation, and improved downstream policy learning without external tactile or force sensors.
