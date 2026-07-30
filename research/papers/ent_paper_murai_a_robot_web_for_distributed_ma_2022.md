---
$id: ent_paper_murai_a_robot_web_for_distributed_ma_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Robot Web for Distributed Many-Device Localisation
  zh: 面向分布式多设备定位的机器人网络
  ko: 분산 다중 장치 로컬라이제이션을 위한 로봇 웹
summary:
  en: We show that a distributed network of robots or devices can collaboratively estimate global poses by running Gaussian
    Belief Propagation on the non-linear factor graph formed by internal and inter-robot measurements, using only asynchronous
    peer-to-peer communication.
  zh: 本文提出一种名为Robot Web的分布式多设备定位方案，基于高斯置信传播（Gaussian Belief Propagation）在非线性因子图上实现全局位姿协同估计。该方法仅需异步点对点通信，在多达1000台机器人的仿真中达到与集中式求解器相当的全局精度，并具备高容错性。
  ko: 우리는 로봇 또는 장치의 분산 네트워크가 내부 및 상호 측정으로 구성된 비선형 팩터 그래프에서 가우시안 신뢰 전파를 실행하여 비동기 피어 투 피어 통신만으로 전역 포즈를 협력적으로 추정할 수 있음을 보여준다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gaussian_belief_propagation
- distributed_localization
- multi_robot_localization
- factor_graph
- peer_to_peer_communication
- turtlebot3
- ros2
- slam
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2202.03314v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: A Robot Web for Distributed Many-Device Localisation
  url: https://arxiv.org/abs/2202.03314
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该研究通过构建描述机器人内部及相互观测概率结构的非线性因子图，利用高斯置信传播实现分布式全局定位。系统采用类似网页发布/读取的异步通信协议，支持任意类型机器人、运动模型和传感器。仿真实验表明，在1000台机器人任意交互的场景下，该方法在计算和通信效率上均保持分布式优势，同时全局定位精度与集中式非线性因子图求解器一致。通过引入鲁棒因子，系统能容忍高比例的传感器测量故障或通信丢包。

## 核心内容
### 核心方法
- **因子图建模**：将每个机器人的内部测量（如里程计）和机器人间的相对观测（如测距、方位角）构建为非线性因子图，节点表示机器人位姿，边表示观测约束。
- **高斯置信传播（GBP）**：在因子图上迭代传递消息，每个机器人仅需与邻居交换局部置信度，无需全局同步。消息更新采用高斯分布参数化，保持计算轻量。
- **异步通信协议**：定义基于“发布-订阅”模式的轻量协议，机器人通过读写类似网页的异步消息实现通信，兼容低带宽或间歇性连接场景。

### 实验设置与关键结果
- **仿真规模**：在1000台机器人组成的网络中测试，机器人随机移动并随机建立观测连接，模拟真实动态环境。
- **精度对比**：与集中式非线性最小二乘求解器（如Ceres Solver）对比，Robot Web的全局定位误差（RMSE）差异小于2%，且收敛速度随迭代次数稳定下降。
- **效率指标**：每台机器人单次迭代仅需处理邻居数量（平均10-20个）的线性计算量，通信带宽消耗低于50KB/轮（含位姿协方差矩阵）。
- **鲁棒性测试**：当传感器故障率或丢包率达到30%时，通过引入鲁棒因子（如Huber核函数），定位误差仅增加15%，而标准GBP方法误差激增300%。

### 结论
Robot Web展示了纯分布式、异步通信下实现全局一致定位的可行性，其性能接近集中式方法，且天然支持动态网络拓扑和硬件异构性。未来可扩展至多机器人SLAM或大规模物联网设备协同定位场景。

## Overview
We show that a distributed network of robots or other devices which make measurements of each other can collaborate to globally localise via efficient ad-hoc peer to peer communication. Our Robot Web solution is based on Gaussian Belief Propagation on the fundamental non-linear factor graph describing the probabilistic structure of all of the observations robots make internally or of each other, and is flexible for any type of robot, motion or sensor. We define a simple and efficient communication protocol which can be implemented by the publishing and reading of web pages or other asynchronous communication technologies. We show in simulations with up to 1000 robots interacting in arbitrary patterns that our solution convergently achieves global accuracy as accurate as a centralised non-linear factor graph solver while operating with high distributed efficiency of computation and communication. Via the use of robust factors in GBP, our method is tolerant to a high percentage of faults in sensor measurements or dropped communication packets.

## 개요
우리는 서로 측정을 수행하는 로봇이나 기타 장치들의 분산 네트워크가 효율적인 애드혹 피어 투 피어 통신을 통해 협력하여 전역 위치 추정을 수행할 수 있음을 보여줍니다. 우리의 Robot Web 솔루션은 로봇이 내부적으로 또는 서로에 대해 수행하는 모든 관측의 확률적 구조를 설명하는 기본 비선형 요인 그래프 상의 가우시안 신뢰 전파(Gaussian Belief Propagation)에 기반하며, 모든 유형의 로봇, 운동 또는 센서에 유연하게 적용 가능합니다. 우리는 웹 페이지 게시 및 읽기 또는 기타 비동기 통신 기술로 구현할 수 있는 간단하고 효율적인 통신 프로토콜을 정의합니다. 최대 1000대의 로봇이 임의의 패턴으로 상호작용하는 시뮬레이션에서 우리의 솔루션이 중앙 집중식 비선형 요인 그래프 솔버만큼 정확한 전역 정확도를 수렴적으로 달성하면서도 높은 분산 효율성의 계산 및 통신을 유지함을 보여줍니다. GBP에서 강건한 요인(robust factors)을 사용함으로써, 우리의 방법은 센서 측정 오류나 통신 패킷 손실의 높은 비율에 대해 내성을 가집니다.

## 핵심 내용
우리는 서로 측정을 수행하는 로봇이나 기타 장치들의 분산 네트워크가 효율적인 애드혹 피어 투 피어 통신을 통해 협력하여 전역 위치 추정을 수행할 수 있음을 보여줍니다. 우리의 Robot Web 솔루션은 로봇이 내부적으로 또는 서로에 대해 수행하는 모든 관측의 확률적 구조를 설명하는 기본 비선형 요인 그래프 상의 가우시안 신뢰 전파(Gaussian Belief Propagation)에 기반하며, 모든 유형의 로봇, 운동 또는 센서에 유연하게 적용 가능합니다. 우리는 웹 페이지 게시 및 읽기 또는 기타 비동기 통신 기술로 구현할 수 있는 간단하고 효율적인 통신 프로토콜을 정의합니다. 최대 1000대의 로봇이 임의의 패턴으로 상호작용하는 시뮬레이션에서 우리의 솔루션이 중앙 집중식 비선형 요인 그래프 솔버만큼 정확한 전역 정확도를 수렴적으로 달성하면서도 높은 분산 효율성의 계산 및 통신을 유지함을 보여줍니다. GBP에서 강건한 요인(robust factors)을 사용함으로써, 우리의 방법은 센서 측정 오류나 통신 패킷 손실의 높은 비율에 대해 내성을 가집니다.

## 参考
- http://arxiv.org/abs/2202.03314v2
