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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.30111v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
임베디드 에이전트는 일반적으로 지각, 기억, 계획 및 행동 모듈을 수동으로 설계한 조합으로 구축됩니다. 이러한 모듈성은 방대한 아키텍처 설계 공간을 제공하지만, 현재 시스템은 여전히 연구자의 직관에 의존하여 정보 저장 위치, 관찰 처리 방식, 모델 호출 연결 방법을 결정합니다. 에이전트 아키텍처 탐색(AAS)은 텍스트 도메인 에이전트를 위한 이러한 설계를 자동화하지만, 시뮬레이터 롤아웃을 통한 지각적 임베디드 에이전트에 대한 체계적 평가는 이루어지지 않았습니다. 우리는 이러한 전이를 연구합니다. AgentCanvas를 소개합니다. 이는 편집 가능한 노드-와이어 프로그램으로 임베디드 실행기를 호스팅하며, 시뮬레이터 인식 실행과 에피소드 수준 로그를 제공하는 타입 그래프 런타임입니다. 또한 KDLoop는 제안, 비평, 실험 및 증류를 순환하고 정체 시 트리거된 반성을 포함하는 코딩 에이전트 탐색 절차입니다. 우리는 시각-언어 내비게이션, 임베디드 질문 응답 및 언어 조건 조작을 포괄하는 네 가지 임베디드 실행기에서 세 가지 AAS 변형을 평가합니다. 결과 3x4 행렬은 아키텍처 수준 탐색이 임베디드 작업에서 배포 가능하고 방향성 있는 성공률 향상을 생성할 수 있음을 보여주지만, 한 명백히 높은 점수의 후보는 누출이 있는 것으로 기각됩니다. 동시에 실험은 텍스트 도메인 AAS에서 약화된 제약 조건을 드러냅니다: 최적화 신호가 롤아웃 노이즈에 의해 가려질 수 있고, 탐색이 로컬 편집 분지에 갇힐 수 있으며, 상세 로그가 제공되어도 에피소드 수준 신용 할당이 부분적으로만 나타납니다. 이러한 결과는 임베디드 에이전트를 위한 자동 아키텍처 탐색의 가능성과 현재 한계를 특성화합니다.

## 핵심 내용
임베디드 에이전트는 일반적으로 지각, 기억, 계획 및 행동 모듈을 수동으로 설계한 조합으로 구축됩니다. 이러한 모듈성은 방대한 아키텍처 설계 공간을 제공하지만, 현재 시스템은 여전히 연구자의 직관에 의존하여 정보 저장 위치, 관찰 처리 방식, 모델 호출 연결 방법을 결정합니다. 에이전트 아키텍처 탐색(AAS)은 텍스트 도메인 에이전트를 위한 이러한 설계를 자동화하지만, 시뮬레이터 롤아웃을 통한 지각적 임베디드 에이전트에 대한 체계적 평가는 이루어지지 않았습니다. 우리는 이러한 전이를 연구합니다. AgentCanvas를 소개합니다. 이는 편집 가능한 노드-와이어 프로그램으로 임베디드 실행기를 호스팅하며, 시뮬레이터 인식 실행과 에피소드 수준 로그를 제공하는 타입 그래프 런타임입니다. 또한 KDLoop는 제안, 비평, 실험 및 증류를 순환하고 정체 시 트리거된 반성을 포함하는 코딩 에이전트 탐색 절차입니다. 우리는 시각-언어 내비게이션, 임베디드 질문 응답 및 언어 조건 조작을 포괄하는 네 가지 임베디드 실행기에서 세 가지 AAS 변형을 평가합니다. 결과 3x4 행렬은 아키텍처 수준 탐색이 임베디드 작업에서 배포 가능하고 방향성 있는 성공률 향상을 생성할 수 있음을 보여주지만, 한 명백히 높은 점수의 후보는 누출이 있는 것으로 기각됩니다. 동시에 실험은 텍스트 도메인 AAS에서 약화된 제약 조건을 드러냅니다: 최적화 신호가 롤아웃 노이즈에 의해 가려질 수 있고, 탐색이 로컬 편집 분지에 갇힐 수 있으며, 상세 로그가 제공되어도 에피소드 수준 신용 할당이 부분적으로만 나타납니다. 이러한 결과는 임베디드 에이전트를 위한 자동 아키텍처 탐색의 가능성과 현재 한계를 특성화합니다.

## 参考
- http://arxiv.org/abs/2606.30111v2
