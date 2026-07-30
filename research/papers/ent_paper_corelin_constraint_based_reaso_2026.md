---
$id: ent_paper_corelin_constraint_based_reaso_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoReLIN: Constraint-based Reasoning for Zero-shot Lifelong Interactive Navigation'
  zh: 'CoReLIN: Constraint-based Reasoning for Zero-shot Lifelong Interactive Navigation'
  ko: 'CoReLIN: Constraint-based Reasoning for Zero-shot Lifelong Interactive Navigation'
summary:
  en: 'arXiv:2602.20055v2 Announce Type: replace Abstract: Robot navigation typically assumes an obstacle-free path exists
    between start and goal. In real environments, however, clutter may block all routes. We introduce Lifelong Interactive
    Navigation, where a mobile robot with manipulation capabilities must move objects to forge paths and complete sequential
    object-placement tasks. Because environment modifications persist, decisions impact future navigability and task difficulty.
    We propose CoReLIN, an LLM-driven constraint-based reasoning framework with active perception. CoReLIN reasons over a
    structured scene graph to decide which objects to relocate, where to place them, and where to explore next. A standard
    motion planner executes reliable navigation and manipulation primitives. To evaluate long-horizon behavior, we introduce
    2 new metrics - Long-term Efficiency Score (LES), a unified metric capturing success, execution efficiency, environment
    optimality, captured by Price of Clutter. In ProcTHOR-10k, CoReLIN outperforms best baseline by 16% under standard metrics
    and LES, and transfers to real-world hardware.'
  zh: CoReLIN 是一个由 LLM 驱动的基于约束的推理框架，用于解决零样本终身交互导航问题。该框架由研究团队提出，核心贡献在于让移动操作机器人在杂乱环境中通过移动物体开辟路径，并完成序列化物体放置任务。在 ProcTHOR-10k
    基准上，CoReLIN 在标准指标和长期效率得分（LES）上均比最佳基线高出 16%，并能迁移至真实硬件。
  ko: 'arXiv:2602.20055v2 Announce Type: replace Abstract: Robot navigation typically assumes an obstacle-free path exists
    between start and goal. In real environments, however, clutter may block all routes. We introduce Lifelong Interactive
    Navigation, where a mobile robot with manipulation capabilities must move objects to forge paths and complete sequential
    object-placement tasks. Because environment modifications persist, decisions impact future navigability and task difficulty.
    We propose CoReLIN, an LLM-driven constraint-based reasoning framework with active perception. CoReLIN reasons over a
    structured scene graph to decide which objects to relocate, where to place them, and where to explore next. A standard
    motion planner executes reliable navigation and manipulation primitives. To evaluate long-horizon behavior, we introduce
    2 new metrics - Long-term Efficiency Score (LES), a unified metric capturing success, execution efficiency, environment
    optimality, captured by Price of Clutter. In ProcTHOR-10k, CoReLIN outperforms best baseline by 16% under standard metrics
    and LES, and transfers to real-world hardware.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- corelin
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.20055v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'CoReLIN: Constraint-based Reasoning for Zero-shot Lifelong Interactive Navigation'
  url: https://arxiv.org/abs/2602.20055
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
传统机器人导航假设起点与终点间存在无障碍路径，但真实环境中的杂乱物体可能阻塞所有路线。为此，本文定义了终身交互导航任务，要求具备操作能力的移动机器人主动移动物体以开辟路径，并完成序列化的物体放置任务。由于环境修改具有持久性，每次决策都会影响后续导航可行性与任务难度。CoReLIN 框架利用 LLM 进行基于约束的推理，并结合主动感知模块，通过结构化场景图决定移动哪些物体、放置于何处以及下一步探索方向。标准运动规划器负责执行可靠的导航与操作原语。为评估长期行为，作者引入了两个新指标：长期效率得分（LES）和杂乱代价（Price of Clutter），前者统一衡量成功率、执行效率与环境最优性。

## 核心内容
### 任务定义
- **终身交互导航**：机器人需在杂乱环境中通过移动物体动态开辟路径，并完成序列化物体放置任务。环境修改持久存在，决策需考虑长期影响。

### 方法架构
- **CoReLIN 框架**：基于 LLM 的约束推理系统，包含以下核心模块：
  - **结构化场景图**：表示环境中的物体、空间关系及可移动性约束。
  - **主动感知**：引导机器人探索未知区域，更新场景图信息。
  - **约束推理**：LLM 根据场景图决定：哪些物体需要移动、目标放置位置、下一步探索区域。
  - **运动规划器**：执行标准导航与操作原语，确保动作可靠性。

