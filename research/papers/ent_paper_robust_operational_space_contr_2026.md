---
$id: ent_paper_robust_operational_space_contr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robust Operational Space Control with Conformal Disturbance Bounds for Safe
    Redundant Manipulation
  zh: Robust Operational Space Control with Conformal Disturbance Bounds for Safe
    Redundant Manipulation
  ko: Robust Operational Space Control with Conformal Disturbance Bounds for Safe
    Redundant Manipulation
summary:
  en: "arXiv:2607.00424v1 Announce Type: new \nAbstract: Redundant robotic manipulators\
    \ operating in constrained and human-interactive environments require accurate\
    \ task-space tracking together with rigorous safety guarantees under dynamic uncertainties.\
    \ Classical operational space computed torque controller (OSCTC) relies on accurate\
    \ dynamic models and degrades in the presence of disturbances. In contrast, the\
    \ data-driven paradigm of residual learning approximates disturbances as functions\
    \ learned from full-state measurements, which are often noisy in practice, lack\
    \ rigorous theoretical guarantees, and introduce additional design complexity.\
    \ This paper proposes a robust OSCTC framework that integrates an extended state\
    \ observer (ESO) with conformal prediction to combine model-based robustness and\
    \ data-driven adaptability. The ESO estimates lumped disturbances directly in\
    \ operational space without requiring full-state measurements as in residual learning,\
    \ and a robust control barrier function (CBF) is constructed to enforce safety\
    \ under uncertainty. However, robust CBFs require a known disturbance-variation\
    \ bound to guarantee absolute safety, which often leads to conservatism in practice.\
    \ To address this limitation, we further employ a sliding-window conformal prediction\
    \ mechanism to estimate the bound online in a distribution-free manner, thereby\
    \ achieving practical probabilistic safety guarantees. Experiments on a 7-DoF\
    \ Franka Research 3 manipulator demonstrate millimeter-level tracking accuracy\
    \ and real-time safe control at 1~kHz under various disturbances."
  zh: "arXiv:2607.00424v1 Announce Type: new \nAbstract: Redundant robotic manipulators\
    \ operating in constrained and human-interactive environments require accurate\
    \ task-space tracking together with rigorous safety guarantees under dynamic uncertainties.\
    \ Classical operational space computed torque controller (OSCTC) relies on accurate\
    \ dynamic models and degrades in the presence of disturbances. In contrast, the\
    \ data-driven paradigm of residual learning approximates disturbances as functions\
    \ learned from full-state measurements, which are often noisy in practice, lack\
    \ rigorous theoretical guarantees, and introduce additional design complexity.\
    \ This paper proposes a robust OSCTC framework that integrates an extended state\
    \ observer (ESO) with conformal prediction to combine model-based robustness and\
    \ data-driven adaptability. The ESO estimates lumped disturbances directly in\
    \ operational space without requiring full-state measurements as in residual learning,\
    \ and a robust control barrier function (CBF) is constructed to enforce safety\
    \ under uncertainty. However, robust CBFs require a known disturbance-variation\
    \ bound to guarantee absolute safety, which often leads to conservatism in practice.\
    \ To address this limitation, we further employ a sliding-window conformal prediction\
    \ mechanism to estimate the bound online in a distribution-free manner, thereby\
    \ achieving practical probabilistic safety guarantees. Experiments on a 7-DoF\
    \ Franka Research 3 manipulator demonstrate millimeter-level tracking accuracy\
    \ and real-time safe control at 1~kHz under various disturbances."
  ko: "arXiv:2607.00424v1 Announce Type: new \nAbstract: Redundant robotic manipulators\
    \ operating in constrained and human-interactive environments require accurate\
    \ task-space tracking together with rigorous safety guarantees under dynamic uncertainties.\
    \ Classical operational space computed torque controller (OSCTC) relies on accurate\
    \ dynamic models and degrades in the presence of disturbances. In contrast, the\
    \ data-driven paradigm of residual learning approximates disturbances as functions\
    \ learned from full-state measurements, which are often noisy in practice, lack\
    \ rigorous theoretical guarantees, and introduce additional design complexity.\
    \ This paper proposes a robust OSCTC framework that integrates an extended state\
    \ observer (ESO) with conformal prediction to combine model-based robustness and\
    \ data-driven adaptability. The ESO estimates lumped disturbances directly in\
    \ operational space without requiring full-state measurements as in residual learning,\
    \ and a robust control barrier function (CBF) is constructed to enforce safety\
    \ under uncertainty. However, robust CBFs require a known disturbance-variation\
    \ bound to guarantee absolute safety, which often leads to conservatism in practice.\
    \ To address this limitation, we further employ a sliding-window conformal prediction\
    \ mechanism to estimate the bound online in a distribution-free manner, thereby\
    \ achieving practical probabilistic safety guarantees. Experiments on a 7-DoF\
    \ Franka Research 3 manipulator demonstrate millimeter-level tracking accuracy\
    \ and real-time safe control at 1~kHz under various disturbances."
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
- robust_operational_space_contr
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-03'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: Robust Operational Space Control with Conformal Disturbance Bounds for Safe
    Redundant Manipulation (arXiv)
  url: https://arxiv.org/abs/2607.00424
  date: '2026'
  accessed_at: '2026-07-03'
---

## 概述
arXiv:2607.00424v1 Announce Type: new 
Abstract: Redundant robotic manipulators operating in constrained and human-interactive environments require accurate task-space tracking together with rigorous safety guarantees under dynamic uncertainties. Classical operational space computed torque controller (OSCTC) relies on accurate dynamic models and degrades in the presence of disturbances. In contrast, the data-driven paradigm of residual learning approximates disturbances as functions learned from full-state measurements, which are often noisy in practice, lack rigorous theoretical guarantees, and introduce additional design complexity. This paper proposes a robust OSCTC framework that integrates an extended state observer (ESO) with conformal prediction to combine model-based robustness and data-driven adaptability. The ESO estimates lumped disturbances directly in operational space without requiring full-state measurements as in residual learning, and a robust control barrier function (CBF) is constructed to enforce safety under uncertainty. However, robust CBFs require a known disturbance-variation bound to guarantee absolute safety, which often leads to conservatism in practice. To address this limitation, we further employ a sliding-window conformal prediction mechanism to estimate the bound online in a distribution-free manner, thereby achieving practical probabilistic safety guarantees. Experiments on a 7-DoF Franka Research 3 manipulator demonstrate millimeter-level tracking accuracy and real-time safe control at 1~kHz under various disturbances.

## Overview
arXiv:2607.00424v1 Announce Type: new 
Abstract: Redundant robotic manipulators operating in constrained and human-interactive environments require accurate task-space tracking together with rigorous safety guarantees under dynamic uncertainties. Classical operational space computed torque controller (OSCTC) relies on accurate dynamic models and degrades in the presence of disturbances. In contrast, the data-driven paradigm of residual learning approximates disturbances as functions learned from full-state measurements, which are often noisy in practice, lack rigorous theoretical guarantees, and introduce additional design complexity. This paper proposes a robust OSCTC framework that integrates an extended state observer (ESO) with conformal prediction to combine model-based robustness and data-driven adaptability. The ESO estimates lumped disturbances directly in operational space without requiring full-state measurements as in residual learning, and a robust control barrier function (CBF) is constructed to enforce safety under uncertainty. However, robust CBFs require a known disturbance-variation bound to guarantee absolute safety, which often leads to conservatism in practice. To address this limitation, we further employ a sliding-window conformal prediction mechanism to estimate the bound online in a distribution-free manner, thereby achieving practical probabilistic safety guarantees. Experiments on a 7-DoF Franka Research 3 manipulator demonstrate millimeter-level tracking accuracy and real-time safe control at 1~kHz under various disturbances.

## 개요
arXiv:2607.00424v1 Announce Type: new 
Abstract: Redundant robotic manipulators operating in constrained and human-interactive environments require accurate task-space tracking together with rigorous safety guarantees under dynamic uncertainties. Classical operational space computed torque controller (OSCTC) relies on accurate dynamic models and degrades in the presence of disturbances. In contrast, the data-driven paradigm of residual learning approximates disturbances as functions learned from full-state measurements, which are often noisy in practice, lack rigorous theoretical guarantees, and introduce additional design complexity. This paper proposes a robust OSCTC framework that integrates an extended state observer (ESO) with conformal prediction to combine model-based robustness and data-driven adaptability. The ESO estimates lumped disturbances directly in operational space without requiring full-state measurements as in residual learning, and a robust control barrier function (CBF) is constructed to enforce safety under uncertainty. However, robust CBFs require a known disturbance-variation bound to guarantee absolute safety, which often leads to conservatism in practice. To address this limitation, we further employ a sliding-window conformal prediction mechanism to estimate the bound online in a distribution-free manner, thereby achieving practical probabilistic safety guarantees. Experiments on a 7-DoF Franka Research 3 manipulator demonstrate millimeter-level tracking accuracy and real-time safe control at 1~kHz under various disturbances.
