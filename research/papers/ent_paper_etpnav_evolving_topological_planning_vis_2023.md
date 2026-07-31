---
$id: ent_paper_etpnav_evolving_topological_planning_vis_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments'
  zh: 'ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments'
  ko: 'ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments'
summary:
  en: 'Vision-language navigation is a task that requires an agent to follow instructions to navigate in environments. It
    becomes increasingly crucial in the field of embodied AI, with potential applications in autonomous navigation, search
    and rescue, and human-robot interaction. Institutions per source list: 中国科学院大学.'
  zh: ETPNav 是一种面向连续环境视觉语言导航（VLN-CE）的新型框架，由研究团队提出。其核心贡献在于通过在线拓扑地图构建与跨模态规划器，将导航分解为高层规划与低层控制，并利用试错启发式避障控制器提升鲁棒性。在 R2R-CE 和 RxR-CE
    基准上，该方法分别实现了超过 10% 和 20% 的性能提升。
  ko: 'Vision-language navigation is a task that requires an agent to follow instructions to navigate in environments. It
    becomes increasingly crucial in the field of embodied AI, with potential applications in autonomous navigation, search
    and rescue, and human-robot interaction. Institutions per source list: 中国科学院大学.'
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
- etpnav
- evolving
- topological
- planning
- vis
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 824 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2304.03047 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2304.03047v3); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2304.03047 ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments'
  url: https://arxiv.org/abs/2304.03047
  accessed_at: '2026-07-31'
  date: '2023-04-06'
- id: src_002
  type: website
  title: Project page
  url: https://github.com/MarSaKi/ETPNav
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

ETPNav 针对 VLN-CE 任务中环境抽象与避障控制两大挑战，提出了一种分层导航框架。该框架无需先验环境经验，通过自组织预测航点在线构建拓扑地图，使智能体能够将导航过程分解为基于指令的高层路径规划与低层运动控制。高层规划采用 transformer 架构的跨模态模型，结合拓扑地图与语言指令生成导航计划；低层控制则通过试错启发式策略避免智能体陷入障碍物。实验表明，ETPNav 在 R2R-CE 和 RxR-CE 数据集上显著超越此前最优方法。

## 核心内容
### 方法架构
ETPNav 的核心设计围绕两个关键能力展开：
- **环境抽象与远程规划**：通过在线拓扑地图构建，智能体沿已遍历路径自组织预测航点，无需预先环境经验。该地图将导航分解为高层规划（基于指令选择子目标）与低层控制（执行局部运动）。
- **避障控制**：采用试错启发式控制器，当智能体检测到障碍物时，通过迭代尝试不同方向避免卡滞，确保低层动作的鲁棒性。

### 跨模态规划器
- 基于 transformer 架构，融合拓扑地图节点特征与语言指令的跨模态表示。
- 规划器输出一系列子目标航点，指导智能体逐步接近最终目标。

### 实验设置与结果
- **数据集**：在 R2R-CE 与 RxR-CE 两个 VLN-CE 基准上评估。
- **关键性能**：
  - 在 R2R-CE 上，ETPNav 相比此前最优方法（prior state-of-the-art）提升超过 10%。
  - 在 RxR-CE 上，提升幅度超过 20%。
- **代码开源**：完整实现发布于 https://github.com/MarSaKi/ETPNav。

### 结论
ETPNav 通过在线拓扑规划与分层控制，有效解决了连续环境中长距离导航与避障的耦合问题，为 VLN-CE 任务提供了新的性能标杆。

