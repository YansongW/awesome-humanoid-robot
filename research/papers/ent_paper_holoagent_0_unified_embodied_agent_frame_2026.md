---
$id: ent_paper_holoagent_0_unified_embodied_agent_frame_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory'
  zh: 'HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory'
  ko: 'HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory'
summary:
  en: 'LLM agents follow a practical execution loop in digital environments: they reason over structured states, invoke tools,
    inspect feedback, and revise actions. Extending this loop to physical robots is difficult because physical execution is
    continuous, embodiment-dependent, uncertain, and constrained by safety. Existing embodied-AI systems have advanced manipulation,
    spatial understanding,.'
  zh: HoloAgent-0 是地平线机器人（Horizon Robotics）与 D-Robotics Robotics 提出的统一具身智能体框架，通过 Embodied AgentOS、3D 空间记忆与具身技能三层耦合，弥合数字 LLM
    智能体与物理机器人之间的执行鸿沟。核心贡献在于将物理技能抽象为类型化、可监控的接口，并以持久空间记忆为中心驱动闭环规划，在仿真导航、真实机器人导航与 3D 语义映射上均取得领先结果。
  ko: 'LLM agents follow a practical execution loop in digital environments: they reason over structured states, invoke tools,
    inspect feedback, and revise actions. Extending this loop to physical robots is difficult because physical execution is
    continuous, embodiment-dependent, uncertain, and constrained by safety. Existing embodied-AI systems have advanced manipulation,
    spatial understanding,.'
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
- holoagent
- '0'
- unified
- embodied
- agent
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-classics (2026-08-05), source channel(s): xiaoze_P082. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.23565 HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory'
  url: https://arxiv.org/abs/2606.23565
  date: '2026-06-22'
  accessed_at: '2026-08-05'
---

## 概述

HoloAgent-0 是地平线机器人（Horizon Robotics）与 D-Robotics Robotics 提出的统一具身智能体框架，通过 Embodied AgentOS、3D 空间记忆与具身技能三层耦合，弥合数字 LLM 智能体与物理机器人之间的执行鸿沟。核心贡献在于将物理技能抽象为类型化、可监控的接口，并以持久空间记忆为中心驱动闭环规划，在仿真导航、真实机器人导航与 3D 语义映射上均取得领先结果。

## 它改变了什么

数字环境中的 LLM 智能体已收敛于「推理→调用工具→检查反馈→修订」的循环，但物理机器人执行是连续、不确定且受安全约束的，现有机器人中间件与指令条件化策略（VLA 等）只提供零散组件，缺乏以闭环物理执行接口为中心的完整框架。HoloAgent-0 真正改变的是将「技能」从绑定特定动作表示或平台的黑盒策略，提升为可组合、可观测、可验证的类型化接口，使长时程任务（如叠衣服）能分解为导航、感知、放置与操作的协调步骤。

这一改变的关键在于承认物理技能不像软件 API 那样有清晰输入/输出类型与确定性反馈，因此框架以记忆中心为设计原则，在调度动作前查询房间、视图、物体、位姿与近期技能结果，使规划成为重复的 observe–retrieve–act–monitor 循环而非一次性文本生成。这直接回应了机器人因空间记忆过期而走错房间、抓取已移动物体失败等系统级挑战。

## 方法拆解

### 三层架构
- **Embodied AgentOS**：将自然语言指令转换为可执行技能图，调度机器人资源，监控执行，并根据运行时反馈触发澄清或重新规划。规划循环为 observe–retrieve–act–monitor。
- **Memory Layer**：持久空间接地与执行历史，包括几何记忆（LiDAR 后端 FAST-LIVO 类紧耦合或纯视觉后端 GeoFlow-SLAM++，要求 N ≥ 3 个标定相机）与语义记忆（SAM2 掩码 + SigLIP 描述符）。
- **Skill Layer**：类型化可监控技能调用，通过 ROS2 命令/状态话题与 AgentOS 连接。

