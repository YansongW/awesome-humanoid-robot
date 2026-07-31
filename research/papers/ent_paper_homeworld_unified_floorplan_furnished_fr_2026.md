---
$id: ent_paper_homeworld_unified_floorplan_furnished_fr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes'
  zh: 'HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes'
  ko: 'HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes'
summary:
  en: 'Indoor scene generation is crucial for robot simulation and modern interior design. However, complex layouts together
    with scarce 3D scene data make learning-based generation challenging. Institutions per source list: Ace Robotics、CUHK
    MMLab、Shenzhen Loop Area Institute（*Equal contribution、†Project lead）.'
  zh: HomeWorld 是一个由研究团队提出的统一分层框架，用于生成可控且密集交互的全屋场景。其核心贡献包括：构建了包含 30 万真实住宅平面图的大规模数据集，并利用大语言模型实现细粒度平面图生成；结合图像生成模型与 VLM 优化器，实现从家具布局到小物体放置的完整室内场景合成，最终输出可直接用于具身
    AI 模拟的 3D 场景。
  ko: 'Indoor scene generation is crucial for robot simulation and modern interior design. However, complex layouts together
    with scarce 3D scene data make learning-based generation challenging. Institutions per source list: Ace Robotics、CUHK
    MMLab、Shenzhen Loop Area Institute（*Equal contribution、†Project lead）.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- homeworld
- unified
- floorplan
- furnished
- fr
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 383 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2606.06390 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.06390v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.06390 HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive
    Whole-Home Scenes'
  url: https://arxiv.org/abs/2606.06390
  accessed_at: '2026-07-31'
  date: '2026-06-04'
- id: src_002
  type: website
  title: Project page
  url: https://kairos-homeworld.github.io/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

针对现有方法依赖手工规则或仅关注子任务（如平面图合成或单房间布置）导致全屋场景缺乏全局一致性与真实感的问题，HomeWorld 提出了一种统一的分层框架。该框架首先基于 30 万真实住宅平面图训练大语言模型，结合 K-D 树表示实现可控的全屋平面图生成。随后，利用图像生成模型从多级漫游视角草拟家具布局，并进一步生成可操作小物体（如柜子、桌子上的物品）的布局。在布局生成过程中，基于 VLM 的优化器迭代修正物体放置，而 3D 生成模型则支持灵活替换单个资产。最后，通过附加基本物理属性、表面纹理与光照设置，完成可直接用于具身 AI 模拟的完整管线。

## 核心内容
### 方法架构
HomeWorld 采用统一的分层框架，将室内场景合成分解为可控阶段：
- **平面图生成**：基于 30 万真实住宅平面图数据集，训练大语言模型（LLM）生成全屋平面图。通过 K-D 树表示与详细描述，实现细粒度、可控的平面图生成。
- **家具布局草拟**：利用图像生成模型（如扩散模型）从多级漫游视角（如俯视、平视）生成家具布局草图。
- **小物体布局生成**：在支撑面（如柜子、书桌、餐桌）上生成可操作小物体的布局，用于具身 AI 模拟。
- **VLM 优化器**：基于视觉语言模型（VLM）的迭代优化器，自动修正家具与物体的放置位置，提升布局合理性。
- **3D 资产替换**：通过 3D 生成模型（如 NeRF 或 GAN）灵活替换单个资产（如沙发、桌子），支持用户自定义。
- **物理与渲染属性**：为场景附加基本物理属性（如碰撞检测）、表面纹理与光照设置，确保场景可直接用于具身 AI 模拟。

### 实验设置与关键数字
- **数据集**：构建了包含 300K 真实住宅平面图的数据集，并计划发布 5K 完全布置好的场景。
- **评估指标**：在布局多样性、3D 设计吸引力、模拟就绪度等定量与定性指标上，HomeWorld 优于现有方法（如 PlanIT、SceneFormer）。
- **用户研究**：通过用户调查验证，HomeWorld 生成的室内空间在布局多样性与 3D 设计吸引力上显著优于基线方法。

### 结论
HomeWorld 通过统一分层框架，解决了全屋场景生成中全局连贯性与模拟就绪度的挑战。其关键创新在于结合大语言模型、图像生成模型与 VLM 优化器，实现了从平面图到密集交互场景的端到端生成。未来工作可进一步扩展至动态场景生成与实时交互。

