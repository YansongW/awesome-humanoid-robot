---
$id: ent_paper_interaction_dynamics_for_dexte_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Interaction Dynamics for Dexterous Manipulation
  zh: Interaction Dynamics for Dexterous Manipulation
  ko: Interaction Dynamics for Dexterous Manipulation
summary:
  en: "arXiv:2606.14606v2 Announce Type: replace \nAbstract: Dexterous manipulation\
    \ is fundamentally a problem of interaction dynamics: the hand must track precise\
    \ finger trajectories, regulate the contact force exchanged with grasped objects,\
    \ respect actuation and safety limits, and remain predictable when contact persists\
    \ -- objectives in tension for any fixed-gain controller. A sustained contact\
    \ torque $\\tau_{\\text{ext}}$ through a joint stiffness $K_d$ produces the structural\
    \ bias $e_\\infty=\\tau_{\\text{ext}}/K_d$, so stiffening for accuracy sacrifices\
    \ contact safety while softening yields by design. We make these interaction dynamics\
    \ explicit and actuator-agnostic through a constant-$A_d$ double-integrator backbone,\
    \ instantiating the offset-free architecture established for physical human-robot\
    \ interaction (pHRI) and preserving its modeling assumptions on the reduced residual\
    \ dynamics. An algebraic feedforward reduces the tendon transmission -- hydraulic,\
    \ cable, pneumatic, twisted-string, or series-elastic -- to a constant-coefficient\
    \ double integrator, so the QP cost inverse is precomputed offline and a 10-step\
    \ receding-horizon QP runs at 500\\,Hz under contact-force (ISO/TS 15066), actuation,\
    \ and jerk constraints. An encoder-only augmented-Kalman disturbance state drives\
    \ steady-state error to zero under constant contact loads in the nominal detectable\
    \ case. In simulation, a hydraulically actuated finger -- the worked example,\
    \ adding pressure and cavitation constraints -- attains 0.6\\,mrad RMS, 0.1\\\
    ,mrad steady-state, and 7.3\\,mrad peak deflection under 1.5\\,Nm contact: 153$\\\
    times$, 1500$\\times$, and 21$\\times$ better than classical impedance. The realized\
    \ first-move stiffness (18$\\to$323\\,Nm/rad with update rate) is independently\
    \ verified, and the architecture scales to a 16-DOF LEAP Hand MuJoCo model, recovering\
    \ from 2.5\\,N grasp disturbances within 0.7\\,s."
  zh: "arXiv:2606.14606v2 Announce Type: replace \nAbstract: Dexterous manipulation\
    \ is fundamentally a problem of interaction dynamics: the hand must track precise\
    \ finger trajectories, regulate the contact force exchanged with grasped objects,\
    \ respect actuation and safety limits, and remain predictable when contact persists\
    \ -- objectives in tension for any fixed-gain controller. A sustained contact\
    \ torque $\\tau_{\\text{ext}}$ through a joint stiffness $K_d$ produces the structural\
    \ bias $e_\\infty=\\tau_{\\text{ext}}/K_d$, so stiffening for accuracy sacrifices\
    \ contact safety while softening yields by design. We make these interaction dynamics\
    \ explicit and actuator-agnostic through a constant-$A_d$ double-integrator backbone,\
    \ instantiating the offset-free architecture established for physical human-robot\
    \ interaction (pHRI) and preserving its modeling assumptions on the reduced residual\
    \ dynamics. An algebraic feedforward reduces the tendon transmission -- hydraulic,\
    \ cable, pneumatic, twisted-string, or series-elastic -- to a constant-coefficient\
    \ double integrator, so the QP cost inverse is precomputed offline and a 10-step\
    \ receding-horizon QP runs at 500\\,Hz under contact-force (ISO/TS 15066), actuation,\
    \ and jerk constraints. An encoder-only augmented-Kalman disturbance state drives\
    \ steady-state error to zero under constant contact loads in the nominal detectable\
    \ case. In simulation, a hydraulically actuated finger -- the worked example,\
    \ adding pressure and cavitation constraints -- attains 0.6\\,mrad RMS, 0.1\\\
    ,mrad steady-state, and 7.3\\,mrad peak deflection under 1.5\\,Nm contact: 153$\\\
    times$, 1500$\\times$, and 21$\\times$ better than classical impedance. The realized\
    \ first-move stiffness (18$\\to$323\\,Nm/rad with update rate) is independently\
    \ verified, and the architecture scales to a 16-DOF LEAP Hand MuJoCo model, recovering\
    \ from 2.5\\,N grasp disturbances within 0.7\\,s."
  ko: "arXiv:2606.14606v2 Announce Type: replace \nAbstract: Dexterous manipulation\
    \ is fundamentally a problem of interaction dynamics: the hand must track precise\
    \ finger trajectories, regulate the contact force exchanged with grasped objects,\
    \ respect actuation and safety limits, and remain predictable when contact persists\
    \ -- objectives in tension for any fixed-gain controller. A sustained contact\
    \ torque $\\tau_{\\text{ext}}$ through a joint stiffness $K_d$ produces the structural\
    \ bias $e_\\infty=\\tau_{\\text{ext}}/K_d$, so stiffening for accuracy sacrifices\
    \ contact safety while softening yields by design. We make these interaction dynamics\
    \ explicit and actuator-agnostic through a constant-$A_d$ double-integrator backbone,\
    \ instantiating the offset-free architecture established for physical human-robot\
    \ interaction (pHRI) and preserving its modeling assumptions on the reduced residual\
    \ dynamics. An algebraic feedforward reduces the tendon transmission -- hydraulic,\
    \ cable, pneumatic, twisted-string, or series-elastic -- to a constant-coefficient\
    \ double integrator, so the QP cost inverse is precomputed offline and a 10-step\
    \ receding-horizon QP runs at 500\\,Hz under contact-force (ISO/TS 15066), actuation,\
    \ and jerk constraints. An encoder-only augmented-Kalman disturbance state drives\
    \ steady-state error to zero under constant contact loads in the nominal detectable\
    \ case. In simulation, a hydraulically actuated finger -- the worked example,\
    \ adding pressure and cavitation constraints -- attains 0.6\\,mrad RMS, 0.1\\\
    ,mrad steady-state, and 7.3\\,mrad peak deflection under 1.5\\,Nm contact: 153$\\\
    times$, 1500$\\times$, and 21$\\times$ better than classical impedance. The realized\
    \ first-move stiffness (18$\\to$323\\,Nm/rad with update rate) is independently\
    \ verified, and the architecture scales to a 16-DOF LEAP Hand MuJoCo model, recovering\
    \ from 2.5\\,N grasp disturbances within 0.7\\,s."
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
- interaction_dynamics_for_dexte
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
  title: Interaction Dynamics for Dexterous Manipulation (arXiv)
  url: https://arxiv.org/abs/2606.14606
  date: '2026'
  accessed_at: '2026-07-08'
