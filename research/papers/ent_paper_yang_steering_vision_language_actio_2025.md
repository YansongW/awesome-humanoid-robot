---
$id: ent_paper_yang_steering_vision_language_actio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach'
  zh: TACO
  ko: 'Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach'
summary:
  en: 'Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach (TACO), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Artificial Intelligence, China Telecom, University of Science
    and Technology of China, Tsinghua University, The Hong Kong University of Science and Technology.'
  zh: 'Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach (TACO), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Artificial Intelligence, China Telecom, University of Science
    and Technology of China, Tsinghua University, The Hong Kong University of Science and Technology.'
  ko: 'Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach (TACO), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Artificial Intelligence, China Telecom, University of Science
    and Technology of China, Tsinghua University, The Hong Kong University of Science and Technology.'
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
- taco
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.05171v2.
sources:
- id: src_001
  type: paper
  title: 'Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach (arXiv)'
  url: https://arxiv.org/abs/2502.05171
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TACO source
  url: https://doi.org/10.48550/arXiv.2502.05171
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We study a novel language model architecture that is capable of scaling test-time computation by implicitly reasoning in latent space. Our model works by iterating a recurrent block, thereby unrolling to arbitrary depth at test-time. This stands in contrast to mainstream reasoning models that scale up compute by producing more tokens. Unlike approaches based on chain-of-thought, our approach does not require any specialized training data, can work with small context windows, and can capture types of reasoning that are not easily represented in words. We scale a proof-of-concept model to 3.5 billion parameters and 800 billion tokens. We show that the resulting model can improve its performance on reasoning benchmarks, sometimes dramatically, up to a computation load equivalent to 50 billion parameters.

## 核心内容
We study a novel language model architecture that is capable of scaling test-time computation by implicitly reasoning in latent space. Our model works by iterating a recurrent block, thereby unrolling to arbitrary depth at test-time. This stands in contrast to mainstream reasoning models that scale up compute by producing more tokens. Unlike approaches based on chain-of-thought, our approach does not require any specialized training data, can work with small context windows, and can capture types of reasoning that are not easily represented in words. We scale a proof-of-concept model to 3.5 billion parameters and 800 billion tokens. We show that the resulting model can improve its performance on reasoning benchmarks, sometimes dramatically, up to a computation load equivalent to 50 billion parameters.

## 参考
- http://arxiv.org/abs/2502.05171v2

