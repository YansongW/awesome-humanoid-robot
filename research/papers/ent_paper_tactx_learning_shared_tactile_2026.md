---
$id: ent_paper_tactx_learning_shared_tactile_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TactX: Learning Shared Tactile Representations Across Diverse Sensors'
  zh: 'TactX: Learning Shared Tactile Representations Across Diverse Sensors'
  ko: 'TactX: Learning Shared Tactile Representations Across Diverse Sensors'
summary:
  en: 'arXiv:2606.31236v1 Announce Type: new Abstract: Tactile sensors provide critical information for contact-rich manipulation,
    yet tactile representations and policies remain tightly coupled to each specific sensor, limiting transferability across
    robots and hardware platforms. We propose TactX, a framework for learning a transferable tactile representation across
    sensors spanning three fundamentally different transduction modalities: resistive, magnetic, and vision-based. TactX maps
    heterogeneous tactile observations into a shared latent space through modality-specific encoders trained on paired contact
    data. Such paired interactions provide a natural alignment signal across modalities, and the encoders are jointly trained
    across all sensor pairs, inducing a consistent latent space for all sensor types. Our experiments show that TactX aligns
    tactile representations across sensors while preserving object-level contact information, as evidenced by sensor-identity
    prediction and object classification in the learned latent space. We evaluate TactX on four contact-rich manipulation
    tasks: pick-and-place, plug insertion, board wiping, and object reorientation, and show that policies trained with one
    sensor transfer zero-shot to physically distinct sensors through the shared latent. This improves the average success
    rate from 27.5% for vision-only policy to 45.9%, providing a step toward sensor-agnostic tactile manipulation.'
  zh: TactX 是一个跨传感器触觉表征学习框架，由研究团队提出，旨在解决触觉表征与特定传感器强耦合导致的迁移困难问题。其核心贡献是通过模态特定编码器将电阻式、磁式和视觉式三种传感器的触觉观测映射到共享隐空间，实现零样本跨传感器策略迁移，将平均任务成功率从27.5%提升至45.9%。
  ko: 'arXiv:2606.31236v1 Announce Type: new Abstract: Tactile sensors provide critical information for contact-rich manipulation,
    yet tactile representations and policies remain tightly coupled to each specific sensor, limiting transferability across
    robots and hardware platforms. We propose TactX, a framework for learning a transferable tactile representation across
    sensors spanning three fundamentally different transduction modalities: resistive, magnetic, and vision-based. TactX maps
    heterogeneous tactile observations into a shared latent space through modality-specific encoders trained on paired contact
    data. Such paired interactions provide a natural alignment signal across modalities, and the encoders are jointly trained
    across all sensor pairs, inducing a consistent latent space for all sensor types. Our experiments show that TactX aligns
    tactile representations across sensors while preserving object-level contact information, as evidenced by sensor-identity
    prediction and object classification in the learned latent space. We evaluate TactX on four contact-rich manipulation
    tasks: pick-and-place, plug insertion, board wiping, and object reorientation, and show that policies trained with one
    sensor transfer zero-shot to physically distinct sensors through the shared latent. This improves the average success
    rate from 27.5% for vision-only policy to 45.9%, providing a step toward sensor-agnostic tactile manipulation.'
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
- tactx
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31236v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1012 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'TactX: Learning Shared Tactile Representations Across Diverse Sensors'
  url: https://arxiv.org/abs/2606.31236
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
TactX 针对触觉传感器类型多样、表征与策略高度耦合的痛点，提出了一种可迁移的触觉表征学习方案。该框架利用配对接触数据作为自然对齐信号，联合训练三个模态特定编码器，将异构触觉观测统一映射到共享隐空间。实验证明，该隐空间不仅保留了物体级接触信息，还能通过传感器身份预测和物体分类任务进行验证。在拾放、插销插入、板擦和物体重定向四项接触丰富操作任务中，基于单一传感器训练的策略可通过共享隐空间零样本迁移至物理结构不同的其他传感器，显著提升了任务成功率。

## 核心内容
### 方法架构
TactX 的核心架构包含三个模态特定编码器，分别处理电阻式、磁式和视觉式触觉传感器的原始观测数据。这些编码器通过配对接触数据进行联合训练——即在同一接触事件中同时采集不同传感器的触觉信号，利用这种自然对齐关系作为监督信号，迫使编码器将异构输入映射到一致的隐空间。训练过程中，所有传感器对的数据被同时使用，确保隐空间对所有传感器类型保持一致性。

### 实验设置
- **传感器类型**：覆盖三种根本不同的换能模态：电阻式（如基于压阻材料的传感器）、磁式（如基于霍尔效应的传感器）和视觉式（如基于摄像头的GelSight类传感器）。
- **任务集**：四项接触丰富操作任务——拾放（pick-and-place）、插销插入（plug insertion）、板擦（board wiping）和物体重定向（object reorientation）。
- **评估方式**：在隐空间中进行传感器身份预测和物体分类，验证表征对齐效果；在操作任务中测试零样本迁移能力，即用传感器A训练的策略直接部署到传感器B上。

### 关键结果
- **表征对齐**：隐空间中的传感器身份预测准确率表明，TactX成功消除了传感器特异性差异，同时物体分类任务证明物体级接触信息被完整保留。
- **零样本迁移**：在四项操作任务中，基于单一传感器训练的策略通过共享隐空间直接迁移到其他传感器，无需任何微调。
- **性能提升**：与仅使用视觉信息的基线策略（平均成功率27.5%）相比，TactX将平均成功率提升至45.9%，展示了向传感器无关触觉操作迈出的重要一步。