---

## 概述
arXiv:2606.14606v2 Announce Type: replace 
Abstract: Dexterous manipulation is fundamentally a problem of interaction dynamics: the hand must track precise finger trajectories, regulate the contact force exchanged with grasped objects, respect actuation and safety limits, and remain predictable when contact persists -- objectives in tension for any fixed-gain controller. A sustained contact torque $\tau_{\text{ext}}$ through a joint stiffness $K_d$ produces the structural bias $e_\infty=\tau_{\text{ext}}/K_d$, so stiffening for accuracy sacrifices contact safety while softening yields by design. We make these interaction dynamics explicit and actuator-agnostic through a constant-$A_d$ double-integrator backbone, instantiating the offset-free architecture established for physical human-robot interaction (pHRI) and preserving its modeling assumptions on the reduced residual dynamics. An algebraic feedforward reduces the tendon transmission -- hydraulic, cable, pneumatic, twisted-string, or series-elastic -- to a constant-coefficient double integrator, so the QP cost inverse is precomputed offline and a 10-step receding-horizon QP runs at 500\,Hz under contact-force (ISO/TS 15066), actuation, and jerk constraints. An encoder-only augmented-Kalman disturbance state drives steady-state error to zero under constant contact loads in the nominal detectable case. In simulation, a hydraulically actuated finger -- the worked example, adding pressure and cavitation constraints -- attains 0.6\,mrad RMS, 0.1\,mrad steady-state, and 7.3\,mrad peak deflection under 1.5\,Nm contact: 153$\times$, 1500$\times$, and 21$\times$ better than classical impedance. The realized first-move stiffness (18$\to$323\,Nm/rad with update rate) is independently verified, and the architecture scales to a 16-DOF LEAP Hand MuJoCo model, recovering from 2.5\,N grasp disturbances within 0.7\,s.

