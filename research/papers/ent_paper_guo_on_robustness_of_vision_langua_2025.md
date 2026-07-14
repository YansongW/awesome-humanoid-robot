---
$id: ent_paper_guo_on_robustness_of_vision_langua_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations
  zh: RobustVLA
  ko: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations
summary:
  en: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations (RobustVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Tsinghua University, PKU-Psibot Lab,
    Beihang University, Peking University.
  zh: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations (RobustVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Tsinghua University, PKU-Psibot Lab,
    Beihang University, Peking University.
  ko: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations (RobustVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Tsinghua University, PKU-Psibot Lab,
    Beihang University, Peking University.
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
- robustvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.00037v4.
sources:
- id: src_001
  type: paper
  title: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations (arXiv)
  url: https://arxiv.org/abs/2510.00037
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RobustVLA source
  url: https://doi.org/10.48550/arXiv.2510.00037
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In Vision-Language-Actionf(VLA) models, robustness to real-world perturbations is critical for deployment. Existing methods target simple visual disturbances, overlooking the broader multi-modal perturbations that arise in actions, instructions, environments, and observations. Here, we first evaluate the robustness of mainstream VLAs under 17 perturbations across four modalities. We find (1) actions as the most fragile modality, (2) Existing visual-robust VLA do not gain robustness in other modality, and (3) pi0 demonstrates superior robustness. To build multi-modal robust VLAs, we propose RobustVLA against perturbations in VLA inputs and outputs. For output robustness, we perform offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective. This can be seen as adversarial training, label smoothing, and outlier penalization. For input robustness, we enforce consistent actions across input variations that preserve task semantics. To account for multiple perturbations, we formulate robustness as a multi-armed bandit problem and apply an upper confidence bound algorithm to automatically identify the most harmful noise. Experiments on LIBERO demonstrate our RobustVLA delivers absolute gains over baselines of 12.6% on the pi0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust BYOVLA that requires external LLMs, and a 10.4% gain under mixed perturbations. On the real-world FR5 robot, under four types of multimodal perturbations, RobustVLA shows strong low-data performance, outperforming pi0 by 65.6% success rate with 25 demonstrations. Even with abundant demos, our method still outperform pi0 by 30% success rate. Code and demo videos available at https://github.com/gakakulicc/RobustVLA.

## 核心内容
In Vision-Language-Actionf(VLA) models, robustness to real-world perturbations is critical for deployment. Existing methods target simple visual disturbances, overlooking the broader multi-modal perturbations that arise in actions, instructions, environments, and observations. Here, we first evaluate the robustness of mainstream VLAs under 17 perturbations across four modalities. We find (1) actions as the most fragile modality, (2) Existing visual-robust VLA do not gain robustness in other modality, and (3) pi0 demonstrates superior robustness. To build multi-modal robust VLAs, we propose RobustVLA against perturbations in VLA inputs and outputs. For output robustness, we perform offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective. This can be seen as adversarial training, label smoothing, and outlier penalization. For input robustness, we enforce consistent actions across input variations that preserve task semantics. To account for multiple perturbations, we formulate robustness as a multi-armed bandit problem and apply an upper confidence bound algorithm to automatically identify the most harmful noise. Experiments on LIBERO demonstrate our RobustVLA delivers absolute gains over baselines of 12.6% on the pi0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust BYOVLA that requires external LLMs, and a 10.4% gain under mixed perturbations. On the real-world FR5 robot, under four types of multimodal perturbations, RobustVLA shows strong low-data performance, outperforming pi0 by 65.6% success rate with 25 demonstrations. Even with abundant demos, our method still outperform pi0 by 30% success rate. Code and demo videos available at https://github.com/gakakulicc/RobustVLA.

## 参考
- http://arxiv.org/abs/2510.00037v4

