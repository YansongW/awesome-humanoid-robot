---
$id: ent_paper_now_you_see_that_learning_end_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Now You See That: Learning End-to-End Humanoid Locomotion from Raw Pixels'
  zh: 'Now You See That: Learning End-to-End Humanoid Locomotion from Raw Pixels'
  ko: 'Now You See That: Learning End-to-End Humanoid Locomotion from Raw Pixels'
summary:
  en: 'Now You See That: Learning End-to-End Humanoid Locomotion from Raw Pixels is a 2026 work on locomotion for humanoid
    robots.'
  zh: 这是一项2026年关于人形机器人视觉驱动运动的研究，由作者团队提出。核心贡献包括：开发高保真深度传感器仿真以缩小sim-to-real差距，以及提出视觉感知行为蒸馏方法结合地形特定奖励塑造，实现从原始像素到鲁棒运动的端到端学习。该方法在两种不同立体深度相机的人形平台上验证，能处理高平台、宽间隙及双向长楼梯等极端与精细任务。
  ko: 'Now You See That: Learning End-to-End Humanoid Locomotion from Raw Pixels is a 2026 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- now_you_see_that
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06382v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Now You See That: Learning End-to-End Humanoid Locomotion from Raw Pixels (arXiv)'
  url: https://arxiv.org/abs/2602.06382
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对视觉人形运动的两大难题：sim-to-real差距带来的感知噪声，以及多样化地形训练中目标冲突。为此，作者构建了端到端框架，包含高保真深度传感器仿真（模拟立体匹配伪影和校准不确定性）和视觉感知行为蒸馏（结合潜在空间对齐与噪声不变辅助任务）。同时，引入地形特定奖励塑造与多评论家、多判别器学习，让专用网络捕捉各地形动态与运动先验。在两种人形平台上验证，策略在多样环境中表现鲁棒，成功应对高平台、宽间隙及双向长楼梯等挑战。

## 核心内容
### 方法架构
- **高保真深度传感器仿真**：针对sim-to-real差距，开发仿真模型捕捉真实立体深度相机的立体匹配伪影和校准不确定性，生成更真实的噪声深度观测。
- **视觉感知行为蒸馏**：通过潜在空间对齐和噪声不变辅助任务，将特权高度图的知识迁移到噪声深度观测，实现从原始像素到运动的端到端学习。
- **地形特定奖励塑造**：引入多评论家（multi-critic）和多判别器（multi-discriminator）学习，为每种地形类型（如平地、楼梯、高平台）设计专用网络，捕获其独特动力学和运动先验。

### 实验设置
- **平台**：两种不同立体深度相机的人形机器人。
- **任务**：包括极端挑战（高平台、宽间隙）和精细任务（双向长楼梯遍历）。
- **评估**：在多样环境中测试策略的鲁棒性和泛化能力。

### 关键结果
- 策略在sim-to-real转移中表现鲁棒，有效处理感知噪声。
- 成功完成高平台跳跃、宽间隙跨越及双向长楼梯连续攀爬等任务，验证了框架的通用性。
- 与基线方法相比，在精细任务（如楼梯遍历）上性能显著提升，表明地形特定学习策略的有效性。

### 结论
该端到端框架通过高保真仿真、行为蒸馏和地形自适应学习，解决了视觉人形运动的关键挑战，为实际部署提供了可行方案。

## Overview
Achieving robust vision-based humanoid locomotion remains challenging due to two fundamental issues: the sim-to-real gap introduces significant perception noise that degrades performance on fine-grained tasks, and training a unified policy across diverse terrains is hindered by conflicting learning objectives. To address these challenges, we present an end-to-end framework for vision-driven humanoid locomotion. For robust sim-to-real transfer, we develop a high-fidelity depth sensor simulation that captures stereo matching artifacts and calibration uncertainties inherent in real-world sensing. We further propose a vision-aware behavior distillation approach that combines latent space alignment with noise-invariant auxiliary tasks, enabling effective knowledge transfer from privileged height maps to noisy depth observations. For versatile terrain adaptation, we introduce terrain-specific reward shaping integrated with multi-critic and multi-discriminator learning, where dedicated networks capture the distinct dynamics and motion priors of each terrain type. We validate our approach on two humanoid platforms equipped with different stereo depth cameras. The resulting policy demonstrates robust performance across diverse environments, seamlessly handling extreme challenges such as high platforms and wide gaps, as well as fine-grained tasks including bidirectional long-term staircase traversal.

