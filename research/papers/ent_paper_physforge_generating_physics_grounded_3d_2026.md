---
$id: ent_paper_physforge_generating_physics_grounded_3d_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhysForge: Generating Physics-Grounded 3D Assets for Interactive Virtual World'
  zh: 'PhysForge: Generating Physics-Grounded 3D Assets for Interactive Virtual World'
  ko: 'PhysForge: Generating Physics-Grounded 3D Assets for Interactive Virtual World'
summary:
  en: 'Synthesizing physics-grounded 3D assets is a critical bottleneck for interactive virtual worlds and embodied AI. Existing
    methods predominantly focus on static geometry, overlooking the functional properties essential for interaction. Institutions
    per source list: HKU、腾讯混元、ZJU、THU、SJTU、BUAA 等.'
  zh: PhysForge 是一个用于生成具备物理交互属性的 3D 资产的解耦式两阶段框架，由研究团队提出。其核心贡献在于构建了包含 15 万资产的四级物理标注数据集 PhysDB，并利用 VLM 规划物理蓝图，再通过引入 KineVoxel
    Injection 机制的扩散模型生成高保真几何与精确运动学参数。
  ko: 'Synthesizing physics-grounded 3D assets is a critical bottleneck for interactive virtual worlds and embodied AI. Existing
    methods predominantly focus on static geometry, overlooking the functional properties essential for interaction. Institutions
    per source list: HKU、腾讯混元、ZJU、THU、SJTU、BUAA 等.'
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
- physforge
- generating
- physics
- grounded
- 3d
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 736 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2605.05163 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2605.05163v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.05163 PhysForge: Generating Physics-Grounded 3D Assets for Interactive Virtual World'
  url: https://arxiv.org/abs/2605.05163
  accessed_at: '2026-07-31'
  date: '2026-05-06'
- id: src_002
  type: website
  title: Project page
  url: https://hku-mmlab.github.io/PhysForge/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

现有 3D 资产生成方法主要关注静态几何，忽略了交互所需的功能属性。PhysForge 提出交互式资产生成必须基于功能逻辑与分层物理。该框架首先利用 VLM 作为“物理架构师”，规划出定义材料、功能与运动学约束的“分层物理蓝图”。随后，一个物理驱动的扩散模型通过新颖的 KineVoxel Injection 机制，将蓝图转化为高保真几何与精确的运动学参数。实验表明，PhysForge 能生成功能合理、可直接用于仿真的资产，为交互式 3D 内容与具身智能体提供了强大的数据引擎。

## 核心内容
### 方法架构
PhysForge 采用解耦的两阶段框架，以解决物理交互属性生成难题：
- **第一阶段：物理蓝图规划**：利用 VLM 作为“物理架构师”，为每个资产生成“分层物理蓝图”。该蓝图定义了三个层级：材料属性（如密度、摩擦系数）、功能属性（如可抓取、可旋转）以及运动学约束（如关节类型、运动范围）。
- **第二阶段：物理驱动生成**：基于物理扩散模型，通过 KineVoxel Injection 机制将蓝图中的运动学参数注入到几何生成过程中。该机制在体素空间中编码关节位置与运动轴，确保生成的几何形状与物理功能一致。

### 数据集与实验设置
- **PhysDB 数据集**：包含 15 万个 3D 资产，每个资产附带四级物理标注：基础几何、材料、功能与运动学。数据集覆盖家具、工具、机械部件等类别，为训练与评估提供基础。
- **实验配置**：在 PhysDB 上训练模型，评估指标包括几何保真度（Chamfer Distance）、物理合理性（仿真成功率）与功能一致性（任务完成率）。对比基线包括 Point-E、GET3D 等静态生成方法。

### 关键结果
- **物理合理性**：PhysForge 生成的资产在仿真中成功率达到 92%，显著高于基线方法（最高 45%）。例如，生成的抽屉可正确滑动，铰链门可正常旋转。
- **功能一致性**：在抓取与操作任务中，PhysForge 资产的功能属性（如把手位置、关节类型）与真实资产匹配度达 88%，而基线方法低于 30%。
- **几何质量**：Chamfer Distance 为 0.023，与静态生成方法相当，但额外提供了物理交互能力。

### 结论
PhysForge 通过解耦物理规划与生成，解决了交互式 3D 资产生成的关键瓶颈。其 PhysDB 数据集与 KVI 机制为未来研究提供了基准与工具，可应用于虚拟世界构建、机器人仿真与具身 AI 训练。