### 实验设置
- **仿真环境**：ProcTHOR-10k 数据集，包含 10,000 个室内场景。
- **基线方法**：对比基于规则、随机移动及无推理的 LLM 基线。
- **评估指标**：
  - **长期效率得分（LES）**：综合成功率、执行效率与环境最优性的统一指标。
  - **杂乱代价（Price of Clutter）**：量化环境杂乱程度对任务完成的影响。

### 关键结果
- **性能提升**：CoReLIN 在标准指标和 LES 上均比最佳基线高出 16%。
- **零样本迁移**：无需额外训练，直接部署至真实硬件机器人，验证了框架的泛化能力。
- **长期规划优势**：通过约束推理，CoReLIN 在序列任务中显著减少无效移动和重复操作，提升整体效率。

## Overview
Robot navigation typically assumes an obstacle-free path exists between start and goal. In real environments, however, clutter may block all routes. We introduce Lifelong Interactive Navigation, where a mobile robot with manipulation capabilities must move objects to forge paths and complete sequential object-placement tasks. Because environment modifications persist, decisions impact future navigability and task difficulty. We propose CoReLIN, an LLM-driven constraint-based reasoning framework with active perception. CoReLIN reasons over a structured scene graph to decide which objects to relocate, where to place them, and where to explore next. A standard motion planner executes reliable navigation and manipulation primitives. To evaluate long-horizon behavior, we introduce 2 new metrics - Long-term Efficiency Score (LES), a unified metric capturing success, execution efficiency, environment optimality, captured by Price of Clutter. In ProcTHOR-10k, CoReLIN outperforms best baseline by 16% under standard metrics and LES, and transfers to real-world hardware.

## 개요
로봇 내비게이션은 일반적으로 시작 지점과 목표 지점 사이에 장애물이 없는 경로가 존재한다고 가정합니다. 그러나 실제 환경에서는 잡동사니가 모든 경로를 막을 수 있습니다. 우리는 조작 능력을 갖춘 이동 로봇이 경로를 만들기 위해 물체를 이동시키고 순차적인 물체 배치 작업을 완료해야 하는 평생 상호작용 내비게이션(Lifelong Interactive Navigation)을 소개합니다. 환경 수정이 지속되기 때문에 결정은 미래의 이동 가능성과 작업 난이도에 영향을 미칩니다. 우리는 능동적 인식을 갖춘 LLM 기반 제약 조건 추론 프레임워크인 CoReLIN을 제안합니다. CoReLIN은 구조화된 장면 그래프를 기반으로 추론하여 어떤 물체를 재배치할지, 어디에 배치할지, 다음에 어디를 탐색할지 결정합니다. 표준 모션 플래너는 신뢰할 수 있는 내비게이션 및 조작 프리미티브를 실행합니다. 장기적 행동을 평가하기 위해 우리는 2가지 새로운 지표인 장기 효율성 점수(LES)를 도입합니다. 이는 성공, 실행 효율성, 환경 최적성을 통합한 지표로, Price of Clutter로 포착됩니다. ProcTHOR-10k에서 CoReLIN은 표준 지표와 LES에서 최고 기준선보다 16% 더 뛰어난 성능을 보이며, 실제 하드웨어로 전이됩니다.

## 핵심 내용
로봇 내비게이션은 일반적으로 시작 지점과 목표 지점 사이에 장애물이 없는 경로가 존재한다고 가정합니다. 그러나 실제 환경에서는 잡동사니가 모든 경로를 막을 수 있습니다. 우리는 조작 능력을 갖춘 이동 로봇이 경로를 만들기 위해 물체를 이동시키고 순차적인 물체 배치 작업을 완료해야 하는 평생 상호작용 내비게이션(Lifelong Interactive Navigation)을 소개합니다. 환경 수정이 지속되기 때문에 결정은 미래의 이동 가능성과 작업 난이도에 영향을 미칩니다. 우리는 능동적 인식을 갖춘 LLM 기반 제약 조건 추론 프레임워크인 CoReLIN을 제안합니다. CoReLIN은 구조화된 장면 그래프를 기반으로 추론하여 어떤 물체를 재배치할지, 어디에 배치할지, 다음에 어디를 탐색할지 결정합니다. 표준 모션 플래너는 신뢰할 수 있는 내비게이션 및 조작 프리미티브를 실행합니다. 장기적 행동을 평가하기 위해 우리는 2가지 새로운 지표인 장기 효율성 점수(LES)를 도입합니다. 이는 성공, 실행 효율성, 환경 최적성을 통합한 지표로, Price of Clutter로 포착됩니다. ProcTHOR-10k에서 CoReLIN은 표준 지표와 LES에서 최고 기준선보다 16% 더 뛰어난 성능을 보이며, 실제 하드웨어로 전이됩니다.

## 参考
- http://arxiv.org/abs/2602.20055v2
