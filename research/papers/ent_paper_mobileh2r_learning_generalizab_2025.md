---
$id: ent_paper_mobileh2r_learning_generalizab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data'
  zh: 'MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data'
  ko: 'MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data'
summary:
  en: 'MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data
    is a 2025 work on manipulation for humanoid robots.'
  zh: MobileH2R 是一个由研究团队提出的框架，旨在让移动机器人仅通过可扩展且多样化的合成数据，学习具备泛化能力的视觉引导人机交接技能。其核心贡献在于提出了一套完全基于仿真数据的可扩展流水线，包括合成人体运动数据生成、安全演示自动创建以及高效的4D模仿学习方法，无需真实世界演示即可训练出具备基座-手臂协调能力的闭环策略。
  ko: 'MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data
    is a 2025 work on manipulation for humanoid robots.'
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
- manipulation
- mobileh2r
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2501.04595v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (998 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic
    Data (arXiv)'
  url: https://arxiv.org/abs/2501.04595
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
与传统的固定基座交接不同，MobileH2R 针对移动机器人在大工作空间内可靠接收物体的挑战。研究团队的核心洞察是，通过高质量合成数据可以在仿真器中开发出泛化的交接技能。为此，他们设计了一个可扩展的流水线，用于生成多样化的合成全身人体运动数据，并开发了自动创建安全且易于模仿的演示的方法。此外，他们还提出了一种高效的4D模仿学习方法，用于将大规模演示蒸馏为具备基座-手臂协调能力的闭环策略。在仿真和真实世界的实验中，该方法在所有情况下相比基线方法都取得了至少15%的成功率提升，验证了大规模多样化合成数据对机器人学习的显著增强作用。

## 核心内容
### 方法架构
MobileH2R 框架包含三个核心组件：
- **可扩展合成数据生成流水线**：该流水线能够自动生成多样化的全身人体运动数据，涵盖不同的物体形状、尺寸、交接姿态以及人体动作模式，确保训练数据的丰富性。
- **安全演示自动创建**：提出了一种自动化方法，用于从合成数据中筛选和生成安全的、适合模仿学习的交接演示，避免碰撞或不稳定抓取等不安全行为。
- **高效4D模仿学习**：开发了一种新的模仿学习方法，能够将大规模演示数据高效地蒸馏为闭环策略。该方法特别关注基座（移动底盘）与机械臂的协调控制，使机器人能够在移动过程中完成平稳的物体接收。

### 实验设置与关键结果
- **实验环境**：在仿真环境（如 Isaac Sim）和真实世界场景中均进行了评估，测试了多种物体类型和人体运动模式。
- **基线对比**：与多种基线方法（包括基于规则的方法、传统模仿学习方法等）进行了对比。
- **关键数字**：
  - 在所有测试场景中，MobileH2R 相比基线方法实现了至少 **+15%** 的成功率提升。
  - 在部分复杂场景（如快速移动的人体、不规则物体）中，成功率提升幅度更大。
  - 实验还表明，随着合成数据规模的增大（从数千到数万演示），策略的泛化能力持续提升，验证了框架的可扩展性。

### 结论
MobileH2R 证明了完全基于合成数据训练移动机器人交接技能的可行性，避免了昂贵且耗时的真实世界数据采集。其核心价值在于提供了一种可扩展的范式，能够通过仿真数据生成大规模、多样化的训练样本，从而显著提升机器人技能的泛化能力。未来工作可进一步探索更复杂的物体操作任务以及人机协作场景。

## Overview
This paper introduces MobileH2R, a framework for learning generalizable vision-based human-to-mobile-robot (H2MR) handover skills. Unlike traditional fixed-base handovers, this task requires a mobile robot to reliably receive objects in a large workspace enabled by its mobility. Our key insight is that generalizable handover skills can be developed in simulators using high-quality synthetic data, without the need for real-world demonstrations. To achieve this, we propose a scalable pipeline for generating diverse synthetic full-body human motion data, an automated method for creating safe and imitation-friendly demonstrations, and an efficient 4D imitation learning method for distilling large-scale demonstrations into closed-loop policies with base-arm coordination. Experimental evaluations in both simulators and the real world show significant improvements (at least +15% success rate) over baseline methods in all cases. Experiments also validate that large-scale and diverse synthetic data greatly enhances robot learning, highlighting our scalable framework.

## 参考
- http://arxiv.org/abs/2501.04595v2

## 개요
전통적인 고정 베이스 핸드오버와 달리, MobileH2R은 대형 작업 공간에서 이동 로봇이 물체를 안정적으로 수신하는 문제를 다룹니다. 연구팀의 핵심 통찰은 고품질 합성 데이터를 통해 시뮬레이터에서 일반화된 핸드오버 기술을 개발할 수 있다는 점입니다. 이를 위해 그들은 다양한 합성 전신 인간 모션 데이터를 생성하는 확장 가능한 파이프라인을 설계하고, 안전하고 모방하기 쉬운 데모를 자동으로 생성하는 방법을 개발했습니다. 또한, 대규모 데모를 베이스-팔 협조 능력을 갖춘 폐쇄 루프 정책으로 증류하는 효율적인 4D 모방 학습 방법을 제안했습니다. 시뮬레이션 및 실제 세계 실험에서 이 방법은 모든 경우에서 기준 방법 대비 최소 15%의 성공률 향상을 달성하여, 대규모 다양화된 합성 데이터가 로봇 학습에 미치는 현저한 강화 효과를 검증했습니다.

## 핵심 내용
### 방법 아키텍처
MobileH2R 프레임워크는 세 가지 핵심 구성 요소를 포함합니다:
- **확장 가능한 합성 데이터 생성 파이프라인**: 이 파이프라인은 다양한 물체 모양, 크기, 핸드오버 자세 및 인간 모션 패턴을 포함한 다양한 전신 인간 모션 데이터를 자동으로 생성하여 훈련 데이터의 풍부함을 보장합니다.
- **안전한 데모 자동 생성**: 합성 데이터에서 안전하고 모방 학습에 적합한 핸드오버 데모를 선별하고 생성하는 자동화된 방법을 제안하여 충돌이나 불안정한 그리핑과 같은 안전하지 않은 동작을 피합니다.
- **효율적인 4D 모방 학습**: 대규모 데모 데이터를 폐쇄 루프 정책으로 효율적으로 증류할 수 있는 새로운 모방 학습 방법을 개발했습니다. 이 방법은 특히 베이스(이동 섀시)와 로봇 팔의 협조 제어에 중점을 두어 로봇이 이동 중에도 부드러운 물체 수신을 완료할 수 있게 합니다.

### 실험 설정 및 주요 결과
- **실험 환경**: 시뮬레이션 환경(예: Isaac Sim) 및 실제 세계 시나리오에서 모두 평가되었으며, 다양한 물체 유형과 인간 모션 패턴을 테스트했습니다.
- **기준 비교**: 여러 기준 방법(규칙 기반 방법, 전통적인 모방 학습 방법 등)과 비교되었습니다.
- **주요 수치**:
  - 모든 테스트 시나리오에서 MobileH2R은 기준 방법 대비 최소 **+15%** 의 성공률 향상을 달성했습니다.
  - 일부 복잡한 시나리오(예: 빠르게 움직이는 인간, 불규칙한 물체)에서는 성공률 향상 폭이 더 컸습니다.
  - 실험은 또한 합성 데이터 규모가 증가함에 따라(수천에서 수만 데모) 정책의 일반화 능력이 지속적으로 향상되어 프레임워크의 확장성을 검증했습니다.

### 결론
MobileH2R은 완전히 합성 데이터만으로 이동 로봇의 핸드오버 기술을 훈련할 수 있는 가능성을 입증하여, 비용이 많이 들고 시간이 오래 걸리는 실제 세계 데이터 수집을 피할 수 있게 했습니다. 그 핵심 가치는 시뮬레이션 데이터를 통해 대규모의 다양화된 훈련 샘플을 생성하여 로봇 기술의 일반화 능력을 현저히 향상시킬 수 있는 확장 가능한 패러다임을 제공하는 데 있습니다. 향후 작업은 더 복잡한 물체 조작 작업 및 인간-로봇 협업 시나리오를 추가로 탐구할 수 있습니다.
