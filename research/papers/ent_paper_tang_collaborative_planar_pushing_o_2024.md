---
$id: ent_paper_tang_collaborative_planar_pushing_o_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Collaborative Planar Pushing of Polytopic Objects with Multiple Robots in Complex
    Scenes
  zh: 多机器人在复杂场景中协同推动多面体物体
  ko: 복잡한 장면에서 다중 로봇을 이용한 다면체 객체의 협동 평면 밀기
summary:
  en: This 2024 arXiv paper proposes a hybrid optimization framework in which a team
    of mobile robots collaboratively pushes polytopic objects through cluttered environments,
    combining quasi-static contact-mode generation, a hierarchical hybrid search,
    and online nonlinear model predictive control.
  zh: 该2024年arXiv论文提出了一种混合优化框架，使多个移动机器人能够在障碍物密集的复杂环境中协同推动多面体物体，结合了准静态接触模式生成、分层混合搜索和在线非线性模型预测控制。
  ko: 이 2024년 arXiv 논문은 여러 이동 로봇이 장애물이 밀집된 복잡한 환경에서 다면체 객체를 협동하여 평면으로 밀 수 있도록 준정적
    접촉 모드 생성, 계층적 하이브리드 검색, 온라인 비선형 모델 예측 제어를 결합한 하이브리드 최적화 프레임워크를 제안한다.
domains:
- 07_ai_models_algorithms
- 03_manufacturing_processes
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- multi_robot_pushing
- contact_mode_planning
- hybrid_optimization
- non_prehensile_manipulation
- quasi_static_analysis
- nonlinear_model_predictive_control
- planar_pushing
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the supplied metadata and abstract; full text was not independently
    consulted, so section-level citations are approximate.
sources:
- id: src_001
  type: paper
  title: Collaborative Planar Pushing of Polytopic Objects with Multiple Robots in
    Complex Scenes
  url: https://arxiv.org/abs/2405.07908
  date: '2024'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

The paper addresses collaborative planar pushing: controlling a group of mobile robots to transport general polytopic objects through obstacle-cluttered environments to a desired goal. Unlike prior work that treats pushing mainly as a single-arm non-prehensile manipulation primitive, this study focuses on low-cost mobile robots that lack manipulators and must coordinate contact forces to move large or bulky objects. The proposed approach is built around hybrid optimization over a sequence of contact modes and the corresponding pushing forces.

The framework consists of three coupled stages. First, a set of sufficient contact modes is generated through multi-directional feasibility estimation based on quasi-static analyses; this step is formulated as a sparse linear program and is applicable to general polygonal objects and any number of robots. Second, a hierarchical hybrid-search algorithm decomposes the desired navigation path into arc segments and selects the optimal parameterized mode at each step, avoiding the need for pre-defined contact modes. Third, a nonlinear model predictive controller tracks the planned pushing velocities online for each robot, with event-triggered re-planning to handle uncertainty and robot failures. The authors state completeness guarantees under mild assumptions and validate the method in both high-fidelity simulations and hardware experiments.

## Key Contributions

- A hierarchical hybrid-search algorithm for multi-robot planar pushing of general polytopic objects without pre-defined contact modes.
- Theoretical feasibility and completeness guarantees for arbitrary numbers of robots, any polytopic object shape, and any desired object trajectory.
- Sparse linear-program-based contact-mode generation using multi-directional quasi-static feasibility estimation.
- Online nonlinear model predictive control for pushing-velocity tracking, with event-triggered re-planning to improve robustness against uncertainty and individual robot failures.

## Relevance to Humanoid Robotics

Although the work studies wheeled mobile robots rather than humanoids, the underlying problems—contact-mode planning, multi-agent coordination, constrained contact forces, and robust online control—are directly relevant to humanoid production floors and warehouses. Humanoid or mobile manipulator fleets can adapt the same contact-mode generation and hybrid-search ideas when collaboratively transporting bulky workpieces through cluttered spaces. The NMPC-based velocity-tracking and event-triggered re-planning strategies also transfer to balancing, stepping, and pushing tasks in humanoid systems where real-time reaction to disturbances is essential.