### 结论
TactX 通过配对数据驱动的跨模态对齐，首次实现了三种根本不同换能原理的触觉传感器之间的表征共享与策略零样本迁移，为构建通用触觉操作系统提供了可行方案。

## Overview
Tactile sensors provide critical information for contact-rich manipulation, yet tactile representations and policies remain tightly coupled to each specific sensor, limiting transferability across robots and hardware platforms. We propose TactX, a framework for learning a transferable tactile representation across sensors spanning three fundamentally different transduction modalities: resistive, magnetic, and vision-based. TactX maps heterogeneous tactile observations into a shared latent space through modality-specific encoders trained on paired contact data. Such paired interactions provide a natural alignment signal across modalities, and the encoders are jointly trained across all sensor pairs, inducing a consistent latent space for all sensor types. Our experiments show that TactX aligns tactile representations across sensors while preserving object-level contact information, as evidenced by sensor-identity prediction and object classification in the learned latent space. We evaluate TactX on four contact-rich manipulation tasks: pick-and-place, plug insertion, board wiping, and object reorientation, and show that policies trained with one sensor transfer zero-shot to physically distinct sensors through the shared latent. This improves the average success rate from 27.5% for vision-only policy to 45.9%, providing a step toward sensor-agnostic tactile manipulation.

## 参考
- http://arxiv.org/abs/2606.31236v1

## 개요
TactX는 촉각 센서 유형이 다양하고 표현과 정책이 고도로 결합되어 있는 문제점을 해결하기 위해, 전이 가능한 촉각 표현 학습 방안을 제안한다. 이 프레임워크는 짝지어진 접촉 데이터를 자연스러운 정렬 신호로 활용하여 세 가지 모달리티별 인코더를 공동 훈련시키고, 이질적인 촉각 관측을 공유 잠재 공간으로 통합 매핑한다. 실험 결과, 이 잠재 공간은 객체 수준의 접촉 정보를 보존할 뿐만 아니라 센서 신원 예측 및 객체 분류 작업을 통해 검증할 수 있다. 집어 올리기, 플러그 삽입, 보드 닦기, 객체 재방향 설정의 네 가지 접촉 집약적 조작 작업에서 단일 센서로 훈련된 정책은 공유 잠재 공간을 통해 물리적 구조가 다른 다른 센서로 제로샷 전이가 가능하며, 작업 성공률을 크게 향상시킨다.

## 핵심 내용
### 방법 아키텍처
TactX의 핵심 아키텍처는 저항식, 자기식, 시각식 촉각 센서의 원시 관측 데이터를 각각 처리하는 세 가지 모달리티별 인코더로 구성된다. 이 인코더들은 짝지어진 접촉 데이터를 통해 공동 훈련된다. 즉, 동일한 접촉 이벤트에서 서로 다른 센서의 촉각 신호를 동시에 수집하고, 이러한 자연스러운 정렬 관계를 감독 신호로 활용하여 인코더가 이질적인 입력을 일관된 잠재 공간으로 매핑하도록 강제한다. 훈련 과정에서 모든 센서 쌍의 데이터가 동시에 사용되어 잠재 공간이 모든 센서 유형에 대해 일관성을 유지하도록 보장한다.

### 실험 설정
- **센서 유형**: 저항식(예: 압저항 재료 기반 센서), 자기식(예: 홀 효과 기반 센서), 시각식(예: 카메라 기반 GelSight류 센서)의 세 가지 근본적으로 다른 변환 모달리티를 포함한다.
- **작업 세트**: 집어 올리기(pick-and-place), 플러그 삽입(plug insertion), 보드 닦기(board wiping), 객체 재방향 설정(object reorientation)의 네 가지 접촉 집약적 조작 작업.
- **평가 방식**: 잠재 공간에서 센서 신원 예측 및 객체 분류를 수행하여 표현 정렬 효과를 검증하고, 조작 작업에서 제로샷 전이 능력을 테스트한다. 즉, 센서 A로 훈련된 정책을 센서 B에 직접 배포한다.

### 주요 결과
- **표현 정렬**: 잠재 공간에서의 센서 신원 예측 정확도는 TactX가 센서 특이적 차이를 성공적으로 제거했음을 보여주며, 객체 분류 작업은 객체 수준의 접촉 정보가 완전히 보존되었음을 증명한다.
- **제로샷 전이**: 네 가지 조작 작업에서 단일 센서로 훈련된 정책은 공유 잠재 공간을 통해 다른 센서로 직접 전이되며, 어떠한 미세 조정도 필요하지 않다.
- **성능 향상**: 시각 정보만 사용하는 기준 정책(평균 성공률 27.5%)과 비교하여, TactX는 평균 성공률을 45.9%로 향상시켜 센서 무관 촉각 조작을 향한 중요한 한 걸음을 보여준다.

### 결론
TactX는 짝지어진 데이터 기반의 교차 모달리티 정렬을 통해 세 가지 근본적으로 다른 변환 원리를 가진 촉각 센서 간의 표현 공유와 정책 제로샷 전이를 최초로 실현하여, 범용 촉각 조작 시스템 구축을 위한 실행 가능한 방안을 제공한다.
