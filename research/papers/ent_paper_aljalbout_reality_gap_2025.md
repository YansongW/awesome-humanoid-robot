---
$id: ent_paper_aljalbout_reality_gap_2025
$schema: ../../../../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'The Reality Gap in Robotics: Challenges, Solutions, and Best Practices'
  zh: 机器人中的现实鸿沟：挑战、解决方案与最佳实践
  ko: '로보틱스의 현실 격차: 과제, 해결책 및 모범 사례'
summary:
  en: A 2025 survey that maps the sim-to-real reality gap into perception and action-dynamics discrepancies, and reviews mitigation
    strategies including domain randomization, system identification, and sim-real co-training.
  zh: 这是一篇2025年的综述论文，系统梳理了机器人学中的“现实差距”问题。作者将差距划分为感知差异和动作-动力学差异两大类，并综述了域随机化、系统辨识、仿真-现实协同训练等主流缓解策略。
  ko: 2025년 서베이로, 시뮬레이션-현실 간 현실 격차를 지각 및 동작 역학 불일치로 분류하고 도메인 랜덤화, 시스템 식별, 시뮬-현실 공동 학습 등 완화 전략을 검토함.
domains:
- 07_ai_models_algorithms
- 02_components
- 08_software_middleware
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- reality_gap
- survey
- domain_randomization
- system_identification
- physics_simulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.20808v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (978 chars, DeepSeek).'
sources:
- id: src_paper_aljalbout_reality_gap_2025
  type: paper
  title: 'The Reality Gap in Robotics: Challenges, Solutions, and Best Practices'
  url: https://arxiv.org/abs/2510.20808
  date: '2025-10-23'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---
## 概述
该综述指出，机器学习在机器人导航、移动和操作等领域取得显著进展，很大程度上得益于仿真环境的广泛使用。然而，仿真中的抽象与近似必然导致模拟环境与真实环境之间的“现实差距”，严重阻碍系统从仿真向真实世界的迁移。论文将现实差距明确分为感知差异和动作-动力学差异两类，并系统回顾了域随机化、真实到仿真迁移、状态与动作抽象、仿真-现实协同训练等缓解方法。尽管这些技术已在多种平台上展现出令人鼓舞的结果，但挑战依然存在，需要更深入地理解现实差距的根本原因与解决方案。

## 核心内容
### 核心问题
- 现实差距（reality gap）源于仿真中的抽象与近似，导致模拟环境与真实环境之间存在不可忽视的偏差。
- 这种偏差严重阻碍了机器人系统从仿真训练到真实部署的成功迁移。

### 差距分类
- **感知差异（perception discrepancy）**：仿真传感器模型与真实传感器之间的差异，包括噪声、分辨率、光照等。
- **动作-动力学差异（action-dynamics discrepancy）**：仿真物理引擎与真实物理世界之间的差异，涉及摩擦力、惯性、接触动力学等。

### 缓解策略
- **域随机化（domain randomization）**：在仿真中随机化视觉、物理参数，迫使策略学习鲁棒特征。
- **系统辨识（system identification）**：通过真实数据校准仿真模型参数，缩小动力学差异。
- **真实到仿真迁移（real-to-sim transfer）**：从真实环境数据构建更精确的仿真模型。
- **状态与动作抽象（state and action abstractions）**：在仿真中简化状态空间或动作空间，降低迁移难度。
- **仿真-现实协同训练（sim-real co-training）**：交替使用仿真和真实数据训练，逐步弥合差距。

### 评估指标
- 论文强调需要统一的评估指标来衡量现实差距的缩小程度，包括迁移成功率、性能衰减率、鲁棒性测试等。

### 结论
- 尽管现有方法已在多种平台（如四足机器人、机械臂、无人机）上取得进展，但现实差距的根本原因仍需更深入的理论分析。
- 未来方向包括：更精细的感知模型、自适应系统辨识、以及结合物理先验的混合训练方法。

