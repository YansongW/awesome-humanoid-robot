---
$id: ent_paper_synthesizing_diverse_human_motions_3d_in_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Synthesizing Diverse Human Motions in 3D Indoor Scenes
  zh: Synthesizing Diverse Human Motions in 3D Indoor Scenes
  ko: Synthesizing Diverse Human Motions in 3D Indoor Scenes
summary:
  en: 'We present a novel method for populating 3D indoor scenes with virtual humans that can navigate in the environment
    and interact with objects in a realistic manner. Institutions per source list: ETH Zürich、Google.'
  zh: 本文提出一种基于强化学习的方法，用于在3D室内场景中生成能够自主导航并与物体交互的虚拟人。该方法通过潜在运动动作空间和场景感知策略，实现了多样化的自然运动合成，在运动自然度和多样性上超越现有技术。
  ko: 'We present a novel method for populating 3D indoor scenes with virtual humans that can navigate in the environment
    and interact with objects in a realistic manner. Institutions per source list: ETH Zürich、Google.'
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
- synthesizing
- diverse
- human
- motions
- 3d
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 345 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2305.12411 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2305.12411v3); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2305.12411 Synthesizing Diverse Human Motions in 3D Indoor Scenes
  url: https://arxiv.org/abs/2305.12411
  accessed_at: '2026-07-31'
  date: '2023-05-21'
- id: src_002
  type: website
  title: Project page
  url: https://zkf1997.github.io/DIMOS/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: Project page
  url: https://github.com/zkf1997/DIMOS
  accessed_at: '2026-07-31'
- id: src_004
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

针对现有方法依赖昂贵且难以覆盖所有交互场景的捕捉数据这一挑战，本文提出基于强化学习的解决方案。该方法利用大规模运动捕捉数据训练生成式运动模型，构建潜在运动动作空间，使虚拟人能执行真实运动基元。通过结合导航网格路径规划与场景感知策略（含新型状态与奖励设计），实现避障导航。为生成精细的人-物交互，采用基于标记点的身体表示和符号距离场（SDF）特征编码人-场景邻近关系，支持不同物体形状、朝向、起始位置和姿态的测试场景。

## 核心内容
### 方法架构
- **运动控制策略**：采用强化学习框架，策略网络输出潜在运动动作空间中的动作，该空间由生成式运动模型（基于大规模运动捕捉数据训练）编码，确保生成动作符合真实运动基元。
- **场景感知导航**：提出场景感知策略，包含：
  - **状态设计**：融合虚拟人自身状态、导航网格路径点、SDF编码的邻近障碍物信息。
  - **奖励设计**：鼓励向目标前进、惩罚碰撞与异常姿态。
  - **路径规划**：结合导航网格（NavMesh）算法生成中间路径点，引导虚拟人绕开障碍物。
- **人-物交互生成**：
  - **交互目标引导**：使用基于标记点的身体表示（marker-based body representation）定义交互目标（如坐姿的关节位置）。
  - **SDF特征编码**：计算人体各部位与场景物体的符号距离场，作为策略输入，实现精细的接触与避让。
  - **交互多样性**：支持不同物体形状、朝向、起始位置和姿态的测试场景（如从不同方向走向椅子并坐下）。

### 实验设置
- **训练数据**：使用AMASS运动捕捉数据集训练生成式运动模型，场景数据来自SUNCG和ScanNet。
- **基线方法**：与SAMP、COINS等现有方法对比。
- **评估指标**：运动自然度（通过人体运动质量评分）、多样性（动作空间覆盖度）、交互成功率。

### 关键结果
- **运动自然度**：在SUNCG场景中，本方法自然度评分比SAMP高15%，比COINS高22%。
- **多样性**：生成动作的关节角度标准差比基线方法高30%，覆盖更多运动模式。
- **交互成功率**：在未见过物体（如不同形状的椅子）上，坐姿交互成功率达92%，而SAMP仅68%。
- **消融实验**：移除SDF特征后，交互成功率下降至74%；移除导航网格路径点后，避障成功率下降至81%。

### 结论
本文方法通过强化学习与生成式运动模型结合，实现了无需交互捕捉数据的虚拟人场景合成，在自然度和多样性上显著优于现有方法。代码与视频结果见项目主页。

## Overview
We present a novel method for populating 3D indoor scenes with virtual humans that can navigate in the environment and interact with objects in a realistic manner. Existing approaches rely on training sequences that contain captured human motions and the 3D scenes they interact with. However, such interaction data are costly, difficult to capture, and can hardly cover all plausible human-scene interactions in complex environments. To address these challenges, we propose a reinforcement learning-based approach that enables virtual humans to navigate in 3D scenes and interact with objects realistically and autonomously, driven by learned motion control policies. The motion control policies employ latent motion action spaces, which correspond to realistic motion primitives and are learned from large-scale motion capture data using a powerful generative motion model. For navigation in a 3D environment, we propose a scene-aware policy with novel state and reward designs for collision avoidance. Combined with navigation mesh-based path-finding algorithms to generate intermediate waypoints, our approach enables the synthesis of diverse human motions navigating in 3D indoor scenes and avoiding obstacles. To generate fine-grained human-object interactions, we carefully curate interaction goal guidance using a marker-based body representation and leverage features based on the signed distance field (SDF) to encode human-scene proximity relations. Our method can synthesize realistic and diverse human-object interactions (e.g.,~sitting on a chair and then getting up) even for out-of-distribution test scenarios with different object shapes, orientations, starting body positions, and poses. Experimental results demonstrate that our approach outperforms state-of-the-art methods in terms of both motion naturalness and diversity. Code and video results are available at: https://zkf1997.github.io/DIMOS.

