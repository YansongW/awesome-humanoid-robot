---
$id: ent_paper_rma_rapid_motor_adaptation_for_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RMA: Rapid Motor Adaptation for Legged Robots'
  zh: 'RMA: Rapid Motor Adaptation for Legged Robots'
  ko: 'RMA: Rapid Motor Adaptation for Legged Robots'
summary:
  en: 'Successful real-world deployment of legged robots would require them to adapt in real-time to unseen scenarios like
    changing terrains, changing payloads, wear and tear. This paper presents Rapid Motor Adaptation (RMA) algorithm to solve
    this problem of real-time online adaptation in quadruped robots. RMA consists of two components: a base policy and an
    adaptation module. The combination of these components enables the robot to adapt to novel situations in fractions of
    a second. RMA is trained completely in simulation without using any domain knowledge like reference trajectories or predefined
    foot trajectory generators and is deployed on the A1 robot without any fine-tuning. We train RMA on a varied terrain generator
    using bioenergetics-inspired rewards and deploy it on a variety of diffic'
  zh: 'RMA: Rapid Motor Adaptation for Legged Robots is a paper on 仿真到真实 for humanoid robotics.'
  ko: 'RMA: Rapid Motor Adaptation for Legged Robots is a paper on 仿真到真实 for humanoid robotics.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- rma
- sim_to_real
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: RMA: Rapid Motor Adaptation
    for Legged Robots.'
sources:
- id: src_001
  type: website
  title: 'RMA: Rapid Motor Adaptation for Legged Robots'
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Successful real-world deployment of legged robots would require them to adapt in real-time to unseen scenarios like changing terrains, changing payloads, wear and tear. This paper presents Rapid Motor Adaptation (RMA) algorithm to solve this problem of real-time online adaptation in quadruped robots. RMA consists of two components: a base policy and an adaptation module. The combination of these components enables the robot to adapt to novel situations in fractions of a second. RMA is trained completely in simulation without using any domain knowledge like reference trajectories or predefined foot trajectory generators and is deployed on the A1 robot without any fine-tuning. We train RMA on a varied terrain generator using bioenergetics-inspired rewards and deploy it on a variety of difficult terrains including rocky, slippery, deformable surfaces in environments with grass, long vegetation, concrete, pebbles, stairs, sand, etc. RMA shows state-of-the-art performance across diverse real-world as well as simulation experiments. Video results at https://ashish-kmr.github.io/rma-legged-robots/

## 核心内容
Successful real-world deployment of legged robots would require them to adapt in real-time to unseen scenarios like changing terrains, changing payloads, wear and tear. This paper presents Rapid Motor Adaptation (RMA) algorithm to solve this problem of real-time online adaptation in quadruped robots. RMA consists of two components: a base policy and an adaptation module. The combination of these components enables the robot to adapt to novel situations in fractions of a second. RMA is trained completely in simulation without using any domain knowledge like reference trajectories or predefined foot trajectory generators and is deployed on the A1 robot without any fine-tuning. We train RMA on a varied terrain generator using bioenergetics-inspired rewards and deploy it on a variety of difficult terrains including rocky, slippery, deformable surfaces in environments with grass, long vegetation, concrete, pebbles, stairs, sand, etc. RMA shows state-of-the-art performance across diverse real-world as well as simulation experiments. Video results at https://ashish-kmr.github.io/rma-legged-robots/

## 参考
- Semantic Scholar search: RMA: Rapid Motor Adaptation for Legged Robots

## Overview
Successful real-world deployment of legged robots would require them to adapt in real-time to unseen scenarios like changing terrains, changing payloads, wear and tear. This paper presents Rapid Motor Adaptation (RMA) algorithm to solve this problem of real-time online adaptation in quadruped robots. RMA consists of two components: a base policy and an adaptation module. The combination of these components enables the robot to adapt to novel situations in fractions of a second. RMA is trained completely in simulation without using any domain knowledge like reference trajectories or predefined foot trajectory generators and is deployed on the A1 robot without any fine-tuning. We train RMA on a varied terrain generator using bioenergetics-inspired rewards and deploy it on a variety of difficult terrains including rocky, slippery, deformable surfaces in environments with grass, long vegetation, concrete, pebbles, stairs, sand, etc. RMA shows state-of-the-art performance across diverse real-world as well as simulation experiments. Video results at https://ashish-kmr.github.io/rma-legged-robots/

