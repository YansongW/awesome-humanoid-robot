---
$id: ent_paper_chen_fast_in_slow_a_dual_system_vla_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning'
  zh: Fast-in-Slow
  ko: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning'
summary:
  en: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning (Fast-in-Slow), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The Chinese University of Hong Kong, State Key Laboratory
    of Multimedia Information Processing, School of Computer Science, Peking University, AI2Robotics, Beijing Academy of Artificial
    Intelligence (BAAI), and published at NIPS25.'
  zh: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning (Fast-in-Slow), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The Chinese University of Hong Kong, State Key Laboratory
    of Multimedia Information Processing, School of Computer Science, Peking University, AI2Robotics, Beijing Academy of Artificial
    Intelligence (BAAI), and published at NIPS25.'
  ko: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning (Fast-in-Slow), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The Chinese University of Hong Kong, State Key Laboratory
    of Multimedia Information Processing, School of Computer Science, Peking University, AI2Robotics, Beijing Academy of Artificial
    Intelligence (BAAI), and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fast_in_slow
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01953v1.
sources:
- id: src_001
  type: paper
  title: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning (arXiv)'
  url: https://arxiv.org/abs/2506.01953
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Generalized policy and execution efficiency constitute the two critical challenges in robotic manipulation. While recent foundation policies benefit from the common-sense reasoning capabilities of internet-scale pretrained vision-language models (VLMs), they often suffer from low execution frequency. To mitigate this dilemma, dual-system approaches, inspired by Kahneman's theory, have been proposed to leverage a VLM-based System 2 model handling high-level reasoning and a separate System 1 action model ensuring real-time control. However, existing designs maintain both systems as separate models, limiting System 1 from fully leveraging the rich pretrained knowledge from the VLM-based System 2. In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 by partially sharing parameters. This innovative paradigm not only enables high-frequency execution in System 1 but also facilitates coordination between the reasoning and execution components within a single foundation model of System 2. Given their fundamentally distinct roles within FiS-VLA, we design the two systems to incorporate heterogeneous modality inputs alongside asynchronous operating frequencies, enabling both fast and precise manipulation. To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2's contextual reasoning representation. For evaluation, FiS-VLA outperforms previous state-of-the-art methods by 8% in simulation and 11% in real-world tasks in terms of average success rate, while achieving a 117.7 Hz control frequency with action chunk set to eight. Project web page: fast-in-slow.github.io.

## 核心内容
Generalized policy and execution efficiency constitute the two critical challenges in robotic manipulation. While recent foundation policies benefit from the common-sense reasoning capabilities of internet-scale pretrained vision-language models (VLMs), they often suffer from low execution frequency. To mitigate this dilemma, dual-system approaches, inspired by Kahneman's theory, have been proposed to leverage a VLM-based System 2 model handling high-level reasoning and a separate System 1 action model ensuring real-time control. However, existing designs maintain both systems as separate models, limiting System 1 from fully leveraging the rich pretrained knowledge from the VLM-based System 2. In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 by partially sharing parameters. This innovative paradigm not only enables high-frequency execution in System 1 but also facilitates coordination between the reasoning and execution components within a single foundation model of System 2. Given their fundamentally distinct roles within FiS-VLA, we design the two systems to incorporate heterogeneous modality inputs alongside asynchronous operating frequencies, enabling both fast and precise manipulation. To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2's contextual reasoning representation. For evaluation, FiS-VLA outperforms previous state-of-the-art methods by 8% in simulation and 11% in real-world tasks in terms of average success rate, while achieving a 117.7 Hz control frequency with action chunk set to eight. Project web page: fast-in-slow.github.io.

## 参考
- http://arxiv.org/abs/2506.01953v1

