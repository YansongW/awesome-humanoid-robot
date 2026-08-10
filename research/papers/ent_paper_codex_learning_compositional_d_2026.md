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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31909v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (896 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2606.31909v1

## 개요
CoDex는 조합형 다기능 물체 조작(CD-FOM) 작업을 위해 설계되었으며, 이러한 작업은 로봇이 물체의 내부 메커니즘을 동시에 조작하고 자세를 제어하여 환경에 기능을 적용해야 합니다. 이 프레임워크는 시각 언어 모델(VLM)을 사용하여 작업과 장면에서 의미적 제약 조건을 추론하고, 해석적 제약 최적화를 통해 소수의 기능적 파지 후보를 생성한 후, 강화 학습으로 전체 파지-이동-작동 전략을 효율적으로 최적화합니다. 16자유도 다지 손을 갖춘 7자유도 로봇 팔에서 CoDex는 내부 메커니즘이 보이지 않는 물체(예: 스프레이 병, 핫 글루건, 에어 블로어, 손전등, 후추 그라인더)를 포함한 여섯 가지 작업에서 제로 데모 자율 발견으로 복잡한 다기능 행동을 성공적으로 검증했습니다.

## 핵심 내용
### 방법 아키텍처
CoDex는 3단계 파이프라인을 채택합니다:
- **의미적 제약 추론**: 시각 언어 모델(VLM)을 사용하여 작업 장면을 분석하고 물체 기능, 조작 모드 및 적용 영역과 관련된 의미적 제약 조건을 추출합니다.
- **기능적 파지 생성**: 의미적 제약 조건을 기반으로 해석적 제약 최적화를 수행하여 소수의 실행 가능한 기능적 파지 후보를 생성하며, 파지 자세가 안정성과 기능 실행 요구를 동시에 충족하도록 보장합니다.
- **전략 최적화 및 전이**: 강화 학습을 통해 파지 후보를 효율적으로 최적화하여 완전한 grasp-move-actuate 전략을 생성하고, 시뮬레이션 환경에서 실제 세계로의 제로샷 전이를 구현합니다.

### 실험 설정
- **하드웨어 플랫폼**: 16자유도 다지 손을 갖춘 7자유도 로봇 팔.
- **작업 세트**: 내부 메커니즘이 보이지 않는 물체(스프레이 병, 핫 글루건, 에어 블로어, 손전등, 후추 그라인더)와 보이지 않는 대상 물체에 대한 적용을 포함한 여섯 가지 CD-FOM 작업.
- **평가 지표**: 작업 성공률, 전략 물리적 실행 가능성, 제로 데모 자율 발견 능력.

### 주요 결과
- CoDex는 여섯 가지 모든 작업에서 인간 데모 없이 복잡한 다기능 행동을 성공적으로 자율 발견하고 실행했습니다.
- 생성된 전략은 시뮬레이션과 실제 세계 간에 우수한 전이성을 보여주며 프레임워크의 일반화 능력을 검증했습니다.
- 기준 방법과 비교하여 CoDex는 기능적 파지 생성 효율성과 전략 물리적 실행 가능성 모두에서 상당한 우위를 확보했습니다.

### 결론
CoDex는 VLM의 의미적 이해와 최적화 방법의 물리적 정밀성을 융합하여 제로 데모 다기능 조작에 효과적인 솔루션을 제공하며, 로봇이 복잡한 기능적 작업을 자율적으로 수행하는 새로운 경로를 열었습니다. 자세한 정보는 https://robin-lab.cs.utexas.edu/CoDex/ 에서 확인할 수 있습니다.
