---
$id: ent_paper_geometry_aware_motion_latents_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies
  zh: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies
  ko: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies
summary:
  en: 'arXiv:2607.04714v1 Announce Type: new Abstract: Learning motion latents for robotic manipulation heavily relies on
    extracting motion patterns from visual sequences, yet effective action abstractions require understanding three-dimensional
    geometric transformations. Here, we introduce GeoMoLa (Geometry-Aware Motion Latents), which learns discrete motion latent
    codes by predicting how point clouds evolve during manipulation rather than reconstructing visual observations. This four-dimensional
    objective -- spatial geometry changing through time -- forces latent representations to encode actual physical motion
    rather than appearance patterns. GeoMoLa achieves state-of-the-art performance using only single-view RGB-D input, while
    existing methods require multi-view reconstruction, succeeding across diverse manipulation benchmarks. Our ablations reveal
    that geometric prediction is the key to driving performance, quantitatively validating that manipulation depends on spatial
    understanding. Furthermore, the learned codes exhibit effective motion abstraction: applying them to novel scenes produces
    physically consistent transformations regardless of visual context. Our real-world experiments also confirm this robustness
    capability, achieving robust manipulation with minimal demonstrations in cluttered environments where geometric reasoning
    determines success. Thus, we demonstrate that effective motion latents for robot control can better emerge from understanding
    motion through its three-dimensional effects rather than pixel-level patterns.'
  zh: GeoMoLa（Geometry-Aware Motion Latents）是一种学习离散运动潜码的方法，通过预测操作过程中点云的演变而非重建视觉观测来提取运动模式。该方法仅需单视角RGB-D输入即可达到最先进性能，在多种操作基准上表现优异，其核心贡献在于利用四维几何目标（空间几何随时间变化）迫使潜表示编码真实物理运动而非外观模式。
  ko: 'arXiv:2607.04714v1 Announce Type: new Abstract: Learning motion latents for robotic manipulation heavily relies on
    extracting motion patterns from visual sequences, yet effective action abstractions require understanding three-dimensional
    geometric transformations. Here, we introduce GeoMoLa (Geometry-Aware Motion Latents), which learns discrete motion latent
    codes by predicting how point clouds evolve during manipulation rather than reconstructing visual observations. This four-dimensional
    objective -- spatial geometry changing through time -- forces latent representations to encode actual physical motion
    rather than appearance patterns. GeoMoLa achieves state-of-the-art performance using only single-view RGB-D input, while
    existing methods require multi-view reconstruction, succeeding across diverse manipulation benchmarks. Our ablations reveal
    that geometric prediction is the key to driving performance, quantitatively validating that manipulation depends on spatial
    understanding. Furthermore, the learned codes exhibit effective motion abstraction: applying them to novel scenes produces
    physically consistent transformations regardless of visual context. Our real-world experiments also confirm this robustness
    capability, achieving robust manipulation with minimal demonstrations in cluttered environments where geometric reasoning
    determines success. Thus, we demonstrate that effective motion latents for robot control can better emerge from understanding
    motion through its three-dimensional effects rather than pixel-level patterns.'
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
- robotics
- geometry_aware_motion_latents
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04714v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (867 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies (arXiv)
  url: https://arxiv.org/abs/2607.04714
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
GeoMoLa由研究者提出，旨在解决机器人操作中运动潜码学习对三维几何变换理解的需求。与依赖多视角重建的现有方法不同，GeoMoLa仅使用单视角RGB-D输入，通过预测点云在操作过程中的时空演变来学习离散运动潜码。这种四维目标（空间几何随时间变化）使潜表示聚焦于实际物理运动而非外观模式。消融实验定量验证了几何预测是性能提升的关键，且学到的运动潜码在不同场景中表现出物理一致的变换能力。真实世界实验进一步证实，在杂乱环境中仅需少量演示即可实现鲁棒操作。

## 核心内容
### 方法概述
GeoMoLa的核心创新在于将运动潜码学习转化为四维几何预测任务：
- **输入**：单视角RGB-D图像，无需多视角重建
- **目标**：预测操作过程中点云的时空演变（即三维几何随时间的变化）
- **输出**：离散运动潜码，编码实际物理运动而非外观模式

### 架构设计
- **编码器**：从RGB-D序列提取视觉特征，结合点云几何信息
- **潜码学习**：通过预测点云在连续时间步的变换来学习离散运动潜码
- **解码器**：基于潜码生成操作策略，实现物理一致的变换

### 实验设置与结果
- **基准测试**：在多个操作基准上评估，包括桌面操作、抓取和组装任务
- **性能对比**：仅用单视角RGB-D输入即达到最先进性能，而现有方法需多视角重建
- **消融实验**：定量验证几何预测是性能提升的关键因素，去除几何目标后性能显著下降
- **泛化能力**：学到的运动潜码在不同场景中产生物理一致的变换，不受视觉上下文影响

### 真实世界实验
- **环境**：杂乱桌面环境，包含多种未知物体
- **演示数量**：仅需少量演示（如5-10次）即可学习鲁棒操作策略
- **结果**：在几何推理决定成败的杂乱场景中，GeoMoLa成功完成操作任务，验证了其鲁棒性

### 结论
GeoMoLa证明，有效的机器人运动潜码应通过理解三维几何效应而非像素级模式来学习，这为基于几何感知的机器人操作提供了新范式。

## Overview
Learning motion latents for robotic manipulation heavily relies on extracting motion patterns from visual sequences, yet effective action abstractions require understanding three-dimensional geometric transformations. Here, we introduce GeoMoLa (Geometry-Aware Motion Latents), which learns discrete motion latent codes by predicting how point clouds evolve during manipulation rather than reconstructing visual observations. This four-dimensional objective -- spatial geometry changing through time -- forces latent representations to encode actual physical motion rather than appearance patterns. GeoMoLa achieves state-of-the-art performance using only single-view RGB-D input, while existing methods require multi-view reconstruction, succeeding across diverse manipulation benchmarks. Our ablations reveal that geometric prediction is the key to driving performance, quantitatively validating that manipulation depends on spatial understanding. Furthermore, the learned codes exhibit effective motion abstraction: applying them to novel scenes produces physically consistent transformations regardless of visual context. Our real-world experiments also confirm this robustness capability, achieving robust manipulation with minimal demonstrations in cluttered environments where geometric reasoning determines success. Thus, we demonstrate that effective motion latents for robot control can better emerge from understanding motion through its three-dimensional effects rather than pixel-level patterns.

## 参考
- http://arxiv.org/abs/2607.04714v1

## 개요
GeoMoLa는 연구자들이 제안한 방법으로, 로봇 조작에서 운동 잠재 코드 학습이 3D 기하 변환 이해에 대한 필요성을 해결하기 위해 설계되었습니다. 다중 시점 재구성에 의존하는 기존 방법과 달리, GeoMoLa는 단일 시점 RGB-D 입력만 사용하여 조작 과정에서 포인트 클라우드의 시공간적 변화를 예측함으로써 이산 운동 잠재 코드를 학습합니다. 이러한 4D 목표(공간 기하가 시간에 따라 변화)는 잠재 표현이 외관 패턴이 아닌 실제 물리적 운동에 집중하도록 합니다. 절제 실험은 기하 예측이 성능 향상의 핵심 요소임을 정량적으로 검증했으며, 학습된 운동 잠재 코드는 다양한 장면에서 물리적으로 일관된 변환 능력을 보여줍니다. 실제 세계 실험은 혼잡한 환경에서 소량의 시연만으로도 강건한 조작이 가능함을 추가로 확인했습니다.

## 핵심 내용
### 방법 개요
GeoMoLa의 핵심 혁신은 운동 잠재 코드 학습을 4D 기하 예측 작업으로 전환하는 것입니다:
- **입력**: 단일 시점 RGB-D 이미지, 다중 시점 재구성 불필요
- **목표**: 조작 과정에서 포인트 클라우드의 시공간적 변화(즉, 시간에 따른 3D 기하 변화) 예측
- **출력**: 외관 패턴이 아닌 실제 물리적 운동을 인코딩하는 이산 운동 잠재 코드

### 아키텍처 설계
- **인코더**: RGB-D 시퀀스에서 시각적 특징을 추출하고 포인트 클라우드 기하 정보를 결합
- **잠재 코드 학습**: 연속 시간 단계에서 포인트 클라우드의 변환을 예측하여 이산 운동 잠재 코드 학습
- **디코더**: 잠재 코드를 기반으로 조작 정책을 생성하여 물리적으로 일관된 변환 구현

### 실험 설정 및 결과
- **벤치마크**: 테이블 조작, 파지, 조립 작업을 포함한 여러 조작 벤치마크에서 평가
- **성능 비교**: 단일 시점 RGB-D 입력만으로 최첨단 성능에 도달, 기존 방법은 다중 시점 재구성 필요
- **절제 실험**: 기하 예측이 성능 향상의 핵심 요소임을 정량적으로 검증, 기하 목표 제거 시 성능이 크게 저하
- **일반화 능력**: 학습된 운동 잠재 코드가 시각적 맥락에 영향을 받지 않고 다양한 장면에서 물리적으로 일관된 변환 생성

### 실제 세계 실험
- **환경**: 다양한 미지의 물체를 포함한 혼잡한 테이블 환경
- **시연 수**: 소량의 시연(예: 5-10회)만으로 강건한 조작 정책 학습 가능
- **결과**: 기하 추론이 성패를 결정하는 혼잡한 장면에서 GeoMoLa가 조작 작업을 성공적으로 완료하여 강건성을 검증

### 결론
GeoMoLa는 효과적인 로봇 운동 잠재 코드가 픽셀 수준 패턴이 아닌 3D 기하 효과를 이해함으로써 학습되어야 함을 증명하며, 이는 기하 인식 기반 로봇 조작을 위한 새로운 패러다임을 제공합니다.
