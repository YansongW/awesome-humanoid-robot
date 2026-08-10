---
$id: ent_paper_automating_the_design_of_embod_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Automating the Design of Embodied Agent Architectures
  zh: Automating the Design of Embodied Agent Architectures
  ko: Automating the Design of Embodied Agent Architectures
summary:
  en: 'arXiv:2606.30111v2 Announce Type: replace Abstract: Embodied agents are typically built as hand-designed compositions
    of perception, memory, planning, and action modules. This modularity exposes a large architectural design space, but current
    systems still rely on researcher intuition to choose where information is stored, how observations are processed, and
    how model calls are connected. Agent Architecture Search (AAS) automates such design for text-domain agents, but has not
    been systematically evaluated on perceptual embodied agents through simulator rollouts. We study this transfer. We introduce
    AgentCanvas, a typed-graph runtime that hosts embodied executors as editable node-and-wire programs with simulator-aware
    execution and episode-level logs, and KDLoop, a coding-agent search procedure that cycles through proposal, critique,
    experiment, and distillation, with triggered reflection after stalls. We evaluate three AAS variants across four embodied
    executors spanning vision-language navigation, embodied question answering, and language-conditioned manipulation. The
    resulting 3x4 matrix shows that architecture-level search can produce deployable and directional success-rate gains on
    embodied tasks, while one apparent high-scoring candidate is rejected as leak-bearing. At the same time, the experiments
    expose constraints that are muted in text-domain AAS: optimization signals can be masked by rollout noise, search can
    become trapped in local edit basins, and episode-level credit assignment only partially emerges even when detailed logs
    are available. These results characterize both the promise and the current limits of automated architecture search for
    embodied agents.'
  zh: 本文研究将文本域智能体架构搜索（AAS）迁移至具身感知智能体。作者提出AgentCanvas运行时和KDLoop搜索流程，在四个具身执行器上评估三种AAS变体，发现架构搜索可带来成功率提升，但也暴露出噪声干扰、局部最优和信用分配不完整等限制。
  ko: 'arXiv:2606.30111v2 Announce Type: replace Abstract: Embodied agents are typically built as hand-designed compositions
    of perception, memory, planning, and action modules. This modularity exposes a large architectural design space, but current
    systems still rely on researcher intuition to choose where information is stored, how observations are processed, and
    how model calls are connected. Agent Architecture Search (AAS) automates such design for text-domain agents, but has not
    been systematically evaluated on perceptual embodied agents through simulator rollouts. We study this transfer. We introduce
    AgentCanvas, a typed-graph runtime that hosts embodied executors as editable node-and-wire programs with simulator-aware
    execution and episode-level logs, and KDLoop, a coding-agent search procedure that cycles through proposal, critique,
    experiment, and distillation, with triggered reflection after stalls. We evaluate three AAS variants across four embodied
    executors spanning vision-language navigation, embodied question answering, and language-conditioned manipulation. The
    resulting 3x4 matrix shows that architecture-level search can produce deployable and directional success-rate gains on
    embodied tasks, while one apparent high-scoring candidate is rejected as leak-bearing. At the same time, the experiments
    expose constraints that are muted in text-domain AAS: optimization signals can be masked by rollout noise, search can
    become trapped in local edit basins, and episode-level credit assignment only partially emerges even when detailed logs
    are available. These results characterize both the promise and the current limits of automated architecture search for
    embodied agents.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- automating_the_design_of_embod
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.30111v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1017 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Automating the Design of Embodied Agent Architectures (arXiv)
  url: https://arxiv.org/abs/2606.30111
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
具身智能体通常由人工设计的感知、记忆、规划和动作模块组合而成，这种模块化设计暴露了巨大的架构空间，但当前系统仍依赖研究者直觉进行决策。本文首次系统性地将Agent Architecture Search（AAS）从文本域迁移至具身感知智能体，通过模拟器回滚进行评估。作者开发了AgentCanvas——一种类型化图运行时，将具身执行器封装为可编辑的节点-连线程序，支持模拟器感知执行和回合级日志；同时提出KDLoop搜索流程，通过提议、批评、实验和蒸馏的循环，并在停滞时触发反思。在涵盖视觉语言导航、具身问答和语言条件操作的四个执行器上，三种AAS变体的3x4评估矩阵显示，架构级搜索能带来可部署的方向性成功率提升，但一个高分候选被识别为存在信息泄露。实验同时揭示了文本域AAS中不明显的约束：优化信号可能被回滚噪声掩盖，搜索易陷入局部编辑盆地，即使有详细日志，回合级信用分配也仅部分实现。

## 核心内容
### 核心贡献
- **AgentCanvas**：类型化图运行时，将具身执行器表示为可编辑的节点-连线程序，支持模拟器感知执行和回合级日志记录。
- **KDLoop**：编码智能体搜索流程，包含提议、批评、实验和蒸馏四个阶段，并在搜索停滞时触发反思机制。

### 实验设置
- **评估矩阵**：3种AAS变体 × 4个具身执行器，覆盖三个任务领域：
  - 视觉语言导航（Vision-Language Navigation）
  - 具身问答（Embodied Question Answering）
  - 语言条件操作（Language-Conditioned Manipulation）
- **关键发现**：
  - 架构级搜索可产生可部署的成功率提升，且具有方向性
  - 一个看似高分候选被拒绝，因其存在信息泄露（leak-bearing）
