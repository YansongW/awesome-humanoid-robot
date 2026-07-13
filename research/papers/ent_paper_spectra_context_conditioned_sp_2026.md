---
$id: ent_paper_spectra_context_conditioned_sp_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SPECTRA: Context-Conditioned Spectral Movement Primitives for Robot Skill Generalization'
  zh: 'SPECTRA: Context-Conditioned Spectral Movement Primitives for Robot Skill Generalization'
  ko: ''
summary:
  en: "arXiv:2607.06978v1 Announce Type: new \nAbstract: Robot imitation learning\
    \ for manipulation should preserve demonstrated task geometry while producing\
    \ dynamically admissible robot motions. Existing pipelines often learn task-dependent\
    \ trajectories and impose execution limits afterward through filtering, smoothing,\
    \ clipping, or time scaling, which may distort task-critical end-effector paths.\n\
    \  We propose the Spectral Movement Primitive (SMP), a frequency-domain imitation\
    \ learning framework that couples task-space skill generation with joint-space\
    \ execution regulation. Demonstrations are represented by truncated finite-horizon\
    \ Fourier coefficients. An empirically selected low-frequency task band captures\
    \ the dominant motion geometry, while higher harmonics contribute disproportionately\
    \ to derivative growth. A frame-aware context-conditioned GMM/GMR prior predicts\
    \ the task-band coefficients in a canonical task frame, and the resulting Cartesian\
    \ trajectory is mapped to joint space through sequential inverse kinematics. A\
    \ phase-coupled regulator then limits the requested phase progression without\
    \ modifying the spectral coefficients, thereby enforcing joint velocity and acceleration\
    \ limits while preserving the represented path.\n  Experiments evaluate task-band\
    \ reconstruction, robustness to composite demonstration corruption, out-of-distribution\
    \ cross-board generalization, joint-space dynamic admissibility, end-effector\
    \ path preservation, and deployment on a Franka Panda robot. Results show compact\
    \ geometric reconstruction, consistent transfer across unseen task frames, substantial\
    \ reductions in dynamic violations and jerk, and preservation of the intended\
    \ end-effector path during phase regulation."
  zh: "arXiv:2607.06978v1 Announce Type: new \nAbstract: Robot imitation learning\
    \ for manipulation should preserve demonstrated task geometry while producing\
    \ dynamically admissible robot motions. Existing pipelines often learn task-dependent\
    \ trajectories and impose execution limits afterward through filtering, smoothing,\
    \ clipping, or time scaling, which may distort task-critical end-effector paths.\n\
    \  We propose the Spectral Movement Primitive (SMP), a frequency-domain imitation\
    \ learning framework that couples task-space skill generation with joint-space\
    \ execution regulation. Demonstrations are represented by truncated finite-horizon\
    \ Fourier coefficients. An empirically selected low-frequency task band captures\
    \ the dominant motion geometry, while higher harmonics contribute disproportionately\
    \ to derivative growth. A frame-aware context-conditioned GMM/GMR prior predicts\
    \ the task-band coefficients in a canonical task frame, and the resulting Cartesian\
    \ trajectory is mapped to joint space through sequential inverse kinematics. A\
    \ phase-coupled regulator then limits the requested phase progression without\
    \ modifying the spectral coefficients, thereby enforcing joint velocity and acceleration\
    \ limits while preserving the represented path.\n  Experiments evaluate task-band\
    \ reconstruction, robustness to composite demonstration corruption, out-of-distribution\
    \ cross-board generalization, joint-space dynamic admissibility, end-effector\
    \ path preservation, and deployment on a Franka Panda robot. Results show compact\
    \ geometric reconstruction, consistent transfer across unseen task frames, substantial\
    \ reductions in dynamic violations and jerk, and preservation of the intended\
    \ end-effector path during phase regulation."
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
- spectra
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-10'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'SPECTRA: Context-Conditioned Spectral Movement Primitives for Robot Skill
    Generalization (arXiv)'
  url: https://arxiv.org/abs/2607.06978
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2607.06978v1 Announce Type: new 
Abstract: Robot imitation learning for manipulation should preserve demonstrated task geometry while producing dynamically admissible robot motions. Existing pipelines often learn task-dependent trajectories and impose execution limits afterward through filtering, smoothing, clipping, or time scaling, which may distort task-critical end-effector paths.
  We propose the Spectral Movement Primitive (SMP), a frequency-domain imitation learning framework that couples task-space skill generation with joint-space execution regulation. Demonstrations are represented by truncated finite-horizon Fourier coefficients. An empirically selected low-frequency task band captures the dominant motion geometry, while higher harmonics contribute disproportionately to derivative growth. A frame-aware context-conditioned GMM/GMR prior predicts the task-band coefficients in a canonical task frame, and the resulting Cartesian trajectory is mapped to joint space through sequential inverse kinematics. A phase-coupled regulator then limits the requested phase progression without modifying the spectral coefficients, thereby enforcing joint velocity and acceleration limits while preserving the represented path.
  Experiments evaluate task-band reconstruction, robustness to composite demonstration corruption, out-of-distribution cross-board generalization, joint-space dynamic admissibility, end-effector path preservation, and deployment on a Franka Panda robot. Results show compact geometric reconstruction, consistent transfer across unseen task frames, substantial reductions in dynamic violations and jerk, and preservation of the intended end-effector path during phase regulation.
