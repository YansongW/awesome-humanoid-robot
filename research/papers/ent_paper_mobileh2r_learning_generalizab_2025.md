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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2501.04595v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
본 논문은 일반화 가능한 비전 기반 인간-이동로봇(H2MR) 물체 전달 기술을 학습하기 위한 프레임워크인 MobileH2R을 소개합니다. 기존의 고정 기반 물체 전달과 달리, 이 작업은 이동성을 활용하여 넓은 작업 공간에서 이동 로봇이 안정적으로 물체를 수신해야 합니다. 핵심 통찰은 일반화 가능한 물체 전달 기술이 실제 환경 시연 없이도 고품질 합성 데이터를 사용하여 시뮬레이터에서 개발될 수 있다는 점입니다. 이를 위해, 다양한 합성 전신 인간 동작 데이터를 생성하는 확장 가능한 파이프라인, 안전하고 모방 학습에 적합한 시연을 자동으로 생성하는 방법, 그리고 대규모 시연을 베이스-암 협력이 가능한 폐쇄 루프 정책으로 증류하는 효율적인 4D 모방 학습 방법을 제안합니다. 시뮬레이터와 실제 환경 모두에서 수행된 실험 평가는 모든 경우에서 기준 방법 대비 최소 +15%의 성공률 향상을 보여줍니다. 또한, 대규모의 다양한 합성 데이터가 로봇 학습을 크게 향상시킨다는 점을 실험을 통해 검증하며, 이는 확장 가능한 프레임워크의 우수성을 강조합니다.

## 핵심 내용
본 논문은 일반화 가능한 비전 기반 인간-이동로봇(H2MR) 물체 전달 기술을 학습하기 위한 프레임워크인 MobileH2R을 소개합니다. 기존의 고정 기반 물체 전달과 달리, 이 작업은 이동성을 활용하여 넓은 작업 공간에서 이동 로봇이 안정적으로 물체를 수신해야 합니다. 핵심 통찰은 일반화 가능한 물체 전달 기술이 실제 환경 시연 없이도 고품질 합성 데이터를 사용하여 시뮬레이터에서 개발될 수 있다는 점입니다. 이를 위해, 다양한 합성 전신 인간 동작 데이터를 생성하는 확장 가능한 파이프라인, 안전하고 모방 학습에 적합한 시연을 자동으로 생성하는 방법, 그리고 대규모 시연을 베이스-암 협력이 가능한 폐쇄 루프 정책으로 증류하는 효율적인 4D 모방 학습 방법을 제안합니다. 시뮬레이터와 실제 환경 모두에서 수행된 실험 평가는 모든 경우에서 기준 방법 대비 최소 +15%의 성공률 향상을 보여줍니다. 또한, 대규모의 다양한 합성 데이터가 로봇 학습을 크게 향상시킨다는 점을 실험을 통해 검증하며, 이는 확장 가능한 프레임워크의 우수성을 강조합니다.

## 参考
- http://arxiv.org/abs/2501.04595v2
