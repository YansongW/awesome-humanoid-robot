---
$id: ent_paper_learning_to_control_physically_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions
  zh: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions
  ko: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions
summary:
  en: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions is a 2025 work on physics-based
    character animation for humanoid robots.
  zh: Mimic2DM 是 2025 年提出的一种物理仿真角色运动控制框架，由相关研究团队开发。其核心贡献在于仅利用从视频中提取的 2D 关键点轨迹，无需 3D 运动数据，即可训练出能控制 3D 角色执行多样化物理合理动作的策略，并支持人-物交互与非人角色。
  ko: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions is a 2025 work on physics-based
    character animation for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- learning_to_control_physically
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.08500v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1015 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions (arXiv)
  url: https://arxiv.org/abs/2512.08500
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对从视频数据直接学习 3D 角色运动控制器所面临的泛化性差与物理合理性不足的问题，Mimic2DM 提出了一种全新的模仿学习范式。该框架通过最小化重投影误差，训练一个通用的单视角 2D 运动跟踪策略，使其能在物理仿真中跟随任意 2D 参考运动。当该策略在来自不同视角的多样化 2D 运动数据上训练后，能够通过聚合多视角信息获得 3D 运动跟踪能力。此外，Mimic2DM 还集成了一个基于 Transformer 的自回归 2D 运动生成器，用于产生高质量参考轨迹以引导跟踪策略，从而在舞蹈、足球运球和动物运动等多个领域合成出物理合理且多样的动作。

## 核心内容
### 方法概述
Mimic2DM 的核心思想是绕过传统的 3D 运动重建步骤，直接从视频中提取的 2D 关键点轨迹学习控制策略。该方法包含两个主要组件：
- **2D 运动跟踪策略**：通过最小化重投影误差进行训练，该策略能够直接利用单视角 2D 关键点作为参考，在物理仿真中驱动角色。训练数据来自不同视角的 2D 运动，使得策略能够隐式地学习 3D 运动信息。
- **2D 运动生成器**：采用 Transformer 架构构建的自回归模型，负责生成高质量、连续的 2D 参考轨迹。该生成器与跟踪策略组成分层控制框架，生成器提供高层指导，跟踪策略负责底层物理执行。

### 实验设置与关键结果
- **训练数据**：完全依赖从公开视频中提取的 2D 关键点，未使用任何 3D 运动捕捉数据。
- **测试领域**：涵盖舞蹈、足球运球、动物运动以及人-物交互场景。
- **关键性能**：
  - 在舞蹈任务中，成功合成出包含转身、跳跃等复杂动作的流畅序列。
  - 在足球运球场景中，角色能够根据 2D 参考轨迹实现带球跑动与变向。
  - 对于非人角色（如四足动物），Mimic2DM 同样能生成物理合理的运动，展示了其跨形态泛化能力。
- **对比优势**：与依赖 3D 重建的基线方法相比，Mimic2DM 在运动多样性、物理合理性和对遮挡的鲁棒性上均表现更优，尤其在处理人-物交互时，避免了重建方法常见的穿透与滑步问题。

### 结论
Mimic2DM 证明了仅利用 2D 视频数据即可有效学习 3D 物理仿真角色的控制策略，显著降低了数据获取成本并提升了方法的通用性。该框架为从大规模互联网视频中学习复杂运动技能提供了可行路径。

## Overview
Video data is more cost-effective than motion capture data for learning 3D character motion controllers, yet synthesizing realistic and diverse behaviors directly from videos remains challenging. Previous approaches typically rely on off-the-shelf motion reconstruction techniques to obtain 3D trajectories for physics-based imitation. These reconstruction methods struggle with generalizability, as they either require 3D training data (potentially scarce) or fail to produce physically plausible poses, hindering their application to challenging scenarios like human-object interaction (HOI) or non-human characters. We tackle this challenge by introducing Mimic2DM, a novel motion imitation framework that learns the control policy directly and solely from widely available 2D keypoint trajectories extracted from videos. By minimizing the reprojection error, we train a general single-view 2D motion tracking policy capable of following arbitrary 2D reference motions in physics simulation, using only 2D motion data. The policy, when trained on diverse 2D motions captured from different or slightly different viewpoints, can further acquire 3D motion tracking capabilities by aggregating multiple views. Moreover, we develop a transformer-based autoregressive 2D motion generator and integrate it into a hierarchical control framework, where the generator produces high-quality 2D reference trajectories to guide the tracking policy. We show that the proposed approach is versatile and can effectively learn to synthesize physically plausible and diverse motions across a range of domains, including dancing, soccer dribbling, and animal movements, without any reliance on explicit 3D motion data. Project Website: https://jiann-li.github.io/mimic2dm/