## 개요
강건한 비전 기반 휴머노이드 보행을 달성하는 것은 두 가지 근본적인 문제로 인해 여전히 어려운 과제입니다: 시뮬레이션-실제 간극은 미세 작업 성능을 저하시키는 상당한 인식 노이즈를 유발하며, 다양한 지형에서 통합 정책을 훈련하는 것은 상충되는 학습 목표로 인해 방해를 받습니다. 이러한 문제를 해결하기 위해, 우리는 비전 기반 휴머노이드 보행을 위한 종단간 프레임워크를 제시합니다. 강건한 시뮬레이션-실제 전이를 위해, 실제 센싱에 내재된 스테레오 매칭 아티팩트와 캘리브레이션 불확실성을 포착하는 고충실도 깊이 센서 시뮬레이션을 개발합니다. 또한 잠재 공간 정렬과 노이즈 불변 보조 작업을 결합한 비전 인식 행동 증류 접근법을 제안하여, 특권 높이 맵에서 노이즈가 있는 깊이 관측으로의 효과적인 지식 전이를 가능하게 합니다. 다양한 지형 적응을 위해, 다중 비평가 및 다중 판별기 학습과 통합된 지형별 보상 형성을 도입하여, 전용 네트워크가 각 지형 유형의 고유한 역학 및 운동 사전을 포착하도록 합니다. 우리는 서로 다른 스테레오 깊이 카메라를 장착한 두 휴머노이드 플랫폼에서 접근법을 검증합니다. 결과 정책은 다양한 환경에서 강건한 성능을 보여주며, 높은 플랫폼과 넓은 간격과 같은 극한 도전 과제와 양방향 장기 계단 통과를 포함한 미세 작업을 원활히 처리합니다.

## 핵심 내용
강건한 비전 기반 휴머노이드 보행을 달성하는 것은 두 가지 근본적인 문제로 인해 여전히 어려운 과제입니다: 시뮬레이션-실제 간극은 미세 작업 성능을 저하시키는 상당한 인식 노이즈를 유발하며, 다양한 지형에서 통합 정책을 훈련하는 것은 상충되는 학습 목표로 인해 방해를 받습니다. 이러한 문제를 해결하기 위해, 우리는 비전 기반 휴머노이드 보행을 위한 종단간 프레임워크를 제시합니다. 강건한 시뮬레이션-실제 전이를 위해, 실제 센싱에 내재된 스테레오 매칭 아티팩트와 캘리브레이션 불확실성을 포착하는 고충실도 깊이 센서 시뮬레이션을 개발합니다. 또한 잠재 공간 정렬과 노이즈 불변 보조 작업을 결합한 비전 인식 행동 증류 접근법을 제안하여, 특권 높이 맵에서 노이즈가 있는 깊이 관측으로의 효과적인 지식 전이를 가능하게 합니다. 다양한 지형 적응을 위해, 다중 비평가 및 다중 판별기 학습과 통합된 지형별 보상 형성을 도입하여, 전용 네트워크가 각 지형 유형의 고유한 역학 및 운동 사전을 포착하도록 합니다. 우리는 서로 다른 스테레오 깊이 카메라를 장착한 두 휴머노이드 플랫폼에서 접근법을 검증합니다. 결과 정책은 다양한 환경에서 강건한 성능을 보여주며, 높은 플랫폼과 넓은 간격과 같은 극한 도전 과제와 양방향 장기 계단 통과를 포함한 미세 작업을 원활히 처리합니다.

## 参考
- http://arxiv.org/abs/2602.06382v2
