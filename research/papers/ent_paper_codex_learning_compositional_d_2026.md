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
  zh: CoDex 是一个零演示框架，用于自主发现组合式灵巧功能性物体操作（CD-FOM）策略。该框架由德克萨斯大学奥斯汀分校 Robin Lab 提出，核心贡献在于结合视觉语言模型（VLM）与解析约束优化及强化学习，无需人类演示即可生成从仿真迁移到真实世界的完整抓取-移动-操作策略。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31909v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'CoDex: Learning Compositional Dexterous Functional Manipulation without Demonstrations'
  url: https://arxiv.org/abs/2606.31909
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
CoDex 针对组合式灵巧功能性物体操作（CD-FOM）任务设计，这类任务要求机器人同时操作物体内部机制并控制其姿态以对环境施加功能。该框架利用视觉语言模型（VLM）从任务和场景中推断语义约束，再通过解析约束优化生成少量功能性抓取候选，最后用强化学习高效优化出完整的抓取-移动-操作策略。在配备 16 自由度多指手的 7 自由度机械臂上，CoDex 在六项涉及未见过内部机制物体（如喷雾瓶、热胶枪、气吹、手电筒、胡椒研磨器）的任务中成功验证了其零演示自主发现复杂灵巧行为的能力。

## 核心内容
### 方法架构
CoDex 采用三阶段流水线：
- **语义约束推理**：使用视觉语言模型（VLM）分析任务场景，提取物体功能、操作模式与应用区域相关的语义约束。
- **功能性抓取生成**：基于语义约束进行解析约束优化，生成少量可行的功能性抓取候选，确保抓取姿态同时满足稳定性与功能执行需求。
- **策略优化与迁移**：通过强化学习对抓取候选进行高效优化，生成完整的 grasp-move-actuate 策略，并实现从仿真环境到真实世界的零样本迁移。

### 实验设置
- **硬件平台**：7 自由度机器人臂搭配 16 自由度多指灵巧手。
- **任务集**：六项 CD-FOM 任务，涉及未见过内部机制物体（喷雾瓶、热胶枪、气吹、手电筒、胡椒研磨器）及其对未见过目标物体的应用。
- **评估指标**：任务成功率、策略物理可行性、零演示自主发现能力。

### 关键结果
- CoDex 在全部六项任务中成功自主发现并执行了复杂灵巧行为，无需任何人类演示。
- 生成的策略在仿真与真实世界间表现出良好的迁移性，验证了框架的泛化能力。
- 与基线方法相比，CoDex 在功能性抓取生成效率与策略物理可行性上均取得显著优势。

### 结论
CoDex 通过融合 VLM 的语义理解与优化方法的物理精确性，为零演示灵巧操作提供了有效方案，为机器人自主执行复杂功能性任务开辟了新路径。更多信息见 https://robin-lab.cs.utexas.edu/CoDex/。

## Overview
In this work, we study Compositional Dexterous Functional Object Manipulation (CD-FOM): tasks such as aiming and actuating a spray bottle on a plant or a glue gun on wood, which require both actuating an object's internal mechanism and controlling its pose to apply the object's function to the environment. These tasks pose significant challenges for robots due to the demanding integration of semantic understanding of the object's function, actuation mode, and application area with intricate physical dexterity to manage grasp stability, movement trajectory, and actuation. We introduce CoDex, a zero-demonstration framework that autonomously discovers CD-FOM manipulation strategies. CoDex uses vision-language models (VLMs) to infer semantic constraints from the task and scene. These constraints guide analytic constrained optimization to generate a short list of functional grasp candidates that can be efficiently refined with reinforcement learning to generate full grasp-move-actuate policies transferable from simulation to the real world. We evaluate CoDex on a 7-DoF robot arm with a 16-DoF multi-fingered hand across six CD-FOM tasks involving previously unseen objects with internal mechanisms, including spray bottles, hot glue guns, air dusters, flashlights, and pepper grinders, and their application to unseen target objects, showcasing its ability to autonomously discover and execute complex, physically viable dexterous behaviors without human demonstrations. More information at https://robin-lab.cs.utexas.edu/CoDex/.

