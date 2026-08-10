---
$id: ent_paper_iterative_closed_loop_motion_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control
  zh: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control
  ko: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control
summary:
  en: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control is a 2026 work on physics-based
    character animation for humanoid robots.
  zh: 这是一篇2026年关于人形机器人物理仿真控制的工作，提出了闭环自动运动数据生成与迭代框架。核心贡献在于通过物理指标和客观评估实现策略与数据的难度迭代，突破原有性能上限。在PHC单基元跟踪器上，仅用AMASS数据集约1/10的数据量，测试集平均失败率降低45%。
  ko: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control is a 2026 work on physics-based
    character animation for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- iterative_closed_loop_motion_s
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.21599v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (629 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control (arXiv)
  url: https://arxiv.org/abs/2602.21599
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
物理仿真人形控制依赖具有多样数据分布的运动数据集进行训练，但数据集固定的难度分布限制了控制策略的性能上限。同时，通过专业动作捕捉系统获取高质量数据的方式受成本制约，难以实现大规模扩展。为此，本文提出闭环自动运动数据生成与迭代框架，能够生成包含武术、舞蹈、格斗、运动、体操等丰富动作语义的高质量运动数据。该框架通过物理指标和客观评估实现策略与数据的难度迭代，使训练出的跟踪器突破原有难度限制。

## 核心内容
### 方法架构
- 提出闭环自动运动数据生成与迭代框架，核心包含两个关键模块：
  - **数据生成模块**：自动生成具有丰富动作语义的高质量运动数据，涵盖武术、舞蹈、格斗、运动、体操等类别
  - **难度迭代模块**：通过物理指标（如关节力矩、接触力等）和客观评估（如跟踪误差、稳定性指标）实现策略与数据的协同迭代

### 实验设置
- 基准模型：PHC单基元跟踪器
- 训练数据：仅使用AMASS数据集约1/10的数据量
- 测试集：包含2201个运动片段
- 评估指标：平均失败率

### 关键结果
- 与基线相比，测试集平均失败率降低45%
- 通过难度迭代机制，训练出的跟踪器能够突破原始数据集的难度限制
- 全面的消融实验和对比实验验证了框架的合理性和优势

### 结论
该框架有效解决了数据集固定难度分布导致的性能瓶颈问题，同时降低了高质量运动数据的获取成本，为人形机器人物理仿真控制的大规模扩展提供了可行方案。

## Overview
Physics-based humanoid control relies on training with motion datasets that have diverse data distributions. However, the fixed difficulty distribution of datasets limits the performance ceiling of the trained control policies. Additionally, the method of acquiring high-quality data through professional motion capture systems is constrained by costs, making it difficult to achieve large-scale scalability. To address these issues, we propose a closed-loop automated motion data generation and iterative framework. It can generate high-quality motion data with rich action semantics, including martial arts, dance, combat, sports, gymnastics, and more. Furthermore, our framework enables difficulty iteration of policies and data through physical metrics and objective evaluations, allowing the trained tracker to break through its original difficulty limits. On the PHC single-primitive tracker, using only approximately 1/10 of the AMASS dataset size, the average failure rate on the test set (2201 clips) is reduced by 45% compared to the baseline. Finally, we conduct comprehensive ablation and comparative experiments to highlight the rationality and advantages of our framework.

## 参考
- http://arxiv.org/abs/2602.21599v2

## 개요
물리 시뮬레이션 휴머노이드 제어는 다양한 데이터 분포를 가진 모션 데이터셋을 기반으로 훈련되지만, 데이터셋의 고정된 난이도 분포는 제어 정책의 성능 상한을 제한합니다. 또한, 전문 모션 캡처 시스템을 통해 고품질 데이터를 획득하는 방식은 비용 제약으로 인해 대규모 확장이 어렵습니다. 이를 해결하기 위해, 본 논문은 폐루프 자동 모션 데이터 생성 및 반복 프레임워크를 제안하며, 무술, 춤, 격투, 스포츠, 체조 등 풍부한 동작 의미를 포함한 고품질 모션 데이터를 생성할 수 있습니다. 이 프레임워크는 물리 지표와 객관적 평가를 통해 정책과 데이터의 난이도 반복을 구현하여, 훈련된 트래커가 기존 난이도 제한을 돌파할 수 있게 합니다.

## 핵심 내용
### 방법 아키텍처
- 폐루프 자동 모션 데이터 생성 및 반복 프레임워크를 제안하며, 핵심은 두 가지 주요 모듈로 구성됩니다:
  - **데이터 생성 모듈**: 무술, 춤, 격투, 스포츠, 체조 등 범주를 포함한 풍부한 동작 의미를 가진 고품질 모션 데이터를 자동 생성
  - **난이도 반복 모듈**: 물리 지표(예: 관절 토크, 접촉력 등)와 객관적 평가(예: 추적 오차, 안정성 지표)를 통해 정책과 데이터의 협력적 반복 구현

### 실험 설정
- 기준 모델: PHC 단일 프리미티브 트래커
- 훈련 데이터: AMASS 데이터셋의 약 1/10 데이터량만 사용
- 테스트 세트: 2201개 모션 클립 포함
- 평가 지표: 평균 실패율

### 주요 결과
- 기준선 대비 테스트 세트 평균 실패율 45% 감소
- 난이도 반복 메커니즘을 통해 훈련된 트래커가 원본 데이터셋의 난이도 제한을 돌파할 수 있음
- 포괄적인 절제 실험 및 비교 실험을 통해 프레임워크의 합리성과 우수성 검증

### 결론
이 프레임워크는 데이터셋의 고정된 난이도 분포로 인한 성능 병목 문제를 효과적으로 해결하며, 고품질 모션 데이터 획득 비용을 낮추어 휴머노이드 로봇 물리 시뮬레이션 제어의 대규모 확장을 위한 실현 가능한 솔루션을 제공합니다.
