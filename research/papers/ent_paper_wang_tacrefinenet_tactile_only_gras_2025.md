---
$id: ent_paper_wang_tacrefinenet_tactile_only_gras_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses'
  zh: TacRefineNet
  ko: 'TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses'
summary:
  en: 'TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses (TacRefineNet), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Xiaomi Robotics.'
  zh: 'TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses (TacRefineNet), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Xiaomi Robotics.'
  ko: 'TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses (TacRefineNet), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Xiaomi Robotics.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- tacrefinenet
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.25746v1.
sources:
- id: src_001
  type: paper
  title: 'TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses (arXiv)'
  url: https://arxiv.org/abs/2509.25746
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TacRefineNet source
  url: https://doi.org/10.48550/arXiv.2509.25746
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Despite progress in both traditional dexterous grasping pipelines and recent Vision-Language-Action (VLA) approaches, the grasp execution stage remains prone to pose inaccuracies, especially in long-horizon tasks, which undermines overall performance. To address this "last-mile" challenge, we propose TacRefineNet, a tactile-only framework that achieves fine in-hand pose refinement of known objects in arbitrary target poses using multi-finger fingertip sensing. Our method iteratively adjusts the end-effector pose based on tactile feedback, aligning the object to the desired configuration. We design a multi-branch policy network that fuses tactile inputs from multiple fingers along with proprioception to predict precise control updates. To train this policy, we combine large-scale simulated data from a physics-based tactile model in MuJoCo with real-world data collected from a physical system. Comparative experiments show that pretraining on simulated data and fine-tuning with a small amount of real data significantly improves performance over simulation-only training. Extensive real-world experiments validate the effectiveness of the method, achieving millimeter-level grasp accuracy using only tactile input. To our knowledge, this is the first method to enable arbitrary in-hand pose refinement via multi-finger tactile sensing alone. Project website is available at https://sites.google.com/view/tacrefinenet

## 核心内容
Despite progress in both traditional dexterous grasping pipelines and recent Vision-Language-Action (VLA) approaches, the grasp execution stage remains prone to pose inaccuracies, especially in long-horizon tasks, which undermines overall performance. To address this "last-mile" challenge, we propose TacRefineNet, a tactile-only framework that achieves fine in-hand pose refinement of known objects in arbitrary target poses using multi-finger fingertip sensing. Our method iteratively adjusts the end-effector pose based on tactile feedback, aligning the object to the desired configuration. We design a multi-branch policy network that fuses tactile inputs from multiple fingers along with proprioception to predict precise control updates. To train this policy, we combine large-scale simulated data from a physics-based tactile model in MuJoCo with real-world data collected from a physical system. Comparative experiments show that pretraining on simulated data and fine-tuning with a small amount of real data significantly improves performance over simulation-only training. Extensive real-world experiments validate the effectiveness of the method, achieving millimeter-level grasp accuracy using only tactile input. To our knowledge, this is the first method to enable arbitrary in-hand pose refinement via multi-finger tactile sensing alone. Project website is available at https://sites.google.com/view/tacrefinenet

## 参考
- http://arxiv.org/abs/2509.25746v1

## Overview
Despite progress in both traditional dexterous grasping pipelines and recent Vision-Language-Action (VLA) approaches, the grasp execution stage remains prone to pose inaccuracies, especially in long-horizon tasks, which undermines overall performance. To address this "last-mile" challenge, we propose TacRefineNet, a tactile-only framework that achieves fine in-hand pose refinement of known objects in arbitrary target poses using multi-finger fingertip sensing. Our method iteratively adjusts the end-effector pose based on tactile feedback, aligning the object to the desired configuration. We design a multi-branch policy network that fuses tactile inputs from multiple fingers along with proprioception to predict precise control updates. To train this policy, we combine large-scale simulated data from a physics-based tactile model in MuJoCo with real-world data collected from a physical system. Comparative experiments show that pretraining on simulated data and fine-tuning with a small amount of real data significantly improves performance over simulation-only training. Extensive real-world experiments validate the effectiveness of the method, achieving millimeter-level grasp accuracy using only tactile input. To our knowledge, this is the first method to enable arbitrary in-hand pose refinement via multi-finger tactile sensing alone. Project website is available at https://sites.google.com/view/tacrefinenet