### 语义记忆融合
对每个 2D 掩码计算三个 SigLIP 描述符——d₀（完整关键帧）、d₁（掩码段）、d₂（最小包围框），按公式 d = Σᵢ₌₀² wᵢ ⊙ dᵢ 进行逐维度加权平均融合。实例关联通过投影现有 3D 实例到当前视图，计算 IoU(mₖ, m̃ⱼ) 匹配，匹配观测合并，无匹配则初始化新实例。

### HMSG 分层场景图
按楼层、房间、视图、物体四层组织，具有空间包含的分层边与视图连通性/物体可见性的拓扑边。记忆更新触发事件包括：与现有记忆冲突的新观测、移动或移除物体的技能结果、用户显式反馈。更新顺序为：先重定位，再更新局部度量地图，关联语义实例，最后仅刷新 HMSG 受影响子图。

### 导航与操作
- **HoloNavi**：分层目标导航，LLM 解析为结构化空间查询，分层 CLIP 特征匹配剪枝搜索空间；在线验证循环将候选视图发送给 VLM 进行 fast-to-slow 推理；主动空间探索按预期信息增益、语义相关性、可穿越性和安全约束对候选视点评分。
- **HoloBrain**：VLA 操作后端，报告 object-not-found、物体移动、抓取失败、不可达位姿、碰撞风险等状态。
- **HoloMotion**：支持运动跟踪模式（重定向演示）与速度跟踪模式（行走、转弯）。

## 关键创新

1. **类型化技能接口作为统一执行抽象**：将机器人能力暴露为带命令参数、前置条件、目标引用与预期效果的类型化调用，同时通过状态话题返回进度、失败模式、置信度与可恢复性。这是首次将软件工程中的类型化接口概念系统性地应用于物理技能组合，使异构机器人（人形 G1、R1、轮式双臂平台）能共享同一执行协议。

2. **记忆中心的设计原则**：持久 3D 空间记忆是规划的主要上下文，而非辅助模块。AgentOS 在调度动作前必须查询记忆，且记忆更新采用「局部刷新」策略——仅更新受影响的场景图子图，避免全局重建。这直接解决了物理世界中空间记忆过期导致的任务失败。

3. **跨 embodiment 协调机制**：异构机器人共享记忆记录、类型化技能调用与状态事件，AgentOS 根据能力、位置、可用性和安全状态将任务级技能调用绑定到具体 embodiment。这是对现有单机器人框架的实质性扩展，使多机器人协作成为框架原生能力。

## 实验与结果

### 仿真导航（HM3D-ObjNav）
HoloAgent-Nav 在 SR 与 SPL 上均超过已发表最强基线 MSGNav，并优于 FSR-VLN 的 fast 与 slow 变体。

| 方法 | SR (%) ↑ | SPL (%) ↑ |
|---|---|---|
| SG-Nav | 49.6 | 25.5 |
| VLFM | 62.6 | 31.0 |
| DORAEMON | 66.5 | 20.6 |
| WMNav | 72.2 | 33.3 |
| MSGNav | 74.1 | 33.4 |
| FSR-VLN (fast-matching) | 72.1 | 36.9 |
| FSR-VLN (slow-reasoning) | 80.8 | 41.0 |
| HoloAgent-Nav | 82.6 | 42.8 |

### 真实机器人导航
在物理公寓中遵循 FSR-VLN 基准构建，Top-1 与 Top-5 候选选择下评估目标到达。HoloAgent-Nav 在 1.0 m、2.0 m、3.0 m 阈值下分数相同，表明成功试验已停在严格阈值内。

| 方法 | Top-1@1.0m | Top-1@2.0m | Top-1@3.0m | Top-5@1.0m | Top-5@2.0m | Top-5@3.0m |
|---|---|---|---|---|---|---|
| OK-Robot | 60.92 | 60.92 | 60.92 | 63.22 | 63.22 | 63.22 |
| MobilityVLA | 34.48 | 59.77 | 75.86 | – | – | – |
| HOV-SG | 51.72 | 57.47 | 58.62 | 77.00 | 81.61 | 82.76 |
| FSR-VLN | 91.95 | 91.95 | 94.25 | 94.25 | 96.55 | 96.55 |
| HoloAgent-Nav | 97.70 | 97.70 | 97.70 | 98.90 | 98.90 | 98.90 |

