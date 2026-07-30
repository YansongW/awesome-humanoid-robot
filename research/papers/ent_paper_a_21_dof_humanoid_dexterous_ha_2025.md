---
$id: ent_paper_a_21_dof_humanoid_dexterous_ha_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'A 21-DOF Humanoid Dexterous Hand with Hybrid SMA-Motor Actuation: CYJ Hand-0'
  zh: 'A 21-DOF Humanoid Dexterous Hand with Hybrid SMA-Motor Actuation: CYJ Hand-0'
  ko: 'A 21-DOF Humanoid Dexterous Hand with Hybrid SMA-Motor Actuation: CYJ Hand-0'
summary:
  en: 'A 21-DOF Humanoid Dexterous Hand with Hybrid SMA-Motor Actuation: CYJ Hand-0 is a 2025 work on hardware design for
    humanoid robots.'
  zh: CYJ Hand-0 是一款 2025 年提出的 21 自由度仿人灵巧手，采用混合形状记忆合金（SMA）与直流电机驱动。其核心贡献在于通过 3D 打印 AlSi10Mg 金属框架和钓鱼线人工肌腱，复现人手骨骼与肌腱-肌肉结构，实现仿生灵巧性。
  ko: 'A 21-DOF Humanoid Dexterous Hand with Hybrid SMA-Motor Actuation: CYJ Hand-0 is a 2025 work on hardware design for
    humanoid robots.'
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
- a_21_dof_humanoid_dexterous_ha
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.14538v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'A 21-DOF Humanoid Dexterous Hand with Hybrid SMA-Motor Actuation: CYJ Hand-0 (arXiv)'
  url: https://arxiv.org/abs/2507.14538
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
CYJ Hand-0 的混合驱动系统将线性电机用于手指屈曲，SMA 模块用于手指伸展和侧向外展，两者集成在紧凑的混合驱动单元中，并安装于定制后支撑结构上。该手采用高强度钓鱼线作为人工肌腱，全 3D 打印的 AlSi10Mg 金属框架模拟人手骨骼与肌腱-肌肉结构。在基于 Arduino Mega 2560 的控制系统下进行的机械与运动学实验，验证了设计的有效性及其仿生灵巧性。

## 核心内容
### 设计与架构
- **自由度**：21 个自由度，实现高度仿人运动。
- **驱动系统**：混合肌腱驱动，结合形状记忆合金（SMA）与直流电机。
  - 线性电机模块：控制手指屈曲。
  - SMA 模块：控制手指伸展与侧向外展。
- **结构材料**：全 3D 打印 AlSi10Mg 金属框架，模拟人手骨骼结构。
- **人工肌腱**：采用高强度钓鱼线，模拟人体肌腱功能。
- **集成单元**：混合驱动单元紧凑集成于定制后支撑结构上。

### 实验与验证
- **控制系统**：基于 Arduino Mega 2560 实现控制。
- **实验内容**：机械与运动学实验，验证设计有效性与仿生灵巧性。
- **关键结果**：实验证明该设计能有效复现人手运动模式，实现灵巧操作。

## Overview
CYJ Hand-0 is a 21-DOF humanoid dexterous hand featuring a hybrid tendon-driven actuation system that combines shape memory alloys (SMAs) and DC motors. The hand employs high-strength fishing line as artificial tendons and uses a fully 3D-printed AlSi10Mg metal frame designed to replicate the skeletal and tendon-muscle structure of the human hand. A linear motor-driven module controls finger flexion, while an SMA-based module enables finger extension and lateral abduction. These modules are integrated into a compact hybrid actuation unit mounted on a custom rear support structure. Mechanical and kinematic experiments, conducted under an Arduino Mega 2560-based control system, validate the effectiveness of the design and demonstrate its biomimetic dexterity.

## 개요
CYJ Hand-0는 형상기억합금(SMA)과 DC 모터를 결합한 하이브리드 텐던 구동 시스템을 갖춘 21자유도 인간형 정밀 손이다. 이 손은 고강도 낚싯줄을 인공 힘줄로 사용하며, 인간 손의 골격 및 힘줄-근육 구조를 재현하도록 설계된 완전 3D 프린팅 AlSi10Mg 금속 프레임을 채택했다. 선형 모터 구동 모듈은 손가락 굽힘을 제어하고, SMA 기반 모듈은 손가락 폄과 측면 외전을 가능하게 한다. 이러한 모듈은 맞춤형 후방 지지 구조에 장착된 소형 하이브리드 구동 장치에 통합된다. Arduino Mega 2560 기반 제어 시스템 하에서 수행된 기계적 및 운동학적 실험은 설계의 효과성을 검증하고 생체 모방적 기민함을 입증한다.

## 핵심 내용
CYJ Hand-0는 형상기억합금(SMA)과 DC 모터를 결합한 하이브리드 텐던 구동 시스템을 갖춘 21자유도 인간형 정밀 손이다. 이 손은 고강도 낚싯줄을 인공 힘줄로 사용하며, 인간 손의 골격 및 힘줄-근육 구조를 재현하도록 설계된 완전 3D 프린팅 AlSi10Mg 금속 프레임을 채택했다. 선형 모터 구동 모듈은 손가락 굽힘을 제어하고, SMA 기반 모듈은 손가락 폄과 측면 외전을 가능하게 한다. 이러한 모듈은 맞춤형 후방 지지 구조에 장착된 소형 하이브리드 구동 장치에 통합된다. Arduino Mega 2560 기반 제어 시스템 하에서 수행된 기계적 및 운동학적 실험은 설계의 효과성을 검증하고 생체 모방적 기민함을 입증한다.

## 参考
- http://arxiv.org/abs/2507.14538v1
