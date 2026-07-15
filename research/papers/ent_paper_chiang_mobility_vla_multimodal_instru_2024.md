---
$id: ent_paper_chiang_mobility_vla_multimodal_instru_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs'
  zh: Mobility VLA
  ko: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs'
summary:
  en: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs (Mobility VLA), is a
    2024 large vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL24.'
  zh: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs (Mobility VLA), is a
    2024 large vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL24.'
  ko: 'Mobility VLA: Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs (Mobility VLA), is a
    2024 large vision-language-action model for robotic manipulation, introduced by Google DeepMind, and published at CoRL24.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- mobility_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.07775v2.
sources:
- id: src_001
  type: paper
  title: Mobility VLA source
  url: https://proceedings.mlr.press/v270/xu25b.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
An elusive goal in navigation research is to build an intelligent agent that can understand multimodal instructions including natural language and image, and perform useful navigation. To achieve this, we study a widely useful category of navigation tasks we call Multimodal Instruction Navigation with demonstration Tours (MINT), in which the environment prior is provided through a previously recorded demonstration video. Recent advances in Vision Language Models (VLMs) have shown a promising path in achieving this goal as it demonstrates capabilities in perceiving and reasoning about multimodal inputs. However, VLMs are typically trained to predict textual output and it is an open research question about how to best utilize them in navigation. To solve MINT, we present Mobility VLA, a hierarchical Vision-Language-Action (VLA) navigation policy that combines the environment understanding and common sense reasoning power of long-context VLMs and a robust low-level navigation policy based on topological graphs. The high-level policy consists of a long-context VLM that takes the demonstration tour video and the multimodal user instruction as input to find the goal frame in the tour video. Next, a low-level policy uses the goal frame and an offline constructed topological graph to generate robot actions at every timestep. We evaluated Mobility VLA in a 836m^2 real world environment and show that Mobility VLA has a high end-to-end success rates on previously unsolved multimodal instructions such as "Where should I return this?" while holding a plastic bin. A video demonstrating Mobility VLA can be found here: https://youtu.be/-Tof__Q8_5s

## 核心内容
An elusive goal in navigation research is to build an intelligent agent that can understand multimodal instructions including natural language and image, and perform useful navigation. To achieve this, we study a widely useful category of navigation tasks we call Multimodal Instruction Navigation with demonstration Tours (MINT), in which the environment prior is provided through a previously recorded demonstration video. Recent advances in Vision Language Models (VLMs) have shown a promising path in achieving this goal as it demonstrates capabilities in perceiving and reasoning about multimodal inputs. However, VLMs are typically trained to predict textual output and it is an open research question about how to best utilize them in navigation. To solve MINT, we present Mobility VLA, a hierarchical Vision-Language-Action (VLA) navigation policy that combines the environment understanding and common sense reasoning power of long-context VLMs and a robust low-level navigation policy based on topological graphs. The high-level policy consists of a long-context VLM that takes the demonstration tour video and the multimodal user instruction as input to find the goal frame in the tour video. Next, a low-level policy uses the goal frame and an offline constructed topological graph to generate robot actions at every timestep. We evaluated Mobility VLA in a 836m^2 real world environment and show that Mobility VLA has a high end-to-end success rates on previously unsolved multimodal instructions such as "Where should I return this?" while holding a plastic bin. A video demonstrating Mobility VLA can be found here: https://youtu.be/-Tof__Q8_5s

## 参考
- http://arxiv.org/abs/2407.07775v2

