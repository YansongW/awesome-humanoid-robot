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
  zh: 'arXiv:2606.30111v2 Announce Type: replace Abstract: Embodied agents are typically built as hand-designed compositions
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.30111v2.
sources:
- id: src_001
  type: paper
  title: Automating the Design of Embodied Agent Architectures (arXiv)
  url: https://arxiv.org/abs/2606.30111
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Embodied agents are typically built as hand-designed compositions of perception, memory, planning, and action modules. This modularity exposes a large architectural design space, but current systems still rely on researcher intuition to choose where information is stored, how observations are processed, and how model calls are connected. Agent Architecture Search (AAS) automates such design for text-domain agents, but has not been systematically evaluated on perceptual embodied agents through simulator rollouts. We study this transfer. We introduce AgentCanvas, a typed-graph runtime that hosts embodied executors as editable node-and-wire programs with simulator-aware execution and episode-level logs, and KDLoop, a coding-agent search procedure that cycles through proposal, critique, experiment, and distillation, with triggered reflection after stalls. We evaluate three AAS variants across four embodied executors spanning vision-language navigation, embodied question answering, and language-conditioned manipulation. The resulting 3x4 matrix shows that architecture-level search can produce deployable and directional success-rate gains on embodied tasks, while one apparent high-scoring candidate is rejected as leak-bearing. At the same time, the experiments expose constraints that are muted in text-domain AAS: optimization signals can be masked by rollout noise, search can become trapped in local edit basins, and episode-level credit assignment only partially emerges even when detailed logs are available. These results characterize both the promise and the current limits of automated architecture search for embodied agents.

## 核心内容
Embodied agents are typically built as hand-designed compositions of perception, memory, planning, and action modules. This modularity exposes a large architectural design space, but current systems still rely on researcher intuition to choose where information is stored, how observations are processed, and how model calls are connected. Agent Architecture Search (AAS) automates such design for text-domain agents, but has not been systematically evaluated on perceptual embodied agents through simulator rollouts. We study this transfer. We introduce AgentCanvas, a typed-graph runtime that hosts embodied executors as editable node-and-wire programs with simulator-aware execution and episode-level logs, and KDLoop, a coding-agent search procedure that cycles through proposal, critique, experiment, and distillation, with triggered reflection after stalls. We evaluate three AAS variants across four embodied executors spanning vision-language navigation, embodied question answering, and language-conditioned manipulation. The resulting 3x4 matrix shows that architecture-level search can produce deployable and directional success-rate gains on embodied tasks, while one apparent high-scoring candidate is rejected as leak-bearing. At the same time, the experiments expose constraints that are muted in text-domain AAS: optimization signals can be masked by rollout noise, search can become trapped in local edit basins, and episode-level credit assignment only partially emerges even when detailed logs are available. These results characterize both the promise and the current limits of automated architecture search for embodied agents.

## 参考
- http://arxiv.org/abs/2606.30111v2

## Overview
Embodied agents are typically built as hand-designed compositions of perception, memory, planning, and action modules. This modularity exposes a large architectural design space, but current systems still rely on researcher intuition to choose where information is stored, how observations are processed, and how model calls are connected. Agent Architecture Search (AAS) automates such design for text-domain agents, but has not been systematically evaluated on perceptual embodied agents through simulator rollouts. We study this transfer. We introduce AgentCanvas, a typed-graph runtime that hosts embodied executors as editable node-and-wire programs with simulator-aware execution and episode-level logs, and KDLoop, a coding-agent search procedure that cycles through proposal, critique, experiment, and distillation, with triggered reflection after stalls. We evaluate three AAS variants across four embodied executors spanning vision-language navigation, embodied question answering, and language-conditioned manipulation. The resulting 3x4 matrix shows that architecture-level search can produce deployable and directional success-rate gains on embodied tasks, while one apparent high-scoring candidate is rejected as leak-bearing. At the same time, the experiments expose constraints that are muted in text-domain AAS: optimization signals can be masked by rollout noise, search can become trapped in local edit basins, and episode-level credit assignment only partially emerges even when detailed logs are available. These results characterize both the promise and the current limits of automated architecture search for embodied agents.

## Content
Embodied agents are typically built as hand-designed compositions of perception, memory, planning, and action modules. This modularity exposes a large architectural design space, but current systems still rely on researcher intuition to choose where information is stored, how observations are processed, and how model calls are connected. Agent Architecture Search (AAS) automates such design for text-domain agents, but has not been systematically evaluated on perceptual embodied agents through simulator rollouts. We study this transfer. We introduce AgentCanvas, a typed-graph runtime that hosts embodied executors as editable node-and-wire programs with simulator-aware execution and episode-level logs, and KDLoop, a coding-agent search procedure that cycles through proposal, critique, experiment, and distillation, with triggered reflection after stalls. We evaluate three AAS variants across four embodied executors spanning vision-language navigation, embodied question answering, and language-conditioned manipulation. The resulting 3x4 matrix shows that architecture-level search can produce deployable and directional success-rate gains on embodied tasks, while one apparent high-scoring candidate is rejected as leak-bearing. At the same time, the experiments expose constraints that are muted in text-domain AAS: optimization signals can be masked by rollout noise, search can become trapped in local edit basins, and episode-level credit assignment only partially emerges even when detailed logs are available. These results characterize both the promise and the current limits of automated architecture search for embodied agents.

