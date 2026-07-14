---
$id: ent_paper_example_based_motion_synthesis_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Example-based Motion Synthesis via Generative Motion Matching
  zh: Example-based Motion Synthesis via Generative Motion Matching
  ko: Example-based Motion Synthesis via Generative Motion Matching
summary:
  en: Example-based Motion Synthesis via Generative Motion Matching is a 2023 work on human motion analysis and synthesis
    for humanoid robots.
  zh: Example-based Motion Synthesis via Generative Motion Matching is a 2023 work on human motion analysis and synthesis
    for humanoid robots.
  ko: Example-based Motion Synthesis via Generative Motion Matching is a 2023 work on human motion analysis and synthesis
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- example_based_motion_synthesis
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.00378v1.
sources:
- id: src_001
  type: paper
  title: Example-based Motion Synthesis via Generative Motion Matching (arXiv)
  url: https://arxiv.org/abs/2306.00378
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
We present GenMM, a generative model that "mines" as many diverse motions as possible from a single or few example sequences. In stark contrast to existing data-driven methods, which typically require long offline training time, are prone to visual artifacts, and tend to fail on large and complex skeletons, GenMM inherits the training-free nature and the superior quality of the well-known Motion Matching method. GenMM can synthesize a high-quality motion within a fraction of a second, even with highly complex and large skeletal structures. At the heart of our generative framework lies the generative motion matching module, which utilizes the bidirectional visual similarity as a generative cost function to motion matching, and operates in a multi-stage framework to progressively refine a random guess using exemplar motion matches. In addition to diverse motion generation, we show the versatility of our generative framework by extending it to a number of scenarios that are not possible with motion matching alone, including motion completion, key frame-guided generation, infinite looping, and motion reassembly. Code and data for this paper are at https://wyysf-98.github.io/GenMM/

## 核心内容
We present GenMM, a generative model that "mines" as many diverse motions as possible from a single or few example sequences. In stark contrast to existing data-driven methods, which typically require long offline training time, are prone to visual artifacts, and tend to fail on large and complex skeletons, GenMM inherits the training-free nature and the superior quality of the well-known Motion Matching method. GenMM can synthesize a high-quality motion within a fraction of a second, even with highly complex and large skeletal structures. At the heart of our generative framework lies the generative motion matching module, which utilizes the bidirectional visual similarity as a generative cost function to motion matching, and operates in a multi-stage framework to progressively refine a random guess using exemplar motion matches. In addition to diverse motion generation, we show the versatility of our generative framework by extending it to a number of scenarios that are not possible with motion matching alone, including motion completion, key frame-guided generation, infinite looping, and motion reassembly. Code and data for this paper are at https://wyysf-98.github.io/GenMM/

## 参考
- http://arxiv.org/abs/2306.00378v1

