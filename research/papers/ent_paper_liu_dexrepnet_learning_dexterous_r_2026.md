---
$id: ent_paper_liu_dexrepnet_learning_dexterous_r_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexRepNet++: Learning Dexterous Robotic Manipulation with Geometric and Spatial Hand-Object Representations'
  zh: DexRepNet++：基于几何与空间手-物表征学习灵巧机器人操作
  ko: 'DexRepNet++: 기하학적 및 공간적 손-물체 표현을 활용한 능숙한 로봇 조작 학습'
summary:
  en: This paper proposes DexRep, a structured hand-object interaction representation that fuses occupancy, surface, and local-geometry
    features, and integrates it with deep reinforcement learning to achieve generalizable dexterous grasping, in-hand reorientation,
    and bimanual handover with real-world sim-to-real transfer.
  zh: 本文提出DexRep，一种将占用、表面和局部几何特征融合的结构化手-物交互表征，并将其与深度强化学习结合，以实现可泛化的灵巧抓取、手中重定向和双手递接，且具有真实世界的仿真到现实迁移能力。
  ko: 본 논문은 점유, 표면 및 국부 기하 특징을 융합한 구조화된 손-물체 상호작용 표현인 DexRep을 제안하고, 이를 심층 강화학습과 통합하여 일반화 가능한 능숙한 파지, 손 내 재배향, 양손 전달을 실현하고
    실제 환경으로의 시뮬레이션-투-리얼 전이를 보여준다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- dexterous_manipulation
- hand_object_representation
- reinforcement_learning
- sim_to_real
- point_cloud
- multi_fingered_hand
- bimanual_handover
- in_hand_reorientation
- grasping
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.21811v1.
sources:
- id: src_001
  type: paper
  title: 'DexRepNet++: Learning Dexterous Robotic Manipulation with Geometric and Spatial Hand-Object Representations'
  url: https://arxiv.org/abs/2602.21811
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
related_entities:
- id: ent_component_allegro_hand
  relationship: evaluates_on
  description:
    en: Deploys real-world grasp policies on an Allegro Hand.
    zh: 在Allegro Hand上部署真实世界抓取策略。
    ko: Allegro Hand에 실제 환경 파지 정책을 배포함.
---
## 概述
Robotic dexterous manipulation is a challenging problem due to high degrees of freedom (DoFs) and complex contacts of multi-fingered robotic hands. Many existing deep reinforcement learning (DRL) based methods aim at improving sample efficiency in high-dimensional output action spaces. However, existing works often overlook the role of representations in achieving generalization of a manipulation policy in the complex input space during the hand-object interaction. In this paper, we propose DexRep, a novel hand-object interaction representation to capture object surface features and spatial relations between hands and objects for dexterous manipulation skill learning. Based on DexRep, policies are learned for three dexterous manipulation tasks, i.e. grasping, in-hand reorientation, bimanual handover, and extensive experiments are conducted to verify the effectiveness. In simulation, for grasping, the policy learned with 40 objects achieves a success rate of 87.9% on more than 5000 unseen objects of diverse categories, significantly surpassing existing work trained with thousands of objects; for the in-hand reorientation and handover tasks, the policies also boost the success rates and other metrics of existing hand-object representations by 20% to 40%. The grasp policies with DexRep are deployed to the real world under multi-camera and single-camera setups and demonstrate a small sim-to-real gap.

## 核心内容
Robotic dexterous manipulation is a challenging problem due to high degrees of freedom (DoFs) and complex contacts of multi-fingered robotic hands. Many existing deep reinforcement learning (DRL) based methods aim at improving sample efficiency in high-dimensional output action spaces. However, existing works often overlook the role of representations in achieving generalization of a manipulation policy in the complex input space during the hand-object interaction. In this paper, we propose DexRep, a novel hand-object interaction representation to capture object surface features and spatial relations between hands and objects for dexterous manipulation skill learning. Based on DexRep, policies are learned for three dexterous manipulation tasks, i.e. grasping, in-hand reorientation, bimanual handover, and extensive experiments are conducted to verify the effectiveness. In simulation, for grasping, the policy learned with 40 objects achieves a success rate of 87.9% on more than 5000 unseen objects of diverse categories, significantly surpassing existing work trained with thousands of objects; for the in-hand reorientation and handover tasks, the policies also boost the success rates and other metrics of existing hand-object representations by 20% to 40%. The grasp policies with DexRep are deployed to the real world under multi-camera and single-camera setups and demonstrate a small sim-to-real gap.

## 参考
- http://arxiv.org/abs/2602.21811v1