### 3D 语义映射（ScanNet 与 Replica）
HoloAgent-Memory 在 ScanNet 上 mIoU 达 31.58，超过所有在线方法；在 Replica 上 mIoU 为 29.93，频率加权指标仍有差距。

| 数据集 | 方法 | Online | mIoU ↑ | mAcc ↑ | f-mIoU ↑ | f-Acc ↑ |
|---|---|---|---|---|---|---|
| ScanNet | Omni-Map | ✓ | 25.42 | 50.93 | 50.86 | 57.05 |
| ScanNet | HoloAgent-Memory | ✓ | 31.58 | 45.54 | 47.43 | 61.58 |
| Replica | Omni-Map | ✓ | 29.06 | 44.54 | 64.42 | 72.22 |
| Replica | HoloAgent-Memory | ✓ | 29.93 | 43.60 | 57.00 | 65.39 |

## 边界与局限

作者明确承认操作、全身运动和跨 embodiment 协调使用异构硬件，尚未在统一可重复协议下标准化，因此不报告端到端成功基准，全栈行为仅提供定性执行轨迹。论文未明确真实机器人导航的具体成功率数字（仅说明报告 Top-1 和 Top-5 候选选择下的目标到达成功率）、未提供 3D 语义映射的具体数值结果（除表格外）、未报告训练配置细节。Replica 上频率加权指标的差距表明大面积实体和多视图特征聚合仍需改进。每个新具身引入不同的感知、驱动、安全和恢复约束，人形机器人尤其苛刻，因为移动、操作、平衡和交互必须作为耦合技能栈运行。

## 工程启示

复现时先核对 ROS2 命令/状态接口的一致性——模拟与硬件必须使用相同接口，技能调度、监控和任务状态更新遵循一致执行协议。最容易踩坑的是视觉后端要求 N ≥ 3 个标定相机，多相机标定质量直接影响语义记忆的实例关联精度。语义记忆融合中三个 SigLIP 描述符的权重 wᵢ 需要针对场景调整，论文未明确默认值。导航评估中 1.0 m、2.0 m、3.0 m 阈值下分数相同，说明成功试验已停在严格阈值内，剩余失败需要更好的恢复而非更宽松的定位——调试时应优先改进失败恢复逻辑而非放宽评估标准。开发期间记录 ROS2 bags、结构化日志、RViz 视图和 Rerun 可视化用于诊断，建议下游团队沿用此实践。

## Overview
LLM agents follow a practical execution loop in digital environments: they reason over structured states, invoke tools, inspect feedback, and revise actions. Extending this loop to physical robots is difficult because physical execution is continuous, embodiment-dependent, uncertain, and constrained by safety. Existing embodied-AI systems have advanced manipulation, spatial understanding, navigation, and humanoid control, but these capabilities often remain specialized modules or loosely coupled decision loops. In this work, we introduce HoloAgent-0, a unified embodied agent framework for real-world robot deployment. Embodied AgentOS converts language instructions into executable skill graphs, schedules robot resources, monitors execution, and triggers clarification or re-planning from runtime feedback. HoloAgent-0 organizes heterogeneous robot models and controllers through three coupled layers: Embodied AgentOS for closed-loop execution, 3D spatial memory for physical world grounding, and embodied skills for robot action. We deploy HoloAgent-0 on real hardware and evaluate its spatial memory, long-horizon navigation, and closed-loop execution across motion generation, object search, cross-robot coordination, and mobile manipulation.

## 参考
- https://arxiv.org/abs/2606.23565

## 개요

HoloAgent-0는 Horizon Robotics와 D-Robotics Robotics가 제안한 통합 임베디드 에이전트 프레임워크로, Embodied AgentOS, 3D 공간 메모리, 임베디드 스킬의 3계층 결합을 통해 디지털 LLM 에이전트와 물리적 로봇 간의 실행 격차를 해소합니다. 핵심 기여는 물리적 스킬을 타입화되고 모니터링 가능한 인터페이스로 추상화하고, 지속적 공간 메모리를 중심으로 폐루프 계획을 구동하여 시뮬레이션 내비게이션, 실제 로봇 내비게이션, 3D 의미론적 매핑에서 선도적인 결과를 달성한 것입니다.

