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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.20808v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
머신러닝은 내비게이션, 로코모션, 매니퓰레이션 등 다양한 로보틱스 분야에서 상당한 발전을 촉진했습니다. 이러한 성과 중 상당수는 실제 환경에 배치되기 전에 로봇 시스템을 훈련하고 테스트하는 핵심 도구로서 시뮬레이션의 광범위한 사용에 의해 주도되었습니다. 그러나 시뮬레이션은 추상화와 근사치로 구성되어 있어 시뮬레이션 환경과 실제 환경 간의 차이, 즉 현실 격차(reality gap)를 필연적으로 초래합니다. 이러한 차이는 시스템이 시뮬레이션에서 실제 세계로 성공적으로 이전되는 것을 크게 저해합니다. 이 격차를 해소하는 것은 로보틱스에서 가장 시급한 과제 중 하나로 남아 있습니다. 최근 시뮬레이션-실제 전환(sim-to-real transfer)의 발전은 로코모션, 내비게이션, 매니퓰레이션을 포함한 다양한 플랫폼에서 유망한 결과를 보여주었습니다. 도메인 무작위화(domain randomization), 실제-시뮬레이션 전환(real-to-sim transfer), 상태 및 행동 추상화(state and action abstractions), 시뮬레이션-실제 공동 훈련(sim-real co-training)과 같은 기술을 활용하여 많은 연구가 현실 격차를 극복했습니다. 그러나 여전히 과제가 남아 있으며, 현실 격차의 근본 원인과 해결책에 대한 더 깊은 이해가 필요합니다. 본 설문조사에서는 시뮬레이션-실제 전환 환경에 대한 포괄적인 개요를 제시하며, 현실 격차와 시뮬레이션-실제 전환의 원인, 해결책 및 평가 지표를 강조합니다.

## 핵심 내용
머신러닝은 내비게이션, 로코모션, 매니퓰레이션 등 다양한 로보틱스 분야에서 상당한 발전을 촉진했습니다. 이러한 성과 중 상당수는 실제 환경에 배치되기 전에 로봇 시스템을 훈련하고 테스트하는 핵심 도구로서 시뮬레이션의 광범위한 사용에 의해 주도되었습니다. 그러나 시뮬레이션은 추상화와 근사치로 구성되어 있어 시뮬레이션 환경과 실제 환경 간의 차이, 즉 현실 격차(reality gap)를 필연적으로 초래합니다. 이러한 차이는 시스템이 시뮬레이션에서 실제 세계로 성공적으로 이전되는 것을 크게 저해합니다. 이 격차를 해소하는 것은 로보틱스에서 가장 시급한 과제 중 하나로 남아 있습니다. 최근 시뮬레이션-실제 전환(sim-to-real transfer)의 발전은 로코모션, 내비게이션, 매니퓰레이션을 포함한 다양한 플랫폼에서 유망한 결과를 보여주었습니다. 도메인 무작위화(domain randomization), 실제-시뮬레이션 전환(real-to-sim transfer), 상태 및 행동 추상화(state and action abstractions), 시뮬레이션-실제 공동 훈련(sim-real co-training)과 같은 기술을 활용하여 많은 연구가 현실 격차를 극복했습니다. 그러나 여전히 과제가 남아 있으며, 현실 격차의 근본 원인과 해결책에 대한 더 깊은 이해가 필요합니다. 본 설문조사에서는 시뮬레이션-실제 전환 환경에 대한 포괄적인 개요를 제시하며, 현실 격차와 시뮬레이션-실제 전환의 원인, 해결책 및 평가 지표를 강조합니다.

## 参考
- http://arxiv.org/abs/2510.20808v1