- **暴露的约束**：
  - 优化信号可能被回滚噪声（rollout noise）掩盖
  - 搜索容易陷入局部编辑盆地（local edit basins）
  - 即使有详细日志，回合级信用分配（episode-level credit assignment）也仅部分实现

### 结论
这些结果刻画了自动化架构搜索在具身智能体中的前景与当前局限，表明从文本域到具身域的迁移面临独特的挑战，包括噪声鲁棒性、搜索空间探索和信用分配等问题。

## Overview
Embodied agents are typically built as hand-designed compositions of perception, memory, planning, and action modules. This modularity exposes a large architectural design space, but current systems still rely on researcher intuition to choose where information is stored, how observations are processed, and how model calls are connected. Agent Architecture Search (AAS) automates such design for text-domain agents, but has not been systematically evaluated on perceptual embodied agents through simulator rollouts. We study this transfer. We introduce AgentCanvas, a typed-graph runtime that hosts embodied executors as editable node-and-wire programs with simulator-aware execution and episode-level logs, and KDLoop, a coding-agent search procedure that cycles through proposal, critique, experiment, and distillation, with triggered reflection after stalls. We evaluate three AAS variants across four embodied executors spanning vision-language navigation, embodied question answering, and language-conditioned manipulation. The resulting 3x4 matrix shows that architecture-level search can produce deployable and directional success-rate gains on embodied tasks, while one apparent high-scoring candidate is rejected as leak-bearing. At the same time, the experiments expose constraints that are muted in text-domain AAS: optimization signals can be masked by rollout noise, search can become trapped in local edit basins, and episode-level credit assignment only partially emerges even when detailed logs are available. These results characterize both the promise and the current limits of automated architecture search for embodied agents.

## 参考
- http://arxiv.org/abs/2606.30111v2

## 개요
구현 지능 에이전트는 일반적으로 수동으로 설계된 인식, 기억, 계획 및 동작 모듈의 조합으로 구성됩니다. 이러한 모듈식 설계는 거대한 아키텍처 공간을 노출하지만, 현재 시스템은 여전히 연구자의 직관에 의존하여 결정을 내립니다. 본 논문은 처음으로 Agent Architecture Search(AAS)를 텍스트 도메인에서 구현 지각 에이전트로 체계적으로 이전하고, 시뮬레이터 롤백을 통해 평가합니다. 저자는 AgentCanvas——구현 실행기를 편집 가능한 노드-연결 프로그램으로 캡슐화하는 타입화된 그래프 런타임을 개발하여, 시뮬레이터 지각 실행 및 에피소드 수준 로그를 지원합니다. 동시에 KDLoop 검색 프로세스를 제안하며, 제안, 비판, 실험 및 증류의 순환을 통해 진행되고, 정체 시 반성을 트리거합니다. 시각 언어 내비게이션, 구현 질의응답 및 언어 조건 조작을 포함한 네 가지 실행기에서 세 가지 AAS 변형의 3x4 평가 매트릭스는 아키텍처 수준 검색이 배포 가능한 방향성 성공률 향상을 가져올 수 있음을 보여주지만, 높은 점수의 후보 중 하나가 정보 누출이 있는 것으로 식별되었습니다. 실험은 또한 텍스트 도메인 AAS에서는 명확하지 않은 제약을 드러냈습니다: 최적화 신호가 롤백 노이즈에 의해 가려질 수 있고, 검색이 로컬 편집 분지에 빠지기 쉬우며, 상세한 로그가 있어도 에피소드 수준 신용 할당은 부분적으로만 구현됩니다.

## 핵심 내용
### 핵심 기여
- **AgentCanvas**: 구현 실행기를 편집 가능한 노드-연결 프로그램으로 표현하는 타입화된 그래프 런타임으로, 시뮬레이터 지각 실행 및 에피소드 수준 로그 기록을 지원합니다.
- **KDLoop**: 제안, 비판, 실험 및 증류의 네 단계를 포함하는 에이전트 검색 프로세스를 인코딩하며, 검색 정체 시 반성 메커니즘을 트리거합니다.

### 실험 설정
- **평가 매트릭스**: 3가지 AAS 변형 × 4개의 구현 실행기, 세 가지 작업 영역을 포괄:
  - 시각 언어 내비게이션(Vision-Language Navigation)
  - 구현 질의응답(Embodied Question Answering)
  - 언어 조건 조작(Language-Conditioned Manipulation)
- **주요 발견**:
  - 아키텍처 수준 검색은 배포 가능한 성공률 향상을 생성할 수 있으며 방향성을 가집니다
  - 겉보기에 높은 점수의 후보 하나가 정보 누출(leak-bearing)로 인해 거부되었습니다
- **노출된 제약**:
  - 최적화 신호가 롤백 노이즈(rollout noise)에 의해 가려질 수 있습니다
  - 검색은 로컬 편집 분지(local edit basins)에 빠지기 쉽습니다
  - 상세한 로그가 있어도 에피소드 수준 신용 할당(episode-level credit assignment)은 부분적으로만 구현됩니다

### 결론
이러한 결과는 구현 지능 에이전트에서 자동화된 아키텍처 검색의 전망과 현재 한계를 특성화하며, 텍스트 도메인에서 구현 도메인으로의 이전이 노이즈 견고성, 검색 공간 탐색 및 신용 할당 문제를 포함한 독특한 도전에 직면함을 시사합니다.
