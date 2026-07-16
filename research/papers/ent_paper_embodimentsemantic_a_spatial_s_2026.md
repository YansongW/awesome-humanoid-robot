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
  zh: 'arXiv:2607.00020v1 Announce Type: new Abstract: Spatial grounding remains a key limitation of vision-language-action
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00020v1.
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
Spatial grounding remains a key limitation of vision-language-action (VLA) systems for robotic manipulation. While current models can recognize objects and follow language instructions, they often lack an explicit representation of how objects are arranged in space, including support, containment, ordering, occlusion, and depth-sensitive relations. We introduce EmbodimentSemantic, a spatial scene-graph dataset and benchmark for evaluating relational grounding in embodied manipulation. EmbodimentSemantic represents scenes as directed object-relation-object triplets, where each triplet specifies a spatial relation between an ordered pair of objects using a fixed set of relations. This representation enables direct evaluation of object binding, relation prediction, and spatial consistency. The dataset includes real-world manipulation observations collected with the low-cost SO101 robot arm, together with generated scene graphs for studying spatial grounding in practical robotic settings. To provide controlled validation, we also introduce a simulator-grounded LIBERO benchmark with over 60K manipulation frames and more than 120K camera-specific scene graphs across paired third-person and wrist views, where ground-truth relations are derived automatically from MuJoCo geometry, world coordinates, camera projections, and visibility constraints. We further test whether scene graphs improve downstream control by injecting them into existing VLA policy prompts. Experiments across open-source and commercial VLMs show that current models often predict plausible relations but struggle with exact depth-aware and viewpoint-dependent spatial structure. EmbodimentSemantic provides a unified framework for diagnosing spatial grounding in VLM perception and testing its utility for VLA manipulation.

## 核心内容
Spatial grounding remains a key limitation of vision-language-action (VLA) systems for robotic manipulation. While current models can recognize objects and follow language instructions, they often lack an explicit representation of how objects are arranged in space, including support, containment, ordering, occlusion, and depth-sensitive relations. We introduce EmbodimentSemantic, a spatial scene-graph dataset and benchmark for evaluating relational grounding in embodied manipulation. EmbodimentSemantic represents scenes as directed object-relation-object triplets, where each triplet specifies a spatial relation between an ordered pair of objects using a fixed set of relations. This representation enables direct evaluation of object binding, relation prediction, and spatial consistency. The dataset includes real-world manipulation observations collected with the low-cost SO101 robot arm, together with generated scene graphs for studying spatial grounding in practical robotic settings. To provide controlled validation, we also introduce a simulator-grounded LIBERO benchmark with over 60K manipulation frames and more than 120K camera-specific scene graphs across paired third-person and wrist views, where ground-truth relations are derived automatically from MuJoCo geometry, world coordinates, camera projections, and visibility constraints. We further test whether scene graphs improve downstream control by injecting them into existing VLA policy prompts. Experiments across open-source and commercial VLMs show that current models often predict plausible relations but struggle with exact depth-aware and viewpoint-dependent spatial structure. EmbodimentSemantic provides a unified framework for diagnosing spatial grounding in VLM perception and testing its utility for VLA manipulation.

## 参考
- http://arxiv.org/abs/2607.00020v1

## Overview
Spatial grounding remains a key limitation of vision-language-action (VLA) systems for robotic manipulation. While current models can recognize objects and follow language instructions, they often lack an explicit representation of how objects are arranged in space, including support, containment, ordering, occlusion, and depth-sensitive relations. We introduce EmbodimentSemantic, a spatial scene-graph dataset and benchmark for evaluating relational grounding in embodied manipulation. EmbodimentSemantic represents scenes as directed object-relation-object triplets, where each triplet specifies a spatial relation between an ordered pair of objects using a fixed set of relations. This representation enables direct evaluation of object binding, relation prediction, and spatial consistency. The dataset includes real-world manipulation observations collected with the low-cost SO101 robot arm, together with generated scene graphs for studying spatial grounding in practical robotic settings. To provide controlled validation, we also introduce a simulator-grounded LIBERO benchmark with over 60K manipulation frames and more than 120K camera-specific scene graphs across paired third-person and wrist views, where ground-truth relations are derived automatically from MuJoCo geometry, world coordinates, camera projections, and visibility constraints. We further test whether scene graphs improve downstream control by injecting them into existing VLA policy prompts. Experiments across open-source and commercial VLMs show that current models often predict plausible relations but struggle with exact depth-aware and viewpoint-dependent spatial structure. EmbodimentSemantic provides a unified framework for diagnosing spatial grounding in VLM perception and testing its utility for VLA manipulation.

