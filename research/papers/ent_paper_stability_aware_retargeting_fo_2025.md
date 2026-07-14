---
$id: ent_paper_stability_aware_retargeting_fo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation
  zh: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation
  ko: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation
summary:
  en: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation is a 2025 work on teleoperation for humanoid robots.
  zh: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation is a 2025 work on teleoperation for humanoid robots.
  ko: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation is a 2025 work on teleoperation for humanoid robots.
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
- stability_aware_retargeting_fo
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.04353v1.
sources:
- id: src_001
  type: paper
  title: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation (arXiv)
  url: https://arxiv.org/abs/2510.04353
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Teleoperation is a powerful method to generate reference motions and enable humanoid robots to perform a broad range of tasks. However, teleoperation becomes challenging when using hand contacts and non-coplanar surfaces, often leading to motor torque saturation or loss of stability through slipping. We propose a centroidal stability-based retargeting method that dynamically adjusts contact points and posture during teleoperation to enhance stability in these difficult scenarios. Central to our approach is an efficient analytical calculation of the stability margin gradient. This gradient is used to identify scenarios for which stability is highly sensitive to teleoperation setpoints and inform the local adjustment of these setpoints. We validate the framework in simulation and hardware by teleoperating manipulation tasks on a humanoid, demonstrating increased stability margins. We also demonstrate empirically that higher stability margins correlate with improved impulse resilience and joint torque margin.

## 核心内容
Teleoperation is a powerful method to generate reference motions and enable humanoid robots to perform a broad range of tasks. However, teleoperation becomes challenging when using hand contacts and non-coplanar surfaces, often leading to motor torque saturation or loss of stability through slipping. We propose a centroidal stability-based retargeting method that dynamically adjusts contact points and posture during teleoperation to enhance stability in these difficult scenarios. Central to our approach is an efficient analytical calculation of the stability margin gradient. This gradient is used to identify scenarios for which stability is highly sensitive to teleoperation setpoints and inform the local adjustment of these setpoints. We validate the framework in simulation and hardware by teleoperating manipulation tasks on a humanoid, demonstrating increased stability margins. We also demonstrate empirically that higher stability margins correlate with improved impulse resilience and joint torque margin.

## 参考
- http://arxiv.org/abs/2510.04353v1