## 무엇을 바꾸었는가

디지털 환경의 LLM 에이전트는 '추론→도구 호출→피드백 확인→수정'의 루프로 수렴했지만, 물리적 로봇 실행은 연속적이고 불확실하며 안전 제약을 받습니다. 기존 로봇 미들웨어와 명령 조건화 정책(VLA 등)은 단편적인 구성 요소만 제공할 뿐, 폐루프 물리적 실행 인터페이스를 중심으로 한 완전한 프레임워크가 부재했습니다. HoloAgent-0가 진정으로 바꾼 것은 '스킬'을 특정 동작 표현이나 플랫폼에 바인딩된 블랙박스 정책에서, 조합 가능하고 관찰 가능하며 검증 가능한 타입화된 인터페이스로 승격시켜, 긴 시간 범위의 작업(예: 옷 개기)을 내비게이션, 인식, 배치, 조작의 조정된 단계로 분해할 수 있게 한 것입니다.

이 변화의 핵심은 물리적 스킬이 소프트웨어 API처럼 명확한 입력/출력 타입과 결정적 피드백을 가지지 않는다는 점을 인정하고, 프레임워크가 메모리 중심 설계 원칙을 채택하여 스케줄링 동작 전에 방, 뷰, 객체, 자세, 최근 스킬 결과를 조회함으로써 계획을 일회성 텍스트 생성이 아닌 반복적인 observe–retrieve–act–monitor 루프로 만든 것입니다. 이는 공간 메모리 만료로 로봇이 잘못된 방으로 가거나, 이동된 객체를 잡지 못하는 등의 시스템 수준 과제에 직접 대응합니다.

## 방법 분석

### 3계층 아키텍처
- **Embodied AgentOS**: 자연어 명령을 실행 가능한 스킬 그래프로 변환하고, 로봇 리소스를 스케줄링하며, 실행을 모니터링하고, 런타임 피드백에 따라 명확화 또는 재계획을 트리거합니다. 계획 루프는 observe–retrieve–act–monitor입니다.
- **메모리 계층**: 지속적 공간 접지 및 실행 이력으로, 기하 메모리(LiDAR 백엔드 FAST-LIVO 유사 긴밀 결합 또는 순수 비전 백엔드 GeoFlow-SLAM++, N ≥ 3개의 캘리브레이션 카메라 요구)와 의미 메모리(SAM2 마스크 + SigLIP 디스크립터)를 포함합니다.
- **스킬 계층**: 타입화되고 모니터링 가능한 스킬 호출로, ROS2 명령/상태 토픽을 통해 AgentOS와 연결됩니다.

### 의미 메모리 융합
각 2D 마스크에 대해 세 개의 SigLIP 디스크립터——d₀(전체 키프레임), d₁(마스크 세그먼트), d₂(최소 바운딩 박스)——를 계산하고, 공식 d = Σᵢ₌₀² wᵢ ⊙ dᵢ에 따라 차원별 가중 평균 융합을 수행합니다. 인스턴스 연관은 기존 3D 인스턴스를 현재 뷰에 투영하고 IoU(mₖ, m̃ⱼ) 매칭을 계산하여, 매칭된 관측은 병합하고 매칭이 없으면 새 인스턴스를 초기화합니다.

### HMSG 계층적 장면 그래프
층, 방, 뷰, 객체의 4계층으로 구성되며, 공간 포함 관계의 계층적 엣지와 뷰 연결성/객체 가시성의 토폴로지 엣지를 가집니다. 메모리 업데이트를 트리거하는 이벤트는 다음과 같습니다: 기존 메모리와 충돌하는 새 관측, 객체 이동 또는 제거의 스킬 결과, 사용자 명시적 피드백. 업데이트 순서는 먼저 재위치, 그다음 로컬 메트릭 맵 업데이트, 의미 인스턴스 연관, 마지막으로 HMSG의 영향받은 서브그래프만 새로고침합니다.