## Overview
Vision-language navigation is a task that requires an agent to follow instructions to navigate in environments. It becomes increasingly crucial in the field of embodied AI, with potential applications in autonomous navigation, search and rescue, and human-robot interaction. In this paper, we propose to address a more practical yet challenging counterpart setting - vision-language navigation in continuous environments (VLN-CE). To develop a robust VLN-CE agent, we propose a new navigation framework, ETPNav, which focuses on two critical skills: 1) the capability to abstract environments and generate long-range navigation plans, and 2) the ability of obstacle-avoiding control in continuous environments. ETPNav performs online topological mapping of environments by self-organizing predicted waypoints along a traversed path, without prior environmental experience. It privileges the agent to break down the navigation procedure into high-level planning and low-level control. Concurrently, ETPNav utilizes a transformer-based cross-modal planner to generate navigation plans based on topological maps and instructions. The plan is then performed through an obstacle-avoiding controller that leverages a trial-and-error heuristic to prevent navigation from getting stuck in obstacles. Experimental results demonstrate the effectiveness of the proposed method. ETPNav yields more than 10% and 20% improvements over prior state-of-the-art on R2R-CE and RxR-CE datasets, respectively. Our code is available at https://github.com/MarSaKi/ETPNav.

## 参考
- https://arxiv.org/abs/2304.03047
- https://github.com/MarSaKi/ETPNav
- https://github.com/ImChong/Robotics_Notebooks

## 개요

ETPNav는 VLN-CE 작업에서 환경 추상화와 장애물 회피 제어라는 두 가지 주요 도전 과제를 해결하기 위해 계층적 내비게이션 프레임워크를 제안합니다. 이 프레임워크는 사전 환경 경험 없이 자가 조직적 예측 웨이포인트를 통해 온라인으로 토폴로지 맵을 구축하여, 에이전트가 내비게이션 과정을 명령 기반의 고수준 경로 계획과 저수준 운동 제어로 분해할 수 있도록 합니다. 고수준 계획은 트랜스포머 아키텍처의 교차 모달 모델을 사용하여 토폴로지 맵과 언어 명령을 결합해 내비게이션 계획을 생성하고, 저수준 제어는 시행착오 휴리스틱 전략을 통해 에이전트가 장애물에 갇히는 것을 방지합니다. 실험 결과, ETPNav는 R2R-CE 및 RxR-CE 데이터셋에서 이전 최고 성능 방법을 크게 능가했습니다.

## 핵심 내용
### 방법 아키텍처
ETPNav의 핵심 설계는 두 가지 주요 능력을 중심으로 전개됩니다:
- **환경 추상화와 원거리 계획**: 온라인 토폴로지 맵 구축을 통해 에이전트가 이미 탐색한 경로를 따라 자가 조직적으로 웨이포인트를 예측하며, 사전 환경 경험이 필요하지 않습니다. 이 맵은 내비게이션을 고수준 계획(명령 기반 하위 목표 선택)과 저수준 제어(국소 운동 실행)로 분해합니다.
- **장애물 회피 제어**: 시행착오 휴리스틱 컨트롤러를 사용하여, 에이전트가 장애물을 감지하면 다양한 방향을 반복적으로 시도해 막힘을 방지하며, 저수준 동작의 견고성을 보장합니다.

### 교차 모달 플래너
- 트랜스포머 아키텍처를 기반으로, 토폴로지 맵 노드 특징과 언어 명령의 교차 모달 표현을 융합합니다.
- 플래너는 일련의 하위 목표 웨이포인트를 출력하여 에이전트가 최종 목표에 점진적으로 접근하도록 안내합니다.

### 실험 설정 및 결과
- **데이터셋**: R2R-CE 및 RxR-CE 두 VLN-CE 벤치마크에서 평가되었습니다.
- **주요 성능**:
  - R2R-CE에서 ETPNav는 이전 최고 성능 방법(prior state-of-the-art)보다 10% 이상 향상되었습니다.
  - RxR-CE에서는 20% 이상 향상되었습니다.
- **코드 공개**: 전체 구현은 https://github.com/MarSaKi/ETPNav에서 제공됩니다.

### 결론
ETPNav는 온라인 토폴로지 계획과 계층적 제어를 통해 연속 환경에서의 장거리 내비게이션과 장애물 회피의 결합 문제를 효과적으로 해결하며, VLN-CE 작업에 새로운 성능 기준을 제시합니다.