## Overview
Robotic dexterous manipulation is a challenging problem due to high degrees of freedom (DoFs) and complex contacts of multi-fingered robotic hands. Many existing deep reinforcement learning (DRL) based methods aim at improving sample efficiency in high-dimensional output action spaces. However, existing works often overlook the role of representations in achieving generalization of a manipulation policy in the complex input space during the hand-object interaction. In this paper, we propose DexRep, a novel hand-object interaction representation to capture object surface features and spatial relations between hands and objects for dexterous manipulation skill learning. Based on DexRep, policies are learned for three dexterous manipulation tasks, i.e. grasping, in-hand reorientation, bimanual handover, and extensive experiments are conducted to verify the effectiveness. In simulation, for grasping, the policy learned with 40 objects achieves a success rate of 87.9% on more than 5000 unseen objects of diverse categories, significantly surpassing existing work trained with thousands of objects; for the in-hand reorientation and handover tasks, the policies also boost the success rates and other metrics of existing hand-object representations by 20% to 40%. The grasp policies with DexRep are deployed to the real world under multi-camera and single-camera setups and demonstrate a small sim-to-real gap.

## Content
Robotic dexterous manipulation is a challenging problem due to high degrees of freedom (DoFs) and complex contacts of multi-fingered robotic hands. Many existing deep reinforcement learning (DRL) based methods aim at improving sample efficiency in high-dimensional output action spaces. However, existing works often overlook the role of representations in achieving generalization of a manipulation policy in the complex input space during the hand-object interaction. In this paper, we propose DexRep, a novel hand-object interaction representation to capture object surface features and spatial relations between hands and objects for dexterous manipulation skill learning. Based on DexRep, policies are learned for three dexterous manipulation tasks, i.e. grasping, in-hand reorientation, bimanual handover, and extensive experiments are conducted to verify the effectiveness. In simulation, for grasping, the policy learned with 40 objects achieves a success rate of 87.9% on more than 5000 unseen objects of diverse categories, significantly surpassing existing work trained with thousands of objects; for the in-hand reorientation and handover tasks, the policies also boost the success rates and other metrics of existing hand-object representations by 20% to 40%. The grasp policies with DexRep are deployed to the real world under multi-camera and single-camera setups and demonstrate a small sim-to-real gap.

## 개요
로봇의 정밀 조작은 다관절 로봇 손의 높은 자유도(DoFs)와 복잡한 접촉으로 인해 어려운 문제입니다. 기존의 많은 심층 강화 학습(DRL) 기반 방법은 고차원 출력 행동 공간에서 샘플 효율성을 향상시키는 것을 목표로 합니다. 그러나 기존 연구는 손-객체 상호작용 중 복잡한 입력 공간에서 조작 정책의 일반화를 달성하는 데 있어 표현의 역할을 종종 간과합니다. 본 논문에서는 정밀 조작 기술 학습을 위해 객체 표면 특징과 손과 객체 간의 공간 관계를 포착하는 새로운 손-객체 상호작용 표현인 DexRep을 제안합니다. DexRep을 기반으로 세 가지 정밀 조작 작업(파지, 손 안에서의 재배향, 양손 전달)에 대한 정책을 학습하고, 효과를 검증하기 위해 광범위한 실험을 수행합니다. 시뮬레이션에서 파지의 경우, 40개의 객체로 학습된 정책이 다양한 범주의 5000개 이상의 보지 못한 객체에 대해 87.9%의 성공률을 달성하여 수천 개의 객체로 학습된 기존 연구를 크게 능가합니다. 손 안에서의 재배향 및 전달 작업의 경우, 정책은 기존 손-객체 표현의 성공률 및 기타 지표를 20%에서 40%까지 향상시킵니다. DexRep을 사용한 파지 정책은 다중 카메라 및 단일 카메라 설정에서 실제 환경에 배포되어 시뮬레이션과 실제 간의 격차가 작음을 보여줍니다.

## 핵심 내용
로봇의 정밀 조작은 다관절 로봇 손의 높은 자유도(DoFs)와 복잡한 접촉으로 인해 어려운 문제입니다. 기존의 많은 심층 강화 학습(DRL) 기반 방법은 고차원 출력 행동 공간에서 샘플 효율성을 향상시키는 것을 목표로 합니다. 그러나 기존 연구는 손-객체 상호작용 중 복잡한 입력 공간에서 조작 정책의 일반화를 달성하는 데 있어 표현의 역할을 종종 간과합니다. 본 논문에서는 정밀 조작 기술 학습을 위해 객체 표면 특징과 손과 객체 간의 공간 관계를 포착하는 새로운 손-객체 상호작용 표현인 DexRep을 제안합니다. DexRep을 기반으로 세 가지 정밀 조작 작업(파지, 손 안에서의 재배향, 양손 전달)에 대한 정책을 학습하고, 효과를 검증하기 위해 광범위한 실험을 수행합니다. 시뮬레이션에서 파지의 경우, 40개의 객체로 학습된 정책이 다양한 범주의 5000개 이상의 보지 못한 객체에 대해 87.9%의 성공률을 달성하여 수천 개의 객체로 학습된 기존 연구를 크게 능가합니다. 손 안에서의 재배향 및 전달 작업의 경우, 정책은 기존 손-객체 표현의 성공률 및 기타 지표를 20%에서 40%까지 향상시킵니다. DexRep을 사용한 파지 정책은 다중 카메라 및 단일 카메라 설정에서 실제 환경에 배포되어 시뮬레이션과 실제 간의 격차가 작음을 보여줍니다.
