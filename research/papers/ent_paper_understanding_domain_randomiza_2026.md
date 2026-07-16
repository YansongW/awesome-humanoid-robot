---
$id: ent_paper_understanding_domain_randomiza_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Understanding Domain Randomization for Sim-to-real Transfer
  zh: Understanding Domain Randomization for Sim-to-real Transfer
  ko: Understanding Domain Randomization for Sim-to-real Transfer
summary:
  en: Reinforcement learning encounters many challenges when applied directly in the real world. Sim-to-real transfer is widely
    used to transfer the knowledge learned from simulation to the real world. Domain randomization -- one of the most popular
    algorithms for sim-to-real transfer -- has been demonstrated to be effective in various tasks in robotics and autonomous
    driving. Despite its empirical successes, theoretical understanding on why this simple algorithm works is limited. In
    this paper, we propose a theoretical framework for sim-to-real transfers, in which the simulator is modeled as a set of
    MDPs with tunable parameters (corresponding to unknown physical parameters such as friction). We provide sharp bounds
    on the sim-to-real gap -- the difference between the value of policy returned b
  zh: Understanding Domain Randomization for Sim-to-real Transfer is a paper on 仿真到现实 for humanoid robotics.
  ko: Understanding Domain Randomization for Sim-to-real Transfer is a paper on 仿真到现实 for humanoid robotics.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- foundation
- humanoid
- reinforcement_learning
- understanding_domain_randomiza
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: Understanding Domain Randomization
    for Sim-to-real Transfer.'
sources:
- id: src_001
  type: website
  title: Understanding Domain Randomization for Sim-to-real Transfer
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning encounters many challenges when applied directly in the real world. Sim-to-real transfer is widely used to transfer the knowledge learned from simulation to the real world. Domain randomization -- one of the most popular algorithms for sim-to-real transfer -- has been demonstrated to be effective in various tasks in robotics and autonomous driving. Despite its empirical successes, theoretical understanding on why this simple algorithm works is limited. In this paper, we propose a theoretical framework for sim-to-real transfers, in which the simulator is modeled as a set of MDPs with tunable parameters (corresponding to unknown physical parameters such as friction). We provide sharp bounds on the sim-to-real gap -- the difference between the value of policy returned by domain randomization and the value of an optimal policy for the real world. We prove that sim-to-real transfer can succeed under mild conditions without any real-world training samples. Our theory also highlights the importance of using memory (i.e., history-dependent policies) in domain randomization. Our proof is based on novel techniques that reduce the problem of bounding the sim-to-real gap to the problem of designing efficient learning algorithms for infinite-horizon MDPs, which we believe are of independent interest.

## 核心内容
Reinforcement learning encounters many challenges when applied directly in the real world. Sim-to-real transfer is widely used to transfer the knowledge learned from simulation to the real world. Domain randomization -- one of the most popular algorithms for sim-to-real transfer -- has been demonstrated to be effective in various tasks in robotics and autonomous driving. Despite its empirical successes, theoretical understanding on why this simple algorithm works is limited. In this paper, we propose a theoretical framework for sim-to-real transfers, in which the simulator is modeled as a set of MDPs with tunable parameters (corresponding to unknown physical parameters such as friction). We provide sharp bounds on the sim-to-real gap -- the difference between the value of policy returned by domain randomization and the value of an optimal policy for the real world. We prove that sim-to-real transfer can succeed under mild conditions without any real-world training samples. Our theory also highlights the importance of using memory (i.e., history-dependent policies) in domain randomization. Our proof is based on novel techniques that reduce the problem of bounding the sim-to-real gap to the problem of designing efficient learning algorithms for infinite-horizon MDPs, which we believe are of independent interest.

## 参考
- Semantic Scholar search: Understanding Domain Randomization for Sim-to-real Transfer

## Overview
Reinforcement learning encounters many challenges when applied directly in the real world. Sim-to-real transfer is widely used to transfer the knowledge learned from simulation to the real world. Domain randomization -- one of the most popular algorithms for sim-to-real transfer -- has been demonstrated to be effective in various tasks in robotics and autonomous driving. Despite its empirical successes, theoretical understanding on why this simple algorithm works is limited. In this paper, we propose a theoretical framework for sim-to-real transfers, in which the simulator is modeled as a set of MDPs with tunable parameters (corresponding to unknown physical parameters such as friction). We provide sharp bounds on the sim-to-real gap -- the difference between the value of policy returned by domain randomization and the value of an optimal policy for the real world. We prove that sim-to-real transfer can succeed under mild conditions without any real-world training samples. Our theory also highlights the importance of using memory (i.e., history-dependent policies) in domain randomization. Our proof is based on novel techniques that reduce the problem of bounding the sim-to-real gap to the problem of designing efficient learning algorithms for infinite-horizon MDPs, which we believe are of independent interest.

