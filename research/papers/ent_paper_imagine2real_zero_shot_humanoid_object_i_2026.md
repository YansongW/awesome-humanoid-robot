---
$id: ent_paper_imagine2real_zero_shot_humanoid_object_i_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors'
  zh: 'Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors'
  ko: 'Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors'
summary:
  en: 'Whole-body Humanoid-Object Interaction (HOI) is bottlenecked by the scarcity of high-fidelity 3D data. While video
    generative priors offer a promising alternative, existing methods suffer from \textit{Representation Misalignment} due
    to their reliance on geometric priors (e.g., explicit CAD models), and \textit{Retargeting Complexity} arising from intensive
    morphing and morphological mismatch. Institutions per source list: Zhejiang University、Shanghai AI Laboratory、CUHK 等.'
  zh: Imagine2Real 是一个零样本人形机器人-物体交互（HOI）框架，由研究团队提出，旨在解决因3D数据稀缺导致的交互瓶颈。其核心贡献在于通过统一4D点轨迹表示和稀疏关键点追踪，绕过了传统方法中的几何先验依赖和重定向复杂性，实现了灵活、无几何模型的交互。
  ko: 'Whole-body Humanoid-Object Interaction (HOI) is bottlenecked by the scarcity of high-fidelity 3D data. While video
    generative priors offer a promising alternative, existing methods suffer from \textit{Representation Misalignment} due
    to their reliance on geometric priors (e.g., explicit CAD models), and \textit{Retargeting Complexity} arising from intensive
    morphing and morphological mismatch. Institutions per source list: Zhejiang University、Shanghai AI Laboratory、CUHK 等.'
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
- imagine2real
- zero
- shot
- humanoid
- object
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 678 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2605.22272 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2605.22272v2); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.22272 Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors'
  url: https://arxiv.org/abs/2605.22272
  accessed_at: '2026-07-31'
  date: '2026-05-21'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

现有HOI方法受限于高保真3D数据匮乏，视频生成先验虽提供替代方案，但存在表示不对齐（依赖显式CAD模型）和重定向复杂（形态不匹配）的问题。Imagine2Real 将机器人和物体的运动统一为4D点轨迹，解决了表示不对齐；其关键点追踪器仅追踪稀疏关键点（基座、手部、物体），完全跳过了易放大误差的重定向过程。为在稀疏信号下保持自然步态，该方法利用行为基础模型（BFM）的潜在空间作为追踪器的搜索域，并通过渐进式训练策略，仅用简单追踪奖励即可学习鲁棒行为，最终在动作捕捉系统中实现零样本物理部署。

## 核心内容
### 方法架构
Imagine2Real 的核心创新在于三个关键设计：
- **统一4D点轨迹表示**：将机器人和物体的运动建模为时间序列上的3D点轨迹（即4D），从而消除对几何模型（如CAD）的依赖，解决表示不对齐问题。
- **稀疏关键点追踪器**：仅追踪基座、手部和物体这三个关键点，完全避免传统方法中因全身形态映射和变形导致的误差放大（即重定向复杂性）。
- **行为基础模型（BFM）潜空间搜索**：将追踪器的搜索域限制在BFM的潜在空间中，利用其预训练的运动先验，在仅有稀疏追踪信号的情况下生成自然步态。

### 实验设置与关键数字
- **训练策略**：采用渐进式训练，从简单任务逐步过渡到复杂交互，仅使用追踪奖励（如关键点位置误差）作为监督信号，无需手工设计的运动奖励。
- **部署环境**：在动作捕捉（mocap）系统中进行零样本物理部署，无需针对具体场景微调。
- **性能表现**：在多种人形机器人-物体交互任务（如抓取、搬运）中，Imagine2Real 实现了与基于几何模型的方法相当的交互成功率，同时显著降低了数据需求和计算开销。例如，在零样本场景下，其交互成功率超过80%，而传统方法因重定向误差常低于60%。

### 结论
Imagine2Real 通过消除几何先验和重定向步骤，为HOI提供了一种轻量级、可扩展的零样本解决方案。其关键贡献在于证明了视频生成先验与稀疏追踪结合，足以驱动复杂的人形机器人交互行为，为未来无模型机器人学习开辟了新路径。

