---
$id: ent_paper_one_shot_humanoid_whole_body_m_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: One-shot Humanoid Whole-body Motion Learning
  zh: One-shot Humanoid Whole-body Motion Learning
  ko: One-shot Humanoid Whole-body Motion Learning
summary:
  en: One-shot Humanoid Whole-body Motion Learning is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.
  zh: One-shot Humanoid Whole-body Motion Learning 是2025年提出的人形机器人全身运动学习方法，由相关研究团队完成。其核心贡献在于仅需单个非行走动作样本，结合辅助行走动作和预训练模型，即可高效学习新动作，并在CMU
    MoCap数据集上取得优于基线方法的性能。
  ko: One-shot Humanoid Whole-body Motion Learning is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.
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
- loco_manipulation
- one_shot_humanoid_whole_body_m
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.25241v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (775 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: One-shot Humanoid Whole-body Motion Learning (arXiv)
  url: https://arxiv.org/abs/2510.25241
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该工作针对人形机器人全身运动学习数据采集成本高的问题，提出了一种数据高效的单样本适应方法。方法利用保序最优传输计算行走与非行走序列的距离，通过测地线插值生成中间姿态骨架，再经碰撞避免优化和重定向后，在仿真环境中通过强化学习进行策略适应。实验表明，该方法在CMU MoCap数据集上各项指标均优于现有基线。

## 核心内容
### 方法架构
- **核心思想**：利用单个非行走目标样本，结合辅助行走动作和基于行走训练的基模型，实现数据高效的全身运动学习。
- **关键步骤**：
  1. **保序最优传输**：计算行走与非行走序列之间的距离，保持时间顺序一致性。
  2. **测地线插值**：沿测地线生成新的中间姿态骨架，实现动作平滑过渡。
  3. **碰撞避免优化**：对生成的骨架进行碰撞检测与修正，确保物理可行性。
  4. **重定向与仿真集成**：将优化后的骨架重定向到人形机器人模型，并集成到仿真环境中。
  5. **强化学习策略适应**：在仿真环境中通过RL训练策略，使机器人能够执行新动作。

### 实验设置
- **数据集**：CMU MoCap数据集，包含多种人体运动序列。
- **基线方法**：对比了传统多样本学习方法与单样本适应方法。
- **评估指标**：包括动作保真度、平衡性、碰撞避免成功率等。

### 关键结果
- 在CMU MoCap数据集上，该方法在所有评估指标上均优于基线方法。
- 单样本学习显著降低了数据采集成本，同时保持了动作质量。
- 代码已开源：https://github.com/hhuang-code/One-shot-WBM

### 结论
该方法通过保序最优传输与测地线插值，实现了人形机器人全身运动的高效单样本学习，为数据稀缺场景下的机器人运动学习提供了新思路。

## Overview
Whole-body humanoid motion represents a fundamental challenge in robotics, requiring balance, coordination, and adaptability to enable human-like behaviors. However, existing methods typically require multiple training samples per motion, rendering the collection of high-quality human motion datasets both labor-intensive and costly. To address this, we propose a data-efficient adaptation approach that learns a new humanoid motion from a single non-walking target sample together with auxiliary walking motions and a walking-trained base model. The core idea lies in leveraging order-preserving optimal transport to compute distances between walking and non-walking sequences, followed by interpolation along geodesics to generate new intermediate pose skeletons, which are then optimized for collision-free configurations and retargeted to the humanoid before integration into a simulated environment for policy adaptation via reinforcement learning. Experimental evaluations on the CMU MoCap dataset demonstrate that our method consistently outperforms baselines, achieving superior performance across metrics. Our code is available at: https://github.com/hhuang-code/One-shot-WBM.

## 参考
- http://arxiv.org/abs/2510.25241v2

## 개요
본 연구는 휴머노이드 로봇의 전신 운동 학습 데이터 수집 비용이 높은 문제를 해결하기 위해, 데이터 효율적인 단일 샘플 적응 방법을 제안한다. 이 방법은 순서 보존 최적 수송(Order-preserving Optimal Transport)을 이용해 보행 및 비보행 시퀀스 간의 거리를 계산하고, 측지선 보간(Geodesic Interpolation)을 통해 중간 자세 골격을 생성한 후, 충돌 회피 최적화와 리타게팅(Retargeting)을 거쳐 시뮬레이션 환경에서 강화 학습을 통한 정책 적응을 수행한다. 실험 결과, 이 방법은 CMU MoCap 데이터셋에서 모든 지표에서 기존 베이스라인보다 우수한 성능을 보였다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 단일 비보행 대상 샘플을 활용하고, 보조 보행 동작 및 보행 기반 훈련된 기본 모델을 결합하여 데이터 효율적인 전신 운동 학습을 구현한다.
- **주요 단계**:
  1. **순서 보존 최적 수송**: 보행 및 비보행 시퀀스 간의 거리를 계산하며, 시간 순서 일관성을 유지한다.
  2. **측지선 보간**: 측지선을 따라 새로운 중간 자세 골격을 생성하여 동작의 부드러운 전환을 구현한다.
  3. **충돌 회피 최적화**: 생성된 골격에 대해 충돌 감지 및 수정을 수행하여 물리적 실현 가능성을 보장한다.
  4. **리타게팅 및 시뮬레이션 통합**: 최적화된 골격을 휴머노이드 로봇 모델에 리타게팅하고 시뮬레이션 환경에 통합한다.
  5. **강화 학습 정책 적응**: 시뮬레이션 환경에서 RL을 통해 정책을 훈련하여 로봇이 새로운 동작을 수행할 수 있게 한다.

### 실험 설정
- **데이터셋**: CMU MoCap 데이터셋으로, 다양한 인간 운동 시퀀스를 포함한다.
- **베이스라인 방법**: 기존의 다중 샘플 학습 방법과 단일 샘플 적응 방법을 비교한다.
- **평가 지표**: 동작 충실도, 균형성, 충돌 회피 성공률 등을 포함한다.

### 주요 결과
- CMU MoCap 데이터셋에서 이 방법은 모든 평가 지표에서 베이스라인 방법보다 우수한 성능을 보였다.
- 단일 샘플 학습은 데이터 수집 비용을 크게 줄이면서 동작 품질을 유지했다.
- 코드는 오픈소스로 공개됨: https://github.com/hhuang-code/One-shot-WBM

### 결론
이 방법은 순서 보존 최적 수송과 측지선 보간을 통해 휴머노이드 로봇의 전신 운동을 효율적으로 단일 샘플 학습할 수 있게 하며, 데이터가 부족한 상황에서의 로봇 운동 학습에 새로운 접근 방식을 제공한다.
