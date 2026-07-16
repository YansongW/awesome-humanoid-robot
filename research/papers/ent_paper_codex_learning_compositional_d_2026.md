---
$id: ent_paper_codex_learning_compositional_d_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoDex: Learning Compositional Dexterous Functional Manipulation without Demonstrations'
  zh: 'CoDex: Learning Compositional Dexterous Functional Manipulation without Demonstrations'
  ko: 'CoDex: Learning Compositional Dexterous Functional Manipulation without Demonstrations'
summary:
  en: 'arXiv:2606.31909v1 Announce Type: new Abstract: In this work, we study Compositional Dexterous Functional Object Manipulation
    (CD-FOM): tasks such as aiming and actuating a spray bottle on a plant or a glue gun on wood, which require both actuating
    an object''s internal mechanism and controlling its pose to apply the object''s function to the environment. These tasks
    pose significant challenges for robots due to the demanding integration of semantic understanding of the object''s function,
    actuation mode, and application area with intricate physical dexterity to manage grasp stability, movement trajectory,
    and actuation. We introduce CoDex, a zero-demonstration framework that autonomously discovers CD-FOM manipulation strategies.
    CoDex uses vision-language models (VLMs) to infer semantic constraints from the task and scene. These constraints guide
    analytic constrained optimization to generate a short list of functional grasp candidates that can be efficiently refined
    with reinforcement learning to generate full grasp-move-actuate policies transferable from simulation to the real world.
    We evaluate CoDex on a 7-DoF robot arm with a 16-DoF multi-fingered hand across six CD-FOM tasks involving previously
    unseen objects with internal mechanisms, including spray bottles, hot glue guns, air dusters, flashlights, and pepper
    grinders, and their application to unseen target objects, showcasing its ability to autonomously discover and execute
    complex, physically viable dexterous behaviors without human demonstrations. More information at https://robin-lab.cs.utexas.edu/CoDex/.'
  zh: 'arXiv:2606.31909v1 Announce Type: new Abstract: In this work, we study Compositional Dexterous Functional Object Manipulation
    (CD-FOM): tasks such as aiming and actuating a spray bottle on a plant or a glue gun on wood, which require both actuating
    an object''s internal mechanism and controlling its pose to apply the object''s function to the environment. These tasks
    pose significant challenges for robots due to the demanding integration of semantic understanding of the object''s function,
    actuation mode, and application area with intricate physical dexterity to manage grasp stability, movement trajectory,
    and actuation. We introduce CoDex, a zero-demonstration framework that autonomously discovers CD-FOM manipulation strategies.
    CoDex uses vision-language models (VLMs) to infer semantic constraints from the task and scene. These constraints guide
    analytic constrained optimization to generate a short list of functional grasp candidates that can be efficiently refined
    with reinforcement learning to generate full grasp-move-actuate policies transferable from simulation to the real world.
    We evaluate CoDex on a 7-DoF robot arm with a 16-DoF multi-fingered hand across six CD-FOM tasks involving previously
    unseen objects with internal mechanisms, including spray bottles, hot glue guns, air dusters, flashlights, and pepper
    grinders, and their application to unseen target objects, showcasing its ability to autonomously discover and execute
    complex, physically viable dexterous behaviors without human demonstrations. More information at https://robin-lab.cs.utexas.edu/CoDex/.'
  ko: 'arXiv:2606.31909v1 Announce Type: new Abstract: In this work, we study Compositional Dexterous Functional Object Manipulation
    (CD-FOM): tasks such as aiming and actuating a spray bottle on a plant or a glue gun on wood, which require both actuating
    an object''s internal mechanism and controlling its pose to apply the object''s function to the environment. These tasks
    pose significant challenges for robots due to the demanding integration of semantic understanding of the object''s function,
    actuation mode, and application area with intricate physical dexterity to manage grasp stability, movement trajectory,
    and actuation. We introduce CoDex, a zero-demonstration framework that autonomously discovers CD-FOM manipulation strategies.
    CoDex uses vision-language models (VLMs) to infer semantic constraints from the task and scene. These constraints guide
    analytic constrained optimization to generate a short list of functional grasp candidates that can be efficiently refined
    with reinforcement learning to generate full grasp-move-actuate policies transferable from simulation to the real world.
    We evaluate CoDex on a 7-DoF robot arm with a 16-DoF multi-fingered hand across six CD-FOM tasks involving previously
    unseen objects with internal mechanisms, including spray bottles, hot glue guns, air dusters, flashlights, and pepper
    grinders, and their application to unseen target objects, showcasing its ability to autonomously discover and execute
    complex, physically viable dexterous behaviors without human demonstrations. More information at https://robin-lab.cs.utexas.edu/CoDex/.'
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31909v1.
sources:
- id: src_001
  type: paper
  title: 'CoDex: Learning Compositional Dexterous Functional Manipulation without Demonstrations'
  url: https://arxiv.org/abs/2606.31909
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
In this work, we study Compositional Dexterous Functional Object Manipulation (CD-FOM): tasks such as aiming and actuating a spray bottle on a plant or a glue gun on wood, which require both actuating an object's internal mechanism and controlling its pose to apply the object's function to the environment. These tasks pose significant challenges for robots due to the demanding integration of semantic understanding of the object's function, actuation mode, and application area with intricate physical dexterity to manage grasp stability, movement trajectory, and actuation. We introduce CoDex, a zero-demonstration framework that autonomously discovers CD-FOM manipulation strategies. CoDex uses vision-language models (VLMs) to infer semantic constraints from the task and scene. These constraints guide analytic constrained optimization to generate a short list of functional grasp candidates that can be efficiently refined with reinforcement learning to generate full grasp-move-actuate policies transferable from simulation to the real world. We evaluate CoDex on a 7-DoF robot arm with a 16-DoF multi-fingered hand across six CD-FOM tasks involving previously unseen objects with internal mechanisms, including spray bottles, hot glue guns, air dusters, flashlights, and pepper grinders, and their application to unseen target objects, showcasing its ability to autonomously discover and execute complex, physically viable dexterous behaviors without human demonstrations. More information at https://robin-lab.cs.utexas.edu/CoDex/.

