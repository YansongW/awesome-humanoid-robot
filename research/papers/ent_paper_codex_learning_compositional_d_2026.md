---
$id: ent_paper_codex_learning_compositional_d_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoDex: Learning Compositional Dexterous Functional Manipulation without Demonstrations'
  zh: 'CoDex: Learning Compositional Dexterous Functional Manipulation without Demonstrations'
  ko: ''
summary:
  en: "arXiv:2606.31909v1 Announce Type: new \nAbstract: In this work, we study Compositional\
    \ Dexterous Functional Object Manipulation (CD-FOM): tasks such as aiming and\
    \ actuating a spray bottle on a plant or a glue gun on wood, which require both\
    \ actuating an object's internal mechanism and controlling its pose to apply the\
    \ object's function to the environment. These tasks pose significant challenges\
    \ for robots due to the demanding integration of semantic understanding of the\
    \ object's function, actuation mode, and application area with intricate physical\
    \ dexterity to manage grasp stability, movement trajectory, and actuation. We\
    \ introduce CoDex, a zero-demonstration framework that autonomously discovers\
    \ CD-FOM manipulation strategies. CoDex uses vision-language models (VLMs) to\
    \ infer semantic constraints from the task and scene. These constraints guide\
    \ analytic constrained optimization to generate a short list of functional grasp\
    \ candidates that can be efficiently refined with reinforcement learning to generate\
    \ full grasp-move-actuate policies transferable from simulation to the real world.\
    \ We evaluate CoDex on a 7-DoF robot arm with a 16-DoF multi-fingered hand across\
    \ six CD-FOM tasks involving previously unseen objects with internal mechanisms,\
    \ including spray bottles, hot glue guns, air dusters, flashlights, and pepper\
    \ grinders, and their application to unseen target objects, showcasing its ability\
    \ to autonomously discover and execute complex, physically viable dexterous behaviors\
    \ without human demonstrations. More information at https://robin-lab.cs.utexas.edu/CoDex/."
  zh: "arXiv:2606.31909v1 Announce Type: new \nAbstract: In this work, we study Compositional\
    \ Dexterous Functional Object Manipulation (CD-FOM): tasks such as aiming and\
    \ actuating a spray bottle on a plant or a glue gun on wood, which require both\
    \ actuating an object's internal mechanism and controlling its pose to apply the\
    \ object's function to the environment. These tasks pose significant challenges\
    \ for robots due to the demanding integration of semantic understanding of the\
    \ object's function, actuation mode, and application area with intricate physical\
    \ dexterity to manage grasp stability, movement trajectory, and actuation. We\
    \ introduce CoDex, a zero-demonstration framework that autonomously discovers\
    \ CD-FOM manipulation strategies. CoDex uses vision-language models (VLMs) to\
    \ infer semantic constraints from the task and scene. These constraints guide\
    \ analytic constrained optimization to generate a short list of functional grasp\
    \ candidates that can be efficiently refined with reinforcement learning to generate\
    \ full grasp-move-actuate policies transferable from simulation to the real world.\
    \ We evaluate CoDex on a 7-DoF robot arm with a 16-DoF multi-fingered hand across\
    \ six CD-FOM tasks involving previously unseen objects with internal mechanisms,\
    \ including spray bottles, hot glue guns, air dusters, flashlights, and pepper\
    \ grinders, and their application to unseen target objects, showcasing its ability\
    \ to autonomously discover and execute complex, physically viable dexterous behaviors\
    \ without human demonstrations. More information at https://robin-lab.cs.utexas.edu/CoDex/."
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
- codex
- humanoid
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
  title: 'CoDex: Learning Compositional Dexterous Functional Manipulation without
    Demonstrations'
  url: https://arxiv.org/abs/2606.31909
  date: '2026'
  accessed_at: '2026-07-01'
---

arXiv:2606.31909v1 Announce Type: new 
Abstract: In this work, we study Compositional Dexterous Functional Object Manipulation (CD-FOM): tasks such as aiming and actuating a spray bottle on a plant or a glue gun on wood, which require both actuating an object's internal mechanism and controlling its pose to apply the object's function to the environment. These tasks pose significant challenges for robots due to the demanding integration of semantic understanding of the object's function, actuation mode, and application area with intricate physical dexterity to manage grasp stability, movement trajectory, and actuation. We introduce CoDex, a zero-demonstration framework that autonomously discovers CD-FOM manipulation strategies. CoDex uses vision-language models (VLMs) to infer semantic constraints from the task and scene. These constraints guide analytic constrained optimization to generate a short list of functional grasp candidates that can be efficiently refined with reinforcement learning to generate full grasp-move-actuate policies transferable from simulation to the real world. We evaluate CoDex on a 7-DoF robot arm with a 16-DoF multi-fingered hand across six CD-FOM tasks involving previously unseen objects with internal mechanisms, including spray bottles, hot glue guns, air dusters, flashlights, and pepper grinders, and their application to unseen target objects, showcasing its ability to autonomously discover and execute complex, physically viable dexterous behaviors without human demonstrations. More information at https://robin-lab.cs.utexas.edu/CoDex/.
