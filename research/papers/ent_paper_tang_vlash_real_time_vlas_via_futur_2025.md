---
$id: ent_paper_tang_vlash_real_time_vlas_via_futur_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference'
  zh: VLASH
  ko: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference'
summary:
  en: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference (VLASH), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT.'
  zh: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference (VLASH), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT.'
  ko: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference (VLASH), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT.'
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
- vision_language_action
- vla
- vlash
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.01031v1.
sources:
- id: src_001
  type: paper
  title: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference (arXiv)'
  url: https://arxiv.org/abs/2512.01031
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLASH source
  url: https://doi.org/10.48550/arXiv.2512.01031
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action models (VLAs) are becoming increasingly capable across diverse robotic tasks. However, their real-world deployment remains slow and inefficient: demonstration videos are often sped up by 5-10x to appear smooth, with noticeable action stalls and delayed reactions to environmental changes. Asynchronous inference offers a promising solution to achieve continuous and low-latency control by enabling robots to execute actions and perform inference simultaneously. However, because the robot and environment continue to evolve during inference, a temporal misalignment arises between the prediction and execution intervals. This leads to significant action instability, while existing methods either degrade accuracy or introduce runtime overhead to mitigate it. We propose VLASH, a general asynchronous inference framework for VLAs that delivers smooth, accurate, and fast reaction control without additional overhead or architectural changes. VLASH estimates the future execution-time state by rolling the robot state forward with the previously generated action chunk, thereby bridging the gap between prediction and execution. Experiments show that VLASH achieves up to 2.03x speedup and reduces reaction latency by up to 17.4x compared to synchronous inference while fully preserving the original accuracy. Moreover, it empowers VLAs to handle fast-reaction, high-precision tasks such as playing ping-pong and playing whack-a-mole, where traditional synchronous inference fails. Code is available at https://github.com/mit-han-lab/vlash

## 核心内容
Vision-Language-Action models (VLAs) are becoming increasingly capable across diverse robotic tasks. However, their real-world deployment remains slow and inefficient: demonstration videos are often sped up by 5-10x to appear smooth, with noticeable action stalls and delayed reactions to environmental changes. Asynchronous inference offers a promising solution to achieve continuous and low-latency control by enabling robots to execute actions and perform inference simultaneously. However, because the robot and environment continue to evolve during inference, a temporal misalignment arises between the prediction and execution intervals. This leads to significant action instability, while existing methods either degrade accuracy or introduce runtime overhead to mitigate it. We propose VLASH, a general asynchronous inference framework for VLAs that delivers smooth, accurate, and fast reaction control without additional overhead or architectural changes. VLASH estimates the future execution-time state by rolling the robot state forward with the previously generated action chunk, thereby bridging the gap between prediction and execution. Experiments show that VLASH achieves up to 2.03x speedup and reduces reaction latency by up to 17.4x compared to synchronous inference while fully preserving the original accuracy. Moreover, it empowers VLAs to handle fast-reaction, high-precision tasks such as playing ping-pong and playing whack-a-mole, where traditional synchronous inference fails. Code is available at https://github.com/mit-han-lab/vlash

## 参考
- http://arxiv.org/abs/2512.01031v1

