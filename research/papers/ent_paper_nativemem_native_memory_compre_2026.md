---
$id: ent_paper_nativemem_native_memory_compre_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation'
  zh: 'NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation'
  ko: ''
summary:
  en: "arXiv:2607.06678v1 Announce Type: new \nAbstract: How can pretrained Vision-Language-Action\
    \ (VLA) models retain long-horizon visual histories with high-frequency updates\
    \ without sacrificing efficiency? Existing approaches rely on external memory\
    \ management, which restrains either the memory horizon or the reactiveness of\
    \ pretrained policies. To this end, we present NativeMEM, a VLA policy that features\
    \ long-term and real-time updated memory. At its core is an efficient memory encoding\
    \ scheme, Native Memory Compression, which repurposes the VLA's own vision encoder\
    \ to compress each historical frame from each camera view into a single token.\
    \ Appended to the input sequence, these memory tokens enable the pretrained VLA\
    \ to attend over long-term history with negligible latency overhead, requiring\
    \ neither an external planner nor a freshly initialized memory module. To align\
    \ the memory tokens with the pretrained policy, we first develop a generic memory\
    \ tokenizer under the supervision of a frozen VLA on memory-demanding data, and\
    \ then unfreeze the VLA for task-specific fine-tuning. NativeMEM consistently\
    \ outperforms prior methods, boosting success rates from 32.4% to 84.0% in simulation\
    \ and up to 98.7% on real robots, while maintaining low inference latency and\
    \ GPU memory usage. Notably, NativeMEM exhibits high data efficiency by achieving\
    \ competitive results with prior arts using only 20% of the training data."
  zh: "arXiv:2607.06678v1 Announce Type: new \nAbstract: How can pretrained Vision-Language-Action\
    \ (VLA) models retain long-horizon visual histories with high-frequency updates\
    \ without sacrificing efficiency? Existing approaches rely on external memory\
    \ management, which restrains either the memory horizon or the reactiveness of\
    \ pretrained policies. To this end, we present NativeMEM, a VLA policy that features\
    \ long-term and real-time updated memory. At its core is an efficient memory encoding\
    \ scheme, Native Memory Compression, which repurposes the VLA's own vision encoder\
    \ to compress each historical frame from each camera view into a single token.\
    \ Appended to the input sequence, these memory tokens enable the pretrained VLA\
    \ to attend over long-term history with negligible latency overhead, requiring\
    \ neither an external planner nor a freshly initialized memory module. To align\
    \ the memory tokens with the pretrained policy, we first develop a generic memory\
    \ tokenizer under the supervision of a frozen VLA on memory-demanding data, and\
    \ then unfreeze the VLA for task-specific fine-tuning. NativeMEM consistently\
    \ outperforms prior methods, boosting success rates from 32.4% to 84.0% in simulation\
    \ and up to 98.7% on real robots, while maintaining low inference latency and\
    \ GPU memory usage. Notably, NativeMEM exhibits high data efficiency by achieving\
    \ competitive results with prior arts using only 20% of the training data."
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
- nativemem
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-10'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation
    (arXiv)'
  url: https://arxiv.org/abs/2607.06678
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2607.06678v1 Announce Type: new 
Abstract: How can pretrained Vision-Language-Action (VLA) models retain long-horizon visual histories with high-frequency updates without sacrificing efficiency? Existing approaches rely on external memory management, which restrains either the memory horizon or the reactiveness of pretrained policies. To this end, we present NativeMEM, a VLA policy that features long-term and real-time updated memory. At its core is an efficient memory encoding scheme, Native Memory Compression, which repurposes the VLA's own vision encoder to compress each historical frame from each camera view into a single token. Appended to the input sequence, these memory tokens enable the pretrained VLA to attend over long-term history with negligible latency overhead, requiring neither an external planner nor a freshly initialized memory module. To align the memory tokens with the pretrained policy, we first develop a generic memory tokenizer under the supervision of a frozen VLA on memory-demanding data, and then unfreeze the VLA for task-specific fine-tuning. NativeMEM consistently outperforms prior methods, boosting success rates from 32.4% to 84.0% in simulation and up to 98.7% on real robots, while maintaining low inference latency and GPU memory usage. Notably, NativeMEM exhibits high data efficiency by achieving competitive results with prior arts using only 20% of the training data.
