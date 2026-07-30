---
$id: ent_paper_mimic2dm_learning_to_control_p_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mimic2DM: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions'
  zh: 'Mimic2DM: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions'
  ko: 'Mimic2DM: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions'
summary:
  en: Video data is more cost-effective than motion capture data for learning 3D character motion controllers, yet synthesizing
    realistic and diverse behaviors directly from videos remains challenging. Previous approaches typically rely on off-the-shelf
    motion reconstruction techniques to obtain 3D trajectories for physics-based imitation. These reconstruction methods struggle
    with generalizability, as they either require 3D training data (potentially scarce) or fail to produce physically plausible
    poses, hindering their application to challenging scenarios like human-object interaction (HOI) or non-human characters.
    We tackle this challenge by introducing Mimic2DM, a novel motion imitation framework that learns the control policy directly
    and solely from widely available 2D keypoint trajectorie
  zh: Mimic2DM 是一个新颖的运动模仿框架，由研究团队提出，旨在直接从广泛可用的 2D 关键点轨迹学习控制策略，无需依赖昂贵的 3D 运动数据。其核心贡献在于通过最小化重投影误差训练单视角 2D 运动跟踪策略，并利用 Transformer
    自回归生成器实现层次化控制，从而在物理模拟中合成逼真且多样化的 3D 角色运动。
  ko: 'Mimic2DM: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions is a paper
    on 物理动画 for humanoid robotics.'
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
- mimic2dm
- physics_based
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: Mimic2DM: Learning to Control
    Physically-simulated 3D Characters via Generating and Mimicking 2D Motions. [2026-07-29] zh content backfilled from English
    abstract via scripts/sinicize_english_cards.py'
sources:
- id: src_001
  type: website
  title: 'Mimic2DM: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions'
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Mimic2DM 通过直接从视频中提取的 2D 关键点轨迹学习控制策略，解决了传统方法依赖 3D 运动重建的泛化性问题。该框架首先训练一个通用的单视角 2D 运动跟踪策略，通过最小化重投影误差在物理模拟中跟随任意 2D 参考运动。当策略在来自不同或略微不同视角的多样化 2D 运动上训练时，它能通过聚合多视角信息获得 3D 运动跟踪能力。此外，研究团队开发了一个基于 Transformer 的自回归 2D 运动生成器，并将其集成到层次化控制框架中，生成高质量 2D 参考轨迹以指导跟踪策略。

## 核心内容
### 方法概述
Mimic2DM 的核心创新在于完全绕过 3D 运动重建，直接利用 2D 关键点轨迹进行物理模拟控制。框架包含两个主要组件：
- **2D 运动跟踪策略**：通过最小化重投影误差训练，使策略在物理模拟中能够跟随任意 2D 参考运动。该策略在多样化视角的 2D 运动数据上训练后，能通过多视角聚合隐式学习 3D 运动跟踪能力。
- **Transformer 自回归生成器**：基于 Transformer 架构，生成高质量 2D 参考轨迹，作为层次化控制框架的上层指导。

### 实验设置与关键结果
- **训练数据**：仅使用从视频中提取的 2D 关键点轨迹，无需任何 3D 运动数据。
- **测试领域**：涵盖舞蹈、足球运球、动物运动等多样化场景，包括人-物交互（HOI）和非人类角色。
- **关键性能**：
  - 在舞蹈动作合成中，Mimic2DM 生成的物理合理动作与真实视频高度一致。
  - 在足球运球任务中，成功模拟了人与球的交互，无需显式 3D 运动数据。
  - 在动物运动（如四足行走）中，展示了跨物种的泛化能力。
- **对比基线**：相比依赖 3D 重建的方法，Mimic2DM 在泛化性和物理合理性上显著提升，尤其在挑战性场景（如 HOI）中表现突出。

### 结论
Mimic2DM 证明了直接从 2D 关键点轨迹学习 3D 角色运动控制的可行性，为低成本、高泛化性的运动合成提供了新范式。项目网站提供更多演示和代码：https://jiann-li.github.io/mimic2dm/

## Overview
Video data is more cost-effective than motion capture data for learning 3D character motion controllers, yet synthesizing realistic and diverse behaviors directly from videos remains challenging. Previous approaches typically rely on off-the-shelf motion reconstruction techniques to obtain 3D trajectories for physics-based imitation. These reconstruction methods struggle with generalizability, as they either require 3D training data (potentially scarce) or fail to produce physically plausible poses, hindering their application to challenging scenarios like human-object interaction (HOI) or non-human characters. We tackle this challenge by introducing Mimic2DM, a novel motion imitation framework that learns the control policy directly and solely from widely available 2D keypoint trajectories extracted from videos. By minimizing the reprojection error, we train a general single-view 2D motion tracking policy capable of following arbitrary 2D reference motions in physics simulation, using only 2D motion data. The policy, when trained on diverse 2D motions captured from different or slightly different viewpoints, can further acquire 3D motion tracking capabilities by aggregating multiple views. Moreover, we develop a transformer-based autoregressive 2D motion generator and integrate it into a hierarchical control framework, where the generator produces high-quality 2D reference trajectories to guide the tracking policy. We show that the proposed approach is versatile and can effectively learn to synthesize physically plausible and diverse motions across a range of domains, including dancing, soccer dribbling, and animal movements, without any reliance on explicit 3D motion data. Project Website: https://jiann-li.github.io/mimic2dm/

