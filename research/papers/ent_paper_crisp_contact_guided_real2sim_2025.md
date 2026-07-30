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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.14696v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
우리는 단안 비디오에서 시뮬레이션 가능한 인간 동작과 장면 기하학을 복원하는 방법인 CRISP를 소개합니다. 인간-장면 공동 복원에 관한 기존 연구는 물리적 상호작용 없이 데이터 기반 사전 지식과 공동 최적화에 의존하거나, 잡음이 있는 기하학을 복원하여 장면 상호작용을 포함한 동작 추적 정책이 실패하게 만듭니다. 반면, 우리의 핵심 통찰은 깊이, 법선, 흐름에 대한 간단한 클러스터링 파이프라인을 통해 장면의 포인트 클라우드 복원에 평면 프리미티브를 피팅하여 볼록하고 깨끗하며 시뮬레이션 준비가 된 기하학을 복원하는 것입니다. 상호작용 중에 가려질 수 있는 장면 기하학을 복원하기 위해 인간-장면 접촉 모델링을 활용합니다(예: 인간 자세를 사용하여 가려진 의자 좌석을 복원). 마지막으로, 강화 학습을 통해 휴머노이드 컨트롤러를 구동하는 데 이를 사용하여 인간과 장면 복원이 물리적으로 타당하도록 보장합니다. 우리의 접근 방식은 인간 중심 비디오 벤치마크(EMDB, PROX)에서 동작 추적 실패율을 55.2%에서 6.9%로 줄이고, RL 시뮬레이션 처리량을 43% 향상시킵니다. 또한 캐주얼하게 촬영된 비디오, 인터넷 비디오, 심지어 Sora 생성 비디오를 포함한 실제 비디오에서 이를 검증합니다. 이는 CRISP가 대규모로 물리적으로 유효한 인간 동작과 상호작용 환경을 생성할 수 있는 능력을 보여주며, 로봇공학 및 AR/VR을 위한 실물-시뮬레이션 응용을 크게 발전시킵니다.

## 핵심 내용
우리는 단안 비디오에서 시뮬레이션 가능한 인간 동작과 장면 기하학을 복원하는 방법인 CRISP를 소개합니다. 인간-장면 공동 복원에 관한 기존 연구는 물리적 상호작용 없이 데이터 기반 사전 지식과 공동 최적화에 의존하거나, 잡음이 있는 기하학을 복원하여 장면 상호작용을 포함한 동작 추적 정책이 실패하게 만듭니다. 반면, 우리의 핵심 통찰은 깊이, 법선, 흐름에 대한 간단한 클러스터링 파이프라인을 통해 장면의 포인트 클라우드 복원에 평면 프리미티브를 피팅하여 볼록하고 깨끗하며 시뮬레이션 준비가 된 기하학을 복원하는 것입니다. 상호작용 중에 가려질 수 있는 장면 기하학을 복원하기 위해 인간-장면 접촉 모델링을 활용합니다(예: 인간 자세를 사용하여 가려진 의자 좌석을 복원). 마지막으로, 강화 학습을 통해 휴머노이드 컨트롤러를 구동하는 데 이를 사용하여 인간과 장면 복원이 물리적으로 타당하도록 보장합니다. 우리의 접근 방식은 인간 중심 비디오 벤치마크(EMDB, PROX)에서 동작 추적 실패율을 55.2%에서 6.9%로 줄이고, RL 시뮬레이션 처리량을 43% 향상시킵니다. 또한 캐주얼하게 촬영된 비디오, 인터넷 비디오, 심지어 Sora 생성 비디오를 포함한 실제 비디오에서 이를 검증합니다. 이는 CRISP가 대규모로 물리적으로 유효한 인간 동작과 상호작용 환경을 생성할 수 있는 능력을 보여주며, 로봇공학 및 AR/VR을 위한 실물-시뮬레이션 응용을 크게 발전시킵니다.

## 参考
- http://arxiv.org/abs/2512.14696v3
