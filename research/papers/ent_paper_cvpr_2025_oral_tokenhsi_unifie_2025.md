---
$id: ent_paper_cvpr_2025_oral_tokenhsi_unifie_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization'
  zh: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization'
  ko: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization'
summary:
  en: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization is a 2025
    work on physics-based character animation for humanoid robots.'
  zh: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization is a 2025
    work on physics-based character animation for humanoid robots.'
  ko: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization is a 2025
    work on physics-based character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- cvpr_2025_oral_tokenhsi
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.19901v2.
sources:
- id: src_001
  type: paper
  title: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization (arXiv)'
  url: https://arxiv.org/abs/2503.19901
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization project
    page'
  url: https://liangpan99.github.io/TokenHSI/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Synthesizing diverse and physically plausible Human-Scene Interactions (HSI) is pivotal for both computer animation and embodied AI. Despite encouraging progress, current methods mainly focus on developing separate controllers, each specialized for a specific interaction task. This significantly hinders the ability to tackle a wide variety of challenging HSI tasks that require the integration of multiple skills, e.g., sitting down while carrying an object. To address this issue, we present TokenHSI, a single, unified transformer-based policy capable of multi-skill unification and flexible adaptation. The key insight is to model the humanoid proprioception as a separate shared token and combine it with distinct task tokens via a masking mechanism. Such a unified policy enables effective knowledge sharing across skills, thereby facilitating the multi-task training. Moreover, our policy architecture supports variable length inputs, enabling flexible adaptation of learned skills to new scenarios. By training additional task tokenizers, we can not only modify the geometries of interaction targets but also coordinate multiple skills to address complex tasks. The experiments demonstrate that our approach can significantly improve versatility, adaptability, and extensibility in various HSI tasks. Website: https://liangpan99.github.io/TokenHSI/

## 核心内容
Synthesizing diverse and physically plausible Human-Scene Interactions (HSI) is pivotal for both computer animation and embodied AI. Despite encouraging progress, current methods mainly focus on developing separate controllers, each specialized for a specific interaction task. This significantly hinders the ability to tackle a wide variety of challenging HSI tasks that require the integration of multiple skills, e.g., sitting down while carrying an object. To address this issue, we present TokenHSI, a single, unified transformer-based policy capable of multi-skill unification and flexible adaptation. The key insight is to model the humanoid proprioception as a separate shared token and combine it with distinct task tokens via a masking mechanism. Such a unified policy enables effective knowledge sharing across skills, thereby facilitating the multi-task training. Moreover, our policy architecture supports variable length inputs, enabling flexible adaptation of learned skills to new scenarios. By training additional task tokenizers, we can not only modify the geometries of interaction targets but also coordinate multiple skills to address complex tasks. The experiments demonstrate that our approach can significantly improve versatility, adaptability, and extensibility in various HSI tasks. Website: https://liangpan99.github.io/TokenHSI/

## 参考
- http://arxiv.org/abs/2503.19901v2