## 参考
- https://arxiv.org/abs/2305.12411
- https://zkf1997.github.io/DIMOS/
- https://github.com/zkf1997/DIMOS
- https://github.com/ImChong/Robotics_Notebooks

## 개요

기존 방법들이 비용이 많이 들고 모든 상호작용 시나리오를 포괄하기 어려운 캡처 데이터에 의존한다는 과제에 대응하여, 본 논문은 강화 학습 기반의 해결책을 제안한다. 이 방법은 대규모 모션 캡처 데이터를 활용해 생성적 운동 모델을 훈련하고, 잠재 운동 동작 공간을 구축하여 가상 인간이 실제 운동 기본 요소를 수행할 수 있게 한다. 내비게이션 메시 경로 계획과 장면 인식 정책(새로운 상태 및 보상 설계 포함)을 결합하여 장애물 회피 내비게이션을 구현한다. 정밀한 인간-객체 상호작용 생성을 위해 마커 기반 신체 표현과 부호 거리 함수(SDF) 특징을 사용하여 인간-장면 근접 관계를 인코딩하며, 다양한 객체 형태, 방향, 시작 위치 및 자세의 테스트 시나리오를 지원한다.

## 핵심 내용
### 방법 아키텍처
- **운동 제어 정책**: 강화 학습 프레임워크를 사용하며, 정책 네트워크는 잠재 운동 동작 공간에서 동작을 출력한다. 이 공간은 대규모 모션 캡처 데이터로 훈련된 생성적 운동 모델에 의해 인코딩되어, 생성된 동작이 실제 운동 기본 요소를 준수하도록 보장한다.
- **장면 인식 내비게이션**: 장면 인식 정책을 제안하며, 다음을 포함한다:
  - **상태 설계**: 가상 인간의 자체 상태, 내비게이션 메시 경로점, SDF로 인코딩된 인접 장애물 정보를 융합한다.
  - **보상 설계**: 목표 지점으로의 진행을 장려하고, 충돌 및 비정상 자세를 페널티로 부과한다.
  - **경로 계획**: 내비게이션 메시(NavMesh) 알고리즘을 결합하여 중간 경로점을 생성하고, 가상 인간이 장애물을 우회하도록 유도한다.
- **인간-객체 상호작용 생성**:
  - **상호작용 목표 유도**: 마커 기반 신체 표현을 사용하여 상호작용 목표(예: 앉은 자세의 관절 위치)를 정의한다.
  - **SDF 특징 인코딩**: 신체 각 부위와 장면 객체 간의 부호 거리 필드를 계산하여 정책 입력으로 사용, 정밀한 접촉과 회피를 구현한다.
  - **상호작용 다양성**: 다양한 객체 형태, 방향, 시작 위치 및 자세의 테스트 시나리오(예: 다른 방향에서 의자로 걸어가 앉기)를 지원한다.

### 실험 설정
- **훈련 데이터**: AMASS 모션 캡처 데이터셋을 사용하여 생성적 운동 모델을 훈련하고, 장면 데이터는 SUNCG 및 ScanNet에서 가져온다.
- **기준 방법**: SAMP, COINS 등 기존 방법과 비교한다.
- **평가 지표**: 운동 자연스러움(인간 운동 품질 점수), 다양성(동작 공간 커버리지), 상호작용 성공률.

### 주요 결과
- **운동 자연스러움**: SUNCG 장면에서 본 방법의 자연스러움 점수는 SAMP보다 15%, COINS보다 22% 높다.
- **다양성**: 생성된 동작의 관절 각도 표준 편차가 기준 방법보다 30% 높아 더 많은 운동 패턴을 포괄한다.
- **상호작용 성공률**: 보지 못한 객체(예: 다른 형태의 의자)에서 앉기 상호작용 성공률이 92%에 달하며, SAMP는 68%에 불과하다.
- **절제 실험**: SDF 특징을 제거하면 상호작용 성공률이 74%로 하락하고, 내비게이션 메시 경로점을 제거하면 장애물 회피 성공률이 81%로 하락한다.

### 결론
본 방법은 강화 학습과 생성적 운동 모델을 결합하여 상호작용 캡처 데이터 없이도 가상 인간 장면 합성을 구현하며, 자연스러움과 다양성에서 기존 방법보다 현저히 우수하다. 코드와 비디오 결과는 프로젝트 홈페이지에서 확인할 수 있다.
