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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.20343v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
근골격 휴머노이드는 인간의 근골격계를 밀접하게 모방한 로봇으로, 가변 강성 제어, 중복성, 유연성 등 다양한 장점을 제공합니다. 그러나 그들의 신체 구조는 복잡하며, 근육 경로가 기하학적 모델에서 크게 벗어나는 경우가 많습니다. 이를 해결하기 위해, 특히 관절 각도, 근육 장력, 근육 길이 간의 관계인 신체 도식을 학습하는 많은 연구가 수행되었습니다. 이러한 연구는 일반적으로 실제 로봇에서 수집된 데이터에만 의존하지만, 이 데이터 수집 과정은 노동 집약적이며, 데이터 양이 제한적일 때 학습이 어려워집니다. 따라서 본 연구에서는 물리 정보 신경망(PINNs)의 개념을 근골격 휴머노이드의 신체 도식 학습에 적용하여, 적은 양의 데이터로도 높은 정확도의 학습을 가능하게 하는 방법을 제안합니다. 올바른 관절 구조를 가정한 상태에서 토크와 근육 장력 간의 관계를 지배하는 물리 법칙뿐만 아니라 실제 로봇에서 얻은 데이터를 활용함으로써, 더 효율적인 학습이 가능해집니다. 제안된 방법을 시뮬레이션과 실제 근골격 휴머노이드에 적용하고, 그 효과와 특성에 대해 논의합니다.

## 핵심 내용
근골격 휴머노이드는 인간의 근골격계를 밀접하게 모방한 로봇으로, 가변 강성 제어, 중복성, 유연성 등 다양한 장점을 제공합니다. 그러나 그들의 신체 구조는 복잡하며, 근육 경로가 기하학적 모델에서 크게 벗어나는 경우가 많습니다. 이를 해결하기 위해, 특히 관절 각도, 근육 장력, 근육 길이 간의 관계인 신체 도식을 학습하는 많은 연구가 수행되었습니다. 이러한 연구는 일반적으로 실제 로봇에서 수집된 데이터에만 의존하지만, 이 데이터 수집 과정은 노동 집약적이며, 데이터 양이 제한적일 때 학습이 어려워집니다. 따라서 본 연구에서는 물리 정보 신경망(PINNs)의 개념을 근골격 휴머노이드의 신체 도식 학습에 적용하여, 적은 양의 데이터로도 높은 정확도의 학습을 가능하게 하는 방법을 제안합니다. 올바른 관절 구조를 가정한 상태에서 토크와 근육 장력 간의 관계를 지배하는 물리 법칙뿐만 아니라 실제 로봇에서 얻은 데이터를 활용함으로써, 더 효율적인 학습이 가능해집니다. 제안된 방법을 시뮬레이션과 실제 근골격 휴머노이드에 적용하고, 그 효과와 특성에 대해 논의합니다.

## 参考
- http://arxiv.org/abs/2506.20343v2
