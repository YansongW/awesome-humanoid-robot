---
$id: ent_paper_embodimentsemantic_a_spatial_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EmbodimentSemantic: A Spatial Scene-Graph Dataset and Benchmark for Vision-Language Models on Embodied Manipulation
    Trajectories'
  zh: 'EmbodimentSemantic: A Spatial Scene-Graph Dataset and Benchmark for Vision-Language Models on Embodied Manipulation
    Trajectories'
  ko: 'EmbodimentSemantic: A Spatial Scene-Graph Dataset and Benchmark for Vision-Language Models on Embodied Manipulation
    Trajectories'
summary:
  en: 'arXiv:2607.00020v1 Announce Type: new Abstract: Spatial grounding remains a key limitation of vision-language-action
    (VLA) systems for robotic manipulation. While current models can recognize objects and follow language instructions, they
    often lack an explicit representation of how objects are arranged in space, including support, containment, ordering,
    occlusion, and depth-sensitive relations. We introduce EmbodimentSemantic, a spatial scene-graph dataset and benchmark
    for evaluating relational grounding in embodied manipulation. EmbodimentSemantic represents scenes as directed object-relation-object
    triplets, where each triplet specifies a spatial relation between an ordered pair of objects using a fixed set of relations.
    This representation enables direct evaluation of object binding, relation prediction, and spatial consistency. The dataset
    includes real-world manipulation observations collected with the low-cost SO101 robot arm, together with generated scene
    graphs for studying spatial grounding in practical robotic settings. To provide controlled validation, we also introduce
    a simulator-grounded LIBERO benchmark with over 60K manipulation frames and more than 120K camera-specific scene graphs
    across paired third-person and wrist views, where ground-truth relations are derived automatically from MuJoCo geometry,
    world coordinates, camera projections, and visibility constraints. We further test whether scene graphs improve downstream
    control by injecting them into existing VLA policy prompts. Experiments across open-source and commercial VLMs show that
    current models often predict plausible relations but struggle with exact depth-aware and viewpoint-dependent spatial structure.
    EmbodimentSemantic provides a unified framework for diagnosing spatial grounding in VLM perception and testing its utility
    for VLA manipulation.'
  zh: EmbodimentSemantic 是一个用于评估具身操作中空间关系理解的数据集与基准，由研究团队提出。其核心贡献在于将场景表示为有向对象-关系-对象三元组，并包含真实世界与仿真数据，以诊断视觉-语言模型在深度感知和视角依赖空间结构上的局限。
  ko: 'arXiv:2607.00020v1 Announce Type: new Abstract: Spatial grounding remains a key limitation of vision-language-action
    (VLA) systems for robotic manipulation. While current models can recognize objects and follow language instructions, they
    often lack an explicit representation of how objects are arranged in space, including support, containment, ordering,
    occlusion, and depth-sensitive relations. We introduce EmbodimentSemantic, a spatial scene-graph dataset and benchmark
    for evaluating relational grounding in embodied manipulation. EmbodimentSemantic represents scenes as directed object-relation-object
    triplets, where each triplet specifies a spatial relation between an ordered pair of objects using a fixed set of relations.
    This representation enables direct evaluation of object binding, relation prediction, and spatial consistency. The dataset
    includes real-world manipulation observations collected with the low-cost SO101 robot arm, together with generated scene
    graphs for studying spatial grounding in practical robotic settings. To provide controlled validation, we also introduce
    a simulator-grounded LIBERO benchmark with over 60K manipulation frames and more than 120K camera-specific scene graphs
    across paired third-person and wrist views, where ground-truth relations are derived automatically from MuJoCo geometry,
    world coordinates, camera projections, and visibility constraints. We further test whether scene graphs improve downstream
    control by injecting them into existing VLA policy prompts. Experiments across open-source and commercial VLMs show that
    current models often predict plausible relations but struggle with exact depth-aware and viewpoint-dependent spatial structure.
    EmbodimentSemantic provides a unified framework for diagnosing spatial grounding in VLM perception and testing its utility
    for VLA manipulation.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- embodimentsemantic
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00020v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (770 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'EmbodimentSemantic: A Spatial Scene-Graph Dataset and Benchmark for Vision-Language Models on Embodied Manipulation
    Trajectories (arXiv)'
  url: https://arxiv.org/abs/2607.00020
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
EmbodimentSemantic 旨在解决视觉-语言-动作系统在机器人操作中空间定位能力不足的问题。该工作将场景表示为有向对象-关系-对象三元组，使用固定关系集描述对象间的空间关系，从而直接评估对象绑定、关系预测和空间一致性。数据集包含使用低成本 SO101 机械臂采集的真实操作观测数据，以及基于仿真器的 LIBERO 基准，后者包含超过 6 万个操作帧和超过 12 万个相机特定场景图。实验表明，当前模型虽能预测合理关系，但在精确的深度感知和视角依赖空间结构上表现不佳。

## 核心内容
### 方法
- **场景图表示**：EmbodimentSemantic 将场景建模为有向对象-关系-对象三元组，每个三元组使用固定关系集（如支撑、包含、顺序、遮挡、深度敏感关系）指定一对有序对象间的空间关系。
- **数据采集**：真实世界数据使用低成本 SO101 机械臂采集，包含实际操作观测和生成的场景图，用于研究实际机器人环境中的空间定位。
- **仿真基准**：引入基于 MuJoCo 仿真器的 LIBERO 基准，包含超过 6 万个操作帧和超过 12 万个相机特定场景图，覆盖配对第三人称和腕部视角。真实关系通过 MuJoCo 几何、世界坐标、相机投影和可见性约束自动推导。

### 实验设置
- **模型测试**：在开源和商业视觉-语言模型上测试，评估对象绑定、关系预测和空间一致性。
- **下游控制**：将场景图注入现有 VLA 策略提示，测试其对下游控制性能的提升。

### 关键结果
- 当前模型能预测合理关系，但在精确的深度感知和视角依赖空间结构上表现不佳。
- EmbodimentSemantic 提供了一个统一框架，用于诊断 VLM 感知中的空间定位问题，并测试其在 VLA 操作中的实用性。

## Overview
Spatial grounding remains a key limitation of vision-language-action (VLA) systems for robotic manipulation. While current models can recognize objects and follow language instructions, they often lack an explicit representation of how objects are arranged in space, including support, containment, ordering, occlusion, and depth-sensitive relations. We introduce EmbodimentSemantic, a spatial scene-graph dataset and benchmark for evaluating relational grounding in embodied manipulation. EmbodimentSemantic represents scenes as directed object-relation-object triplets, where each triplet specifies a spatial relation between an ordered pair of objects using a fixed set of relations. This representation enables direct evaluation of object binding, relation prediction, and spatial consistency. The dataset includes real-world manipulation observations collected with the low-cost SO101 robot arm, together with generated scene graphs for studying spatial grounding in practical robotic settings. To provide controlled validation, we also introduce a simulator-grounded LIBERO benchmark with over 60K manipulation frames and more than 120K camera-specific scene graphs across paired third-person and wrist views, where ground-truth relations are derived automatically from MuJoCo geometry, world coordinates, camera projections, and visibility constraints. We further test whether scene graphs improve downstream control by injecting them into existing VLA policy prompts. Experiments across open-source and commercial VLMs show that current models often predict plausible relations but struggle with exact depth-aware and viewpoint-dependent spatial structure. EmbodimentSemantic provides a unified framework for diagnosing spatial grounding in VLM perception and testing its utility for VLA manipulation.

## 参考
- http://arxiv.org/abs/2607.00020v1

## 개요
EmbodimentSemantic은 로봇 조작에서 시각-언어-행동 시스템의 공간 위치 파악 능력 부족 문제를 해결하는 것을 목표로 한다. 이 작업은 장면을 방향성 객체-관계-객체 삼중항으로 표현하고, 고정된 관계 집합을 사용하여 객체 간의 공간 관계를 설명함으로써 객체 바인딩, 관계 예측 및 공간 일관성을 직접 평가한다. 데이터셋에는 저비용 SO101 로봇 팔로 수집한 실제 조작 관측 데이터와 시뮬레이터 기반 LIBERO 벤치마크가 포함되며,后者는 6만 개 이상의 조작 프레임과 12만 개 이상의 카메라별 장면 그래프를 포함한다. 실험 결과, 현재 모델은 합리적인 관계를 예측할 수 있지만 정밀한 깊이 인식 및 시점 의존적 공간 구조에서는 성능이 낮은 것으로 나타났다.

## 핵심 내용
### 방법
- **장면 그래프 표현**: EmbodimentSemantic은 장면을 방향성 객체-관계-객체 삼중항으로 모델링하며, 각 삼중항은 고정된 관계 집합(예: 지지, 포함, 순서, 가림, 깊이 민감 관계)을 사용하여 한 쌍의 순서 있는 객체 간의 공간 관계를 지정한다.
- **데이터 수집**: 실제 세계 데이터는 저비용 SO101 로봇 팔로 수집되며, 실제 조작 관측 및 생성된 장면 그래프를 포함하여 실제 로봇 환경에서의 공간 위치 파악을 연구한다.
- **시뮬레이션 벤치마크**: MuJoCo 시뮬레이터 기반 LIBERO 벤치마크를 도입하며, 6만 개 이상의 조작 프레임과 12만 개 이상의 카메라별 장면 그래프를 포함하고, 쌍을 이루는 3인칭 및 손목 시점을 다룬다. 실제 관계는 MuJoCo 기하학, 세계 좌표, 카메라 투영 및 가시성 제약을 통해 자동으로 도출된다.

### 실험 설정
- **모델 테스트**: 오픈소스 및 상용 시각-언어 모델에서 테스트하여 객체 바인딩, 관계 예측 및 공간 일관성을 평가한다.
- **하위 제어**: 장면 그래프를 기존 VLA 정책 프롬프트에 주입하여 하위 제어 성능 향상에 미치는 영향을 테스트한다.

### 주요 결과
- 현재 모델은 합리적인 관계를 예측할 수 있지만 정밀한 깊이 인식 및 시점 의존적 공간 구조에서는 성능이 낮다.
- EmbodimentSemantic은 VLM 인식에서 공간 위치 파악 문제를 진단하고 VLA 조작에서의 유용성을 테스트하기 위한 통합 프레임워크를 제공한다.
