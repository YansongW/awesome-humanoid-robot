---
$id: ent_paper_training_vision_language_actio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought
    Supervision
  zh: Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought
    Supervision
  ko: ''
summary:
  en: "arXiv:2606.30552v2 Announce Type: replace \nAbstract: Cross-embodiment transfer\
    \ in vision-language-action (VLA) models remains challenging because low-level\
    \ state and action spaces differ fundamentally across robot platforms. We observe\
    \ that the high-level cognitive process underlying manipulation, including scene\
    \ perception, object identification, task planning, and sub-task decomposition,\
    \ is largely shared across embodiments. Based on this observation, we present\
    \ ZR-0, a 2.6 billion parameter end-to-end VLA model that uses dense Embodied\
    \ Chain-of-Thought (ECoT) supervision to align cross-embodiment representations\
    \ within the vision-language model (VLM). ZR-0 adopts a dual-stream architecture:\
    \ a pre-trained VLM (System 2) generates structured ECoT reasoning during training,\
    \ while a Diffusion Transformer-based action expert (System 1) produces continuous\
    \ action chunks via flow matching. The two components are coupled through cross-attention,\
    \ with an attention mask that restricts the action expert to input prompt features\
    \ only, enabling ECoT generation to be entirely skipped at inference without any\
    \ performance loss. ZR-0 is pre-trained on ProcCorpus-60M, a large-scale dataset\
    \ comprising approximately 60 million frames (approximately 1,000 hours) from\
    \ over 400K trajectories, with dense ECoT annotations covering 96.8% of all frames.\
    \ We evaluate ZR-0 on three simulation benchmarks spanning single-arm (LIBERO),\
    \ bimanual (RoboTwin 2.0), and humanoid (RoboCasa GR-1 Tabletop) embodiments,\
    \ as well as real-world experiments on the xArm platform, demonstrating strong\
    \ performance across all settings. Code and model checkpoints are available at\
    \ https://github.com/RUCKBReasoning/ZR-0."
  zh: "arXiv:2606.30552v2 Announce Type: replace \nAbstract: Cross-embodiment transfer\
    \ in vision-language-action (VLA) models remains challenging because low-level\
    \ state and action spaces differ fundamentally across robot platforms. We observe\
    \ that the high-level cognitive process underlying manipulation, including scene\
    \ perception, object identification, task planning, and sub-task decomposition,\
    \ is largely shared across embodiments. Based on this observation, we present\
    \ ZR-0, a 2.6 billion parameter end-to-end VLA model that uses dense Embodied\
    \ Chain-of-Thought (ECoT) supervision to align cross-embodiment representations\
    \ within the vision-language model (VLM). ZR-0 adopts a dual-stream architecture:\
    \ a pre-trained VLM (System 2) generates structured ECoT reasoning during training,\
    \ while a Diffusion Transformer-based action expert (System 1) produces continuous\
    \ action chunks via flow matching. The two components are coupled through cross-attention,\
    \ with an attention mask that restricts the action expert to input prompt features\
    \ only, enabling ECoT generation to be entirely skipped at inference without any\
    \ performance loss. ZR-0 is pre-trained on ProcCorpus-60M, a large-scale dataset\
    \ comprising approximately 60 million frames (approximately 1,000 hours) from\
    \ over 400K trajectories, with dense ECoT annotations covering 96.8% of all frames.\
    \ We evaluate ZR-0 on three simulation benchmarks spanning single-arm (LIBERO),\
    \ bimanual (RoboTwin 2.0), and humanoid (RoboCasa GR-1 Tabletop) embodiments,\
    \ as well as real-world experiments on the xArm platform, demonstrating strong\
    \ performance across all settings. Code and model checkpoints are available at\
    \ https://github.com/RUCKBReasoning/ZR-0."
  ko: ''
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
- training_vision_language_actio
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-03'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought
    Supervision (arXiv)
  url: https://arxiv.org/abs/2606.30552
  date: '2026'
  accessed_at: '2026-07-03'
---

arXiv:2606.30552v2 Announce Type: replace 
Abstract: Cross-embodiment transfer in vision-language-action (VLA) models remains challenging because low-level state and action spaces differ fundamentally across robot platforms. We observe that the high-level cognitive process underlying manipulation, including scene perception, object identification, task planning, and sub-task decomposition, is largely shared across embodiments. Based on this observation, we present ZR-0, a 2.6 billion parameter end-to-end VLA model that uses dense Embodied Chain-of-Thought (ECoT) supervision to align cross-embodiment representations within the vision-language model (VLM). ZR-0 adopts a dual-stream architecture: a pre-trained VLM (System 2) generates structured ECoT reasoning during training, while a Diffusion Transformer-based action expert (System 1) produces continuous action chunks via flow matching. The two components are coupled through cross-attention, with an attention mask that restricts the action expert to input prompt features only, enabling ECoT generation to be entirely skipped at inference without any performance loss. ZR-0 is pre-trained on ProcCorpus-60M, a large-scale dataset comprising approximately 60 million frames (approximately 1,000 hours) from over 400K trajectories, with dense ECoT annotations covering 96.8% of all frames. We evaluate ZR-0 on three simulation benchmarks spanning single-arm (LIBERO), bimanual (RoboTwin 2.0), and humanoid (RoboCasa GR-1 Tabletop) embodiments, as well as real-world experiments on the xArm platform, demonstrating strong performance across all settings. Code and model checkpoints are available at https://github.com/RUCKBReasoning/ZR-0.
