---
$id: ent_operator_task_jacobian
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: operator
names:
  en: Task Jacobian
  zh: 任务 Jacobian
  ko: 작업 Jacobian
summary:
  en: The matrix that maps joint-space velocities and accelerations to the velocity/acceleration of a task coordinate in operational
    space.
  zh: 将关节空间速度和加速度映射到操作空间任务坐标速度/加速度的矩阵。
  ko: 관절 공간 속도와 가속도를 작업 공간의 작업 좌표 속도/가속도로 매핑하는 행렬이다.
domains:
- 07_ai_models_algorithms
- 00_foundations
layers:
- intelligence
- foundations
functional_roles:
- knowledge
tags:
- jacobian
- task_space
- differential_kinematics
- linear_algebra
- humanoid_control
theoretical_depth:
- formalism
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Standard linear-algebra operator in robotics. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: paper
  title: Robotics, Vision and Control
  url: https://petercorke.com/rvc/home/
  date: '2017'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_foundation_linear_algebra
  relationship: has_prerequisite
  description:
    en: The Jacobian is built from partial derivatives, a core linear-algebra concept.
    zh: Jacobian 由偏导数构成，是线性代数的核心概念。
    ko: Jacobian은 편미분으로 구성되며, 선형대수학의 핵심 개념이다.
---

## 概述
将关节空间速度和加速度映射到操作空间任务坐标速度/加速度的矩阵。

## 核心内容
### 任务 Jacobian的定义与定位
任务 Jacobian属于 **运营商** 类型。 所属领域包括：AI 模型与算法, 基础学科。 价值链层级：智能层, foundations。 将关节空间速度和加速度映射到操作空间任务坐标速度/加速度的矩阵。 英文名称为 *Task Jacobian*。 韩文名称为 *작업 Jacobian*。

### 任务 Jacobian的关键维度
理解任务 Jacobian需要从定义、边界条件、相关实体以及典型应用场景等多个维度展开，以形成系统性的认知。
该实体在人形机器人知识图谱中起到连接基础理论与工程实践的桥梁作用。

### 实践意义
在人形机器人产业化的背景下，任务 Jacobian对于技术研究、产品开发、投资决策与生态建设均具有参考价值。
准确把握其内涵与外延，有助于避免概念混淆并推动跨学科协作。

### 研究与发展方向
随着人形机器人技术不断演进，任务 Jacobian的相关理论与实践也将持续更新，需要保持跟踪与审校。

### 相关标签
- jacobian
- task_space
- differential_kinematics
- linear_algebra
- humanoid_control

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键运营商之一，任务 Jacobian在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Robotics, Vision and Control](https://petercorke.com/rvc/home/)

## Overview
A matrix that maps joint-space velocities and accelerations to task-space velocities/accelerations in operational space.

## Content
### Definition and Positioning of the Task Jacobian
The Task Jacobian belongs to the **operator** type. Its domains include AI models and algorithms, as well as foundational disciplines. Its value chain level is the intelligence layer and foundations. It is a matrix that maps joint-space velocities and accelerations to task-space velocities/accelerations in operational space. Its English name is *Task Jacobian*. Its Korean name is *작업 Jacobian*.

### Key Dimensions of the Task Jacobian
Understanding the Task Jacobian requires a multi-dimensional approach, including its definition, boundary conditions, related entities, and typical application scenarios, to form a systematic understanding. This entity serves as a bridge connecting foundational theory and engineering practice in the humanoid robot knowledge graph.

### Practical Significance
In the context of humanoid robot industrialization, the Task Jacobian holds reference value for technical research, product development, investment decisions, and ecosystem construction. Accurately grasping its connotation and extension helps avoid conceptual confusion and promotes interdisciplinary collaboration.

### Research and Development Directions
As humanoid robot technology continues to evolve, the theories and practices related to the Task Jacobian will also be continuously updated, requiring ongoing tracking and review.

### Related Tags
- jacobian
- task_space
- differential_kinematics
- linear_algebra
- humanoid_control

### Role in the Humanoid Robot System
As one of the key operators in the humanoid robot industry chain, the Task Jacobian plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, actuation, energy, structure, and verification, collectively determining overall system performance. Related research and applications are continuously advancing to further improve its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
관절 공간 속도와 가속도를 작업 공간(task space)의 작업 좌표 속도/가속도로 매핑하는 행렬입니다.

## 핵심 내용
### 작업 Jacobian의 정의와 위치
작업 Jacobian은 **연산자(operator)** 유형에 속합니다. 관련 분야로는 AI 모델 및 알고리즘, 기초 학문이 포함됩니다. 가치 사슬 계층은 지능 계층, 기초(foundations)입니다. 관절 공간 속도와 가속도를 작업 공간의 작업 좌표 속도/가속도로 매핑하는 행렬입니다. 영문 명칭은 *Task Jacobian*이며, 한글 명칭은 *작업 Jacobian*입니다.

### 작업 Jacobian의 핵심 차원
작업 Jacobian을 이해하려면 정의, 경계 조건, 관련 개체 및 대표적인 응용 시나리오 등 여러 차원에서 접근하여 체계적인 인식을 형성해야 합니다. 이 개체는 휴머노이드 로봇 지식 그래프에서 기초 이론과 공학 실무를 연결하는 다리 역할을 합니다.

### 실무적 의의
휴머노이드 로봇 산업화 배경에서 작업 Jacobian은 기술 연구, 제품 개발, 투자 결정 및 생태계 구축에 참고 가치를 제공합니다. 그 내포와 외연을 정확히 파악하면 개념 혼동을 방지하고 학제 간 협력을 촉진하는 데 도움이 됩니다.

### 연구 및 발전 방향
휴머노이드 로봇 기술이 지속적으로 발전함에 따라 작업 Jacobian의 관련 이론과 실무도 계속 업데이트되므로 지속적인 추적과 검토가 필요합니다.

### 관련 태그
- jacobian
- task_space
- differential_kinematics
- linear_algebra
- humanoid_control

### 휴머노이드 로봇 시스템에서의 역할
휴머노이드 로봇 산업 체인에서 핵심 연산자 중 하나로서 작업 Jacobian은 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