## 개요
비디오 데이터는 3D 캐릭터 모션 컨트롤러를 학습하는 데 모션 캡처 데이터보다 비용 효율적이지만, 비디오에서 직접 현실적이고 다양한 행동을 합성하는 것은 여전히 어려운 과제입니다. 기존 접근법은 일반적으로 물리 기반 모방을 위해 3D 궤적을 얻기 위해 기성 모션 재구성 기술에 의존합니다. 이러한 재구성 방법은 일반화에 어려움을 겪는데, 3D 학습 데이터(잠재적으로 부족할 수 있음)를 필요로 하거나 물리적으로 타당한 포즈를 생성하지 못해 인간-객체 상호작용(HOI)이나 비인간 캐릭터와 같은 까다로운 시나리오에 적용하기 어렵습니다. 우리는 Mimic2DM이라는 새로운 모션 모방 프레임워크를 도입하여 이 문제를 해결합니다. 이 프레임워크는 비디오에서 추출한 널리 사용 가능한 2D 키포인트 궤적만을 직접 사용하여 제어 정책을 학습합니다. 재투영 오차를 최소화함으로써, 2D 모션 데이터만을 사용하여 물리 시뮬레이션에서 임의의 2D 참조 모션을 추적할 수 있는 일반적인 단일 시점 2D 모션 추적 정책을 훈련합니다. 이 정책은 서로 다른 또는 약간 다른 시점에서 캡처된 다양한 2D 모션으로 훈련될 때, 여러 시점을 집계하여 3D 모션 추적 능력을 추가로 획득할 수 있습니다. 또한, 우리는 트랜스포머 기반의 자기회귀 2D 모션 생성기를 개발하고 이를 계층적 제어 프레임워크에 통합하여, 생성기가 고품질의 2D 참조 궤적을 생성하여 추적 정책을 안내합니다. 제안된 접근법은 다재다능하며, 명시적인 3D 모션 데이터에 의존하지 않고 춤, 축구 드리블, 동물 움직임 등 다양한 영역에서 물리적으로 타당하고 다양한 모션을 합성하는 것을 효과적으로 학습할 수 있음을 보여줍니다. 프로젝트 웹사이트: https://jiann-li.github.io/mimic2dm/

## 핵심 내용
비디오 데이터는 3D 캐릭터 모션 컨트롤러를 학습하는 데 모션 캡처 데이터보다 비용 효율적이지만, 비디오에서 직접 현실적이고 다양한 행동을 합성하는 것은 여전히 어려운 과제입니다. 기존 접근법은 일반적으로 물리 기반 모방을 위해 3D 궤적을 얻기 위해 기성 모션 재구성 기술에 의존합니다. 이러한 재구성 방법은 일반화에 어려움을 겪는데, 3D 학습 데이터(잠재적으로 부족할 수 있음)를 필요로 하거나 물리적으로 타당한 포즈를 생성하지 못해 인간-객체 상호작용(HOI)이나 비인간 캐릭터와 같은 까다로운 시나리오에 적용하기 어렵습니다. 우리는 Mimic2DM이라는 새로운 모션 모방 프레임워크를 도입하여 이 문제를 해결합니다. 이 프레임워크는 비디오에서 추출한 널리 사용 가능한 2D 키포인트 궤적만을 직접 사용하여 제어 정책을 학습합니다. 재투영 오차를 최소화함으로써, 2D 모션 데이터만을 사용하여 물리 시뮬레이션에서 임의의 2D 참조 모션을 추적할 수 있는 일반적인 단일 시점 2D 모션 추적 정책을 훈련합니다. 이 정책은 서로 다른 또는 약간 다른 시점에서 캡처된 다양한 2D 모션으로 훈련될 때, 여러 시점을 집계하여 3D 모션 추적 능력을 추가로 획득할 수 있습니다. 또한, 우리는 트랜스포머 기반의 자기회귀 2D 모션 생성기를 개발하고 이를 계층적 제어 프레임워크에 통합하여, 생성기가 고품질의 2D 참조 궤적을 생성하여 추적 정책을 안내합니다. 제안된 접근법은 다재다능하며, 명시적인 3D 모션 데이터에 의존하지 않고 춤, 축구 드리블, 동물 움직임 등 다양한 영역에서 물리적으로 타당하고 다양한 모션을 합성하는 것을 효과적으로 학습할 수 있음을 보여줍니다. 프로젝트 웹사이트: https://jiann-li.github.io/mimic2dm/

## 参考
- Semantic Scholar search: Mimic2DM: Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions
