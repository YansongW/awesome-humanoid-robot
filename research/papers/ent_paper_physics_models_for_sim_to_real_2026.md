---
$id: ent_paper_physics_models_for_sim_to_real_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis
  zh: Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis
  ko: Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis
summary:
  en: "arXiv:2606.28805v2 Announce Type: replace \nAbstract: At competitive speeds and spins, a table tennis ball follows\
    \ complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training\
    \ a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world,\
    \ making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully\
    \ the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the\
    \ game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot\
    \ table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball\
    \ behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight,\
    \ ball-table contact, and ball-racket contact. that accurately capture the ball behavior over a vast range of speeds and\
    \ spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number\
    \ and spin ratio in the aerodynamics equations. For the table contact model we model effects of ball buckling on the coefficient\
    \ of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model,\
    \ we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients\
    \ of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches\
    \ (277 games), the proposed models significantly reduces prediction errors (e.g., 59% median landing-position error reduction).\
    \ The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable\
    \ of competing against professional players."
  zh: "arXiv:2606.28805v2 Announce Type: replace \nAbstract: At competitive speeds and spins, a table tennis ball follows\
    \ complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training\
    \ a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world,\
    \ making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully\
    \ the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the\
    \ game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot\
    \ table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball\
    \ behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight,\
    \ ball-table contact, and ball-racket contact. that accurately capture the ball behavior over a vast range of speeds and\
    \ spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number\
    \ and spin ratio in the aerodynamics equations. For the table contact model we model effects of ball buckling on the coefficient\
    \ of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model,\
    \ we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients\
    \ of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches\
    \ (277 games), the proposed models significantly reduces prediction errors (e.g., 59% median landing-position error reduction).\
    \ The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable\
    \ of competing against professional players."
  ko: "arXiv:2606.28805v2 Announce Type: replace \nAbstract: At competitive speeds and spins, a table tennis ball follows\
    \ complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training\
    \ a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world,\
    \ making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully\
    \ the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the\
    \ game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot\
    \ table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball\
    \ behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight,\
    \ ball-table contact, and ball-racket contact. that accurately capture the ball behavior over a vast range of speeds and\
    \ spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number\
    \ and spin ratio in the aerodynamics equations. For the table contact model we model effects of ball buckling on the coefficient\
    \ of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model,\
    \ we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients\
    \ of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches\
    \ (277 games), the proposed models significantly reduces prediction errors (e.g., 59% median landing-position error reduction).\
    \ The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable\
    \ of competing against professional players."
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
- physics_models_for_sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.28805v2.
sources:
- id: src_001
  type: paper
  title: Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis (arXiv)
  url: https://arxiv.org/abs/2606.28805
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
At competitive speeds and spins, a table tennis ball follows complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact. that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations. For the table contact model we model effects of ball buckling on the coefficient of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduces prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable of competing against professional players.

## 核心内容
At competitive speeds and spins, a table tennis ball follows complex, counterintuitive trajectories that a robot must track and precisely counter within fractions of a second. Training a reinforcement learning policy capable of these skills is prohibitively expensive and dangerous in the real world, making high-fidelity simulation essential. Transferability of such policies, however, critically depends on how faithfully the simulation captures real-world dynamics - a requirement made even more stringent by the adversarial nature of the game, where any modeling inaccuracy becomes an exploitable weakness for the opponent. Prior state-of-the-art in robot table tennis generally focuses on a limited range of velocities and spins and fails to capture the richness of ball behaviors encountered in professional-level play. In this work, we present physics models for aerodynamic ball flight, ball-table contact, and ball-racket contact. that accurately capture the ball behavior over a vast range of speeds and spins relevant to the game. Specifically, we model drag and Magnus force coefficients as functions of Reynolds number and spin ratio in the aerodynamics equations. For the table contact model we model effects of ball buckling on the coefficient of restitution and incorporate residuals into the instantaneous point-contact models. For the racket contact model, we introduce a residual neural network component to complement coefficients related to normal and tangential coefficients of restitution as well as torsional spin damping. Evaluated on an unprecedentedly large dataset of competitive matches (277 games), the proposed models significantly reduces prediction errors (e.g., 59% median landing-position error reduction). The resulting models were used to train the RL policies for the first real-world robot table tennis AI agent capable of competing against professional players.

## 参考
- http://arxiv.org/abs/2606.28805v2