## 参考
- http://arxiv.org/abs/2512.08500v1

## 개요
비디오 데이터에서 직접 3D 캐릭터 모션 컨트롤러를 학습할 때 발생하는 일반화 성능 저하와 물리적 타당성 부족 문제를 해결하기 위해, Mimic2DM은 새로운 모방 학습 패러다임을 제안한다. 이 프레임워크는 재투영 오차를 최소화하여 단일 시점 2D 모션 추적 정책을 훈련하며, 물리 시뮬레이션에서 임의의 2D 참조 모션을 따를 수 있게 한다. 이 정책이 다양한 시점의 다양한 2D 모션 데이터로 훈련되면, 다중 시점 정보를 집계하여 3D 모션 추적 능력을 얻을 수 있다. 또한 Mimic2DM은 Transformer 기반의 자기회귀 2D 모션 생성기를 통합하여 고품질 참조 궤적을 생성해 추적 정책을 안내하며, 이를 통해 춤, 축구 드리블, 동물 운동 등 여러 영역에서 물리적으로 타당하고 다양한 동작을 합성한다.

## 핵심 내용
### 방법 개요
Mimic2DM의 핵심 아이디어는 전통적인 3D 모션 재구성 단계를 우회하고, 비디오에서 추출된 2D 키포인트 궤적에서 직접 제어 정책을 학습하는 것이다. 이 방법은 두 가지 주요 구성 요소를 포함한다:
- **2D 모션 추적 정책**: 재투영 오차를 최소화하여 훈련되며, 단일 시점 2D 키포인트를 참조로 직접 사용하여 물리 시뮬레이션에서 캐릭터를 구동한다. 훈련 데이터는 다양한 시점의 2D 모션으로 구성되어, 정책이 암시적으로 3D 모션 정보를 학습할 수 있게 한다.
- **2D 모션 생성기**: Transformer 아키텍처로 구축된 자기회귀 모델로, 고품질의 연속적인 2D 참조 궤적을 생성하는 역할을 한다. 이 생성기는 추적 정책과 함께 계층적 제어 프레임워크를 구성하며, 생성기는 높은 수준의 지침을 제공하고 추적 정책은 낮은 수준의 물리적 실행을 담당한다.

### 실험 설정 및 주요 결과
- **훈련 데이터**: 공개 비디오에서 추출된 2D 키포인트에만 전적으로 의존하며, 3D 모션 캡처 데이터는 사용하지 않았다.
- **테스트 영역**: 춤, 축구 드리블, 동물 운동, 인간-물체 상호작용 시나리오를 포함한다.
- **주요 성능**:
  - 춤 작업에서 회전, 점프 등 복잡한 동작을 포함한 유연한 시퀀스를 성공적으로 합성했다.
  - 축구 드리블 시나리오에서 캐릭터는 2D 참조 궤적에 따라 공을 가지고 달리거나 방향을 전환할 수 있다.
  - 비인간 캐릭터(예: 네발 동물)의 경우에도 Mimic2DM은 물리적으로 타당한 운동을 생성할 수 있어, 형태를 넘나드는 일반화 능력을 보여준다.
- **비교 우위**: 3D 재구성에 의존하는 기준선 방법과 비교하여, Mimic2DM은 운동 다양성, 물리적 타당성, 폐색에 대한 강건성에서 더 우수한 성능을 보이며, 특히 인간-물체 상호작용 처리 시 재구성 방법에서 흔히 발생하는 관통 및 미끄러짐 문제를 피한다.

### 결론
Mimic2DM은 2D 비디오 데이터만으로도 3D 물리 시뮬레이션 캐릭터의 제어 정책을 효과적으로 학습할 수 있음을 입증하며, 데이터 획득 비용을 크게 줄이고 방법의 일반성을 향상시킨다. 이 프레임워크는 대규모 인터넷 비디오에서 복잡한 운동 기술을 학습할 수 있는 실현 가능한 경로를 제공한다.
