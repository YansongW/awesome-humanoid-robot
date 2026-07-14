---
$id: ent_paper_tang_collaborative_planar_pushing_o_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Collaborative Planar Pushing of Polytopic Objects with Multiple Robots in Complex Scenes
  zh: 多机器人在复杂场景中协同推动多面体物体
  ko: 복잡한 장면에서 다중 로봇을 이용한 다면체 객체의 협동 평면 밀기
summary:
  en: This 2024 arXiv paper proposes a hybrid optimization framework in which a team of mobile robots collaboratively pushes
    polytopic objects through cluttered environments, combining quasi-static contact-mode generation, a hierarchical hybrid
    search, and online nonlinear model predictive control.
  zh: 该2024年arXiv论文提出了一种混合优化框架，使多个移动机器人能够在障碍物密集的复杂环境中协同推动多面体物体，结合了准静态接触模式生成、分层混合搜索和在线非线性模型预测控制。
  ko: 이 2024년 arXiv 논문은 여러 이동 로봇이 장애물이 밀집된 복잡한 환경에서 다면체 객체를 협동하여 평면으로 밀 수 있도록 준정적 접촉 모드 생성, 계층적 하이브리드 검색, 온라인 비선형 모델 예측 제어를
    결합한 하이브리드 최적화 프레임워크를 제안한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.07908v2.
sources:
- id: src_001
  type: paper
  title: Collaborative Planar Pushing of Polytopic Objects with Multiple Robots in Complex Scenes
  url: https://arxiv.org/abs/2405.07908
  date: '2024'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
Pushing is a simple yet effective skill for robots to interact with and further change the environment. Related work has been mostly focused on utilizing it as a non-prehensile manipulation primitive for a robotic manipulator. However, it can also be beneficial for low-cost mobile robots that are not equipped with a manipulator. This work tackles the general problem of controlling a team of mobile robots to push collaboratively polytopic objects within complex obstacle-cluttered environments. It incorporates several characteristic challenges for contact-rich tasks such as the hybrid switching among different contact modes and under-actuation due to constrained contact forces. The proposed method is based on hybrid optimization over a sequence of possible modes and the associated pushing forces, where (i) a set of sufficient modes is generated with a multi-directional feasibility estimation, based on quasi-static analyses for general objects and any number of robots; (ii) a hierarchical hybrid search algorithm is designed to iteratively decompose the navigation path via arc segments and select the optimal parameterized mode; and (iii) a nonlinear model predictive controller is proposed to track the desired pushing velocities adaptively online for each robot. The proposed framework is complete under mild assumptions. Its efficiency and effectiveness are validated in high-fidelity simulations and hardware experiments. Robustness to motion and actuation uncertainties is also demonstrated.

## 核心内容
Pushing is a simple yet effective skill for robots to interact with and further change the environment. Related work has been mostly focused on utilizing it as a non-prehensile manipulation primitive for a robotic manipulator. However, it can also be beneficial for low-cost mobile robots that are not equipped with a manipulator. This work tackles the general problem of controlling a team of mobile robots to push collaboratively polytopic objects within complex obstacle-cluttered environments. It incorporates several characteristic challenges for contact-rich tasks such as the hybrid switching among different contact modes and under-actuation due to constrained contact forces. The proposed method is based on hybrid optimization over a sequence of possible modes and the associated pushing forces, where (i) a set of sufficient modes is generated with a multi-directional feasibility estimation, based on quasi-static analyses for general objects and any number of robots; (ii) a hierarchical hybrid search algorithm is designed to iteratively decompose the navigation path via arc segments and select the optimal parameterized mode; and (iii) a nonlinear model predictive controller is proposed to track the desired pushing velocities adaptively online for each robot. The proposed framework is complete under mild assumptions. Its efficiency and effectiveness are validated in high-fidelity simulations and hardware experiments. Robustness to motion and actuation uncertainties is also demonstrated.

## 参考
- http://arxiv.org/abs/2405.07908v2

