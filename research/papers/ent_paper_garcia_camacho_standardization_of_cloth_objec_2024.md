---
$id: ent_paper_garcia_camacho_standardization_of_cloth_objec_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Standardization of Cloth Objects and its Relevance in Robotic Manipulation
  zh: 布料物体的标准化及其在机器人操作中的相关性
  ko: 천 객체의 표준화 및 로봇 조작과의 관련성
summary:
  en: This paper proposes a non-destructive, easy-to-use measurement framework grounded in textile-industry standards to characterize
    physical and mechanical cloth properties, and evaluates how stiffness, elasticity, and friction influence five robotic
    manipulation primitives performed with a Franka-Emika Panda robot.
  zh: 本文提出了一种基于纺织工业标准的无损、易用的测量框架，用于表征布料的物理和机械特性，并评估了刚度、弹性和摩擦力如何影响Franka-Emika Panda机器人执行的五种机器人操作基元。
  ko: 본 논문은 섬유 산업 표준에 기반한 비파괴적이고 사용하기 쉬운 측정 프레임워크를 제안하여 천의 물리적 및 기계적 특성을 특성화하고, Franka-Emika Panda 로봇으로 수행된 다섯 가지 로봇 조작 프리미티브에
    강성, 탄성, 마찰이 미치는 영향을 평가한다.
domains:
- 10_evaluation_benchmarks
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- cloth_manipulation
- deformable_objects
- fabric_characterization
- textile_measurement
- benchmarking
- reproducibility
- franka_emika_panda
- manipulation_primitives
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.04608v1.
sources:
- id: src_001
  type: paper
  title: Standardization of Cloth Objects and its Relevance in Robotic Manipulation
  url: https://arxiv.org/abs/2403.04608
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
The field of robotics faces inherent challenges in manipulating deformable objects, particularly in understanding and standardising fabric properties like elasticity, stiffness, and friction. While the significance of these properties is evident in the realm of cloth manipulation, accurately categorising and comprehending them in real-world applications remains elusive. This study sets out to address two primary objectives: (1) to provide a framework suitable for robotics applications to characterise cloth objects, and (2) to study how these properties influence robotic manipulation tasks. Our preliminary results validate the framework's ability to characterise cloth properties and compare cloth sets, and reveal the influence that different properties have on the outcome of five manipulation primitives. We believe that, in general, results on the manipulation of clothes should be reported along with a better description of the garments used in the evaluation. This paper proposes a set of these measures.

## 核心内容
The field of robotics faces inherent challenges in manipulating deformable objects, particularly in understanding and standardising fabric properties like elasticity, stiffness, and friction. While the significance of these properties is evident in the realm of cloth manipulation, accurately categorising and comprehending them in real-world applications remains elusive. This study sets out to address two primary objectives: (1) to provide a framework suitable for robotics applications to characterise cloth objects, and (2) to study how these properties influence robotic manipulation tasks. Our preliminary results validate the framework's ability to characterise cloth properties and compare cloth sets, and reveal the influence that different properties have on the outcome of five manipulation primitives. We believe that, in general, results on the manipulation of clothes should be reported along with a better description of the garments used in the evaluation. This paper proposes a set of these measures.

## 参考
- http://arxiv.org/abs/2403.04608v1

## Overview
The field of robotics faces inherent challenges in manipulating deformable objects, particularly in understanding and standardising fabric properties like elasticity, stiffness, and friction. While the significance of these properties is evident in the realm of cloth manipulation, accurately categorising and comprehending them in real-world applications remains elusive. This study sets out to address two primary objectives: (1) to provide a framework suitable for robotics applications to characterise cloth objects, and (2) to study how these properties influence robotic manipulation tasks. Our preliminary results validate the framework's ability to characterise cloth properties and compare cloth sets, and reveal the influence that different properties have on the outcome of five manipulation primitives. We believe that, in general, results on the manipulation of clothes should be reported along with a better description of the garments used in the evaluation. This paper proposes a set of these measures.

## Content
The field of robotics faces inherent challenges in manipulating deformable objects, particularly in understanding and standardising fabric properties like elasticity, stiffness, and friction. While the significance of these properties is evident in the realm of cloth manipulation, accurately categorising and comprehending them in real-world applications remains elusive. This study sets out to address two primary objectives: (1) to provide a framework suitable for robotics applications to characterise cloth objects, and (2) to study how these properties influence robotic manipulation tasks. Our preliminary results validate the framework's ability to characterise cloth properties and compare cloth sets, and reveal the influence that different properties have on the outcome of five manipulation primitives. We believe that, in general, results on the manipulation of clothes should be reported along with a better description of the garments used in the evaluation. This paper proposes a set of these measures.

## 개요
로봇공학 분야는 변형 가능한 물체를 조작하는 데 있어 본질적인 어려움에 직면해 있으며, 특히 탄성, 강성, 마찰과 같은 직물 특성을 이해하고 표준화하는 데 어려움을 겪고 있습니다. 이러한 특성의 중요성은 직물 조작 영역에서 명백하지만, 실제 응용에서 이를 정확하게 분류하고 이해하는 것은 여전히 어려운 과제입니다. 본 연구는 두 가지 주요 목표를 설정합니다: (1) 로봇공학 응용에 적합한 직물 객체 특성화 프레임워크를 제공하고, (2) 이러한 특성이 로봇 조작 작업에 미치는 영향을 연구하는 것입니다. 예비 결과는 프레임워크가 직물 특성을 특성화하고 직물 세트를 비교할 수 있는 능력을 검증하며, 다섯 가지 조작 기본 동작의 결과에 다양한 특성이 미치는 영향을 밝혀냅니다. 일반적으로 의류 조작에 대한 결과는 평가에 사용된 의류에 대한 더 나은 설명과 함께 보고되어야 한다고 생각합니다. 본 논문은 이러한 측정값 세트를 제안합니다.

## 핵심 내용
로봇공학 분야는 변형 가능한 물체를 조작하는 데 있어 본질적인 어려움에 직면해 있으며, 특히 탄성, 강성, 마찰과 같은 직물 특성을 이해하고 표준화하는 데 어려움을 겪고 있습니다. 이러한 특성의 중요성은 직물 조작 영역에서 명백하지만, 실제 응용에서 이를 정확하게 분류하고 이해하는 것은 여전히 어려운 과제입니다. 본 연구는 두 가지 주요 목표를 설정합니다: (1) 로봇공학 응용에 적합한 직물 객체 특성화 프레임워크를 제공하고, (2) 이러한 특성이 로봇 조작 작업에 미치는 영향을 연구하는 것입니다. 예비 결과는 프레임워크가 직물 특성을 특성화하고 직물 세트를 비교할 수 있는 능력을 검증하며, 다섯 가지 조작 기본 동작의 결과에 다양한 특성이 미치는 영향을 밝혀냅니다. 일반적으로 의류 조작에 대한 결과는 평가에 사용된 의류에 대한 더 나은 설명과 함께 보고되어야 한다고 생각합니다. 본 논문은 이러한 측정값 세트를 제안합니다.
