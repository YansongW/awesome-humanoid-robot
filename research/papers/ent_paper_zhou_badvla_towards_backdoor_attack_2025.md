---
$id: ent_paper_zhou_badvla_towards_backdoor_attack_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization'
  zh: BadVLA
  ko: 'BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization'
summary:
  en: 'BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization (BadVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    Lehigh University, and published at NIPS25.'
  zh: 'BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization (BadVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    Lehigh University, and published at NIPS25.'
  ko: 'BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization (BadVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Huazhong University of Science and Technology,
    Lehigh University, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- badvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.16640v1.
sources:
- id: src_001
  type: paper
  title: 'BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization (arXiv)'
  url: https://arxiv.org/abs/2505.16640
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: BadVLA source
  url: https://doi.org/10.48550/arXiv.2505.16640
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have advanced robotic control by enabling end-to-end decision-making directly from multimodal inputs. However, their tightly coupled architectures expose novel security vulnerabilities. Unlike traditional adversarial perturbations, backdoor attacks represent a stealthier, persistent, and practically significant threat-particularly under the emerging Training-as-a-Service paradigm-but remain largely unexplored in the context of VLA models. To address this gap, we propose BadVLA, a backdoor attack method based on Objective-Decoupled Optimization, which for the first time exposes the backdoor vulnerabilities of VLA models. Specifically, it consists of a two-stage process: (1) explicit feature-space separation to isolate trigger representations from benign inputs, and (2) conditional control deviations that activate only in the presence of the trigger, while preserving clean-task performance. Empirical results on multiple VLA benchmarks demonstrate that BadVLA consistently achieves near-100% attack success rates with minimal impact on clean task accuracy. Further analyses confirm its robustness against common input perturbations, task transfers, and model fine-tuning, underscoring critical security vulnerabilities in current VLA deployments. Our work offers the first systematic investigation of backdoor vulnerabilities in VLA models, highlighting an urgent need for secure and trustworthy embodied model design practices. We have released the project page at https://badvla-project.github.io/.

## 核心内容
Vision-Language-Action (VLA) models have advanced robotic control by enabling end-to-end decision-making directly from multimodal inputs. However, their tightly coupled architectures expose novel security vulnerabilities. Unlike traditional adversarial perturbations, backdoor attacks represent a stealthier, persistent, and practically significant threat-particularly under the emerging Training-as-a-Service paradigm-but remain largely unexplored in the context of VLA models. To address this gap, we propose BadVLA, a backdoor attack method based on Objective-Decoupled Optimization, which for the first time exposes the backdoor vulnerabilities of VLA models. Specifically, it consists of a two-stage process: (1) explicit feature-space separation to isolate trigger representations from benign inputs, and (2) conditional control deviations that activate only in the presence of the trigger, while preserving clean-task performance. Empirical results on multiple VLA benchmarks demonstrate that BadVLA consistently achieves near-100% attack success rates with minimal impact on clean task accuracy. Further analyses confirm its robustness against common input perturbations, task transfers, and model fine-tuning, underscoring critical security vulnerabilities in current VLA deployments. Our work offers the first systematic investigation of backdoor vulnerabilities in VLA models, highlighting an urgent need for secure and trustworthy embodied model design practices. We have released the project page at https://badvla-project.github.io/.

## 参考
- http://arxiv.org/abs/2505.16640v1

