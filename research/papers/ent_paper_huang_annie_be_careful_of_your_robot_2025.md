---
$id: ent_paper_huang_annie_be_careful_of_your_robot_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ANNIE: Be Careful of Your Robots'
  zh: ANNIE
  ko: 'ANNIE: Be Careful of Your Robots'
summary:
  en: 'ANNIE: Be Careful of Your Robots (ANNIE), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by Institute of Automation, Chinese Academy of Sciences, Georgia Institute of Technology, University of Texas at Dallas,
    Institute of Computing Technology, Chinese Academy of Sciences.'
  zh: 'ANNIE: Be Careful of Your Robots (ANNIE), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by Institute of Automation, Chinese Academy of Sciences, Georgia Institute of Technology, University of Texas at Dallas,
    Institute of Computing Technology, Chinese Academy of Sciences.'
  ko: 'ANNIE: Be Careful of Your Robots (ANNIE), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by Institute of Automation, Chinese Academy of Sciences, Georgia Institute of Technology, University of Texas at Dallas,
    Institute of Computing Technology, Chinese Academy of Sciences.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- annie
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.03383v1.
sources:
- id: src_001
  type: paper
  title: 'ANNIE: Be Careful of Your Robots (arXiv)'
  url: https://arxiv.org/abs/2509.03383
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ANNIE source
  url: https://doi.org/10.48550/arXiv.2509.03383
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The integration of vision-language-action (VLA) models into embodied AI (EAI) robots is rapidly advancing their ability to perform complex, long-horizon tasks in humancentric environments. However, EAI systems introduce critical security risks: a compromised VLA model can directly translate adversarial perturbations on sensory input into unsafe physical actions. Traditional safety definitions and methodologies from the machine learning community are no longer sufficient. EAI systems raise new questions, such as what constitutes safety, how to measure it, and how to design effective attack and defense mechanisms in physically grounded, interactive settings. In this work, we present the first systematic study of adversarial safety attacks on embodied AI systems, grounded in ISO standards for human-robot interactions. We (1) formalize a principled taxonomy of safety violations (critical, dangerous, risky) based on physical constraints such as separation distance, velocity, and collision boundaries; (2) introduce ANNIEBench, a benchmark of nine safety-critical scenarios with 2,400 video-action sequences for evaluating embodied safety; and (3) ANNIE-Attack, a task-aware adversarial framework with an attack leader model that decomposes long-horizon goals into frame-level perturbations. Our evaluation across representative EAI models shows attack success rates exceeding 50% across all safety categories. We further demonstrate sparse and adaptive attack strategies and validate the real-world impact through physical robot experiments. These results expose a previously underexplored but highly consequential attack surface in embodied AI systems, highlighting the urgent need for security-driven defenses in the physical AI era. Code is available at https://github.com/RLCLab/Annie.

## 核心内容
The integration of vision-language-action (VLA) models into embodied AI (EAI) robots is rapidly advancing their ability to perform complex, long-horizon tasks in humancentric environments. However, EAI systems introduce critical security risks: a compromised VLA model can directly translate adversarial perturbations on sensory input into unsafe physical actions. Traditional safety definitions and methodologies from the machine learning community are no longer sufficient. EAI systems raise new questions, such as what constitutes safety, how to measure it, and how to design effective attack and defense mechanisms in physically grounded, interactive settings. In this work, we present the first systematic study of adversarial safety attacks on embodied AI systems, grounded in ISO standards for human-robot interactions. We (1) formalize a principled taxonomy of safety violations (critical, dangerous, risky) based on physical constraints such as separation distance, velocity, and collision boundaries; (2) introduce ANNIEBench, a benchmark of nine safety-critical scenarios with 2,400 video-action sequences for evaluating embodied safety; and (3) ANNIE-Attack, a task-aware adversarial framework with an attack leader model that decomposes long-horizon goals into frame-level perturbations. Our evaluation across representative EAI models shows attack success rates exceeding 50% across all safety categories. We further demonstrate sparse and adaptive attack strategies and validate the real-world impact through physical robot experiments. These results expose a previously underexplored but highly consequential attack surface in embodied AI systems, highlighting the urgent need for security-driven defenses in the physical AI era. Code is available at https://github.com/RLCLab/Annie.

## 参考
- http://arxiv.org/abs/2509.03383v1

