---
$id: ent_paper_li_controlvla_few_shot_object_cen_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models'
  zh: ControlVLA
  ko: 'ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models'
summary:
  en: 'ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models (ControlVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Tsinghua University, State Key Lab of General
    Artiﬁcial Intelligence, BIGAI, Peking University, Astribot, and published at CoRL25.'
  zh: 'ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models (ControlVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Tsinghua University, State Key Lab of General
    Artiﬁcial Intelligence, BIGAI, Peking University, Astribot, and published at CoRL25.'
  ko: 'ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models (ControlVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Tsinghua University, State Key Lab of General
    Artiﬁcial Intelligence, BIGAI, Peking University, Astribot, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- controlvla
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.16211v1.
sources:
- id: src_001
  type: paper
  title: 'ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2506.16211
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ControlVLA source
  url: https://doi.org/10.48550/arXiv.2506.16211
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning real-world robotic manipulation is challenging, particularly when limited demonstrations are available. Existing methods for few-shot manipulation often rely on simulation-augmented data or pre-built modules like grasping and pose estimation, which struggle with sim-to-real gaps and lack extensibility. While large-scale imitation pre-training shows promise, adapting these general-purpose policies to specific tasks in data-scarce settings remains unexplored. To achieve this, we propose ControlVLA, a novel framework that bridges pre-trained VLA models with object-centric representations via a ControlNet-style architecture for efficient fine-tuning. Specifically, to introduce object-centric conditions without overwriting prior knowledge, ControlVLA zero-initializes a set of projection layers, allowing them to gradually adapt the pre-trained manipulation policies. In real-world experiments across 6 diverse tasks, including pouring cubes and folding clothes, our method achieves a 76.7% success rate while requiring only 10-20 demonstrations -- a significant improvement over traditional approaches that require more than 100 demonstrations to achieve comparable success. Additional experiments highlight ControlVLA's extensibility to long-horizon tasks and robustness to unseen objects and backgrounds.

## 核心内容
Learning real-world robotic manipulation is challenging, particularly when limited demonstrations are available. Existing methods for few-shot manipulation often rely on simulation-augmented data or pre-built modules like grasping and pose estimation, which struggle with sim-to-real gaps and lack extensibility. While large-scale imitation pre-training shows promise, adapting these general-purpose policies to specific tasks in data-scarce settings remains unexplored. To achieve this, we propose ControlVLA, a novel framework that bridges pre-trained VLA models with object-centric representations via a ControlNet-style architecture for efficient fine-tuning. Specifically, to introduce object-centric conditions without overwriting prior knowledge, ControlVLA zero-initializes a set of projection layers, allowing them to gradually adapt the pre-trained manipulation policies. In real-world experiments across 6 diverse tasks, including pouring cubes and folding clothes, our method achieves a 76.7% success rate while requiring only 10-20 demonstrations -- a significant improvement over traditional approaches that require more than 100 demonstrations to achieve comparable success. Additional experiments highlight ControlVLA's extensibility to long-horizon tasks and robustness to unseen objects and backgrounds.

## 参考
- http://arxiv.org/abs/2506.16211v1