## Content
Despite progress in both traditional dexterous grasping pipelines and recent Vision-Language-Action (VLA) approaches, the grasp execution stage remains prone to pose inaccuracies, especially in long-horizon tasks, which undermines overall performance. To address this "last-mile" challenge, we propose TacRefineNet, a tactile-only framework that achieves fine in-hand pose refinement of known objects in arbitrary target poses using multi-finger fingertip sensing. Our method iteratively adjusts the end-effector pose based on tactile feedback, aligning the object to the desired configuration. We design a multi-branch policy network that fuses tactile inputs from multiple fingers along with proprioception to predict precise control updates. To train this policy, we combine large-scale simulated data from a physics-based tactile model in MuJoCo with real-world data collected from a physical system. Comparative experiments show that pretraining on simulated data and fine-tuning with a small amount of real data significantly improves performance over simulation-only training. Extensive real-world experiments validate the effectiveness of the method, achieving millimeter-level grasp accuracy using only tactile input. To our knowledge, this is the first method to enable arbitrary in-hand pose refinement via multi-finger tactile sensing alone. Project website is available at https://sites.google.com/view/tacrefinenet

## 개요
기존의 전통적인 정교한 파지 파이프라인과 최근의 Vision-Language-Action (VLA) 접근법 모두에서 진전이 있었음에도 불구하고, 파지 실행 단계는 특히 장기 과제에서 자세 부정확성이 발생하기 쉬우며, 이는 전반적인 성능을 저하시킵니다. 이러한 "마지막 단계" 문제를 해결하기 위해, 우리는 다중 손가락 끝 감지를 사용하여 임의의 목표 자세에서 알려진 물체의 미세한 손 내 자세 정밀 조정을 달성하는 촉각 전용 프레임워크인 TacRefineNet을 제안합니다. 우리의 방법은 촉각 피드백을 기반으로 엔드 이펙터 자세를 반복적으로 조정하여 물체를 원하는 구성으로 정렬합니다. 우리는 여러 손가락의 촉각 입력과 고유 감각을 융합하여 정밀한 제어 업데이트를 예측하는 다중 분기 정책 네트워크를 설계합니다. 이 정책을 훈련하기 위해, MuJoCo의 물리 기반 촉각 모델에서 얻은 대규모 시뮬레이션 데이터와 물리적 시스템에서 수집한 실제 데이터를 결합합니다. 비교 실험 결과, 시뮬레이션 데이터로 사전 훈련하고 소량의 실제 데이터로 미세 조정하는 것이 시뮬레이션 전용 훈련보다 성능을 크게 향상시키는 것으로 나타났습니다. 광범위한 실제 실험을 통해 이 방법의 효과를 검증했으며, 촉각 입력만으로 밀리미터 수준의 파지 정확도를 달성했습니다. 우리가 아는 한, 이는 다중 손가락 촉각 감지만으로 임의의 손 내 자세 정밀 조정을 가능하게 하는 첫 번째 방법입니다. 프로젝트 웹사이트는 https://sites.google.com/view/tacrefinenet 에서 확인할 수 있습니다.

## 핵심 내용
기존의 전통적인 정교한 파지 파이프라인과 최근의 Vision-Language-Action (VLA) 접근법 모두에서 진전이 있었음에도 불구하고, 파지 실행 단계는 특히 장기 과제에서 자세 부정확성이 발생하기 쉬우며, 이는 전반적인 성능을 저하시킵니다. 이러한 "마지막 단계" 문제를 해결하기 위해, 우리는 다중 손가락 끝 감지를 사용하여 임의의 목표 자세에서 알려진 물체의 미세한 손 내 자세 정밀 조정을 달성하는 촉각 전용 프레임워크인 TacRefineNet을 제안합니다. 우리의 방법은 촉각 피드백을 기반으로 엔드 이펙터 자세를 반복적으로 조정하여 물체를 원하는 구성으로 정렬합니다. 우리는 여러 손가락의 촉각 입력과 고유 감각을 융합하여 정밀한 제어 업데이트를 예측하는 다중 분기 정책 네트워크를 설계합니다. 이 정책을 훈련하기 위해, MuJoCo의 물리 기반 촉각 모델에서 얻은 대규모 시뮬레이션 데이터와 물리적 시스템에서 수집한 실제 데이터를 결합합니다. 비교 실험 결과, 시뮬레이션 데이터로 사전 훈련하고 소량의 실제 데이터로 미세 조정하는 것이 시뮬레이션 전용 훈련보다 성능을 크게 향상시키는 것으로 나타났습니다. 광범위한 실제 실험을 통해 이 방법의 효과를 검증했으며, 촉각 입력만으로 밀리미터 수준의 파지 정확도를 달성했습니다. 우리가 아는 한, 이는 다중 손가락 촉각 감지만으로 임의의 손 내 자세 정밀 조정을 가능하게 하는 첫 번째 방법입니다. 프로젝트 웹사이트는 https://sites.google.com/view/tacrefinenet 에서 확인할 수 있습니다.
