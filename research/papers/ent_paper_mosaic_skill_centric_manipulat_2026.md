---
$id: ent_paper_mosaic_skill_centric_manipulat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MOSAIC: Skill-Centric Manipulation Planning with Physics Simulation'
  zh: 'MOSAIC: Skill-Centric Manipulation Planning with Physics Simulation'
  ko: ''
summary:
  en: "arXiv:2504.16738v3 Announce Type: replace \nAbstract: Planning long-horizon\
    \ manipulation motions using a set of predefined skills is a central challenge\
    \ in robotics; solving it efficiently could enable general-purpose robots to tackle\
    \ novel tasks by flexibly composing generic skills. Solutions to this problem\
    \ lie in an infinitely vast space of parameterized skill sequences -- a space\
    \ where common incremental methods struggle to find sequences that have non-obvious\
    \ intermediate steps. Some approaches reason over lower-dimensional, symbolic\
    \ spaces, which are more tractable to explore but may be brittle and are laborious\
    \ to construct. In this work, we introduce MOSAIC, a skill-centric, multi-directional\
    \ planning approach that targets these challenges by reasoning about which skills\
    \ to employ and where they are most likely to succeed, by utilizing physics simulation\
    \ to estimate skill execution outcomes. Specifically, MOSAIC employs two complementary\
    \ skill families: Generators, which identify ``islands of competence'' where skills\
    \ are demonstrably effective, and Connectors, which link these skill-trajectories\
    \ by solving boundary value problems. By focusing planning efforts on regions\
    \ of high competence, MOSAIC efficiently discovers physically-grounded solutions.\
    \ We demonstrate its efficacy on complex long-horizon problems in both simulation\
    \ and the real world, using a diverse set of skills including generative diffusion\
    \ models, motion planning algorithms, and manipulation-specific models. Visit\
    \ skill-mosaic.github.io for demonstrations and examples."
  zh: "arXiv:2504.16738v3 Announce Type: replace \nAbstract: Planning long-horizon\
    \ manipulation motions using a set of predefined skills is a central challenge\
    \ in robotics; solving it efficiently could enable general-purpose robots to tackle\
    \ novel tasks by flexibly composing generic skills. Solutions to this problem\
    \ lie in an infinitely vast space of parameterized skill sequences -- a space\
    \ where common incremental methods struggle to find sequences that have non-obvious\
    \ intermediate steps. Some approaches reason over lower-dimensional, symbolic\
    \ spaces, which are more tractable to explore but may be brittle and are laborious\
    \ to construct. In this work, we introduce MOSAIC, a skill-centric, multi-directional\
    \ planning approach that targets these challenges by reasoning about which skills\
    \ to employ and where they are most likely to succeed, by utilizing physics simulation\
    \ to estimate skill execution outcomes. Specifically, MOSAIC employs two complementary\
    \ skill families: Generators, which identify ``islands of competence'' where skills\
    \ are demonstrably effective, and Connectors, which link these skill-trajectories\
    \ by solving boundary value problems. By focusing planning efforts on regions\
    \ of high competence, MOSAIC efficiently discovers physically-grounded solutions.\
    \ We demonstrate its efficacy on complex long-horizon problems in both simulation\
    \ and the real world, using a diverse set of skills including generative diffusion\
    \ models, motion planning algorithms, and manipulation-specific models. Visit\
    \ skill-mosaic.github.io for demonstrations and examples."
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
- mosaic
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
  title: 'MOSAIC: Skill-Centric Manipulation Planning with Physics Simulation (arXiv)'
  url: https://arxiv.org/abs/2504.16738
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2504.16738v3 Announce Type: replace 
Abstract: Planning long-horizon manipulation motions using a set of predefined skills is a central challenge in robotics; solving it efficiently could enable general-purpose robots to tackle novel tasks by flexibly composing generic skills. Solutions to this problem lie in an infinitely vast space of parameterized skill sequences -- a space where common incremental methods struggle to find sequences that have non-obvious intermediate steps. Some approaches reason over lower-dimensional, symbolic spaces, which are more tractable to explore but may be brittle and are laborious to construct. In this work, we introduce MOSAIC, a skill-centric, multi-directional planning approach that targets these challenges by reasoning about which skills to employ and where they are most likely to succeed, by utilizing physics simulation to estimate skill execution outcomes. Specifically, MOSAIC employs two complementary skill families: Generators, which identify ``islands of competence'' where skills are demonstrably effective, and Connectors, which link these skill-trajectories by solving boundary value problems. By focusing planning efforts on regions of high competence, MOSAIC efficiently discovers physically-grounded solutions. We demonstrate its efficacy on complex long-horizon problems in both simulation and the real world, using a diverse set of skills including generative diffusion models, motion planning algorithms, and manipulation-specific models. Visit skill-mosaic.github.io for demonstrations and examples.