## 개요
임베디드 에이전트는 일반적으로 지각, 기억, 계획 및 행동 모듈을 수동으로 설계한 조합으로 구축됩니다. 이러한 모듈성은 방대한 아키텍처 설계 공간을 제공하지만, 현재 시스템은 여전히 연구자의 직관에 의존하여 정보 저장 위치, 관찰 처리 방식, 모델 호출 연결 방법을 결정합니다. 에이전트 아키텍처 탐색(AAS)은 텍스트 도메인 에이전트를 위한 이러한 설계를 자동화하지만, 시뮬레이터 롤아웃을 통한 지각적 임베디드 에이전트에 대한 체계적 평가는 이루어지지 않았습니다. 우리는 이러한 전이를 연구합니다. AgentCanvas를 소개합니다. 이는 편집 가능한 노드-와이어 프로그램으로 임베디드 실행기를 호스팅하며, 시뮬레이터 인식 실행과 에피소드 수준 로그를 제공하는 타입 그래프 런타임입니다. 또한 KDLoop는 제안, 비평, 실험 및 증류를 순환하고 정체 시 트리거된 반성을 포함하는 코딩 에이전트 탐색 절차입니다. 우리는 시각-언어 내비게이션, 임베디드 질문 응답 및 언어 조건 조작을 포괄하는 네 가지 임베디드 실행기에서 세 가지 AAS 변형을 평가합니다. 결과 3x4 행렬은 아키텍처 수준 탐색이 임베디드 작업에서 배포 가능하고 방향성 있는 성공률 향상을 생성할 수 있음을 보여주지만, 한 명백히 높은 점수의 후보는 누출이 있는 것으로 기각됩니다. 동시에 실험은 텍스트 도메인 AAS에서 약화된 제약 조건을 드러냅니다: 최적화 신호가 롤아웃 노이즈에 의해 가려질 수 있고, 탐색이 로컬 편집 분지에 갇힐 수 있으며, 상세 로그가 제공되어도 에피소드 수준 신용 할당이 부분적으로만 나타납니다. 이러한 결과는 임베디드 에이전트를 위한 자동 아키텍처 탐색의 가능성과 현재 한계를 특성화합니다.

## 핵심 내용
임베디드 에이전트는 일반적으로 지각, 기억, 계획 및 행동 모듈을 수동으로 설계한 조합으로 구축됩니다. 이러한 모듈성은 방대한 아키텍처 설계 공간을 제공하지만, 현재 시스템은 여전히 연구자의 직관에 의존하여 정보 저장 위치, 관찰 처리 방식, 모델 호출 연결 방법을 결정합니다. 에이전트 아키텍처 탐색(AAS)은 텍스트 도메인 에이전트를 위한 이러한 설계를 자동화하지만, 시뮬레이터 롤아웃을 통한 지각적 임베디드 에이전트에 대한 체계적 평가는 이루어지지 않았습니다. 우리는 이러한 전이를 연구합니다. AgentCanvas를 소개합니다. 이는 편집 가능한 노드-와이어 프로그램으로 임베디드 실행기를 호스팅하며, 시뮬레이터 인식 실행과 에피소드 수준 로그를 제공하는 타입 그래프 런타임입니다. 또한 KDLoop는 제안, 비평, 실험 및 증류를 순환하고 정체 시 트리거된 반성을 포함하는 코딩 에이전트 탐색 절차입니다. 우리는 시각-언어 내비게이션, 임베디드 질문 응답 및 언어 조건 조작을 포괄하는 네 가지 임베디드 실행기에서 세 가지 AAS 변형을 평가합니다. 결과 3x4 행렬은 아키텍처 수준 탐색이 임베디드 작업에서 배포 가능하고 방향성 있는 성공률 향상을 생성할 수 있음을 보여주지만, 한 명백히 높은 점수의 후보는 누출이 있는 것으로 기각됩니다. 동시에 실험은 텍스트 도메인 AAS에서 약화된 제약 조건을 드러냅니다: 최적화 신호가 롤아웃 노이즈에 의해 가려질 수 있고, 탐색이 로컬 편집 분지에 갇힐 수 있으며, 상세 로그가 제공되어도 에피소드 수준 신용 할당이 부분적으로만 나타납니다. 이러한 결과는 임베디드 에이전트를 위한 자동 아키텍처 탐색의 가능성과 현재 한계를 특성화합니다.
