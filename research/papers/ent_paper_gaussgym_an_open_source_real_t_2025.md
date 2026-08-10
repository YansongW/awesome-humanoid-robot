---
$id: ent_paper_gaussgym_an_open_source_real_t_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels'
  zh: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels'
  ko: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels'
summary:
  en: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels is a 2025 work on locomotion for
    humanoid robots.'
  zh: GaussGym 是一个 2025 年开源的实到仿框架，由研究团队提出，用于从像素学习人形机器人运动。其核心贡献是将 3D Gaussian Splatting 作为可替换渲染器集成到 IsaacGym 等物理仿真器中，实现每秒超过
    100,000 步的高通量仿真，同时保持高视觉保真度，并展示了在 sim-to-real 场景中的有效性。
  ko: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels is a 2025 work on locomotion for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gaussgym
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.15352v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1001 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'GaussGym: An open-source real-to-sim framework for learning locomotion from pixels (arXiv)'
  url: https://arxiv.org/abs/2510.15352
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
GaussGym 通过将 3D Gaussian Splatting 作为即插即用渲染器嵌入向量化物理仿真器（如 IsaacGym），在消费级 GPU 上实现了超过 100,000 步/秒的仿真速度，同时维持高视觉保真度。该框架在多种任务中展示了其性能，并验证了在 sim-to-real 机器人设置中的适用性。除了基于深度的感知，结果还表明丰富的视觉语义能改善导航与决策，例如避开不良区域。此外，GaussGym 能轻松集成来自 iPhone 扫描、大规模场景数据集（如 GrandTour、ARKit）以及生成式视频模型（如 Veo）输出的数千个环境，从而快速创建逼真的训练世界。

## 核心内容
### 方法
GaussGym 提出了一种新颖的实到仿框架，核心是将 3D Gaussian Splatting 作为可替换渲染器集成到向量化物理仿真器中。这种方法结合了高通量仿真与高保真视觉感知，使机器人能从像素级输入学习运动策略。

### 架构
- **渲染器集成**：3D Gaussian Splatting 作为即插即用组件，替代传统渲染管线，与 IsaacGym 等物理引擎无缝协作。
- **仿真速度**：在消费级 GPU 上达到每秒超过 100,000 步的仿真速度，远超传统方法。
- **视觉保真度**：保持高视觉质量，支持多样化的任务场景。

### 实验设置
- **任务多样性**：在多种 locomotion 任务上验证框架性能，涵盖不同复杂度的环境。
- **数据来源**：集成来自 iPhone 扫描、大规模场景数据集（如 GrandTour、ARKit）以及生成式视频模型（如 Veo）的输出，实现快速创建数千个训练环境。
- **感知模态**：除了深度感知，重点利用视觉语义信息，如避免不良区域，提升导航与决策能力。

### 关键数字
- 仿真速度：超过 100,000 步/秒（消费级 GPU）。
- 环境数量：支持数千个环境的并行训练。
- 数据集：包括 GrandTour、ARKit 等大规模场景数据集。

### 结论
GaussGym 通过桥接高通量仿真与高保真感知，推动了可扩展和泛化的机器人学习。所有代码和数据将开源，供社区进一步开发。视频、代码和数据可在 https://escontrela.me/gauss_gym/ 获取。

## Overview
We present a novel approach for photorealistic robot simulation that integrates 3D Gaussian Splatting as a drop-in renderer within vectorized physics simulators such as IsaacGym. This enables unprecedented speed -- exceeding 100,000 steps per second on consumer GPUs -- while maintaining high visual fidelity, which we showcase across diverse tasks. We additionally demonstrate its applicability in a sim-to-real robotics setting. Beyond depth-based sensing, our results highlight how rich visual semantics improve navigation and decision-making, such as avoiding undesirable regions. We further showcase the ease of incorporating thousands of environments from iPhone scans, large-scale scene datasets (e.g., GrandTour, ARKit), and outputs from generative video models like Veo, enabling rapid creation of realistic training worlds. This work bridges high-throughput simulation and high-fidelity perception, advancing scalable and generalizable robot learning. All code and data will be open-sourced for the community to build upon. Videos, code, and data available at https://escontrela.me/gauss_gym/.

## 参考
- http://arxiv.org/abs/2510.15352v1

## 개요
GaussGym은 3D Gaussian Splatting을 플러그 앤 플레이 렌더러로 벡터화된 물리 시뮬레이터(예: IsaacGym)에 내장하여, 소비자용 GPU에서 초당 100,000스텝 이상의 시뮬레이션 속도를 달성하면서도 높은 시각적 충실도를 유지합니다. 이 프레임워크는 다양한 작업에서 성능을 입증했으며, sim-to-real 로봇 설정에서의 적용 가능성을 검증했습니다. 깊이 기반 인식 외에도, 풍부한 시각적 의미 정보가 탐색 및 의사 결정(예: 바람직하지 않은 영역 회피)을 개선할 수 있음을 결과가 보여줍니다. 또한 GaussGym은 iPhone 스캔, 대규모 장면 데이터셋(예: GrandTour, ARKit), 생성형 비디오 모델(예: Veo)의 출력에서 얻은 수천 개의 환경을 쉽게 통합하여 사실적인 훈련 세계를 빠르게 생성할 수 있습니다.

## 핵심 내용
### 방법
GaussGym은 3D Gaussian Splatting을 벡터화된 물리 시뮬레이터에 교체 가능한 렌더러로 통합하는 새로운 실사(sim-to-real) 프레임워크를 제안합니다. 이 방법은 높은 처리량의 시뮬레이션과 높은 충실도의 시각적 인식을 결합하여, 로봇이 픽셀 수준 입력에서 운동 정책을 학습할 수 있게 합니다.

### 아키텍처
- **렌더러 통합**: 3D Gaussian Splatting은 플러그 앤 플레이 구성 요소로 작동하여 기존 렌더링 파이프라인을 대체하고 IsaacGym과 같은 물리 엔진과 원활하게 협력합니다.
- **시뮬레이션 속도**: 소비자용 GPU에서 초당 100,000스텝 이상의 시뮬레이션 속도를 달성하며, 이는 기존 방법을 크게 능가합니다.
- **시각적 충실도**: 높은 시각적 품질을 유지하여 다양한 작업 시나리오를 지원합니다.

### 실험 설정
- **작업 다양성**: 다양한 복잡성의 환경을 포함한 여러 보행(locomotion) 작업에서 프레임워크 성능을 검증합니다.
- **데이터 소스**: iPhone 스캔, 대규모 장면 데이터셋(예: GrandTour, ARKit), 생성형 비디오 모델(예: Veo)의 출력을 통합하여 수천 개의 훈련 환경을 빠르게 생성합니다.
- **인식 양식**: 깊이 인식 외에도, 바람직하지 않은 영역 회피와 같은 시각적 의미 정보를 활용하여 탐색 및 의사 결정 능력을 향상시키는 데 중점을 둡니다.

### 주요 수치
- 시뮬레이션 속도: 초당 100,000스텝 이상(소비자용 GPU).
- 환경 수: 수천 개 환경의 병렬 훈련 지원.
- 데이터셋: GrandTour, ARKit 등 대규모 장면 데이터셋 포함.

### 결론
GaussGym은 높은 처리량의 시뮬레이션과 높은 충실도의 인식을 연결함으로써 확장 가능하고 일반화 가능한 로봇 학습을 촉진합니다. 모든 코드와 데이터는 커뮤니티의 추가 개발을 위해 오픈소스로 공개될 예정입니다. 비디오, 코드, 데이터는 https://escontrela.me/gauss_gym/ 에서 확인할 수 있습니다.