## Content
Reinforcement learning encounters many challenges when applied directly in the real world. Sim-to-real transfer is widely used to transfer the knowledge learned from simulation to the real world. Domain randomization -- one of the most popular algorithms for sim-to-real transfer -- has been demonstrated to be effective in various tasks in robotics and autonomous driving. Despite its empirical successes, theoretical understanding on why this simple algorithm works is limited. In this paper, we propose a theoretical framework for sim-to-real transfers, in which the simulator is modeled as a set of MDPs with tunable parameters (corresponding to unknown physical parameters such as friction). We provide sharp bounds on the sim-to-real gap -- the difference between the value of policy returned by domain randomization and the value of an optimal policy for the real world. We prove that sim-to-real transfer can succeed under mild conditions without any real-world training samples. Our theory also highlights the importance of using memory (i.e., history-dependent policies) in domain randomization. Our proof is based on novel techniques that reduce the problem of bounding the sim-to-real gap to the problem of designing efficient learning algorithms for infinite-horizon MDPs, which we believe are of independent interest.

## 개요
강화 학습은 실제 세계에 직접 적용될 때 많은 도전에 직면합니다. 시뮬레이션에서 실제 세계로의 전환(Sim-to-real transfer)은 시뮬레이션에서 학습된 지식을 실제 세계로 전이하는 데 널리 사용됩니다. 도메인 무작위화(Domain randomization)는 시뮬레이션-실제 전환을 위한 가장 인기 있는 알고리즘 중 하나로, 로봇 공학 및 자율 주행의 다양한 작업에서 효과적임이 입증되었습니다. 경험적 성공에도 불구하고, 이 간단한 알고리즘이 작동하는 이유에 대한 이론적 이해는 제한적입니다. 본 논문에서는 시뮬레이터를 조정 가능한 매개변수(마찰과 같은 알려지지 않은 물리적 매개변수에 해당)를 가진 MDP 집합으로 모델링하는 시뮬레이션-실제 전환을 위한 이론적 프레임워크를 제안합니다. 우리는 도메인 무작위화에 의해 반환된 정책의 가치와 실제 세계를 위한 최적 정책의 가치 간의 차이인 시뮬레이션-실제 격차(Sim-to-real gap)에 대한 명확한 경계를 제공합니다. 우리는 실제 세계 훈련 샘플 없이도 완화된 조건에서 시뮬레이션-실제 전환이 성공할 수 있음을 증명합니다. 또한 우리의 이론은 도메인 무작위화에서 메모리(즉, 이력 의존적 정책) 사용의 중요성을 강조합니다. 증명은 시뮬레이션-실제 격차를 제한하는 문제를 무한 지평 MDP를 위한 효율적인 학습 알고리즘 설계 문제로 축소하는 새로운 기술에 기반하며, 이는 독립적인 관심을 가질 만하다고 믿습니다.

## 핵심 내용
강화 학습은 실제 세계에 직접 적용될 때 많은 도전에 직면합니다. 시뮬레이션에서 실제 세계로의 전환(Sim-to-real transfer)은 시뮬레이션에서 학습된 지식을 실제 세계로 전이하는 데 널리 사용됩니다. 도메인 무작위화(Domain randomization)는 시뮬레이션-실제 전환을 위한 가장 인기 있는 알고리즘 중 하나로, 로봇 공학 및 자율 주행의 다양한 작업에서 효과적임이 입증되었습니다. 경험적 성공에도 불구하고, 이 간단한 알고리즘이 작동하는 이유에 대한 이론적 이해는 제한적입니다. 본 논문에서는 시뮬레이터를 조정 가능한 매개변수(마찰과 같은 알려지지 않은 물리적 매개변수에 해당)를 가진 MDP 집합으로 모델링하는 시뮬레이션-실제 전환을 위한 이론적 프레임워크를 제안합니다. 우리는 도메인 무작위화에 의해 반환된 정책의 가치와 실제 세계를 위한 최적 정책의 가치 간의 차이인 시뮬레이션-실제 격차(Sim-to-real gap)에 대한 명확한 경계를 제공합니다. 우리는 실제 세계 훈련 샘플 없이도 완화된 조건에서 시뮬레이션-실제 전환이 성공할 수 있음을 증명합니다. 또한 우리의 이론은 도메인 무작위화에서 메모리(즉, 이력 의존적 정책) 사용의 중요성을 강조합니다. 증명은 시뮬레이션-실제 격차를 제한하는 문제를 무한 지평 MDP를 위한 효율적인 학습 알고리즘 설계 문제로 축소하는 새로운 기술에 기반하며, 이는 독립적인 관심을 가질 만하다고 믿습니다.
