---
$id: ent_paper_cao_learning_sim_to_real_dense_obj_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Sim-to-Real Dense Object Descriptors for Robotic Manipulation
  zh: 面向机器人操作的仿真到现实稠密物体描述符学习
  ko: 로봇 조작을 위한 시뮬레이션-현실 밀집 객체 기술자 학습
summary:
  en: This paper proposes Sim-to-Real Dense Object Nets (SRDONs), a dense object descriptor representation that unifies simulated
    and real visual data in a shared feature space with pixel-wise consistency, enabling zero real-world training transfer
    for robotic manipulation tasks.
  zh: 本文提出Sim-to-Real Dense Object Nets (SRDONs)，一种密集物体描述子表示方法，能将模拟与真实视觉数据统一到共享特征空间并保持像素级一致性。该方法由研究团队开发，核心贡献在于实现零真实世界训练的机器人操作任务迁移。
  ko: 본 논문은 시뮬레이션과 실제 시각 데이터를 픽셀 수준의 일관성을 가진 공유 특징 공간으로 통합하는 밀집 객체 기술자 표현인 SRDONs(Sim-to-Real Dense Object Nets)를 제안하여, 로봇
    조작 작업에서 실제 세계 훈련 없이 전이가 가능하도록 한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- dense_object_descriptors
- vision_based_manipulation
- contrastive_learning
- domain_adaptation
- rgb_d_perception
- zero_shot_transfer
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2304.08703v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (741 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Sim-to-Real Dense Object Descriptors for Robotic Manipulation
  url: https://arxiv.org/abs/2304.08703
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
针对机器人操作中视觉理解与模拟到真实迁移两大挑战，本文提出SRDONs。该方法通过物体到物体的匹配策略，将不同场景与不同域（模拟/真实）的图像对对齐到统一特征空间，从而利用GraspNet等公开数据集减少真实数据标注需求。实验证明，预训练的SRDONs在未见物体和未见视觉环境中显著提升多种机器人操作任务性能，且无需真实世界训练数据。

## 核心内容
### 方法架构
- **核心表示**：SRDONs是一种密集物体描述子，为每个像素生成特征向量，使模拟与真实图像在像素级对齐到共享特征空间。
- **匹配策略**：提出物体到物体（object-to-object）匹配方法，用于处理不同场景和不同域（如模拟与真实）的图像对，通过跨域一致性约束学习域不变特征。

### 实验设置
- **数据集**：利用公开数据集GraspNet作为模拟数据源，减少真实数据采集成本。
- **任务场景**：在多种机器人操作任务中测试，包括抓取、放置等，评估对象为未见物体和未见视觉环境。

### 关键数字与结论
- **零训练迁移**：预训练SRDONs在未见物体和未见视觉环境中实现零真实世界训练（zero real-world training）的性能提升。
- **性能提升**：相比基线方法，SRDONs在多种操作任务中显著提高成功率，尤其在跨域场景下表现鲁棒。
- **通用性**：SRDONs可作为模拟到真实操作任务的通用构建模块（building block），适用于不同任务类型。

### 结论
SRDONs通过统一模拟与真实数据的特征空间，有效弥合了域间差异，为机器人操作提供了一种无需真实标注的实用解决方案。未来工作可扩展至更复杂的操作任务与多物体场景。

## Overview
It is crucial to address the following issues for ubiquitous robotics manipulation applications: (a) vision-based manipulation tasks require the robot to visually learn and understand the object with rich information like dense object descriptors; and (b) sim-to-real transfer in robotics aims to close the gap between simulated and real data. In this paper, we present Sim-to-Real Dense Object Nets (SRDONs), a dense object descriptor that not only understands the object via appropriate representation but also maps simulated and real data to a unified feature space with pixel consistency. We proposed an object-to-object matching method for image pairs from different scenes and different domains. This method helps reduce the effort of training data from real-world by taking advantage of public datasets, such as GraspNet. With sim-to-real object representation consistency, our SRDONs can serve as a building block for a variety of sim-to-real manipulation tasks. We demonstrate in experiments that pre-trained SRDONs significantly improve performances on unseen objects and unseen visual environments for various robotic tasks with zero real-world training.

## 参考
- http://arxiv.org/abs/2304.08703v1

## 개요
로봇 조작에서의 시각적 이해와 시뮬레이션-실제 전환이라는 두 가지 주요 과제를 해결하기 위해, 본 논문은 SRDONs를 제안한다. 이 방법은 객체-객체 매칭 전략을 통해 서로 다른 장면과 서로 다른 도메인(시뮬레이션/실제)의 이미지 쌍을 통일된 특징 공간에 정렬함으로써, GraspNet과 같은 공개 데이터셋을 활용하여 실제 데이터 주석 요구를 줄인다. 실험 결과, 사전 훈련된 SRDONs는 보지 못한 객체와 보지 못한 시각적 환경에서 다양한 로봇 조작 작업 성능을 크게 향상시키며, 실제 세계 훈련 데이터 없이도 가능함을 보여준다.

## 핵심 내용
### 방법 아키텍처
- **핵심 표현**: SRDONs는 밀집 객체 디스크립터로, 각 픽셀에 대해 특징 벡터를 생성하여 시뮬레이션과 실제 이미지를 픽셀 수준에서 공유 특징 공간에 정렬한다.
- **매칭 전략**: 서로 다른 장면과 서로 다른 도메인(예: 시뮬레이션과 실제)의 이미지 쌍을 처리하기 위한 객체-객체(object-to-object) 매칭 방법을 제안하며, 교차 도메인 일관성 제약을 통해 도메인 불변 특징을 학습한다.

### 실험 설정
- **데이터셋**: 공개 데이터셋 GraspNet을 시뮬레이션 데이터 소스로 활용하여 실제 데이터 수집 비용을 줄인다.
- **작업 시나리오**: 그리핑, 배치 등 다양한 로봇 조작 작업에서 테스트하며, 평가 대상은 보지 못한 객체와 보지 못한 시각적 환경이다.

### 주요 수치와 결론
- **제로 훈련 전이**: 사전 훈련된 SRDONs는 보지 못한 객체와 보지 못한 시각적 환경에서 제로 실제 세계 훈련(zero real-world training) 성능 향상을 달성한다.
- **성능 향상**: 기준 방법과 비교하여 SRDONs는 다양한 조작 작업에서 성공률을 크게 높이며, 특히 교차 도메인 시나리오에서 강건한 성능을 보인다.
- **범용성**: SRDONs는 시뮬레이션-실제 조작 작업을 위한 범용 구성 블록(building block)으로 사용될 수 있으며, 다양한 작업 유형에 적용 가능하다.

### 결론
SRDONs는 시뮬레이션과 실제 데이터의 특징 공간을 통일함으로써 도메인 간 차이를 효과적으로 좁히며, 실제 주석 없이도 로봇 조작을 위한 실용적인 솔루션을 제공한다. 향후 작업은 더 복잡한 조작 작업과 다중 객체 시나리오로 확장될 수 있다.