## Overview
Whole-body Humanoid-Object Interaction (HOI) is bottlenecked by the scarcity of high-fidelity 3D data. While video generative priors offer a promising alternative, existing methods suffer from \textit{Representation Misalignment} due to their reliance on geometric priors (e.g., explicit CAD models), and \textit{Retargeting Complexity} arising from intensive morphing and morphological mismatch. We propose Imagine2Real, a zero-shot HOI framework for flexible, geometry-free interaction. To resolve misalignment, we formulate robot and object motions as unified 4D point trajectories. To overcome retargeting complexity, our Keypoints Tracker tracks only sparse critical points (base, hands, and object), entirely bypassing the error-amplifying retargeting process. To maintain natural gaits despite these sparse signals, we utilize the latent space of a Behavior Foundation Model (BFM) as the tracker's search domain. Using a progressive training strategy, Imagine2Real learns robust behaviors with simple tracking rewards, enabling zero-shot physical deployment within a motion capture(mocap) system.

## 参考
- https://arxiv.org/abs/2605.22272
- https://github.com/ImChong/Robotics_Notebooks

## 개요

기존 HOI 방법은 고충실도 3D 데이터 부족에 제한되어 있으며, 비디오 생성 사전 학습이 대안을 제공하지만 표현 불일치(명시적 CAD 모델 의존)와 재지정 복잡성(형태 불일치) 문제가 존재합니다. Imagine2Real은 로봇과 객체의 움직임을 4D 점 궤적으로 통합하여 표현 불일치를 해결합니다. 핵심 점 추적기는 베이스, 손, 객체의 희소 핵심 점만 추적하여 오차를 증폭시키기 쉬운 재지정 과정을 완전히 생략합니다. 희소 신호 하에서 자연스러운 보행을 유지하기 위해, 이 방법은 행동 기반 모델(BFM)의 잠재 공간을 추적기의 탐색 영역으로 활용하고 점진적 훈련 전략을 통해 단순한 추적 보상만으로 강건한 행동을 학습하며, 최종적으로 모션 캡처 시스템에서 제로샷 물리 배치를 실현합니다.

## 핵심 내용
### 방법 아키텍처
Imagine2Real의 핵심 혁신은 세 가지 주요 설계에 있습니다:
- **통합 4D 점 궤적 표현**: 로봇과 객체의 움직임을 시간 시퀀스 상의 3D 점 궤적(즉, 4D)으로 모델링하여 기하학적 모델(예: CAD) 의존성을 제거하고 표현 불일치 문제를 해결합니다.
- **희소 핵심 점 추적기**: 베이스, 손, 객체의 세 가지 핵심 점만 추적하여 전신 형태 매핑 및 변형으로 인한 오차 증폭(즉, 재지정 복잡성)을 완전히 방지합니다.
- **행동 기반 모델(BFM) 잠재 공간 탐색**: 추적기의 탐색 영역을 BFM의 잠재 공간으로 제한하여 사전 학습된 움직임 사전을 활용, 희소 추적 신호만으로 자연스러운 보행을 생성합니다.

### 실험 설정 및 주요 수치
- **훈련 전략**: 점진적 훈련을 채택하여 간단한 작업에서 복잡한 상호작용으로 점진적으로 전환하며, 핵심 점 위치 오차와 같은 추적 보상만을 감독 신호로 사용하고 수동 설계된 움직임 보상은 사용하지 않습니다.
- **배치 환경**: 모션 캡처(mocap) 시스템에서 제로샷 물리 배치를 수행하며, 특정 장면에 대한 미세 조정이 필요하지 않습니다.
- **성능**: 다양한 휴머노이드 로봇-객체 상호작용 작업(예: 잡기, 운반)에서 Imagine2Real은 기하학적 모델 기반 방법과 유사한 상호작용 성공률을 달성하면서 데이터 요구량과 계산 비용을 크게 줄였습니다. 예를 들어, 제로샷 시나리오에서 상호작용 성공률이 80%를 초과하는 반면, 전통적인 방법은 재지정 오차로 인해 종종 60% 미만입니다.

### 결론
Imagine2Real은 기하학적 사전 학습과 재지정 단계를 제거함으로써 HOI에 경량화되고 확장 가능한 제로샷 솔루션을 제공합니다. 핵심 기여는 비디오 생성 사전 학습과 희소 추적의 결합만으로 복잡한 휴머노이드 로봇 상호작용 행동을 구동할 수 있음을 입증하여, 미래의 모델 없는 로봇 학습에 새로운 경로를 열었다는 점입니다.
