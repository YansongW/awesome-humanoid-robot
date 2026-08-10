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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06382v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (794 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2602.06382v2

## 개요
이 연구는 시각 기반 휴머노이드 운동의 두 가지 주요 난제, 즉 sim-to-real 격차로 인한 인식 노이즈와 다양한 지형 훈련에서의 목표 충돌을 다룹니다. 이를 위해 저자들은 고충실도 깊이 센서 시뮬레이션(스테레오 매칭 아티팩트 및 캘리브레이션 불확실성 모사)과 시각 인식 행동 증류(잠재 공간 정렬 및 노이즈 불변 보조 작업 결합)를 포함한 엔드투엔드 프레임워크를 구축했습니다. 동시에 지형 특화 보상 형성과 멀티 크리틱, 멀티 디스크리미네이터 학습을 도입하여 전용 네트워크가 각 지형의 역학 및 운동 사전 지식을 포착하도록 했습니다. 두 가지 휴머노이드 플랫폼에서 검증한 결과, 정책은 다양한 환경에서 강건한 성능을 보였으며 높은 플랫폼, 넓은 간격, 양방향 긴 계단과 같은 도전 과제를 성공적으로 처리했습니다.

## 핵심 내용
### 방법 아키텍처
- **고충실도 깊이 센서 시뮬레이션**: sim-to-real 격차를 해결하기 위해 실제 스테레오 깊이 카메라의 스테레오 매칭 아티팩트와 캘리브레이션 불확실성을 포착하는 시뮬레이션 모델을 개발하여 더 현실적인 노이즈 깊이 관측을 생성합니다.
- **시각 인식 행동 증류**: 잠재 공간 정렬과 노이즈 불변 보조 작업을 통해 특권 높이 맵의 지식을 노이즈 깊이 관측으로 전이하여 원시 픽셀에서 운동까지의 엔드투엔드 학습을 구현합니다.
- **지형 특화 보상 형성**: 멀티 크리틱 및 멀티 디스크리미네이터 학습을 도입하여 각 지형 유형(예: 평지, 계단, 높은 플랫폼)에 맞는 전용 네트워크를 설계하고 고유한 역학 및 운동 사전 지식을 포착합니다.

### 실험 설정
- **플랫폼**: 서로 다른 두 가지 스테레오 깊이 카메라를 장착한 휴머노이드 로봇.
- **작업**: 극한 도전(높은 플랫폼, 넓은 간격) 및 정밀 작업(양방향 긴 계단 통과) 포함.
- **평가**: 다양한 환경에서 정책의 강건성과 일반화 능력을 테스트.

### 주요 결과
- 정책은 sim-to-real 전이에서 강건한 성능을 보이며 인식 노이즈를 효과적으로 처리합니다.
- 높은 플랫폼 점프, 넓은 간격 횡단, 양방향 긴 계단 연속 등반과 같은 작업을 성공적으로 완료하여 프레임워크의 일반성을 검증했습니다.
- 기준 방법과 비교하여 정밀 작업(예: 계단 통과)에서 성능이 크게 향상되어 지형 특화 학습 전략의 효과를 입증했습니다.

### 결론
이 엔드투엔드 프레임워크는 고충실도 시뮬레이션, 행동 증류 및 지형 적응 학습을 통해 시각 기반 휴머노이드 운동의 핵심 과제를 해결하며 실제 배포를 위한 실현 가능한 솔루션을 제공합니다.
