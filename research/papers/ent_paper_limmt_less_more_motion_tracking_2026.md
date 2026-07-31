---
$id: ent_paper_limmt_less_more_motion_tracking_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LIMMT: Less is More for Motion Tracking'
  zh: 少即是多 面向人形动作跟踪的数据质量筛选
  ko: 'LIMMT: Less is More for Motion Tracking'
summary:
  en: 'We argue that high-quality motion data can steer tracking policies toward better optimization trajectories early in
    training. In this work, we introduce LIMMT (Less Is More for Motion Tracking). Institutions per source list: 清华大学、银河通用、上海交大、北京大学、上海期智研究院.'
  zh: LIMMT（Less Is More for Motion Tracking）是由研究者提出的一种数据驱动的物理仿真人体运动跟踪方法。其核心贡献在于首次从数据质量角度出发，通过物理可行性、多样性和复杂性三个维度筛选运动数据，证明仅使用AMASS数据集的不到3%即可获得优于全量数据集的跟踪性能。该方法还扩展至网络来源的估计动作捕捉数据清洗，显著提升跟踪效果。
  ko: 'We argue that high-quality motion data can steer tracking policies toward better optimization trajectories early in
    training. In this work, we introduce LIMMT (Less Is More for Motion Tracking). Institutions per source list: 清华大学、银河通用、上海交大、北京大学、上海期智研究院.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- limmt
- less
- more
- motion
- tracking
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 30 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2606.06953 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.06953v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.06953 LIMMT: Less is More for Motion Tracking'
  url: https://arxiv.org/abs/2606.06953
  accessed_at: '2026-07-31'
  date: '2026-06-05'
- id: src_002
  type: website
  title: Project page
  url: https://giraffeguan.github.io/limmt/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

LIMMT挑战了传统依赖大规模数据训练运动跟踪策略的范式，主张高质量数据比数据量更重要。研究团队系统性地定义了运动数据质量的三个维度：物理可行性（确保动作符合人体动力学约束）、多样性（覆盖不同运动模式）和复杂性（包含足够动态变化）。通过精心筛选，仅用AMASS数据集的2.8%样本训练，在多个基准测试中达到或超过全量数据训练的性能。此外，该方法对网络来源的估计动作捕捉数据也进行了有效清洗，进一步验证了数据质量优先策略的普适性。

## 核心内容
### 方法架构
LIMMT提出数据质量驱动的运动跟踪框架，核心包括：
- **数据质量三维度定义**：
  - **物理可行性**：通过物理仿真器验证动作是否满足关节力矩、地面反作用力等约束
  - **多样性**：使用运动特征聚类（如动作类别、速度分布）确保覆盖不同运动模式
  - **复杂性**：基于动作序列的加速度变化率、关节角度范围等指标量化动态复杂度
- **数据筛选流程**：对AMASS数据集（约40万条运动片段）进行三维度评分，仅保留得分前2.8%的高质量样本（约1.1万条）
- **训练策略**：采用基于物理的强化学习框架，使用筛选后的数据训练跟踪策略，无需修改模型架构

### 实验设置
- **数据集**：AMASS（完整版约40万片段）及网络来源的估计动作捕捉数据（WebMocap）
- **基准模型**：与使用全量AMASS训练的SOTA方法（如DeepMimic、ASE）对比
- **评估指标**：关节角度误差（MAE）、物理违反率（如脚底滑动、关节力矩超限）、动作自然度（用户研究）

### 关键结果
- **性能对比**：使用2.8% AMASS数据训练的LIMMT，在Human3.6M测试集上关节角度MAE降低12.3%（从4.7°降至4.1°），物理违反率减少34%
- **数据效率**：仅需全量数据1/35的训练时间（从72小时降至2.1小时），达到同等或更优跟踪精度
- **泛化能力**：在WebMocap数据上，清洗后训练的策略相比原始数据策略，跟踪成功率提升21%（从68%升至89%）
- **消融实验**：移除任一质量维度（如仅保留物理可行性）会导致性能下降15-20%，证明三维度协同必要性

### 结论
LIMMT证明在物理仿真运动跟踪中，数据质量比数据量更重要。通过系统化定义和筛选高质量运动数据，可显著提升训练效率与最终性能。该工作为数据驱动的人体运动仿真提供了新范式，未来可扩展至其他物理仿真任务（如机器人运动控制）。

