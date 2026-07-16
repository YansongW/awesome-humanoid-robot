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

## Overview
Pushing is a simple yet effective skill for robots to interact with and further change the environment. Related work has been mostly focused on utilizing it as a non-prehensile manipulation primitive for a robotic manipulator. However, it can also be beneficial for low-cost mobile robots that are not equipped with a manipulator. This work tackles the general problem of controlling a team of mobile robots to push collaboratively polytopic objects within complex obstacle-cluttered environments. It incorporates several characteristic challenges for contact-rich tasks such as the hybrid switching among different contact modes and under-actuation due to constrained contact forces. The proposed method is based on hybrid optimization over a sequence of possible modes and the associated pushing forces, where (i) a set of sufficient modes is generated with a multi-directional feasibility estimation, based on quasi-static analyses for general objects and any number of robots; (ii) a hierarchical hybrid search algorithm is designed to iteratively decompose the navigation path via arc segments and select the optimal parameterized mode; and (iii) a nonlinear model predictive controller is proposed to track the desired pushing velocities adaptively online for each robot. The proposed framework is complete under mild assumptions. Its efficiency and effectiveness are validated in high-fidelity simulations and hardware experiments. Robustness to motion and actuation uncertainties is also demonstrated.

## Content
Pushing is a simple yet effective skill for robots to interact with and further change the environment. Related work has been mostly focused on utilizing it as a non-prehensile manipulation primitive for a robotic manipulator. However, it can also be beneficial for low-cost mobile robots that are not equipped with a manipulator. This work tackles the general problem of controlling a team of mobile robots to push collaboratively polytopic objects within complex obstacle-cluttered environments. It incorporates several characteristic challenges for contact-rich tasks such as the hybrid switching among different contact modes and under-actuation due to constrained contact forces. The proposed method is based on hybrid optimization over a sequence of possible modes and the associated pushing forces, where (i) a set of sufficient modes is generated with a multi-directional feasibility estimation, based on quasi-static analyses for general objects and any number of robots; (ii) a hierarchical hybrid search algorithm is designed to iteratively decompose the navigation path via arc segments and select the optimal parameterized mode; and (iii) a nonlinear model predictive controller is proposed to track the desired pushing velocities adaptively online for each robot. The proposed framework is complete under mild assumptions. Its efficiency and effectiveness are validated in high-fidelity simulations and hardware experiments. Robustness to motion and actuation uncertainties is also demonstrated.

## 개요
Pushing은 로봇이 환경과 상호작용하고 더 나아가 환경을 변화시키는 간단하면서도 효과적인 기술입니다. 관련 연구는 주로 로봇 매니퓰레이터를 위한 비파지적 조작 기본 동작으로 활용하는 데 초점을 맞춰 왔습니다. 그러나 매니퓰레이터가 장착되지 않은 저비용 이동 로봇에게도 유용할 수 있습니다. 본 연구는 복잡한 장애물로 가득한 환경 내에서 이동 로봇 팀이 협력적으로 다면체 객체를 밀어내는 일반적인 문제를 다룹니다. 이는 접촉 모드 간의 하이브리드 전환 및 제한된 접촉 힘으로 인한 저구동과 같은 접촉이 많은 작업의 여러 특징적인 도전 과제를 포함합니다. 제안된 방법은 가능한 모드 시퀀스와 관련된 밀기 힘에 대한 하이브리드 최적화를 기반으로 하며, (i) 일반 객체와 임의의 로봇 수에 대한 준정적 분석을 기반으로 다방향 타당성 추정을 통해 충분한 모드 집합을 생성하고, (ii) 호 세그먼트를 통해 내비게이션 경로를 반복적으로 분해하고 최적의 매개변수화된 모드를 선택하는 계층적 하이브리드 검색 알고리즘을 설계하며, (iii) 각 로봇이 온라인에서 적응적으로 원하는 밀기 속도를 추적하는 비선형 모델 예측 제어기를 제안합니다. 제안된 프레임워크는 약한 가정 하에서 완전성을 갖습니다. 그 효율성과 효과성은 고충실도 시뮬레이션과 하드웨어 실험을 통해 검증되었습니다. 또한 운동 및 작동 불확실성에 대한 강건성도 입증되었습니다.

## 핵심 내용
Pushing은 로봇이 환경과 상호작용하고 더 나아가 환경을 변화시키는 간단하면서도 효과적인 기술입니다. 관련 연구는 주로 로봇 매니퓰레이터를 위한 비파지적 조작 기본 동작으로 활용하는 데 초점을 맞춰 왔습니다. 그러나 매니퓰레이터가 장착되지 않은 저비용 이동 로봇에게도 유용할 수 있습니다. 본 연구는 복잡한 장애물로 가득한 환경 내에서 이동 로봇 팀이 협력적으로 다면체 객체를 밀어내는 일반적인 문제를 다룹니다. 이는 접촉 모드 간의 하이브리드 전환 및 제한된 접촉 힘으로 인한 저구동과 같은 접촉이 많은 작업의 여러 특징적인 도전 과제를 포함합니다. 제안된 방법은 가능한 모드 시퀀스와 관련된 밀기 힘에 대한 하이브리드 최적화를 기반으로 하며, (i) 일반 객체와 임의의 로봇 수에 대한 준정적 분석을 기반으로 다방향 타당성 추정을 통해 충분한 모드 집합을 생성하고, (ii) 호 세그먼트를 통해 내비게이션 경로를 반복적으로 분해하고 최적의 매개변수화된 모드를 선택하는 계층적 하이브리드 검색 알고리즘을 설계하며, (iii) 각 로봇이 온라인에서 적응적으로 원하는 밀기 속도를 추적하는 비선형 모델 예측 제어기를 제안합니다. 제안된 프레임워크는 약한 가정 하에서 완전성을 갖습니다. 그 효율성과 효과성은 고충실도 시뮬레이션과 하드웨어 실험을 통해 검증되었습니다. 또한 운동 및 작동 불확실성에 대한 강건성도 입증되었습니다.
