---
$id: ent_paper_hapmorph_pneumatic_framework_multi_dimen_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HapMorph: A Pneumatic Framework for Multi-Dimensional Haptic Property Rendering'
  zh: 'HapMorph: A Pneumatic Framework for Multi-Dimensional Haptic Property Rendering'
  ko: 'HapMorph: A Pneumatic Framework for Multi-Dimensional Haptic Property Rendering'
summary:
  en: 'Haptic interfaces that can simultaneously modulate multiple physical properties remain a fundamental challenge in human-robot
    interaction. Existing systems typically allow the rendering of either geometric features or mechanical properties, but
    rarely both, within wearable form factors. Institutions per source list: Institute of Mechanical Intelligence、Scuola Superiore
    Sant''Anna (SSSA)、Pisa、Italy.'
  zh: HapMorph 是一种基于气动原理的框架，由研究团队开发，用于在可穿戴设备中同时连续调节物体的尺寸和刚度。其核心贡献在于通过拮抗式织物气动执行器（AFPAs）实现了多维度触觉属性的解耦控制，并展示了在轻量化（21克）设计下的高精度感知性能。
  ko: 'Haptic interfaces that can simultaneously modulate multiple physical properties remain a fundamental challenge in human-robot
    interaction. Existing systems typically allow the rendering of either geometric features or mechanical properties, but
    rarely both, within wearable form factors. Institutions per source list: Institute of Mechanical Intelligence、Scuola Superiore
    Sant''Anna (SSSA)、Pisa、Italy.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- hapmorph
- pneumatic
- framework
- multi
- dimen
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 380 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2509.05433v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2509.05433 HapMorph: A Pneumatic Framework for Multi-Dimensional Haptic Property Rendering'
  url: https://arxiv.org/abs/2509.05433
  accessed_at: '2026-07-31'
  date: '2025-09-05'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

HapMorph 通过双腔压力调节机制，实现了对物体尺寸（50-104毫米）和刚度（最高4.7 N/mm）的独立控制。该框架采用拮抗式织物气动执行器（AFPAs），在仅21克的可穿戴部件中实现了多维度触觉渲染。人类感知实验表明，用户能以89.4%的准确率和6.7秒的平均响应时间区分三个尺寸类别和三个刚度水平共九种状态。此外，HapMorph 还展示了通过结合AFPAs与互补气动结构实现形状或几何形态变化与刚度同步控制的扩展架构。

## 核心内容
### 方法
HapMorph 的核心是拮抗式织物气动执行器（AFPAs），通过双腔压力调节实现尺寸与刚度的解耦控制。执行器采用织物材料，在充气时产生拮抗作用，从而独立改变物体的几何尺寸和机械刚度。

### 架构
- **硬件设计**：原型专为手部交互设计，可穿戴部件仅重21克，尺寸变化范围为50至104毫米，刚度调节最高达4.7 N/mm。
- **控制机制**：通过调节两个独立气腔的压力，分别控制尺寸和刚度，实现连续、同步的调制。

### 实验设置
- **系统表征**：通过系统化测试验证了尺寸与刚度的解耦控制能力，确保双通道压力调节的独立性。
- **人类感知研究**：招募10名参与者，测试其对三个尺寸类别（小、中、大）和三个刚度水平（软、中、硬）共九种离散状态的区分能力。

### 关键数字
- 尺寸变化范围：50至104毫米
- 最大刚度：4.7 N/mm
- 可穿戴部件质量：21克
- 感知准确率：89.4%
- 平均响应时间：6.7秒

### 结论
HapMorph 验证了拮抗式气动原理在可穿戴触觉界面中的可行性，实现了多维度触觉属性的同步渲染。其轻量化设计和高效控制为下一代触觉接口提供了新路径，未来可扩展至形状或几何形态变化与刚度控制的结合。

