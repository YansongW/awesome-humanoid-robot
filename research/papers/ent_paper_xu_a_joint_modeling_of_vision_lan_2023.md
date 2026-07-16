---
$id: ent_paper_xu_a_joint_modeling_of_vision_lan_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter
  zh: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter
  ko: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter
summary:
  en: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter (A Joint Modeling of Vision-Language-Action
    for Target-oriented Grasping in Clutter), is a 2023 large vision-language-action model for robotic manipulation, introduced
    by Zhejiang University, and published at ICRA23.
  zh: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter (A Joint Modeling of Vision-Language-Action
    for Target-oriented Grasping in Clutter), is a 2023 large vision-language-action model for robotic manipulation, introduced
    by Zhejiang University, and published at ICRA23.
  ko: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter (A Joint Modeling of Vision-Language-Action
    for Target-oriented Grasping in Clutter), is a 2023 large vision-language-action model for robotic manipulation, introduced
    by Zhejiang University, and published at ICRA23.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_joint_modeling_of_vision_lan
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.12610v3.
sources:
- id: src_001
  type: website
  title: A Joint Modeling of Vision-Language-Action for Target-oriented Grasping in Clutter source
  url: https://doi.org/10.1109/ICRA48891.2023.10161041
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We focus on the task of language-conditioned grasping in clutter, in which a robot is supposed to grasp the target object based on a language instruction. Previous works separately conduct visual grounding to localize the target object, and generate a grasp for that object. However, these works require object labels or visual attributes for grounding, which calls for handcrafted rules in planner and restricts the range of language instructions. In this paper, we propose to jointly model vision, language and action with object-centric representation. Our method is applicable under more flexible language instructions, and not limited by visual grounding error. Besides, by utilizing the powerful priors from the pre-trained multi-modal model and grasp model, sample efficiency is effectively improved and the sim2real problem is relived without additional data for transfer. A series of experiments carried out in simulation and real world indicate that our method can achieve better task success rate by less times of motion under more flexible language instructions. Moreover, our method is capable of generalizing better to scenarios with unseen objects and language instructions. Our code is available at https://github.com/xukechun/Vision-Language-Grasping

## 核心内容
We focus on the task of language-conditioned grasping in clutter, in which a robot is supposed to grasp the target object based on a language instruction. Previous works separately conduct visual grounding to localize the target object, and generate a grasp for that object. However, these works require object labels or visual attributes for grounding, which calls for handcrafted rules in planner and restricts the range of language instructions. In this paper, we propose to jointly model vision, language and action with object-centric representation. Our method is applicable under more flexible language instructions, and not limited by visual grounding error. Besides, by utilizing the powerful priors from the pre-trained multi-modal model and grasp model, sample efficiency is effectively improved and the sim2real problem is relived without additional data for transfer. A series of experiments carried out in simulation and real world indicate that our method can achieve better task success rate by less times of motion under more flexible language instructions. Moreover, our method is capable of generalizing better to scenarios with unseen objects and language instructions. Our code is available at https://github.com/xukechun/Vision-Language-Grasping

## 参考
- http://arxiv.org/abs/2302.12610v3

## Overview
We focus on the task of language-conditioned grasping in clutter, in which a robot is supposed to grasp the target object based on a language instruction. Previous works separately conduct visual grounding to localize the target object, and generate a grasp for that object. However, these works require object labels or visual attributes for grounding, which calls for handcrafted rules in planner and restricts the range of language instructions. In this paper, we propose to jointly model vision, language and action with object-centric representation. Our method is applicable under more flexible language instructions, and not limited by visual grounding error. Besides, by utilizing the powerful priors from the pre-trained multi-modal model and grasp model, sample efficiency is effectively improved and the sim2real problem is relived without additional data for transfer. A series of experiments carried out in simulation and real world indicate that our method can achieve better task success rate by less times of motion under more flexible language instructions. Moreover, our method is capable of generalizing better to scenarios with unseen objects and language instructions. Our code is available at https://github.com/xukechun/Vision-Language-Grasping

