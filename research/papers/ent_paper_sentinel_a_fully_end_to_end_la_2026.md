---
$id: ent_paper_sentinel_a_fully_end_to_end_la_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control'
  zh: 端到端语言动作模型也绕不开机器人动力学数据
  ko: 'SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control'
summary:
  en: 'SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control is a knowledge node related to paper
    in the humanoid robot value chain.'
  zh: Existing humanoid control systems often rely on teleoperation or modular generation pipelines that separate language
    understanding from physical execution. However, the former is entirely human-driven, and the latter lacks tight alignment
    between language commands and physical behaviors. In this paper, we present SENTINEL, a fully end-to-end language-action
    model for humanoid whole-body control. We construct a large-scale dataset by tracking human motions in simulation using
    a pretrained whole body controller, combined with their text annotations. The model directly maps language commands and
    proprioceptive inputs to low-level actions without any intermediate representation. The model generates action chunks
    using flow matching, which can be subsequently refined by a residual action head f
  ko: 'SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control is a knowledge node related to paper
    in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- task_interface
- visual_closed_loop
- vla
- whole_body_control
- world_model
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19236v1.
sources:
- id: src_001
  type: paper
  title: 'SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control (arXiv)'
  url: https://arxiv.org/abs/2511.19236
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 端到端语言动作模型也绕不开机器人动力学数据 project page
  url: https://arxiv.org/abs/2511.19236
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Existing humanoid control systems often rely on teleoperation or modular generation pipelines that separate language understanding from physical execution. However, the former is entirely human-driven, and the latter lacks tight alignment between language commands and physical behaviors. In this paper, we present SENTINEL, a fully end-to-end language-action model for humanoid whole-body control. We construct a large-scale dataset by tracking human motions in simulation using a pretrained whole body controller, combined with their text annotations. The model directly maps language commands and proprioceptive inputs to low-level actions without any intermediate representation. The model generates action chunks using flow matching, which can be subsequently refined by a residual action head for real-world deployment. Our method exhibits strong semantic understanding and stable execution on humanoid robots in both simulation and real-world deployment, and also supports multi-modal extensions by converting inputs into texts.

## 核心内容
Existing humanoid control systems often rely on teleoperation or modular generation pipelines that separate language understanding from physical execution. However, the former is entirely human-driven, and the latter lacks tight alignment between language commands and physical behaviors. In this paper, we present SENTINEL, a fully end-to-end language-action model for humanoid whole-body control. We construct a large-scale dataset by tracking human motions in simulation using a pretrained whole body controller, combined with their text annotations. The model directly maps language commands and proprioceptive inputs to low-level actions without any intermediate representation. The model generates action chunks using flow matching, which can be subsequently refined by a residual action head for real-world deployment. Our method exhibits strong semantic understanding and stable execution on humanoid robots in both simulation and real-world deployment, and also supports multi-modal extensions by converting inputs into texts.

## 参考
- http://arxiv.org/abs/2511.19236v1

