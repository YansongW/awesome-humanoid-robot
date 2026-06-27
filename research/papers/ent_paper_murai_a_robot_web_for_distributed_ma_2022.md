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
  en: We show that a distributed network of robots or devices can collaboratively
    estimate global poses by running Gaussian Belief Propagation on the non-linear
    factor graph formed by internal and inter-robot measurements, using only asynchronous
    peer-to-peer communication.
  zh: 我们展示了一个分布式的机器人或设备网络可以通过在由内部和机间测量构成的非线性因子图上运行高斯置信传播，仅利用异步点对点通信协同估计全局位姿。
  ko: 우리는 로봇 또는 장치의 분산 네트워크가 내부 및 상호 측정으로 구성된 비선형 팩터 그래프에서 가우시안 신뢰 전파를 실행하여 비동기 피어
    투 피어 통신만으로 전역 포즈를 협력적으로 추정할 수 있음을 보여준다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; full-text review is
    required before final verification.
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

## Overview

The paper proposes the Robot Web, a decentralised approach to global localisation for large numbers of robots or other devices. Each device maintains a fragment of a shared non-linear factor graph and runs Gaussian Belief Propagation (GBP) locally. Devices exchange compact marginal messages over an asynchronous, web-like publish/read protocol, removing the need for a central server or all-to-all broadcasts.

The authors extend GBP to support inference on Lie Groups so that the framework can handle practical pose-estimation problems. Robust factors are incorporated to tolerate outlier measurements and packet drops. The system is evaluated in simulation with up to 1,000 robots and on a real fleet of nine TurtleBot3 robots running Raspberry Pi 3B+ computers, demonstrating comparable accuracy to a centralised GTSAM solver.

## Key Contributions

- A distributed, scalable GBP-based localisation system that handles thousands of robots, asynchronous communication, message loss, dynamic topology changes, and a high fraction of outlier measurements.
- A general framework for distributed multi-robot inference with a novel extension of GBP to support Lie Groups for practical pose estimation.
- Extensive simulation evaluation comparing distributed GBP against a centralised GTSAM solver across robot count, sensor noise, and communication conditions.
- Real-time experiments on nine TurtleBot3 robots running entirely on limited onboard computational resources.

## Relevance to Humanoid Robotics

The Robot Web provides a decentralised state-estimation layer that could support fleets of humanoid robots operating without centralised cloud infrastructure. Its peer-to-peer protocol and tolerance to dropped packets and outlier measurements are directly relevant to robust, scalable coordination of humanoids in dynamic environments. By distributing computation across devices, the method aligns with the onboard resource constraints typical of mobile humanoid platforms.