## Content
Successful real-world deployment of legged robots would require them to adapt in real-time to unseen scenarios like changing terrains, changing payloads, wear and tear. This paper presents Rapid Motor Adaptation (RMA) algorithm to solve this problem of real-time online adaptation in quadruped robots. RMA consists of two components: a base policy and an adaptation module. The combination of these components enables the robot to adapt to novel situations in fractions of a second. RMA is trained completely in simulation without using any domain knowledge like reference trajectories or predefined foot trajectory generators and is deployed on the A1 robot without any fine-tuning. We train RMA on a varied terrain generator using bioenergetics-inspired rewards and deploy it on a variety of difficult terrains including rocky, slippery, deformable surfaces in environments with grass, long vegetation, concrete, pebbles, stairs, sand, etc. RMA shows state-of-the-art performance across diverse real-world as well as simulation experiments. Video results at https://ashish-kmr.github.io/rma-legged-robots/

## 개요
다리 로봇의 성공적인 실제 배치를 위해서는 변화하는 지형, 변화하는 탑재 하중, 마모 등과 같은 예상치 못한 시나리오에 실시간으로 적응할 수 있어야 합니다. 본 논문은 사족 보행 로봇의 실시간 온라인 적응 문제를 해결하기 위해 Rapid Motor Adaptation(RMA) 알고리즘을 제시합니다. RMA는 기본 정책(base policy)과 적응 모듈(adaptation module)의 두 가지 구성 요소로 이루어져 있습니다. 이 구성 요소들의 조합을 통해 로봇은 순식간에 새로운 상황에 적응할 수 있습니다. RMA는 참조 궤적이나 사전 정의된 발 궤적 생성기와 같은 도메인 지식을 전혀 사용하지 않고 시뮬레이션에서 완전히 훈련되며, 추가 미세 조정 없이 A1 로봇에 배치됩니다. 우리는 생체 에너지학에서 영감을 받은 보상(bioenergetics-inspired rewards)을 사용하여 다양한 지형 생성기에서 RMA를 훈련하고, 잔디, 긴 초목, 콘크리트, 자갈, 계단, 모래 등이 있는 환경의 바위, 미끄러움, 변형 가능한 표면을 포함한 다양한 어려운 지형에 배치합니다. RMA는 다양한 실제 실험과 시뮬레이션 실험에서 최첨단 성능을 보여줍니다. 비디오 결과는 https://ashish-kmr.github.io/rma-legged-robots/ 에서 확인할 수 있습니다.

## 핵심 내용
다리 로봇의 성공적인 실제 배치를 위해서는 변화하는 지형, 변화하는 탑재 하중, 마모 등과 같은 예상치 못한 시나리오에 실시간으로 적응할 수 있어야 합니다. 본 논문은 사족 보행 로봇의 실시간 온라인 적응 문제를 해결하기 위해 Rapid Motor Adaptation(RMA) 알고리즘을 제시합니다. RMA는 기본 정책(base policy)과 적응 모듈(adaptation module)의 두 가지 구성 요소로 이루어져 있습니다. 이 구성 요소들의 조합을 통해 로봇은 순식간에 새로운 상황에 적응할 수 있습니다. RMA는 참조 궤적이나 사전 정의된 발 궤적 생성기와 같은 도메인 지식을 전혀 사용하지 않고 시뮬레이션에서 완전히 훈련되며, 추가 미세 조정 없이 A1 로봇에 배치됩니다. 우리는 생체 에너지학에서 영감을 받은 보상(bioenergetics-inspired rewards)을 사용하여 다양한 지형 생성기에서 RMA를 훈련하고, 잔디, 긴 초목, 콘크리트, 자갈, 계단, 모래 등이 있는 환경의 바위, 미끄러움, 변형 가능한 표면을 포함한 다양한 어려운 지형에 배치합니다. RMA는 다양한 실제 실험과 시뮬레이션 실험에서 최첨단 성능을 보여줍니다. 비디오 결과는 https://ashish-kmr.github.io/rma-legged-robots/ 에서 확인할 수 있습니다.