### 내비게이션 및 조작
- **HoloNavi**: 계층적 목표 내비게이션으로, LLM이 구조화된 공간 쿼리로 파싱하고, 계층적 CLIP 특징 매칭으로 검색 공간을 가지치기합니다. 온라인 검증 루프는 후보 뷰를 VLM에 보내 fast-to-slow 추론을 수행합니다. 능동적 공간 탐색은 예상 정보 이득, 의미 관련성, 통과 가능성, 안전 제약에 따라 후보 뷰를 점수화합니다.
- **HoloBrain**: VLA 조작 백엔드로, object-not-found, 객체 이동, 그립 실패, 도달 불가능한 자세, 충돌 위험 등의 상태를 보고합니다.
- **HoloMotion**: 모션 추적 모드(재지향 데모)와 속도 추적 모드(보행, 회전)를 지원합니다.

## 핵심 혁신

1. **타입화된 스킬 인터페이스를 통합 실행 추상화로**: 로봇 능력을 명령 매개변수, 사전 조건, 목표 참조, 예상 효과를 가진 타입화된 호출로 노출하고, 상태 토픽을 통해 진행률, 실패 모드, 신뢰도, 복구 가능성을 반환합니다. 이는 소프트웨어 공학의 타입화된 인터페이스 개념을 물리적 스킬 조합에 체계적으로 적용한 최초의 사례로, 이기종 로봇(휴머노이드 G1, R1, 휠형 이중 암 플랫폼)이 동일한 실행 프로토콜을 공유할 수 있게 합니다.

2. **메모리 중심 설계 원칙**: 지속적 3D 공간 메모리는 보조 모듈이 아닌 계획의 주요 컨텍스트입니다. AgentOS는 동작 스케줄링 전에 메모리를 조회해야 하며, 메모리 업데이트는 '로컬 새로고침' 전략을 채택하여 영향받은 장면 그래프 서브그래프만 업데이트하고 전역 재구성을 피합니다. 이는 물리적 세계에서 공간 메모리 만료로 인한 작업 실패를 직접 해결합니다.

3. **크로스 임베디드 조정 메커니즘**: 이기종 로봇이 공유 메모리 기록, 타입화된 스킬 호출, 상태 이벤트를 공유하며, AgentOS는 능력, 위치, 가용성, 안전 상태에 따라 작업 수준 스킬 호출을 특정 임베디드에 바인딩합니다. 이는 기존 단일 로봇 프레임워크에 대한 실질적 확장으로, 다중 로봇 협업을 프레임워크의 기본 능력으로 만듭니다.

## 실험 및 결과

### 시뮬레이션 내비게이션(HM3D-ObjNav)
HoloAgent-Nav는 SR과 SPL 모두에서 발표된 최강 베이스라인 MSGNav를 능가하며, FSR-VLN의 fast 및 slow 변형보다 우수합니다.

| 방법 | SR (%) ↑ | SPL (%) ↑ |
|---|---|---|
| SG-Nav | 49.6 | 25.5 |
| VLFM | 62.6 | 31.0 |
| DORAEMON | 66.5 | 20.6 |
| WMNav | 72.2 | 33.3 |
| MSGNav | 74.1 | 33.4 |
| FSR-VLN (fast-matching) | 72.1 | 36.9 |
| FSR-VLN (slow-reasoning) | 80.8 | 41.0 |
| HoloAgent-Nav | 82.6 | 42.8 |

### 실제 로봇 내비게이션
물리적 아파트에서 FSR-VLN 벤치마크를 따라 구축되었으며, Top-1 및 Top-5 후보 선택에서 목표 도달을 평가합니다. HoloAgent-Nav는 1.0m, 2.0m, 3.0m 임계값에서 동일한 점수를 기록하여, 성공한 실험이 엄격한 임계값 내에 정지했음을 나타냅니다.

