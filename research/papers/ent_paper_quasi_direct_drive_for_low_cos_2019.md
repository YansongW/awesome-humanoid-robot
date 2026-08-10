---
$id: ent_paper_quasi_direct_drive_for_low_cos_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Quasi-Direct Drive for Low-Cost Compliant Robotic Manipulation
  zh: Quasi-Direct Drive for Low-Cost Compliant Robotic Manipulation
  ko: Quasi-Direct Drive for Low-Cost Compliant Robotic Manipulation
summary:
  en: Quasi-Direct Drive for Low-Cost Compliant Robotic Manipulation is a 2019 work on hardware design for humanoid robots.
  zh: Quasi-Direct Drive 是 2019 年提出的一种低成本、力控机器人硬件设计范式。其原型 Blue 是一款人形尺度、7 自由度、2kg 负载的机械臂，成本低于 5000 美元。核心贡献在于证明了准直驱驱动在动态性能上满足人机交互需求，并集成了基于虚拟现实的遥操作接口。
  ko: Quasi-Direct Drive for Low-Cost Compliant Robotic Manipulation is a 2019 work on hardware design for humanoid robots.
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
- quasi_direct_drive_for_low_cos
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1904.03815v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (728 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Quasi-Direct Drive for Low-Cost Compliant Robotic Manipulation (arXiv)
  url: https://arxiv.org/abs/1904.03815
  date: '2019'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Quasi-Direct Drive for Low-Cost Compliant Robotic Manipulation project page
  url: https://berkeleyopenarms.github.io/
  date: '2019'
  accessed_at: '2026-07-01'
---
## 概述
该工作旨在解决机器人广泛、安全部署于非结构化人类环境中的两大障碍：成本与力控能力。作者提出 Quasi-Direct Drive 驱动范式，并据此构建了名为 Blue 的 7 自由度人形机械臂原型。Blue 的制造成本低于 5000 美元，却实现了 7.5Hz 的标称位置控制带宽和 4mm 以内的重复定位精度，动态性能满足人类操作需求。此外，研究还开发了一套基于虚拟现实的接口，可用于遥操作和机器人训练数据采集。

## 核心内容
### 核心方法：Quasi-Direct Drive 驱动范式
- 该范式在传统高减速比驱动与直接驱动之间取得平衡，旨在兼顾低成本、力控柔顺性与足够的动态性能。
- 通过优化电机与减速器的选型与匹配，在保持力控能力的同时大幅降低硬件成本。

### 原型系统：Blue 机械臂
- **构型**：人形尺度、7 自由度机械臂，负载能力为 2kg。
- **成本**：制造成本低于 5000 美元，远低于同类力控机器人。
- **动态性能**：
  - 标称位置控制带宽：7.5Hz。
  - 重复定位精度：4mm 以内。
  - 这些指标满足或超过了人类操作员对机器人交互的需求。

### 遥操作与数据采集接口
- 开发了一套基于虚拟现实的交互界面，支持：
  - **遥操作**：操作员可通过 VR 设备远程控制 Blue 执行任务。
  - **训练数据采集**：该接口可收集人类演示数据，用于后续的机器人学习训练。

### 可制造性与扩展性
- 论文还讨论了 Blue 系统的可制造性、规模化生产潜力以及潜在应用场景。
- 更多视频与信息可访问 berkeleyopenarms.github.io。

## Overview
Robots must cost less and be force-controlled to enable widespread, safe deployment in unconstrained human environments. We propose Quasi-Direct Drive actuation as a capable paradigm for robotic force-controlled manipulation in human environments at low-cost. Our prototype - Blue - is a human scale 7 Degree of Freedom arm with 2kg payload. Blue can cost less than $5000. We show that Blue has dynamic properties that meet or exceed the needs of human operators: the robot has a nominal position-control bandwidth of 7.5Hz and repeatability within 4mm. We demonstrate a Virtual Reality based interface that can be used as a method for telepresence and collecting robot training demonstrations. Manufacturability, scaling, and potential use-cases for the Blue system are also addressed. Videos and additional information can be found online at berkeleyopenarms.github.io

## 参考
- http://arxiv.org/abs/1904.03815v2

## 개요
이 연구는 로봇이 비구조화된 인간 환경에서 광범위하고 안전하게 배치되기 위한 두 가지 장애물, 즉 비용과 힘 제어 능력을 해결하는 것을 목표로 한다. 저자는 Quasi-Direct Drive 구동 패러다임을 제안하고, 이를 기반으로 Blue라는 7자유도 인간형 로봇 팔 프로토타입을 구축했다. Blue의 제조 비용은 5000달러 미만이지만, 7.5Hz의 공칭 위치 제어 대역폭과 4mm 이내의 반복 위치 정밀도를 달성하여 인간 조작 요구를 충족하는 동적 성능을 보여준다. 또한, 연구는 원격 조작 및 로봇 훈련 데이터 수집에 사용할 수 있는 가상 현실 기반 인터페이스도 개발했다.

## 핵심 내용
### 핵심 방법: Quasi-Direct Drive 구동 패러다임
- 이 패러다임은 기존의 고감속비 구동과 직접 구동 사이의 균형을 이루며, 저비용, 힘 제어 유연성, 충분한 동적 성능을 동시에 고려하는 것을 목표로 한다.
- 모터와 감속기의 선정 및 매칭을 최적화하여 힘 제어 능력을 유지하면서도 하드웨어 비용을 크게 절감한다.

### 프로토타입 시스템: Blue 로봇 팔
- **구성**: 인간형 크기, 7자유도 로봇 팔, 2kg의 부하 용량.
- **비용**: 제조 비용이 5000달러 미만으로, 동급 힘 제어 로봇보다 훨씬 저렴하다.
- **동적 성능**:
  - 공칭 위치 제어 대역폭: 7.5Hz.
  - 반복 위치 정밀도: 4mm 이내.
  - 이러한 지표는 인간 조작자가 로봇 상호작용에 요구하는 수준을 충족하거나 초과한다.

### 원격 조작 및 데이터 수집 인터페이스
- 가상 현실 기반 상호작용 인터페이스를 개발하여 다음을 지원한다:
  - **원격 조작**: 조작자는 VR 장치를 통해 Blue를 원격으로 제어하여 작업을 수행할 수 있다.
  - **훈련 데이터 수집**: 이 인터페이스는 인간 시연 데이터를 수집하여 이후 로봇 학습 훈련에 사용할 수 있다.

### 제조 가능성 및 확장성
- 논문은 Blue 시스템의 제조 가능성, 대규모 생산 잠재력 및 잠재적 응용 시나리오에 대해서도 논의한다.
- 더 많은 비디오와 정보는 berkeleyopenarms.github.io에서 확인할 수 있다.
