---
$id: ent_paper_zerowbc_learning_natural_visuo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video'
  zh: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video'
  ko: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video'
summary:
  en: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video is a 2026 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- loco_manipulation
- whole_body_control
- zerowbc
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.09170v3.
sources:
- id: src_001
  type: paper
  title: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video (arXiv)'
  url: https://arxiv.org/abs/2603.09170
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video project page'
  url: https://zerowbc.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Achieving versatile and natural whole-body humanoid interaction control remains challenging due to the high cost of whole-body teleoperation data. We present ZeroWBC, a teleoperation-free framework that learns humanoid whole-body interaction from human egocentric videos paired with synchronized whole-body motion and text annotations. ZeroWBC adopts a generation-then-tracking formulation to tackle the static scene whole-body interaction control problem. Given an initial egocentric image and a language instruction, a fine-tuned Vision-Language Model generates future human whole-body motion tokens, which are decoded into continuous motions and retargeted to the humanoid. The resulting reference motions, together with root and key body-part trajectories, are then executed by a general interactive motion tracking policy. To improve interaction performance, we introduce an interaction-oriented tracking reward that prioritizes global root and key body-part trajectory alignment while preserving natural whole-body motion. Experiments on the Unitree G1 humanoid robot show that ZeroWBC enables diverse scene-aware behaviors without robot teleoperation demonstrations. These results suggest a scalable paradigm for learning natural humanoid whole-body interaction from human egocentric data.

## 核心内容
Achieving versatile and natural whole-body humanoid interaction control remains challenging due to the high cost of whole-body teleoperation data. We present ZeroWBC, a teleoperation-free framework that learns humanoid whole-body interaction from human egocentric videos paired with synchronized whole-body motion and text annotations. ZeroWBC adopts a generation-then-tracking formulation to tackle the static scene whole-body interaction control problem. Given an initial egocentric image and a language instruction, a fine-tuned Vision-Language Model generates future human whole-body motion tokens, which are decoded into continuous motions and retargeted to the humanoid. The resulting reference motions, together with root and key body-part trajectories, are then executed by a general interactive motion tracking policy. To improve interaction performance, we introduce an interaction-oriented tracking reward that prioritizes global root and key body-part trajectory alignment while preserving natural whole-body motion. Experiments on the Unitree G1 humanoid robot show that ZeroWBC enables diverse scene-aware behaviors without robot teleoperation demonstrations. These results suggest a scalable paradigm for learning natural humanoid whole-body interaction from human egocentric data.

## 参考
- http://arxiv.org/abs/2603.09170v3

