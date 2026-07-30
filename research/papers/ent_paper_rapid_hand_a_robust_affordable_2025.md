---
$id: ent_paper_rapid_hand_a_robust_affordable_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RAPID Hand: A Robust, Affordable, Perception-Integrated, Dexterous Manipulation Platform for Generalist Robot Autonomy'
  zh: 'RAPID Hand: A Robust, Affordable, Perception-Integrated, Dexterous Manipulation Platform for Generalist Robot Autonomy'
  ko: 'RAPID Hand: A Robust, Affordable, Perception-Integrated, Dexterous Manipulation Platform for Generalist Robot Autonomy'
summary:
  en: 'RAPID Hand: A Robust, Affordable, Perception-Integrated, Dexterous Manipulation Platform for Generalist Robot Autonomy
    is a 2025 work on hardware design for humanoid robots.'
  zh: RAPID Hand 是一个面向通用机器人自主性的低成本、高灵巧度操作平台，由 2025 年的研究团队提出。其核心贡献在于通过协同优化硬件与软件，集成了紧凑的 20 自由度手部、亚 7 毫秒延迟的全手感知系统以及高自由度遥操作接口，实现了稳定、高质量的数据采集。实验表明，基于该平台收集数据训练的扩散策略性能优于先前工作。
  ko: 'RAPID Hand: A Robust, Affordable, Perception-Integrated, Dexterous Manipulation Platform for Generalist Robot Autonomy
    is a 2025 work on hardware design for humanoid robots.'
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
- rapid_hand
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.07490v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'RAPID Hand: A Robust, Affordable, Perception-Integrated, Dexterous Manipulation Platform for Generalist Robot Autonomy
    (arXiv)'
  url: https://arxiv.org/abs/2506.07490
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
RAPID Hand 旨在解决低成本、高灵巧度平台稀缺的问题，以支持真实世界多指机器人操作数据的收集，推动通用机器人自主性发展。该平台通过协同设计硬件与软件，采用紧凑实用的手部本体论和硬件级感知框架，将腕部视觉、指尖触觉感知与本体感觉稳定集成，延迟低于 7 毫秒且空间对齐。为应对高自由度手部遥操作的挑战，研究团队通过通用驱动方案、定制感知电子元件和两种重定向约束，对手部设计、感知集成和遥操作接口进行了联合优化。平台由低成本、现成的组件构建，并将公开以促进可复现性和易用性。

## 核心内容
### 方法
- **手部设计**：采用紧凑的 20 自由度手部本体论，通过通用驱动方案实现高灵巧度与低成本平衡。
- **感知集成**：硬件级感知框架整合腕部视觉、指尖触觉感知与本体感觉，延迟低于 7 毫秒，并确保空间对齐。
- **遥操作接口**：针对高自由度手部，通过两种重定向约束（retargeting constraints）优化遥操作，提升精度与稳定性。

### 实验设置
- 平台评估涵盖硬件性能、感知系统与遥操作接口。
- 使用收集的数据训练扩散策略（diffusion policy），并与先前工作对比。

### 关键数字
- 手部自由度：20-DoF
- 感知延迟：亚 7 毫秒（sub-7 ms）
- 组件来源：低成本、现成组件（off-the-shelf components）

### 结论
- 训练扩散策略的性能优于先前工作，验证了平台在可靠、高质量数据收集方面的能力。
- 平台将公开，确保可复现性与易用性。

## Overview
This paper addresses the scarcity of low-cost but high-dexterity platforms for collecting real-world multi-fingered robot manipulation data towards generalist robot autonomy. To achieve it, we propose the RAPID Hand, a co-optimized hardware and software platform where the compact 20-DoF hand, robust whole-hand perception, and high-DoF teleoperation interface are jointly designed. Specifically, RAPID Hand adopts a compact and practical hand ontology and a hardware-level perception framework that stably integrates wrist-mounted vision, fingertip tactile sensing, and proprioception with sub-7 ms latency and spatial alignment. Collecting high-quality demonstrations on high-DoF hands is challenging, as existing teleoperation methods struggle with precision and stability on complex multi-fingered systems. We address this by co-optimizing hand design, perception integration, and teleoperation interface through a universal actuation scheme, custom perception electronics, and two retargeting constraints. We evaluate the platform's hardware, perception, and teleoperation interface. Training a diffusion policy on collected data shows superior performance over prior works, validating the system's capability for reliable, high-quality data collection. The platform is constructed from low-cost and off-the-shelf components and will be made public to ensure reproducibility and ease of adoption.