| 방법 | Top-1@1.0m | Top-1@2.0m | Top-1@3.0m | Top-5@1.0m | Top-5@2.0m | Top-5@3.0m |
|---|---|---|---|---|---|---|
| OK-Robot | 60.92 | 60.92 | 60.92 | 63.22 | 63.22 | 63.22 |
| MobilityVLA | 34.48 | 59.77 | 75.86 | – | – | – |
| HOV-SG | 51.72 | 57.47 | 58.62 | 77.00 | 81.61 | 82.76 |
| FSR-VLN | 91.95 | 91.95 | 94.25 | 94.25 | 96.55 | 96.55 |
| HoloAgent-Nav | 97.70 | 97.70 | 97.70 | 98.90 | 98.90 | 98.90 |

### 3D 의미 매핑(ScanNet 및 Replica)
HoloAgent-Memory는 ScanNet에서 mIoU 31.58로 모든 온라인 방법을 능가하며, Replica에서는 mIoU 29.93으로 주파수 가중 지표에서 여전히 격차가 있습니다.

| 데이터셋 | 방법 | Online | mIoU ↑ | mAcc ↑ | f-mIoU ↑ | f-Acc ↑ |
|---|---|---|---|---|---|---|
| ScanNet | Omni-Map | ✓ | 25.42 | 50.93 | 50.86 | 57.05 |
| ScanNet | HoloAgent-Memory | ✓ | 31.58 | 45.54 | 47.43 | 61.58 |
| Replica | Omni-Map | ✓ | 29.06 | 44.54 | 64.42 | 72.22 |
| Replica | HoloAgent-Memory | ✓ | 29.93 | 43.60 | 57.00 | 65.39 |

## 한계와 제약

저자는 조작, 전신 운동, 크로스 임베디드 조정이 이기종 하드웨어를 사용하며 아직 통일된 재현 가능한 프로토콜로 표준화되지 않았음을 명시적으로 인정하므로, 엔드투엔드 성공 벤치마크를 보고하지 않으며, 풀스택 동작은 정성적 실행 궤적만 제공합니다. 논문은 실제 로봇 내비게이션의 구체적인 성공률 수치를 명시하지 않았고(Top-1 및 Top-5 후보 선택에서의 목표 도달 성공률만 보고), 3D 의미 매핑의 구체적인 수치 결과를 표 외에 제공하지 않았으며, 훈련 구성 세부 사항도 보고하지 않았습니다. Replica에서 주파수 가중 지표의 격차는 대형 엔티티와 다중 뷰 특징 집계가 여전히 개선이 필요함을 시사합니다. 각 새 임베디드는 서로 다른 인식, 구동, 안전, 복구 제약을 도입하며, 휴머노이드 로봇은 이동, 조작, 균형, 상호작용이 결합된 스킬 스택으로 작동해야 하므로 특히 까다롭습니다.

## 엔지니어링 시사점

재현 시 먼저 ROS2 명령/상태 인터페이스의 일관성을 확인하십시오——시뮬레이션과 하드웨어는 동일한 인터페이스를 사용해야 하며, 스킬 스케줄링, 모니터링, 작업 상태 업데이트는 일관된 실행 프로토콜을 따릅니다. 가장 함정에 빠지기 쉬운 부분은 비전 백엔드가 N ≥ 3개의 캘리브레이션 카메라를 요구한다는 점으로, 다중 카메라 캘리브레이션 품질이 의미 메모리의 인스턴스 연관 정밀도에 직접 영향을 미칩니다. 의미 메모리 융합에서 세 개의 SigLIP 디스크립터의 가중치 wᵢ는 장면에 따라 조정해야 하며, 논문은 기본값을 명시하지 않았습니다. 내비게이션 평가에서 1.0m, 2.0m, 3.0m 임계값에서 점수가 동일하다는 것은 성공한 실험이 엄격한 임계값 내에 정지했음을 의미하며, 남은 실패는 더 관대한 위치 추정이 아닌 더 나은 복구가 필요합니다——디버깅 시 평가 기준을 완화하는 대신 실패 복구 로직 개선을 우선시해야 합니다. 개발 중 ROS2 bags, 구조화된 로그, RViz 뷰, Rerun 시각화를 기록하여 진단에 사용하며, 다운스트림 팀도 이 관행을 따르기를 권장합니다.
