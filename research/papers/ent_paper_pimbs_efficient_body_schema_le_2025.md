---
$id: ent_paper_pimbs_efficient_body_schema_le_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids'
  zh: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids'
  ko: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids'
summary:
  en: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids is a 2025 work on hardware design for humanoid
    robots.'
  zh: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids is a 2025 work on hardware design for humanoid
    robots.'
  ko: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids is a 2025 work on hardware design for humanoid
    robots.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- hardware_design
- humanoid
- pimbs
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.20343v2.
sources:
- id: src_001
  type: paper
  title: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids (arXiv)'
  url: https://arxiv.org/abs/2506.20343
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Musculoskeletal humanoids are robots that closely mimic the human musculoskeletal system, offering various advantages such as variable stiffness control, redundancy, and flexibility. However, their body structure is complex, and muscle paths often significantly deviate from geometric models. To address this, numerous studies have been conducted to learn body schema, particularly the relationships among joint angles, muscle tension, and muscle length. These studies typically rely solely on data collected from the actual robot, but this data collection process is labor-intensive, and learning becomes difficult when the amount of data is limited. Therefore, in this study, we propose a method that applies the concept of Physics-Informed Neural Networks (PINNs) to the learning of body schema in musculoskeletal humanoids, enabling high-accuracy learning even with a small amount of data. By utilizing not only data obtained from the actual robot but also the physical laws governing the relationship between torque and muscle tension under the assumption of correct joint structure, more efficient learning becomes possible. We apply the proposed method to both simulation and an actual musculoskeletal humanoid and discuss its effectiveness and characteristics.

## 核心内容
Musculoskeletal humanoids are robots that closely mimic the human musculoskeletal system, offering various advantages such as variable stiffness control, redundancy, and flexibility. However, their body structure is complex, and muscle paths often significantly deviate from geometric models. To address this, numerous studies have been conducted to learn body schema, particularly the relationships among joint angles, muscle tension, and muscle length. These studies typically rely solely on data collected from the actual robot, but this data collection process is labor-intensive, and learning becomes difficult when the amount of data is limited. Therefore, in this study, we propose a method that applies the concept of Physics-Informed Neural Networks (PINNs) to the learning of body schema in musculoskeletal humanoids, enabling high-accuracy learning even with a small amount of data. By utilizing not only data obtained from the actual robot but also the physical laws governing the relationship between torque and muscle tension under the assumption of correct joint structure, more efficient learning becomes possible. We apply the proposed method to both simulation and an actual musculoskeletal humanoid and discuss its effectiveness and characteristics.

## 参考
- http://arxiv.org/abs/2506.20343v2

## Overview
Musculoskeletal humanoids are robots that closely mimic the human musculoskeletal system, offering various advantages such as variable stiffness control, redundancy, and flexibility. However, their body structure is complex, and muscle paths often significantly deviate from geometric models. To address this, numerous studies have been conducted to learn body schema, particularly the relationships among joint angles, muscle tension, and muscle length. These studies typically rely solely on data collected from the actual robot, but this data collection process is labor-intensive, and learning becomes difficult when the amount of data is limited. Therefore, in this study, we propose a method that applies the concept of Physics-Informed Neural Networks (PINNs) to the learning of body schema in musculoskeletal humanoids, enabling high-accuracy learning even with a small amount of data. By utilizing not only data obtained from the actual robot but also the physical laws governing the relationship between torque and muscle tension under the assumption of correct joint structure, more efficient learning becomes possible. We apply the proposed method to both simulation and an actual musculoskeletal humanoid and discuss its effectiveness and characteristics.

## Content
Musculoskeletal humanoids are robots that closely mimic the human musculoskeletal system, offering various advantages such as variable stiffness control, redundancy, and flexibility. However, their body structure is complex, and muscle paths often significantly deviate from geometric models. To address this, numerous studies have been conducted to learn body schema, particularly the relationships among joint angles, muscle tension, and muscle length. These studies typically rely solely on data collected from the actual robot, but this data collection process is labor-intensive, and learning becomes difficult when the amount of data is limited. Therefore, in this study, we propose a method that applies the concept of Physics-Informed Neural Networks (PINNs) to the learning of body schema in musculoskeletal humanoids, enabling high-accuracy learning even with a small amount of data. By utilizing not only data obtained from the actual robot but also the physical laws governing the relationship between torque and muscle tension under the assumption of correct joint structure, more efficient learning becomes possible. We apply the proposed method to both simulation and an actual musculoskeletal humanoid and discuss its effectiveness and characteristics.

## 개요
근골격 휴머노이드는 인간의 근골격계를 밀접하게 모방한 로봇으로, 가변 강성 제어, 중복성, 유연성 등 다양한 장점을 제공합니다. 그러나 그들의 신체 구조는 복잡하며, 근육 경로가 기하학적 모델에서 크게 벗어나는 경우가 많습니다. 이를 해결하기 위해, 특히 관절 각도, 근육 장력, 근육 길이 간의 관계인 신체 도식을 학습하는 많은 연구가 수행되었습니다. 이러한 연구는 일반적으로 실제 로봇에서 수집된 데이터에만 의존하지만, 이 데이터 수집 과정은 노동 집약적이며, 데이터 양이 제한적일 때 학습이 어려워집니다. 따라서 본 연구에서는 물리 정보 신경망(PINNs)의 개념을 근골격 휴머노이드의 신체 도식 학습에 적용하여, 적은 양의 데이터로도 높은 정확도의 학습을 가능하게 하는 방법을 제안합니다. 올바른 관절 구조를 가정한 상태에서 토크와 근육 장력 간의 관계를 지배하는 물리 법칙뿐만 아니라 실제 로봇에서 얻은 데이터를 활용함으로써, 더 효율적인 학습이 가능해집니다. 제안된 방법을 시뮬레이션과 실제 근골격 휴머노이드에 적용하고, 그 효과와 특성에 대해 논의합니다.

## 핵심 내용
근골격 휴머노이드는 인간의 근골격계를 밀접하게 모방한 로봇으로, 가변 강성 제어, 중복성, 유연성 등 다양한 장점을 제공합니다. 그러나 그들의 신체 구조는 복잡하며, 근육 경로가 기하학적 모델에서 크게 벗어나는 경우가 많습니다. 이를 해결하기 위해, 특히 관절 각도, 근육 장력, 근육 길이 간의 관계인 신체 도식을 학습하는 많은 연구가 수행되었습니다. 이러한 연구는 일반적으로 실제 로봇에서 수집된 데이터에만 의존하지만, 이 데이터 수집 과정은 노동 집약적이며, 데이터 양이 제한적일 때 학습이 어려워집니다. 따라서 본 연구에서는 물리 정보 신경망(PINNs)의 개념을 근골격 휴머노이드의 신체 도식 학습에 적용하여, 적은 양의 데이터로도 높은 정확도의 학습을 가능하게 하는 방법을 제안합니다. 올바른 관절 구조를 가정한 상태에서 토크와 근육 장력 간의 관계를 지배하는 물리 법칙뿐만 아니라 실제 로봇에서 얻은 데이터를 활용함으로써, 더 효율적인 학습이 가능해집니다. 제안된 방법을 시뮬레이션과 실제 근골격 휴머노이드에 적용하고, 그 효과와 특성에 대해 논의합니다.
