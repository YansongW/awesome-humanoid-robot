---
$id: ent_software_moveit_motion_planning_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: software_platform
names:
  en: MoveIt Motion Planning
  zh: MoveIt 运动规划
  ko: MoveIt 모션 계획
summary:
  en: Motion-planning framework commonly used for manipulation arms and whole-body planning.
  zh: MoveIt 是 ROS 生态中常用的运动规划框架，集成 OMPL 等规划器、逆运动学求解与碰撞检测，广泛用于机械臂及人形机器人的全身运动规划。
  ko: 조작 팔 및 전신 계획에 일반적으로 사용되는 모션 계획 프레임워크.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- manipulation
- motion_planning
- moveit
- ros
- software_platform
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-02'
  confidence: medium
  notes: Imported via ingestion framework from source_type=website. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: website
  title: MoveIt Motion Planning
  url: https://moveit.ros.org/
  date: '2024'
  accessed_at: '2026-07-02'
---

## 概述
常用于机械臂和全身运动规划的框架。

## 核心内容
### MoveIt 运动规划的定义与定位
MoveIt 运动规划属于 **软件平台** 类型。 所属领域包括：软件中间件, AI 模型与算法。 价值链层级：智能层。 常用于机械臂和全身运动规划的框架。 英文名称为 *MoveIt Motion Planning*。 韩文名称为 *MoveIt 모션 계획*。

### MoveIt 运动规划的工作原理与技术架构
MoveIt 运动规划的核心机制决定了其在人形机器人系统中的性能边界。理解其内部结构、信号流与控制接口，有助于进行系统集成与优化。
在选型与集成过程中，需要关注其与控制器、通信总线、电源系统与机械结构的兼容性。

### 关键参数与选型要点
在工程实践中，选用MoveIt 运动规划需要综合考虑性能指标、可靠性、成本、供应链成熟度以及与整机系统的兼容性。
关键参数通常包括精度、带宽、扭矩、功耗、重量、接口协议与环境适应性等。
针对不同应用场景，可能需要在性能与成本之间进行权衡，并预留适当的冗余与安全裕量。

### 典型应用与发展趋势
MoveIt 运动规划已广泛应用于人形机器人的原型验证、学术研究与早期商业化产品中。
未来随着产业链成熟，其集成度、智能化水平与成本效益有望持续提升。

### 相关标签
- manipulation
- motion_planning
- moveit
- ros
- software_platform

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键软件平台之一，MoveIt 运动规划在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [MoveIt Motion Planning](https://moveit.ros.org/)


