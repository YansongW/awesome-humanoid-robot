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
  zh: We show that a distributed network of robots or other devices which make measurements of each other can collaborate
    to globally localise via efficient ad-hoc peer to peer communication. Our Robot Web solution is based on Gaussian Belief
    Propagation on the fundamental non-linear factor graph describing the probabilistic structure of all of the observations
    robots make internally or of each other, and is flexible for any type of robot, motion or sensor. We define a simple and
    efficient communication protocol which can be implemented by the publishing and reading of web pages or other asynchronou
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2202.03314v2.
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
We show that a distributed network of robots or other devices which make measurements of each other can collaborate to globally localise via efficient ad-hoc peer to peer communication. Our Robot Web solution is based on Gaussian Belief Propagation on the fundamental non-linear factor graph describing the probabilistic structure of all of the observations robots make internally or of each other, and is flexible for any type of robot, motion or sensor. We define a simple and efficient communication protocol which can be implemented by the publishing and reading of web pages or other asynchronous communication technologies. We show in simulations with up to 1000 robots interacting in arbitrary patterns that our solution convergently achieves global accuracy as accurate as a centralised non-linear factor graph solver while operating with high distributed efficiency of computation and communication. Via the use of robust factors in GBP, our method is tolerant to a high percentage of faults in sensor measurements or dropped communication packets.

## 核心内容
We show that a distributed network of robots or other devices which make measurements of each other can collaborate to globally localise via efficient ad-hoc peer to peer communication. Our Robot Web solution is based on Gaussian Belief Propagation on the fundamental non-linear factor graph describing the probabilistic structure of all of the observations robots make internally or of each other, and is flexible for any type of robot, motion or sensor. We define a simple and efficient communication protocol which can be implemented by the publishing and reading of web pages or other asynchronous communication technologies. We show in simulations with up to 1000 robots interacting in arbitrary patterns that our solution convergently achieves global accuracy as accurate as a centralised non-linear factor graph solver while operating with high distributed efficiency of computation and communication. Via the use of robust factors in GBP, our method is tolerant to a high percentage of faults in sensor measurements or dropped communication packets.

## 参考
- http://arxiv.org/abs/2202.03314v2

## Overview
We show that a distributed network of robots or other devices which make measurements of each other can collaborate to globally localise via efficient ad-hoc peer to peer communication. Our Robot Web solution is based on Gaussian Belief Propagation on the fundamental non-linear factor graph describing the probabilistic structure of all of the observations robots make internally or of each other, and is flexible for any type of robot, motion or sensor. We define a simple and efficient communication protocol which can be implemented by the publishing and reading of web pages or other asynchronous communication technologies. We show in simulations with up to 1000 robots interacting in arbitrary patterns that our solution convergently achieves global accuracy as accurate as a centralised non-linear factor graph solver while operating with high distributed efficiency of computation and communication. Via the use of robust factors in GBP, our method is tolerant to a high percentage of faults in sensor measurements or dropped communication packets.

## Content
We show that a distributed network of robots or other devices which make measurements of each other can collaborate to globally localise via efficient ad-hoc peer to peer communication. Our Robot Web solution is based on Gaussian Belief Propagation on the fundamental non-linear factor graph describing the probabilistic structure of all of the observations robots make internally or of each other, and is flexible for any type of robot, motion or sensor. We define a simple and efficient communication protocol which can be implemented by the publishing and reading of web pages or other asynchronous communication technologies. We show in simulations with up to 1000 robots interacting in arbitrary patterns that our solution convergently achieves global accuracy as accurate as a centralised non-linear factor graph solver while operating with high distributed efficiency of computation and communication. Via the use of robust factors in GBP, our method is tolerant to a high percentage of faults in sensor measurements or dropped communication packets.

## 개요
우리는 서로 측정을 수행하는 로봇이나 기타 장치들의 분산 네트워크가 효율적인 애드혹 피어 투 피어 통신을 통해 협력하여 전역 위치 추정을 수행할 수 있음을 보여줍니다. 우리의 Robot Web 솔루션은 로봇이 내부적으로 또는 서로에 대해 수행하는 모든 관측의 확률적 구조를 설명하는 기본 비선형 요인 그래프 상의 가우시안 신뢰 전파(Gaussian Belief Propagation)에 기반하며, 모든 유형의 로봇, 운동 또는 센서에 유연하게 적용 가능합니다. 우리는 웹 페이지 게시 및 읽기 또는 기타 비동기 통신 기술로 구현할 수 있는 간단하고 효율적인 통신 프로토콜을 정의합니다. 최대 1000대의 로봇이 임의의 패턴으로 상호작용하는 시뮬레이션에서 우리의 솔루션이 중앙 집중식 비선형 요인 그래프 솔버만큼 정확한 전역 정확도를 수렴적으로 달성하면서도 높은 분산 효율성의 계산 및 통신을 유지함을 보여줍니다. GBP에서 강건한 요인(robust factors)을 사용함으로써, 우리의 방법은 센서 측정 오류나 통신 패킷 손실의 높은 비율에 대해 내성을 가집니다.

## 핵심 내용
우리는 서로 측정을 수행하는 로봇이나 기타 장치들의 분산 네트워크가 효율적인 애드혹 피어 투 피어 통신을 통해 협력하여 전역 위치 추정을 수행할 수 있음을 보여줍니다. 우리의 Robot Web 솔루션은 로봇이 내부적으로 또는 서로에 대해 수행하는 모든 관측의 확률적 구조를 설명하는 기본 비선형 요인 그래프 상의 가우시안 신뢰 전파(Gaussian Belief Propagation)에 기반하며, 모든 유형의 로봇, 운동 또는 센서에 유연하게 적용 가능합니다. 우리는 웹 페이지 게시 및 읽기 또는 기타 비동기 통신 기술로 구현할 수 있는 간단하고 효율적인 통신 프로토콜을 정의합니다. 최대 1000대의 로봇이 임의의 패턴으로 상호작용하는 시뮬레이션에서 우리의 솔루션이 중앙 집중식 비선형 요인 그래프 솔버만큼 정확한 전역 정확도를 수렴적으로 달성하면서도 높은 분산 효율성의 계산 및 통신을 유지함을 보여줍니다. GBP에서 강건한 요인(robust factors)을 사용함으로써, 우리의 방법은 센서 측정 오류나 통신 패킷 손실의 높은 비율에 대해 내성을 가집니다.
