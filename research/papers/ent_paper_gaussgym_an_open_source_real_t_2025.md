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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.15352v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
본 논문은 3D 가우시안 스플래팅(3D Gaussian Splatting)을 IsaacGym과 같은 벡터화된 물리 시뮬레이터 내에서 플러그인 렌더러로 통합하는 사실적인 로봇 시뮬레이션을 위한 새로운 접근 방식을 제시합니다. 이를 통해 소비자용 GPU에서 초당 100,000 스텝을 초과하는 전례 없는 속도를 달성하면서도 높은 시각적 충실도를 유지하며, 다양한 작업에서 그 성능을 입증합니다. 또한 sim-to-real 로봇 환경에서의 적용 가능성을 보여줍니다. 깊이 기반 센싱을 넘어, 풍부한 시각적 의미론이 바람직하지 않은 영역을 회피하는 등 내비게이션과 의사 결정을 어떻게 개선하는지 강조합니다. iPhone 스캔, 대규모 장면 데이터셋(예: GrandTour, ARKit), Veo와 같은 생성형 비디오 모델의 출력물을 통해 수천 개의 환경을 손쉽게 통합하여 현실적인 훈련 세계를 신속하게 생성할 수 있음을 추가로 보여줍니다. 이 연구는 고처리량 시뮬레이션과 고충실도 인식을 연결하여 확장 가능하고 일반화 가능한 로봇 학습을 발전시킵니다. 모든 코드와 데이터는 커뮤니티가 활용할 수 있도록 오픈소스로 공개될 예정입니다. 비디오, 코드, 데이터는 https://escontrela.me/gauss_gym/에서 확인할 수 있습니다.

## 핵심 내용
본 논문은 3D 가우시안 스플래팅(3D Gaussian Splatting)을 IsaacGym과 같은 벡터화된 물리 시뮬레이터 내에서 플러그인 렌더러로 통합하는 사실적인 로봇 시뮬레이션을 위한 새로운 접근 방식을 제시합니다. 이를 통해 소비자용 GPU에서 초당 100,000 스텝을 초과하는 전례 없는 속도를 달성하면서도 높은 시각적 충실도를 유지하며, 다양한 작업에서 그 성능을 입증합니다. 또한 sim-to-real 로봇 환경에서의 적용 가능성을 보여줍니다. 깊이 기반 센싱을 넘어, 풍부한 시각적 의미론이 바람직하지 않은 영역을 회피하는 등 내비게이션과 의사 결정을 어떻게 개선하는지 강조합니다. iPhone 스캔, 대규모 장면 데이터셋(예: GrandTour, ARKit), Veo와 같은 생성형 비디오 모델의 출력물을 통해 수천 개의 환경을 손쉽게 통합하여 현실적인 훈련 세계를 신속하게 생성할 수 있음을 추가로 보여줍니다. 이 연구는 고처리량 시뮬레이션과 고충실도 인식을 연결하여 확장 가능하고 일반화 가능한 로봇 학습을 발전시킵니다. 모든 코드와 데이터는 커뮤니티가 활용할 수 있도록 오픈소스로 공개될 예정입니다. 비디오, 코드, 데이터는 https://escontrela.me/gauss_gym/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2510.15352v1