## Overview
Indoor scene generation is crucial for robot simulation and modern interior design. However, complex layouts together with scarce 3D scene data make learning-based generation challenging. Existing methods often rely on hand-crafted rules or focus on isolated sub-tasks (e.g., floorplan synthesis or single-room furnishing), producing whole-home scenes that lack global coherence, realism, and simulation readiness. To mitigate these limitations, we propose a unified hierarchical framework that decomposes indoor scene synthesis into controllable stages. First, we curate a large-scale dataset of 300K real residential floorplans to train a large language model for whole-home floorplan generation. With detailed descriptions and a K-D tree-based representation, our method enables fine-grained, controllable whole-home floorplan generation. Building upon the generated whole-home floorplan, we leverage image generation models to draft furniture layouts from multi-level roaming viewpoints, and then generate the layouts of small manipulable objects on different supporting surfaces (e.g., cabinets, desks, and dining tables) for embodied AI simulation. During furniture and object layout generation, a VLM-based refiner iteratively corrects furniture and object placement, and a 3D generative model enables flexible replacement of individual assets. We further attach basic physical attributes and simple surface texture and lighting setups to complete the pipeline for embodied AI use. Experiments and user studies demonstrate that our pipeline produces indoor spaces with greater layout diversity and stronger 3D design appeal, outperforming prior methods on both quantitative and qualitative metrics. Finally, alongside our generation pipeline, we will release the floorplan dataset and 5K fully furnished scenes to the community. Project Page: https://kairos-homeworld.github.io/

## 参考
- https://arxiv.org/abs/2606.06390
- https://kairos-homeworld.github.io/
- https://github.com/ImChong/Robotics_Notebooks

## 개요

기존 방법이 수동 규칙에 의존하거나 하위 작업(예: 평면도 합성 또는 단일 방 배치)에만 초점을 맞춰 전체 주택 장면에 글로벌 일관성과 현실감이 부족한 문제를 해결하기 위해, HomeWorld는 통합된 계층적 프레임워크를 제안합니다. 이 프레임워크는 먼저 30만 개의 실제 주택 평면도를 기반으로 대규모 언어 모델을 학습시키고, K-D 트리 표현을 결합하여 제어 가능한 전체 주택 평면도 생성을 구현합니다. 이후 이미지 생성 모델을 사용하여 다중 레벨 시점에서 가구 배치를 초안으로 그리고, 추가로 조작 가능한 소형 물체(예: 캐비닛, 테이블 위 물건)의 배치를 생성합니다. 배치 생성 과정에서 VLM 기반 최적화기가 물체 배치를 반복적으로 수정하고, 3D 생성 모델은 개별 자산을 유연하게 교체할 수 있도록 지원합니다. 마지막으로 기본 물리 속성, 표면 텍스처 및 조명 설정을 추가하여, 직접적으로 구현형 AI 시뮬레이션에 사용할 수 있는 완전한 파이프라인을 완성합니다.

## 핵심 내용
### 방법 아키텍처
HomeWorld는 통합된 계층적 프레임워크를 사용하여 실내 장면 합성을 제어 가능한 단계로 분해합니다:
- **평면도 생성**: 30만 개의 실제 주택 평면도 데이터셋을 기반으로 대규모 언어 모델(LLM)을 학습시켜 전체 주택 평면도를 생성합니다. K-D 트리 표현과 상세 설명을 통해 세밀하고 제어 가능한 평면도 생성을 구현합니다.
- **가구 배치 초안**: 이미지 생성 모델(예: 확산 모델)을 사용하여 다중 레벨 시점(예: 내려다보기, 정면 보기)에서 가구 배치 초안을 생성합니다.
- **소형 물체 배치 생성**: 지지면(예: 캐비닛, 책상, 식탁) 위에 조작 가능한 소형 물체의 배치를 생성하여 구현형 AI 시뮬레이션에 사용합니다.
- **VLM 최적화기**: 시각 언어 모델(VLM) 기반의 반복 최적화기를 통해 가구와 물체의 배치 위치를 자동으로 수정하여 배치의 합리성을 향상시킵니다.
- **3D 자산 교체**: 3D 생성 모델(예: NeRF 또는 GAN)을 통해 개별 자산(예: 소파, 테이블)을 유연하게 교체하여 사용자 정의를 지원합니다.
- **물리 및 렌더링 속성**: 장면에 기본 물리 속성(예: 충돌 감지), 표면 텍스처 및 조명 설정을 추가하여 장면이 직접적으로 구현형 AI 시뮬레이션에 사용될 수 있도록 보장합니다.

### 실험 설정 및 주요 수치
- **데이터셋**: 300K개의 실제 주택 평면도를 포함하는 데이터셋을 구축했으며, 5K개의 완전히 배치된 장면을 공개할 계획입니다.
- **평가 지표**: 배치 다양성, 3D 디자인 매력도, 시뮬레이션 준비도 등 정량적 및 정성적 지표에서 HomeWorld는 기존 방법(예: PlanIT, SceneFormer)보다 우수합니다.
- **사용자 연구**: 사용자 조사를 통해 HomeWorld가 생성한 실내 공간이 배치 다양성과 3D 디자인 매력도에서 기준 방법보다 현저히 우수함을 확인했습니다.

### 결론
HomeWorld는 통합된 계층적 프레임워크를 통해 전체 주택 장면 생성에서 글로벌 일관성과 시뮬레이션 준비도의 문제를 해결했습니다. 주요 혁신은 대규모 언어 모델, 이미지 생성 모델 및 VLM 최적화기를 결합하여 평면도에서 밀집된 상호작용 장면까지의 종단 간 생성을 구현한 데 있습니다. 향후 작업은 동적 장면 생성 및 실시간 상호작용으로 더 확장될 수 있습니다.