## Overview
Haptic interfaces that can simultaneously modulate multiple physical properties remain a fundamental challenge in human-robot interaction. Existing systems typically allow the rendering of either geometric features or mechanical properties, but rarely both, within wearable form factors. Here, we introduce HapMorph, a pneumatic framework that enables continuous, simultaneous modulation of object size and stiffness through antagonistic fabric-based pneumatic actuators (AFPAs). We implemented a HapMorph protoytpe designed for hands interaction achieving size variation from 50 to 104 mm, stiffness modulation up to 4.7 N/mm and mass of the wearable parts of just 21 g. Through systematic characterization, we demonstrate decoupled control of size and stiffness properties via dual-chamber pressure regulation. Human perception studies with 10 participants reveal that users can distinguish nine discrete states across three size categories and three stiffness levels with 89.4% accuracy and 6.7 s average response time. We further demonstrate extended architectures that combine AFPAs with complementary pneumatic structures to enable shape or geometry morphing with concurrent stiffness control. Our results establish antagonistic pneumatic principle as a pathway toward next-generation haptic interfaces, capable of multi-dimensiona rendering properties within practical wearable constraints.

## 参考
- https://arxiv.org/abs/2509.05433
- https://github.com/ImChong/Robotics_Notebooks

## 개요

HapMorph는 이중 챔버 압력 조절 메커니즘을 통해 물체의 크기(50-104mm)와 강성(최대 4.7 N/mm)을 독립적으로 제어할 수 있습니다. 이 프레임워크는 길항적 직물 공압 액추에이터(AFPAs)를 사용하여 단 21g의 웨어러블 부품으로 다차원 촉각 렌더링을 구현합니다. 인간 인지 실험 결과, 사용자는 89.4%의 정확도와 평균 6.7초의 응답 시간으로 세 가지 크기 범주와 세 가지 강성 수준으로 구성된 총 아홉 가지 상태를 구분할 수 있었습니다. 또한 HapMorph는 AFPAs와 상호 보완적인 공압 구조를 결합하여 형태 또는 기하학적 변화와 강성 동기 제어를 구현하는 확장 아키텍처를 보여줍니다.

## 핵심 내용
### 방법
HapMorph의 핵심은 길항적 직물 공압 액추에이터(AFPAs)로, 이중 챔버 압력 조절을 통해 크기와 강성의 비연결 제어를 실현합니다. 액추에이터는 직물 재질로 제작되어 공기 주입 시 길항 작용을 생성하며, 이를 통해 물체의 기하학적 크기와 기계적 강성을 독립적으로 변경할 수 있습니다.

### 아키텍처
- **하드웨어 설계**: 프로토타입은 손 상호작용에 특화되어 설계되었으며, 웨어러블 부품은 단 21g에 불과하고 크기 변화 범위는 50~104mm, 강성 조절은 최대 4.7 N/mm까지 가능합니다.
- **제어 메커니즘**: 두 개의 독립적인 공압 챔버 압력을 각각 조절하여 크기와 강성을 제어하며, 연속적이고 동기화된 변조를 구현합니다.

### 실험 설정
- **시스템 특성화**: 체계적인 테스트를 통해 크기와 강성의 비연결 제어 능력을 검증하고, 이중 채널 압력 조절의 독립성을 보장합니다.
- **인간 인지 연구**: 10명의 참가자를 모집하여 세 가지 크기 범주(소, 중, 대)와 세 가지 강성 수준(연, 중, 경)으로 구성된 총 아홉 가지 이산 상태를 구분하는 능력을 테스트합니다.

### 주요 수치
- 크기 변화 범위: 50~104mm
- 최대 강성: 4.7 N/mm
- 웨어러블 부품 질량: 21g
- 인지 정확도: 89.4%
- 평균 응답 시간: 6.7초

### 결론
HapMorph는 길항적 공압 원리가 웨어러블 촉각 인터페이스에서 실현 가능함을 검증하였으며, 다차원 촉각 속성의 동기 렌더링을 구현했습니다. 경량 설계와 효율적인 제어는 차세대 촉각 인터페이스에 새로운 경로를 제공하며, 향후 형태 또는 기하학적 변화와 강성 제어의 결합으로 확장될 수 있습니다.