## Overview
Machine learning has facilitated significant advancements across various robotics domains, including navigation, locomotion, and manipulation. Many such achievements have been driven by the extensive use of simulation as a critical tool for training and testing robotic systems prior to their deployment in real-world environments. However, simulations consist of abstractions and approximations that inevitably introduce discrepancies between simulated and real environments, known as the reality gap. These discrepancies significantly hinder the successful transfer of systems from simulation to the real world. Closing this gap remains one of the most pressing challenges in robotics. Recent advances in sim-to-real transfer have demonstrated promising results across various platforms, including locomotion, navigation, and manipulation. By leveraging techniques such as domain randomization, real-to-sim transfer, state and action abstractions, and sim-real co-training, many works have overcome the reality gap. However, challenges persist, and a deeper understanding of the reality gap's root causes and solutions is necessary. In this survey, we present a comprehensive overview of the sim-to-real landscape, highlighting the causes, solutions, and evaluation metrics for the reality gap and sim-to-real transfer.

## 参考
- http://arxiv.org/abs/2510.20808v1

## 개요
이 리뷰 논문은 기계 학습이 로봇 내비게이션, 이동, 조작 등의 분야에서 상당한 진전을 이루었으며, 이는 주로 시뮬레이션 환경의 광범위한 사용 덕분이라고 지적합니다. 그러나 시뮬레이션의 추상화와 근사화는 필연적으로 시뮬레이션 환경과 실제 환경 사이의 '현실 격차(reality gap)'를 초래하며, 이는 시스템이 시뮬레이션에서 실제 세계로 전이되는 것을 심각하게 방해합니다. 논문은 현실 격차를 명확히 지각 차이(perception discrepancy)와 행동-동역학 차이(action-dynamics discrepancy)의 두 가지 유형으로 구분하고, 도메인 무작위화(domain randomization), 실제-시뮬레이션 전이(real-to-sim transfer), 상태 및 행동 추상화(state and action abstractions), 시뮬레이션-실제 협력 훈련(sim-real co-training) 등의 완화 방법을 체계적으로 검토합니다. 이러한 기술들은 다양한 플랫폼에서 고무적인 결과를 보여주었지만, 현실 격차의 근본 원인과 해결책에 대한 더 깊은 이해가 여전히 필요하며 도전 과제가 남아 있습니다.

## 핵심 내용
### 핵심 문제
- 현실 격차(reality gap)는 시뮬레이션의 추상화와 근사화에서 비롯되며, 시뮬레이션 환경과 실제 환경 사이에 무시할 수 없는 편차를 초래합니다.
- 이러한 편차는 로봇 시스템이 시뮬레이션 훈련에서 실제 배포로 성공적으로 전이되는 것을 심각하게 방해합니다.

### 격차 분류
- **지각 차이(perception discrepancy)**: 시뮬레이션 센서 모델과 실제 센서 간의 차이로, 노이즈, 해상도, 조명 등을 포함합니다.
- **행동-동역학 차이(action-dynamics discrepancy)**: 시뮬레이션 물리 엔진과 실제 물리 세계 간의 차이로, 마찰력, 관성, 접촉 동역학 등을 포함합니다.

### 완화 전략
- **도메인 무작위화(domain randomization)**: 시뮬레이션에서 시각적, 물리적 매개변수를 무작위화하여 정책이 강건한 특징을 학습하도록 강제합니다.
- **시스템 식별(system identification)**: 실제 데이터를 통해 시뮬레이션 모델 매개변수를 보정하여 동역학 차이를 줄입니다.
- **실제-시뮬레이션 전이(real-to-sim transfer)**: 실제 환경 데이터를 기반으로 더 정밀한 시뮬레이션 모델을 구축합니다.
- **상태 및 행동 추상화(state and action abstractions)**: 시뮬레이션에서 상태 공간 또는 행동 공간을 단순화하여 전이 난이도를 낮춥니다.
- **시뮬레이션-실제 협력 훈련(sim-real co-training)**: 시뮬레이션과 실제 데이터를 번갈아 사용하여 훈련하며 점진적으로 격차를 좁힙니다.

### 평가 지표
- 논문은 현실 격차의 축소 정도를 측정하기 위한 통일된 평가 지표의 필요성을 강조하며, 전이 성공률, 성능 감쇠율, 강건성 테스트 등을 포함합니다.

### 결론
- 기존 방법들이 다양한 플랫폼(예: 네 발 로봇, 로봇 팔, 드론)에서 진전을 이루었지만, 현실 격차의 근본 원인에 대한 더 깊은 이론적 분석이 여전히 필요합니다.
- 향후 방향으로는 더 정밀한 지각 모델, 적응형 시스템 식별, 그리고 물리적 사전 지식을 결합한 혼합 훈련 방법 등이 포함됩니다.