## 개요
본 논문은 범용 로봇 자율성을 위한 실제 다지 로봇 조작 데이터 수집에 있어 저비용이면서도 높은 기민성을 갖춘 플랫폼의 부족 문제를 다룹니다. 이를 해결하기 위해 우리는 RAPID Hand를 제안합니다. 이는 소형 20자유도(DoF) 손, 강건한 전손 인식, 높은 자유도의 원격 조작 인터페이스가 공동 설계된 하드웨어 및 소프트웨어 최적화 플랫폼입니다. 구체적으로, RAPID Hand는 소형이면서 실용적인 손 온톨로지와 손목 장착형 비전, 손끝 촉각 센싱, 고유 감각을 7ms 미만의 지연 시간과 공간적 정렬로 안정적으로 통합하는 하드웨어 수준의 인식 프레임워크를 채택합니다. 높은 자유도의 손에서 고품질 시연 데이터를 수집하는 것은 기존 원격 조작 방법이 복잡한 다지 시스템에서 정밀도와 안정성에 어려움을 겪기 때문에 도전적입니다. 우리는 보편적 구동 방식, 맞춤형 인식 전자 장치, 두 가지 리타겟팅 제약 조건을 통해 손 설계, 인식 통합, 원격 조작 인터페이스를 공동 최적화하여 이 문제를 해결합니다. 플랫폼의 하드웨어, 인식, 원격 조작 인터페이스를 평가합니다. 수집된 데이터로 확산 정책을 훈련한 결과, 이전 연구보다 우수한 성능을 보여 시스템의 신뢰할 수 있는 고품질 데이터 수집 능력을 검증합니다. 플랫폼은 저비용 및 기성 부품으로 구성되며, 재현성과 채택 용이성을 보장하기 위해 공개될 예정입니다.

## 핵심 내용
본 논문은 범용 로봇 자율성을 위한 실제 다지 로봇 조작 데이터 수집에 있어 저비용이면서도 높은 기민성을 갖춘 플랫폼의 부족 문제를 다룹니다. 이를 해결하기 위해 우리는 RAPID Hand를 제안합니다. 이는 소형 20자유도(DoF) 손, 강건한 전손 인식, 높은 자유도의 원격 조작 인터페이스가 공동 설계된 하드웨어 및 소프트웨어 최적화 플랫폼입니다. 구체적으로, RAPID Hand는 소형이면서 실용적인 손 온톨로지와 손목 장착형 비전, 손끝 촉각 센싱, 고유 감각을 7ms 미만의 지연 시간과 공간적 정렬로 안정적으로 통합하는 하드웨어 수준의 인식 프레임워크를 채택합니다. 높은 자유도의 손에서 고품질 시연 데이터를 수집하는 것은 기존 원격 조작 방법이 복잡한 다지 시스템에서 정밀도와 안정성에 어려움을 겪기 때문에 도전적입니다. 우리는 보편적 구동 방식, 맞춤형 인식 전자 장치, 두 가지 리타겟팅 제약 조건을 통해 손 설계, 인식 통합, 원격 조작 인터페이스를 공동 최적화하여 이 문제를 해결합니다. 플랫폼의 하드웨어, 인식, 원격 조작 인터페이스를 평가합니다. 수집된 데이터로 확산 정책을 훈련한 결과, 이전 연구보다 우수한 성능을 보여 시스템의 신뢰할 수 있는 고품질 데이터 수집 능력을 검증합니다. 플랫폼은 저비용 및 기성 부품으로 구성되며, 재현성과 채택 용이성을 보장하기 위해 공개될 예정입니다.

## 参考
- http://arxiv.org/abs/2506.07490v1
