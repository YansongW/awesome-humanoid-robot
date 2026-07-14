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
  en: "arXiv:2606.30111v2 Announce Type: replace \nAbstract: Embodied agents are typically built as hand-designed compositions\
    \ of perception, memory, planning, and action modules. This modularity exposes a large architectural design space, but\
    \ current systems still rely on researcher intuition to choose where information is stored, how observations are processed,\
    \ and how model calls are connected. Agent Architecture Search (AAS) automates such design for text-domain agents, but\
    \ has not been systematically evaluated on perceptual embodied agents through simulator rollouts. We study this transfer.\
    \ We introduce AgentCanvas, a typed-graph runtime that hosts embodied executors as editable node-and-wire programs with\
    \ simulator-aware execution and episode-level logs, and KDLoop, a coding-agent search procedure that cycles through proposal,\
    \ critique, experiment, and distillation, with triggered reflection after stalls. We evaluate three AAS variants across\
    \ four embodied executors spanning vision-language navigation, embodied question answering, and language-conditioned manipulation.\
    \ The resulting 3x4 matrix shows that architecture-level search can produce deployable and directional success-rate gains\
    \ on embodied tasks, while one apparent high-scoring candidate is rejected as leak-bearing. At the same time, the experiments\
    \ expose constraints that are muted in text-domain AAS: optimization signals can be masked by rollout noise, search can\
    \ become trapped in local edit basins, and episode-level credit assignment only partially emerges even when detailed logs\
    \ are available. These results characterize both the promise and the current limits of automated architecture search for\
    \ embodied agents."
  zh: "arXiv:2606.30111v2 Announce Type: replace \nAbstract: Embodied agents are typically built as hand-designed compositions\
    \ of perception, memory, planning, and action modules. This modularity exposes a large architectural design space, but\
    \ current systems still rely on researcher intuition to choose where information is stored, how observations are processed,\
    \ and how model calls are connected. Agent Architecture Search (AAS) automates such design for text-domain agents, but\
    \ has not been systematically evaluated on perceptual embodied agents through simulator rollouts. We study this transfer.\
    \ We introduce AgentCanvas, a typed-graph runtime that hosts embodied executors as editable node-and-wire programs with\
    \ simulator-aware execution and episode-level logs, and KDLoop, a coding-agent search procedure that cycles through proposal,\
    \ critique, experiment, and distillation, with triggered reflection after stalls. We evaluate three AAS variants across\
    \ four embodied executors spanning vision-language navigation, embodied question answering, and language-conditioned manipulation.\
    \ The resulting 3x4 matrix shows that architecture-level search can produce deployable and directional success-rate gains\
    \ on embodied tasks, while one apparent high-scoring candidate is rejected as leak-bearing. At the same time, the experiments\
    \ expose constraints that are muted in text-domain AAS: optimization signals can be masked by rollout noise, search can\
    \ become trapped in local edit basins, and episode-level credit assignment only partially emerges even when detailed logs\
    \ are available. These results characterize both the promise and the current limits of automated architecture search for\
    \ embodied agents."
  ko: "arXiv:2606.30111v2 Announce Type: replace \nAbstract: Embodied agents are typically built as hand-designed compositions\
    \ of perception, memory, planning, and action modules. This modularity exposes a large architectural design space, but\
    \ current systems still rely on researcher intuition to choose where information is stored, how observations are processed,\
    \ and how model calls are connected. Agent Architecture Search (AAS) automates such design for text-domain agents, but\
    \ has not been systematically evaluated on perceptual embodied agents through simulator rollouts. We study this transfer.\
    \ We introduce AgentCanvas, a typed-graph runtime that hosts embodied executors as editable node-and-wire programs with\
    \ simulator-aware execution and episode-level logs, and KDLoop, a coding-agent search procedure that cycles through proposal,\
    \ critique, experiment, and distillation, with triggered reflection after stalls. We evaluate three AAS variants across\
    \ four embodied executors spanning vision-language navigation, embodied question answering, and language-conditioned manipulation.\
    \ The resulting 3x4 matrix shows that architecture-level search can produce deployable and directional success-rate gains\
    \ on embodied tasks, while one apparent high-scoring candidate is rejected as leak-bearing. At the same time, the experiments\
    \ expose constraints that are muted in text-domain AAS: optimization signals can be masked by rollout noise, search can\
    \ become trapped in local edit basins, and episode-level credit assignment only partially emerges even when detailed logs\
    \ are available. These results characterize both the promise and the current limits of automated architecture search for\
    \ embodied agents."
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