## 核心内容
In this work, we study Compositional Dexterous Functional Object Manipulation (CD-FOM): tasks such as aiming and actuating a spray bottle on a plant or a glue gun on wood, which require both actuating an object's internal mechanism and controlling its pose to apply the object's function to the environment. These tasks pose significant challenges for robots due to the demanding integration of semantic understanding of the object's function, actuation mode, and application area with intricate physical dexterity to manage grasp stability, movement trajectory, and actuation. We introduce CoDex, a zero-demonstration framework that autonomously discovers CD-FOM manipulation strategies. CoDex uses vision-language models (VLMs) to infer semantic constraints from the task and scene. These constraints guide analytic constrained optimization to generate a short list of functional grasp candidates that can be efficiently refined with reinforcement learning to generate full grasp-move-actuate policies transferable from simulation to the real world. We evaluate CoDex on a 7-DoF robot arm with a 16-DoF multi-fingered hand across six CD-FOM tasks involving previously unseen objects with internal mechanisms, including spray bottles, hot glue guns, air dusters, flashlights, and pepper grinders, and their application to unseen target objects, showcasing its ability to autonomously discover and execute complex, physically viable dexterous behaviors without human demonstrations. More information at https://robin-lab.cs.utexas.edu/CoDex/.

## 参考
- http://arxiv.org/abs/2606.31909v1

## Overview
In this work, we study Compositional Dexterous Functional Object Manipulation (CD-FOM): tasks such as aiming and actuating a spray bottle on a plant or a glue gun on wood, which require both actuating an object's internal mechanism and controlling its pose to apply the object's function to the environment. These tasks pose significant challenges for robots due to the demanding integration of semantic understanding of the object's function, actuation mode, and application area with intricate physical dexterity to manage grasp stability, movement trajectory, and actuation. We introduce CoDex, a zero-demonstration framework that autonomously discovers CD-FOM manipulation strategies. CoDex uses vision-language models (VLMs) to infer semantic constraints from the task and scene. These constraints guide analytic constrained optimization to generate a short list of functional grasp candidates that can be efficiently refined with reinforcement learning to generate full grasp-move-actuate policies transferable from simulation to the real world. We evaluate CoDex on a 7-DoF robot arm with a 16-DoF multi-fingered hand across six CD-FOM tasks involving previously unseen objects with internal mechanisms, including spray bottles, hot glue guns, air dusters, flashlights, and pepper grinders, and their application to unseen target objects, showcasing its ability to autonomously discover and execute complex, physically viable dexterous behaviors without human demonstrations. More information at https://robin-lab.cs.utexas.edu/CoDex/.

