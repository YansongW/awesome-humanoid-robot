---
$id: ent_paper_liu_trivla_a_triple_system_based_u_0
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control'
  zh: TriVLA
  ko: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control'
summary:
  en: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control (TriVLA), is a 0 large
    vision-language-action model for robotic manipulation, introduced by Fudan University, Shanghai Innovation Institute.'
  zh: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control (TriVLA), is a 0 large
    vision-language-action model for robotic manipulation, introduced by Fudan University, Shanghai Innovation Institute.'
  ko: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control (TriVLA), is a 0 large
    vision-language-action model for robotic manipulation, introduced by Fudan University, Shanghai Innovation Institute.'
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
- robotic_manipulation
- trivla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.01424v3.
sources:
- id: src_001
  type: paper
  title: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control (arXiv)'
  url: https://arxiv.org/abs/2507.01424
  date: '0'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TriVLA source
  url: https://doi.org/10.48550/arXiv.2507.01424
  date: '0'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in vision-language models (VLMs) have enabled robots to follow open-ended instructions and demonstrate impressive commonsense reasoning. However, current vision-language-action (VLA) frameworks primarily rely on static representations and limited temporal context, restricting agents to short-horizon, reactive behaviors and hindering robust generalization in dynamic embodied environments. Inspired by cognitive neuroscience theories of episodic memory, we propose, to our knowledge, one of the first formalized episodic world models in VLA, enabling embodied robots to accumulate, recall, and predict sequential experiences. As an instantiation of this concept, our unified TriVLA realizes the episodic world model through a triple-system architecture: integrating multimodal grounding from a pretrained VLM (System 2) and temporally rich dynamics perception from a video diffusion model (System 3). This enables the agent to accumulate and recall sequential experiences, interpret current contexts, and predict future environmental evolution. Guided by episodic representations that span both the past and anticipated future, the downstream policy (System 1) generates coherent, context-aware action sequences through flow-matching and cross-modal attention mechanisms. Experimental results show that TriVLA operates efficiently at approximately 36 Hz and consistently outperforms baseline models on standard benchmarks and challenging real-world manipulation tasks. It demonstrates strong long-horizon planning and open-ended intent understanding, showcasing the advantages of episodic world model-inspired reasoning for robust, generalizable robot intelligence. Project Page: https://zhenyangliu.github.io/TriVLA/.

## 核心内容
Recent advances in vision-language models (VLMs) have enabled robots to follow open-ended instructions and demonstrate impressive commonsense reasoning. However, current vision-language-action (VLA) frameworks primarily rely on static representations and limited temporal context, restricting agents to short-horizon, reactive behaviors and hindering robust generalization in dynamic embodied environments. Inspired by cognitive neuroscience theories of episodic memory, we propose, to our knowledge, one of the first formalized episodic world models in VLA, enabling embodied robots to accumulate, recall, and predict sequential experiences. As an instantiation of this concept, our unified TriVLA realizes the episodic world model through a triple-system architecture: integrating multimodal grounding from a pretrained VLM (System 2) and temporally rich dynamics perception from a video diffusion model (System 3). This enables the agent to accumulate and recall sequential experiences, interpret current contexts, and predict future environmental evolution. Guided by episodic representations that span both the past and anticipated future, the downstream policy (System 1) generates coherent, context-aware action sequences through flow-matching and cross-modal attention mechanisms. Experimental results show that TriVLA operates efficiently at approximately 36 Hz and consistently outperforms baseline models on standard benchmarks and challenging real-world manipulation tasks. It demonstrates strong long-horizon planning and open-ended intent understanding, showcasing the advantages of episodic world model-inspired reasoning for robust, generalizable robot intelligence. Project Page: https://zhenyangliu.github.io/TriVLA/.

## 参考
- http://arxiv.org/abs/2507.01424v3

