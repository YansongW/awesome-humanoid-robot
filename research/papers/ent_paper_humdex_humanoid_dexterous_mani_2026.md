---
$id: ent_paper_humdex_humanoid_dexterous_mani_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumDex: Humanoid Dexterous Manipulation Made Easy'
  zh: 'HumDex: Humanoid Dexterous Manipulation Made Easy'
  ko: 'HumDex: Humanoid Dexterous Manipulation Made Easy'
summary:
  en: 'HumDex: Humanoid Dexterous Manipulation Made Easy is a 2026 work on manipulation for humanoid robots.'
  zh: HumDex 是 2026 年提出的一套面向人形机器人全身灵巧操作的便携式遥操作系统。该系统通过 IMU 运动追踪与基于学习的重定向方法，解决了数据采集中的便携性与精度矛盾，并基于此提出两阶段模仿学习框架，显著提升了操作泛化能力。项目已完全开源。
  ko: 'HumDex: Humanoid Dexterous Manipulation Made Easy is a 2026 work on manipulation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humdex
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.12260v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (787 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'HumDex: Humanoid Dexterous Manipulation Made Easy (arXiv)'
  url: https://arxiv.org/abs/2603.12260
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人全身灵巧操作面临高质量演示数据采集效率低下的核心瓶颈。现有遥操作系统普遍存在便携性差、视野遮挡或精度不足等问题，难以胜任复杂全身任务。HumDex 采用 IMU 运动追踪技术，在保证便携性的同时实现精确的全身姿态追踪；针对灵巧手控制，引入无需手动调参的基于学习的重定向方法，生成平滑自然的抓取动作。该系统不仅支持高效的人类运动数据采集，还构建了两阶段模仿学习框架：先在多样化人类运动数据上预训练以学习通用先验，再在机器人数据上微调以弥合具身差异。实验表明，该方法能以极低的数据采集成本，显著提升对新构型、新物体和新背景的泛化能力。

## 核心内容
### 核心挑战
- 人形机器人全身灵巧操作的主要瓶颈在于高质量演示数据的采集效率。
- 现有遥操作系统在便携性、视野遮挡和精度方面存在权衡，难以满足复杂全身任务需求。

### 系统设计
- **便携性与精度平衡**：采用 IMU 运动追踪技术，实现精确的全身姿态追踪，同时保持系统易于部署。
- **灵巧手控制**：提出基于学习的重定向方法，无需手动参数调整即可生成平滑、自然的手部运动。

### 数据采集与学习框架
- **高效数据采集**：HumDex 支持高效采集人类运动数据，为后续学习提供基础。
- **两阶段模仿学习**：
  - **第一阶段**：在多样化人类运动数据上预训练，学习通用操作先验。
  - **第二阶段**：在机器人数据上微调，弥合具身差异，实现精确执行。

### 实验与结果
- 该方法显著提升了对新构型、新物体和新背景的泛化能力。
- 数据采集成本极低，系统完全可复现。

### 开源信息
- 项目已完全开源，代码与文档可在 GitHub 获取：https://github.com/physical-superintelligence-lab/humdex

## Overview
This paper investigates humanoid whole-body dexterous manipulation, where the efficient collection of high-quality demonstration data remains a central bottleneck. Existing teleoperation systems often suffer from limited portability, occlusion, or insufficient precision, which hinders their applicability to complex whole-body tasks. To address these challenges, we introduce HumDex, a portable teleoperation system designed for humanoid whole-body dexterous manipulation. Our system leverages IMU-based motion tracking to address the portability-precision trade-off, enabling accurate full-body tracking while remaining easy to deploy. For dexterous hand control, we further introduce a learning-based retargeting method that generates smooth and natural hand motions without manual parameter tuning. Beyond teleoperation, HumDex enables efficient collection of human motion data. Building on this capability, we propose a two-stage imitation learning framework that first pre-trains on diverse human motion data to learn generalizable priors, and then fine-tunes on robot data to bridge the embodiment gap for precise execution. We demonstrate that this approach significantly improves generalization to new configurations, objects, and backgrounds with minimal data acquisition costs. The entire system is fully reproducible and open-sourced at https://github.com/physical-superintelligence-lab/humdex.

## 参考
- http://arxiv.org/abs/2603.12260v2

## 개요
휴머노이드 로봇의 전신 기민한 조작은 고품질 시연 데이터 수집 효율이 낮다는 핵심 병목에 직면해 있습니다. 기존 원격 조작 시스템은 휴대성 부족, 시야 가림 또는 정밀도 부족 등의 문제가普遍적으로 존재하여 복잡한 전신 작업을 수행하기 어렵습니다. HumDex는 IMU 모션 추적 기술을 채택하여 휴대성을 유지하면서도 정밀한 전신 자세 추적을 구현합니다. 기민한 손 제어를 위해 수동 파라미터 조정이 필요 없는 학습 기반 리타게팅 방법을 도입하여 부드럽고 자연스러운 파지 동작을 생성합니다. 이 시스템은 효율적인 인간 모션 데이터 수집을 지원할 뿐만 아니라 2단계 모방 학습 프레임워크를 구축합니다: 먼저 다양한 인간 모션 데이터에서 사전 학습하여 일반적인 사전 지식을 학습하고, 이후 로봇 데이터에서 미세 조정하여 구현 차이를 해소합니다. 실험 결과, 이 방법은 매우 낮은 데이터 수집 비용으로 새로운 구성, 새로운 물체 및 새로운 배경에 대한 일반화 능력을显著히 향상시킵니다.

## 핵심 내용
### 핵심 과제
- 휴머노이드 로봇의 전신 기민한 조작의 주요 병목은 고품질 시연 데이터의 수집 효율입니다.
- 기존 원격 조작 시스템은 휴대성, 시야 가림 및 정밀도 간의 트레이드오프가 존재하여 복잡한 전신 작업 요구를 충족하기 어렵습니다.

### 시스템 설계
- **휴대성과 정밀도의 균형**: IMU 모션 추적 기술을 채택하여 정밀한 전신 자세 추적을 구현하면서도 시스템 배포 용이성을 유지합니다.
- **기민한 손 제어**: 수동 파라미터 조정이 필요 없는 학습 기반 리타게팅 방법을 제안하여 부드럽고 자연스러운 손 동작을 생성합니다.

### 데이터 수집 및 학습 프레임워크
- **효율적인 데이터 수집**: HumDex는 인간 모션 데이터의 효율적인 수집을 지원하여 후속 학습의 기반을 제공합니다.
- **2단계 모방 학습**:
  - **1단계**: 다양한 인간 모션 데이터에서 사전 학습하여 일반적인 조작 사전 지식을 학습합니다.
  - **2단계**: 로봇 데이터에서 미세 조정하여 구현 차이를 해소하고 정밀한 실행을 구현합니다.

### 실험 및 결과
- 이 방법은 새로운 구성, 새로운 물체 및 새로운 배경에 대한 일반화 능력을显著히 향상시킵니다.
- 데이터 수집 비용이 매우 낮으며 시스템은 완전히 재현 가능합니다.

### 오픈소스 정보
- 프로젝트는 완전히 오픈소스로 제공되며 코드와 문서는 GitHub에서 확인할 수 있습니다: https://github.com/physical-superintelligence-lab/humdex