## Content
Spatial grounding remains a key limitation of vision-language-action (VLA) systems for robotic manipulation. While current models can recognize objects and follow language instructions, they often lack an explicit representation of how objects are arranged in space, including support, containment, ordering, occlusion, and depth-sensitive relations. We introduce EmbodimentSemantic, a spatial scene-graph dataset and benchmark for evaluating relational grounding in embodied manipulation. EmbodimentSemantic represents scenes as directed object-relation-object triplets, where each triplet specifies a spatial relation between an ordered pair of objects using a fixed set of relations. This representation enables direct evaluation of object binding, relation prediction, and spatial consistency. The dataset includes real-world manipulation observations collected with the low-cost SO101 robot arm, together with generated scene graphs for studying spatial grounding in practical robotic settings. To provide controlled validation, we also introduce a simulator-grounded LIBERO benchmark with over 60K manipulation frames and more than 120K camera-specific scene graphs across paired third-person and wrist views, where ground-truth relations are derived automatically from MuJoCo geometry, world coordinates, camera projections, and visibility constraints. We further test whether scene graphs improve downstream control by injecting them into existing VLA policy prompts. Experiments across open-source and commercial VLMs show that current models often predict plausible relations but struggle with exact depth-aware and viewpoint-dependent spatial structure. EmbodimentSemantic provides a unified framework for diagnosing spatial grounding in VLM perception and testing its utility for VLA manipulation.

## 개요
공간적 접지(Spatial grounding)는 로봇 조작을 위한 시각-언어-행동(VLA) 시스템의 핵심적인 한계로 남아 있습니다. 현재 모델은 객체를 인식하고 언어 명령을 따를 수 있지만, 지지, 포함, 순서, 가림, 깊이 민감 관계 등 객체가 공간에 어떻게 배열되어 있는지에 대한 명시적 표현이 부족한 경우가 많습니다. 우리는 구현된 조작에서 관계적 접지를 평가하기 위한 공간 장면 그래프 데이터셋이자 벤치마크인 EmbodimentSemantic을 소개합니다. EmbodimentSemantic은 장면을 방향성 있는 객체-관계-객체 삼중항으로 표현하며, 각 삼중항은 고정된 관계 집합을 사용하여 순서가 있는 객체 쌍 간의 공간 관계를 지정합니다. 이 표현은 객체 결합, 관계 예측 및 공간 일관성의 직접적인 평가를 가능하게 합니다. 데이터셋에는 저비용 SO101 로봇 팔로 수집된 실제 조작 관찰 데이터와 실제 로봇 환경에서 공간 접지를 연구하기 위한 생성된 장면 그래프가 포함됩니다. 통제된 검증을 위해, 우리는 또한 60K개 이상의 조작 프레임과 120K개 이상의 카메라별 장면 그래프를 포함하는 시뮬레이터 기반 LIBERO 벤치마크를 소개합니다. 이는 쌍을 이루는 3인칭 및 손목 뷰에 걸쳐 있으며, 실제 관계는 MuJoCo 기하학, 세계 좌표, 카메라 투영 및 가시성 제약 조건에서 자동으로 파생됩니다. 또한, 기존 VLA 정책 프롬프트에 장면 그래프를 주입하여 하위 제어를 개선하는지 테스트합니다. 오픈소스 및 상용 VLM에 걸친 실험은 현재 모델이 그럴듯한 관계를 예측하는 경우가 많지만 정확한 깊이 인식 및 시점 의존적 공간 구조에 어려움을 겪는다는 것을 보여줍니다. EmbodimentSemantic은 VLM 인식에서 공간 접지를 진단하고 VLA 조작에 대한 유용성을 테스트하기 위한 통합 프레임워크를 제공합니다.

## 핵심 내용
공간적 접지(Spatial grounding)는 로봇 조작을 위한 시각-언어-행동(VLA) 시스템의 핵심적인 한계로 남아 있습니다. 현재 모델은 객체를 인식하고 언어 명령을 따를 수 있지만, 지지, 포함, 순서, 가림, 깊이 민감 관계 등 객체가 공간에 어떻게 배열되어 있는지에 대한 명시적 표현이 부족한 경우가 많습니다. 우리는 구현된 조작에서 관계적 접지를 평가하기 위한 공간 장면 그래프 데이터셋이자 벤치마크인 EmbodimentSemantic을 소개합니다. EmbodimentSemantic은 장면을 방향성 있는 객체-관계-객체 삼중항으로 표현하며, 각 삼중항은 고정된 관계 집합을 사용하여 순서가 있는 객체 쌍 간의 공간 관계를 지정합니다. 이 표현은 객체 결합, 관계 예측 및 공간 일관성의 직접적인 평가를 가능하게 합니다. 데이터셋에는 저비용 SO101 로봇 팔로 수집된 실제 조작 관찰 데이터와 실제 로봇 환경에서 공간 접지를 연구하기 위한 생성된 장면 그래프가 포함됩니다. 통제된 검증을 위해, 우리는 또한 60K개 이상의 조작 프레임과 120K개 이상의 카메라별 장면 그래프를 포함하는 시뮬레이터 기반 LIBERO 벤치마크를 소개합니다. 이는 쌍을 이루는 3인칭 및 손목 뷰에 걸쳐 있으며, 실제 관계는 MuJoCo 기하학, 세계 좌표, 카메라 투영 및 가시성 제약 조건에서 자동으로 파생됩니다. 또한, 기존 VLA 정책 프롬프트에 장면 그래프를 주입하여 하위 제어를 개선하는지 테스트합니다. 오픈소스 및 상용 VLM에 걸친 실험은 현재 모델이 그럴듯한 관계를 예측하는 경우가 많지만 정확한 깊이 인식 및 시점 의존적 공간 구조에 어려움을 겪는다는 것을 보여줍니다. EmbodimentSemantic은 VLM 인식에서 공간 접지를 진단하고 VLA 조작에 대한 유용성을 테스트하기 위한 통합 프레임워크를 제공합니다.
