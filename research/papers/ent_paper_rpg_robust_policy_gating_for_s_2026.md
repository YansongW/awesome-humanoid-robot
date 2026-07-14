---
$id: ent_paper_rpg_robust_policy_gating_for_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RPG: Robust Policy Gating for Smooth Multi-Skill Transitions in Humanoid Fighting'
  zh: 'RPG: Robust Policy Gating for Smooth Multi-Skill Transitions in Humanoid Fighting'
  ko: 'RPG: Robust Policy Gating for Smooth Multi-Skill Transitions in Humanoid Fighting'
summary:
  en: "arXiv:2604.21355v2 Announce Type: replace \nAbstract: Humanoid robots have\
    \ demonstrated impressive motor skills in a wide range of tasks, yet whole-body\
    \ control for humanlike long-time, dynamic fighting remains particularly challenging\
    \ due to the stringent requirements on agility and stability. While imitation\
    \ learning enables robots to execute human-like fighting skills, existing approaches\
    \ often rely on switching among multiple single-skill policies or employing a\
    \ general policy to imitate input reference motions. These strategies suffer from\
    \ instability when transitioning between skills, as the mismatch of initial and\
    \ terminal states across skills or reference motions introduces out-of-domain\
    \ disturbances, resulting in unsmooth or unstable behaviors. In this work, we\
    \ propose RPG, a hybrid expert policy framework, for smooth and stable humanoid\
    \ multi-skills transition. Our approach incorporates motion transition randomization\
    \ and temporal randomization to train a unified policy that generates agile fighting\
    \ actions with stability and smoothness during skill transitions. Furthermore,\
    \ we design a control pipeline that integrates walking/running locomotion with\
    \ fighting skills, allowing humanlike long-time combat of arbitrary duration that\
    \ can be seamlessly interrupted or transit action policies at any time. Extensive\
    \ experiments in simulation demonstrate the effectiveness of the proposed framework,\
    \ and real-world deployment on the Unitree G1 humanoid robot further validates\
    \ its robustness and applicability."
  zh: "arXiv:2604.21355v2 Announce Type: replace \nAbstract: Humanoid robots have\
    \ demonstrated impressive motor skills in a wide range of tasks, yet whole-body\
    \ control for humanlike long-time, dynamic fighting remains particularly challenging\
    \ due to the stringent requirements on agility and stability. While imitation\
    \ learning enables robots to execute human-like fighting skills, existing approaches\
    \ often rely on switching among multiple single-skill policies or employing a\
    \ general policy to imitate input reference motions. These strategies suffer from\
    \ instability when transitioning between skills, as the mismatch of initial and\
    \ terminal states across skills or reference motions introduces out-of-domain\
    \ disturbances, resulting in unsmooth or unstable behaviors. In this work, we\
    \ propose RPG, a hybrid expert policy framework, for smooth and stable humanoid\
    \ multi-skills transition. Our approach incorporates motion transition randomization\
    \ and temporal randomization to train a unified policy that generates agile fighting\
    \ actions with stability and smoothness during skill transitions. Furthermore,\
    \ we design a control pipeline that integrates walking/running locomotion with\
    \ fighting skills, allowing humanlike long-time combat of arbitrary duration that\
    \ can be seamlessly interrupted or transit action policies at any time. Extensive\
    \ experiments in simulation demonstrate the effectiveness of the proposed framework,\
    \ and real-world deployment on the Unitree G1 humanoid robot further validates\
    \ its robustness and applicability."
  ko: "arXiv:2604.21355v2 Announce Type: replace \nAbstract: Humanoid robots have\
    \ demonstrated impressive motor skills in a wide range of tasks, yet whole-body\
    \ control for humanlike long-time, dynamic fighting remains particularly challenging\
    \ due to the stringent requirements on agility and stability. While imitation\
    \ learning enables robots to execute human-like fighting skills, existing approaches\
    \ often rely on switching among multiple single-skill policies or employing a\
    \ general policy to imitate input reference motions. These strategies suffer from\
    \ instability when transitioning between skills, as the mismatch of initial and\
    \ terminal states across skills or reference motions introduces out-of-domain\
    \ disturbances, resulting in unsmooth or unstable behaviors. In this work, we\
    \ propose RPG, a hybrid expert policy framework, for smooth and stable humanoid\
    \ multi-skills transition. Our approach incorporates motion transition randomization\
    \ and temporal randomization to train a unified policy that generates agile fighting\
    \ actions with stability and smoothness during skill transitions. Furthermore,\
    \ we design a control pipeline that integrates walking/running locomotion with\
    \ fighting skills, allowing humanlike long-time combat of arbitrary duration that\
    \ can be seamlessly interrupted or transit action policies at any time. Extensive\
    \ experiments in simulation demonstrate the effectiveness of the proposed framework,\
    \ and real-world deployment on the Unitree G1 humanoid robot further validates\
    \ its robustness and applicability."
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
- rpg
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
  title: 'RPG: Robust Policy Gating for Smooth Multi-Skill Transitions in Humanoid
    Fighting'
  url: https://arxiv.org/abs/2604.21355
  date: '2026'
  accessed_at: '2026-07-01'
