---
$id: ent_paper_training_and_evaluating_diffus_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Training and Evaluating Diffusion Policies with Long Context Lengths
  zh: Training and Evaluating Diffusion Policies with Long Context Lengths
  ko: ''
summary:
  en: "arXiv:2606.16447v2 Announce Type: replace \nAbstract: Imitation learning has\
    \ enabled highly-dexterous robotic manipulation from RGB observations. Policies\
    \ trained with these methods, however, typically condition robot actions on only\
    \ a short history of observations. These policies cannot solve tasks that require\
    \ memory and can get stuck repeatedly executing the same failing motions. In this\
    \ work, we first benchmark policy performance as context length is incrementally\
    \ increased from short to long, across a spectrum of tasks with varying local\
    \ stability and memory requirements, and in multiple data regimes. To our knowledge,\
    \ this is the first study to investigate context length for Diffusion Policies\
    \ at this level of detail. Our results challenge prior claims: naively scaling\
    \ context length is not as brittle as advertised in literature. With an appropriate\
    \ conditioning method and denoising backbone (UNet+Cross-Attention), single-task\
    \ policies achieve high success rates on many tasks in the usual data regime even\
    \ with naive scaling. Next, we propose a training algorithm to jointly train policies\
    \ at multiple context lengths, further reducing the sample complexity of long-context\
    \ learning. Finally, we apply our findings to re-evaluate some previously proposed\
    \ solutions to long-context imitation learning."
  zh: "arXiv:2606.16447v2 Announce Type: replace \nAbstract: Imitation learning has\
    \ enabled highly-dexterous robotic manipulation from RGB observations. Policies\
    \ trained with these methods, however, typically condition robot actions on only\
    \ a short history of observations. These policies cannot solve tasks that require\
    \ memory and can get stuck repeatedly executing the same failing motions. In this\
    \ work, we first benchmark policy performance as context length is incrementally\
    \ increased from short to long, across a spectrum of tasks with varying local\
    \ stability and memory requirements, and in multiple data regimes. To our knowledge,\
    \ this is the first study to investigate context length for Diffusion Policies\
    \ at this level of detail. Our results challenge prior claims: naively scaling\
    \ context length is not as brittle as advertised in literature. With an appropriate\
    \ conditioning method and denoising backbone (UNet+Cross-Attention), single-task\
    \ policies achieve high success rates on many tasks in the usual data regime even\
    \ with naive scaling. Next, we propose a training algorithm to jointly train policies\
    \ at multiple context lengths, further reducing the sample complexity of long-context\
    \ learning. Finally, we apply our findings to re-evaluate some previously proposed\
    \ solutions to long-context imitation learning."
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
- training_and_evaluating_diffus
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-11'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: Training and Evaluating Diffusion Policies with Long Context Lengths (arXiv)
  url: https://arxiv.org/abs/2606.16447
  date: '2026'
  accessed_at: '2026-07-11'
---

arXiv:2606.16447v2 Announce Type: replace 
Abstract: Imitation learning has enabled highly-dexterous robotic manipulation from RGB observations. Policies trained with these methods, however, typically condition robot actions on only a short history of observations. These policies cannot solve tasks that require memory and can get stuck repeatedly executing the same failing motions. In this work, we first benchmark policy performance as context length is incrementally increased from short to long, across a spectrum of tasks with varying local stability and memory requirements, and in multiple data regimes. To our knowledge, this is the first study to investigate context length for Diffusion Policies at this level of detail. Our results challenge prior claims: naively scaling context length is not as brittle as advertised in literature. With an appropriate conditioning method and denoising backbone (UNet+Cross-Attention), single-task policies achieve high success rates on many tasks in the usual data regime even with naive scaling. Next, we propose a training algorithm to jointly train policies at multiple context lengths, further reducing the sample complexity of long-context learning. Finally, we apply our findings to re-evaluate some previously proposed solutions to long-context imitation learning.