## Overview
arXiv:2606.14606v2 Announce Type: replace 
Abstract: Dexterous manipulation is fundamentally a problem of interaction dynamics: the hand must track precise finger trajectories, regulate the contact force exchanged with grasped objects, respect actuation and safety limits, and remain predictable when contact persists -- objectives in tension for any fixed-gain controller. A sustained contact torque $\tau_{\text{ext}}$ through a joint stiffness $K_d$ produces the structural bias $e_\infty=\tau_{\text{ext}}/K_d$, so stiffening for accuracy sacrifices contact safety while softening yields by design. We make these interaction dynamics explicit and actuator-agnostic through a constant-$A_d$ double-integrator backbone, instantiating the offset-free architecture established for physical human-robot interaction (pHRI) and preserving its modeling assumptions on the reduced residual dynamics. An algebraic feedforward reduces the tendon transmission -- hydraulic, cable, pneumatic, twisted-string, or series-elastic -- to a constant-coefficient double integrator, so the QP cost inverse is precomputed offline and a 10-step receding-horizon QP runs at 500\,Hz under contact-force (ISO/TS 15066), actuation, and jerk constraints. An encoder-only augmented-Kalman disturbance state drives steady-state error to zero under constant contact loads in the nominal detectable case. In simulation, a hydraulically actuated finger -- the worked example, adding pressure and cavitation constraints -- attains 0.6\,mrad RMS, 0.1\,mrad steady-state, and 7.3\,mrad peak deflection under 1.5\,Nm contact: 153$\times$, 1500$\times$, and 21$\times$ better than classical impedance. The realized first-move stiffness (18$\to$323\,Nm/rad with update rate) is independently verified, and the architecture scales to a 16-DOF LEAP Hand MuJoCo model, recovering from 2.5\,N grasp disturbances within 0.7\,s.

## 개요
arXiv:2606.14606v2 Announce Type: replace 
Abstract: Dexterous manipulation is fundamentally a problem of interaction dynamics: the hand must track precise finger trajectories, regulate the contact force exchanged with grasped objects, respect actuation and safety limits, and remain predictable when contact persists -- objectives in tension for any fixed-gain controller. A sustained contact torque $\tau_{\text{ext}}$ through a joint stiffness $K_d$ produces the structural bias $e_\infty=\tau_{\text{ext}}/K_d$, so stiffening for accuracy sacrifices contact safety while softening yields by design. We make these interaction dynamics explicit and actuator-agnostic through a constant-$A_d$ double-integrator backbone, instantiating the offset-free architecture established for physical human-robot interaction (pHRI) and preserving its modeling assumptions on the reduced residual dynamics. An algebraic feedforward reduces the tendon transmission -- hydraulic, cable, pneumatic, twisted-string, or series-elastic -- to a constant-coefficient double integrator, so the QP cost inverse is precomputed offline and a 10-step receding-horizon QP runs at 500\,Hz under contact-force (ISO/TS 15066), actuation, and jerk constraints. An encoder-only augmented-Kalman disturbance state drives steady-state error to zero under constant contact loads in the nominal detectable case. In simulation, a hydraulically actuated finger -- the worked example, adding pressure and cavitation constraints -- attains 0.6\,mrad RMS, 0.1\,mrad steady-state, and 7.3\,mrad peak deflection under 1.5\,Nm contact: 153$\times$, 1500$\times$, and 21$\times$ better than classical impedance. The realized first-move stiffness (18$\to$323\,Nm/rad with update rate) is independently verified, and the architecture scales to a 16-DOF LEAP Hand MuJoCo model, recovering from 2.5\,N grasp disturbances within 0.7\,s.
