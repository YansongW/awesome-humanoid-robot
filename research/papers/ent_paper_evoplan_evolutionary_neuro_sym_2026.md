---
$id: ent_paper_evoplan_evolutionary_neuro_sym_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EvoPlan: Evolutionary Neuro-Symbolic Robot Planning with Spatio-Temporal Guarantees'
  zh: 'EvoPlan: Evolutionary Neuro-Symbolic Robot Planning with Spatio-Temporal Guarantees'
  ko: ''
summary:
  en: "arXiv:2607.06724v1 Announce Type: new \nAbstract: LLM-based robot planners\
    \ are fluent but cannot guarantee that their plans are executable or safe. Classical\
    \ PDDL planners can guarantee these properties, but only after the problem is\
    \ fully specified, and they make poor use of an LLM's ability to read context\
    \ and repair plans. This paper presents a neuro-symbolic framework with three\
    \ parts. All LLM calls use a locally-hosted open-weight model, so the pipeline\
    \ can be deployed on-robot with no cloud dependency. First, an offline procedure\
    \ that mines a single global Signal Temporal Logic (STL) constraint on mobility\
    \ from demonstration data. The procedure recovers codified rules (e.g., stopping\
    \ at red lights, mined from nuPlan driving logs) or population preferences (e.g.,\
    \ social-navigation comfort, mined from SCAND teleoperation), depending on what\
    \ the demonstrations encode. Because the demonstrations are a one-class signal,\
    \ we generate the missing negatives with counterfactual perturbations and an LLM\
    \ violation generator and then fit the constraint by evolutionary search. We use\
    \ the mined constraint to shield a vision-language driving policy on Bench2Drive\
    \ and two discrete-action navigation policies on HA-VLN-CE. Second, an evolutionary\
    \ PDDL planner: an LLM proposes and repairs plans, programmatic validators decide\
    \ which ones survive, and the validated portion of the plan grows over iterations.\
    \ We test the planner on the open-world ALFWorld Text benchmark, where it beats\
    \ strong baselines and stays robust when the goal vocabulary does not match the\
    \ action-model vocabulary. Third, a constrained execution loop: the planner's\
    \ plan is compiled into waypoints, the waypoints are checked against the mined\
    \ constraint, and the planner re-plans on a violation. We illustrate the full\
    \ pipeline via demonstrations using the Gazebo simulator."
  zh: "arXiv:2607.06724v1 Announce Type: new \nAbstract: LLM-based robot planners\
    \ are fluent but cannot guarantee that their plans are executable or safe. Classical\
    \ PDDL planners can guarantee these properties, but only after the problem is\
    \ fully specified, and they make poor use of an LLM's ability to read context\
    \ and repair plans. This paper presents a neuro-symbolic framework with three\
    \ parts. All LLM calls use a locally-hosted open-weight model, so the pipeline\
    \ can be deployed on-robot with no cloud dependency. First, an offline procedure\
    \ that mines a single global Signal Temporal Logic (STL) constraint on mobility\
    \ from demonstration data. The procedure recovers codified rules (e.g., stopping\
    \ at red lights, mined from nuPlan driving logs) or population preferences (e.g.,\
    \ social-navigation comfort, mined from SCAND teleoperation), depending on what\
    \ the demonstrations encode. Because the demonstrations are a one-class signal,\
    \ we generate the missing negatives with counterfactual perturbations and an LLM\
    \ violation generator and then fit the constraint by evolutionary search. We use\
    \ the mined constraint to shield a vision-language driving policy on Bench2Drive\
    \ and two discrete-action navigation policies on HA-VLN-CE. Second, an evolutionary\
    \ PDDL planner: an LLM proposes and repairs plans, programmatic validators decide\
    \ which ones survive, and the validated portion of the plan grows over iterations.\
    \ We test the planner on the open-world ALFWorld Text benchmark, where it beats\
    \ strong baselines and stays robust when the goal vocabulary does not match the\
    \ action-model vocabulary. Third, a constrained execution loop: the planner's\
    \ plan is compiled into waypoints, the waypoints are checked against the mined\
    \ constraint, and the planner re-plans on a violation. We illustrate the full\
    \ pipeline via demonstrations using the Gazebo simulator."
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
- evoplan
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
  title: 'EvoPlan: Evolutionary Neuro-Symbolic Robot Planning with Spatio-Temporal
    Guarantees (arXiv)'
  url: https://arxiv.org/abs/2607.06724
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2607.06724v1 Announce Type: new 
Abstract: LLM-based robot planners are fluent but cannot guarantee that their plans are executable or safe. Classical PDDL planners can guarantee these properties, but only after the problem is fully specified, and they make poor use of an LLM's ability to read context and repair plans. This paper presents a neuro-symbolic framework with three parts. All LLM calls use a locally-hosted open-weight model, so the pipeline can be deployed on-robot with no cloud dependency. First, an offline procedure that mines a single global Signal Temporal Logic (STL) constraint on mobility from demonstration data. The procedure recovers codified rules (e.g., stopping at red lights, mined from nuPlan driving logs) or population preferences (e.g., social-navigation comfort, mined from SCAND teleoperation), depending on what the demonstrations encode. Because the demonstrations are a one-class signal, we generate the missing negatives with counterfactual perturbations and an LLM violation generator and then fit the constraint by evolutionary search. We use the mined constraint to shield a vision-language driving policy on Bench2Drive and two discrete-action navigation policies on HA-VLN-CE. Second, an evolutionary PDDL planner: an LLM proposes and repairs plans, programmatic validators decide which ones survive, and the validated portion of the plan grows over iterations. We test the planner on the open-world ALFWorld Text benchmark, where it beats strong baselines and stays robust when the goal vocabulary does not match the action-model vocabulary. Third, a constrained execution loop: the planner's plan is compiled into waypoints, the waypoints are checked against the mined constraint, and the planner re-plans on a violation. We illustrate the full pipeline via demonstrations using the Gazebo simulator.