## Content
We focus on the task of language-conditioned grasping in clutter, in which a robot is supposed to grasp the target object based on a language instruction. Previous works separately conduct visual grounding to localize the target object, and generate a grasp for that object. However, these works require object labels or visual attributes for grounding, which calls for handcrafted rules in planner and restricts the range of language instructions. In this paper, we propose to jointly model vision, language and action with object-centric representation. Our method is applicable under more flexible language instructions, and not limited by visual grounding error. Besides, by utilizing the powerful priors from the pre-trained multi-modal model and grasp model, sample efficiency is effectively improved and the sim2real problem is relived without additional data for transfer. A series of experiments carried out in simulation and real world indicate that our method can achieve better task success rate by less times of motion under more flexible language instructions. Moreover, our method is capable of generalizing better to scenarios with unseen objects and language instructions. Our code is available at https://github.com/xukechun/Vision-Language-Grasping

## 개요
본 연구는 혼잡한 환경에서 언어 조건부 파지 작업에 초점을 맞춥니다. 이 작업에서 로봇은 언어 명령에 기반하여 목표 물체를 잡아야 합니다. 기존 연구들은 시각적 접지를 통해 목표 물체를 위치 파악하고, 해당 물체에 대한 파지를 생성하는 방식을 개별적으로 수행했습니다. 그러나 이러한 연구들은 접지를 위해 물체 레이블이나 시각적 속성을 필요로 하며, 이는 계획기에서 수동 규칙을 요구하고 언어 명령의 범위를 제한합니다. 본 논문에서는 객체 중심 표현을 통해 시각, 언어 및 행동을 공동으로 모델링하는 방법을 제안합니다. 우리의 방법은 더 유연한 언어 명령 하에서 적용 가능하며, 시각적 접지 오류에 제한되지 않습니다. 또한, 사전 훈련된 다중 모달 모델과 파지 모델의 강력한 사전 지식을 활용함으로써 샘플 효율성이 효과적으로 향상되고, 전이를 위한 추가 데이터 없이 sim2real 문제가 완화됩니다. 시뮬레이션 및 실제 환경에서 수행된 일련의 실험은 우리의 방법이 더 유연한 언어 명령 하에서 더 적은 동작 횟수로 더 높은 작업 성공률을 달성할 수 있음을 나타냅니다. 또한, 우리의 방법은 보지 못한 물체와 언어 명령이 있는 시나리오에 더 잘 일반화할 수 있습니다. 코드는 https://github.com/xukechun/Vision-Language-Grasping 에서 확인할 수 있습니다.

## 핵심 내용
본 연구는 혼잡한 환경에서 언어 조건부 파지 작업에 초점을 맞춥니다. 이 작업에서 로봇은 언어 명령에 기반하여 목표 물체를 잡아야 합니다. 기존 연구들은 시각적 접지를 통해 목표 물체를 위치 파악하고, 해당 물체에 대한 파지를 생성하는 방식을 개별적으로 수행했습니다. 그러나 이러한 연구들은 접지를 위해 물체 레이블이나 시각적 속성을 필요로 하며, 이는 계획기에서 수동 규칙을 요구하고 언어 명령의 범위를 제한합니다. 본 논문에서는 객체 중심 표현을 통해 시각, 언어 및 행동을 공동으로 모델링하는 방법을 제안합니다. 우리의 방법은 더 유연한 언어 명령 하에서 적용 가능하며, 시각적 접지 오류에 제한되지 않습니다. 또한, 사전 훈련된 다중 모달 모델과 파지 모델의 강력한 사전 지식을 활용함으로써 샘플 효율성이 효과적으로 향상되고, 전이를 위한 추가 데이터 없이 sim2real 문제가 완화됩니다. 시뮬레이션 및 실제 환경에서 수행된 일련의 실험은 우리의 방법이 더 유연한 언어 명령 하에서 더 적은 동작 횟수로 더 높은 작업 성공률을 달성할 수 있음을 나타냅니다. 또한, 우리의 방법은 보지 못한 물체와 언어 명령이 있는 시나리오에 더 잘 일반화할 수 있습니다. 코드는 https://github.com/xukechun/Vision-Language-Grasping 에서 확인할 수 있습니다.