---

## 概述
arXiv:2604.21355v2 Announce Type: replace 
Abstract: Humanoid robots have demonstrated impressive motor skills in a wide range of tasks, yet whole-body control for humanlike long-time, dynamic fighting remains particularly challenging due to the stringent requirements on agility and stability. While imitation learning enables robots to execute human-like fighting skills, existing approaches often rely on switching among multiple single-skill policies or employing a general policy to imitate input reference motions. These strategies suffer from instability when transitioning between skills, as the mismatch of initial and terminal states across skills or reference motions introduces out-of-domain disturbances, resulting in unsmooth or unstable behaviors. In this work, we propose RPG, a hybrid expert policy framework, for smooth and stable humanoid multi-skills transition. Our approach incorporates motion transition randomization and temporal randomization to train a unified policy that generates agile fighting actions with stability and smoothness during skill transitions. Furthermore, we design a control pipeline that integrates walking/running locomotion with fighting skills, allowing humanlike long-time combat of arbitrary duration that can be seamlessly interrupted or transit action policies at any time. Extensive experiments in simulation demonstrate the effectiveness of the proposed framework, and real-world deployment on the Unitree G1 humanoid robot further validates its robustness and applicability.

## Overview
arXiv:2604.21355v2 Announce Type: replace 
Abstract: Humanoid robots have demonstrated impressive motor skills in a wide range of tasks, yet whole-body control for humanlike long-time, dynamic fighting remains particularly challenging due to the stringent requirements on agility and stability. While imitation learning enables robots to execute human-like fighting skills, existing approaches often rely on switching among multiple single-skill policies or employing a general policy to imitate input reference motions. These strategies suffer from instability when transitioning between skills, as the mismatch of initial and terminal states across skills or reference motions introduces out-of-domain disturbances, resulting in unsmooth or unstable behaviors. In this work, we propose RPG, a hybrid expert policy framework, for smooth and stable humanoid multi-skills transition. Our approach incorporates motion transition randomization and temporal randomization to train a unified policy that generates agile fighting actions with stability and smoothness during skill transitions. Furthermore, we design a control pipeline that integrates walking/running locomotion with fighting skills, allowing humanlike long-time combat of arbitrary duration that can be seamlessly interrupted or transit action policies at any time. Extensive experiments in simulation demonstrate the effectiveness of the proposed framework, and real-world deployment on the Unitree G1 humanoid robot further validates its robustness and applicability.

## 개요
arXiv:2604.21355v2 Announce Type: replace 
Abstract: Humanoid robots have demonstrated impressive motor skills in a wide range of tasks, yet whole-body control for humanlike long-time, dynamic fighting remains particularly challenging due to the stringent requirements on agility and stability. While imitation learning enables robots to execute human-like fighting skills, existing approaches often rely on switching among multiple single-skill policies or employing a general policy to imitate input reference motions. These strategies suffer from instability when transitioning between skills, as the mismatch of initial and terminal states across skills or reference motions introduces out-of-domain disturbances, resulting in unsmooth or unstable behaviors. In this work, we propose RPG, a hybrid expert policy framework, for smooth and stable humanoid multi-skills transition. Our approach incorporates motion transition randomization and temporal randomization to train a unified policy that generates agile fighting actions with stability and smoothness during skill transitions. Furthermore, we design a control pipeline that integrates walking/running locomotion with fighting skills, allowing humanlike long-time combat of arbitrary duration that can be seamlessly interrupted or transit action policies at any time. Extensive experiments in simulation demonstrate the effectiveness of the proposed framework, and real-world deployment on the Unitree G1 humanoid robot further validates its robustness and applicability.
