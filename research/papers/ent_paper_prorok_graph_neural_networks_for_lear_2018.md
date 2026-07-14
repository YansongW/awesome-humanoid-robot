---
$id: ent_paper_prorok_graph_neural_networks_for_lear_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Graph Neural Networks for Learning Robot Team Coordination
  zh: 用于学习机器人团队协调的图神经网络
  ko: 로봇 팀 조정 학습을 위한 그래프 신경망
summary:
  en: This paper applies Graph Neural Networks (GNNs) to multi-robot coordination, modeling robot teams as graphs where robots
    are nodes and communication links are edges, and learns differentiable message-passing and state-update functions to estimate
    algebraic connectivity in a supervised setting.
  zh: 本文将图神经网络（GNN）应用于多机器人协调，将机器人团队建模为图（机器人为节点、通信链路为边），并在监督学习设置中学习可微的消息传递与状态更新函数，以估计网络的代数连通性。
  ko: 본 논문은 그래프 신경망(GNN)을 다중 로봇 조정에 적용하여 로봇을 노드로, 통신 링크를 엣지로 하는 그래프로 로봇 팀을 모델링하고, 지도 학습 환경에서 대수적 연결성을 추정하기 위해 미분 가능한 메시지 전달
    및 상태 업데이트 함수를 학습한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- graph_neural_network
- multi_robot_coordination
- distributed_coordination
- message_passing
- algebraic_connectivity
- local_readout
- robot_team
- gated_graph_neural_network
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1805.03737v2.
sources:
- id: src_001
  type: paper
  title: Graph Neural Networks for Learning Robot Team Coordination
  url: https://arxiv.org/abs/1805.03737
  date: '2018'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
This paper shows how Graph Neural Networks can be used for learning distributed coordination mechanisms in connected teams of robots. We capture the relational aspect of robot coordination by modeling the robot team as a graph, where each robot is a node, and edges represent communication links. During training, robots learn how to pass messages and update internal states, so that a target behavior is reached. As a proxy for more complex problems, this short paper considers the problem where each robot must locally estimate the algebraic connectivity of the team's network topology.

## 核心内容
This paper shows how Graph Neural Networks can be used for learning distributed coordination mechanisms in connected teams of robots. We capture the relational aspect of robot coordination by modeling the robot team as a graph, where each robot is a node, and edges represent communication links. During training, robots learn how to pass messages and update internal states, so that a target behavior is reached. As a proxy for more complex problems, this short paper considers the problem where each robot must locally estimate the algebraic connectivity of the team's network topology.

## 参考
- http://arxiv.org/abs/1805.03737v2

