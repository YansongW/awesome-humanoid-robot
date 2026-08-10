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
  zh: PIMBS 是 2025 年针对肌肉骨骼仿人机器人的一项硬件设计工作。其核心贡献是将 Physics-Informed Neural Networks (PINNs) 概念应用于身体图式学习，使得在少量数据下也能实现高精度学习。该方法通过结合实际机器人数据与物理定律，提升了学习效率。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.20343v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (630 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids (arXiv)'
  url: https://arxiv.org/abs/2506.20343
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
肌肉骨骼仿人机器人因结构复杂，肌肉路径常偏离几何模型，传统身体图式学习方法依赖大量人工采集数据，且数据量不足时学习困难。为此，本研究提出 PIMBS 方法，将 Physics-Informed Neural Networks (PINNs) 引入身体图式学习。该方法不仅利用实际机器人数据，还引入关节结构与力矩-肌肉张力关系的物理定律，从而在数据有限时仍能高效学习。研究在仿真环境和实际肌肉骨骼仿人机器人上验证了该方法的有效性与特性。

## 核心内容
### 背景与问题
- 肌肉骨骼仿人机器人模仿人类肌肉骨骼系统，具备可变刚度控制、冗余性和灵活性等优势。
- 其身体结构复杂，肌肉路径常显著偏离几何模型，因此需要学习身体图式，特别是关节角度、肌肉张力与肌肉长度之间的关系。
- 传统方法仅依赖实际机器人采集的数据，但数据收集过程劳动密集，且数据量有限时学习困难。

### 方法：PIMBS
- 提出将 Physics-Informed Neural Networks (PINNs) 概念应用于身体图式学习。
- 核心思路：不仅使用实际机器人数据，还利用物理定律（在正确关节结构假设下，力矩与肌肉张力之间的关系）作为约束。
- 这使得在少量数据下也能实现高精度学习，提升学习效率。

### 实验设置与结果
- 方法在仿真环境和实际肌肉骨骼仿人机器人上均进行了验证。
- 实验讨论了该方法的有效性与特性，但摘要与正文未提供具体数字或对比基准。

## Overview
Musculoskeletal humanoids are robots that closely mimic the human musculoskeletal system, offering various advantages such as variable stiffness control, redundancy, and flexibility. However, their body structure is complex, and muscle paths often significantly deviate from geometric models. To address this, numerous studies have been conducted to learn body schema, particularly the relationships among joint angles, muscle tension, and muscle length. These studies typically rely solely on data collected from the actual robot, but this data collection process is labor-intensive, and learning becomes difficult when the amount of data is limited. Therefore, in this study, we propose a method that applies the concept of Physics-Informed Neural Networks (PINNs) to the learning of body schema in musculoskeletal humanoids, enabling high-accuracy learning even with a small amount of data. By utilizing not only data obtained from the actual robot but also the physical laws governing the relationship between torque and muscle tension under the assumption of correct joint structure, more efficient learning becomes possible. We apply the proposed method to both simulation and an actual musculoskeletal humanoid and discuss its effectiveness and characteristics.

## 参考
- http://arxiv.org/abs/2506.20343v2

## 개요
근골격 휴머노이드 로봇은 구조가 복잡하여 근육 경로가 기하학적 모델에서 자주 벗어나며, 전통적인 신체 도식 학습 방법은 대량의 수작업 데이터 수집에 의존하고 데이터 양이 부족할 때 학습이 어렵습니다. 이를 위해 본 연구는 PIMBS 방법을 제안하여 Physics-Informed Neural Networks (PINNs)를 신체 도식 학습에 도입합니다. 이 방법은 실제 로봇 데이터를 활용할 뿐만 아니라 관절 구조와 토크-근육 장력 관계의 물리 법칙을 도입하여 데이터가 제한된 상황에서도 효율적으로 학습할 수 있습니다. 연구는 시뮬레이션 환경과 실제 근골격 휴머노이드 로봇에서 이 방법의 유효성과 특성을 검증했습니다.

## 핵심 내용
### 배경 및 문제
- 근골격 휴머노이드 로봇은 인간의 근골격계를 모방하며 가변 강성 제어, 중복성, 유연성 등의 장점을 갖습니다.
- 신체 구조가 복잡하여 근육 경로가 기하학적 모델에서 크게 벗어나는 경우가 많아, 관절 각도, 근육 장력, 근육 길이 간의 관계를 포함한 신체 도식 학습이 필요합니다.
- 전통적인 방법은 실제 로봇에서 수집한 데이터에만 의존하지만, 데이터 수집 과정은 노동 집약적이며 데이터 양이 제한될 때 학습이 어렵습니다.

### 방법: PIMBS
- Physics-Informed Neural Networks (PINNs) 개념을 신체 도식 학습에 적용할 것을 제안합니다.
- 핵심 아이디어: 실제 로봇 데이터뿐만 아니라 물리 법칙(올바른 관절 구조 가정 하에서 토크와 근육 장력 간의 관계)을 제약 조건으로 활용합니다.
- 이를 통해 소량의 데이터로도 높은 정밀도의 학습이 가능하며 학습 효율이 향상됩니다.

### 실험 설정 및 결과
- 이 방법은 시뮬레이션 환경과 실제 근골격 휴머노이드 로봇 모두에서 검증되었습니다.
- 실험은 이 방법의 유효성과 특성을 논의했지만, 초록과 본문에서는 구체적인 수치나 비교 기준을 제공하지 않았습니다.
