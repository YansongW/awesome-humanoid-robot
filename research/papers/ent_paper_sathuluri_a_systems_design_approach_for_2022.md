---
$id: ent_paper_sathuluri_a_systems_design_approach_for_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A systems design approach for the co-design of a humanoid robot arm
  zh: 一种用于人形机器人手臂协同设计的系统设计方法
  ko: 휴머노이드 로봇 팔의 공동 설계를 위한 시스템 설계 접근법
summary:
  en: This paper proposes a top-down, V-model-based co-design methodology for a humanoid robot arm, using an attribute dependency
    graph and optimization to construct a maximum-permissible solution space of design variables and to decompose high-level
    requirements into tolerance-aware subsystem requirements.
  zh: Classically, the development of humanoid robots has been sequential and iterative. Such bottom-up design procedures
    rely heavily on intuition and are often biased by the designer's experience. Exploiting the non-linear coupled design
    space of robots is non-trivial and requires a systematic procedure for exploration. We adopt the top-down design strategy,
    the V-model, used in automotive and aerospace industries. Our co-design approach identifies non-intuitive designs from
    within the design space and obtains the maximum permissible range of the design variables as a solution space, to physically
  ko: 본 논문은 V 모델 기반의 상향식 공동 설계 방법론을 제시하여 휴머노이드 로봇 팔의 설계 변수에 대한 최대 허용 솔루션 공간을 구축하고, 상위 요구사항을 허용 오차가 있는 하위 시스템 수준 요구사항으로 분해한다.
domains:
- 06_design_engineering
- 02_components
- 05_mass_production
layers:
- midstream
- upstream
functional_roles:
- knowledge
- system
tags:
- humanoid_robot_arm
- co_design
- v_model
- solution_space
- design_space_exploration
- systems_design
- sim_to_real
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.14256v1.
sources:
- id: src_001
  type: paper
  title: A systems design approach for the co-design of a humanoid robot arm
  url: https://arxiv.org/abs/2212.14256
  date: '2022'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## 概述
Classically, the development of humanoid robots has been sequential and iterative. Such bottom-up design procedures rely heavily on intuition and are often biased by the designer's experience. Exploiting the non-linear coupled design space of robots is non-trivial and requires a systematic procedure for exploration. We adopt the top-down design strategy, the V-model, used in automotive and aerospace industries. Our co-design approach identifies non-intuitive designs from within the design space and obtains the maximum permissible range of the design variables as a solution space, to physically realise the obtained design. We show that by constructing the solution space, one can (1) decompose higher-level requirements onto sub-system-level requirements with tolerance, alleviating the "chicken-or-egg" problem during the design process, (2) decouple the robot's morphology from its controller, enabling greater design flexibility, (3) obtain independent sub-system level requirements, reducing the development time by parallelising the development process.

## 核心内容
Classically, the development of humanoid robots has been sequential and iterative. Such bottom-up design procedures rely heavily on intuition and are often biased by the designer's experience. Exploiting the non-linear coupled design space of robots is non-trivial and requires a systematic procedure for exploration. We adopt the top-down design strategy, the V-model, used in automotive and aerospace industries. Our co-design approach identifies non-intuitive designs from within the design space and obtains the maximum permissible range of the design variables as a solution space, to physically realise the obtained design. We show that by constructing the solution space, one can (1) decompose higher-level requirements onto sub-system-level requirements with tolerance, alleviating the "chicken-or-egg" problem during the design process, (2) decouple the robot's morphology from its controller, enabling greater design flexibility, (3) obtain independent sub-system level requirements, reducing the development time by parallelising the development process.

## 参考
- http://arxiv.org/abs/2212.14256v1


