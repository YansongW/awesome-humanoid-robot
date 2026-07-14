---
$id: ent_paper_lv_f1_a_vision_language_action_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions'
  zh: F1
  ko: 'F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions'
summary:
  en: 'F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions (F1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Harbin Institute of Technology (Shenzhen).'
  zh: 'F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions (F1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Harbin Institute of Technology (Shenzhen).'
  ko: 'F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions (F1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Harbin Institute of Technology (Shenzhen).'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- f1
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.06951v2.
sources:
- id: src_001
  type: paper
  title: 'F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions (arXiv)'
  url: https://arxiv.org/abs/2509.06951
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: F1 source
  url: https://doi.org/10.48550/arXiv.2509.06951
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Executing language-conditioned tasks in dynamic visual environments remains a central challenge in embodied AI. Existing Vision-Language-Action (VLA) models predominantly adopt reactive state-to-action mappings, often leading to short-sighted behaviors and poor robustness in dynamic scenes. In this paper, we introduce F1, a pretrained VLA framework which integrates the visual foresight generation into decision-making pipeline. F1 adopts a Mixture-of-Transformer architecture with dedicated modules for perception, foresight generation, and control, thereby bridging understanding, generation, and actions. At its core, F1 employs a next-scale prediction mechanism to synthesize goal-conditioned visual foresight as explicit planning targets. By forecasting plausible future visual states, F1 reformulates action generation as a foresight-guided inverse dynamics problem, enabling actions that implicitly achieve visual goals. To endow F1 with robust and generalizable capabilities, we propose a three-stage training recipe on an extensive dataset comprising over 330k trajectories across 136 diverse tasks. This training scheme enhances modular reasoning and equips the model with transferable visual foresight, which is critical for complex and dynamic environments. Extensive evaluations on real-world tasks and simulation benchmarks demonstrate F1 consistently outperforms existing approaches, achieving substantial gains in both task success rate and generalization ability.

## 核心内容
Executing language-conditioned tasks in dynamic visual environments remains a central challenge in embodied AI. Existing Vision-Language-Action (VLA) models predominantly adopt reactive state-to-action mappings, often leading to short-sighted behaviors and poor robustness in dynamic scenes. In this paper, we introduce F1, a pretrained VLA framework which integrates the visual foresight generation into decision-making pipeline. F1 adopts a Mixture-of-Transformer architecture with dedicated modules for perception, foresight generation, and control, thereby bridging understanding, generation, and actions. At its core, F1 employs a next-scale prediction mechanism to synthesize goal-conditioned visual foresight as explicit planning targets. By forecasting plausible future visual states, F1 reformulates action generation as a foresight-guided inverse dynamics problem, enabling actions that implicitly achieve visual goals. To endow F1 with robust and generalizable capabilities, we propose a three-stage training recipe on an extensive dataset comprising over 330k trajectories across 136 diverse tasks. This training scheme enhances modular reasoning and equips the model with transferable visual foresight, which is critical for complex and dynamic environments. Extensive evaluations on real-world tasks and simulation benchmarks demonstrate F1 consistently outperforms existing approaches, achieving substantial gains in both task success rate and generalization ability.

## 参考
- http://arxiv.org/abs/2509.06951v2