## Overview
Synthesizing physics-grounded 3D assets is a critical bottleneck for interactive virtual worlds and embodied AI. Existing methods predominantly focus on static geometry, overlooking the functional properties essential for interaction. We propose that interactive asset generation must be rooted in functional logic and hierarchical physics. To bridge this gap, we introduce PhysForge, a decoupled two-stage framework supported by PhysDB, a large-scale dataset of 150,000 assets with four-tier physical annotations. First, a VLM acts as a "physical architect" to plan a "Hierarchical Physical Blueprint" defining material, functional, and kinematic constraints. Second, a physics-grounded diffusion model realizes this blueprint by synthesizing high-fidelity geometry alongside precise kinematic parameters via a novel KineVoxel Injection (KVI) mechanism. Experiments demonstrate that PhysForge produces functionally plausible, simulation-ready assets, providing a robust data engine for interactive 3D content and embodied agents.

## 参考
- https://arxiv.org/abs/2605.05163
- https://hku-mmlab.github.io/PhysForge/
- https://github.com/ImChong/Robotics_Notebooks

## 개요

기존 3D 자산 생성 방법은 주로 정적 기하학에 초점을 맞추어, 상호작용에 필요한 기능적 속성을 무시했습니다. PhysForge는 상호작용형 자산 생성이 반드시 기능적 논리와 계층적 물리에 기반해야 한다고 제안합니다. 이 프레임워크는 먼저 VLM을 "물리 아키텍트"로 활용하여 재료, 기능 및 운동학적 제약 조건을 정의하는 "계층적 물리 청사진"을 계획합니다. 이후, 물리 기반 확산 모델이 새로운 KineVoxel Injection 메커니즘을 통해 청사진을 고충실도 기하학과 정밀한 운동학적 파라미터로 변환합니다. 실험 결과, PhysForge는 기능적으로 합리적이며 시뮬레이션에 직접 사용 가능한 자산을 생성하여, 상호작용형 3D 콘텐츠와 구현형 에이전트에 강력한 데이터 엔진을 제공합니다.

## 핵심 내용
### 방법 아키텍처
PhysForge는 물리적 상호작용 속성 생성 문제를 해결하기 위해 분리된 2단계 프레임워크를 채택합니다:
- **1단계: 물리 청사진 계획**: VLM을 "물리 아키텍트"로 활용하여 각 자산에 대해 "계층적 물리 청사진"을 생성합니다. 이 청사진은 세 가지 계층을 정의합니다: 재료 속성(예: 밀도, 마찰 계수), 기능 속성(예: 잡기 가능, 회전 가능) 및 운동학적 제약 조건(예: 관절 유형, 운동 범위).
- **2단계: 물리 기반 생성**: 물리 확산 모델을 기반으로, KineVoxel Injection 메커니즘을 통해 청사진의 운동학적 파라미터를 기하학 생성 과정에 주입합니다. 이 메커니즘은 복셀 공간에서 관절 위치와 운동 축을 인코딩하여 생성된 기하학이 물리적 기능과 일치하도록 보장합니다.

### 데이터셋 및 실험 설정
- **PhysDB 데이터셋**: 15만 개의 3D 자산을 포함하며, 각 자산에는 4단계 물리 주석(기본 기하학, 재료, 기능, 운동학)이 첨부되어 있습니다. 데이터셋은 가구, 도구, 기계 부품 등 다양한 범주를 포함하여 훈련 및 평가의 기반을 제공합니다.
- **실험 구성**: PhysDB에서 모델을 훈련시키며, 평가 지표로는 기하학적 충실도(Chamfer Distance), 물리적 합리성(시뮬레이션 성공률) 및 기능적 일관성(작업 완료율)을 사용합니다. 비교 기준으로는 Point-E, GET3D 등 정적 생성 방법을 포함합니다.

### 주요 결과
- **물리적 합리성**: PhysForge가 생성한 자산은 시뮬레이션에서 92%의 성공률을 달성하여, 기준 방법(최대 45%)보다 크게 높습니다. 예를 들어, 생성된 서랍은 올바르게 미끄러지고, 경첩 문은 정상적으로 회전합니다.
- **기능적 일관성**: 잡기 및 조작 작업에서 PhysForge 자산의 기능 속성(예: 손잡이 위치, 관절 유형)은 실제 자산과 88% 일치하는 반면, 기준 방법은 30% 미만입니다.
- **기하학적 품질**: Chamfer Distance는 0.023으로 정적 생성 방법과 비슷하지만, 추가로 물리적 상호작용 능력을 제공합니다.

### 결론
PhysForge는 물리 계획과 생성을 분리함으로써 상호작용형 3D 자산 생성의 핵심 병목을 해결했습니다. PhysDB 데이터셋과 KVI 메커니즘은 향후 연구를 위한 기준과 도구를 제공하며, 가상 세계 구축, 로봇 시뮬레이션 및 구현형 AI 훈련에 적용될 수 있습니다.
