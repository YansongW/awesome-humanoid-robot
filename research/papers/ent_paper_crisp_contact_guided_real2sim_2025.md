---
$id: ent_paper_crisp_contact_guided_real2sim_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives'
  zh: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives'
  ko: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives'
summary:
  en: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives is a 2025 work on physics-based character
    animation for humanoid robots.'
  zh: CRISP 是一种从单目视频中恢复可仿真人体运动与场景几何的方法，由研究团队于 2025 年提出。其核心贡献在于通过平面基元拟合与接触引导重建，生成干净、凸且可直接用于仿真的场景几何，并结合强化学习驱动人形控制器，显著降低运动跟踪失败率并提升仿真效率。
  ko: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives is a 2025 work on physics-based character
    animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- crisp
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.14696v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (887 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives (arXiv)'
  url: https://arxiv.org/abs/2512.14696
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
CRISP 针对现有联合人体-场景重建方法中缺乏物理约束、几何噪声导致交互策略失败的问题，提出利用深度、法向和光流信息对点云进行聚类，将场景几何拟合为平面基元。该方法通过人体-场景接触建模（如利用姿态重建被遮挡的椅子座位）来补全交互中的遮挡几何，最终将重建结果用于强化学习训练人形控制器，确保物理合理性。在 EMDB 和 PROX 基准上，运动跟踪失败率从 55.2% 降至 6.9%，RL 仿真吞吐量提升 43%，并在随意拍摄视频、互联网视频甚至 Sora 生成视频上验证了泛化能力。

## 核心内容
### 方法架构
- **场景几何重建**：从单目视频中提取点云，通过基于深度、法向和光流的简单聚类管道，将场景拟合为凸的平面基元（如平面、立方体），去除噪声和伪影，生成可直接用于物理仿真的干净几何。
- **接触引导的遮挡补全**：利用人体-场景接触建模，例如根据人体坐姿姿态推断被遮挡的椅子座位形状，从而恢复交互过程中不可见的场景部分。
- **物理仿真驱动**：将重建的人体运动与场景几何输入强化学习框架，训练人形控制器（humanoid controller）执行运动跟踪策略，确保动作在物理上可行（如避免穿透、保持平衡）。

### 实验设置与关键数字
- **基准测试**：在 EMDB 和 PROX 两个以人为中心的视频基准上评估，运动跟踪失败率从基线方法的 55.2% 大幅降至 6.9%。
- **仿真效率**：RL 仿真吞吐量相比现有方法提升 43%，表明平面基元几何显著降低了物理引擎的计算开销。
- **泛化验证**：在随意拍摄视频、互联网视频以及 Sora 生成的视频上均能生成物理有效的人体运动与交互环境，证明方法对数据来源的鲁棒性。

### 结论
CRISP 通过平面基元拟合与接触引导重建，解决了单目视频中人体-场景联合重建的物理不一致问题，为机器人学和 AR/VR 领域的真实到仿真（real-to-sim）应用提供了可扩展的解决方案。其核心优势在于生成干净、可仿真的几何，并利用强化学习确保运动与场景交互的物理合理性。

## Overview
We introduce CRISP, a method that recovers simulatable human motion and scene geometry from monocular video. Prior work on joint human-scene reconstruction relies on data-driven priors and joint optimization with no physics in the loop, or recovers noisy geometry with artifacts that cause motion tracking policies with scene interactions to fail. In contrast, our key insight is to recover convex, clean, and simulation-ready geometry by fitting planar primitives to a point cloud reconstruction of the scene, via a simple clustering pipeline over depth, normals, and flow. To reconstruct scene geometry that might be occluded during interactions, we make use of human-scene contact modeling (e.g., we use human posture to reconstruct the occluded seat of a chair). Finally, we ensure that human and scene reconstructions are physically-plausible by using them to drive a humanoid controller via reinforcement learning. Our approach reduces motion tracking failure rates from 55.2\% to 6.9\% on human-centric video benchmarks (EMDB, PROX), while delivering a 43\% faster RL simulation throughput. We further validate it on in-the-wild videos including casually-captured videos, Internet videos, and even Sora-generated videos. This demonstrates CRISP's ability to generate physically-valid human motion and interaction environments at scale, greatly advancing real-to-sim applications for robotics and AR/VR.

## 参考
- http://arxiv.org/abs/2512.14696v3

## 개요
CRISP는 기존의 결합된 인간-장면 재구성 방법에서 물리적 제약이 부족하고 기하학적 노이즈로 인해 상호작용 전략이 실패하는 문제를 해결하기 위해, 깊이, 법선 및 광류 정보를 활용하여 포인트 클라우드를 클러스터링하고 장면 기하학을 평면 프리미티브로 피팅하는 방법을 제안합니다. 이 방법은 인간-장면 접촉 모델링(예: 자세를 이용해 가려진 의자 좌석 재구성)을 통해 상호작용 중 가려진 기하학을 보완하며, 최종적으로 재구성 결과를 강화 학습에 사용하여 휴머노이드 컨트롤러를 훈련시켜 물리적 타당성을 보장합니다. EMDB 및 PROX 벤치마크에서 모션 추적 실패율이 55.2%에서 6.9%로 감소했고, RL 시뮬레이션 처리량이 43% 향상되었으며, 무작위 촬영 비디오, 인터넷 비디오 및 Sora 생성 비디오에서도 일반화 능력을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
- **장면 기하학 재구성**: 단안 비디오에서 포인트 클라우드를 추출하고, 깊이, 법선 및 광류 기반의 간단한 클러스터링 파이프라인을 통해 장면을 볼록한 평면 프리미티브(예: 평면, 큐브)로 피팅하여 노이즈와 아티팩트를 제거하고, 물리 시뮬레이션에 직접 사용할 수 있는 깨끗한 기하학을 생성합니다.
- **접촉 기반 가려짐 보완**: 인간-장면 접촉 모델링을 활용하여, 예를 들어 인간의 앉은 자세를 기반으로 가려진 의자 좌석의 형태를 추론함으로써 상호작용 중 보이지 않는 장면 부분을 복원합니다.
- **물리 시뮬레이션 기반**: 재구성된 인간 모션과 장면 기하학을 강화 학습 프레임워크에 입력하여 휴머노이드 컨트롤러를 훈련시키고 모션 추적 전략을 실행하며, 동작이 물리적으로 가능하도록(예: 관통 방지, 균형 유지) 보장합니다.

### 실험 설정 및 주요 수치
- **벤치마크 테스트**: 인간 중심의 두 비디오 벤치마크인 EMDB 및 PROX에서 평가했으며, 모션 추적 실패율이 기준 방법의 55.2%에서 6.9%로 크게 감소했습니다.
- **시뮬레이션 효율성**: RL 시뮬레이션 처리량이 기존 방법 대비 43% 향상되어, 평면 프리미티브 기하학이 물리 엔진의 계산 오버헤드를 크게 줄였음을 보여줍니다.
- **일반화 검증**: 무작위 촬영 비디오, 인터넷 비디오 및 Sora 생성 비디오에서도 물리적으로 유효한 인간 모션과 상호작용 환경을 생성할 수 있어, 데이터 소스에 대한 방법의 강건성을 입증합니다.

### 결론
CRISP는 평면 프리미티브 피팅과 접촉 기반 재구성을 통해 단안 비디오에서 인간-장면 결합 재구성의 물리적 불일치 문제를 해결하며, 로보틱스 및 AR/VR 분야의 real-to-sim 응용을 위한 확장 가능한 솔루션을 제공합니다. 핵심 장점은 깨끗하고 시뮬레이션 가능한 기하학을 생성하고, 강화 학습을 활용하여 모션과 장면 상호작용의 물리적 타당성을 보장한다는 점입니다.
