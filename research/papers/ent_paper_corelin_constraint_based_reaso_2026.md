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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.20055v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (950 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2602.20055v2

## 개요
전통적인 로봇 내비게이션은 시작점과 목표점 사이에 장애물이 없는 경로가 존재한다고 가정하지만, 실제 환경의 어수선한 물체들이 모든 경로를 막을 수 있습니다. 이를 위해 본 논문은 평생 상호작용 내비게이션 작업을 정의하며, 조작 능력을 갖춘 이동 로봇이 물체를 능동적으로 이동시켜 경로를 개척하고, 순차적인 물체 배치 작업을 완료해야 합니다. 환경 수정은 지속적이므로, 각 결정은 이후 내비게이션 가능성과 작업 난이도에 영향을 미칩니다. CoReLIN 프레임워크는 LLM을 활용한 제약 기반 추론과 능동 인식 모듈을 결합하여, 구조화된 장면 그래프를 통해 어떤 물체를 이동할지, 어디에 배치할지, 다음 탐색 방향을 결정합니다. 표준 운동 계획기는 안정적인 내비게이션 및 조작 기본 동작을 실행합니다. 장기 행동을 평가하기 위해 저자들은 두 가지 새로운 지표를 도입했습니다: 장기 효율 점수(LES)와 어수선함 비용(Price of Clutter)으로, 전자는 성공률, 실행 효율, 환경 최적성을 통합적으로 측정합니다.

## 핵심 내용
### 작업 정의
- **평생 상호작용 내비게이션**: 로봇은 어수선한 환경에서 물체를 이동시켜 동적으로 경로를 개척하고, 순차적인 물체 배치 작업을 완료해야 합니다. 환경 수정은 지속적으로 존재하며, 결정은 장기적 영향을 고려해야 합니다.

### 방법 아키텍처
- **CoReLIN 프레임워크**: LLM 기반 제약 추론 시스템으로, 다음 핵심 모듈을 포함합니다:
  - **구조화된 장면 그래프**: 환경 내 물체, 공간 관계, 이동 가능성 제약을 표현합니다.
  - **능동 인식**: 로봇이 미지의 영역을 탐색하고 장면 그래프 정보를 업데이트하도록 안내합니다.
  - **제약 추론**: LLM이 장면 그래프를 기반으로 다음을 결정합니다: 이동해야 할 물체, 목표 배치 위치, 다음 탐색 영역.
  - **운동 계획기**: 표준 내비게이션 및 조작 기본 동작을 실행하여 동작 신뢰성을 보장합니다.

### 실험 설정
- **시뮬레이션 환경**: ProcTHOR-10k 데이터셋, 10,000개의 실내 장면 포함.
- **기준 방법**: 규칙 기반, 무작위 이동, 추론 없는 LLM 기준과 비교.
- **평가 지표**:
  - **장기 효율 점수(LES)**: 성공률, 실행 효율, 환경 최적성을 통합한 지표.
  - **어수선함 비용(Price of Clutter)**: 환경의 어수선함 정도가 작업 완료에 미치는 영향을 정량화.

### 주요 결과
- **성능 향상**: CoReLIN은 표준 지표와 LES 모두에서 최고 기준선보다 16% 높은 성능을 보였습니다.
- **제로샷 전이**: 추가 훈련 없이 실제 하드웨어 로봇에 직접 배포하여 프레임워크의 일반화 능력을 검증했습니다.
- **장기 계획 이점**: 제약 추론을 통해 CoReLIN은 순차 작업에서 비효율적인 이동과 반복 조작을 크게 줄여 전반적인 효율성을 향상시켰습니다.