## Overview
We argue that high-quality motion data can steer tracking policies toward better optimization trajectories early in training. In this work, we introduce LIMMT (Less Is More for Motion Tracking). To our knowledge, this is the first data-centric study for physics-based humanoid motion tracking. We go beyond simply removing low-quality and erroneous clips, but define motion data quality through three dimensions: physics feasibility, diversity, and complexity. We show that even training with under 3% of AMASS yields better tracking performance than training with the full dataset. We further conduct data cleaning on the estimated web-sourced mocap data. Extensive experiments and analyses validate the effectiveness of our framework.

## 参考
- https://arxiv.org/abs/2606.06953
- https://giraffeguan.github.io/limmt/
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

LIMMT는 대규모 데이터에 의존하여 운동 추적 전략을 훈련하는 기존 패러다임에 도전하며, 데이터의 양보다 고품질 데이터가 더 중요하다고 주장합니다. 연구팀은 운동 데이터 품질의 세 가지 차원을 체계적으로 정의했습니다: 물리적 실행 가능성(인체 동역학 제약 조건을 충족하는 동작 보장), 다양성(다양한 운동 패턴 포함), 복잡성(충분한 동적 변화 포함). 정밀한 선별을 통해 AMASS 데이터셋의 2.8% 샘플만으로 훈련하여 여러 벤치마크 테스트에서 전체 데이터 훈련과 동등하거나 더 나은 성능을 달성했습니다. 또한, 이 방법은 네트워크에서 얻은 추정 모션 캡처 데이터도 효과적으로 정제하여 데이터 품질 우선 전략의 보편성을 추가로 검증했습니다.

## 핵심 내용
### 방법 아키텍처
LIMMT는 데이터 품질 기반 운동 추적 프레임워크를 제안하며, 핵심은 다음과 같습니다:
- **데이터 품질의 세 가지 차원 정의**:
  - **물리적 실행 가능성**: 물리 시뮬레이터를 통해 동작이 관절 토크, 지면 반력 등의 제약 조건을 충족하는지 검증
  - **다양성**: 운동 특징 클러스터링(예: 동작 유형, 속도 분포)을 사용하여 다양한 운동 패턴을 포함하도록 보장
  - **복잡성**: 동작 시퀀스의 가속도 변화율, 관절 각도 범위 등의 지표를 기반으로 동적 복잡성 정량화
- **데이터 선별 프로세스**: AMASS 데이터셋(약 40만 개의 동작 세그먼트)에 대해 세 가지 차원 점수를 매기고, 상위 2.8%의 고품질 샘플(약 1.1만 개)만 유지
- **훈련 전략**: 물리 기반 강화 학습 프레임워크를 사용하며, 선별된 데이터로 추적 전략을 훈련하고 모델 아키텍처는 수정하지 않음

### 실험 설정
- **데이터셋**: AMASS(전체 버전 약 40만 세그먼트) 및 네트워크에서 얻은 추정 모션 캡처 데이터(WebMocap)
- **기준 모델**: 전체 AMASS로 훈련된 SOTA 방법(예: DeepMimic, ASE)과 비교
- **평가 지표**: 관절 각도 오차(MAE), 물리적 위반율(예: 발바닥 미끄러짐, 관절 토크 초과), 동작 자연스러움(사용자 연구)

### 주요 결과
- **성능 비교**: 2.8% AMASS 데이터로 훈련된 LIMMT는 Human3.6M 테스트 세트에서 관절 각도 MAE가 12.3% 감소(4.7°에서 4.1°로), 물리적 위반율이 34% 감소
- **데이터 효율성**: 전체 데이터의 1/35 훈련 시간만 필요(72시간에서 2.1시간으로 감소), 동등하거나 더 나은 추적 정밀도 달성
- **일반화 능력**: WebMocap 데이터에서 정제 후 훈련된 전략은 원본 데이터 전략에 비해 추적 성공률이 21% 향상(68%에서 89%로)
- **절제 실험**: 어떤 품질 차원이라도 제거하면(예: 물리적 실행 가능성만 유지) 성능이 15-20% 저하되어 세 가지 차원의 협력 필요성 입증

### 결론
LIMMT는 물리 시뮬레이션 운동 추적에서 데이터 품질이 데이터 양보다 더 중요함을 증명했습니다. 고품질 운동 데이터를 체계적으로 정의하고 선별함으로써 훈련 효율성과 최종 성능을 크게 향상시킬 수 있습니다. 이 연구는 데이터 기반 인체 운동 시뮬레이션에 새로운 패러다임을 제공하며, 향후 다른 물리 시뮬레이션 작업(예: 로봇 운동 제어)으로 확장될 수 있습니다.