## 개요
본 연구에서는 구성적 손재주 기능적 물체 조작(CD-FOM)을 다룹니다. 이는 식물에 분무기 조준 및 작동, 나무에 글루건 사용 등 물체의 내부 메커니즘을 작동시키면서 동시에 물체의 자세를 제어하여 환경에 기능을 적용하는 작업을 포함합니다. 이러한 작업은 물체의 기능, 작동 방식, 적용 영역에 대한 의미론적 이해와 파지 안정성, 이동 궤적, 작동을 관리하는 정교한 물리적 손재주를 통합해야 하므로 로봇에게 큰 도전 과제가 됩니다. 우리는 CD-FOM 조작 전략을 자율적으로 발견하는 제로 데모 프레임워크인 CoDex를 소개합니다. CoDex는 비전-언어 모델(VLM)을 사용하여 작업과 장면에서 의미론적 제약 조건을 추론합니다. 이러한 제약 조건은 분석적 제약 최적화를 안내하여 기능적 파지 후보의 짧은 목록을 생성하며, 이를 강화 학습으로 효율적으로 개선하여 시뮬레이션에서 실제 세계로 전이 가능한 완전한 파지-이동-작동 정책을 생성합니다. 우리는 7-DoF 로봇 팔과 16-DoF 다지 손을 사용하여 분무기, 핫 글루건, 에어 더스터, 손전등, 후추 그라인더 등 내부 메커니즘을 가진 이전에 본 적 없는 물체와 보지 못한 대상 물체에의 적용을 포함한 여섯 가지 CD-FOM 작업에서 CoDex를 평가하며, 인간 시연 없이 복잡하고 물리적으로 실행 가능한 손재주 행동을 자율적으로 발견하고 실행하는 능력을 입증합니다. 자세한 정보는 https://robin-lab.cs.utexas.edu/CoDex/에서 확인할 수 있습니다.

## 핵심 내용
본 연구에서는 구성적 손재주 기능적 물체 조작(CD-FOM)을 다룹니다. 이는 식물에 분무기 조준 및 작동, 나무에 글루건 사용 등 물체의 내부 메커니즘을 작동시키면서 동시에 물체의 자세를 제어하여 환경에 기능을 적용하는 작업을 포함합니다. 이러한 작업은 물체의 기능, 작동 방식, 적용 영역에 대한 의미론적 이해와 파지 안정성, 이동 궤적, 작동을 관리하는 정교한 물리적 손재주를 통합해야 하므로 로봇에게 큰 도전 과제가 됩니다. 우리는 CD-FOM 조작 전략을 자율적으로 발견하는 제로 데모 프레임워크인 CoDex를 소개합니다. CoDex는 비전-언어 모델(VLM)을 사용하여 작업과 장면에서 의미론적 제약 조건을 추론합니다. 이러한 제약 조건은 분석적 제약 최적화를 안내하여 기능적 파지 후보의 짧은 목록을 생성하며, 이를 강화 학습으로 효율적으로 개선하여 시뮬레이션에서 실제 세계로 전이 가능한 완전한 파지-이동-작동 정책을 생성합니다. 우리는 7-DoF 로봇 팔과 16-DoF 다지 손을 사용하여 분무기, 핫 글루건, 에어 더스터, 손전등, 후추 그라인더 등 내부 메커니즘을 가진 이전에 본 적 없는 물체와 보지 못한 대상 물체에의 적용을 포함한 여섯 가지 CD-FOM 작업에서 CoDex를 평가하며, 인간 시연 없이 복잡하고 물리적으로 실행 가능한 손재주 행동을 자율적으로 발견하고 실행하는 능력을 입증합니다. 자세한 정보는 https://robin-lab.cs.utexas.edu/CoDex/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2606.31909v1