## Content
In this work, we study Compositional Dexterous Functional Object Manipulation (CD-FOM): tasks such as aiming and actuating a spray bottle on a plant or a glue gun on wood, which require both actuating an object's internal mechanism and controlling its pose to apply the object's function to the environment. These tasks pose significant challenges for robots due to the demanding integration of semantic understanding of the object's function, actuation mode, and application area with intricate physical dexterity to manage grasp stability, movement trajectory, and actuation. We introduce CoDex, a zero-demonstration framework that autonomously discovers CD-FOM manipulation strategies. CoDex uses vision-language models (VLMs) to infer semantic constraints from the task and scene. These constraints guide analytic constrained optimization to generate a short list of functional grasp candidates that can be efficiently refined with reinforcement learning to generate full grasp-move-actuate policies transferable from simulation to the real world. We evaluate CoDex on a 7-DoF robot arm with a 16-DoF multi-fingered hand across six CD-FOM tasks involving previously unseen objects with internal mechanisms, including spray bottles, hot glue guns, air dusters, flashlights, and pepper grinders, and their application to unseen target objects, showcasing its ability to autonomously discover and execute complex, physically viable dexterous behaviors without human demonstrations. More information at https://robin-lab.cs.utexas.edu/CoDex/.

## 개요
본 연구에서는 구성적 손재주 기능적 물체 조작(CD-FOM)을 다룹니다. 이는 식물에 분무기 조준 및 작동, 나무에 글루건 사용 등 물체의 내부 메커니즘을 작동시키면서 동시에 물체의 자세를 제어하여 환경에 기능을 적용하는 작업을 포함합니다. 이러한 작업은 물체의 기능, 작동 방식, 적용 영역에 대한 의미론적 이해와 파지 안정성, 이동 궤적, 작동을 관리하는 정교한 물리적 손재주를 통합해야 하므로 로봇에게 큰 도전 과제가 됩니다. 우리는 CD-FOM 조작 전략을 자율적으로 발견하는 제로 데모 프레임워크인 CoDex를 소개합니다. CoDex는 비전-언어 모델(VLM)을 사용하여 작업과 장면에서 의미론적 제약 조건을 추론합니다. 이러한 제약 조건은 분석적 제약 최적화를 안내하여 기능적 파지 후보의 짧은 목록을 생성하며, 이를 강화 학습으로 효율적으로 개선하여 시뮬레이션에서 실제 세계로 전이 가능한 완전한 파지-이동-작동 정책을 생성합니다. 우리는 7-DoF 로봇 팔과 16-DoF 다지 손을 사용하여 분무기, 핫 글루건, 에어 더스터, 손전등, 후추 그라인더 등 내부 메커니즘을 가진 이전에 본 적 없는 물체와 보지 못한 대상 물체에의 적용을 포함한 여섯 가지 CD-FOM 작업에서 CoDex를 평가하며, 인간 시연 없이 복잡하고 물리적으로 실행 가능한 손재주 행동을 자율적으로 발견하고 실행하는 능력을 입증합니다. 자세한 정보는 https://robin-lab.cs.utexas.edu/CoDex/에서 확인할 수 있습니다.

## 핵심 내용
본 연구에서는 구성적 손재주 기능적 물체 조작(CD-FOM)을 다룹니다. 이는 식물에 분무기 조준 및 작동, 나무에 글루건 사용 등 물체의 내부 메커니즘을 작동시키면서 동시에 물체의 자세를 제어하여 환경에 기능을 적용하는 작업을 포함합니다. 이러한 작업은 물체의 기능, 작동 방식, 적용 영역에 대한 의미론적 이해와 파지 안정성, 이동 궤적, 작동을 관리하는 정교한 물리적 손재주를 통합해야 하므로 로봇에게 큰 도전 과제가 됩니다. 우리는 CD-FOM 조작 전략을 자율적으로 발견하는 제로 데모 프레임워크인 CoDex를 소개합니다. CoDex는 비전-언어 모델(VLM)을 사용하여 작업과 장면에서 의미론적 제약 조건을 추론합니다. 이러한 제약 조건은 분석적 제약 최적화를 안내하여 기능적 파지 후보의 짧은 목록을 생성하며, 이를 강화 학습으로 효율적으로 개선하여 시뮬레이션에서 실제 세계로 전이 가능한 완전한 파지-이동-작동 정책을 생성합니다. 우리는 7-DoF 로봇 팔과 16-DoF 다지 손을 사용하여 분무기, 핫 글루건, 에어 더스터, 손전등, 후추 그라인더 등 내부 메커니즘을 가진 이전에 본 적 없는 물체와 보지 못한 대상 물체에의 적용을 포함한 여섯 가지 CD-FOM 작업에서 CoDex를 평가하며, 인간 시연 없이 복잡하고 물리적으로 실행 가능한 손재주 행동을 자율적으로 발견하고 실행하는 능력을 입증합니다. 자세한 정보는 https://robin-lab.cs.utexas.edu/CoDex/에서 확인할 수 있습니다.
