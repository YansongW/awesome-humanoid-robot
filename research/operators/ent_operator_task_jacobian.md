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
  zh: '核心内容 ### 任务 Jacobian的定义与定位 任务 Jacobian属于 **operator** 类型。 所属领域包括：07_ai_models_algorithms, 00_foundations。 价值链层级：intelligence,
    foundations。 将关节空间速度和加速度映射到操作空间任务坐标速度/加速度的矩阵。 英文名称为 *Task Jacobian*。 韩文名称为 *작업 Jacobian*。'
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
任务 Jacobian属于 **operator** 类型。 所属领域包括：07_ai_models_algorithms, 00_foundations。 价值链层级：intelligence, foundations。 将关节空间速度和加速度映射到操作空间任务坐标速度/加速度的矩阵。 英文名称为 *Task Jacobian*。 韩文名称为 *작업 Jacobian*。

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
作为人形机器人产业链中的关键operator之一，任务 Jacobian在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Robotics, Vision and Control](https://petercorke.com/rvc/home/)


